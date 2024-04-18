import altair as alt
from vega_datasets import data

import deployaltair

cars = data.cars()

scatter_plot = alt.Chart(cars).mark_point().encode(
    alt.X('Acceleration:Q').scale(zero=False),
    y='Horsepower:Q'
).properties(height=600, width=800, title = "Cars: Acceleration and Horsepower" )

trend = scatter_plot.transform_regression('Acceleration', 'Horsepower').mark_line(color='red')
chart  = scatter_plot + trend

params = {'title':'Deploy Altair Chart as a web page',
          'subtitle':'Example of how to deploy an Altair chart to a custom HTML template',
          'description':"""
                Below is a scatter diagram with a regression line that explores the relationship between
                accleration an horsepower in the datasets 'cars' from vega datasets.
            """,
          'spec':chart.to_json(indent=None)
}
deployaltair.deploy('./page.html', './bs-simple.html', params)
