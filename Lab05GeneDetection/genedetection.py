"""
|-------------------------------------------------------------------------------
| genedetection.py
|-------------------------------------------------------------------------------
|
| Author:  Kevin Wang
| Created: Nov. 30, 2020
|
| Transcription and Translation of Human DNA into Human Proteins
|
"""

# Standard RNA Nucleotides
rna_nucleotides = "UCAG"

# Declare the two Maps
start_map = {}
acid_map = {}

# Initialize the two Maps
start_map['CU'] = 'Leu'
start_map['GU'] = 'Val'
start_map['UC'] = 'Ser'
start_map['CC'] = 'Pro'
start_map['AC'] = 'Thr'
start_map['GC'] = 'Ala'
start_map['CG'] = 'Arg'
start_map['GG'] = 'Gly'

for nuc in rna_nucleotides:
    for key in start_map.keys():
        acid_map[key + nuc] = start_map[key]

acid_map['UUU'] = 'Phe'
acid_map['UUC'] = 'Phe'
acid_map['UUA'] = 'Leu'
acid_map['UUG'] = 'Leu'

acid_map['AUU'] = 'Ile'
acid_map['AUC'] = 'Ile'
acid_map['AUA'] = 'Ile'
acid_map['AUG'] = 'Met'

acid_map['UAU'] = 'Tyr'
acid_map['UAC'] = 'Tyr'
acid_map['UAA'] = 'Stop'
acid_map['UAG'] = 'Stop'

acid_map['CAU'] = 'His'
acid_map['CAC'] = 'His'
acid_map['CAA'] = 'Gln'
acid_map['CAG'] = 'Gln'

acid_map['AAU'] = 'Asn'
acid_map['AAC'] = 'Asn'
acid_map['AAA'] = 'Lys'
acid_map['AAG'] = 'Lys'

acid_map['GAU'] = 'Asp'
acid_map['GAC'] = 'Asp'
acid_map['GAA'] = 'Glu'
acid_map['GAG'] = 'Glu'

acid_map['UGU'] = 'Cys'
acid_map['UGC'] = 'Cys'
acid_map['UGA'] = 'Stop'
acid_map['UGG'] = 'Trp'

acid_map['AGU'] = 'Ser'
acid_map['AGC'] = 'Ser'
acid_map['AGA'] = 'Arg'
acid_map['AGG'] = 'Arg'


# Returns the Codons of the Gene Sequence as a list
def getTripledDNA(dna):
    tripled_dna = []
    for i in range(0, len(dna)):
        if i % 3 == 0:
            tripled_dna.append(dna[i: i + 3])
    return tripled_dna


# Returns a transcribed mRNA Strand
def transcribe(dna):
    rna = ""
    for char in dna:
        if char == 'C':
            rna += 'G'
            continue
        if char == 'G':
            rna += 'C'
            continue
        if char == 'T':
            rna += 'A'
            continue
        else:
            rna += 'U'
            continue
    return rna


# Returns the effective Gene Sequence as a String
def getGene(mRNA):
    endIndex = 0
    startIndex = mRNA.find("AUG")
    initedRNA = mRNA[startIndex:]

    for i in range(3, len(initedRNA)):
        if i % 3 == 0:
            if initedRNA[i: i + 3] == "UAA" or initedRNA[i:i + 3] == "UAG" or initedRNA[i:i + 3] == "UGA":
                endIndex = i
                break

    gene = initedRNA[: endIndex + 3]
    return gene


# Returns the Codons of the Gene Sequence as a list
def getCodons(gene):
    codons = []
    for i in range(0, len(gene)):
        if i % 3 == 0:
            codons.append(gene[i: i + 3])
    return codons


# Returns the tRNA of the DNA as a list
def get_tRNA(dna):
    tRNA = dna.replace('T', 'U')
    return tRNA


# Returns the Polypeptide as a list of Amino Acids
def createPolypeptide(codons):
    aacids = []
    for codon in codons:
        aacids.append(acid_map[codon])

    return aacids


DNA = "TACTTTGCATTAGCAAAAACAGACGGGTATCTAGGGCCCACCGTGCAGTACCGACCGTTTTACTGCACCACGTTGCCTTAGATT"
print("DNA:  " + DNA)
Result_TDNA = getTripledDNA(DNA)
print("TDNA: " + str(Result_TDNA))
Result_mRNA = transcribe(DNA)
print("mRNA: " + Result_mRNA)
Result_Gene = getGene(Result_mRNA)
print("Gene: " + Result_Gene)
print("Gene Length: " + str(len(Result_Gene)))
Result_Codons = getCodons(Result_Gene)
print("Codons: " + str(Result_Codons))
Result_tRNA = get_tRNA(DNA)
print("tRNA: " + str(Result_tRNA))
Result_Polypeptide = createPolypeptide(Result_Codons)
print("Polypeptide: " + str(Result_Polypeptide))
