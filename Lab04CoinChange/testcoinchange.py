"""
|-------------------------------------------------------------------------------
| testcoinchange.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 11, 2019
|
| This is the PyUnit test bench for coinchange.py
| Do not alter the contents of this file.
|
"""

from coinchange import *
import unittest

class TestCoinChange(unittest.TestCase):
    def testone(self):
        expected = 4
        actual = minimumcoins(41)
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = 1
        actual = minimumcoins(1)
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = 2
        actual = minimumcoins(15)
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = 7
        actual = minimumcoins(160)
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = 92
        actual = minimumcoins(2300)
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = 18
        actual = minimumcoins(420)
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = 238
        actual = minimumcoins(5926)
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = 320
        actual = minimumcoins(7932)
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = 422
        actual = minimumcoins(10454)
        self.assertEqual(expected, actual)

    def testten(self):
        expected = 926
        actual = minimumcoins(23078)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
