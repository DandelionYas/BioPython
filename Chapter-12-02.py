# Exersice
a = input('Enter first number:')
b = input('Enter second number:')
try:
    sum_result = int(a) + int(b)
    print('The answer is:', sum_result)
except ValueError:
    print('Value Error occured!')    
except: 
    print('Something went wrong!')
else:
    print('Finally executed successfully!')
