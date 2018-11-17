"""
Missing values and interpolation:
One common application of interpolation in data analysis is to fill in missing data.

In this exercise, noisy measured data that has some dropped or otherwise missing values has been loaded. The goal is to
compare two time series, and then look at summary statistics of the differences. The problem is that one of the data
sets is missing data at some of the times. The pre-loaded data ts1 has value for all times, yet the data set ts2 does
not: it is missing data for the weekends.

Your job is to first interpolate to fill in the data for all days. Then, compute the differences between the two data
sets, now that they both have full support for all times. Finally, generate the summary statistics that describe the
distribution of differences.

Instructions:
*   Replace the index of ts2 with that of ts1, and then fill in the missing values of ts2 by using
    .interpolate(how='linear'). Save the result as ts2_interp.
*   Compute the difference between ts1 and ts2_interp. Take the absolute value of the difference with np.abs(), and
    assign the result to differences.
*   Generate and print summary statistics of the differences with .describe() and print().
"""


import pandas as pd
import numpy as np

# Prepare a dataframe1
days1 = ['20160701', '20160702', '20160703', '20160704', '20160705', '20160706', '20160707', '20160708', '20160709',
         '20160710', '20160711', '20160712', '20160713', '20160714', '20160715', '20160716', '20160717']
time_format = '%Y-%m-%d'
days1 = pd.to_datetime(days1, format=time_format)
value1 = [int(i) for i in range(17)]
ts1 = pd.Series(value1, index=days1)

# Prepare a dataframe2
days2 = ['20160701', '20160704', '20160705', '20160706', '20160707', '20160708', '20160711', '20160712', '20160713',
         '20160714', '20160715']
time_format = '%Y-%m-%d'
days2 = pd.to_datetime(days2, format=time_format)
value2 = [int(i) for i in range(11)]
ts2 = pd.Series(value2, index=days2)

# *****************************

# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

# Compute the absolute difference of ts1 and ts2_interp: differences
differences = np.abs(ts1 - ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())
