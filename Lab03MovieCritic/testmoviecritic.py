"""
|-------------------------------------------------------------------------------
| testmoviecritic.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Sep 19, 2019
|
| This is the PyUnit test bench for moviecritic.py
| Do not alter the contents of this file.
|
"""

from moviecritic import *
import unittest

class TestAttendMovie(unittest.TestCase):
    def testcaseone(self):
        expected = "extremely interested"
        actual = selectfilm(3.50, 3)
        self.assertEqual(expected, actual)
    
    def testcasetwo(self):
        expected = "barely interested"
        actual = selectfilm(15.50, 5)
        self.assertEqual(expected, actual)

    def testcasethree(self):
        expected = "very interested"
        actual = selectfilm(10.50, 4.5)
        self.assertEqual(expected, actual)

    def testcasefour(self):
        expected = "moderately interested"
        actual = selectfilm(7.50, 2.5)
        self.assertEqual(expected, actual)

    def testcasefive(self):
        expected = "barely interested"
        actual = selectfilm(2.50, 1.5)
        self.assertEqual(expected, actual)

    def testcasesix(self):
        expected = "completely uninterested"
        actual = selectfilm(25.50, 0.5)
        self.assertEqual(expected, actual)

    def testcaseseven(self):
        expected = "moderately interested"
        actual = selectfilm(5.00, 2)
        self.assertEqual(expected, actual)
        
    def testcaseeight(self):
        expected = "moderately interested"
        actual = selectfilm(11.99, 4)
        self.assertEqual(expected, actual)

    def testcasenine(self):
        expected = "barely interested"
        actual = selectfilm(4.99, 1.9)
        self.assertEqual(expected, actual)

    def testcaseten(self):
        expected = "extremely interested"
        actual = selectfilm(4.99, 2)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

