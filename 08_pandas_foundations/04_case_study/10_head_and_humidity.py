"""
Heat or humidity
Dew point is a measure of relative humidity based on pressure and temperature. A dew point above 65 is considered
uncomfortable while a temperature above 90 is also considered uncomfortable.

In this exercise, you will explore the maximum temperature and dew point of each month. The columns of interest are
'dew_point_faren' and 'dry_bulb_faren'. After resampling them appropriately to get the maximum temperature and dew point
in each month, generate a histogram of these values as subplots. Uncomfortably, you will notice that the maximum dew
point is above 65 every month!
"""

# Import pandas and matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data file: df_clean
df_clean = pd.read_csv('../_datasets/NOAA_QCLCD_2011_clean.txt', index_col=[0])
# Convert the index to datetime: date_times
df_clean.index = pd.to_datetime(df_clean.index)

"""
Instructions:
*   Select the 'dew_point_faren' and 'dry_bulb_faren' columns (in that order). Resample by month and aggregate the 
    maximum monthly temperatures. Assign the result to monthly_max.
*   Plot a histogram of the resampled data with bins=8, alpha=0.5, and subplots=True.
"""

# Resample dew_point_faren and dry_bulb_faren by Month, aggregating the maximum values: monthly_max
monthly_max = df_clean[['dew_point_faren', 'dry_bulb_faren']].resample('M').max()

# Generate a histogram with bins=8, alpha=0.5, subplots=True
monthly_max.plot(kind='hist', bins=8, alpha=0.5, subplots=True)

# Show the plot
plt.show()
