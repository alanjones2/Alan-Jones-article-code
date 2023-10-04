import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import pandas as pd
import stutils as stu

def read_file():
    file = 'https://github.com/alanjones2/GISS/raw/main/data/GLB.Ts%2BdSST.csv'

    df = pd.read_csv(file, skiprows=1)
    return "Global Data", df

st.set_page_config(layout="wide")

st.title("A new Plotly component for Streamlit")

st.info("""Streamlit's inbuilt Plotly function is restricted to use only one
        of two template themes - the built-in Streamlit theme, or the default Plotly theme.
        We develop a new component to make displaying Plotly charts more flexible.""")

title, df = read_file()

period = 'JJA'
scale = 'inferno'
template = 'plotly_dark'
fig = px.bar(df, x='Year', y = period, color="JJA", title = f"{title} - {period}", 
       color_continuous_scale=scale, template=template, width=800, height=400)

col1, col2 = st.columns(2,gap="small")
with col1:
    st.info("Chart using new component")
    stu.plotly_chart(fig)
with col2:
    st.info("Chart using st.plotly_chart()")
    st.plotly_chart(fig)

#### New template ###

st.header("Create a new template")
st.info("""On reflection maybe the Plotly Dark template is a bit too dark
         - let's change the background color to a lighter colour while keeping everything else the same""")

import plotly.graph_objects as go
import plotly.io as pio

pio.templates["draft"] = go.layout.Template()

bg = 'dimgrey' # still dark but not black
pio.templates["draft"].layout.paper_bgcolor=bg
pio.templates["draft"].layout.plot_bgcolor=bg

period = 'JJA'
scale = 'inferno'
template = 'plotly_dark+draft'
fig = px.bar(df, x='Year', y = period, color="JJA", title = f"{title} - {period}", 
       color_continuous_scale=scale, template=template, width=1600, height=400)

stu.plotly_chart(fig)