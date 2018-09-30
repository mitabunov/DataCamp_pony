"""
List comprehensions for time-stamped data:

Use a list comprehension to extract the time from time-stamped Twitter data.
"""

import pandas as pd
df = pd.read_csv(r"../_datasets/tweets.csv")

# Extract the created_at column from df: tweet_time
tweet_time = df.loc[:, 'created_at']

# Extract the clock time: tweet_clock_time. Each row is a string that represents a timestamp, and you will access the
# 12th to 19th characters in the string to extract the time.
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)
