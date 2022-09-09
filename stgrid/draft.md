# How to Create a Grid Layout in Streamlit

## We present a method to programmaticlly create a grid layout in Streamlit

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/1_23w13JLGqofbNLlDajur5A.jpeg)

_Piet Mondrian, Public domain, via Wikimedia Commons_

The good folk at Streamlit have given us a lot of ways of displaying data and charts, and have also provided several methods for laying an data science application.

There is no native grid layout. But this is easily solved and we shall see how we can construct a grid using standard Streamlit layout functions and then create a simple fuction to draw a grid of any dimensions.

A grid lets us layout out text, data and charts in a neat and consistant way in rows and columns.

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

It creates a 2 x 2 grid with two charts in the right column and captions in the left column. It's easy to follow and works well. The result looks like this:

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/stgrid/images/Screenshot2x2grid.png)

The problem is that if we were to create a, for example, 10 x 10 grid, the code would get very cumbersome.

What I'd like to do is to create a grid that can be accessed as a two-dimesional array. So instead of the explicit code that we see above, we could write something like:

```` Python
mygrid[0][0].write('Caption for first chart')
mygrid[0][1].line_chart((1,0), height=100)
mygrid[1][0].write('Caption for second chart')
mygrid[1][1].line_chart((0,1), height=100)
````

I think you will agree that this a concise way of achieving the same thing and for a much bigger grid would be much more managable.