"""
Using other aggregations in pivot tables:
You can also use aggregation functions within a pivot table by specifying the aggfunc parameter. In this exercise, you
will practice using the 'count' and len aggregation functions - which produce the same result - on the users DataFrame.

Instructions:
*   Define a DataFrame count_by_weekday1 that shows the count of each column with the parameter aggfunc='count'. The
    index here is 'weekday'.
*   Print count_by_weekday1. This has been done for you.
*   Replace aggfunc='count' with aggfunc=len and verify you obtain the same result.
"""


import pandas as pd
# Import users, set index to city and weekday, and sort index
users = pd.read_csv('../_datasets/users.csv', index_col=0)
print(users)
print(50*'-'+'\n'+50*'-')
# *************************************

# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index='weekday', aggfunc='count')
# Print count_by_weekday
print(count_by_weekday1)
# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = users.pivot_table(index='weekday', aggfunc=len)
# Verify that the same result is obtained
print(50*'=')
print(count_by_weekday1.equals(count_by_weekday2))
