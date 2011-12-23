#!/usr/bin/env python

#
# Python-Tail - Unix tail implementation in Python <https://github.com/kasun/python-tail>
# Author - Kasun Herath <kasunh01 at gmail.com>
#

import os

class Tail:
    ''' Represent a tail command '''
    def __init__(self, *args):
        ''' Initiate a Tail instance and add files to be tracked if provided '''
        self.files = []
        tmp_filelist = []
        for file_ in args:
            self.check_file_validity(file_)
            tmp_filelist.append(file_)
        self.files.extend(list(set(tmp_filelist)))

    def add_files(self, *args):
        ''' Add files to be tracked '''
        tmp_filelist = []
        for file_ in [file_ for file_ in args if file_ not in self.files]:
            self.check_file_validity(file_)
            tmp_filelist.append(file_)
        self.files.extend(list(set(tmp_filelist)))

    def print_tail(self, *args, **kargs):
        if 'f' in args:
            self.print_follow(list(args).remove('f'))

    def print_follow(self):
        if not self.callback:
            raise TailError('Follow option passed without registering a callback function')

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
