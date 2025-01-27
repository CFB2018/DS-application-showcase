
"""
Launch Site Location Analysis

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