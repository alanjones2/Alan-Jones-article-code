import streamlit as st
import navbar

current_page = "Page 2"
st.header(current_page)

with st.sidebar:navbar.nav2(current_page)
