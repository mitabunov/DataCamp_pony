"""
Daily hours of clear sky:
In a previous exercise, you analyzed the 'sky_condition' column to explore the difference in temperature on sunny days
compared to overcast days. Recall that a 'sky_condition' of 'CLR' represents a sunny day. In this exercise, you will
explore sunny days in greater detail. Specifically, you will use a box plot to visualize the fraction of days that are
sunny.

The 'sky_condition' column is recorded hourly. Your job is to resample this column appropriately such that you can
extract the number of sunny hours in a day and the number of total hours. Then, you can divide the number of sunny hours
by the number of total hours, and generate a box plot of the resulting fraction.
"""

# Import pandas and matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data file: df_clean
df_clean = pd.read_csv('../_datasets/NOAA_QCLCD_2011_clean.txt', index_col=[0])
# Convert the index to datetime: date_times
df_clean.index = pd.to_datetime(df_clean.index)

"""
Instructions 1/3:
*   Get the cases in df_clean where the sky is clear. That is, when 'sky_condition' equals 'CLR', assigning to 
    is_sky_clear.
*   Resample is_sky_clear by day, assigning to resampled.
"""

# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = df_clean['sky_condition']=='CLR'
# Resample is_sky_clear by day
resampled = is_sky_clear.resample('D')
# See the result
print(resampled)

"""
Instructions 2/3:
*   Calculate the number of measured sunny hours per day as the sum of resampled, assigning to sunny_hours.
*   Calculate the total number of measured hours per day as the count of resampled, assigning to total_hours.
*   Calculate the fraction of hours per day that were sunny as the ratio of sunny hours to total hours.
"""

# Calculate the number of sunny hours per day
sunny_hours = resampled.sum()
# Calculate the number of measured hours per day
total_hours = df_clean['sky_condition'].resample('D').count()
# Calculate the fraction of hours per day that were sunny
sunny_fraction = sunny_hours/total_hours
print(sunny_fraction.head())

"""
Instructions 3/3:
*   Draw a box plot of sunny_fraction using .plot() with kind set to `'box'``.
"""

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind='box')
plt.show()
