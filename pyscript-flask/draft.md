# PyScript v. Flask: How to Create a Python App in the Browser or on a Server 

## PyScript lets you to create web apps in Python without the need of server. Flask is a Python web app frame work for making server based apps. We write the same simple app using both.

PyScript is Python in the browser and promises a new way of writing web applications. It's very much at the _alpha_ stage at the moment but is already a usable system.

But do we need a new way? It's true that I can create a fully functioning web app in PyScript (with the help of some HTML and maybe a smattering of Javascript) but I can already do that with Flask! 

With Flask the Python code runs on the server and updates the web page as needed. With PyScript the Python code runs in the browser and interacts with the web page directly.

So, is it better or easier to use PyScript than a server based application? We are going too compare two similar applications one written in PyScript and the other using Flask, the Python based application framework. 

Is there any advantage to running code in the browser rather than on a server? The obvious answer is the one of deployment. A browser based app only needs to be copied to a web server and it will just work. A server based app, however, may need a little more effort to deploy it to a platform like Heroku, Azure or AWS.

The PyScript app yhat I use here has already featured in previous articles, so you can take a look at these to get a more in-depth view of how PyScript works (see Notes, below).

We'll look at the PyScript app first and then see how we construct something similar using Flask.

The app itself is fairly simple. It displays one of four charts that represent aspects of the weather in London, UK, in the year 2020. The charts are Maximum and Minimum monthly temperatures, rainfall and hours of sunshine and they use data from my UK Historical Weather repo on Github.

The user can select a chart from a drop down menu and the new chart will be displayed. In neither version of the app is the page refreshed: in the PyScript app a call to Python code reads the data and updates the chart, and in the Flask app, an asynchronous callback is made to the server which responds with the chart data which is used to update the chart.

Let's look at the code.

## The PyScript app

A PyScript app is a HTML web page and structure as follows:

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

Now let's see the the fisrt part of the body, the HTML and Javascript:

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
Without going into too much detail, we begin with a Bootstrap Jumbotron element that acts as a header. This is followed by a dropdown menu that allows the selection of the chart to be displayed.

## The Flask app


## Notes

1. The first articles contains the original web app that used Pandas for plotting. The second shows how to use Plotly to create a similar app.


    [Create an Interactive Web App with PyScript and Pandas](https://towardsdatascience.com/create-an-interactive-web-app-with-pyscript-and-pandas-3918ad2dada1)

    [How to use Ploty with PyScript](https://medium.com/technofile/how-to-use-ploty-with-pyscript-578d3b287293)

