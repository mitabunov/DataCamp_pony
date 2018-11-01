"""
Wrapping up:
Now that you have a clean and tidy dataset, you can do a bit of visualization and aggregation. In this exercise, you'll
begin by creating a histogram of the life_expectancy column. You should not get any values under 0 and you should see
something reasonable on the higher end of the life_expectancy age range.

Your next task is to investigate how average life expectancy changed over the years. To do this, you need to subset the
data by each year, get the life_expectancy column from each subset, and take an average of the values. You can achieve
this using the .groupby() method (http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html).
This .groupby() method is covered in greater depth in Manipulating DataFrames with pandas.

Finally, you can save your tidy and summarized DataFrame to a file using the .to_csv() method.

INSTRUCTIONS:
*   Create a histogram of the life_expectancy column using the .plot() method of gapminder. Specify kind='hist'.
*   Group gapminder by 'year' and aggregate 'life_expectancy' by the mean. To do this:
*   Use the .groupby() method on gapminder with 'year' as the argument. Then select 'life_expectancy' and chain the
    .mean() method to it.
*   Print the head and tail of gapminder_agg. This has been done for you.
*   Create a line plot of average life expectancy per year by using the .plot() method (without any arguments) on
    gapminder_agg.
*   Save gapminder and gapminder_agg to csv files called 'gapminder.csv' and 'gapminder_agg.csv', respectively, using
    the .to_csv() method.
"""


# Import files with pandas
import pandas as pd
import matplotlib.pyplot as plt
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

# Assert that country does not contain any missing values
assert pd.notnull(gapminder.country).all()
# Assert that year does not contain any missing values
assert pd.notnull(gapminder.year).all()
# Drop the missing values
gapminder = gapminder.dropna(axis=0, how='any')

# **************************************************************
# Add first subplot
plt.subplot(2, 1, 1)

# Create a histogram of life_expectancy
gapminder.life_expectancy.plot(kind='hist')

# Group gapminder: gapminder_agg
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot()

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()

# Save both DataFrames to csv files
# gapminder.to_csv('gapminder.csv')
# gapminder_agg.to_csv('gapminder_agg.csv')

"""
Output comment:
You've stepped through each stage of the data cleaning process and your data is now ready for serious analysis! Looking 
at the line plot, it seems like life expectancy has, as expected, increased over the years. There is a surprising dip 
around 1920 that may be worth further investigation!
"""