# Modules in Python
# Documentation page for module index: https://docs.python.org/3/py-modindex.html
import random
x = random.randint(10,50)
print(x)

for i in range(10):
    print(random.randint(10,50), end=' ')

import datetime
x = datetime.datetime.now()
print('\nCurrent Date:',x.day, x.month, x.year)

import math as mt
print('Cosinos 90:',mt.cos(90))

# More efficient way is to import specific function from a module
from math import cos as c
print('Cosinos 90:', c(90))

# No need to mention module name:
from math import *
# Its better not to use this, to prevent any confusion with the name of your own variables
print('Cosinos 90:', cos(90))

# See all funcions in a specific module
import math
print(dir(math))

# Use custom module
import my_module
username = input('Can I have your name please?')
my_module.salam(username)
user_age = my_module.chand_salete()
print(f'{username.upper()} is {user_age} years old.')

# Import specific funcion from the custom module
from my_module import chand_salete as cs, salam as sa
username = input('Your name please?')
sa(username)
user_age = cs()
print(f'{username.title()} is {user_age} years old!')

