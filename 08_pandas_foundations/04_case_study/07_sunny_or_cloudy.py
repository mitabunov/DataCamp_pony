"""
Sunny or cloudy
On average, how much hotter is it when the sun is shining? In this exercise, you will compare temperatures on sunny days
against temperatures on overcast days.

Your job is to use Boolean selection to filter out sunny and overcast days, and then compute the difference of the mean
daily maximum temperatures between each type of day.

The DataFrame df_clean from previous exercises has been provided for you. The column 'sky_condition' provides
information about whether the day was sunny ('CLR') or overcast ('OVC').
"""

# Import pandas
import pandas as pd

# Read in the data file: df_clean
df_clean = pd.read_csv('../_datasets/NOAA_QCLCD_2011_clean.txt', index_col=[0])
# Convert the index to datetime: date_times
df_clean.index = pd.to_datetime(df_clean.index)
df_clean = df_clean.drop(columns=['date', 'Time'])
# ****************************************************************

"""
Instructions 1/3:
*   Calculate the mean of sunny_daily_max, assigning to sunny_daily_max_mean.
*   Calculate the mean of overcast_daily_max, assigning to overcast_daily_max_mean.
*   Print sunny_daily_max_mean minus overcast_daily_max_mean. How much hotter are sunny days?
"""

# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = df_clean['sky_condition']=='CLR'
# Filter df_clean using is_sky_clear
sunny = df_clean.loc[is_sky_clear]
# Resample sunny by day then calculate the max
sunny_daily_max = sunny.resample('D').max()
# See the result
print(sunny_daily_max.head())

"""
Instructions 2/3:
*   Get the cases in df_clean where the sky is overcast. Using .str.contains(), find when 'sky_condition' contains 
    'OVC', assigning to is_sky_overcast.
*   Use .loc[] to filter df_clean by is_sky_overcast, assigning to overcast.
*   Resample overcast by day ('D'), and take the max to find the maximum daily temperature.
"""

# Using df_clean, when does sky_condition contain 'OVC'?
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')
# Filter df_clean using is_sky_overcast
overcast = df_clean[is_sky_overcast]
# Resample overcast by day then calculate the max
overcast_daily_max = overcast.resample('D').max()
# See the result
print(overcast_daily_max.head())

"""
Instructions 3/3:
*   Calculate the mean of sunny_daily_max, assigning to sunny_daily_max_mean.
*   Calculate the mean of overcast_daily_max, assigning to overcast_daily_max_mean.
*   Print sunny_daily_max_mean minus overcast_daily_max_mean. How much hotter are sunny days?
"""

# Calculate the mean of sunny_daily_max
sunny_daily_max_mean = sunny_daily_max.mean()
# Calculate the mean of overcast_daily_max
overcast_daily_max_mean = overcast_daily_max.mean()
# Print the difference (sunny minus overcast)
print(sunny_daily_max_mean - overcast_daily_max_mean)
