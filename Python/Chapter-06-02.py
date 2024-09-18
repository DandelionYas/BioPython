dna_seq='AACTGGGTACCTTAACATGCGTCGCGT'
calculated=dna_seq.count('A')/dna_seq.count('G')*100
print(calculated)
#Round 3 digits
print(round(calculated,3))
print('Content',round(calculated,3))
print('Content='+str(round(calculated,3)))
my_protein='UGCCCGGUAACGACCGGCCGGUAACCGGUAACGAUGCGCCGGUAACGACCC'
print('\"AUG\" Position using find:',my_protein.find('AUG'))
print('\"AUG\" Position using index:',my_protein.index('AUG'))
print('\"AAA\" Position using find:',my_protein.find('AAA')) #return -1
# print('\"AAA\" Position:',my_protein.index('AAA')) #throws exception

print('Index 0',dna_seq[0]) # print character in index 0
print('Index 3:6',dna_seq[3:6]) # starting from index: 3 to 6
print('Index :',dna_seq[:]) # whole string
print('Index :-3',dna_seq[:-3]) #starting from beggining to 3 chars before last

forename='    Yaser      '
surname='      Ghaderipour'
print(forename.rstrip()+surname.lstrip()) #Remove Spaces from left and right
print(forename.strip()+surname.strip()) #Remove Spaces from both sides: R and L

full_name=f"{forename.strip()} {surname.strip()}" # format strings
print(full_name)
full_name=f"Hello, {forename.strip()} {surname.strip()}" 
print(full_name)