"""
|-------------------------------------------------------------------------------
| testpolybiuscipher.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 14, 2019
|
| This is the PyUnit test bench for polybiuscipher.py
| Do not alter the contents of this file.
|
"""

from polybiuscipher import *
import unittest

class TestPolybiusCipher(unittest.TestCase):
    def testone(self):
        expected = "buy12cheesepizzas"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "bcfbfeacbdadafcacafacacedfffffabfa"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = "read8bookseverymonth"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "cdcaabcfbabcbebeedfacafccacdfebfbeaabbaf"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = "study3hourseveryevening"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "fabbfbcffeaeafbefbcdfacafccacdfecafccaaadfaadd"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = "get9hoursofsleep"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "ddcabbeaafbefbcdfabedbfaeecacace"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = "winteriscoming2019"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "ccdfaabbcacddffaadbebfdfaaddbdecacea"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = "exercise30minutesperday"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "cafdcacdaddffacaaeecbfdfaafbbbcafacecacdcfabfe"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = "eat5servingsofvegetables"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "caabbbcbfacacdfcdfaaddfabedbfccaddcabbabbceecafa"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = "run5kilometersin20minutes"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "cdfbaacbeddfeebebfcabbcacdfadfaabdecbfdfaafbbbcafa"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = "donotfeedwildanimals"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "cfbeaabebbdbcacacfccdfeecfabaadfbfabeefa"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

    def testten(self):
        expected = "depositcansinrecycling"
        key = [["n", "a", "1", "c", "3", "h"], ["8", "t", "b", "2", "o", "m"],
               ["e", "5", "w", "r", "p", "d"], ["4", "f", "6", "g", "7", "i"],
               ["9", "j", "0", "k", "l", "q"], ["s", "u", "v", "x", "y", "z"]]
        message = "cfcacebefadfbbadabaafadfaacdcaadfeadeedfaadd"
        actual = decrypt(message, key)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

