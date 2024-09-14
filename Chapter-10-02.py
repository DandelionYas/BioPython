# Packages in Python
# Documentation page for package index: https://pypi.org
# Install numpy => pip install numpy
import numpy as np
print(np.__version__)
print('Mean = ', np.mean([2,4,5,6,8,9]))
print('Median = ', np.median([2,4,5,6,8,9,1,3,2]))

# Exersice 1
import dna_converter 
dna_seq = input('Please enter a DNA sequence:')
print('RNA =', dna_converter.convertToRNA(dna_seq))

# Exersice 2
fahrenheit = input('Enter tempreture in fahreneheit:')
print('Tempreture in Celsius:', 5.9 * (int(fahrenheit)-32))

# Exersice 3
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(300)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

# Exersice 4
import matplotlib.pyplot as pplot
pplot.plot([2,6,10],[4,9,28])
pplot.title('DandelionAcademia'.upper())
pplot.xlabel('No. of students')
pplot.ylabel('No. of courses')
pplot.show()