import streamlit as st

import pandas as pd
import plotly.express as px
import navbar

current_page = "Country Data"
st.header(current_page)

navbar.nav3(current_page)

df = pd.DataFrame(px.data.gapminder())

# Countries
clist = df['country'].unique()

country = st.selectbox("Select a country:", clist)

col1, col2 = st.columns(2)

fig = px.line(df[df['country'] == country],
                x="year", y="gdpPercap", title="GDP per Capita")
col1.plotly_chart(fig, use_container_width=True)

fig = px.line(df[df['country'] == country],
                x="year", y="pop", title="Population Growth")
col2.plotly_chart(fig, use_container_width=True)
