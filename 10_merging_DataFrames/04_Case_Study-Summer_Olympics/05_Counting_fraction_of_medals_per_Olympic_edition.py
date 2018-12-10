"""
Computing fraction of medals per Olympic edition:
In this exercise, you'll start with the DataFrames editions, medals, & medal_counts from prior exercises.

You can extract a Series with the total number of medals awarded in each Olympic edition.

The DataFrame medal_counts can be divided row-wise by the total number of medals awarded each edition; the method
.divide() performs the broadcast as you require.

This gives you a normalized indication of each country's performance in each edition.

Instructions:
*   Set the index of the DataFrame editions to be 'Edition' (using the method .set_index()). Save the result as totals.
*   Extract the 'Grand Total' column from totals and assign the result back to totals.
*   Divide the DataFrame medal_counts by totals along each row. You will have to use the .divide() method with the
    option axis='rows'. Assign the result to fractions.
*   Print first & last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the
    results!
"""


import pandas as pd

# Load All Medalists data 'generated' in previous exercise by concatenating DataFrames for each edition
medals_file_path = '../_datasets/Summer_Olympics/Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.tsv'
medals = pd.read_csv(medals_file_path, skiprows=4, sep='\t')
medals = medals[['Athlete', 'NOC', 'Medal', 'Edition']]
print(medals.head())
print(50*'=')
# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index='Edition', values='Athlete', aggfunc='count', columns='NOC')
print(medal_counts.head())
print(50*'=')
# Load editions
editions_file_path = '../_datasets/Summer_Olympics/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'
editions = pd.read_csv(editions_file_path, sep='\t')
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]
print(editions.head())
print(50*'=')
# *****************************************************

# Set Index of editions: totals
totals = editions.set_index('Edition')
# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']
# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals, axis='rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())
