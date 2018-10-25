"""
Combining columns of data:
Think of column-wise concatenation of data as stitching data together from the sides instead of the top and bottom. To
perform this action, you use the same pd.concat() function, but this time with the keyword argument axis=1. The default,
axis=0, is for a row-wise concatenation.

You'll return to the Ebola dataset (https://data.humdata.org/dataset/ebola-cases-2014) you worked with briefly in the
last chapter. It has been pre-loaded into a DataFrame called ebola_melt. In this DataFrame, the status and country of a
patient is contained in a single column. This column has been parsed into a new DataFrame, status_country, where there
are separate columns for status and country.

Explore the ebola_melt and status_country DataFrames in the IPython Shell. Your job is to concatenate them column-wise
in order to obtain a final, clean DataFrame.

INSTRUCTIONS:
* Concatenate ebola_melt and status_country column-wise into a single DataFrame called ebola_tidy. Be sure to specify
  axis=1 and to pass the two DataFrames in as a list.
* Print the shape and then the head of the concatenated DataFrame, ebola_tidy.
"""

import pandas as pd
ebola = pd.read_csv('../_datasets/ebola.csv')

# Melt ebola: ebola_melt
# Based on the example 7 from chapter 2
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')
# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)
# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Create status_country from ebola and remove copied columns
status_country = ebola_melt[['type', 'country']].copy()
ebola_melt = ebola_melt.drop(['str_split', 'type', 'country'], axis=1)
print(ebola_melt.head())
print(status_country.head())
print(50*'*')

# *****************************************
# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())
