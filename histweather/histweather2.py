import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go
from scipy import stats


#################### Data

weather = pd.read_csv('bigtable.csv')


################################## Layout ##################################################33


st.set_page_config(layout = 'wide')



st.dataframe(weather)


years = weather.Year.unique()
years = years[:-1] # drop 2022 as it is not complete

station_names = weather.Station.unique()

s = st.multiselect('Select a weather station', station_names)

fweather = weather[weather['Station'].isin(s)]

fig1 = px.scatter(fweather, x='Year',y='Tmean',color='Station', trendline='ols')
st.plotly_chart(fig1, use_container_width=True) 

fig1 = px.scatter(fweather, x='Year',y='Sun',color='Station', trendline='ols')
st.plotly_chart(fig1, use_container_width=True) 

fig1 = px.scatter(fweather, x='Year',y='Rain',color='Station', trendline='ols')
st.plotly_chart(fig1, use_container_width=True) 

fig1 = px.scatter(fweather, x='Year',y='AF',color='Station', trendline='ols')
st.plotly_chart(fig1, use_container_width=True) 
   