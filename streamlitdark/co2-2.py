import streamlit as st
import plotly.express as px
import pandas as pd

@st.cache
def get_data(url):
    return pd.read_csv(url)
@st.cache
def get_co2_data(): 
    # OWID Data on CO2 and Greenhouse Gas Emissions
    # Creative Commons BY license
    url = 'https://github.com/owid/co2-data/raw/master/owid-co2-data.csv'
    return get_data(url)
@st.cache
def get_warming_data():
    # OWID Climate Change impacts
    # Creative Commons BY license
    url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Climate%20change%20impacts/Climate%20change%20impacts.csv'
    return get_data(url).query("Entity == 'World' and Year <=2021")


st.set_page_config(layout = "wide")

df_co2= get_co2_data()

df_co2

st.markdown("""
# World CO2 emissions
__The graphs below show the CO2 emissions per capita for the entire 
world and individual countries over time.
Select a year with the slider in the left-hand graph and countries 
from the drop down menu in the other one.__

__Scroll down to see charts demonstrating the correlation between 
the level of CO2 and global warming.__

__Hover over any of the charts to see more detail__

---

""")

col2, space2, col3 = st.columns((10,1,10))

with col2:
    year = st.slider('Select year',1750,2020)
    fig = px.choropleth(df_co2[df_co2['year']==year], locations="iso_code",
                        color="co2_per_capita",
                        hover_name="country",
                        range_color=(0,25),
                        color_continuous_scale=px.colors.sequential.Reds)
    st.plotly_chart(fig, use_container_width=True)

with col3: 
    default_countries = ['World','United States','United Kingdom','EU-27','China', 'Australia']
    countries = df_co2['country'].unique()

    selected_countries = st.multiselect('Select country or group',countries,default_countries)

    df3 = df_co2.query('country in @selected_countries' )

    fig2 = px.line(df3,"year","co2_per_capita",color="country")

    st.plotly_chart(fig2, use_container_width=True)

    
# st.dataframe(get_warming_data())

col4, space3, col5,space4,col6 = st.columns((10,1,10,1,10))
with col4:
    st.markdown("""
    ## Corelation between CO2 emission and global warming

    This can be seen in the adjacent graphs. 
    
    The first show temperature
    has changed since 1850 and you can see that temperatures begin 
    to rise after the beginning of the twentieth century but there 
    is a sharp upturn in that rise about mid-way through (the scatter
    points are the actual figures for each year and the line is a 
    lowess smoothing of those points so that we can more easily see 
    the trend).

    The second graph shows the rise in total CO2 emissions over the 
    same period and a similar trend can be seen with a sharp rise in 
    emissions mid-twentieth century.
    """)
with col5:
    df4 = get_warming_data()
    st.subheader("World sea temperature change ")
    fig3 = px.scatter(df4,"Year","annual_sea_surface_temperature_anomaly", trendline='lowess')
    st.plotly_chart(fig3, use_container_width=True)
with col6:
    st.subheader("Total world CO2 emissions")
    fig4 = px.line(df3.query("country == 'World' and year >= 1850"),"year","co2")
    st.plotly_chart(fig4, use_container_width=True)







st.markdown('__Data Source:__ _Our World in Data CC BY_')