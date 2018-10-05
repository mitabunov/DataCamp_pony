"""
Working with mixed datatypes (1):

Much of the time you will need to import datasets which have different datatypes in different columns; one column may
contain strings and another floats, for example. The function np.loadtxt() will freak at this. There is another
function, np.genfromtxt(), which can handle such structures. If we pass dtype=None to it, it will figure out what types
each column should be.

Working with mixed datatypes (2):
You have just used np.genfromtxt() to import data containing mixed datatypes. There is also another function
np.recfromcsv() that behaves similarly to np.genfromtxt(), except that its default dtype is None. In this exercise,
you'll practice using this to achieve the same result.
"""

# 1
import numpy as np

# Import 'titanic.csv' using the function np.genfromtxt()
data = np.genfromtxt(r'../_datasets/titanic.csv', delimiter=',', names=True, dtype=None)

# Print out first three entries of data
print(data[:3])

# 2
# Assign the filename: file
file = r'../_datasets/titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file, delimiter=',', names=True, dtype=None)

# Print out first three entries of d
print(d[:3])
