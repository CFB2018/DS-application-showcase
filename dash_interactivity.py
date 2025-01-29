

# Add a Launch site Drop-down Input Component
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px

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
    ),
    html.Br(),  # Space between dropdown and chart

    dcc.Graph(id='success-pie-chart') 
])


# Add a callback function to render success-pie-chart based on selected site dropdown
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'))

# Add computation to callback function and return graph
def get_piechart(entered_site):
    if entered_site == 'ALL':
        # Group by 'Launch Site' and count successes
        success_counts = df[df['class'] == 1].groupby('Launch Site').size().reset_index(name='count')

        fig = px.pie(success_counts, values='count', names='Launch Site',
                     title='Total Successful Launches (All Sites)')
    
    else:
        # Filter for the selected site
        filtered_df = df[df['Launch Site'] == entered_site]
        success_counts = filtered_df['class'].value_counts().reset_index()
        success_counts.columns = ['class', 'count']

        fig = px.pie(success_counts, values='count', names='class',
                     title=f'Success vs Failure for {entered_site}')
    
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=8060)


# Open a web and type http://127.0.0.1:8060/ to see the Dashboard