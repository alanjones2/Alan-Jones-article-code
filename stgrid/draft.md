# How to Create a Grid Layout in Streamlit

## We present a method to programmatically create a grid layout in Streamlit

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/1_23w13JLGqofbNLlDajur5A.jpeg)

_Piet Mondrian, Public domain, via Wikimedia Commons_

The good folk at Streamlit have given us a lot of ways of displaying data and charts, and have also provided several methods for laying out a data science application.

But there is no native grid layout. 

Luckily, this is easily solved and we shall see how we can construct a grid using standard Streamlit layout functions and then create a simple function to create a grid of arbitrary dimensions.

A grid lets us layout out text, data and charts in a neat and consistant way in rows and columns. As an example, I've created a Streamlit app using data from the 2022 UN's _World Population Prospects_ report. Among other things, this report looks at how the World's population will grow over the next few decades. The app is based on an article from Our World in Data (see note 1) and looks like this:

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/ScreenshotApp.png)

TK add reference to app

## Constructing a grid layout

We'll take a look at the way the app is structured a little later but first we'll take a look at how we can construct a grid layout in Streamlit.

Streamlit, of course, has columns built in as standard. But rows? Actually, yes, those too. If we stack a bunch of Streamlit containers on top of one another we have rows. If we then divide up each of those containers into the same number of columns, we have a grid.

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

This works well for this simple application but if we were to create a, for example, 10 x 10 grid, the code could get very cumbersome.

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

Here we create an empty two dimensional array and then, in each, we use container and assign two columns to each array element. This gives us a two dimensional array and this enables us to write code exactly as in _Listing 2_.

Again, though, while this works well, scaling it up to a larger grid will result in much more cumbersome code.

## A generic solution

So, how about we write a function to create a two dimensional array of any dimensions, 2 x 2, 3 x 2, 10 x 10 - whatever.

Here it is:

```` Python
# make any grid with a function

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid
````
_Listing 4_

The function in _Listing 4_ takes the number of rows and the number of columns as parameters. Next it creates a one-dimensional array the size of the columns. (The list is initialised with zeroes - an arbitrary value that will be overwritten.)

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
_Listing 5_

Which would create this:

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/Screenshot5x5grid.png)

We can, of course use any appropriate Streamlit function with these grid elements so executing this after the code in _Listing 5_

```` Python
mygrid[2][2].line_chart((0,1), height=100)
````
_Listing 6_

would give you this:

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/Screenshot5x5withchart.png)

So here we have a general way of creating a grid layout of any size and shape. Let's see how I've used it in practice in the World Population app.

## The example app

TK add app description



## Conclusion

Maybe Streamlit will add a grid layout in the future. But until then, I hope you will find this useful.

You can find the full listing of all the code used here and the app on from my [Github web page](https://alanjones2.github.io) and there is a gist of the app code at the very end of the article.

Thanks for reading.


## Notes
1. Data and edited text courtesy of, 
[Our World in Data](https://ourworldindata.org/world-population-update-2022), reproduced in accordance with Creative Commons Attribution 4.0 International ([CC BY 4](https://creativecommons.org/licenses/by/4.0/))

## Listing for the example app
https://gist.github.com/alanjones2/b2574d866d0b19c4d14771a0a72dd746