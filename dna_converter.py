# A function to convern DNA to RNA
def convertToRNA(dna_sequence):
    transcription_dict = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
    rna_sequence = ''
    for nucleotide in dna_sequence:
        rna_sequence += transcription_dict[nucleotide]
    return rna_sequence