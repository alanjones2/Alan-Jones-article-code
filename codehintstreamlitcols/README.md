# Customizing st.columns

_This repo supports the Medium article [Customizing Streamlit Columns](https://medium.com/codefile/customizing-streamlit-columns-4bfd58fcb7c9)_

_See the demo app [here](https://share.streamlit.io/alanjones2/alan-jones-article-code/codehintstreamlitcols/stcols.py)_

Sometimes you want a little padding in between the column in a Streamlit app but there is no mechanism to do this expicitly.

The answer is to insert a blank column in between the ones you are using.

You use the construction

    col1, padding, col2 = st.columns((5,1,5))

this creates 3 columns, the outer two are the ones to use and the centre one is the padding.

You want the padding to be smaller? Just give more weight to the outer ones, e.g.

    col1, padding, col2 = st.columns((10,1,10))

Or how about a centred narrow column?

       padding1, col, padding2 = st.columns((5,5,5))

Or maybe calculate the number of columns you want dynamically.

    cols = st.columns(numCols)
    for c in range(numCols):
        with cols[c]:
            st.write(quotes[c])

Code to demonstrate these is in the file 

- stcols.py

And the actual app can be seen in the Streamlit Cloud [here](https://share.streamlit.io/alanjones2/alan-jones-article-code/codehintstreamlitcols/stcols.py)

---
### If you find this content useful, please consider one or more of the following:

-  ### Sign up for [Medium](https://medium.com/@alan-jones/membership) where you can read all my articles along with thousands of others for $5 a month (_affiliate link_).  
-  ### [Buy a book](https://alanjones.gumroad.com/)
-  ### Subscribe to my [free newsletter](https://technofile.substack.com/)
-  ### Visit my [web page](alanjones2.github.io)