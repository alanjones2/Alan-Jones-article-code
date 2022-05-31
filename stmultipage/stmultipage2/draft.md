# 3 Ways to Create a Multi-Page Streamlit App

## Streamlit may not have been designed for full blown web sites but it is fairly straightforward to create multiple pages in a single app

There are two aspects to creating mutipage apps: how to select the one you want from the user interface and how to select which  code to run.

The UI could be option menu, drop down, buttons, or other UI element. Here we will use a Streamlit ``selectbox`` in a sidebar to select which part of the app to run.

To determine which code to run we will look at 3 different techniques:

 - Use a select statement such as `if else` or 3.10 pattern matching to choose which page to display. This is the easiest method and works well for a small number of pages.
 - Structure apps as a library package. A more sophisticated way of delivering multiple pages that is also easy to use - just follow the pattern.
 - A generic launcher app for a library of apps. This launcher will automatically pick up the apps stored in a library but is still easy to create and use.

 #### The pages

 In each case we will use the same two blocks of code that display data about a country or continent from the Gapminder data that is included with Plotly. So let's look at that code first.

 First let's we get the data:

    df = pd.DataFrame(px.data.gapminder())

 The following code displays two graphs, one for the GDP per Capita for a country and the second for the Population Growth. The data is in the Pandas dataframe ``df`` and we first construct a unique list of country names from the dataframe. The country is then selected from a Streamlit ``selectbox``. We then draw the graphs in two columns so that they appear side by side.

     # Countries
	clist = df['country'].unique()

	country = st.selectbox("Select a country:", clist)

	col1, col2 = st.columns(2)

	fig = px.line(df[df['country'] == country],
		x="year", y="gdpPercap", title="GDP per Capita")
	col1.plotly_chart(fig, use_container_width=True)

	fig = px.line(df[df['country'] == country],
		x="year", y="pop", title="Population Growth")
	col2.plotly_chart(fig, use_container_width=True)

The next block of code is very similar but displays data for all countries in a continent. 

    # Continents
    contlist = df['continent'].unique()
    continent = st.selectbox("Select a continent:", contlist)

    col1, col2 = st.columns(2)

    fig = px.line(df[df['continent'] == continent], 
		x = "year", y = "gdpPercap",
		title = "GDP per Capita",color = 'country')
    col1.plotly_chart(fig)

    fig = px.line(df[df['continent'] == continent], 
		x = "year", y = "pop",
		title = "Population",color = 'country')
    col2.plotly_chart(fig)


So those are the two code blocks that will be our 2 'pages'. For the three solutions I'll show you the framework and indicate where those block of code go.

#### Simple selection

The first technique is very straightforward, we simple use an ``if... else`` or Python 3.10 ``match`` statement to select the code to run. This is very easy but is probably better used for a small number of pages like the two we will use here.

    import streamlit as st
    import pandas as pd
    import plotly.express as px

    st.set_page_config(layout="wide")

    df = pd.DataFrame(px.data.gapminder())


    def countryData():
        # Countries code goes here

    def continentData():
        # Continents code goes here

    st.header("National Statistics")

    page = st.sidebar.selectbox('Select page',['Country data','Continent data']) 

    if page == 'Country data':
        countryData()
    else:
        continentData()

In this solution we define the pages as the functions ``countryData()`` and ``continentData()`` and we put an ``st.selectbox`` in a ``st.sidebar`` as the mechanism for choosing which code we will run. We then simply call the appropriate function depending on the value returned from the ``st.selectbox``.

If you are using Python 3.10 or above you can replace the ``if... else`` with a ``match`` statement something like this:

    match page:
        case 'Country data': countryData()
        case 'Continent data': continentData()

This construct is a bit neater particularly if you have more than two pages.

#### Implement as a library

If you have several pages that you would like t choose from then putting all of the code in a single file gets a bit cumbersome. A better approach is to use the Python package mechanism to hold functions that can be imported into a main program.

The first thing you need to do is create a folder in which your pages will reside and configure this as a library. So first create a subfolder called ``stlib`` and then inside that create a file ``__init__.py``. This file can be empty, it just needs to be there to mark the folder as a library.

Now create to more files in the subfolder, one for the country data page and the other for the continent data page. We'll cal these files ``countryData.py`` and ``continentData.py``.

    def run():

        import streamlit as st

        import pandas as pd
        import plotly.express as px

        df = pd.DataFrame(px.data.gapminder())

        # Continents code goes here

    # This code allows you to run the app standalone
    # as well as part of a library of apps
    if __name__ == "__main__":
        run()


mp1 is simple if/else and inline code
mp2 is like mp1 but with 3.10 pattern matching
mp3 explicitly imports the modules and uses if/else to run them
mp4 reads the module manes from a library function, loads the modules and runs them by matching the strings in the drop down menu