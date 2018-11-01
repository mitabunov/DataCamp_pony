"""
Reshaping your data:
Now that you have all the data combined into a single DataFrame, the next step is to reshape it into a tidy data format.

Currently, the gapminder DataFrame has a separate column for each year. What you want instead is a single column that
contains the year, and a single column that represents the average life expectancy for each year and country. By having
year in its own column, you can use it as a predictor variable in a later analysis.

You can convert the DataFrame into the desired tidy format by melting it.

INSTRUCTIONS:
*   Reshape gapminder by melting it. Keep 'Life expectancy' fixed by specifying it as an argument to the id_vars
    parameter.
*   Rename the three columns of the melted DataFrame to 'country', 'year', and 'life_expectancy' by passing them in as a
    list to gapminder_melt.columns.
*   Print the head of the melted DataFrame.
"""


# Import files with pandas
import pandas as pd
g1800s = pd.read_csv('../_datasets/g1800.csv', delimiter=',')
g1900s = pd.read_csv('../_datasets/g1900.csv', delimiter=',')
g2000s = pd.read_csv('../_datasets/g2000.csv', delimiter=',')
# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s, g1900s, g2000s], axis=0, sort=False)

# **************************************************************
# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(gapminder, id_vars='Life expectancy')

# Rename the columns
gapminder_melt.columns = ['country', 'year', 'life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())
print(gapminder_melt.tail())
