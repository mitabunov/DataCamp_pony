"""
Setting up a pivot table:
Recall from the video that a pivot table allows you to see all of your variables as a function of two other variables.
In this exercise, you will use the .pivot_table() method to see how the users DataFrame entries appear when presented as
functions of the 'weekday' and 'city' columns. That is, with the rows indexed by 'weekday' and the columns indexed by
'city'.

Before using the pivot table, print the users DataFrame in the IPython Shell and observe the layout.

Instructions:
*   Use a pivot table to index the rows of users by 'weekday' and the columns of users by 'city'. These correspond to
    the index and columns parameters of .pivot_table().
*   Print by_city_day. This has been done for you, so hit 'Submit Answer' to see the result.
"""


import pandas as pd
# Import users, set index to city and weekday, and sort index
users = pd.read_csv('../_datasets/users.csv', index_col=0)
print(users)
print(50*'-'+'\n'+50*'-')
# *************************************

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index='weekday', columns='city')
# Print by_city_day
print(by_city_day)
