"""
Using zip:
Zip(), takes any number of iterables and returns a zip object that is an iterator of tuples.
To print the values of a zip object, convert it into a list and then print it.
Printing just a zip object will not return the values unless you unpack it first.

Three lists of strings are pre-loaded: mutants, aliases, and powers.
First, you will use list() and zip() on these lists to generate a list of tuples.
Then, you will create a zip object using zip().
Finally, you will unpack this zip object in a for loop to print the values in each tuple. Observe the different output
generated by printing the list of tuples, then the zip object, and finally, the tuple values in the for loop.
"""

# Provided lists
mutants = ['charles xavier', 'bobby drake',
           'kurt wagner', 'max eisenhardt', 'kitty pride']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis',
          'teleportation', 'magnetokinesis', 'intangibility']

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

