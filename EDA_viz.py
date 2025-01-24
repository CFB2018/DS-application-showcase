
'''
Exploratory Data Analysis with Visualization

'''

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV
df = pd.read_csv('dataset_part_2.csv')
print(df.head(5))

# Plot Flightnumber vs PayloadMass
g = sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 2)
g.fig.suptitle("Payload Mass by Flight Number", fontsize= 20)
g.set_xticklabels(rotation=45, ha='right', fontsize=10)
x_ticks = np.arange(0, len(df['FlightNumber'].unique()), step=2)
g.set_axis_labels("Flight Number", "Payload Mass (kg)", fontsize=14)
plt.xticks(ticks=x_ticks, fontsize=10)
plt.tight_layout()
plt.show()

# View the relationship between Flight number and Launch site
plt.figure(figsize=(12, 6))
sns.countplot(y="LaunchSite", data=df, order=df['LaunchSite'].value_counts().index)
plt.title("Number of Flights by Launch Site", fontsize=20)
plt.xlabel("Number of Flights", fontsize=14)
plt.ylabel("Launch Site", fontsize=14)
plt.tight_layout()
plt.show()