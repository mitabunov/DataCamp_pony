"""
Reduce() and lambda functions:
The reduce() function is useful for performing some computation on a list and, unlike map() and filter(),
returns a single value as a result. To use reduce(), you must import it from the functools module.
"""


# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1+item2, stark)

# Print the result
print(result)
