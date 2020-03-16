"""
|-------------------------------------------------------------------------------
| testfahrenheit
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Aug 14, 2019
|
| This program is the PyUnit test bench for fahrenheit.
|
"""

from fahrenheit import *
import unittest

class TestFahrenheit(unittest.TestCase):
    def testone(self):
        expected = 212.0
        actual = calculatefahrenheit(100)
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = 32.0
        actual = calculatefahrenheit(0)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

