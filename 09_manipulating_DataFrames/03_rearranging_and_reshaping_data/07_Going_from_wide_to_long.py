"""
Going from wide to long:
You can move multiple columns into a single column (making the data long and skinny) by "melting" multiple columns. In
this exercise, you will practice doing this.

The users DataFrame has been pre-loaded for you. As always, explore it in the IPython Shell and note the index.

Instructions:
*   Define a DataFrame skinny where you melt the 'visitors' and 'signups' columns of users into a single column.
*   Print skinny to verify the results. Note the value column that had the cell values in users.
"""

import pandas as pd
# Import users, set index to city and weekday, and sort index
users = pd.read_csv('../_datasets/users.csv', index_col=0)
print(users)
print(50*'-'+'\n'+50*'-')
# *************************************

# Melt users: skinny
skinny = pd.melt(users, id_vars=['weekday', 'city'])
# Print skinny
print(skinny)
