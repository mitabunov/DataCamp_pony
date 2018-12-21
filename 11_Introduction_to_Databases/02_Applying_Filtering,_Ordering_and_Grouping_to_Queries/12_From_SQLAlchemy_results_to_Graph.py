"""
From SQLAlchemy results to a Graph:

We can also take advantage of pandas and Matplotlib to build figures of our data. Remember that data visualization is
essential for both exploratory data analysis and communication of your data!

Instructions:
*   Import matplotlib.pyplot as plt.
*   Create a DataFrame df using pd.DataFrame() on the provided results.
*   Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
*   Print the DataFrame df.
*   Use the plot.bar() method on df to create a bar plot of the results.
*   Display the plot with plt.show().
"""


# Import create_engine, MetaData, Table, select
from sqlalchemy import create_engine, MetaData, Table, select, func
# Create an engine and connection that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///../_datasets/census.sqlite')
connection = engine.connect()
# Load MetaData()
metadata = MetaData()
# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')
# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])
# Group stmt by state
stmt = stmt.group_by(census.columns.state)
# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()
# ********************************************

# import pandas
import pandas as pd
# Import pyplot as plt from matplotlib
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)
# Set Column names
df.columns = results[0].keys()
# Print the DataFrame
print(df)
# Plot the DataFrame
df.plot.bar()
plt.show()
