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


config = {'staticPlot': False,
          'displayModeBar': False, 
          'title':False}

with st.container():
    cols = st.columns((1,2))
    with cols[0]:
        s = f"""
        <div style="background-color:#F0F2F6;padding:10px;height:400px">
            <h4>Mean yearly temperature</h4>
            <hr/>
            <p>
            </p>
        </div>
        """
        st.markdown(s, unsafe_allow_html=True)

    with cols[1]:
        fig1 = px.scatter(fweather, x='Year',y='Tmean',color='Station', trendline='ols')
        # adjust layout to remove space for title 't':0
        fig1.update_layout(margin= {'l': 0, 'r': 0, 'b': 0, 't': 0, 'pad': 10}, height=400)
        st.plotly_chart(fig1, use_container_width=True, config=config) 
with st.container():
    cols = st.columns((1,2))
    with cols[0]:

        s = f"""
        <div style="background-color:#F0F2F6;padding:10px;height:400px">
            <h4>Number of hours of sun</h4>
            <hr/>
            <p>
            </p>
        </div>
        """
        st.markdown(s, unsafe_allow_html=True)

    with cols[1]:

        fig1 = px.scatter(fweather, x='Year',y='Sun',color='Station', trendline='ols')
        fig1.update_layout(margin= {'l': 0, 'r': 0, 'b': 0, 't': 0, 'pad': 10}, height=400)
        st.plotly_chart(fig1, use_container_width=True, config=config) 

with st.container():
    cols = st.columns((1,2))

    with cols[0]:

        s = f"""
        <div style="background-color:#F0F2F6;padding:10px;height:400px">
            <h4>Number of millimeters of rain</h4>
            <hr/>
            <p>
            </p>
        </div>
        """
        st.markdown(s, unsafe_allow_html=True)

    with cols[1]:

        fig1 = px.scatter(fweather, x='Year',y='Rain',color='Station', trendline='ols')
        fig1.update_layout(margin= {'l': 0, 'r': 0, 'b': 0, 't': 0, 'pad': 10}, height=400)
        st.plotly_chart(fig1, use_container_width=True, config=config) 
with st.container():
    cols = st.columns((1,2))
    with cols[0]:

        s = f"""
        <div style="background-color:#F0F2F6;padding:10px;height:400px">
            <h4>Number of days of air frost in a year</h4>
            <hr/>
            <p>
            </p>
        </div>
        """
        st.markdown(s, unsafe_allow_html=True)

    with cols[1]:

        fig1 = px.scatter(fweather, x='Year',y='AF',color='Station', trendline='ols')
        fig1.update_layout(margin= {'l': 0, 'r': 0, 'b': 0, 't': 0, 'pad': 10}, height=400)
        st.plotly_chart(fig1, use_container_width=True, config=config) 






   