# Waterfall charts with Plotly Graph Objects 

Plotly Express is the preferred library for drawing charts but it doesn't have a native waterfall chart. Plotly's Graphic Objects does have one but it is a little complex to use - there are a lot of parameters that need to be set.

The aim of this small project is to create a simple function that will make the typical use case for waterfall charts very easy to implement while still allowing for a fair amount of flexibility.

The code:

- plotlyhelper.py - this contains the `waterfall` function and can be imported as a library

- st_waterfall.py - this is a sample application in the form of a Streamlit app which also contians a Matplotlic implementation

- The other files have a variety of programs that the author was playing around with.