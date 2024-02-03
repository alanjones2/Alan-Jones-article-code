import streamlit as st

st.header("Multipage navigation")

col1, col2, col3 = st.columns(3)

if col1.button("Home page"):
    st.switch_page("multipage-nav3.py")
if col2.button("Page 1"):
    st.switch_page("pages/page1.py")
if col3.button("Page 2"):
    st.switch_page("pages/page2.py")


