"""
Reshaping for analysis:
This exercise starts off with fractions_change and hosts already loaded.

Your task here is to reshape the fractions_change DataFrame for later analysis.

Initially, fractions_change is a wide DataFrame of 26 rows (one for each Olympic edition) and 139 columns (one for the
edition and 138 for the competing countries).

On reshaping with pd.melt(), as you will see, the result is a tall DataFrame with 3588 rows and 3 columns that
summarizes the fractional change in the expanding mean of the percentage of medals won for each country in blocks.

Instructions:
*   Create a DataFrame reshaped by reshaping the DataFrame fractions_change with pd.melt().
*   You'll need to use the keyword argument id_vars='Edition' to set the identifier variable.
*   You'll also need to use the keyword argument value_name='Change' to set the measured variables.
*   Print the shape of the DataFrames reshaped and fractions_change. This has been done for you.
*   Create a DataFrame chn by extracting all the rows from reshaped in which the three letter code for each country
    ('NOC') is 'CHN'.
*   Print the last 5 rows of the DataFrame chn using the .tail() method. This has been done for you, so hit 'Submit
    Answer' to see the results!
"""


import pandas as pd

# Load All Medalists data 'generated' in previous exercise by concatenating DataFrames for each edition
medals_file_path = '../_datasets/Summer_Olympics/Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.tsv'
medals = pd.read_csv(medals_file_path, skiprows=4, sep='\t')
medals = medals[['Athlete', 'NOC', 'Medal', 'Edition']]
# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index='Edition', values='Athlete', aggfunc='count', columns='NOC')
# Load editions
editions_file_path = '../_datasets/Summer_Olympics/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'
editions = pd.read_csv(editions_file_path, sep='\t')
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]
# Set fractions
totals = editions.set_index('Edition')
totals = totals['Grand Total']
fractions = medal_counts.divide(totals, axis='rows')
# Set fractions_change
mean_fractions = fractions.expanding().mean()
fractions_change = mean_fractions.pct_change()*100
fractions_change = fractions_change.reset_index()
# *****************************************************

# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')
# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)
# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped[reshaped['NOC'] == 'CHN']
# Print last 5 rows of chn with .tail()
print(chn.tail())

# Save reshaped to csv
reshaped.to_csv('../_datasets/Summer_Olympics/reshaped.csv', index=False)