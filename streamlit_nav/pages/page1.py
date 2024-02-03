import streamlit as st
import navbar

current_page = "Page 1"
st.header(current_page)

with st.sidebar: navbar.nav(current_page)
