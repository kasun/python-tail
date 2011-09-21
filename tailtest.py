#!/usr/bin/env python

#
# Author - Kasun Herath <kasunh01 at gmail.com>
#
# Test cases for python-tail
#

import unittest

import tail

class TailTests(unittest.TestCase):
    def testInvalidFilePrint(self):
        #self.assertRaises(tail.TailError, 'Invalid file name', tail.Tail, '#$%#$%^.py')
        self.assertRaises(tail.TailError, tail.Tail, '#$%#$%^.py')
    def testDirectoryPrint(self):
        self.assertRaises(tail.TailError, tail.Tail, 'testfiles')
    def testDefaultNoOfPrintLines(self):
        tail_file = tail.Tail('testfiles/testfile.py')
        output = tail_file.print_tail()[1]
        lines = output.split('\n')
        self.assertEqual(len(lines), 10)
    def testNoOfPrintLines(self):
        tail_file = tail.Tail('testfiles/testfile.py')
        output = tail_file.print_tail(n=5)[1]
        lines = output.split('\n')
        self.assertEqual(len(lines), 5)

if __name__ == '__main__':
    unittest.main()
