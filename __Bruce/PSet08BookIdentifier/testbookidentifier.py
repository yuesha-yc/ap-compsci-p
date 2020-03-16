"""
|-------------------------------------------------------------------------------
| testbookidentifier.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 28, 2019
|
| This is the PyUnit test bench for bookidentifier.py
|
"""

from bookidentifier import *
import unittest

class TestBookIdentifier(unittest.TestCase):
    def testone(self):
        expected = "YES"
        actual = validatebook("0789751984")
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = "YES"
        actual = validatebook("0321776410")
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = "YES"
        actual = validatebook("0321842685")
        self.assertEqual(expected, actual)

    def testtfour(self):
        expected = "YES"
        actual = validatebook("0439708184")
        self.assertEqual(expected, actual)

    def testtfive(self):
        expected = "YES"
        actual = validatebook("0553593714")
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = "NO"
        actual = validatebook("0789751985")
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = "NO"
        actual = validatebook("5558675309")
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = "NO"
        actual = validatebook("6178675309")
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = "NO"
        actual = validatebook("2128535937")
        self.assertEqual(expected, actual)

    def testten(self):
        expected = "NO"
        actual = validatebook("4168426060")
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

