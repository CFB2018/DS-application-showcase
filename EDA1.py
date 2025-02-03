
# SQL NOTEBOOK

# Objective: Load the Spacex_dataset into a table in the Db2 database
# Includes a record for each payload carried during a SpaceX mission.
# Execute queries to understand the dataset better.

import pandas as pd
import sqlite3
import prettytable

prettytable.DEFAULT = 'DEFAULT'

# Load the data from CSV
df = pd.read_csv('spacex_web_scraped.csv')

# Connect to the database
con = sqlite3.connect("spacex.db") # database name = spacex.db
cur = con.cursor()

cur.execute("SELECT * FROM spacex") # table name spacex

# Fetch the result
results = cur.fetchall()
for row in results:
    print(row)
    
# Close the connection
con.close()

"""
# Convert Date column to ISO format (YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date'], format='%d %B %Y').dt.strftime('%Y-%m-%d')
print(df)

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


    # Display 5 records where launch sites begin with 'CCA'
    cur.execute("SELECT * FROM spacex WHERE Launch_site LIKE 'CCA%' LIMIT 5")
    # Fetch the results
    records = cur.fetchall()
    print("\nRecords where Launch sites begin with 'CCA':")
    for record in records:
        print(record)  # Print each record
        
    # Calculate total payload mass for NASA (CRS) missions
    cur.execute("""
        SELECT SUM(CAST("Payload mass" AS FLOAT)) 
        FROM spacex 
        WHERE Customer = 'NASA' AND Payload LIKE '%CRS%'
    """)
    total_payload_mass = cur.fetchone()[0]
    print("Total Payload Mass carried by NASA (CRS): {} kg".format(total_payload_mass))

    # Calculate average payload mass for booster version F9 v1.1
    cur.execute("""
        SELECT AVG(CAST("Payload mass" AS FLOAT)) 
        FROM spacex 
        WHERE "Version Booster" = 'F9 v1.1'
    """)
    average_payload_mass = cur.fetchone()[0]
    print("Average Payload Mass carried by booster version F9 v1.1: {} kg".format(round(average_payload_mass,2)))


 # Find the date of the first successful landing outcome on a ground pad
    cur.execute("""
        SELECT MIN(Date) 
        FROM spacex 
        WHERE "Booster landing" LIKE '%Success%'
    """)
    first_successful_landing_date = cur.fetchone()[0]
    print("Date of the first successful landing outcome on ground pad: {}".format(first_successful_landing_date))

# List names of boosters with successful drone ship landings and payload mass between 4000 and 6000
    cur.execute("""
        SELECT DISTINCT "Version Booster" 
        FROM spacex 
        WHERE "Booster landing" = 'Success' 
        AND CAST("Payload mass" AS FLOAT) > 4
        AND CAST("Payload mass" AS FLOAT) < 6
    """)
    successful_boosters = cur.fetchall()

    # Print the names of the successful boosters
    print("Boosters with successful drone ship landings and payload mass between 4000 and 6000:")
    for booster in successful_boosters:
        print(booster[0])
        
    # Count number of successful and failure mission outcomes
    cur.execute("""
        SELECT TRIM("Booster landing") AS landing, COUNT(*) AS total
        FROM spacex
        WHERE TRIM("Booster landing") IN ('Success', 'Failure')
        GROUP BY TRIM("Booster landing")
    """)
    outcomes = cur.fetchall()
    
    successful_count = 0
    failed_count = 0
    
    for outcome in outcomes:
        if "Success" in outcome[0]:
            successful_count += outcome[1]
        elif "Failure" in outcome[0]:
            failed_count += outcome[1]
    print("Successful outcome:{} and Failed outcome {}".format(successful_count, failed_count))
    
    # List the names of the booster versions which have carried max payload mass
    cur.execute("""
        SELECT DISTINCT "Version Booster"
        FROM spacex
        WHERE CAST("Payload mass" AS FLOAT) = (
            SELECT MAX(CAST("Payload mass" AS FLOAT))
            FROM spacex
        )
    """)
    booster_versions = cur.fetchall()
    print("Booster versions that have carried the maximum payload mass:")
    for version in booster_versions:
        print(version[0])
    
    
    # List the records which display the month, failure landing_outcomes, booster version, launch_site in year 2015
    cur.execute("""
        SELECT
            CASE strftime('%m', Date)
            WHEN '01' THEN 'January'
            WHEN '02' THEN 'February'
            WHEN '03' THEN 'March'
            WHEN '04' THEN 'April'
            WHEN '05' THEN 'May'
            WHEN '06' THEN 'June'
            WHEN '07' THEN 'July'
            WHEN '08' THEN 'August'
            WHEN '09' THEN 'September'
            WHEN '10' THEN 'October'
            WHEN '11' THEN 'November'
            WHEN '12' THEN 'December'
        END AS Month,
        "Launch_site",
        "Version Booster"
    FROM spacex
    WHERE TRIM("Booster landing") = 'Failure'
    AND strftime('%Y', Date) = '2015';
""")
    failed_records = cur.fetchall()
    print(f"Number of records fetched: {len(failed_records)}")
    print("Fetched records:", failed_records)            

    
    def fetch_landing_counts():   
        cur.execute("""
            SELECT
                TRIM(UPPER(Booster_landing)) AS LandingOutcome,
                COUNT(*) AS LandingCount
            FROM spacex
            WHERE Date BETWEEN '2010-06-04' AND '2017-03-20'
            GROUP BY Booster_landing
            ORDER BY LandingCount DESC;
        """)

        landing_counts = cur.fetchall()
    
        print("\nLanding Outcomes Ranked (2010-06-04 to 2017-03-20):")
        print(f"{'Landing Outcome':<20} | {'Count'}")
        print("-" * 30)
    
        for row in landing_counts:
            print(f"{row[0]:<15} | {row[1]}")
fetch_landing_counts()

 
finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

"""