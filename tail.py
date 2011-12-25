#!/usr/bin/env python

'''
Python-Tail - Unix tail implementation in Python <https://github.com/kasun/python-tail>
Author - Kasun Herath <kasunh01 at gmail.com>
'''

import os

class Tail:
    ''' Represent a tail command '''
    def __init__(self, file_):
        ''' Initiate a Tail instance '''
        self.tail_file = file_

    def follow(self):
        if not self.callback:
            raise TailError('No callback function registered')

    def register_callback(self, func):
        self.callback = func

    def check_file_validity(self, file_):
        if not os.access(file_, os.F_OK):
            raise TailError("File '%s' does not exist" % (file_))
        if not os.access(file_, os.R_OK):
            raise TailError("File '%s' not readable" % (file_))
        if os.path.isdir(file_):
            raise TailError("File '%s' is a directory" % (file_))

class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
