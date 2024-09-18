# Molecular Weight calculation of a protein sequece
prot_seq = input('Enter your protein sequence: ')
aa_mass = {'A':89, 'V':117, 'L':131, 'I':131, 'P':115, 'F':165, 'W':204, 'M':149, 'G':75, 'S':105, 
           'C':121, 'T':119, 'Y':181, 'N':132, 'Q':146, 'D':133, 'E':147, 'K':146, 'R':174, 'H':155}
prot_mw=0
for aa in prot_seq:
    prot_mw = prot_mw + aa_mass.get(aa.upper(),0)
prot_mw = prot_mw - (18*(len(prot_seq)-1))
print(f'The Molecular Weight is:', prot_mw)

# Exersice 1
primer_seq=input('Enter a primer sequece:')
seq_length=len(primer_seq)
if seq_length < 10:
    print('The primer must have at least ten nucleotides!')
elif seq_length < 25:
    print('This size is OK!')    
else:
    print('The primer is too long!')

# Exersice 2
dna_seq=input('Enter a DNA sequece:')
G_count=0
C_count=0
for nocluted in dna_seq:
    if nocluted == 'G':
        G_count +=1
    elif nocluted == 'C':
        C_count = C_count + 1
result = (G_count+C_count) / len(dna_seq)
print('GC content:', round(result,2))        


# Exersice 3
dna_seq=input('Enter DNA seq:')
index=0
position=-1
while index < len(dna_seq) - 2:
    if  dna_seq[index] == 'A' and dna_seq[index+1] == 'T' and dna_seq[index+2] == 'G':
        print('The position of ATG:', index)
        position = index
    index+=1

if position == -1:
    print('There is no ATG in sequence!')