"""
Generator expressions:
Generator expressions basically have the same syntax as list comprehensions, except that it uses parentheses () instead
of brackets []. Furthermore, if you have ever iterated over a dictionary with .items(), or used the range() function,
for example, you have already encountered and used generators before, without knowing it! When you use these functions,
Python creates generators for you behind the scenes.
"""

"""
1. Create a generator object that produces numeric values.
"""

# Create generator object: result
result = (num for num in range(0, 31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

print(50*'*')
# Print the rest of the values
for value in result:
    print(value)

print(50*'*')
""" 
2. You are given a list of strings lannister and, using a generator expression, create a generator object that you will 
iterate over to print its values.
"""

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)
