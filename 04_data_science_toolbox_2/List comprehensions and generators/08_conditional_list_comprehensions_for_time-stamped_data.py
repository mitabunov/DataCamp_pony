"""
Conditional list comprehensions for time-stamped data:

Use a list comprehension to extract the time from time-stamped Twitter data. Add a conditional expression to the list
comprehension to only select the times in which entry[17:19] is equal to '19'.
"""

import pandas as pd
df = pd.read_csv(r"../_datasets/tweets.csv")

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
