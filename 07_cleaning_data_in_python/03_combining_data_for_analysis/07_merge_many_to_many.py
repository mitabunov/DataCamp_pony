"""
Many-to-many data merge
The final merging scenario occurs when both DataFrames do not have unique keys for a merge. What happens here is that
for each duplicated key, every pairwise combination will be created.

Two example DataFrames that share common key values have been pre-loaded: df1 and df2. Another DataFrame df3, which is
the result of df1 merged with df2, has been pre-loaded. All three DataFrames have been printed - look at the output and
notice how pairwise combinations have been created. This example is to help you develop your intuition for many-to-many
merges.

Here, you'll work with the site and visited DataFrames from before, and a new survey DataFrame. Your task is to merge
site and visited as you did in the earlier exercises. You will then merge this merged DataFrame with survey.

Begin by exploring the site, visited, and survey DataFrames in the IPython Shell.

INSTRUCTIONS:
*   Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did
    in the previous two exercises. Save the result as m2m.
*   Merge the m2m and survey DataFrames on the 'ident' column of m2m and 'taken' column of survey.
*   Hit 'Submit Answer' to print the first 20 lines of the merged DataFrame!
"""


import pandas as pd

# DataFrames preparation
name = ['DR-1', 'DR-3', 'MSK-4']
lat = [-49.85, -47.15, -48.87]
long = [-128.57, -126.72, -123.40]
ident = [619, 622, 734, 735, 751, 752, 837, 844]
name2 = ['DR-1', 'DR-1', 'DR-3', 'DR-3', 'DR-3', 'DR-3', 'MSK-4', 'DR-1']
dated = ['1927-02-08', '1927-02-10', '1939-01-07', '1930-01-12', '1930-02-26', 'NaN', '1932-01-14', '1932-03-22']
taken = [619, 619, 622, 622, 734, 734, 734, 735, 735, 735, 751, 751, 751, 752, 752, 752, 752, 837, 837, 837, 844]
person = ['dyer', 'dyer', 'dyer', 'dyer', 'pb', 'lake', 'pb', 'pb', 'NaN', 'NaN', 'pb', 'pb', 'lake', 'lake', 'lake',
          'lake', 'roe', 'lake', 'lake', 'roe', 'roe']
quant = ['rad', 'sal', 'rad', 'sal', 'rad', 'sal', 'temp', 'rad', 'sal', 'temp', 'rad', 'temp', 'sal', 'rad', 'sal',
         'temp', 'sal', 'rad', 'sal', 'sal', 'rad']
reading = [9.82, 0.13, 7.80, 0.09, 8.41, 0.05, -21.50, 7.22, 0.06, -26.00, 4.35, -18.5, 0.1, 2.19, 0.09, -16, 41.6,
           1.46, 0.21, 22.50, 11.25]

dict_site = {'name': name, 'lat': lat, 'long': long}
dict_visited = {'ident': ident, 'site': name2, 'dated': dated}
dict_survey = {'taken': taken, 'person': person, 'quant': quant, 'reading': reading}

site = pd.DataFrame(dict_site)
visited = pd.DataFrame(dict_visited)
survey = pd.DataFrame(dict_survey)

# *****************************************
# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on="name", right_on='site')

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))

"""
Output comment:
Notice how the keys are duplicated in this many-to-many merge!
"""