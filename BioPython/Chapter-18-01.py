# Pairwise Sequence Alignment
from Bio import Align
aligner = Align.PairwiseAligner()
# print(aligner)
seq1 = 'CGGTAG'
seq2 = 'CGCTAGC'
alignment = aligner.align(seq1, seq2)
print('number of alignments:',len(alignment))
print(alignment[0])
print('target:', alignment[0].target)
print('query:', alignment[0].query)
print('score:', alignment[0].score)
print('algorithm:', aligner.algorithm)
print('epsilon:', aligner.epsilon)

# Customize scores:
aligner.match_score = 1.0
aligner.mismatch_score = -2.0
aligner.gap_score = -2.5
seq1 = 'GTTACCCCGCCATAAC'
seq2 = 'ACCGGGAATAGCCTA'
alignment = aligner.align(seq1, seq2)
print(alignment[0])
print('score:', alignment[0].score)

# Wild Card: exclude the specified letter 
seq1 = 'GTTACCCCGCCATAACNN'
aligner.wildcard = 'N'
alignment = aligner.align(seq1, seq2)
print(alignment[0])
print('score:', alignment[0].score)

# Example: Amino Acids
protein_1 = 'MERSTQELFINFTVVLITVLLMWLLVRSYQY'
protein_2 = 'MGINTRELFLNFTIVLITVILMWLLVRSYQY'
aligner2 = Align.PairwiseAligner()
score = aligner2.score(protein_1, protein_2)
alignments = aligner2.align(protein_1, protein_2)
print(len(alignments))
print(alignments[0])
print(score)
print(alignments[0].score)
# We must tell Aligner which substitution matrix should be used for Amino Acids 
matrix = Align.substitution_matrices.load('BLOSUM62')
aligner2.substitution_matrix = matrix
alignments = aligner2.align(protein_1, protein_2)
print(alignments[0])
print(alignments[0].score)

# Default mode for alignment is Global
# We can use local alignment as well
aligner = Align.PairwiseAligner()
chromosome = 'AAAAAAAACCCCccCAAAAAAaaAAAAGGggGGAAAAAAAAA'
transcript = 'CCCCCCCGGGGGG'
alignment = aligner.align(chromosome.upper(), transcript)
print(len(alignment))
print(alignment[0])
print(alignment[0].score)
print(aligner.mode)
aligner.mode = 'local'
alignment = aligner.align(chromosome.upper(), transcript)
print(len(alignment))
print(alignment[0])
print(alignment[0].score)
print(aligner.mode)