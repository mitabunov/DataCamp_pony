"""
Merging to compute influence:
This exercise starts off with the DataFrames reshaped and hosts in the namespace.

Your task is to merge the two DataFrames and tidy the result.

The end result is a DataFrame summarizing the fractional change in the expanding mean of the percentage of medals won for the host country in each Olympic edition.

Instructions:
*   Merge reshaped and hosts using an inner join. Remember, how='inner' is the default behavior for pd.merge().
*   Print the first 5 rows of the DataFrame merged. This has been done for you. You should see that the rows are jumbled
    chronologically.
*   Set the index of merged to be 'Edition' and sort the index.
*   Print the first 5 rows of the DataFrame influence. This has been done for you, so hit 'Submit Answer' to see the
    results!
"""

import pandas as pd
# import hosts and reshaped
hosts = pd.read_csv('../_datasets/Summer_Olympics/hosts.csv')
reshaped = pd.read_csv('../_datasets/Summer_Olympics/reshaped.csv')
# *****************************************************************

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped, hosts, how='inner')
# Print first 5 rows of merged
print(merged.head())
print(40*'-')
# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()
# Print first 5 rows of influence
print(influence.head())
