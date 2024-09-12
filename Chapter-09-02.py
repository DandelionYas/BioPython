# Exercise 1
def reverseComplement(dna_sequence):
    complement_dict={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    complement_sequence=''
    for nucleotide in dna_sequence:
        complement_sequence += complement_dict[nucleotide]
    return complement_sequence[::-1]
print('********Reverse Complemet Calculator********')
dna_sequence = input("Enter a DNA sequence:")
print('Reverse Complement Sequence:', reverseComplement(dna_sequence))

# Excecise 2
dna_sequence='TGGGACAAGGGGTCACCCGAGTGCTGTCTTCCAATCTACTT'
print(f'DNA Sequence digested by a restriction enzyme: Original Sequence: {dna_sequence}')
print(dna_sequence.split('CCC'))