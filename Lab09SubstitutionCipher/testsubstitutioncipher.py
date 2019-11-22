"""
|-------------------------------------------------------------------------------
| testsubstitutioncipher.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 21, 2019
|
| This is the PyUnit test bench for substitutioncipher.py
| Do not alter the contents of this file.
|
"""

from substitutioncipher import *
import unittest

class TestSubstitutionCipher(unittest.TestCase):
    def testone(self):
        expected = "vkxxn"
        actual = encrypt("hello", "jtrekyavogdxpsncuizlfbmwhq")
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = "tuncrejmjmcrenx"
        actual = encrypt("gonewiththewind", "yfpxcatmelosqnugihwjbkrzdv")
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = "rwllhwgxenjngxpyyo"
        actual = encrypt("pizzaisthebestfood", "hjdonpkewabuqfyrmigxtzscvl")
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = "ocvijvypvajijgeqk"
        actual = encrypt("greatexpectations", "iuaxvrowghdmbqeplckjftnysz")
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = "bylomypqywphqomayuypwbjyl"
        actual = encrypt("besuretoeatyourvegetables", "wbrgysuxzedjtiqnfmlpoavkhc")
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = "reidioenqeyroejthgpgnhjfxdlshhjf"
        actual = encrypt("wearahelmetwhenbicyclingorskiing", "itgwevfohmsnqjxuadlyzbrcpk")
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = "exwanzlkkrbfahfbmlodqfkkndwqltfge"
        actual = encrypt("studywellinadvanceforallyourexams", "fpmalovsryjkgbdciqexwhztnu")
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = "dydqvyivolivksophkvk"
        actual = encrypt("awakewhenthesunrises", "dfmzvgeihnqjcortxpklsbywua")
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = "dfuqkzryszvwszduvdzwd"
        actual = encrypt("slumberwhenthesunsets", "mkgxzojschnfqvipardwulybte")
        self.assertEqual(expected, actual)

    def testten(self):
        expected = "qjitkcrytmswgmyvfwggyyvtquoify"
        actual = encrypt("drinkplentyofteacoffeeandjuice", "vnfqygeliukratwcbjxmohdzsp")
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

