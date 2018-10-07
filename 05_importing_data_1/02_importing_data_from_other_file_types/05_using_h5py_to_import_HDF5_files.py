"""
Using h5py to import HDF5 files:
The file 'LIGO_data.hdf5' is already in your working directory. In this exercise, you'll import it using the h5py
library. You'll also print out its datatype to confirm you have imported it correctly. You'll then study the structure
of the file in order to see precisely what HDF groups it contains.

You can find the LIGO data plus loads of documentation and tutorials here. There is also a great tutorial on Signal
Processing with the data here.

INSTRUCTIONS:
* Import the package h5py.
* Assign the name of the file to the variable file.
* Load the file as read only into the variable data.
* Print the datatype of data.
* Print the names of the groups in the HDF5 file 'LIGO_data.hdf5'.


Extracting data from your HDF5 file:
In this exercise, you'll extract some of the LIGO experiment's actual data from the HDF5 file and you'll visualize it.

To do so, you'll need to first explore the HDF5 group 'strain'.

INSTRUCTIONS:
* Assign the HDF5 group data['strain'] to group.
* In the for loop, print out the keys of the HDF5 group in group.
* Assign to the variable strain the values of the time series data data['strain']['Strain'] using the attribute .value.
* Set num_samples equal to 10000, the number of time points we wish to sample.
* Execute the rest of the code to produce a plot of the time series data in LIGO_data.hdf5.
"""


# Import packages
import numpy as np
import h5py
import matplotlib.pyplot as plt

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)


print(50*'*')

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
