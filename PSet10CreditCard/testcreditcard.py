"""
|-------------------------------------------------------------------------------
| testcreditcard.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 17, 2019
|
| This is the PyUnit test bench for creditcard.py
| Do not alter the contents of this file.
|
"""

from creditcard import *
import unittest

class TestCreditCard(unittest.TestCase):
    def testone(self):
        expected = "AMEX"
        actual = validate("348605027629226")
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = "AMEX"
        actual = validate("378282246310005")
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = "MASTERCARD"
        actual = validate("5105105105105100")
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = "MASTERCARD"
        actual = validate("5334699717990134")
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = "MASTERCARD"
        actual = validate("5555555555554444")
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = "VISA"
        actual = validate("4111111111111111")
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = "VISA"
        actual = validate("4012888888881881")
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = "VALID"
        actual = validate("6451962466988955")
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = "INVALID"
        actual = validate("6176292929")
        self.assertEqual(expected, actual)

    def testten(self):
        expected = "INVALID"
        actual = validate("1234567890314")
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

