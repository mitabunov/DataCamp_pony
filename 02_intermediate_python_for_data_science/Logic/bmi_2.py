"""
Continuation to bmi from Intro to Python Numpy example
This example shows how to use boolean operators against NumPy arrays
"""

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2

print(bmi)

# Cannot use boolean operators with arrays
# print(bmi > 21 and bmi < 22)
# ValueError: The truth value of an array with more than one element
# is ambiguous. Use a.any() or a.all()

print(np.logical_and(bmi > 21, bmi < 22))

print(bmi[np.logical_and(bmi > 21, bmi < 22)])
