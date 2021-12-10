#
#
#
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")

## Function to get the data is cached so that the data is only fetched once
@st.cache
def get_data():
    #consumption based energy per capita
    consumption_per_cap = pd.read_csv("https://raw.githubusercontent.com/alanjones2/dataviz/master/traded-energy/consumption-based-energy-per-capita.csv")

    #production vs consumption energy
    prod_v_cons_energy = pd.read_csv("https://raw.githubusercontent.com/alanjones2/dataviz/master/traded-energy/production-vs-consumption-energy.csv")

    #traded energy share domestic
    traded_energy_shar_dom = pd.read_csv("https://raw.githubusercontent.com/alanjones2/dataviz/master/traded-energy/traded-energy-share-domestic.csv")

    return consumption_per_cap, prod_v_cons_energy, traded_energy_shar_dom

consumption_per_cap, prod_v_cons_energy, traded_energy_shar_dom = get_data()

############################################################################


st.markdown("""
## How Much Energy do Countries _Really_ Use: an Analysis
---
__ Using Streamlit as a document generator, with Plotly and Python, we investigate just how much energy
countries are really responsible for. Because it's not just what you use at home.__ 

Just how much energy do you consume?

There's the electricity that you use to light and heat your home. 
There's the fuel used to get you to work and to do your shopping. These are fairly obvious but what about 
the energy expended in producing the things that you consume? How much energy was required to make the computer 
that you are using right now, or your car, or washing machine or fridge?

And, furthermore, where was that energy expended? If you drive a Toyota, for example, was it made in Japan, 
was your neighbour's Mercedes made in Germany? And when it come to smartphones, most users don't live
in the country where they were actually made. The energy that was used to make all this stuff
was actually expended in another country. So who is responsible for that energy use; is it the producer or the consumer?

Some countries effectively import energy in terms of the goods that they buy from other countries and
similarly, countries also export energy with the goods that they sell.

__Our World in Data__ (OWID) is an organisation that (in it's own words) produces __Research and data to make progress against 
the world’s largest problems__ and they have produce a fascinating report on just where the in the World our energy goes. 
They also permit anyone to reuse their material and data under a the permissive CC BY licence.

So we are going to use that information and data to produce our own analysis using Python and Streamlit. 
I've written about Streamlit before and developed simple apps with it but have generally regarded it as a web
site builder. But, in an attempt to prise myself away (kicking and screaming) from my software developer preducices, I'm going 
to try and look at Streamlit as a way of producing interactive documents.

Before going any further, though, let me wholeheartedly acknowledge that all of the data used here, and much of the information, too, 
originates with OWID and is repoduced here under the CC BY licence. You may also be interested in seeing their original
report [here](https://ourworldindata.org/energy-offshoring).

""")

col1,space1,col2 = st.columns((10,1,10))
with col1:
    st.markdown("""
    #### Energy Consumption per Capita
    Let's start by looking at the energy consumption in each country. OWID provides us with a csv file that
    lists the per capita energy consumption over several years for a number of countries.
    """)

with col2:
    countries = consumption_per_cap['Entity'].unique()
    default_countries = ['United States','United Kingdom','China', 'Australia']
    country = st.multiselect("Select one or more countries",countries,default_countries)


    fig = px.line(consumption_per_cap.query("Entity in @country"), 
                x = "Year", y = "consumption_per_capita",title = 'Energy Consumption per Capita ', color = 'Entity')

    st.plotly_chart(fig,use_container_width = True)

st.dataframe(consumption_per_cap)

st.dataframe(prod_v_cons_energy)

st.dataframe(traded_energy_shar_dom)