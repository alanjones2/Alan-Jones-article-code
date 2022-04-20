import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


from scipy import stats


#################### Data

weather = pd.read_csv('bigtable.csv')

# get the list of years and station from the data
years = weather.Year.unique()
years = years[:-1] # drop 2022 as it is not complete

station_names = weather.Station.unique()

# set up the data for displaying the charts
tables = ('Tmean','Sun','Rain','AF')
tablesTitle = {
    'Tmean':'Mean Temperature',
    'Sun':'Number of hourse of sunshine',
    'Rain':'Rainfall in millimeters',
    'AF':'Number of days when there was an air frost' }


# plotly set up
pio.templates.default = "plotly"

config = {'staticPlot': False,
          'displayModeBar': False, 
          'title':False}

################################## Layout ##################################################33

st.set_page_config(layout = 'wide')

#st.dataframe(weather)
st.title("UK Historical Weather Data Dashboard")
st.write("""Select one or more weather staions from the selection box 
            and view the graphs for Mean Temperature, Sun, Rainfall and Frosts """)

s = st.multiselect('Select a weather station', station_names)

fweather = weather[weather['Station'].isin(s)]

for table in tables:
    with st.container():
        cols = st.columns((1,2))
        with cols[0]:
            s = f"""
            <div style="background-color:#F0F2F6;padding:10px;height:360px">
                <b>{tablesTitle[table]}</b>
                <hr/>
                <p>
                </p>
            </div>
            """
            st.markdown(s, unsafe_allow_html=True)
        with cols[1]:
            fig1 = px.scatter(fweather, x='Year',y=table,color='Station', trendline='ols')
            fig1.update_layout(margin= {'l': 0, 'r': 0, 'b': 0, 't': 0, 'pad': 10}, height=400)
            st.plotly_chart(fig1, use_container_width=True, config=config) 

