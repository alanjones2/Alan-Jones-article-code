import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#st.set_page_config(page_title=None, page_icon=None, layout="wide")

# function to make any grid

def make_grid(cols,rows):
    grid = [0 for i in range(cols)]
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

# Main layout begins here

st.title("""
Three key findings from the 2022 UN Population Prospects
""")

st.write("""
The UN releases an update of its World Population Prospects every two years. 
Its latest release was delayed due to the COVID-19 pandemic and was released in 2022.
""")

st.markdown("---")
        
# Make the grid
mygrid = make_grid(3,(2,4,4))

# Row 0
popgrowth = pd.read_csv('data/population-growth.csv')
worldgrowth = popgrowth[popgrowth['Country name'] == 'World']

fig, ax = plt.subplots()
worldgrowth.plot(x='Year', y='Population growth rate', ax=ax)

mygrid[0][0].markdown("""
#### World population could be 8 billion by end of 2022
""")

mygrid[0][1].write("""
Since 1975 the world has been growing by billion people every 12 years. 

It passed 7 billion in 2011 and, by the end of 2022, 
there will be 8 billion people in the world. 
But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.
""")

mygrid[0][2].pyplot(fig)

# Row 1
popdf = pd.read_csv('data/population.csv')
worldpop = popdf[popdf['Country name'] == 'World']

fig, ax = plt.subplots()
worldpop.plot(x='Year',y='Population', ax=ax)

mygrid[1][0].markdown("""
#### World population will peak at 10.4 billion in 2086
""")

mygrid[1][1].write("""
The world population has increased rapidly over the last century.

The UN projects that the global population will peak before the end of the century,
 in 2086, at just over 10.4 billion people.
""")

mygrid[1][2].pyplot(fig)

# Row 2
fig, ax = plt.subplots()
ax = popdf[popdf['Country name'] == 'India'].plot(x = 'Year',y = 'Population', label = 'India', ax=ax)
popdf[popdf['Country name'] == 'China'].plot(x = 'Year', label = "China", y='Population', ax = ax)

mygrid[2][0].markdown("""
#### In 2023 India will overtake China as the world's most populous country
""")
mygrid[2][1].write("""
China is the world's most populous with more than 1.4 billion people. 
Now, its growth rate has fallen due to a rapid drop in fertility rate 
over the 1970s and 80s.

In India, the rate of decline has been slower, so it is expected to overtake China in 2023.
""")
mygrid[2][2].pyplot(fig)

# Footer
st.markdown("---")
st.markdown("""_Data and text courtesy of, 
[Our World in Data](https://ourworldindata.org/world-population-update-2022)_,
 [CC BY 4](https://creativecommons.org/licenses/by/4.0/)""")