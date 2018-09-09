"""
Next step is a game simulation of walking up the stairs from 0 to 60 steps according to dice throw results:
1   move one step down
2-5 move one step up
6   throw again a move up, as many steps as the new result on dice

The bet is to reach the 60th step in 100 turns.

The game is fixed with random seed. Change the value to receive different results
"""

# Initialization
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1211)
random_walk = [0]                               # a list with the starting point

for x in range(100):
    step = random_walk[-1]                      # Set step: last element in random_walk
    dice = np.random.randint(1, 7)              # dice throw

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    random_walk.append(step)                    # append result to the random_walk list


plt.plot(random_walk)                           # plot random_walk
plt.grid()
plt.show()                                      # show the plot
