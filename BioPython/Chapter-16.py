# Import calss SeqRecord form module SeqRecord
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

# Define SeqRecord: Amino Acid
prot_seq = Seq('QAGKAAEPAKLIVPMVELFMKSDRAFKPKRERG')
record = SeqRecord(prot_seq)
record.id = 'OYX91288.1'
record.name = 'MAG'
record.description = 'mall protein, partial [caulobacter sp. 35-67-4]'
# print(record)

# apply FastA format
print(record.format('fasta'))

# Annotations: for saving extra information 
record.annotations['Kingdom', 'Species'] = 'Animalia', 'Homo sapiens'
print(record)

# Letter Annotation: should be defined for all letters in Seq
sub_record = record[:4]
print(sub_record.seq)
sub_record.letter_annotations['Amino acid score'] = [1.5,1.6,2,1.9]
print(sub_record.letter_annotations)
print(sub_record)

# SeqRecord Object Comparison
record_1 = SeqRecord(Seq('GCGTA'), name='motif')
record_2 = SeqRecord(Seq('GCGTA'), name='motif')
print(record_1.seq == record_1.seq)
print(record_1.name == record_1.name)

# Exercie 1
seq = SeqRecord('GTAATTTGCCGGAACCTCCG')
seq.id = 'PRO91288.2'
seq.description = 'A sample Protein Sequence'

# Exercise 2
print(seq.format('fasta'))

# Exercise 3
print(seq[3:], 'length=',len(seq[3:]))