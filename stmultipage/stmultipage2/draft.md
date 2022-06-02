# 3 Ways to Create a Multi-Page Streamlit App

## Streamlit may not have been designed for full blown web sites but it is fairly straightforward to create multiple pages in a single app

There are two aspects to creating mutipage apps: how to select the one you want from the user interface and how to select which  code to run.

The UI could be option menu, drop down, buttons, or other UI element. Here we will use a Streamlit ``selectbox`` in a sidebar to select which part of the app to run.

To determine which code to run we will look at 3 different techniques:

 - Use a select statement such as `if... else...` or 3.10 pattern matching to choose which page to display. This is the easiest method and works well for a small number of pages.
 - Structure apps as a library package. A more sophisticated way of delivering multiple pages that is also easy to use - just follow the pattern.
 - A generic launcher app for a library of apps. This launcher will automatically pick up the apps stored in a library but is still easy to create and use.

 #### The pages

 In each case we will use the same two blocks of code that display data about a country or continent from the Gapminder data that is included with Plotly. So let's look at that code first.

 First let's we get the data:

```` Python
    df = pd.DataFrame(px.data.gapminder())
````

 The following code displays two graphs, one for the GDP per Capita for a country and the second for the Population Growth. The data is in the Pandas dataframe ``df`` and we first construct a unique list of country names from the dataframe. The country is then selected from a Streamlit ``selectbox``. We then draw the graphs in two columns so that they appear side by side.

```` Python
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
````

The next block of code is very similar but displays data for all countries in a continent. 

```` Python
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
````

So those are the two code blocks that will be our 2 'pages'. For the three solutions I'll show you the framework and indicate where those blocks of code go.

#### Simple selection

The first technique is very straightforward, we simple use an ``if... else...`` or Python 3.10 ``match`` statement to select the code to run. This is very easy but is probably better used for a small number of pages like the two we will use here.
```` Python
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
````
In this solution we define the pages as the functions ``countryData()`` and ``continentData()`` and we put an ``st.selectbox`` in a ``st.sidebar`` as the mechanism for choosing which code we will run. We then simply call the appropriate function depending on the value returned from the ``st.selectbox``.

If you are using Python 3.10 or above you can replace the ``if... else`` with a ``match`` statement something like this:

    match page:
        case 'Country data': countryData()
        case 'Continent data': continentData()

This construct is a bit neater particularly if you have more than a couple of pages.

#### Implement as a library

If you have several pages that you would like to choose from then putting all of the code in a single file gets a bit cumbersome. A better approach is to use the Python package mechanism to hold functions that can be imported into a main program.

The first thing you need to do is create a folder in which your pages will reside and configure this as a library. So first create a subfolder called ``stlib`` and then inside that create a file ``__init__.py``. This file can be empty, it just needs to be there to mark the folder as a library.

Now create two more files in the subfolder, one for the country data page and the other for the continent data page. We'll cal these files ``countryData.py`` and ``continentData.py``.
```` Python
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
````
The main code is coded as a function called ``run()``. It could be named anything but it helps having a standard name to invoke the function as we shall see later.

The last ``if`` statement is optional but if you include it you can run the module as a standalone program.

Now we have the 'pages' implemented as Python modules we can import them and call the ``run()`` function for each one.
```` Python
    message = """
            __Select an application from the list below__
            """

    import streamlit as st
    st.set_page_config(layout = "wide") # optional

    from stlib import countryData
    from stlib import continentData

    with st.sidebar:
        st.markdown(message)
        page = st.selectbox('Select:',['Country Data','Continent Data']) 

    if page == 'Country Data':
        countryData.run()
    else:
        continentData.run()
````
As I hope you can see this quite neat. It uses the same selection technique as in the previous example but the code is deployed in the library.

#### A generic solution

The library approach is quite attractive as it means we can devolve the functionality of 'pages' to a library of functions. However, we can go a step further by storing the module information in an external file (in the library) and construct a generic 'main' program that will read this file and construct the selection menu and call whichever modules are available.

The first thing to do is to create a file with the list of the available modules in the library folder. I've called it libContents.py and it looks like this:

```` Python
    # Return a list of the modules in this package
    def packages():
        return ['countryData','continentData']
````

It's a single function that returns the names of the of modules as a list.

There is a bit more code in this solution but it is much more flexible and you only need to write it once.

The code is shown below and the first thing to note is that we import ``libContents`` explicitly and later we declare the global arrays that will hold the list of modules (names, descriptions and module references). ``moduleNames`` is assigned directly from the ``libContents``, the others we will deal with in the loop that follows. The first thing is to get the module reference from its name using ``importlib.import_module``. We then look for a description of the module in a global string ``description``. If this exists we use store it in the ``descriptions`` list, otherwise we store the module name instead.

This means that the module can now contain a description like this:

````Python
description = "Continent Data"

def run():
    import streamlit as st

    # etc.
````

It not compulsory but if it is there it will be used in the drop down menu.

We are going to use the description in the ``st.selectbox``. This is similar to what we've seen before but it uses a function to define the text that is displayed rather than the actual value passed to it (this is very neat).

So the function ``format_func(name)`` takes the name of the module, finds its index in the ``moduleNames`` list and then uses this index to select the correct text to be displayed for the ``descriptions`` list.

Finally, the line

```` Python
    modules[moduleNames.index(page)].run()
````

Runs the selected module by retrieving the module reference, again by using the index of the module name. 

```` Python
    message = """
            __Select an application from the list below__
           """

    import json
    import streamlit as st
    import importlib
    import stlib    # default library name for apps
    from stlib import libContents

    st.set_page_config(layout = "wide") # optional

    st.header("National Statistics")

    # Global arrays for holding the app names, modules
    # and descriptions of the apps
    moduleNames = libContents.packages()
    descriptions = [] 
    modules = []

    # Find the apps and import them
    for modname in moduleNames:
        m = importlib.import_module('.'+modname,'stlib')
        modules.append(m)
        # If the module has a description attribute use that in the 
        # select box otherwise use the module name
        try:
            descriptions.append(m.description)
        except:
            descriptions.append(modname)

    # Define a function to display the app
    # descriptions instead of the module names
    # in the selctbox, below
    def format_func(name):
        return descriptions[moduleNames.index(name)]


    # Display the sidebar with a menu of apps
    with st.sidebar:
        st.markdown(message)
        page = st.selectbox('Select:',moduleNames, format_func=format_func) 

    # Run the chosen app
    modules[moduleNames.index(page)].run()
````

