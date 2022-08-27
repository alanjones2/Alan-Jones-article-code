#12 visuals 4
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

weather =  pd.read_csv('https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv')

fig, ax = plt.subplots()
weather.plot.scatter(x='Rain', y='Sun', ax=ax)
st.pyplot(fig)
