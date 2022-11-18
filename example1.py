#!/usr/bin/env python

''' 
python-tail example.
Does a tail follow against /var/log/syslog with a time interval of 5 seconds.
Prints recieved new lines to standard out '''

import tail

FILE_PATH = "./follow_test.txt"

def print_line(txt):
    ''' Prints received text '''
    print(txt)


if __name__ == "__main__":
    t = tail.Tail(FILE_PATH)
    t.register_callback(print_line)
    t.follow(s=5)


