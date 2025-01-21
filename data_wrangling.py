
'''
Objective: Perform exploratory data analysis to find patterns in the data and determine training labels.

Booster landing outcomes will be converted into training labels; 1 = booster landed successfully, 
and 2 = booster landing was unsuccessful.
True Ocean (mission outcome was successful), or False Ocean (mission outcome was not successful),
True RTLS or False RTLS , True ASDs or False ASDS
'''

# Import libraries
import pandas as pd
import numpy as np

# load the data
df = pd.read_csv('dataset_part_1.csv')

# Calculate the percentage of the missing values in each attribute
print(df.isnull().sum()/len(df)*100)

print(df.dtypes)

# Calculate number of launches on each site (check column LaunchSite)'
launch_counts = df['LaunchSite'].value_counts()
print(launch_counts)