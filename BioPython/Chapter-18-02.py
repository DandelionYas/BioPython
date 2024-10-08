from Bio import SeqIO
from Bio import Align
from Bio.Align import substitution_matrices

target = SeqIO.read('./files/prot1.fasta', 'fasta')
query = SeqIO.read('./files/prot2.fasta', 'fasta')
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load('BLOSUM62')
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5

score = aligner.score(target.seq, query.seq)
print(score)
alignments = aligner.align(target.seq, query.seq)
print(len(alignments))
# print(alignments[0])
# print(aligner)


from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
seq1='MHQAIFIYQIGYPLKSGYIQSIRSPEYDNW'
seq2='MH--IFIYQIGYALKSGYIQSIRSPEY-NW'
seq3='M---IFIYQIGYAAKSGYIQSIRSPEY--W'
seq_record1=SeqRecord(Seq(seq1), id='Msn')
seq_record2=SeqRecord(Seq(seq2), id='Hub')
seq_record3=SeqRecord(Seq(seq3), id='Unk')
msalign = MultipleSeqAlignment([seq_record1, seq_record2, seq_record3])
print(msalign)
seq4='MF--IFIYQIGYAAKSGYIQSIRSPE---W'
seq_record4=SeqRecord(Seq(seq4), id='Cas')
msalign.append(seq_record4)
print(msalign)

# Calculate IsoElectric Point
from Bio.SeqUtils.ProtParam import ProteinAnalysis
for seq in msalign:
    print(ProteinAnalysis(str(seq.seq)).isoelectric_point())

print(msalign)
print(len(msalign))   
# print 10 first character from the first two alignment
print(msalign[:2,:10]) 
print('-----------------------------------------------')

# An online tool to calculate multiple sequence alignment
# Google: Multiple sequence alignment embl-ebi clustal omega: https://www.ebi.ac.uk/jdispatcher/msa/clustalo?stype=protein
# Generate Alignment for fasta and stockholm formats
from Bio import AlignIO
alignment = AlignIO.read('./files/clustalo.aln-fasta', 'fasta')
alignment = AlignIO.read('./files/clustalo.aln-stockholm', 'stockholm')
print(alignment)
print(f"Alignment length: {alignment.get_alignment_length()}")
for record in alignment:
    print(record)
    break

# Write an alignment to a file:
AlignIO.write(msalign, './files/my_aln.phy', 'phylip')

# Convert formats to eachother
count = AlignIO.convert('./files/my_aln.phy', 'phylip', './files/my_aln.fasta', 'fasta')
print('Number of converted alignments:', count)