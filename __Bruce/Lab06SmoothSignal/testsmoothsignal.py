"""
|-------------------------------------------------------------------------------
| testsmoothsignal.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 30, 2019
|
| This is the PyUnit test bench for smoothsignal.py
| Do not alter the contents of this file.
|
"""

from smoothsignal import *
import unittest

class TestSmoothSignal(unittest.TestCase):
    def testone(self):
        expected = [3, 3, 4, 5, 6, 7, 6, 6, 5, 4, 4, 4]
        waveform = [1, 5, 4, 5, 7, 6, 8, 6, 5, 4, 5, 4]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = [41, 37, 24, 31, 23, 19, 39, 46, 41, 27, 25, 31, 47, 55, 51, 46, 51, 72, 54, 52]
        waveform = [70,13,29,32,34,4,21,94,24,6,51,20,24,97,44,12,83,58,75,30]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = [70, 76, 62, 50, 32, 33, 59, 49, 38, 10, 20, 46, 44, 59, 53, 63, 62, 51, 54, 42]
        waveform = [91,50,88,48,16,33,50,96,3,16,11,35,94,3,82,74,35,77,43,42]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = [86, 88, 88, 76, 62, 43, 56, 66, 73, 53, 45, 53, 69, 72, 56, 59, 47, 54, 52, 62]
        waveform = [94,79,91,94,45,49,36,85,78,56,25,56,78,74,66,30,82,31,49,76]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = [47, 57, 78, 63, 40, 35, 36, 57, 57, 82, 58, 63, 42, 52, 25, 44, 46, 67, 70, 87]
        waveform = [27,68,77,91,21,8,77,23,73,76,98,0,93,33,31,13,88,38,77,97]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = [12, 23, 32, 62, 77, 63, 57, 28, 37, 29, 34, 43, 42, 51, 50, 41, 30, 32, 29, 36]
        waveform = [23,2,46,50,91,92,7,72,7,32,48,22,60,45,48,59,16,16,66,7]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = [37, 44, 40, 70, 72, 78, 56, 67, 54, 77, 55, 60, 35, 50, 59, 82, 61, 52, 28, 38]
        waveform = [71,4,59,57,95,65,75,29,98,37,98,30,52,25,73,80,95,8,55,22]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = [33, 30, 22, 30, 28, 37, 40, 67, 78, 66, 61, 55, 51, 45, 39, 38, 38, 56, 53, 47]
        waveform = [27,40,23,3,64,18,31,73,97,64,38,83,44,26,66,25,25,66,79,16]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = [31, 50, 67, 84, 80, 86, 62, 62, 51, 53, 44, 59, 69, 77, 72, 65, 71, 66, 71, 60]
        waveform = [16,47,87,68,98,75,85,27,76,50,33,51,94,64,74,79,42,93,65,56]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

    def testten(self):
        expected = [62, 61, 35, 49, 56, 73, 48, 28, 30, 53, 66, 54, 33, 33, 56, 76, 81, 70, 77, 78]
        waveform = [86,38,61,6,81,82,57,7,22,61,76,63,23,14,62,94,73,77,62,94]
        actual = levelling(waveform)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()



