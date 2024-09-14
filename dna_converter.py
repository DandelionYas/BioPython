# A function to convern DNA to RNA
def convertToRNA(dna_sequence):
    rna_sequence = ''
    for nucleotide in dna_sequence:
        if nucleotide == 'T':
            rna_sequence += 'U'
        else:
            rna_sequence += nucleotide
    return rna_sequence