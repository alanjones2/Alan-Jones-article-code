#12 visuals 3 heatmap
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url='data/bydecade.csv'
gwdec = pd.read_csv(url)
gwdec=gwdec.set_index('Year')
st.table(gwdec)

fig, ax = plt.subplots()
ax.imshow(gwdec)
ax.set_xticks(range(len(gwdec.columns)))
ax.set_xticklabels(gwdec.columns, rotation=45)
st.pyplot(fig)

import seaborn as sns
fig, ax = plt.subplots()
sns.heatmap(gwdec)
st.pyplot(fig)