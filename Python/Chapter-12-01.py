# Syntax error
# print(Hello Pythonist!)

# Semantic error
# print('Hello'+10)
# print(25/0)

# Logic Error
a=10
b=30
average_ab=a+b/2
print(average_ab)

# Handling Exceptions
try:
    my_var = 10
    print(my_var+'string')
except NameError:
    print('An Name error occured!')
except:
    print('General Error occured!')
else:
    print('No error!')

# Example:
def my_division(a,b):
    try:
        division_reslut = a // b
        print("The answer is:", division_reslut)
    except ZeroDivisionError:
        print('Not possible to divide by zero!')
    except: 
        print('Something went wrong!')
    else:
        print('Successfully executed!')

my_division(7,4)