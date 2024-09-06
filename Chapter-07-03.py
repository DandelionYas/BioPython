# Tuples
my_tuple=(1)
print(my_tuple, type(my_tuple))
# type will not be tuple unless you use comma
my_tuple=(0,15,'Navid')
my_tuple=(1,2,3,4,5)
print(my_tuple, type(my_tuple))
my_list=[1,2,3,4,5]
# Tuples are not mutable
my_list[2]=30
print(my_list)
# my_tuple(2)=30 # Error
# my_tuple[2]=30 # Error
print(my_tuple)

# Convert tuple to list
new_list=list(my_tuple)
print(new_list)
# Use tuples unless you need mutability

# Membership
my_sequence='MRVRSWEDRTSAVW'
print('M' in my_sequence)
print('M' not in my_sequence)
my_list=[1,2,3,4,5]
print(2 in my_list)
print(3 not in my_list)
my_tuple=(1,2,3,4,5)
print(5 in my_tuple)
print(4 not in my_tuple)

# Dictionaries in Python
my_acids={'A':'Ala','M':'Met','R':'Arg','S':'Ser','C':'Cys'}
print(my_acids)
print(len(my_acids))
my_acids['H']='His'
print(my_acids)
print(len(my_acids))
my_acids.pop('M')
print(my_acids)
my_acids.clear()
print(my_acids)
my_acids={'A':'Ala','M':'Met','R':'Arg','S':'Ser','C':'Cys'}
print('keys: ', my_acids.keys())
print('values: ', my_acids.values())
print('key-values: ',my_acids.items())

print('Value for this key \'R\': ', my_acids['R'])
# print('Value for this key \'Z\': ', my_acids['Z']) # ERROR
print(my_acids.get('Z', 'There is no such key!'))

my_acids2=my_acids.copy()
print('Copied dict: ', my_acids2)


# Exercises
# Question-1
tuple_1=(0,1,2,3,4,5,6,7,8,9,10,11)
print(tuple_1[0::2])
print(tuple_1[::-1])
# Question-2
protein = {'Uniport_ID':'P1805', 'Name':'Regulatory A12', 'seq':'MRAGWPKLADGVM', 'seq_length':13}
print(protein)
print(protein['Name'])
protein['Name']='Unknown'
print(protein)
protein.pop('seq')
print(protein)
protein['seq']='MYTRAAVTYHWDECS'
print(protein)
protein.clear()
print(protein)
# Question-3
my_list=['AUG','UGG','CGU','AAA']
my_list_copy=my_list[:]
print(my_list)
print(my_list_copy)
print('my_list count before remove: ',len(my_list))
my_list.pop(2)
print('my_list count:', len(my_list))
print('my_list_copy count:', len(my_list_copy))
# Question-4
my_dict={1:'a',2:'b',3:'c',4:'e',5:'f'}
my_dict_copy=my_dict.copy()
print(my_dict_copy)
# Question-5
my_sequence='ATGCGTCAGTATGAG'
print('Fist accurance of \'AGT\':', my_sequence.index('AGT'))