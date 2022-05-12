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

See other content on my [Github web page](https://alanjones2.github.io/)

If you find this content useful, please consider this... <br/><br/>
<a href='https://ko-fi.com/M4M64THKG' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi2.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>