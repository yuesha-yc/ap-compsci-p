"""
|-------------------------------------------------------------------------------
| testvigenerecipher.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 22, 2019
|
| This is the PyUnit test bench for vigenerecipher.py
| Do not alter the contents of this file.
|
"""

from vigenerecipher import *
import unittest

class TestVigenereCipher(unittest.TestCase):
    def testone(self):
        expected = "hfnlp"
        actual = encrypt("hello", "abc")
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = "neghzfavhufpcfxbtgzrwepoz"
        actual = encrypt("meetmeattheparkatelevenam", "bacon")
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = "xpwntkmugeamuwelejpgkise"
        actual = encrypt("electricvehiclesaregreat", "tesla")
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = "uoammwgsrtmkhvshbyoewusubuanxcrd"
        actual = encrypt("lunchispizzacheeseburgersandsoda", "junkfood")
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = "xeapbfmzazvowmhfminxzeltjyk"
        actual = encrypt("caulifloweristhebesttasting", "vegetable")
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = "deeetymoeltvvesetmyerjlmaigmxekkyeqpum"
        actual = encrypt("cellphonesaregreatuntilthepowerrunsout", "battery")
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = "esvhlocjoohfdrrgvzigrbdrrvbnxpnrjjhnhxltauoz"
        actual = encrypt("readabookduringtheeveninginsteadofwatchingtv", "novel")
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = "lhvxtwenoaihvbihcfvdlerbawofnesjrmktt"
        actual = encrypt("whentheweatheriscoldwearahoodedjacket", "parka")
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = "upgpqlhtitchweuaqwqfgbvewewifdgpahlfzg"
        actual = encrypt("theroadsareflatsoyoucancycleeverywhere", "bicycle")
        self.assertEqual(expected, actual)

    def testten(self):
        expected = "vqxrvpzfmgeuiycacztkscxsxgszrrehyevdqpcsymtfr"
        actual = encrypt("bewareofsuddenrainstormsduringthesummerseason", "umbrella")
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

