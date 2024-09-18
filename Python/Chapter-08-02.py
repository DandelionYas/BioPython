# While loop in Python
n=0
while n<5:
    print('n =',n, end=' ') # end recieves end line character: default: \n
    n=n+1
print('---------')
print('Exit n:', n)

# Break keyword
n=0
while True:
    if n<5:
        print('while true:',n)
    else:
        break
    n+=1            

# Longest DNA Segment
dna_segment=['GGCACAG','GTAATTGGGGACCT','GAAGGTTCC','GGGCCTCA','ATTCTCCGGCCTA','ACCGCGTA','AATTAT','TGACACAGC']
longest=0
index=0
total_data=len(dna_segment)
while index < total_data:
    current=len(dna_segment[index])
    if longest < current:
        longest = current
        longest_segment = dna_segment[index]
    index += 1
print('Longest:', longest, longest_segment)

# for loop in Python
dna='ATGCAGTAGG'
for base in dna:
    print(base)

# use index and enumerate with for loop
dna=['A','G','C','T']
for index,i in enumerate(dna):
    print('enumerate',index, i)

# user range
for i in range(0,6): # from 0 to 5
    print('range',i)

for i in range(3,15,3):
    print('range with step:', i)