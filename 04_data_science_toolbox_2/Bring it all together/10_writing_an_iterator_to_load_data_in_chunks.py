"""
Writing an iterator to load data in chunks (3):
Add a column to a DataFrame.

Starting from the code of the previous exercise, use a list comprehension to create the values for a new column
'Total Urban Population' from the list of tuples that you generated earlier. Recall from the previous exercise that the
first and second elements of each tuple consist of, respectively, values from the columns 'Total Population' and
'Urban population (% of total)'. The values in this new column 'Total Urban Population', therefore, are the product of
the first and second element in each tuple. Furthermore, because the 2nd element is a percentage, you need to divide the
entire result by 100, or alternatively, multiply it by 0.01.

Also plot the data from this new column to create a visualization of the urban population data.

INSTRUCTIONS:
- Write a list comprehension to generate a list of values from pops_list for the new column 'Total Urban Population'.
The output expression should be the product of the first and second element in each tuple in pops_list. Because the 2nd
element is a percentage, you also need to either multiply the result by 0.01 or divide it by 100. In addition, note that
the column 'Total Urban Population' should only be able to take on integer values. To ensure this, make sure you cast
the output expression to an integer with int().
- Create a scatter plot where the x-axis are values from the 'Year' column and the y-axis are values from the 'Total
Urban Population' column.
"""


# Import the pandas package
import pandas as pd
import matplotlib.pyplot as plt

# Code from previous exercise
urb_pop_reader = pd.read_csv(r'../_datasets/world_ind_pop.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'],
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(pop[0]*pop[1]*0.01) for pop in pops_list]

print(df_pop_ceb.head())
print(type(df_pop_ceb['Total Urban Population']))

# test = [(pop, urb) for pop in pops_list for urb in pops_list]
print(df_pop_ceb['Year'])
print(df_pop_ceb['Total Urban Population'])

# Plot urban population data
# df_pop_ceb.plot(kind='scatter', x=df_pop_ceb['Year'], y=df_pop_ceb['Total Urban Population'])
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

print(df_urb_pop.head())
