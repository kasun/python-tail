#!/usr/bin/env python

'''
Python-Tail - Unix tail follow implementation in Python. 

python-tail can be used to monitor changes to a file.

Example:
    import tail

    # Create a tail instance
    t = tail.Tail('file-to-be-followed')

    # Register a callback function to be called when a new line is found in the followed file. 
    # If no callback function is registerd, new lines would be printed to standard out.
    t.register_callback(callback_function)

    # Follow the file with 5 seconds as sleep time between iterations. 
    # If sleep time is not provided 1 second is used as the default time.
    t.follow(s=5) '''

# Author - Kasun Herath <kasunh01 at gmail.com>
# Source - https://github.com/kasun/python-tail

import os
import sys
import time
from cStringIO import StringIO

class Tail(object):
    ''' Represents a tail command. '''
    def __init__(self, tailed_file, max_line_length=float("inf")):
        ''' Initiate a Tail instance.
            Check for file validity, assigns callback function to standard out.
            
            Arguments:
                tailed_file - File to be followed. '''

        self.check_file_validity(tailed_file)
        self.tailed_file = tailed_file
        self.callback = sys.stdout.write
        self.max_line_length=max_line_length

    def follow(self, s=1, poll_time=.01):
        ''' Do a tail follow. If a callback function is registered it is called with every new line. 
        Else printed to standard out.
    
        Arguments:
            s - Number of seconds to wait between each iteration; Defaults to 1. '''
        readBuffer = StringIO()
        with open(self.tailed_file, 'rb') as file_:
            file_.seek(0, os.SEEK_END)
            while True:
                readBuffer.write(file_.read())
                readBuffer.seek(0)
                complete = True
                for line in readBuffer:
                    if not line.endswith(os.linesep): 
                        complete = False
                        break

                    self.callback(line)
                    time.sleep(s)

                # Catch the slop if the last line isn't complete
                readBuffer.truncate(0)
                if not complete:
                    if len(line) > self.max_line_length:
                        raise TailError("Line exceeds maximum allowed line length")

                    readBuffer.write(line)
                
                time.sleep(poll_time)

    def register_callback(self, func):
        ''' Overrides default callback function to provided function. '''
        self.callback = func

    def check_file_validity(self, file_):
        ''' Check whether the a given file exists, readable and is a file '''
        if not os.access(file_, os.F_OK):
            raise TailError("File '%s' does not exist" % (file_))
        if not os.access(file_, os.R_OK):
            raise TailError("File '%s' not readable" % (file_))
        if os.path.isdir(file_):
            raise TailError("File '%s' is a directory" % (file_))

class TailError(IOError):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python tail.py <filename>"
        sys.exit(1)

    tail = Tail(sys.argv[1])
    tail.follow(0)

