# How to Create a Grid Layout in Streamlit

## We present a method to programmatically create a grid layout in Streamlit

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/1_23w13JLGqofbNLlDajur5A.jpeg)

_Piet Mondrian, Public domain, via Wikimedia Commons_

The good folk at Streamlit have given us a lot of ways of displaying data and charts, and have also provided several methods for laying out an data science application.

But there is no native grid layout. Luckily, this is easily solved and we shall see how we can construct a grid using standard Streamlit layout functions and then create a simple function to draw a grid of arbitrary dimensions.

A grid lets us layout out text, data and charts in a neat and consistant way in rows and columns. I've created an example app using UN populaton data from Our World in Data which you can see here.

TK add reference to app

Streamlit, of course, has columns built in as standard. But rows? Yes, those too. If we stack a bunch of Streamlit containers on top of one another we have rows. If we then divide up each of those containers into the same number of columns, we have a grid.

Take a look at this code:

```` Python
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

````
_Listing 1_

It creates a 2 x 2 grid by stacking two containers and dividing each of them into two columns. Each row has a chart in the right column and a caption in the left column. The code is easy to follow and works well. The result looks like this:

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/Screenshot2x2grid.png)

The problem is that if we were to create a, for example, 10 x 10 grid, the code would get very cumbersome.

Wouldn't it be easier to create a grid that can be accessed as a two-dimesional array. So, instead of the explicit code that we see above, we could write something like:

```` Python
mygrid[0][0].write('Caption for first chart')
mygrid[0][1].line_chart((1,0), height=100)
mygrid[1][0].write('Caption for second chart')
mygrid[1][1].line_chart((0,1), height=100)
````
_Listing 2_

I think you might agree that this a more concise way of achieving the same thing and for a bigger grid would be much more managable.

So, a next step might look something like this:

```` Python
# 2x2 grid using an array

mygrid = [[],[]]

with st.container():
    mygrid[0] = st.columns(2)
with st.container():
    mygrid[1] = st.columns(2)

````
_Listing 3_

Here we create an empty two dimensional array and then, in each container, we assign two columns to that array. And this enables us to write code exactly as in _Listing 2_.

Again, though, while this works well, scaling it up to a larger grid will result in much more cumbersome code.

So, how about we write a function to create a two dimensional array of any dimensions, 2 x 2, 3 x 2, 10 x 10 - whatever.

Here it is:

```` Python
# make any grid with a function

def make_grid(cols,rows):
    grid = [0 for i in range(cols)]
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid
````

The function takes the number of rows and the number of coumns as parameters. Next it creates a one-dimensional array the size of the columns. (This is done using list comprehension and the list is initialised with zeroes - an arbitrary value that will be overwritten.)

Then for each of the elements of that array we create a Streamlit container and within that container we create the required number of rows (a list of rows) and assign it to each element of the one-dimensional array, thus creating a two-dimensional array of rows and columns that is returned from the function.

We can now write code that looks like this:

```` Python
mygrid = make_grid(5,5)

mygrid[0][0].write('00')
mygrid[1][1].write('11')
mygrid[2][2].write('22')
mygrid[3][3].write('33')
mygrid[4][4].write('44')
````

Which would create this:

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/Screenshot2x2grid.png)


### Notes
1. Data and edited text courtesy of, 
[Our World in Data](https://ourworldindata.org/world-population-update-2022), reproduced in accordance with Creative Commons Attribution 4.0 International ([CC BY 4](https://creativecommons.org/licenses/by/4.0/))