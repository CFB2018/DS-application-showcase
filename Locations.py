
"""
Launch Site Locations Analysis

Investigate which locations have the highest success rate using interactive visual analytics.
Follow up on the prelim correlations btw the launch site and success rate found in the spaceX launch dataset.
"""

# Import necessary libraries
import folium
from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon
import wget
import pandas as pd

# Mark all launch sites on a map
spacex_geo_df = pd.read_csv('spacex_launch_geo.csv')
#print(spacex_geo_df)

# What are coordinates for each site?
spacex_geo_df = spacex_geo_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df = spacex_geo_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long']]
print(launch_sites_df)