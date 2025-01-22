# Objective: Load the Spacex_dataset into a table in the Db2 database
# Includes a record for each payload carried during a SpaceX mission.
# Execute queries to understand the dataset.

import pandas as pd
import sqlite3
import prettytable

prettytable.DEFAULT = 'DEFAULT'

# Connect to the database
con = sqlite3.connect("spaceX-data.db")
cur = con.cursor()

# load the data
df = pd.read_csv('spacex_web_scraped.csv')
df.to_sql('SPACEXTBL', con, if_exists = 'replace', index = False, method = 'multi')






'''
# Example: Execute a query
cur.execute("SELECT * FROM your_table_name")

# Fetch the results
results = cur.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
con.close()

'''