"""
Bringing it all together (1)
Write a lambda function and use filter() to select retweets, that is, tweets that begin with the string 'RT'.
"""

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv(r'../Functions and Tuples/tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
