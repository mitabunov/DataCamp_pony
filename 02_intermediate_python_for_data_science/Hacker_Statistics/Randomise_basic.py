"""
In this exercise, you'll be using two functions from this package:

- seed(): sets the random seed, so that your results are the reproducible between simulations.
  As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
- rand(): if you don't specify any arguments, it generates a random float between 0 and 1.
- randint(), also a function of the random package, to generate integers randomly
"""

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(1234)
# Generate and print random float
print(np.random.rand())

print(50*'*')

# Use randint() to simulate a dice
print(np.random.randint(1,7))
# Use randint() again
print(np.random.randint(1,7))
