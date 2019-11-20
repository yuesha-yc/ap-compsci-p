"""
|-------------------------------------------------------------------------------
| testwaterbilling.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 08, 2019
|
| This is the PyUnit test bench for waterbilling.py
| Do not alter the contents of this file.
|
"""

from waterbilling import *
import unittest

class TestWaterBilling(unittest.TestCase):
    def testone(self):
        expected = 5.0066
        actual = calculatebill("residential", 444400003, 444400135)
        self.assertAlmostEqual(expected, actual, 2)

    def testtwo(self):
        expected = 5.03415
        actual = calculatebill("residential", 699562838, 699563521)
        self.assertAlmostEqual(expected, actual, 2)

    def testthree(self):
        expected = 9.6522
        actual = calculatebill("residential", 769005304, 769098348)
        self.assertAlmostEqual(expected, actual, 2)

    def testfour(self):
        expected = 1000.0
        actual = calculatebill("commercial", 333123874, 333125349)
        self.assertAlmostEqual(expected, actual, 2)

    def testfive(self):
        expected = 1055.323125
        actual = calculatebill("commercial", 582776462, 585389387)
        self.assertAlmostEqual(expected, actual, 2)

    def testsix(self):
        expected = 1190.145825
        actual = calculatebill("commercial", 480937451, 488943284)
        self.assertAlmostEqual(expected, actual, 2)

    def testseven(self):
        expected = 1000.0
        actual = calculatebill("industrial", 727231412, 727232387)
        self.assertAlmostEqual(expected, actual, 2)

    def testeight(self):
        expected = 2000.0
        actual = calculatebill("industrial", 210453226, 210939213)
        self.assertAlmostEqual(expected, actual, 2)

    def testnine(self):
        expected = 4381.02715
        actual = calculatebill("industrial", 903806449, 959847535)
        self.assertAlmostEqual(expected, actual, 2)

    def testten(self):
        expected = 3000.426425
        actual = calculatebill("industrial", 795112816, 795929873)
        self.assertAlmostEqual(expected, actual, 2)

if __name__ == '__main__':
    unittest.main()

