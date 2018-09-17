"""
Processing large amounts of Twitter data:
Sometimes, the data we have to process reaches a size that is too much for a computer's memory to handle.
This is a common problem faced by data scientists. A solution to this is to process an entire data source chunk by
chunk, instead of a single go all at once.

You will process a large csv file of Twitter data,  working on it in chunks of 10 entries at a time.
"""

import pandas as pd

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv(r"../_datasets/tweets.csv", chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)
