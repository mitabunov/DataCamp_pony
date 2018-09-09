"""
Extended version of the Next step game, contains repeated simulation with result recording.

Clumsiness rule:
There is a 0.1% chance of falling down.
Generate a random float between 0 and 1.
If this value is less than or equal to 0.001, reset step to 0.
"""

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(111)
all_walks = []                                      # Initialize all_walks
simulations = 500

for i in range(simulations):                        # Simulate random walk 500 times
    random_walk = [0]                               # Generate a list with the starting point
    for x in range(100):
        step = random_walk[-1]                      # Set step: last element in random_walk
        dice = np.random.randint(1, 7)              # Throw a dice
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001:               # Implement clumsiness
            step = 0
        random_walk.append(step)                    # Append result to the random_walk list
    all_walks.append(random_walk)                   # Append random_walk to all_walks

np_aw_t = np.transpose(np.array(all_walks))         # Convert all_walks to Numpy array: np_aw. Transpose for clearance

ends = np_aw_t[-1]                                  # Select last row from np_aw_t: ends
reach = ends[ends >= 60]                            # All successful results
win_percent = len(reach)/simulations*100            # Chance of winning the bet in %

print('There is {0} successful results out of {1} simulations.'.format(len(reach), simulations))
print('The chance of winning the bet is {0:.2f} %.'.format(win_percent))

plt.hist(ends)                                      # Plot histogram of ends, display plot
plt.show()
