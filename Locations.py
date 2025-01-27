
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


# Visualize the launch sites on a map 
# Start by creating a Folium map object with NASA as initial location
nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)

"""
# Create a blue circle at NASA Johnson Space Center's coordinate with a popup label showing its name
circle = folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
# Create a blue circle at NASA Johnson Space Center's coordinate with a icon showing its name
marker = folium.map.Marker(
    nasa_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)

Save the map to an HTML file and open it
site_map.save("nasa_map.html")
import webbrowser
webbrowser.open("nasa_map.html")

"""
# Add a circle for each launch site
# List of 5 lauch site coordinates and their names
launch_sites = [{"name": "NASA Johnson Space Center", "coordinate": [29.559684888503615, -95.0830971930759]},
    {"name": "CCAFS LC-40", "coordinate": [28.562302, -80.577356]},
    {"name": "VAFB SLC-4E", "coordinate": [34.632093, -120.610829]},
    {"name": "KSC LC-39A", "coordinate": [28.573255, -80.646895]},
    {"name": "CCAFS SLC-40", "coordinate": [28.5618571, -80.577366]},]

# Loop through the launch sites and add circles + markers
for site in launch_sites:
    circle = folium.Circle(
        location=site["coordinate"],
        radius=1000,
        color='#d35400',
        fill=True,
        fill_color='#d35400').add_child(folium.Popup(site["name"]))
# Add a marker with a label
    marker = folium.Marker(
        location=site["coordinate"],
        icon=DivIcon(
            icon_size=(20,20),
            icon_anchor=(0,0),
            html=f'<div style="font-size: 12px; color:#d35400;"><b>{site["name"]}</b></div>',))

# Add the circle and marker to the map
    site_map.add_child(circle)
    site_map.add_child(marker)

"""
# Save the map to an HTML file and open it
site_map.save("launch_sites_map.html")
import webbrowser
webbrowser.open("launch_sites_map.html")
"""

# Mark the success/failed launches for each site (class)
# Class= 1 # success - green
# Class= 2 # failed - red
print(spacex_geo_df.tail(10))

# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(site_map)

# Function that checks the value of class column
def assign_marker_color(launch_outcome):
    if launch_outcome == 1:
        return 'green'
    else:
        return 'red'

# Add a marker color column to the DataFrame
spacex_geo_df['marker_color'] = spacex_geo_df['class'].apply(assign_marker_color)

# Add markers for each launch site to the map
for index, row in spacex_geo_df.iterrows():
    popup = f"Launch Site: {row['Launch Site']}<br>Outcome: {'Success' if row['class'] == 1 else 'Failed'}"
    folium.Marker(
        location=[row['Lat'], row['Long']],
        popup=popup,
        icon=folium.Icon(color=row['marker_color'])
    ).add_to(marker_cluster)


# Save the map to an HTML file and open it
site_map.save("launch_outcomes_map.html")
import webbrowser
webbrowser.open("launch_outcomes_map.html")

# Calculate the distance btw a launch site to its proximities

# Add Mouse Position to get the coordinate (Lat, Long) for a mouse over on the map
formatter = "function(num) {return L.Util.formatNum(num, 5);};"
mouse_position = MousePosition(
    position='topright',
    separator=' Long: ',
    empty_string='NaN',
    lng_first=False,
    num_digits=20,
    prefix='Lat:',
    lat_formatter=formatter,
    lng_formatter=formatter,
)

site_map.add_child(mouse_position)
site_map