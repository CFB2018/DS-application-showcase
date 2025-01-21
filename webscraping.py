import sys
import requests
from bs4 import BeautifulSoup
import re
import unicodedata
import pandas as pd

def date_time(table_cells):
    return [data_time.strip() for data_time in list(table_cells.strings) if data_time.strip()][:2]

def booster_version(table_cells):
    out = ''.join([booster_version for i, booster_version in enumerate(table_cells.strings) if i % 2 == 0 and booster_version.strip()][:1])
    return out

def landing_status(table_cells):
    out = [i for i in table_cells.strings if i.strip()][0]
    return out

def get_mass(table_cells):
    mass = unicodedata.normalize("NFKD", table_cells.text).strip()
    if mass and "kg" in mass:
        new_mass = mass[:mass.find("kg") + 2]
    else:
        new_mass = 0
    return new_mass

def extract_column_from_header(row):
    if row.br:
        row.br.extract()
    if row.a:
        row.a.extract()
    if row.sup:
        row.sup.extract()
        
    column_name = ' '.join([content.strip() for content in row.contents if content.strip()]) 
    column_name = column_name.strip() 
    
    if not column_name.isdigit(): 
        return column_name    

static_url = "https://en.wikipedia.org/w/index.php?title=List_of_Falcon_9_and_Falcon_Heavy_launches&oldid=1027686922"
response = requests.get(static_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page Title: ", soup.title.string) #Page Title:  List of Falcon 9 and Falcon Heavy launches - Wikipedia
    
    html_tables = soup.find_all("table")
    print("Number of tables found: {}".format(len(html_tables))) # 26
else:
    print("Failed to retrieve data: {}".format(response.status_code))

# Check the content for the 3rd table
first_launch_table = html_tables[2]
print(first_launch_table)

# Extract relevant column names from the HTML table headers by iterating through <th> elements

# Apply find_all() function with `th` element on first_launch_table
header_cells = first_launch_table.find_all("th")

# Extract column names and filter out empty names
column_names = []
for header in header_cells:
    name = extract_column_from_header(header)
    if name is not None and len(name) > 0:
        column_names.append(name)
print("Column Names: {}".format(column_names))