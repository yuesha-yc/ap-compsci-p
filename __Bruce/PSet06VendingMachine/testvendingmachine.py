"""
|-------------------------------------------------------------------------------
| testvendingmachine.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 15, 2019
|
| This is the PyUnit test bench for vendingmachine.py
| Do not alter the contents of this file.
|
"""

from vendingmachine import *
import unittest

class TestVendingMachine(unittest.TestCase):
    def testone(self):
        expected = 3
        actual = dispensechange(5, 5, 5, 160, 200)
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = 15
        actual = dispensechange(20, 0, 0, 125, 500)
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = 9
        actual = dispensechange(0, 10, 0, 210, 300)
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = 58
        actual = dispensechange(0, 0, 60, 235, 525)
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = 17
        actual = dispensechange(6, 5, 10, 195, 425)
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = 72
        actual = dispensechange(10, 20, 50, 235, 895)
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = 54
        actual = dispensechange(19, 82, 23, 675, 1495)
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = 113
        actual = dispensechange(12, 100, 1, 1855, 3160)
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = 182
        actual = dispensechange(100, 1, 83, 2870, 5785)
        self.assertEqual(expected, actual)

    def testten(self):
        expected = 362
        actual = dispensechange(2, 287, 157, 5285, 8570)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
