# Exerciese 1
from Bio.Seq import MutableSeq
change_dict = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
seq = input('Please enter a DNA sequence:')
mutable_seq = MutableSeq(seq)
nucleotide = mutable_seq[1]
mutable_seq[1] = change_dict.get(nucleotide)
print('Changed second nucleotide:', mutable_seq)

# Exercise 2
from Bio.Seq import Seq
seq = input('Please enter a DNA sequence:')
seq = Seq(seq)
print('Complement:', seq.complement())
print('Reverse Complement:', seq.reverse_complement())
print('Transcript:', seq.transcribe())
print('Translated:', seq.translate())

# Exercies 3
from Bio.Seq import Seq
seq = Seq('GTGAATCGTATTT')
# print(seq.translate())
# Fix warning using following approach:
len = len(seq)%3
seq = seq[:-len]
print('Exercise 3',seq.translate())
