# PyScript v. Flask: How to Create a Python App in the Browser or on a Server 

## PyScript lets you create web apps in Python without the need for a server. Flask is a Python web app framework for making server-based apps. We write the same simple app using both.

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/pyscript-flask/splash.png)

PyScript is Python in the browser and promises a new way of writing web applications. It's very much at the _alpha_ stage at the moment but is already a usable system.

But do we need a new way? It's true that I can create a fully functioning web app in PyScript (with the help of some HTML and maybe a smattering of Javascript) but I can already do that with Flask! 

With Flask the Python code runs on the server and updates the web page as needed. With PyScript the Python code runs in the browser and interacts with the web page directly.

So, is it better or easier to use PyScript than a server based application? We are going to compare two similar applications one written in PyScript and the other using Flask, the Python based application framework. 

There is at least one advantage to running code in the browser and that is deployment. A browser based app only needs to be copied to a web server and it will just work. A server based app, however, may need a little more effort to deploy it to a platform like Heroku, Azure or AWS. But once you are used to deploying your server based apps, this doesn't really take much effort.

The PyScript app yhat I use here has already featured in previous articles, so you can take a look at these to get a more in-depth view of how PyScript works (see Notes, below).

We'll look at the PyScript app first and then see how we construct something similar using Flask.

The app itself is fairly simple but it incorporates all the basics of a dashboard type app: it allows user interaction, loads remore data, displays interactive charts and uses the Bootstrap UI framework to make everything look nice. 

Specifically, the app displays one of four charts that represent aspects of the weather in London, UK, in the year 2020. The charts are maximum and minimum monthly temperatures, rainfall and hours of sunshine, and they use data from my UK Historical Weather repo on Github.

The user can select a chart from a drop down menu and the new chart will be displayed. In neither version of the app is the page refreshed: in the PyScript app a call to Python code reads the data and updates the chart directly, and in the Flask app, an asynchronous callback is made to the server which responds with the data which is used to update the chart.

Let's look at the code.

## The PyScript app

A PyScript app is a HTML web page and is structured as follows:

```` HTML
<html>
    <head>
        # Include style sheets Javascript libraries, etc
        <py-env>
            # Python libraries to be used
        </py-env>
    </head>
    <body>
        # HTML and Javascript code
        <py-script>
            # PyScript code
        </py-script>
    </body>
</html>
````

https://gist.github.com/eaefc1e16c79f9965594cab930a6d7fb.git


The ``<head>`` tag contains al the usual stuff that you will find on a web page and also a reference to the PyScript css and Javascript files. The ``<body>`` tags contain the HTML for the page and any required Javascript, and the ``<py-script>`` contains - who'd have thought it - PyScript code.

The PyScript section can refer to an external file but because of CORS restrictions it won't work when running the file locally, it must be run on a server (although, of course, that server could be running on your local machine).

Here is a closer look at the head:

````HTML
<head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
    <py-env>
        - matplotlib
        - pandas
        - plotly
    </py-env>
</head>
````

https://gist.github.com/928db014f1ec92de120eacb22045b30f.git

We start with the references to the PyScript files that we need to run PyScript, followed by references to Boostrap and Plotly CDNs that will be used in the HTML.

The ``<py-env>`` simply lists the Python libraries that will be used in the ``<py-script>`` section.

Now let's see the the first part of the body, the HTML and Javascript:

```` HTML
<body>
    <div class="jumbotron">
        <h1>Weather Data</h1>
        <p class="lead">
            Some graphs about the weather in London in 2020
        </p>
    </div>
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
    <div class="row">
        <div class="col-sm-6 p-2 shadow ml-4 mr-4 mb-4 bg-white rounded">
            <div id="chart1"></div>
        </div>
    </div>
    <script type='text/javascript'>
        function plot(graph, chart) {
            var figure = JSON.parse(graph)
            Plotly.newPlot(chart, figure, {});
        }
    </script>
````

https://gist.github.com/af4a64267ee8c1a1bbde2bbb1204d944.git

Without going into too much detail, we begin with a Bootstrap Jumbotron element that acts as a header. This is followed by a dropdown menu that allows the selection of the chart to be displayed.

We then have a ``<div>`` that is the container for the chart and lastly a short Javascript function that takes the chart data and the id of the container, and plots the chart using the Plotly library. This function will be accessed directly from the Python code.

So that is basically the user interface sorted out. What remains is loading the remote data, filtering it to get the specific data that we want, and creating the chart data. All of this is achieved in Python.

Here is the PyScript section tha contains the Python code.

```` Python
<py-script>
        # Import libraries
        import pandas as pd
        import matplotlib.pyplot as plt
        import js
        import json
        import plotly
        import plotly.express as px
        
        ## Get the data
        from pyodide.http import open_url
        
        url = 'https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv'
        url_content = open_url(url)
        
        df = pd.read_csv(url_content)
        df = df[df['Year']==2020]
        
        def plot(chart):
            fig = px.line(df,
            x="Month", y=chart,
            width=800, height=400)
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            js.plot(graphJSON,"chart1")
                    
        from js import document
        from pyodide import create_proxy
        
        def selectChange(event):
            choice = document.getElementById("select").value
            plot(choice)
        
        def setup():
            # Create a JsProxy for the callback function
            change_proxy = create_proxy(selectChange)
            e = document.getElementById("select")
            e.addEventListener("change", change_proxy)
        
        setup()
        
        plot('Tmax')
    </py-script>
````
https://gist.github.com/d79f263cea384f208e3fcdcbe6a51900.git

First, as with any Python program, we import all of the libraries that we need.

To get the data we need to use the function ``open_url`` from the Pyodide package (PyScript is based on Pyodide and its library is integrated into PyScript). We can then create a Pandas dataframe from this data.

Next we filter the data. The dataframe currently contains data for several decades but we are only going to use that from the year 2020. This is what the following code will do for us. 

```` Python
df = df[df['Year']==2020]
````

The remainder of the code is mostly function definitions.

The function ``plot()`` creates the Plotly chart and uses the Javascript function to plot it in its container. It takes a single parameter that is used to select the chart that is to be displayed, creates the chart data with the Plotly Python package, and finally calls the Javascript function we saw earlier to display the chart in its container. 

Note how easy it is to call Javascript functions. We simply import the ``js`` library and all Javascript functions are available for us to use.

The next to functions rely on the ``imports`` that precede them. ``selectChange()`` is a function that will be called when the value from teh drop down menu is changed. It reads the new value from the ``<select>`` tag and the calls the Python ``plot()`` function that we just looked at to display the selected chart.

Notice that using ``document`` from the ``js`` package lets us query the DOM in exactly the same way as the built-in Javascript function.

Next we need to make the connection between the event generated by the user changing the selected value and this function. This is the job of  ``setup()``. First, this function creates a proxy for the Python function ``selectChange()`` which can be used by Javascript to directly cal that function. The proxy is called ``change_proxy``.

Next we set up an event listener to detect a change in the drop down menu and direct it to call the the ``selectChange`` function via the proxy that we just set up.

The last two lines simply run ``setup()`` to set up the proxy and event listener and call ``plot("Tmax")`` to display a chart by default.

This app may not feel very intuitive for those used to either conventional web page development or Python programming. But the design of a PyScript app is quite elegant: the user interface is defined by HTML and CSS (with a little help from Javascript) while the logic of the application is defined almost entirely in the PyScript section.

It seems to me that this is using the right tools for each job. HTML and CSS are all about how stuff is displayed while Python is for programming and the two should be, and are, kept separate.

## The Flask app

That separation is also found in a server based application, too. But in this case the Python logic runs on the server.

A basic Flask app consists of two components, the server based Python code and an HTML template. When the app is invoked, it returns the HTML template as a web page. It potentially also fills in fields in the template with values from the Python code, although we do not use that capability here.

If you are unfamiliar with Flask applications, I've written a brief introduction in the article  "[How to Create and Run a Flask App
](https://alan-jones.medium.com/how-to-create-and-run-a-flask-app-533b7b101c86)" and there is a more comprehensive introduction on the [Flask web site](https://flask.palletsprojects.com/en/2.1.x/quickstart/).

Briefly, the Python part of the Flask app defines endpoints and Python functions that determine what happens when these end points are addressed. Ths app defines two endpoints, the one that corresponds to the root and another that invokes a callback function.

The root endpoint simply returns the HTML template, while the callback endpoint loads the required data and returns the Plotly chart data for display on teh web page.

let's take a look at the HTML first.

```` HTML
<html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
</head>
<body>
    <div class="jumbotron">
        <h1>Weather Data</h1>
        <p class="lead">
            Some graphs about the weather in London in 2020
        </p>
    </div>

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

    <div class="row">
        <div class="col-sm-6 p-2 shadow ml-4 mr-4 mb-4 bg-white rounded">
            <div id="chart1"></div>
        </div>
    </div>

    <script type='text/javascript'>
        function plot(graph, chart) {
            var figure = JSON.parse(graph)
            Plotly.newPlot("chart1", figure, {});
        }

        async function callback(selection){
            let response = await fetch("/callback?data="+selection);
            if (response.ok) {
                let result = await response.json();  
                Plotly.newPlot('chart1', result, {});
            } else {
                alert(response.status);
            }
        }

        function selectChange(event){
            choice = document.getElementById("select").value
            callback(choice)
        }
        
        function setup(){
            e = document.getElementById("select")
            e.addEventListener("change", selectChange)
        }
    </script>

    <script>
        setup()
        callback("Tmax");
    </script>
</body>
</html>
````

https://gist.github.com/4ce6087e29a79cf9335d584743454e94.git

This file is functionally the same as the HTML part of the PyScript app. Indeed most of the code is the same except that the PyScript sections are missing.

Also, the event listener and the function called by it are now written in Javascript and, of course, no proxy is required.

The major change is the way that the Python code is accessed. This is done by invoking a callback function on the server.

I'll repeat this section of code here:

```` javascript
async function callback(selection){
    let response = await fetch("/callback?data="+selection);
    if (response.ok) {
        let result = await response.json();  
        Plotly.newPlot('chart1', result, {});
    } else {
        alert(response.status);
    }
}
````

https://gist.github.com/0293fa4f73d0e55ba00d10e17bbcccf1.git

This function is an ansybnchronous function, meaning that after it is invoked, execution of the app is not stopped but rather the function is allowed to continue in the background until it is finished. This is ideal for invoking server functions as we cannot be sure how long the server will take to respond and do not want to freeze the app while waiting for that response.

The callback endpoint on the server is called ``callback`` and expects to see a parameter calld ``data`` which will hold the value of the selection from the drop down menu.

The server will respond with the chart data in JSON format and this is used to plot the chart, as before, using the Ploty Javascript library.

This leaves the Python code on the server.

```` Python
from flask import Flask, config, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)
   
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return getGraph(request.args.get('data'))

def getGraph(chart="Tmax"):
    print(chart)
    url = 'https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv'
    
    df = pd.read_csv(url)
    df = df[df['Year']==2020]

    fig = px.line(df,
    x="Month", y=chart,
    width=800, height=400)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
````

https://gist.github.com/5dc12ce69692055444d2159ac06e4ced.git

We start with the imports and then we can see the definition of the two endpoints. The code is in this format:

```` Python
@app.route('/')
def index():
    # some code that returns a web page or other data
````

The first endpoint is the root and uses the Flask function ``render_template()`` to return the HTML template that we saw above.

The second endpoint is the callback function. This does not return a web page, just the data that the web page requires to update itself. It calls the function ``getGraph()`` which does the same job as the PyScript version, it loads and filters the data and then creates the chart data which is returned to the asynchronous Javascript function.

As, I hope you can see, the Flask app does precisely the same job as the PyScript version.

So why would you choose one method over the other?

## Conclusion

Both apps work and they look exactly the same. So, how do you choose which approach to use?

First, we should appreciate that this is a very simple application. A more complex app might download more data, might require a lot more processing, or might need a more sophisticated user interface.

But these examples illustrate the basic operations that are required for this type of app.

I've run both applications on a typical home laptop and they both work well. The PyScript app takes much longer to load but possibly has a marginally quicker response time. To be frank, there's not a lot of difference between them after you've waited for the PyScript version to load (which takes a few seconds). 

Basically, here are several variables in play here: 

- The speed of the internet connection will determine how quickly the request is made to the server and how fast the data gets back
- The power of the server. Most Servers are much more capable than any desktop or laptop
- The power of the user's computer. A weak piece of hardware will be slower than a more powerful one, of course, but this will have much more of an impact on the PyScript app where the processing is being done locally.

## And the winner is...

Both techniques are valid and useful. PyScript probably has a lot of development in front of it and will doubtless improve but, even now, it is  a good solution for lightweight apps.

If there is a lot of processing to be done then the server based solution is probably still the best approach, at the moment, but as hardware gets more powerful (which it always does) and PyScript improves, this situation may change.

PySript is another tool in the toolkit which looks promising. I doubt that it will replace server based applications completely but for apps where the back-end processing is within the capability of a typical host machine then PyScrip will probably find its niche.


## Notes

1. The first articles contains the original web app that used Pandas for plotting. The second shows how to use Plotly to create a similar app.


    [Create an Interactive Web App with PyScript and Pandas](https://towardsdatascience.com/create-an-interactive-web-app-with-pyscript-and-pandas-3918ad2dada1)

    [How to use Ploty with PyScript](https://medium.com/technofile/how-to-use-ploty-with-pyscript-578d3b287293)

2. The weather data is from my repo [uk-historical-weather](https://github.com/alanjones2/uk-historical-weather) and is derived from the UK Met Office [Historic Station Data](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data). It is distributed in accordance with [UK Open Government License](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) and may be used under the same conditions.
