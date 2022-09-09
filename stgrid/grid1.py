import streamlit as st

# a 2x2 grid the long way

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write('Caption for first chart')
    with col2:
        st.line_chart((0,1), height=100)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write('Caption for second chart')
    with col2:
        st.line_chart((1,0), height=100)

st.markdown('---')

# 2x2 grid using an array

grid = [[],[]]

with st.container():
    grid[0] = st.columns(2)
with st.container():
    grid[1] = st.columns(2)

grid[0][0].write('Caption for first chart')
grid[0][1].line_chart((0,1), height=100)
grid[1][0].write('Caption for second chart')
grid[1][1].line_chart((1,0), height=100)

st.markdown('---')

# make any grid with a function

def make_grid(cols,rows):
    grid = [0 for i in range(cols)]
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid
        

mygrid = make_grid(5,5)

mygrid[0][0].write('00')
mygrid[1][1].write('11')
mygrid[2][2].write('22')
mygrid[3][3].write('33')
mygrid[4][4].write('44')

