
# SPACEX.db

# Objective: Load the Spacex_dataset into a table in the Db2 database
# Includes a record for each payload carried during a SpaceX mission
# Execute queries to understand the dataset better
import sqlite3
import pandas as pd

# Load the data from CSV
try:
    df = pd.read_csv('C:/Users/marbj610/Documents/Repository/DS-application-showcase/Spacex.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'Spacex.csv' was not found.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Print columns to debug
print("Columns in DataFrame:", df.columns)

# Convert Date column to ISO format (YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Rename columns to avoid spaces in SQL
df.columns = df.columns.str.replace(' ', '_')  # Replaces spaces with underscores

# Check if 'Launch_site' exists
if 'Launch_site' not in df.columns:
    print("Error: 'Launch_site' column not found in DataFrame.")
    exit()

# Use a context manager for the database connection
with sqlite3.connect("spacex.db") as conn:
    cur = conn.cursor()

    # Drop the table if it already exists
    cur.execute("DROP TABLE IF EXISTS spacex")

    # Load the DataFrame into the SQLite table
    df.to_sql('spacex', conn, if_exists='replace', index=False, method='multi')

    # Query to display unique launch sites
    cur.execute('SELECT DISTINCT Launch_site FROM spacex')
    unique_launch_sites = cur.fetchall()
    print("Unique Launch Sites:")
    for site in unique_launch_sites:
        print(site[0])

    # Display 5 records where launch sites begin with 'CCA'
    cur.execute("SELECT * FROM spacex WHERE Launch_site LIKE 'CCA%' LIMIT 5")
    records = cur.fetchall()
    print("\nRecords where Launch sites begin with 'CCA':")
    for record in records:
        print(record)
        
    