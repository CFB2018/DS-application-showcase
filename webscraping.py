
'''
Objective: Web scrap Falcon 9 launch records HTML table from Wikipedia
Parse the table and convert it into a data frame

'''
# Necessary libraries
import sys
import requests
from bs4 import BeautifulSoup
import re
import unicodedata
import pandas as pd

# This function returns the data and time from the HTML table cell
def date_time(table_cells):
    return [data_time.strip() for data_time in list(table_cells.strings)][0:2]

# This function returns the booster version from the HTML table cell 
def booster_version(table_cells):
    out=''.join([booster_version for i,booster_version in enumerate( table_cells.strings) if i%2==0][0:-1])
    return out

# This function returns the landing status from the HTML table cell 
def landing_status(table_cells):
    out=[i for i in table_cells.strings][0]
    return out

def get_mass(table_cells):
    mass=unicodedata.normalize("NFKD", table_cells.text).strip()
    if mass:
        mass.find("kg")
        new_mass=mass[0:mass.find("kg")+2]
    else:
        new_mass=0
    return new_mass

# This function returns the landing status from the HTML table cell 
def extract_column_from_header(row):
    #If a <br> tag exists in the row, remove it
    if (row.br):
    #If an <a> (anchor tag exists in the row, remove it
        row.br.extract()
    if row.a:
        row.a.extract()
    if row.sup:
        row.sup.extract()
        
    column_name = ' '.join(row.contents) # join the contents into a string separated by space
    column_name = column_name.strip() # remove trailing whitespace
    
    # Filter the digit and empty names
    if not column_name.isdigit(): #ignore column name if its purely numeric
        return column_name    