import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#st.set_page_config(page_title=None, page_icon=None, layout="wide")

# make any grid with a function

def make_grid(cols,rows):
    grid = [0 for i in range(cols)]
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid
        
mygrid = make_grid(3,3)

popgrowth = pd.read_csv('data/population-growth.csv')
#popgrowth
worldgrowth = popgrowth[popgrowth['Country name'] == 'World']
#worldgrowth

fig, ax = plt.subplots()
worldgrowth.plot(x='Year', y='Population growth rate', ax=ax)

mygrid[0][0].subheader("""
The world population will pass 8 billion at the end of 2022
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
