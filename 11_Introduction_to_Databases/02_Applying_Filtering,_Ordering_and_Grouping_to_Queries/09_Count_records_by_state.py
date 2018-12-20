"""
Count of Records by State:
Often, we want to get a count for each record with a particular value in another column. The .group_by() method helps
answer this type of query. You can pass a column to the .group_by() method and use in an aggregate function like sum()
or count(). Much like the .order_by() method, .group_by() can take multiple columns as arguments.

Instructions:
*   Import func from sqlalchemy.
*   Build a select statement to get the value of the state field and a count of the values in the age field, and store
    it as stmt.
*   Use the .group_by() method to group the statement by the state column.
*   Execute stmt using the connection to get the count and store the results as results.
*   Print the keys/column names of the results returned using results[0].keys().
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
# ********************************************

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])
# Group stmt by state
stmt = stmt.group_by(census.columns.state)
# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()
# Print results
print(results)
# Print the keys/column names of the results returned
print(results[0].keys())

"""
Output comment:
Notice that the the key for the count method just came out as count_1. This can make it hard in complex queries to tell 
what column is being referred to: In the next exercise, you'll practice assign more descriptive labels when performing 
such calculations.
"""