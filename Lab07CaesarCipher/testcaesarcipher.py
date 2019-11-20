"""
|-------------------------------------------------------------------------------
| testcaesarcipher.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 06, 2019
|
| This is the PyUnit test bench for caesarcipher.py
| Do not alter the contents of this file.
|
"""

from caesarcipher import *
import unittest

class TestCaesarCipher(unittest.TestCase):
    def testone(self):
        expected = "ifmmp"
        actual = encrypt("hello", 1)
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = "yggv harrs"
        actual = encrypt("good pizza", 18)
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = "jbbq jb xq kllk"
        actual = encrypt("meet me at noon", 23)
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = "htruqnrjsyfwd hfpj ns ymj htskjwjshj wttr"
        actual = encrypt("complimentary cake in the conference room", 5)
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = "aol ilhy pz zapjrf dpao ovulf"
        actual = encrypt("the bear is sticky with honey", 7)
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = "nds ja jiz viy cvga v yjuzi ja ocz joczm"
        actual = encrypt("six of one and half a dozen of the other", 21)
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = "ftdx atr pabex max lng labgxl"
        actual = encrypt("make hay while the sun shines", 19)
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = "m efufot uz fuyq emhqe zuzq"
        actual = encrypt("a stitch in time saves nine", 12)
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = "whh pdwp cheppano eo jkp ckhz"
        actual = encrypt("all that glitters is not gold", 22)
        self.assertEqual(expected, actual)

    def testten(self):
        expected = "yzaje ngxj lux grr ul euax kdgsotgzouty"
        actual = encrypt("study hard for all of your examinations", 6)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

