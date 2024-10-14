from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import AlignIO
from Bio import Align
from Bio.Align import MultipleSeqAlignment
from Bio.Align import substitution_matrices

# Exercise 1
seq1 = Seq('CCACTGCTAGCTAGCG id=zaza')
seq2 = Seq('C-ACT-CTAGCTAG-G id=zizi')
seq3 = Seq('-CACTGCTAGDTAGCG id=zozo')
seq_record1 = SeqRecord(seq1, id = 'zaza', description='first')
seq_record2 = SeqRecord(seq2, id = 'zizi', description='second')
seq_record3 = SeqRecord(seq3, id = 'zozo', description='third')
multi_seq_alignment = MultipleSeqAlignment([seq_record1, seq_record2, seq_record3])
AlignIO.write(multi_seq_alignment, './files/exercise_alignment.fasta', 'fasta')

# Exercise 2
seq1 = SeqIO.read('./files/sequence-AAH36555.1.fasta', 'fasta')
seq2 = SeqIO.read('./files/sequence-S70651.fasta','fasta')
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load('BLOSUM62')
alignment = aligner.align(seq1, seq2)
print('Number of alignments:', len(alignment))
print(alignment[0])
print('Score =', alignment.score)
print('\n\n')

aligner.mode = 'local'
print('Alignment mode changed to local')
alignment2 = aligner.align(seq1, seq2)
print('Number of alignments:', len(alignment2))
print(alignment2[0])
print('Score =', alignment2.score)