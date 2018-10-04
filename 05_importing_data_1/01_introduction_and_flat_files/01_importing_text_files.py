"""
Plain text files
Importing text file
- entire file
- line by line
"""

""" Importing entire text """
# Open a file: file
file = open(r'../_datasets/moby_dick.txt', 'r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

print(50*'*')
""" Importing text line by line """

# Read & print the first 3 lines
with open(r'../_datasets/moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
