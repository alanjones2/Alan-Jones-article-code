import streamlit as st
import navbar

st.set_page_config(layout="wide")
st.header("Multipage navigation")
navbar.nav('Home')

st.markdown("""
            This app is a demonstrator of programmatically selecting a page in a multipage app.
            
            The pages display GDP data for countries or continents. The data is bundled with Plotly
            and originates from the Gapminder Foundation.
            """)

