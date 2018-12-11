"""
Building hosts DataFrame:
Your task here is to prepare a DataFrame hosts by left joining editions and ioc_codes.

Once created, you will subset the Edition and NOC columns and set Edition as the Index.

There are some missing NOC values; you will set those explicitly.

Finally, you'll reset the Index & print the final DataFrame.

Instructions:
*   Create the DataFrame hosts by doing a left join on DataFrames editions and ioc_codes (using pd.merge()).
*   Clean up hosts by subsetting and setting the Index.
    *   Extract the columns 'Edition' and 'NOC'.
    *   Set 'Edition' column as the Index.
*   Use the .loc[] accessor to find and assign the missing values to the 'NOC' column in hosts. This has been done for
    you.
*   Reset the index of hosts using .reset_index(), which you'll need to save as the hosts DataFrame.
*   Hit 'Submit Answer' to see what hosts looks like!
"""

import pandas as pd

# Load editions
editions_file_path = '../_datasets/Summer_Olympics/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'
editions = pd.read_csv(editions_file_path, sep='\t')
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Load IOC
IOC_file_path = '../_datasets/Summer_Olympics/Summer Olympic medalists 1896 to 2008 - IOC COUNTRY CODES.csv'
ioc_codes = pd.read_csv(IOC_file_path)
ioc_codes = ioc_codes[['Country', 'NOC']]

# ***************************************

# Left join editions and ioc_codes: hosts
hosts = editions.merge(ioc_codes, how='left')
# Extract relevant columns and set index: hosts
hosts = hosts[['Edition', 'NOC']].set_index('Edition')
# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()
# Print hosts
print(hosts)

# Save hosts
hosts.to_csv('../_datasets/Summer_Olympics/hosts.csv', index=False)
