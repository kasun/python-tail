#!/usr/bin/env python

'''
Author - Kasun Herath <kasunh01 at gmail.com>
'''

class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
