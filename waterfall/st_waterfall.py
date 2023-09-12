import streamlit as st
import plotlyhelper as ph

st.set_page_config(layout='wide')

st.title("Waterfall graphs with Plotly")

col1, col2 = st.columns(2)

labels = ["Beginning HC", "Hires", "Transfers in", "Transfers out", "Exits", "Ending HC"]
data = [100, 30, 8, -12, -10, 0 ]
title = "Headcount"

fig = ph.waterfall(labels,data, title)

col1.plotly_chart(fig)

fig = ph.waterfall(labels,data, title, color = 'blue')

col2.plotly_chart(fig)

##
labels = ["Beginning HC", "Hires", "Transfers out", "Transfers in", "Exits", "Ending HC"]
data = [50, 30, -12, 8, -10, 0 ]
title = "Headcount"

fig = ph.waterfall(labels,data, title)

st.plotly_chart(fig)

fig = ph.waterfall(labels,data, title, color = 'blue')

st.plotly_chart(fig)

##

labels = ["Start balance", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"]
data = [20, 80, 10, -40, -20, 0 ]
title = "Sales revenue"

fig = ph.waterfall(labels,data, title)

st.plotly_chart(fig)

# Single color
st.header("Single colour")

fig = ph.waterfall(labels,data, title, color = 'blue')

st.plotly_chart(fig)

## colors
st.header("Changing the colour scheme")
fig = ph.waterfall(labels,data, title, icolor = 'orange', dcolor = 'pink', tcolor = 'yellow', ccolor='red')

st.plotly_chart(fig)

## annotation

st.header("Annotations")

annotation = ["Start","","","","","End"]

labels = ["Start balance", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"]
data = [20, 80, 10, -40, -20, 0 ]
title = "Sales revenue"

fig = ph.waterfall(labels,data, title, annotation=annotation)

st.plotly_chart(fig)

### multiple time periods
st.header("Multiple time periods")

labels = ["Year beginning", "Profit1", "Loss1", "Q1", "Profit2", "Loss2", "Q2"]
data = [100, 50, -20, 130, 40, -10, 0 ]
#annotation = []
measure = ['relative','relative', 'relative','total', 'relative','relative','total']
title = "Profit/Loss"

fig = ph.waterfall(labels,data, title, measure=measure)

st.plotly_chart(fig)


##################################################

# Just for comparison here is a similar chart in Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

st.header("...with Matplotlib")

def plt_waterfall(df, title, icolor = 'green', dcolor = 'red', tcolor = 'blue', ccolor = 'lightgrey', color = None):

    if color != None:
        ccolor = icolor = dcolor = tcolor = color
    # add columns
    df['tot'] = df['num'].cumsum()
    df['tot1']= df['tot'].shift(1).fillna(0)

    # add color column
    df.loc[df['num'] >= 0, 'color'] = icolor
    df.loc[df['num'] < 0, 'color'] = dcolor

    # add a total row
    total = df['tot'][len(df.index)-1]
    df.loc[len(df.index)] = ['Total', total,0,0, tcolor] 

    fig,ax = plt.subplots(figsize=(12, 6))
    ax.bar(x=df['category'],height=df['num'],bottom= df['tot1'], color=df['color'])
    ax.bar(x=df['category'], height=df['tot1'], alpha = 0)

    # add text
    for i, v in enumerate(df['num']):
            plt.text(x = i-0.2, y =df['tot1'][i]+df['num'][i]/2 ,s=f"{df['num'][i]}")
            plt.hlines(df['tot1'][i], i-1, i, color = ccolor,linestyles='solid')

    ax.set_title(title)
    return fig

# example data
df = pd.DataFrame({'category':["Start balance", "Consulting", "Net revenue", "Purchases", "Other expenses"],
                   'num':[20, 80, 10, -40, -20 ]})
title = "Sales Revenue"

st.pyplot(plt_waterfall(df, title))

df = pd.DataFrame({'category':["Start balance", "Consulting", "Net revenue", "Purchases", "Other expenses"],
                   'num':[20, 80, 10, -40, -20 ]})
title = "Sales Revenue"

st.pyplot(plt_waterfall(df, title, color='blue'))

