# Exercise 1
from Bio import SeqIO
fasta_record = SeqIO.read('./files/sequence-Z78524.1.fasta','fasta')
fasta_record.id = 'New ID'
print(fasta_record.format('fasta'))

# Exercise 2
genbank_record = SeqIO.read('./files/sequence-Z78524.1.gb','genbank')
print(genbank_record.annotations['source'])
print(genbank_record.seq[14:])

# Exercise 3
import gzip
# rt: read, text
with gzip.open('./files/gencode.v46.pc_translations.fa.gz', 'rt') as handle:
    all_record = SeqIO.parse(handle, 'fasta')
    first_record = next(all_record)
print('First Record from gzip file:',first_record)