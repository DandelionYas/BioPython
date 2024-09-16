# Procedural Programming:
print('**************** Procedural Programming ****************')
num_list=[]
# function to add value to the list
def add_value(value):
   num_list.append(value) 

# function to remove value from the list
def remove_value():
   remove_value = num_list[-1]
   del num_list[-1]
   return remove_value

print('Initial list of value: ', num_list)
add_value(5)
add_value(6)
add_value(9.3)
add_value(12.8)
print('Updated list after adding values to the list: ', num_list)
value=remove_value()
print(f'Update list after removing value {value} is: ', num_list)
# If we want to do it for another list we must have another file containing same methods!

print('**************** Object Oriented Programming ****************')
# Object Oriented Programming:
class NumList:
    def __init__(self):
      self.__list = []
    
    def add_value(self, value):
       self.__list.append(value)

    def remove_value(self):
       removed_value = self.__list[-1]
       del self.__list[-1]
       return removed_value
    
    def get_list(self):
       return self.__list
    
list1 = NumList()
print('Initial list of value: ', list1.get_list())
list1.add_value(6)
list1.add_value(4.8)
list1.add_value(19)
list1.add_value(15)
list1.add_value(32)
print('Updated list after adding values to the list: ', list1.get_list())
value=list1.remove_value()
print(f'Updated list after removing value {value} is: ', list1.get_list())

