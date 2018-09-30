"""
Using conditionals in comprehensions (1):

An interesting mechanism in list comprehensions is that you can also create lists with values that meet only a certain
condition. One way of doing this is by using conditionals on iterator variables.

You can apply a conditional statement to test the iterator variable by adding an if statement in the optional predicate
expression part after the for statement in the comprehension:

[ OUTPUT EXPRESSION for ITERATOR VARIABLE in ITERABLE if PREDICATE EXPRESSION ].

You are given a list of strings fellowship and, using a list comprehension, create a list that only includes the members
of fellowship that have 7 characters or more.
"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) in range(7, 50)]

# Print the new list
print(new_fellowship)

print(50*'*')

"""
Using a list comprehension and an if-else conditional statement in the output expression, create a list that keeps 
members of fellowship with 7 or more characters and replaces others with an empty string. 
"""

# Create list comprehension: new_fellowship
new_fellowship_2 = [member if len(member) >= len(range(7)) else '' for member in fellowship]

# Print the new list
print(new_fellowship_2)
