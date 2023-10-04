# Import libraries
import pandas as pd
import plotly.express as px
import js

# Function to plot the chart
def plot(chart):
            fig = px.line(df,
            x="Year", y=chart,
            width=800, height=400)
            graphJSON = fig.to_json()
            js.plot(graphJSON,"chart1")
    

header = """World CO2 Emissions over Time"""
display(header, target="Header")

display("div1", target="div1")

df = pd.read_csv('./hadcrutworld.csv')

plot('Annual CO₂ emissions')


