"""
pandas line plots:
In the previous chapter, you saw that the .plot() method will place the Index values on the x-axis by default. In this
exercise, you'll practice making line plots with specific columns on the x and y axes.

You will work with a dataset consisting of monthly stock prices in 2015 for AAPL, GOOG, and IBM. The stock prices were
obtained from Yahoo Finance. Your job is to plot the 'Month' column on the x-axis and the AAPL and IBM prices on the
y-axis using a list of column names.

All necessary modules have been imported for you, and the DataFrame is available in the workspace as df. Explore it
using methods such as .head(), .info(), and .describe() to see the column names.

INSTRUCTIONS:
*   Create a list of y-axis column names called y_columns consisting of 'AAPL' and 'IBM'.
*   Generate a line plot with x='Month' and y=y_columns as inputs.
*   Give the plot a title of 'Monthly stock prices'.
*   Specify the y-axis label.
*   Display the plot.
"""


import pandas as pd
import matplotlib.pyplot as plt

Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
AAPL = [117.160004, 128.46000700000002, 124.43, 125.150002, 130.279999, 125.43, 121.300003, 112.760002, 110.300003,
        119.5, 118.300003, 105.260002]
GOOG = [534.5224450000002, 558.402511, 548.002468, 537.340027, 532.1099849999998, 520.51001, 625.6099849999998, 618.25,
        608.419983, 710.8099980000002, 742.599976, 758.880005]
IBM = [153.309998, 161.940002, 160.5, 171.28999299999995, 169.649994, 162.660004, 161.990005, 147.889999, 144.970001,
       140.080002, 139.419998, 137.619995]

data = {'Month': Month, 'AAPL': AAPL, 'GOOG': GOOG, 'IBM': IBM}
df = pd.DataFrame(data)

# ***************************************************************
# Create a list of y-axis column names: y_columns
y_columns = ['AAPL', 'IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()
