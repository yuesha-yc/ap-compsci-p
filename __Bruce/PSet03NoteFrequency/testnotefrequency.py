"""
|-------------------------------------------------------------------------------
| testnotefrequency.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Sep 15, 2019
|
| This is the PyUnit test bench for notefrequency.py
| Do not alter the contents of this file.
|
"""

from notefrequency import *
import unittest

class TestNoteFrequency(unittest.TestCase):
    def testone(self):
        expected = 16.35
        actual = temperedscale(0, 0)
        self.assertAlmostEqual(expected, actual, 2)

    def testtwo(self):
        expected = 16744.036
        actual = temperedscale(10, 0)
        self.assertAlmostEqual(expected, actual, 2)

    def testthree(self):
        expected = 440.00
        actual = temperedscale(4, 9)
        self.assertAlmostEqual(expected, actual, 2)

    def testfour(self):
        expected = 50175.415
        actual = temperedscale(11, 7)
        self.assertAlmostEqual(expected, actual, 2)

    def testfive(self):
        expected = 116.54
        actual = temperedscale(2, 10)
        self.assertAlmostEqual(expected, actual, 2)

    def testsix(self):
        expected = 830.609
        actual = temperedscale(5, 8)
        self.assertAlmostEqual(expected, actual, 2)

    def testseven(self):
        expected = 369.99
        actual = temperedscale(4, 6)
        self.assertAlmostEqual(expected, actual, 2)

    def testeight(self):
        expected = 2217.46
        actual = temperedscale(7, 1)
        self.assertAlmostEqual(expected, actual, 2)

    def testnine(self):
        expected = 9956.063
        actual = temperedscale(9, 3)
        self.assertAlmostEqual(expected, actual, 2)

    def testten(self):
        expected = 100350.83
        actual = temperedscale(12, 7)
        self.assertAlmostEqual(expected, actual, 2)

if __name__ == '__main__':
    unittest.main()
