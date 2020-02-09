"""
|-------------------------------------------------------------------------------
| testdownpayment.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 18, 2019
|
| This is the PyUnit test bench for downpayment.py
| Do not alter the contents of this file.
|
"""

from downpayment import *
import unittest

class TestDownPayment(unittest.TestCase):
    def testone(self):
        expected = 142
        actual = savingsduration(120000, 0.05, 500000, 0.03)
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = 159
        actual = savingsduration(80000, 0.1, 800000, 0.03)
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = 261
        actual = savingsduration(75000, 0.05, 1500000, 0.05)
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = 114
        actual = savingsduration(108145, 0.0315, 287267, 0.067)
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = 334
        actual = savingsduration(134816, 0.098, 6304070, 0.033)
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = 219
        actual = savingsduration(191146, 0.0105, 1134510, 0.087)
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = 131
        actual = savingsduration(588363, 0.058, 3563630, 0.063)
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = 282
        actual = savingsduration(69000, 0.066, 7902030, 0.093)
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = 231
        actual = savingsduration(26675, 0.0492, 470659, 0.0591)
        self.assertEqual(expected, actual)

    def testten(self):
        expected = 474
        actual = savingsduration(949108, 0.0322, 31262058, 0.0278)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
