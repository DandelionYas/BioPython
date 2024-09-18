# Open a file:
file_handle = open('./files/file.txt') 
# Second parameter is 'rt' by default which means to opent text file in read only mode

# Default parameter for read is -1, which means to read all content of the file
print(file_handle.read())
file_handle.close()
print('------------------------')

file_handle = open('./files/file.txt') 
# Read a line form text file:
print(file_handle.readline())
print(file_handle.readline())
file_handle.close()
print('------------------------')

# How to open a file in auto close mode?
with open('./files/file.txt', 'r') as file_handle:
    f_read = file_handle.read()
    print(f_read)
    print('********************')
    print(repr(f_read))

# Separate a specific part of text in file
with open('./files/file.txt', 'r') as file_handle:
    f_read = file_handle.read()
    print(f_read.split('\n') [2] [0:5])

# Read protein data from downloaded file:
with open('./files/sequence.fasta', 'r') as my_protein:
    read_p = my_protein.read()
    protein_name = read_p.split('\n') [0][1:]
    protein_seq = read_p.split('\n')[1:]
print(protein_name)
print(protein_seq)
# Use join method from string to concat all elements in list
protein_seq = ''.join(protein_seq)
print(protein_seq) 
serin_count = 0
for aa in protein_seq:
    if aa in 'S':
        serin_count += 1
print('Serin count =', round(serin_count/len(protein_seq)*100,2), '%')