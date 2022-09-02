#12 visuals 1 text
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


temps = pd.DataFrame()
temps['Day'] = ('Yesterday', 'Today')
temps['Temperature'] = (24,29)

fig, ax = plt.subplots()

temps.plot.bar(x='Day',y='Temperature', ax=ax)

st.pyplot(fig)


st.markdown("---")

st.metric("",29)

st.markdown("---")

col3, col4 = st.columns([1,4])
col3.metric("Temperature", 29, 5)
col4.markdown("#### Yesterday's temperature was 29ºC")
col4.markdown("That's 5º up from the previous day")

st.markdown("---")

col1, col2 = st.columns([1,4])
col1.markdown("# 29ºC")
col2.markdown("#### Yesterday's temperature was 20ºC")
col2.markdown("That's 5º up from the previous day")
