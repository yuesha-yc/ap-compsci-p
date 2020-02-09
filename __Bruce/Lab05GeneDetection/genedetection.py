"""
|-------------------------------------------------------------------------------
| genedetection.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 16, 2019
|
| This program determines which genes are present in a DNA sequence.
|
"""

def findgene(dna, stopcodon):
    # YOUR CODE HERE
    start = dna.index("ATG")
    stop = dna.index(stopcodon)
    length = len(stopcodon)
    ans = dna[start:stop + length]
    return ans 

result = findgene("ATATGTAGCTAGCATAATA", "TAA")
print(result)

