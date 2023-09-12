import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def plt_waterfall(df, title, icolor = 'green', dcolor = 'red', tcolor = 'blue', ccolor = 'lightgrey', color = None):

    if color != None:
        ccolor = icolor = dcolor = tcolor = color
    # add columns
    df['tot'] = df['num'].cumsum()
    df['tot1']= df['tot'].shift(1).fillna(0)

    # add color column
    df.loc[df['num'] >= 0, 'color'] = icolor
    df.loc[df['num'] < 0, 'color'] = dcolor
    df

    # add a total row
    total = df['tot'][len(df.index)-1]
    df.loc[len(df.index)] = ['Total', total,0,0, tcolor] 

    fig,ax = plt.subplots()
    ax.bar(x=df['category'],height=df['num'],bottom= df['tot1'], color=df['color'])
    ax.bar(x=df['category'], height=df['tot1'], alpha = 0)

    # add text
    for i, v in enumerate(df['num']):
            plt.text(x = i-0.2, y =df['tot1'][i]+df['num'][i]/2 ,s=f"{df['num'][i]}")
            plt.hlines(df['tot1'][i], i-1, i, color = ccolor,linestyles='solid')

    ax.set_title(title)
    return fig

# example data
df = pd.DataFrame({'category':['Sales','Service','Expenses','Taxes','Interest'],
                   'num':[100,10,-20,-30,60]})
title = "Revenue"

st.pyplot(plt_waterfall(df, title))


