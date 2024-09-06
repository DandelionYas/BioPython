# Lists
my_string='ATCGTAGATGGGCATTTA'
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])

my_list1=[1,2,3,4,5,6]
print(my_list1)
my_list2=[1,2.6,'Pythonist']
print(my_list2)

a,b,c=8,5.6,'Hello'
my_list3=[1,2.4**2,'Pythonist',a,b,c]
print(my_list3)

nested_list=[1,2.4**2,'Pythonist',[10,20,30]]
print(nested_list)

# Convert a string to list
my_string= "MLKNMMVSCTWER"
converted_list=list(my_string)
print(converted_list)

# Split the words
my_string="I am a Molecular Biologist!"
my_chars=list(my_string)
print(my_chars)
# Default delimeter is space
my_words=my_string.split() 
print(my_words)
my_string_2="Navid Arian,Ali,546-96,navid@gmail.com"
print(my_string_2.split(','))

# multiple asignment for a lot of variables
num_test='134,69,45,53.2,50,85'
a,b,c,d,e,f=num_test.split(',');
print('a=',a)
print('b=',b)

# operations on lists
print([1,2,3]*3)
my_list=[1,2,3]+['first','second','third']
print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# [Start Included : End Not Included]
my_list=[10,20,30,40,50,60]
print(my_list)
print(my_list[:])
print(my_list[0:])
print(my_list[1:])
print(my_list[0:2])
print(my_list[-6:])
print(my_list[:-4])
print(my_list[:100])

# [Start Included : End Not Included : Step]
print('\nsub list with step:')
print(my_list[::])
print(my_list[::2])
print(my_list[::-1])
print(my_list[::-2])
