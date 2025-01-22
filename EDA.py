
# SQL NOTEBOOK
# Objective: Load the Spacex_dataset into a table in the Db2 database
# The data includes a record for each payload carried during a SpaceX mission.
# Execute queries to understand the dataset better.

import sqlite3
import pandas as pd

# Connect to SQLite database spacex.db
conn = sqlite3.connect("spacex.db")
cur = conn.cursor()  # Cursor class to execute SQLite statements

# Drop the table if it already exists
cur.execute("DROP TABLE IF EXISTS spacex")

# Creating the spacex table (define the schema)
CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS spacex (
    ID INTEGER PRIMARY KEY NOT NULL,
    Flight_No INTEGER,
    Launch_site TEXT,
    Payload TEXT,
    Payload_mass TEXT,
    Orbit TEXT,
    Customer TEXT,
    Launch_outcome TEXT,
    Version_Booster TEXT,
    Booster_landing TEXT,
    Date TEXT,
    Time TEXT
);
"""
cur.execute(CREATE_TABLE)
print("Table is Ready")

# Load the data from CSV
df = pd.read_csv('spacex_web_scraped.csv')

# Check the first few rows of the DataFrame to understand its structure
print(df.head())

# Load the DataFrame into the SQLite table
df.to_sql('spacex', conn, if_exists='replace', index=False, method='multi')

# Commit the changes
conn.commit()

# Query to display unique launch sites
cur.execute('SELECT DISTINCT "Launch site" FROM spacex')
unique_launch_sites = cur.fetchall()
print("Unique Launch Sites:")
for site in unique_launch_sites:
    print(site[0])

# Rename a column
alter_table_query = 'ALTER TABLE spacex RENAME COLUMN "Launch site" TO "Launch_site"'
try:
    cur.execute(alter_table_query)
    print("Column renamed successfully")


    # Additional query: Display 5 records where launch sites begin with 'CCA'
    cur.execute("SELECT * FROM spacex WHERE Launch_site LIKE 'CCA%' LIMIT 5")
    # Fetch the results
    records = cur.fetchall()
    print("\nRecords where Launch sites begin with 'CCA':")
    for record in records:
        print(record)  # Print each record



finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
    