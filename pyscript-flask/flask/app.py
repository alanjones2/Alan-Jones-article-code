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