import streamlit as st
import streamlit.components.v1 as components
import plotly

def plotly_chart(fig):
    graphJSON = fig.to_json()
    components.html(f"""
        <div id="chart"></div>
        <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
        <script type='text/javascript'>
            var figure = JSON.parse('{graphJSON}');
            Plotly.newPlot("chart", figure);
        </script>
        """, 
        height=fig.layout.height, width=fig.layout.width)
    
def plotly_chart_md(fig):
    graphJSON = fig.to_json()
    st.markdown(f"""
        <div id="chart"></div>
        <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
        <script type='text/javascript'>
            var figure = JSON.parse('{graphJSON}');
            Plotly.newPlot("chart", figure);
        </script>
        """, unsafe_allow_html=True)