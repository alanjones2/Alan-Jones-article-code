# Create an Interactive Web App with PyScript and Pandas

## PyScript allows us to create a serverless web application with HTML and Python as the scripting language.

![](https://raw.githubusercontent.com/alanjones2/Alan-Jones-article-code/master/pyscript/images/Screenshot2.png)

Is PyScript the future of web applications? Maybe, but probably yet - it's still only an alpha release and there is still a lot of work to do, I'm sure. 

But right now how useful it? 

We are going to create an interactive web application where the logic is entirely written in Python.

You've probably heard of PyScript, it was announced at the PyCon conference in 2022 by Anaconda’s CEO Peter Wang. And it their own [words](https://anaconda.cloud/pyscript-python-in-the-browser) it's "a shiny new technology... that allows users to write Python and in fact many languages in the browser".

The big advantage of PyScript is that you can write web applications in Python without the need for a server. This is achieved by using the Pyodide Python interpreter that is written in WebAssembly, the lower level language for the web that is supported by modern browsers. 

Up until now, Python web apps have been server based and use frameworks such as Django or Flask where the front end is created in HTML and Javascript while the back end is Python running on a remote server. 

More recently Dash and Streamlit have attempted to make building such apps easier by providing Python-only frameworks thus avoiding the need to learn HTML and Javascript. But these are still server based applications.

PyScript is a different approach. In PyScript the user interface is still constructed with HTML but Javascript is replaced with Python (although you can still use Javascript, if you wish, and functions written in two scripting languages can communicate with each other).

## The Web app

I'm going to run through a simple application written in PyScript and HTML that reads data from a remote source and displays a simple dashboard where the user can select data to be shown in a Pandas chart.

The basic form of the app looks like this:

    <html>
        <head>
            <link rel="stylesheet" 
                href="https://pyscript.net/alpha/pyscript.css" />
            <script defer 
                src="https://pyscript.net/alpha/pyscript.js">
            </script>
            <py-env>
                - libraries-that-will-be-used
            </py-env>
        </head>
        <body>

            <!-- HTML layout code goes here -->

            <py-script>
                # PyScript code goes here
            </py-script>
        </body>
    </html>

As you can see it looks similar to a standard HTML file, indeed it is one. But for PyScript app we need to include the links to the PyScript stylesheet and Javascript library in the `<head>` section, as well as including the `<py-env>` block that wee shall see later. 

Following that in the `<body>` we have the HTML layout content followed by the `<py-script>...</py-script>` tags that will contain the Python code.

We will now flesh out those sections.

First, I'm going to use the Bootstrap framework to make the whole app look nice. This means that we need to include the link to the Bootstrap css file. And we'll be using the Matplotlib and Pandas libraries, and those need to be declared in the `<py-env>...</pt-env>` section. The `<head>...</head>` now looks like this:

    <head>
        <link rel="stylesheet" 
            href="https://pyscript.net/alpha/pyscript.css" />
        <script defer 
            src="https://pyscript.net/alpha/pyscript.js">
        </script>
        <link rel="stylesheet" 
            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <py-env>
            - matplotlib
            - pandas
        </py-env>
    </head>

The next thing to look at is the HTML code for the web page. The first section is basically a header for the page. We utilize the _Jumbotron_ container from Bootstrap. This gives us a pleasing box with a grey background and some introductory text in the classic Bootstrap style.

    <div class="jumbotron">
        <h1>Weather Data</h1>
        <p class="lead">
            Some graphs about the weather in London in 2020
        </p>
    </div>

Following this there are two rows: the first has a button and a drop down menu and the second will contain the chart to be displayed.

Here's the first row:

    <div class="row">
        <div class="col-sm-2 p-2 ml-4 mb-1">
            <button type="button" class="btn btn-secondary">Select chart from list:</button>
        </div>

        <div class="col-sm-4 p-2 mr-4 mb-1">
            <select class="form-control" id="select">
                <option value="Tmax">Maximum Temperature</option>
                <option value="Tmin">Minimum Temperature</option>
                <option value="Sun">Sun</option>
                <option value="Rain">Rain</option>        
            </select>
        </div>
    </div>

It comprises two columns, one for the button and the second for the menu (I use a button here just for aesthetic purposes, it doesn't actually function as a button). The options in the drop down will be used to display one of four different charts. The data that will be used is a table of weather conditions in London[1] for the year 2020. There are 12 rows in the table representing each month and the columns in the table represent the _maximum temperature_ for that month, the _minimum temperature_, the number of _hours of sun_ and the amount of _rain in millimetres_.

So the menu items represent these options and will take a value of 'Tmax', 'Tmin', 'Sun' or 'Rain'.

So far we have coded the web page and now we need to define the logic that will react to the user input and draw the chart. This is defined in the `<py-script>` section. The code that we will deal with next goes inside this section.

First import some libraries.

    # Import libraries
    import pandas as pd
    import matplotlib.pyplot as plt

Pandas and Matplotlib, of course, but we also need the following:

    from pyodide.http import open_url

This is a library provided by PyScript that allows us to read from a source on the web and we use it like this:

    url = 'https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv'
    url_content = open_url(url)

    df = pd.read_csv(url_content)

The PyScript implementation the Pandas function `read_csv` isn't able to open the url directly, so we must use the technique above, instead.

The file being downloaded contains several decades of data but in order to keep things simple we will filter it to only hold the data for 2020.

    # filter the data for the year 2020
    df = df[df['Year']==2020]

Now the function to plot the chart in the HTML `div` that we saw earlier.

    # Function to plot the chart
    def plot(chart):
        fig, ax = plt.subplots()
        df.plot(y=chart, x='Month', figsize=(8,4),ax=ax)
        pyscript.write("chart1",fig)

This is pretty standard stuff for plotting with Pandas. The main difference from a 'normal' Python program is the way it is rendered. The `pyscript.write` function take the id of an HTML element and writes the content of the second parameter into it.

This relies on the PyScript implementation included a way of rendering the particular object - in this case a matplotlib chart - and this won't necessarily work with any type of object. For example, if we were to want to display a Plotly chart we would have to use a different technique as rendering a Plotly figure is not directly implemented in PyScript (as yet).

The next thing to do is to define a way of invoking the `plot` function when the user selects a new chart from the drop down menu.

First some more libraries - these are provided as part of PyScript.

    from js import document
    from pyodide import create_proxy

The `js` library aloows PyScript to access Javascript functions, in this particular case we are importing the ability to access the DOM. And  ´create_proxy` from Pyodide does the opposite allowing Javascript to directly call PyScript functions.

    def selectChange(event):
        choice = document.getElementById("select").value
        plot(choice)

This function is called when a change event occurs. It reads the value of the selection and then calls the previously defined `plot` function with that value.

Next we define a proxy that wiil allow the change event to call the PyScript function `selectChange`.

    # set the proxy
    def setup():
        # Create a JsProxy for the callback function
        change_proxy = create_proxy(selectChange)

        e = document.getElementById("select")
        e.addEventListener("change", change_proxy)

Finally, when the page first loads we need to call the `setup` function and run the `plot` function with a default value ('Tmax') in order that a chart is displayed on start up.

And that is the entire code that implements a simple dashboard app like the one in the screenshot at the beginning of the article. The code for this and a link to a demo app will be in a link at the end.

## How does PyScript compare with existing server-based applications? 

In terms of difficulty, as long as you are familiar with Python, constructing a web app is relatively straightforward, probably easier than building a Django or Flask app - more the level of Dash, I would suggest.

Streamlit is a different story, though. Streamlit is more limited on the visual design side but has the advantage that you do not have to learn HTML. Streamlit apps are very easy to create - easier than PyScript, I would say.

However, the advantage that PyScript has over all of its rivals is that it does not rely on a server. That makes deployment very easy - I simply uploaded the app you see here to a Github Pages site (for example) and it just works.

Currently PyScript is a little slow. Since all of the work is being done in the browser, performance is determined by the machine that is running the browser - if you have weak hardware then it may take a long time to load your app, although once it is up and running performance seems to be fine.

Performance will only get better, though, as hardware become more powerful and the PyScript matures and (hopefully) becomes more efficient. And one day, who knows, perhaps we'll see PyScript built into browsers in the same way that Javascript is today.

---

You can find a link to the code and the demo web page on my [web site](https://alanjones2.github.io/).

## Notes

1. The weather data is from my repo [uk-historical-weather](https://github.com/alanjones2/uk-historical-weather) and is derived from the UK Met Office [Historic Station Data](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data). It is distributed in accordance with [UK Open Government License](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) and may be used under the same conditions.