# Nested lists
life_style=[['cars', ['England','Germany', 'Italy'], 'jobs'], ['Toyota', 'BMW', 'Ford', 'Mazda'],['iran','canada',['dentist', 'teacher',['Runner','Writer','Coach']],'USA']]
print(life_style[2][2][2][0])

# Lists are mutable
my_list=[10,20,30,40,50,60]
print(my_list)
my_list[0]='Sara'
my_list=[10,20,30,40,50,60]
my_list[0:0]='Sara','is','coding','python'
print(my_list)
my_list=[10,20,30,40,50,60]
my_list[0:2]='Sara','is','coding','python'
print(my_list)
my_list=[10,20,30,40,50,60]
my_list[2:2]='Sara','is','coding','python'
print(my_list)

# Convert string to list: Two ways
str1="ABCD"
my_list=[]
my_list[:]=str1
print(str1)
print(my_list)
print(list(str1))

# Variables id: Address in memory
a=10
print("Variables's ID",id(a))
a=11
print("Variables's ID",id(a))
# the address is not the same: means its not using reference: variables are not mutable
my_list=[10,20,30,40]
print(id(my_list))
my_list[0]=11
print(id(my_list))
# Lists are mutable: list name is using reference

# Operations on list
my_list=['ATG', 'GGC', 'CCC', 'ATG', 'TTA']
print('count: ', my_list.count('CCC'))
print('ATG index: ', my_list.index('ATG'))
my_list.append('AAA')
print('Appended list: ', my_list)
my_list.insert(1, 'TTT')
print('Appended list: ', my_list)
my_list.remove('CCC')
print('Remove CCC from list: ', my_list)
my_list.remove('ATG')
print('Remove first ATG from list: ', my_list)
my_list.pop()
print('POP last element from list: ', my_list)
my_list.pop(1)
print('POP specific element from list: ', my_list)
del my_list[0]
print('del specific element from list: ', my_list)
print('list length: ', len(my_list))
print(id(my_list))
my_list=[5,10,2,3,6,8,18]
print(id(my_list))
print(my_list)
print(min(my_list), max(my_list), sum(my_list))
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# Copy lists
list1=[1,2,3,4]
list2=list1
list1.pop()
print(list1)
print(list2)
# Reference will be copied

list1=[1,2,3,4]
list2=list1[:]
list1.pop()
print(list1)
print(list2)

# Copy using module
import copy
list1=[1,2,3,4]
list2 = copy.copy(list1)
list1.pop()
print(list1)
print(list2)