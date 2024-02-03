import streamlit as st
from streamlit_option_menu import option_menu

# Define the pages and their file paths
pages = {'Home':'multipage-nav3.py',
         'Continent Data':'pages/continentData.py',
         'Country Data':'pages/countryData.py'}

# Create a list of the page names
page_list = list(pages.keys())

# Functions to create a navigation bar
# takes the current page as a parameter and switches pages if  
# a new one is selected from the menu
# the default is the first page in the pages dict

# Use 'option menu'
def nav(current_page=page_list[0]):
    with st.sidebar:
        p = option_menu("Page Menu", page_list, 
            default_index=page_list.index(current_page), 
            orientation="vertical")

        if current_page != p:
            st.switch_page(pages[p])

# Use a select box
def nav2(current_page=page_list[0]):
    with st.sidebar:
        p = st.selectbox("Page Menu", 
                         page_list, 
                         index=page_list.index(current_page))

        if current_page != p:
            st.switch_page(pages[p])

# Use radio buttons
def nav3(current_page=page_list[0]):
    with st.sidebar:
        p = st.radio("Page Menu", 
                     page_list, 
                     index=page_list.index(current_page))

        if current_page != p:
            st.switch_page(pages[p])
