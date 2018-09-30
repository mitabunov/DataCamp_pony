""" List comprehension """

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

# The list comprehension is [doc[0] for doc in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].
first_character = [doc[0] for doc in doctor]

print(first_character)
print(50*'*')

""" 
Writing list comprehension.
Write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9. 
Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, 
write a list comprehension that produces a list of numbers consisting of the squared values of i.
"""
squares = [i**2 for i in range(0,10)]
print(squares)
