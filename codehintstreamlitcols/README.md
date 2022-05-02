# Padding in st.columns

Sometimes you want a little padding in between the column in a Streamlit app but there is no mechanism to do this expicitly.

The answer is to insert a blank column in between the ones you are using.

You use the construction

    col1, padding, col2 = st.columns((5,1,5))

this creates 3 columns, the outer two are the ones to use and the centre one is the padding.

You want the padding to be smaller? Just give more weight to the outer ones, e.g.

    col1, padding, col2 = st.columns((10,1,10))

Or how about a cenred narrow column?

       padding1, col, padding2 = st.columns((5,5,5))