"""
Computing percentage change in fraction of medals won:
Here, you'll start with the DataFrames editions, medals, medal_counts, & fractions from prior exercises.

To see if there is a host country advantage, you first want to see how the fraction of medals won changes from edition
to edition.

The expanding mean provides a way to see this down each column. It is the value of the mean with all the data available
up to that point in time. If you are interested in learning more about pandas' expanding transformations, this section
of the pandas documentation has additional information.

Instructions:
*   Create mean_fractions by chaining the methods .expanding().mean() to fractions.
*   Compute the percentage change in mean_fractions down each column by applying .pct_change() and multiplying by 100.
    Assign the result to fractions_change.
*   Reset the index of fractions_change using the .reset_index() method. This will make 'Edition' an ordinary column.
*   Print the first and last 5 rows of the DataFrame fractions_change. This has been done for you, so hit 'Submit
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
# Set Index of editions: totals
totals = editions.set_index('Edition')
# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']
# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals, axis='rows')
# *****************************************************

# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()
# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change()*100
# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())
