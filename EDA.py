
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
    Launch_site TEXT UNIQUE,
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

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()