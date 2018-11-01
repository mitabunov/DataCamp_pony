"""
More data cleaning and processing:
It's now time to deal with the missing data. There are several strategies for this: You can drop them, fill them in
using the mean of the column or row that the missing value is in (also known as imputation
(https://en.wikipedia.org/wiki/Imputation_(statistics))), or, if you are dealing with time series data, use a forward
fill or backward fill, in which you replace missing values in a column with the most recent known value in the column.
See pandas Foundations for more on forward fill and backward fill.

In general, it is not the best idea to drop missing values, because in doing so you may end up throwing away useful
information. In this data, the missing values refer to years where no estimate for life expectancy is available for a
given country. You could fill in, or guess what these life expectancies could be by looking at the average life
expectancies for other countries in that year, for example. Whichever strategy you go with, it is important to carefully
consider all options and understand how they will affect your data.

In this exercise, you'll practice dropping missing values. Your job is to drop all the rows that have NaN in the
life_expectancy column. Before doing so, it would be valuable to use assert statements to confirm that year and country
do not have any missing values.

Begin by printing the shape of gapminder in the IPython Shell prior to dropping the missing values. Complete the
exercise to find out what its shape will be after dropping the missing values!

INSTRUCTIONS:
*   Assert that country and year do not contain any missing values. The first assert statement has been written for you.
    Note the chaining of the .all() method to pd.notnull() to confirm that all values in the column are not null.
*   Drop the rows in the data where any observation in life_expectancy is missing. As you confirmed that country and
    year don't have missing values, you can use the .dropna() method on the entire gapminder DataFrame, because any
    missing values would have to be in the life_expectancy column. The .dropna() method has the default keyword
    arguments axis=0 and how='any', which specify that rows with any missing values should be dropped.
*   Print the shape of gapminder.
"""


# Import files with pandas
import pandas as pd
import numpy as np

g1800s = pd.read_csv('../_datasets/g1800.csv', delimiter=',')
g1900s = pd.read_csv('../_datasets/g1900.csv', delimiter=',')
g2000s = pd.read_csv('../_datasets/g2000.csv', delimiter=',')
# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s, g1900s, g2000s], axis=0, sort=False)

# Melt gapminder: gapminder_melt
gapminder = pd.melt(gapminder, id_vars='Life expectancy')
# Rename the columns
gapminder.columns = ['country', 'year', 'life_expectancy']

# Convert the year column to numeric
gapminder.year = pd.to_numeric(gapminder['year'], errors='coerce')
# Test if country is of type object
assert gapminder.country.dtypes == np.object
# Test if year is of type int64
assert gapminder.year.dtypes == np.int64
# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64

# Create the series of countries: countries
countries = gapminder['country']
# Drop all the duplicates from countries
countries = countries.drop_duplicates()
# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'
# Create the Boolean vector: mask
mask = countries.str.contains(pattern)
# Invert the mask: mask_inverse
mask_inverse = ~mask
# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# **************************************************************
# Print the shape of gapminder
print(gapminder.shape)

# Assert that country does not contain any missing values
assert pd.notnull(gapminder.country).all()

# Assert that year does not contain any missing values
assert pd.notnull(gapminder.year).all()

# Drop the missing values
gapminder = gapminder.dropna(axis=0, how='any')

# Print the shape of gapminder
print(gapminder.shape)

"""
Output comment:
After dropping the missing values from 'life_expectancy', the number of rows in the DataFrame has gone down from 169260 
to 43857. In general, you should avoid dropping too much of your data, but if there is no reasonable way to fill in or 
impute missing values, then dropping the missing data may be the best solution.
"""