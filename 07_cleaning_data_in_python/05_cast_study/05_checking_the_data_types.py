"""
Checking the data types:
Now that your data is in the proper shape, you need to ensure that the columns are of the proper data type. That is, you
need to ensure that country is of type object, year is of type int64, and life_expectancy is of type float64.

The tidy DataFrame has been pre-loaded as gapminder. Explore it in the IPython Shell using the .info() method. Notice
that the column 'year' is of type object. This is incorrect, so you'll need to use the pd.to_numeric() function to
convert it to a numeric data type.

INSTRUCTIONS:
*   Convert the year column of gapminder using pd.to_numeric().
*   Assert that the country column is of type np.object. This has been done for you.
*   Assert that the year column is of type np.int64.
*   Assert that the life_expectancy column is of type np.float64.
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

# **************************************************************
# Convert the year column to numeric
gapminder.year = pd.to_numeric(gapminder['year'], errors='coerce')

# Test if country is of type object
assert gapminder.country.dtypes == np.object

# Test if year is of type int64
assert gapminder.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64

"""
Output comment:
Since the assert statements did not throw any errors, you can be sure that your columns have the correct data types!
"""