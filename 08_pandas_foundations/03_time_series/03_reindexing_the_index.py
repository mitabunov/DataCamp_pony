"""
Reindexing the Index:
Reindexing is useful in preparation for adding or otherwise combining two time series data sets. To reindex the data, we
provide a new index and ask pandas to try and match the old data to the new index. If data is unavailable for one of the
new index dates or times, you must tell pandas how to fill it in. Otherwise, pandas will fill with NaN by default.

In this exercise, two time series data sets containing daily data have been pre-loaded for you, each indexed by dates.
The first, ts1, includes weekends, but the second, ts2, does not. The goal is to combine the two data sets in a sensible
way. Your job is to reindex the second data set so that it has weekends as well, and then add it to the first. When you
are done, it would be informative to inspect your results.

Instructions:
*   Create a new time series ts3 by reindexing ts2 with the index of ts1. To do this, call .reindex() on ts2 and pass in
    the index of ts1 (ts1.index).
*   Create another new time series, ts4, by calling the same .reindex() as above, but also specifiying a fill method,
    using the keyword argument method="ffill" to forward-fill values.
*   Add ts1 + ts2. Assign the result to sum12.
*   Add ts1 + ts3. Assign the result to sum13.
*   Add ts1 + ts4, Assign the result to sum14.
"""

import pandas as pd

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
# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)
print('ts3:')
print(ts3)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index, method='ffill')
print('ts4:')
print(ts4)

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2
print('sum12')
print(sum12)

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3
print('sum13')
print(sum13)

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4
print('sum14')
print(sum14)
