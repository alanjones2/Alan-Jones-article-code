#12 visuals 6 slopegraph
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()
df['year']=[2000,2020]
df['London']=(20,25)
df['Manchester']=(18,20)

st.table(df)

fig, ax = plt.subplots()

ax = df.plot(x='year', color = ('red', 'blue'), ax=ax)
ax = df.plot.scatter(x='year',y='London', color= 'red', ax=ax)
df.plot.scatter(x='year',y='Manchester', color = 'blue', ax=ax)

plt.xlim(1995,2025)
plt.xticks([2000, 2020])
ax.set_ylabel('')
st.pyplot(fig)

ax.text(df.year[0] -8, df.London[0], df.columns[1])
ax.text(df.year[0] -2.5,df.London[0], f'{df.London[0]}°C')
ax.text(df.year[1] +1, df.London[1],f'{df.London[1]}°C')
ax.text(df.year[0] -8, df.Manchester[0], df.columns[2])
ax.text(df.year[0] -2.5, df.Manchester[0],f'{df.Manchester[0]}°C')
ax.text(df.year[1] +1, df.Manchester[1],f'{df.Manchester[1]}°C')

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.xaxis.grid(visible=True, color = 'black')
ax.get_yaxis().set_visible(False)

ax.get_legend().set_visible(False)

st.pyplot(fig)

