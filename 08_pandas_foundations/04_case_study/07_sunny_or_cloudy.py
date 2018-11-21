"""
Sunny or cloudy
On average, how much hotter is it when the sun is shining? In this exercise, you will compare temperatures on sunny days
against temperatures on overcast days.

Your job is to use Boolean selection to filter out sunny and overcast days, and then compute the difference of the mean
daily maximum temperatures between each type of day.

The DataFrame df_clean from previous exercises has been provided for you. The column 'sky_condition' provides
information about whether the day was sunny ('CLR') or overcast ('OVC').

Instructions:
*   Use .loc[] to select sunny days and assign to sunny. If 'sky_condition' equals 'CLR', then the day is sunny.
*   Use .loc[] to select overcast days and assign to overcast. If 'sky_condition' contains 'OVC', then the day is
    overcast.
*   Resample sunny and overcast and aggregate by the maximum (.max()) daily ('D') temperature. Assign to sunny_daily_max
    and overcast_daily_max.
*   Print the difference between the mean of sunny_daily_max and overcast_daily_max. This has already been done for you,
    so click 'Submit Answer' to view the result!
"""


# Import pandas
import pandas as pd

# Read in the data file: df_clean
df_clean = pd.read_csv('../_datasets/NOAA_QCLCD_2011_clean.txt', index_col=[0])
# Convert the index to datetime: date_times
df_clean.index = pd.to_datetime(df_clean.index)
df_clean = df_clean.drop(columns=['date', 'Time'])
# ****************************************************************

# Select days that are sunny: sunny
sunny = df_clean.loc[df_clean['sky_condition']=='CLR']

# Select days that are overcast: overcast
overcast = df_clean.loc[df_clean['sky_condition'].str.contains('OVC')]

# Resample sunny and overcast, aggregating by maximum daily temperature
sunny_daily_max = sunny.resample('D').max()
overcast_daily_max = overcast.resample('D').max()

# Print the difference between the mean of sunny_daily_max and overcast_daily_max
print(sunny_daily_max.mean() - overcast_daily_max.mean())