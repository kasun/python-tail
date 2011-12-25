#!/usr/bin/env python

''' python-tail example.
Does a tail follow to /var/log/syslog with a time interval of 5 seconds.
Prints recieved new lines standard out'''

import tail

def print_line(txt):
    ''' Prints received text '''
    print(txt)

t = tail.Tail('/var/log/syslog')
t.register_callback(print_line)
t.follow(5)


