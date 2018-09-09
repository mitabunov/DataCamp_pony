"""
Looping over all elements in 1D Numpy array.
Looping over all elements in 2D Numpy array with np.nditer.
"""

import numpy as np

'1D array'
np_height = np.array([74, 74, 72, 75, 75, 73])
# For loop over np_height
print('Loop over 1D array')
for element in np_height:
    print(str(element)+' inches')


'nd array'
np_baseball = np.array([[74, 74, 72, 75, 75, 73],
                        [180, 215, 210, 205, 190, 195]])
print('Loop over 2D array')
# For loop over np_baseball
for base in np.nditer(np_baseball):
    print(base)
