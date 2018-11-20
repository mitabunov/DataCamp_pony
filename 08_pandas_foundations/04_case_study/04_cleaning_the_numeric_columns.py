"""
Cleaning the numeric columns:
The numeric columns contain missing values labeled as 'M'. In this exercise, your job is to transform these columns such
that they contain only numeric values and interpret missing data as NaN.

The pandas function pd.to_numeric() is ideal for this purpose: It converts a Series of values to floating-point values.
Furthermore, by specifying the keyword argument errors='coerce', you can force strings like 'M' to be interpreted as
NaN.

A DataFrame df_clean is provided for you at the start of the exercise, and as usual, pandas has been imported as pd.

Instructions:
*   Print the 'dry_bulb_faren' temperature between 8 AM and 9 AM on June 20, 2011.
*   Convert the 'dry_bulb_faren' column to numeric values with pd.to_numeric(). Specify errors='coerce'.
*   Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011.
*   Convert the 'wind_speed' and 'dew_point_faren' columns to numeric values with pd.to_numeric(). Again, specify
    errors='coerce'.
"""


# Import pandas
import pandas as pd
# Read in the data file: df
df_dropped = pd.read_csv('../_datasets/NOAA_QCLCD_2011_dropped.txt')

# Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped['date'].astype(str)
# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x: '{:0>4}'.format(x))
# Concatenate the new date and Time columns: date_string
date_string = df_dropped['date']+df_dropped['Time']
# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')
# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)
# ************************************************

# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-06-20 08:00':'2011-06-20 09:00', 'dry_bulb_faren'])

# Convert the dry_bulb_faren column to numeric values: df_clean['dry_bulb_faren']
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')

# Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-06-20 08:00':'2011-06-20 09:00', 'dry_bulb_faren'])

# Convert the wind_speed and dew_point_faren columns to numeric values
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'], errors='coerce')

df_clean.to_csv('../_datasets/NOAA_QCLCD_2011_clean.txt')
