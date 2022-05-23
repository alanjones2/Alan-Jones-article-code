description = "Continent Data"

# Your app goes in the function run()


def run():

    import streamlit as st

    import pandas as pd
    import plotly.express as px

    df = pd.DataFrame(px.data.gapminder())

    # Continents

    contlist = df['continent'].unique()

    continent = st.selectbox("Select a continent:", contlist)

    col1, col2 = st.columns(2)
    fig = px.line(df[df['continent'] == continent],
                  x="year", y="gdpPercap",
                  title="GDP per Capita", color='country')
    col1.plotly_chart(fig)

    fig = px.line(df[df['continent'] == continent],
                  x="year", y="pop",
                  title="Population", color='country')
    col2.plotly_chart(fig)
# end of app


# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()
