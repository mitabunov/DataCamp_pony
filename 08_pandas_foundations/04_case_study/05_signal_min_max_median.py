"""
Signal min, max, median:
Now that you have the data read and cleaned, you can begin with statistical EDA. First, you will analyze the 2011 Austin
weather data.

Your job in this exercise is to analyze the 'dry_bulb_faren' column and print the median temperatures for specific time
ranges. You can do this using partial datetime string selection.

The cleaned dataframe is provided in the workspace as df_clean.

Instructions:
*   Select the 'dry_bulb_faren' column and print the output of .median().
*   Use .loc[] to select the range '2011-Apr':'2011-Jun' from dry_bulb_faren' and print the output of .median().
*   Use .loc[] to select the month '2011-Jan' from 'dry_bulb_faren' and print the output of .median().
"""


# Import pandas
import pandas as pd
# Read in the data file: df
df_clean = pd.read_csv('../_datasets/NOAA_QCLCD_2011_clean.txt', index_col=[0])
# Convert the index to datetime: date_times
df_clean.index = pd.to_datetime(df_clean.index)
# ****************************************************************

# Print the median of the dry_bulb_faren column
print(df_clean['dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the time range '2011-Apr':'2011-Jun'
print(df_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(df_clean.loc['2011-Jan', 'dry_bulb_faren'].median())
