
'''
Objective: Load the Spacex_dataset into  a table in the Db2 database
Includes a record for each payload carried during a SpaceX mission.
Execute queries to understand the dataset.

'''

import pandas as pd

# load the data
df = pd.read_csv('spacex_web_scraped.csv')


# Connect to the database
import csv, sqlite3
import prettytable
prettytable.DEFAULT = 'DEFAULT'

con = sqlite3.connect("spaceX-data.db")
cur = con.cursor()