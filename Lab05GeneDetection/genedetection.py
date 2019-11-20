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
    start = dna.find("ATG")
    end = dna.find(stopcodon)
    gene = dna[start:end+3]
    return gene

result = findgene("ATATGTAGCTAGCATAATA", "TAA")
print(result)

