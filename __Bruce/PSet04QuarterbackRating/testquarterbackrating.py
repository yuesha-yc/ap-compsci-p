"""
|-------------------------------------------------------------------------------
| testquarterbackrating.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Sep 22, 2019
|
| This is the PyUnit test bench for quarterbackrating.py
| Do not alter the contents of this file.
|
"""

from quarterbackrating import *
import unittest

class TestQuarterbackRating(unittest.TestCase):
    def testone(self):
        expected = 99.107
        actual = calculaterating(35, 26, 235, 2, 1)
        self.assertAlmostEqual(expected, actual, 2)

    def testtwo(self):
        expected = 158.333
        actual = calculaterating(33, 26, 465, 5, 0)
        self.assertAlmostEqual(expected, actual, 2)

    def testthree(self):
        expected = 108.534
        actual = calculaterating(62, 40, 464, 4, 0)
        self.assertAlmostEqual(expected, actual, 2)

    def testfour(self):
        expected = 92.385
        actual = calculaterating(58, 35, 437, 4, 2)
        self.assertAlmostEqual(expected, actual, 2)

    def testfive(self):
        expected = 117.250
        actual = calculaterating(50, 36, 422, 3, 0)
        self.assertAlmostEqual(expected, actual, 2)

    def testsix(self):
        expected = 90.544
        actual = calculaterating(26, 19, 172, 0, 0)
        self.assertAlmostEqual(expected, actual, 2)

    def testseven(self):
        expected = 74.019
        actual = calculaterating(34, 17, 167, 1, 0)
        self.assertAlmostEqual(expected, actual, 2)

    def testeight(self):
        expected = 36.300
        actual = calculaterating(33, 16, 151, 0, 2)
        self.assertAlmostEqual(expected, actual, 2)

    def testnine(self):
        expected = 73.958
        actual = calculaterating(20, 16, 145, 1, 2)
        self.assertAlmostEqual(expected, actual, 2)

    def testten(self):
        expected = 49.768
        actual = calculaterating(18, 9, 126, 0, 1)
        self.assertAlmostEqual(expected, actual, 2)

if __name__ == '__main__':
    unittest.main()



