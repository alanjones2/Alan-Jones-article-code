import streamlit as st

st.set_page_config(page_title=None, page_icon=None, layout="wide")

# make any grid with a function

def make_grid(cols,rows):
    grid = [0 for i in range(cols)]
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid
        

mygrid = make_grid(5,2)

mygrid[0][0].subheader("""
The world population will pass 8 billion at the end of 2022
""")
mygrid[0][0].write("""
Since 1975 the world has been adding another billion people every 12 years. 
It passed its last milestone – 7 billion in 2011. And, by the end of 2022, it will pass another one: there will be 8 billion people in the world.

While this rate of absolute growth is similar to previous decades, the growth rate continues to fall. Since 2019, the global population growth rate has fallen below 1%. 

That’s less than half its peak rate of growth – of 2.3% – in the 1960s.

As global fertility rates continue to fall (see below), this rate will continue to fall.

""")

mygrid[0][1].image('images/population-and-demography.png')
mygrid[1][0].write('10')
mygrid[1][1].write('11')
mygrid[2][0].write('20')
mygrid[2][1].write('21')
mygrid[3][0].write('30')
mygrid[3][1].write('31')
mygrid[4][0].write('40')
mygrid[4][1].write('41')

