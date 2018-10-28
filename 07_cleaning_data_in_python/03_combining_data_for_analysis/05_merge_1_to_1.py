"""
1-to-1 data merge
Merging data allows you to combine disparate datasets into a single dataset to do more complex analysis.

Here, you'll be using survey data that contains readings that William Dyer, Frank Pabodie, and Valentina Roerich took in
the late 1920 and 1930 while they were on an expedition towards Antarctica. The dataset was taken from a sqlite database
from the Software Carpentry SQL lesson.

Two DataFrames have been pre-loaded: site and visited. Explore them in the IPython Shell and take note of their
structure and column names. Your task is to perform a 1-to-1 merge of these two DataFrames using the 'name' column of
site and the 'site' column of visited.

INSTRUCTIONS:
*   Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited.
*   Print the merged DataFrame o2o.
"""


import pandas as pd
# DataFrames preparation
name = ['DR-1', 'DR-3', 'MSK-4']
lat = [-49.85, -47.15, -48.87]
long = [-128.57, -126.72, -123.40]
ident = [619, 734, 837]
dated = ['1927-02-08', '1939-01-07', '1932-01-14']

dict_site = {'name': name, 'lat': lat, 'long':long}
dict_visited = {'ident': ident, 'site': name, 'dated':dated}

site = pd.DataFrame(dict_site)
visited = pd.DataFrame(dict_visited)

# ************************************

# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)

print('\n*** Files before merge:')
print(site)
print(visited)

"""
Output comment:
Notice the 1-to-1 correspondence between the name column of the site DataFrame and the site column of the visited 
DataFrame. This is what made the 1-to-1 merge possible.
"""