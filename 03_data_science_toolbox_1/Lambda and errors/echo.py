"""
The function echo_word takes 2 parameters: a string value, word1 and an integer value, echo.
It returns a string that is a concatenation of echo copies of word1.
"""

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1*echo)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)
