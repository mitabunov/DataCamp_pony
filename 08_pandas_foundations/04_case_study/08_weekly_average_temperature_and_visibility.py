"""
Weekly average temperature and visibility:
Is there a correlation between temperature and visibility? Let's find out.

In this exercise, your job is to plot the weekly average temperature and visibility as subplots. To do this, you need to
first select the appropriate columns and then resample by week, aggregating the mean.

In addition to creating the subplots, you will compute the Pearson correlation coefficient using .corr(). The Pearson
correlation coefficient, known also as Pearson's r, ranges from -1 (indicating total negative linear correlation) to 1
(indicating total positive linear correlation). A value close to 1 here would indicate that there is a strong
correlation between temperature and visibility.
"""

# Import pandas
import pandas as pd

# Read in the data file: df_clean
df_clean = pd.read_csv('../_datasets/NOAA_QCLCD_2011_clean.txt', index_col=[0])
# Convert the index to datetime: date_times
df_clean.index = pd.to_datetime(df_clean.index)

"""
Instructions:
*   Import matplotlib.pyplot as plt.
*   Select the 'visibility' and 'dry_bulb_faren' columns and resample them by week, aggregating the mean. Assign the
    result to weekly_mean.
*   Print the output of weekly_mean.corr().
*   Plot the weekly_mean dataframe with .plot(), specifying subplots=True.
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Change visibility type to numeric (otherwise resample will skip visibility)
df_clean.visibility = pd.to_numeric(df_clean['visibility'], errors='coerce')
# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
weekly_mean = df_clean[['visibility', 'dry_bulb_faren']].resample('W').mean()
# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()

