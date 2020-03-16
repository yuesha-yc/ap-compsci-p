"""
|-------------------------------------------------------------------------------
| testrequestline.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 19, 2019
|
| This is the PyUnit test bench for requestline.py
| Do not alter the contents of this file.
|
"""

from requestline import *
import unittest

class TestRequestLine(unittest.TestCase):
    def testone(self):
        expected = "/hello.html"
        actual = parse("GET /hello.html HTTP/1.1")
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = "/hello.php?"
        actual = parse("GET /hello.php? HTTP/1.1")
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = "/hello.php?q=Abigail"
        actual = parse("GET /hello.php?q=Abigail HTTP/1.1")
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = "405 Method Not Allowed"
        actual = parse("POST /pizza.html HTTP/1.1")
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = "501 Not Implemented"
        actual = parse("GET burger.php HTTP/1.1")
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = "400 Bad Request"
        actual = parse("GET /chicken\"wings.php HTTP/1.1")
        self.assertEqual(expected, actual)
    
    def testseven(self):
        expected = "505 HTTP Version Not Supported"
        actual = parse("GET /chips.html HTTP/1.0")
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = "501 Not Implemented"
        actual = parse("GET chips.html HTTP/1.1")
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = "400 Bad Request"
        actual = parse("GET /gardensalad\".php HTTP/1.1")
        self.assertEqual(expected, actual)
    
    def testten(self):
        expected = "505 HTTP Version Not Supported"
        actual = parse("GET /chips.html HTTP/2.1")
        self.assertEqual(expected, actual)
    
if __name__ == '__main__':
    unittest.main()

