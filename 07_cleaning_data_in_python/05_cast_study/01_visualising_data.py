"""
Visualizing your data:
Since 1800, life expectancy around the globe has been steadily going up. You would expect the Gapminder data to confirm
this.

The DataFrame g1800s has been pre-loaded. Your job in this exercise is to create a scatter plot with life expectancy in
'1800' on the x-axis and life expectancy in '1899' on the y-axis.

Here, the goal is to visually check the data for insights as well as errors. When looking at the plot, pay attention to
whether the scatter plot takes the form of a diagonal line, and which points fall below or above the diagonal line. This
will inform how life expectancy in 1899 changed (or did not change) compared to 1800 for different countries. If points
fall on a diagonal line, it means that life expectancy remained the same!

INSTRUCTIONS:
*   Import matplotlib.pyplot as plt.
*   Use the .plot() method on g1800s with kind='scatter' to create a scatter plot with '1800' on the x-axis and '1899' on the y-axis.
*   Display the plot.
"""


# Import matplotlib.pyplot
import matplotlib.pyplot as plt
import pandas as pd

g1800s = pd.read_csv('../_datasets/g1800.csv', delimiter=',')

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()

"""
Output comment:
As you can see, there are a surprising number of countries that fall on the diagonal line. In fact, examining the 
DataFrame reveals that the life expectancy for 140 of the 260 countries did not change at all in the 19th century! This 
is possibly a result of not having access to the data for all the years back then. In this way, visualizing your data 
can help you uncover insights as well as diagnose it for errors.
"""