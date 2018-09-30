"""
Nested list comprehensions

One of the ways in which lists can be used are in representing multi-dimension objects such as matrices.
Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row
can be written as:

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

Recreate this matrix by using nested listed comprehensions.

To create the list of lists, you simply have to supply the list comprehension as the output expression of the overall
list comprehension:
[[OUTPUT EXPRESSION] for ITERATOR VARIABLE in ITERABLE]
"""

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for row in range(0, 5)]

# Print the matrix
for row in matrix:
    print(row)
