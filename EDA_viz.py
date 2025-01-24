
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
g.set_axis_labels("Flight Number", "Payload Mass (kg)", fontsize=14)
plt.tight_layout()
plt.show()

# Relationship between Flight number and Launch site
