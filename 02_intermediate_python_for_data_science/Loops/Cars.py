"""
Loop over DataFrame
Iterating over a Pandas DataFrame is typically done with the iterrows() method.
"""

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

print(cars)
print(50*'*')

# Iterate over rows of cars
for lab, row in cars.iterrows():
    # print index
    print(lab)
    # print data of each row
    print(row)

print(50*'*')

# Print 'cars per cap' data with index
for lab, row in cars.iterrows():
    print(lab+': '+str(row['cars_per_cap']))