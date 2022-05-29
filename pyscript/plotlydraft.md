# How to use Ploty with PyScript

## PyScript doesn't support Plotly directly but there is a simple way around it

![](https://raw.githubusercontent.com/alanjones2/Alan-Jones-article-code/master/pyscript/images/Screenshot2.png)

PyScript is a great idea - it let's you write serverless web applicationa entirely in Python and HTML.

I wrote an introductory article, [Create an Interactive Web App with PyScript and Pandas](https://towardsdatascience.com/create-an-interactive-web-app-with-pyscript-and-pandas-3918ad2dada1), which describes how to write a fairly simple dashboard type app using the Pandas plotting functionality. But thought it would be a good idea to do a Plotly version of the same things.

Please take a look at the original article to familiarize yourself with the basic anatomy of a PyScript app as I'll be building on that to produce the Plotly version.

## The Web app

I'm going to run through a simple application written mostly in PyScript and HTML that reads data from a remote source and displays a simple dashboard where the user can select data to be shown in a Plotly chart.

My original app created charts using Pandas and rendering these in PyScript is built-in. You just have to `write` the resulting Matplotlib figure to the HTML tag where it should be displayed.

Things are a little more complicated when using Ploty because this support is _not_ built in to PyScript. However, a slight modiifcation to the Python program and the addition of a couple of lines of Javascript solves the problem.

I'm assuming that you are familiar with the basic layout of a PyScript program (which is described in the original [article](https://towardsdatascience.com/create-an-interactive-web-app-with-pyscript-and-pandas-3918ad2dada1)).

Here is the `<head>` of the HTML part.

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
            - plotly
        </py-env>
    </head>

It's the same as the original except that `<py-env>` now refers to the Plotly library.

The rest of the HTML is the same as the original, so I won't reproduce it here (you find a link to the entire code at the end), except we need a small javascript function to call the Plotly library. This goes at the the end of the HTML and just before the Python section.

    <script type='text/javascript'>
        function plot(graph, chart) {
            var figure = JSON.parse(graph)
            Plotly.newPlot(chart, figure, {});
        }
    </script>


So far we have coded the web page and now we need to define the logic that will react to the user input and draw the chart. This is defined in the `<py-script>` section. The code that we will deal with next goes inside this section.

First import some libraries. This time we have added imports for Plotly and JSON packages.

    # Import libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    import js
    import json
    import plotly
    import plotly.express as px

And as before...

    from pyodide.http import open_url

The rest of the Python code is the same as before with the exception of the `plot` function

    def plot(chart):
        fig = px.line(df,
        x="Month", y=chart,
        width=800, height=400)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        js.plot(graphJSON,"chart1")

This function uses the Plotly package to draw the charts but Instead of writing the resulting figure directly to the `<div>` it creates a JSON representation of the chart and passes it to the Javascript function that we defined earlier (along with the id of the `<div>` where it should go).

And those are the changes that we need to make to use Plotly instead of Pandas plotting. I hope it was useful.

---

You can find a link to the code and the demo web page on my [web site](https://alanjones2.github.io/).

## Notes

1. The weather data is from my repo [uk-historical-weather](https://github.com/alanjones2/uk-historical-weather) and is derived from the UK Met Office [Historic Station Data](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data). It is distributed in accordance with [UK Open Government License](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) and may be used under the same conditions.