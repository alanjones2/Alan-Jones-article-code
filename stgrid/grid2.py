import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title=None, page_icon=None, layout="wide")

st.title("""
Three key findings from the 2022 UN Population Prospects
""")


st.write("""
The UN releases an update of its World Population Prospects every two years. 
Its latest release was due in 2021 but was delayed as a result of the COVID-19 pandemic. 
But, appropriately, on World Population Day, the dataset was released.
""")

st.markdown("---")

# make any grid with a function

def make_grid(cols,rows):
    grid = [0 for i in range(cols)]
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid
        
mygrid = make_grid(3,(2,4,4))

popgrowth = pd.read_csv('data/population-growth.csv')
#popgrowth
worldgrowth = popgrowth[popgrowth['Country name'] == 'World']
#worldgrowth

fig, ax = plt.subplots()
worldgrowth.plot(x='Year', y='Population growth rate', ax=ax)

mygrid[0][0].subheader("""
World population could be 8 billion by end of 2022
""")

mygrid[0][1].write("""
Since 1975 the world has been adding another billion people every 12 years. 

It passed its last milestone - 7 billion in 2011. And, by the end of 2022, 
it will pass another one: there will be 8 billion people in the world.

While this rate of absolute growth is similar to previous decades, 
the growth rate continues to fall. Since 2019, the global population 
growth rate has fallen below 1%. 

That's less than half its peak rate of growth - of 2.3% - in the 1960s.
""")

mygrid[0][2].pyplot(fig)

popdf = pd.read_csv('data/population.csv')
worldpop = popdf[popdf['Country name'] == 'World']

fig, ax = plt.subplots()
worldpop.plot(x='Year',y='Population', ax=ax)

mygrid[1][0].subheader("""
The global population is projected to peak at around 10.4 billion in 2086
""")

mygrid[1][1].write("""
The world population has increased rapidly over the last century.  When will it come to an end?

Previous versions of the UN World Population Prospects showed a significant slowdown in population growth, with very slow growth – almost reaching a plateau – by the end of the century. In its previous release, it projected that the world population would be around 10.88 billion in 2100, and would not yet have peaked.

In this new release, the UN projects that the global population will peak before the end of the century – in 2086 at just over 10.4 billion people.1

There are several reasons for this earlier, and lower, peak. One is that the UN expects fertility rates to fall more quickly in low-income countries compared to previous revisions. It also expects less of a ‘rebound’ in fertility rates across high-income countries in the second half of the century.

""")

mygrid[1][2].pyplot(fig)

fig, ax = plt.subplots()
ax = popdf[popdf['Country name'] == 'India'].plot(x = 'Year',y = 'Population', label = 'India', ax=ax)
popdf[popdf['Country name'] == 'China'].plot(x = 'Year', label = "China", y='Population', ax = ax)

mygrid[2][0].subheader("""
In 2023 India is expected to take over from China as the world’s most populous country
""")
mygrid[2][1].write("""
China has been the world’s most populous country for decades. It is now home to more than 1.4 billion people. However, its population growth rate has fallen significantly following a rapid drop in its fertility rate over the 1970s and 80s.

The fertility rate in India has also fallen substantially in recent decades – from 5.7 births per woman in 1950 to just 2 births per woman today. However, the rate of this decline has been slower.

Because of this, India will very soon overtake China as the most populous country in the world. The UN expects this to happen in 2023.
""")
mygrid[2][2].pyplot(fig)


st.markdown("---")
st.markdown("""_Data and text courtesy of, 
[Our World in Data](https://ourworldindata.org/world-population-update-2022)_,
 [CC BY 4](https://creativecommons.org/licenses/by/4.0/)""")