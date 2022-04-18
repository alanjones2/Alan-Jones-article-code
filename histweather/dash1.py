import pandas as pd
import streamlit as st
import plotly.express as px




dFile = st.text_input('Data file','Heathrowyearly.csv')

df = pd.read_csv(dFile)

df