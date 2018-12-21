"""
SQLAlchemy ResultsProxy and Pandas Dataframes:

We can feed a ResultProxy directly into a pandas DataFrame, which is the workhorse of many Data Scientists in
PythonLand. Jason demonstrated this in the video. In this exercise, you'll follow exactly the same approach to convert a
ResultProxy into a DataFrame.

Instructions:
*   Import pandas as pd.
*   Create a DataFrame df using pd.DataFrame() on the ResultProxy results.
*   Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
*   Print the DataFrame.
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

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)