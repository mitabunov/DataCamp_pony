"""
Twitter data to DataFrame:
Now you have the Twitter data in a list of dictionaries, tweets_data, where each dictionary corresponds to a single
tweet. Next, you're going to extract the text and language of each tweet. The text in a tweet, t1, is stored as the
value t1['text']; similarly, the language is stored in t1['lang']. Your task is to build a DataFrame in which each row
is a tweet and the columns are 'text' and 'lang'.

INSTRUCTIONS:
* Use pd.DataFrame() to construct a DataFrame of tweet texts and languages; to do so, the first argument should be
  tweets_data, a list of dictionaries. The second argument to pd.DataFrame() is a list of the keys you wish to have as
  columns. Assign the result of the pd.DataFrame() call to df.
* Print the head of the DataFrame.
"""


# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = '../_datasets/tweets3.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

######################################################

# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())
