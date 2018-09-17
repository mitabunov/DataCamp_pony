"""
Iterating over iterables (1):
Iterate over and printing from iterables and iterators.

You are provided with a list of strings flash.
You will practice iterating over the list by using a for loop.
You will also create an iterator for the list and access the values from the iterator.
"""

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)

print(20*'*')

# Create an iterator for flash: superspeed
superspeed = iter(flash)

# Print each item from the iterator
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))

print(20*'*')
print(20*'*')

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

print(20*'*')

# Loop over range(3) and print the values
for num in range(3):
    print(num)

print(20*'*')

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10**100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
