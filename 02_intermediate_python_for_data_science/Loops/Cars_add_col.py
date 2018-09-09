"""
Use a for loop to add a new column, named COUNTRY,
that contains a uppercase version of the country names in the"country" column.
You can use the string method upper() for this.

Two methods used:
- with for loop and iterrows()
- with apply(), when use other column (*)

(*) If you want to add a column to a DataFrame by calling a function on another column, then apply() is more efficient.
"""


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)
cars2 = pd.read_csv('cars.csv', index_col=0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = cars.loc[lab, "country"].upper()
# Print cars
print(cars)

print(50*'*')

# Use .apply(str.upper)
cars2["COUNTRY"] = cars2["country"].apply(str.upper)
# Print cars
print(cars2)
