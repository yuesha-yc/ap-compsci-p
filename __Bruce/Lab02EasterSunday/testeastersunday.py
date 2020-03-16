"""
|-------------------------------------------------------------------------------
| testeastersunday.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Sep 10, 2019
|
| This program is the PyUnit test bench for eastersunday.py
| Do not alter the contents of this file.
|
"""

from eastersunday import *
import unittest

class TestEaster(unittest.TestCase):
    def testone(self):
        expected = (4, 15)
        actual = retrievedate(2001)
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = (4, 4)
        actual = retrievedate(2010)
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = (4, 9)
        actual = retrievedate(1950)
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = (4, 7)
        actual = retrievedate(1996)
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = (4, 20)
        actual = retrievedate(1919)
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = (4, 3)
        actual = retrievedate(1988)
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = (4, 22)
        actual = retrievedate(1973)
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = (4, 6)
        actual = retrievedate(1958)
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = (4, 16)
        actual = retrievedate(1911)
        self.assertEqual(expected, actual)

    def testten(self):
        expected = (3, 31)
        actual = retrievedate(1907)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
