#12 visuals 3 heatmap
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url='https://raw.githubusercontent.com/alanjones2/dataviz/master/tempbydecade.csv'
gwdec = pd.read_csv(url, delimiter=' ', skipinitialspace=True)
gwdec=gwdec.set_index('Year')
st.table(gwdec)

fig, ax = plt.subplots()

ax.imshow(gwdec)

ax.set_xticks(range(len(gwdec.columns)))

ax.set_xticklabels(gwdec.columns, rotation=45)
st.pyplot(fig)