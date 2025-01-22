
# Objective: Load the Spacex_dataset into a table in the Db2 database
# The data includes a record for each payload carried during a SpaceX mission.
# Execute queries to understand the dataset better.


import sqlite3
import pandas as pd
import prettytable

prettytable.DEFAULT = 'DEFAULT'

# Connect to sqlite database
conn = sqlite3.connect("spacex.db")

# Cursor class can invoke methods that execute SQLite statements
cur = conn.cursor()

# Create a table in the database
# Drop the table if it already exists.
cur.execute("DROP TABLE IF EXISTS spacex")

# Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cur.execute(table)
print("Table is Ready")


'''
# load the data
df = pd.read_csv('spacex_web_scraped.csv')
df.to_sql('spacex', conn, if_exists = 'replace', index = False, method = 'multi')


# Example: Execute a query
cur.execute("SELECT * FROM spacex")

# Fetch the results
results = cur.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
con.close()

'''