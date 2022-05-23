
message = """
        __Select an application from the list below__
        """

import streamlit as st
st.set_page_config(layout = "wide") # optional

from stlib import countryData
from stlib import continentData

with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',['Country Data','Continent Data']) 

if page == 'Country Data':
    countryData.run()
else:
    continentData.run()
