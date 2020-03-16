"""
|-------------------------------------------------------------------------------
| testgenedetection.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 16, 2019
|
| This is the PyUnit test bench for genedetection.py
| Do not alter the contents of this file.
|
"""

from genedetection import *
import unittest

class TestGeneDetection(unittest.TestCase):
    def testone(self):
        expected = "ATGTAGCTAGCATAA"
        actual = findgene("ATATGTAGCTAGCATAATA", "TAA")
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = "ATGCATCATCATTAA"
        actual = findgene("CATATGCATCATCATTAACATCATCAT", "TAA")
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = "ATGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAA"
        actual = findgene("GATTACAATGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAAGATTACA", "TAA")
        self.assertEqual(expected, actual)

    def testfour(self):
        expected = "ATGCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATTAA"
        actual = findgene("GGGGGGGGATGCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATTAAGGGGGGGGGGGGGGGGG", "TAA")
        self.assertEqual(expected, actual)

    def testfive(self):
        expected = "ATGACAAATCACAATCACAAATATACACAACAATAG"
        actual = findgene("TCGCTTGCTCGACGCTCGCTGACGATGACAAATCACAATCACAAATATACACAACAATAGACATATCAATA", "TAG")
        self.assertEqual(expected, actual)

    def testsix(self):
        expected = "ATGCGTGCTCGTCGTCGTCGCTCGCTGCTGCTCGTCGCTTAG"
        actual = findgene("ATCTACTATCACCATCATCATAAACTATGCGTGCTCGTCGTCGTCGCTCGCTGCTGCTCGTCGCTTAGATCGATGCATCGATGACATCGAT", "TAG")
        self.assertEqual(expected, actual)

    def testseven(self):
        expected = "ATGTCGCTGCTCGTCGTCGCTCGCTCGCCGGTCTCGCGCGCTTAG"
        actual = findgene("ACGAGAGCAGAGCGCCGCAAGACGACGACAGACGATGTCGCTGCTCGTCGTCGCTCGCTCGCCGGTCTCGCGCGCTTAGCGATCGATCGAT", "TAG")
        self.assertEqual(expected, actual)

    def testeight(self):
        expected = "ATGCGCTTCGCGCGCTCTGCGCGCGCTCTCTCTCGCGCGCTCTCCCGGTGA"
        actual = findgene("ACTACTACATAATTCTCTCTAATCTCTCTATATGCGCTTCGCGCGCTCTGCGCGCGCTCTCTCTCGCGCGCTCTCCCGGTGAATATCGCGCA", "TGA")
        self.assertEqual(expected, actual)

    def testnine(self):
        expected = "ATGCGCTCGGCTCGCGCCGGCGCTCTCGCGCTCGCTTGA"
        actual = findgene("ACGCGCGCGCGAGAGACGAGCAGCAGCATGCGCTCGGCTCGCGCCGGCGCTCTCGCGCTCGCTTGAACTCGGCATATCGCGATATAT", "TGA")
        self.assertEqual(expected, actual)

    def testten(self):
        expected = "ATGTTCGCTCCTGCGCTCTCTCTCGCGCGCGCTCTCGTCGTCTGA"
        actual = findgene("ATCATACATATCTCTCCTATATACTATGTTCGCTCCTGCGCTCTCTCTCGCGCGCGCTCTCGTCGTCTGAATCAGCTAGCATCGATCGAATC", "TGA")
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
