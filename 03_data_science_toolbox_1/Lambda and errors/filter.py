"""
Filter() and lambda functions:
The function filter() offers a way to filter out elements from a list that don't satisfy certain criteria.
Create, from an input list of strings, a new list that contains only strings that have more than 6 characters.
"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member)>6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)
