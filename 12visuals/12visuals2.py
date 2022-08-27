#12 visuals 2
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


temps = pd.DataFrame()
temps['Day'] = ('Yesterday', 'Today')
temps['Temperature'] = (24,29)

st.subheader("st.table")
st.table(temps)

st.subheader("st.table in a narrow column")
col1,col2 = st.columns((1,10))
col1.table(temps)

st.subheader("st.dataframe")
st.dataframe(temps)
