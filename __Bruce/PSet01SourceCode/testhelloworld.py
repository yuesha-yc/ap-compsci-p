"""
|-------------------------------------------------------------------------------
| testhelloworld
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: May 20, 2019
|
| This program is the PyUnit test bench for helloworld.
|
"""

from helloworld import *
import unittest

class TestHelloWorld(unittest.TestCase):
    def testone(self):
        expected = "hello world"
        actual = displaymessage()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

