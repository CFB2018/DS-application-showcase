
# SPACEX.db

# Objective: Load the Spacex_dataset into a table in the Db2 database
# Includes a record for each payload carried during a SpaceX mission
# Execute queries to understand the dataset better

import sqlite3
import pandas as pd

# Load the data from CSV
df = pd.read_csv('spacex_web_scraped.csv')

# Convert Date column to ISO format (YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date'], format='%d %B %Y').dt.strftime('%Y-%m-%d')
print(df)

# Use a context manager for the database connection
with sqlite3.connect("spacex.db") as conn:
    cur = conn.cursor() # Cursor class to execute SQLite statements

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

# Load the DataFrame into the SQLite table
df.to_sql('spacex', conn, if_exists='replace', index=False, method='multi')


# Query to display unique launch sites
cur.execute('SELECT DISTINCT "Launch site" FROM spacex')
unique_launch_sites = cur.fetchall()
print("Unique Launch Sites:")
for site in unique_launch_sites:
    print(site[0])

# The connection is automatically closed here
print("Data loaded and queries executed successfully.")

