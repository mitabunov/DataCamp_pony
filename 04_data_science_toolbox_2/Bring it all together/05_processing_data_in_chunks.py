"""
Processing data in chunks (1):

INSTRUCTIONS:
- Use open() to bind the csv file 'world_ind_pop.csv' as file in the context manager.
- Complete the for loop so that it iterates 1000 times to perform the loop body and process only the first 1000 rows
of data of the file.
"""


# Open a connection to the file
with open(r'../_datasets/world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)
