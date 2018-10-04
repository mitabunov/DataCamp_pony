"""
Using NumPy to import flat files

Load the MNIST digit recognition dataset using the numpy function loadtxt().

The first argument will be the filename.
The second will be the delimiter which, in this case, is a comma.
You can find more information about the MNIST dataset here on the webpage (http://yann.lecun.com/exdb/mnist/) of Yann
LeCun, who is currently Director of AI Research at Facebook and Founding Director of the NYU Center for Data Science,
among many other things.
"""

# Import package
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = r'../_datasets/mnist_digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[90, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()
