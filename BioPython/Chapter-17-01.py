from Bio import SeqIO
# help(SeqIO)
# print(dir(SeqIO))
record = SeqIO.read('./files/sequence.fasta','fasta')
print(type(record))
print(record.id)
print(record.seq)
print(len(record.seq))

# Using method parse for multiple records:
all_record = SeqIO.parse('./gencode.v46.pc_translations.fa','fasta')
print(type(all_record))
for record in all_record:
    first_record = record
    break
print(type(first_record))
print(first_record.id)
print(len(first_record.seq))
# Useing next() function
second_record = next(all_record)
print(second_record.id)
# Coding DNA Sequence: CDS
cds = second_record[28:201]
print(type(cds))
print(cds.seq)
print(type(all_record))
list_record = list(all_record)
print('number of sequences:', len(list_record))
# print first part of id
first_five = list_record[0:5]
i=0
ids=[]
for record in first_five:
    ids.append(first_five[i].id.split('|')[0])
    i+=1
print(ids)
# Modify SeqRecord:
first_record.id = 'New_ID'
first_record.description = 'New Description'
print(first_record.format('fasta'))
print('-------------------------------------')

# Read GenBank formatted Nucleotide Sequence
record = SeqIO.read('./files/sequence.gb', 'genbank')
print(record.seq)
print(record.annotations['organism'])

# Use handle instead of file name
with open('./files/sequence.fasta') as handle:
    all_record = SeqIO.parse(handle, 'fasta')

# Open compressed file:
import gzip
# rt: read, text
with gzip.open('./files/gencode.v46.pc_translations.fa.gz', 'rt') as handle:
    all_record = SeqIO.parse(handle, 'fasta')
    first_record = next(all_record)
print(first_record)