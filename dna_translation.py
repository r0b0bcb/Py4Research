# # # # # # # # # # # # # # # #
# DNA Translation to Protein  #
# r0b0bcb                     #
# 3/28/2018                   #
# # # # # # # # # # # # # # # #

def read_seq(inputfile):
    """Takes input file, reads and removes unwanted special chars"""
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n","")  #removes new line charactor from the plain txt file
    seq = seq.replace("\r","")  #removes return carriage "
    return seq

def dna_2_protein(sequence):
    """Takes 3 digit string. example: sequence = "ATA"
    Translate a string containing a nucleotide sequence into a string 
    containing the corresponding sequence of amino acids. 
    Nucleotides are translated in triplets using the table dictionary; 
    each amino acid 4 is encoded with a string of length 1."""
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
	}

    protein = ""
    if len(sequence) % 3 == 0:
        for loop in range (0, len(sequence), 3):
            codon = sequence[loop : loop+3]
            protein += table[codon]
    return protein

# Reads the file contained in same folder named "dna.txt"
inputfile = "dna.txt"

prt = read_seq("protein.txt")
dna = read_seq("dna.txt")
d2p = dna_2_protein(dna[20:938])[:-1] #NCBI tells dna sequence is from char 21-938, where last char is stop codon, which we don't need

# Since the NCBI gives bot hDNA sequence and Protein translation, we can error check the code.
print("Protein translation successful? %s" %(prt == d2p))
print(d2p)
