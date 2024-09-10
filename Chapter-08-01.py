# Logical operators
print(True == 1)
print(False == 0)
print((6==6) + (7>6))

# Conditional Statement
codon='TGA'
if codon=='ATG':
    print(f'{codon} is the start codon!')
elif codon == 'TTA' or codon == 'TAG' or codon == 'TGA':
    print(f'{codon} is the stop codon!')
else:
    print(f'{codon} is not the start codon!')

control_expression = 1.4
treated_expression = 2.9
if treated_expression > control_expression:
    print('Gene is upregulated!')    
elif treated_expression == control_expression:
    print('Gene expression is not changed!')
else:
    print('Gene is downregulated!')

# Nested if Statements 
codon = input('Enter the codon:')
if codon == 'TAG' or codon == 'TAA' or codon == 'TGA' or codon == 'UAG' or codon == 'UAA' or codon == 'UGA':
    print('This is a STOP codon!')
else:
    if codon == 'ATG' or codon == 'AUG':
        print('It is the START codon!')
    else:
        print('It is not the START or a STOP codon!')

# Use list instead of multiple "or"s
stop_codon=['TAG', 'TAA', 'TGA', 'UAG', 'UAA', 'UGA']
if codon in stop_codon:
    print('This is a STOP codon!')
else:
    if codon == 'ATG' or codon == 'AUG':
        print('It is the START codon!')
    else:
        print('It is not the START or a STOP codon!')

# Use dictionary
aa_dict={'A':'Ala','M':'Met','R':'Arg','S':'Ser','C':'Cys'}
aa_input=input('Enter one letter:')
if aa_input in aa_dict:
    print(f'The letter code for {aa_input} is {aa_dict[aa_input]}')
else:
    print("Sorry, I don't have it in my dictionary")