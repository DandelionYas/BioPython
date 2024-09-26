# import class Sequence from package Seq from BioPython
from Bio.Seq import Seq
func_list = dir(Seq)
# for function in func_list:
    # print(function)


my_seq = Seq('GTAGTCCAGTCCTGAGGAATCCAUGGATCGATACGTCGTTACGTA')
my_seq1 = Seq('GTGAATCGTATTGTATGAATGGGCCGCTGAAAACGCCGATAG')
print(my_seq)
print(my_seq.complement())
print(my_seq.reverse_complement())
print(my_seq.transcribe()) # mRNA sequence

# translate is being done using standard translation
# Google this: NCBI Genetic Codes: 
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
print(my_seq.translate())
# TGA is stop codon by default
print(my_seq1.translate())
# we can only include from beginning to the first stop codon:
print(my_seq1.translate(to_stop=True))
# Default table
print(my_seq1.translate(table=1))
# Use Yeast Mitochondrial Code translation table
# جدول ترجمه میتوکندری مخمر
print(my_seq1.translate(table=3))
# By default GTG will be translated to V but here it will be translated to M 
# Can not be applied to table type 1 because GTG is not start codon
print(my_seq1.translate(table=3, cds=True))

from Bio.Data import CodonTable
# See standard translation table
# print(CodonTable.standard_dna_table)
# print(CodonTable.unambiguous_dna_by_name['Standard'])
print(CodonTable.unambiguous_dna_by_id[3])

my_rna = Seq('GUGAAUCGUAUUGUAUGAAUGGGCCGCUGAAAACGCCGAUAG')
print('RNA: ', my_rna)
print('DNA strand (non template strant): ', my_rna.back_transcribe())
print('Template strand: ', my_rna.back_transcribe().reverse_complement())

# We can use string funcions on Seq object
print(my_rna.find('GUA'))
print(my_rna[1])
print(my_rna[5:18])
print(len(my_rna))
print(my_rna.lower())

# Use Biopython for calculating CG content
from Bio.SeqUtils import gc_fraction as GC
print(round(GC(my_seq1) * 100, 2))

# Its better to just import specific functions from a class
from Bio.Seq import transcribe, translate, back_transcribe
print(transcribe(my_seq1))
print(translate(my_seq1))
print(back_transcribe(my_rna))

# Seq Object is immutable
# we can not change a specific nucleotide in Seq: my_seq[1]='A'
# There is another class for this purpose
from Bio.Seq import MutableSeq
mu_seq = MutableSeq('GTGAATCGATATTGT')
print(mu_seq)
mu_seq[2]='A'
print(mu_seq)
# We can create a Seq from a Mutable Seq to protect it from mutability
seq = Seq(mu_seq)
