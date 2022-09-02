#12 visuals 5 line
from textwrap import fill
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

weather =  pd.read_csv('https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv')

weather['Tmean'] = (weather['Tmax'] + weather['Tmin'])/2
st.table(weather)

fig, ax = plt.subplots()
ax = weather.plot.line(x='Month', y = 'Tmean', ax=ax)
st.pyplot(fig)

ax = weather.plot.line(x='Month', y = 'Tmax', color = 'lightgrey', ax=ax)
ax = weather.plot.line(x='Month', y = 'Tmin',  color = 'lightgrey', ax=ax)

st.pyplot(fig)

plt.fill_between(weather['Month'], weather['Tmax'],weather['Tmin'], color='lightgrey', alpha=0.5)

ax.get_legend().set_visible(False)

ax.set_ylabel('Temperature Range ºC')


st.pyplot(fig)