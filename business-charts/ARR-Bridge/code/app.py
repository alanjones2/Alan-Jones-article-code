import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")

df= pd.DataFrame(
        [
            [10.00, 2.00, 1.50, 0.50, -1.00, -0.50, 0],
            [0,.0, 0, 0, 0, 0, 0],
        ],
        columns=[
                "Opening ARR",
                "New Business",
                "Expansion",
                "Price Increases",
                "Churn",
                "Contraction",
                "Closing ARR"],
        index = [["2025","2026"]]
)

df['Closing ARR']=df.sum(axis=1)
df = df.loc["2025"]

values = [x for x in df.iloc[0]]
text_labels = [str(x) for x in values]

measure = ["relative"] * len(text_labels)
measure[0]="absolute"
measure[-1]="total"
categories = list(df.columns)

closing_ARR = df['Closing ARR'].values[0]
open_ARR = df['Opening ARR'].values[0]
churn = df['Churn'].values[0]
contraction = df['Contraction'].values[0]
expansion  =df['Expansion'].values[0]
price_increases = df['Price Increases'].values[0]

st.header(":color[Annual Recurring Revenue for ABC Software]{foreground='blue'}")

st.subheader("KPIs")

kpis = {
"ARR Growth": (closing_ARR-open_ARR)/open_ARR*100,
"Gross Revenue Retention": (open_ARR+churn+contraction)/open_ARR*100,
"Net Revenue Retention": (open_ARR+expansion+price_increases+churn+contraction)/open_ARR*100,
}
k = list(kpis.keys())
v = list(kpis.values())

cols = st.columns(len(k))
for i in range(len(k)):
    with cols[i]:
        st.metric(k[i],f"{v[i]}%", border=True)

st.subheader("Annual Recurring Revenue")

fig = go.Figure(go.Waterfall(
    measure = measure,
    x = categories,
    textposition = "outside",
    text = text_labels,
    y = values,   
))


st.plotly_chart(fig)