

# Add a Launch site Drop-down Input Component
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


# Load the data from CSV
df = pd.read_csv('spacex_launch_geo.csv')
print(df.head(5))

launch_sites = df['Launch Site'].unique()  # Extract unique launch site names

# Define dropdown options (including the "All Sites" option)
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
                   [{'label': site, 'value': site} for site in launch_sites]
                   
# Initialize Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H4("Select a Launch Site:"),
    dcc.Dropdown(
        id='site-dropdown',
        options = dropdown_options,
        value='ALL',
        placeholder = 'Select a Launch Site',
        searchable=True,
        clearable=False
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=8060)