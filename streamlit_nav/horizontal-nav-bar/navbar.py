import streamlit as st
from streamlit_option_menu import option_menu

# Define the pages and their file paths
pages = {'Home':'multipage-nav3.py',
         'Continent Data':'pages/continentData.py',
         'Country Data':'pages/countryData.py'}

# Create a list of the page names
page_list = list(pages.keys())

# Function to create a navigation bar
# takes the current page as a parameter and switches pages if  
# a new one is selected from the menu
def nav(current_page=page_list[0]):
    p = option_menu(None, page_list, 
        menu_icon="cast",
        default_index=page_list.index(current_page), 
        orientation="horizontal")

    if current_page != p:
        st.switch_page(pages[p])
