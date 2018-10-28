"""
Many-to-1 data merge:
In a many-to-one (or one-to-many) merge, one of the values will be duplicated and recycled in the output. That is, one
of the keys in the merge is not unique.

Here, the two DataFrames site and visited have been pre-loaded once again. Note that this time, visited has multiple
entries for the site column. Confirm this by exploring it in the IPython Shell.

The .merge() method call is the same as the 1-to-1 merge from the previous exercise, but the data and output will be
different.

INSTRUCTIONS:
*   Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did
    in the previous exercise.
*   Print the merged DataFrame and then hit 'Submit Answer' to see the different output produced by this merge!
"""


import pandas as pd

# DataFrames preparation
name = ['DR-1', 'DR-3', 'MSK-4']
lat = [-49.85, -47.15, -48.87]
long = [-128.57, -126.72, -123.40]
ident = [619, 622, 734, 735, 751, 752, 837, 844]
name2 = ['DR-1', 'DR-1', 'DR-3', 'DR-3', 'DR-3', 'DR-3', 'MSK-4', 'DR-1']
dated = ['1927-02-08', '1927-02-10', '1939-01-07', '1930-01-12', '1930-02-26', 'NaN', '1932-01-14', '1932-03-22']

dict_site = {'name': name, 'lat': lat, 'long': long}
dict_visited = {'ident': ident, 'site': name2, 'dated': dated}

site = pd.DataFrame(dict_site)
visited = pd.DataFrame(dict_visited)

# *****************************************
# Merge the DataFrames: m2o
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print m2o
print(m2o)

print('\n*** Files before merge:')
print(site)
print(visited)

"""
Output comment:
Notice how the site data is duplicated during this many-to-1 merge!
"""