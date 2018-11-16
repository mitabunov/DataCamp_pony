"""
Resample and roll with it:
As of pandas version 0.18.0, the interface for applying rolling transformations to time series has become more
consistent and flexible, and feels somewhat like a groupby (If you do not know what a groupby is, don't worry, you will
learn about it in the next course!).

You can now flexibly chain together resampling and rolling operations. In this exercise, the same weather data from the
previous exercises has been pre-loaded for you. Your job is to extract one month of data, resample to find the daily
high temperatures, and then use a rolling and aggregation operation to smooth the data.

Instructions:
*   Use partial string indexing to extract August 2010 temperature data, and assign to august.
*   Resample to daily frequency, saving the maximum daily temperatures, and assign the result to daily_highs.
*   As part of one long method chain, repeat the above resampling (or you can re-use daily_highs) and then combine it
    with .rolling() to apply a 7 day .mean() (with window=7 inside .rolling()) so as to smooth the daily highs. Assign
    the result to daily_highs_smoothed and print the result.
"""


import pandas as pd

# Load dataframe
df = pd.read_csv('../_datasets/weather_data_austin_2010.csv')
# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'
# Convert date_list into a datetime object: my_datetimes
df['Date'] = pd.to_datetime(df['Date'], format=time_format)
# Set Date as index
df.set_index('Date', inplace=True)
# ************************************

# Extract the August 2010 data: august
august = df['Temperature']['2010-08']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)

