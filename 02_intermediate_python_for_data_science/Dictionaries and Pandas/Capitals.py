"""
Dictionaries
Examples of basic operations on dictionaries
"""

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'bonn', 'norway': 'oslo', 'australia': 'vienna'}

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Add italy to europe
europe['italy'] = 'rome'

# Check if italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)
