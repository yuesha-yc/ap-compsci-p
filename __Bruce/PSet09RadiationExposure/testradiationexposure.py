"""
|-------------------------------------------------------------------------------
| testradiationexposure.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 10, 2019
|
| This is the PyUnit test bench for radiationexposure.py
| Do not alter the contents of this file.
|
"""

from radiationexposure import *
import unittest

class TestRadiationExposure(unittest.TestCase):
    def testone(self):
        expected = 39.10318784326239
        actual = decaycurvearea(0, 5, 1)
        self.assertAlmostEqual(expected, actual, 2)

    def testtwo(self):
        expected = 22.94241041057671
        actual = decaycurvearea(5, 11, 1)
        self.assertAlmostEqual(expected, actual, 2)

    def testthree(self):
        expected = 62.045598253839096
        actual = decaycurvearea(0, 11, 1)
        self.assertAlmostEqual(expected, actual, 2)

    def testfour(self):
        expected = 0.4346123561149849
        actual = decaycurvearea(40, 100, 1.5)
        self.assertAlmostEqual(expected, actual, 2)

    def testfive(self):
        expected = 19.29646913965563
        actual = decaycurvearea(5, 10, 0.25)
        self.assertAlmostEqual(expected, actual, 2)

    def testsix(self):
        expected = 25.61267436334904
        actual = decaycurvearea(0, 3, 0.5)
        self.assertAlmostEqual(expected, actual, 2)

    def testseven(self):
        expected = 6.7998675225953455
        actual = decaycurvearea(14, 20, 0.5)
        self.assertAlmostEqual(expected, actual, 2)

    def testeight(self):
        expected = 0.13540603366915924
        actual = decaycurvearea(48, 72, 0.4)
        self.assertAlmostEqual(expected, actual, 2)

    def testnine(self):
        expected = 80.71851259336131
        actual = decaycurvearea(0, 40, 1)
        self.assertAlmostEqual(expected, actual, 2)

    def testten(self):
        expected = 78.52805834817873
        actual = decaycurvearea(0, 60, 0.5)
        self.assertAlmostEqual(expected, actual, 2)

if __name__ == '__main__':
    unittest.main()

