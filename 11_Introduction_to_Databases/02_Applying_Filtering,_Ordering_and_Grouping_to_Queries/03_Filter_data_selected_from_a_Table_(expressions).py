"""
Filter data selected from a Table - Expressions:

In addition to standard Python comparators, we can also use methods such as in_() to create more powerful where()
clauses. You can see a full list of expressions in the SQLAlchemy Documentation
(https://docs.sqlalchemy.org/en/latest/core/sqlelement.html#module-sqlalchemy.sql.expression).

We've already created a list of some of the most densely populated states.

Instructions:
*   Select all records from the census table by passing it in as a list to select().
*   Append a where clause to return all the records with a state in the states list. Use in_(states) on
    census.columns.state to do this.
*   Loop over the ResultProxy connection.execute(stmt) and print the state and pop2000 columns from each record.
"""


# Import create_engine, MetaData, Table, select
from sqlalchemy import create_engine, MetaData, Table, select
# Create an engine and connection that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///../_datasets/census.sqlite')
connection = engine.connect()
# Load MetaData()
metadata = MetaData()
# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)
# ********************************************

# List of states to apply where clause
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)
