
import streamlit as st
import plotly.express as px
import pandas as pd

import DButils

st.set_page_config(layout="wide")


st.info("## Here are the results:")

st.write("The results are presented as a dataframe.")

# Read data from Databutton's datastore
results = DButils.get_results()
st.dataframe(results, use_container_width=True)

df = pd.DataFrame(results)

st.download_button(
    label="Download data as CSV",
    data=df.to_csv().encode("utf-8"),
    file_name="survey_results.csv",
    mime="text/csv",
)


# Plot a summary bar graph

fig = px.bar(results, title="Survey responses - overview")
fig.update_xaxes(title_text="Response")
fig.update_yaxes(title_text="Count")
st.plotly_chart(fig)

# Create an array of bar graph figures
# one for each response (data column) 

figures = []

for q in df.columns:
    fig = px.bar(df[q], title=q)
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title_text="Response")
    fig.update_yaxes(title_text="Count")
    # st.plotly_chart(fig)
    figures.append(fig)

# Choose which graph to display with a set of radio buttons

st.info("### Choose the graph for a specific question")
f = st.radio("Choose a graph", options=df.columns)
column_index = df.columns.get_loc(f)
st.plotly_chart(figures[column_index])
