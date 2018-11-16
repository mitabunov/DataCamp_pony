"""
Separating and resampling:
With pandas, you can resample in different ways on different subsets of your data. For example, resampling different
months of data with different aggregations. In this exercise, the data set containing hourly temperature data from the
last exercise has been pre-loaded.

Your job is to resample the data using a variety of aggregation methods. The DataFrame is available in the workspace as
df. You will be working with the 'Temperature' column.

Instructions:
*   Use partial string indexing to extract temperature data for August 2010 into august.
*   Use the temperature data for August and downsample to find the daily maximum temperatures. Store the result in
    august_highs.
*   Use partial string indexing to extract temperature data for February 2010 into february.
*   Use the temperature data for February and downsample to find the daily minimum temperatures. Store the result in
    february_lows.
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

# Extract temperature data for August: august
august = df['Temperature'].loc['2010-08']
print('*** august ***')
print(august)

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()
print('*** august_highs***')
print(august_highs)

# Extract temperature data for February: february
february = df['Temperature'].loc['2010-02']
print('*** february ***')
print(february)

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()
print('*** february_lows ***')
print(february_lows)
