import streamlit as st
import pandas as pd
import json
import plotly
import plotly.express as px
import yfinance as yf

import time


# Return the JSON data for the Plotly graph
def gm(stock,period, interval):
    stk = yf.Ticker(stock)
  
    # Create a line graph
    df = stk.history(period=(period), interval=interval)
    df=df.reset_index()
    df.columns = ['Date-Time']+list(df.columns[1:])
    max = (df['Open'].max())
    min = (df['Open'].min())
    range = max - min
    margin = range * 0.05
    max = max + margin
    min = min - margin
    fig = px.area(df, x='Date-Time', y="Open",
        hover_data=("Open","Close","Volume"), 
        range_y=(min,max), template="seaborn" )

    return fig, stk

fig, stock = gm('GOOGL','1d','1m')

info = st.empty()
hilo = st.empty()
graph = st.empty()

while True:

    with info:
        st.write(f"""
        {stock.info['shortName']} 
        {stock.info['symbol']}
        {stock.info['dayHigh']}
        {stock.info['dayLow']}
        """)

    with hilo:
        st.metric(label="Day high/Day low", value=stock.info['dayHigh'], delta=stock.info['dayHigh']-stock.info['dayLow'])
    
    with graph:
        st.plotly_chart(fig, use_container_width=True)

    time.sleep(60)
