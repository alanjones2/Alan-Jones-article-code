#12 visuals 4
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()
df['year']=[2000,2020]
df['London']=(20,25)
df['Manchester']=(18,20)

fig, ax = plt.subplots()

ax = df.plot(x='year', color = ('red', 'blue'), ax=ax)
ax = df.plot.scatter(x='year',y='London', color= 'red', ax=ax)
df.plot.scatter(x='year',y='Manchester', color = 'blue', ax=ax)

plt.xlim(1995,2025)
plt.xticks([2000, 2020])

ax.text(df.year[0] -8, df.London[0], df.columns[1])
ax.text(df.year[0] -2.5,df.London[0], f'{df.London[0]}ºC')
ax.text(df.year[1] +1, df.London[1],f'{df.London[1]}ºC')
ax.text(df.year[0] -8, df.Manchester[0], df.columns[2])
ax.text(df.year[0] -2.5, df.Manchester[0],f'{df.Manchester[0]}ºC')
ax.text(df.year[1] +1, df.Manchester[1],f'{df.Manchester[1]}ºC')

#ax.legend(loc='upper center')
ax.get_legend().set_visible(False)
#ax.set_yticks(())
ax.get_yaxis().set_visible(False)
#ax.set_ylabel('Temperature')

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.xaxis.grid(visible=True, color = 'black')

st.pyplot(fig)

