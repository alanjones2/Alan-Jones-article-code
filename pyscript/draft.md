# Create an Interactive Web App with PyScript and Pandas

## PyScript allows us to create a serverless web application with HTML and Python as the scripting language.

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/PyScript/images/Screenshot2.png)

Is PyScript the future of web applications? Maybe, though probably yet - it's still only an alpha release and there is probably still a lot of work to do. 

But we are going to see how useful it is right now by creating an interactive web application where the logic is entirely written in Python.

The big advantage of PyScript is that you can write web applications in Python without the need for a server. Python web apps have usually been server based and use frameworks such as Django or Flask where the front end is created in HTML and Javascript while the back end is Python running on a remote server. 

More recently Dash and Streamlit have attempted to make building such apps easier by providing Python-only frameworks thus avoiding the need to learn HTML and Javascript. But these are still server based applications.

PyScript is a different approach. In PyScript the user interface is still constructed with HTML but Javascript is replaced with Python (although you can still use Javascript, if you wish, and functions written in two scripting languages can communicate with each other).

## The Web app

I'm going to run through a application written in PyScript and HTML that reads data from a remote source and displays a simple dashboard where the user can select data to be shown in a Pandas chart.

The basic form of the app looks like this:

    <html>
        <head>
            <link rel="stylesheet" 
                href="https://pyscript.net/alpha/pyscript.css" />
            <script defer 
                src="https://pyscript.net/alpha/pyscript.js">
            </script>
            <py-env>
                - libraries-that-wil-be-used
            </py-env>
        </head>
        <body>

            <!-- HTML layout code goes here -->

            <py-script>
                # PyScript code goes here
            </py-script>
        </body>
    </html>

As you can see it looks similar to a standard HTML file, indeed it is one. But for PyScript app we need to include the links to the PyScript stylesheet and Javascript library in the `<head>` section. Following that in the `<body>` we see the HTML layout content followed by the `<py-script>...</py-script>` tags that will contain the Python code.

We will now flesh out those sections.

First, I'm going to use the Bootstrap framework to make the whole app look nice. This means that we need to include the link to the Bootstrap css file. And we'll be using the Matplotlib and Pandas libraries, so we need to declare that in the `<py-env>...</pt-env>` section. S the `<head>...</head>` now looks like this:

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

The next thing to look at is the HTML code for the web page. The first section is basically a header for the page. We utilize the _Jumbotron_ container from Bootstrap. This gives us a pleasing box with a grey background and some introductory text in the classic  Bootstrap style.

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

It comprise of two columns, one for the button and the second for the menu (I use a button here just for aesthetic purposes, it doesn't actually function as a button). The options in the drop down will be used to display one of four different charts. The data that will be used is a table of weather conditions in London[1] for the year 2020. There are 12 rows in the table representing each month and the columns in the table represent the maximum temperature that month, the minimum temperature, the number of hours of sun and the amount of rain in millimetres.

So the menu items represent these options and will take a value of 'Tmax', 'Tmin', 'Sun' or 'Rain'.

---

## How does PyScript compare with existing server-based applications? 

In terms of difficulty, as long as you are familiar with Python, constructing a web app is relatively straightforward, probably easier than building a Django or Flask app - more the level of Dash, I would suggest.

Streamlit is a different story, though. Streamlit is more limited on the visual design side but has the advantage that you do not have to learn HTML. Streamlit apps are very easy to create easier than PyScript.

Howver, the advantage that PyScript has over all of its rivals is that it does not rely on a server. That makes deployment very easy - I simply uploaded the app you see here to a Github Pages site ad it just works.

Currently PyScript is a little slow. Since all of the work is being done in the browser, performance is determined by the machine that is running the browser - if you have weak hardware then it may take a long time to load your app, although once it is up and running performance is fine.

Performance will only get better, though, as hardware become more powerful and the PyScript matures and (hopefully) becomes more efficient. And one day, who knows, perhaps we'll see PyScript built into browsers in the same way that Javascript is today.

## Notes

1. The weather data is from my repo [uk-historical-weather](https://github.com/alanjones2/uk-historical-weather) and is derived from the UK Met Office [Historic Station Data](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data). It is distributed in accordance with [UK Open Government License](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) and may be used under the same conditions.