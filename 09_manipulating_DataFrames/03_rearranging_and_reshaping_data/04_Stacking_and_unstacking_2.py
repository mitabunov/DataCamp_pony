"""
Stacking & unstacking II:
You are now going to continue working with the users DataFrame. As always, first explore it in the IPython Shell to see
the layout and note the index.

Your job in this exercise is to unstack and then stack the 'city' level, as you did previously for 'weekday'. Note that
you won't get the same DataFrame.

Instructions:
*   Define a DataFrame bycity with the 'city' level of users unstacked.
*   Print the bycity DataFrame to see the new data layout. This has been done for you.
*   Stack bycity by 'city' and print it to check if you get the same layout as the original users DataFrame.
"""


import pandas as pd
# Import users, set index to city and weekday, and sort index
users = pd.read_csv('../_datasets/users.csv', index_col=0)
users = users.set_index(['city', 'weekday']).sort_index()
print(users.head())
print(50*'-')
print(50*'-')
# *******************************************************

# Unstack users by 'city': bycity
bycity = users.unstack(level='city')
# Print the bycity DataFrame
print(bycity)
print(50*'-')
# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))
