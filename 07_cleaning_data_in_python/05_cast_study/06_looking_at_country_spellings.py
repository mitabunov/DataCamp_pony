"""
Looking at country spellings:
Having tidied your DataFrame and checked the data types, your next task in the data cleaning process is to look at the
'country' column to see if there are any special or invalid characters you may need to deal with.

It is reasonable to assume that country names will contain:
*   The set of lower and upper case letters.
*   Whitespace between words.
*   Periods for any abbreviations.

To confirm that this is the case, you can leverage the power of regular expressions again. For common operations like
this, Python has a built-in string method - str.contains() - which takes a regular expression pattern, and applies it to
the Series, returning True if there is a match, and False otherwise.

Since here you want to find the values that do not match, you have to invert the boolean, which can be done using ~.
This Boolean series can then be used to get the Series of countries that have invalid names.

INSTRUCTIONS:
*   Create a Series called countries consisting of the 'country' column of gapminder.
*   Drop all duplicates from countries using the .drop_duplicates() method.
*   Write a regular expression that tests your assumptions of what characters belong in countries:
    *   Anchor the pattern to match exactly what you want by placing a ^ in the beginning and $ in the end.
    *   Use A-Za-z to match the set of lower and upper case letters, \. to match periods, and \s to match whitespace
        between words.
*   Use str.contains() to create a Boolean vector representing values that match the pattern.
*   Invert the mask by placing a ~ before it.
*   Subset the countries series using the .loc[] accessor and mask_inverse. Then hit 'Submit Answer' to see the invalid
    country names!
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

# **************************************************************
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

# Print invalid_countries
print(invalid_countries)

"""
Output comment:
As you can see, not all these country names are actually invalid so maybe the assumptions need to be tweaked a little. 
However, there certainly are a few cases worth further investigation, such as St. Barth?lemy. Whenever you are dealing 
with columns of raw data consisting of strings, it is important to check them for consistency like this.
"""