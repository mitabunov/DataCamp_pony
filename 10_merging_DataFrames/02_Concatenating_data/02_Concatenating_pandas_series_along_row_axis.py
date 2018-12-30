"""
Concatenating pandas Series along row axis:

Having learned how to append Series, you'll now learn how to achieve the same result by concatenating Series instead.
You'll continue to work with the sales data you've seen previously. This time, the DataFrames jan, feb, and mar have
been pre-loaded.

Your job is to use pd.concat() with a list of Series to achieve the same result that you would get by chaining calls to
.append().

You may be wondering about the difference between pd.concat() and pandas' .append() method. One way to think of the
difference is that .append() is a specific case of a concatenation, while pd.concat() gives you more flexibility, as
you'll see in later exercises.

Instructions:
*   Create an empty list called units. This has been done for you.
*   Use a for loop to iterate over [jan, feb, mar]:
    *   In each iteration of the loop, append the 'Units' column of each DataFrame to units.
*   Concatenate the Series contained in the list units into a longer Series called quarter1 using pd.concat().
    *   Specify the keyword argument axis='rows' to stack the Series vertically.
*   Verify that quarter1 has the individual Series stacked vertically by printing slices.
"""


# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('../_datasets/Sales/sales-jan-2015.csv', parse_dates=True, index_col='Date')
# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('../_datasets/Sales/sales-feb-2015.csv', parse_dates=True, index_col='Date')
# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('../_datasets/Sales/sales-mar-2015.csv', parse_dates=True, index_col='Date')
# ***********************************************

# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis='rows')

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])