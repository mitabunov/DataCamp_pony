"""
Resetting the index of a DataFrame:
After pivoting airquality_melt in the previous exercise, you didn't quite get back the original DataFrame.

What you got back instead was a pandas DataFrame with a hierarchical index (also known as a MultiIndex).

Hierarchical indexes are covered in depth in Manipulating DataFrames with pandas. In essence, they allow you to group
columns or rows by another variable - in this case, by 'Month' as well as 'Day'.

There's a very simple method you can use to get back the original DataFrame from the pivoted DataFrame: .reset_index().
Dan didn't show you how to use this method in the video, but you're now going to practice using it in this exercise to
get back the original DataFrame from airquality_pivot, which has been pre-loaded.

INSTRUCTIONS:
* Print the index of airquality_pivot by accessing its .index attribute. This has been done for you.
* Reset the index of airquality_pivot using its .reset_index() method.
* Print the new index of airquality_pivot.
* Print the head of airquality_pivot.
"""


import pandas as pd
airquality = pd.read_csv("../_datasets/airquality.csv")

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Pivot airquality_melt: airquality_pivot
airquality_pivot = pd.pivot_table(airquality_melt, index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())

# **********************************
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()

# Print the new index of airquality_pivot_reset
print(airquality_pivot_reset.index)

# Print the head of airquality_pivot_reset
print(airquality_pivot_reset.head())
