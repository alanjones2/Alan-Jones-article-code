import streamlit as st

st.header("Multipage navigation")

if st.button("Home page"):
    st.switch_page("multipage-nav1.py")
if st.button("Page 1"):
    st.switch_page("pages/page1.py")
if st.button("Page 2"):
    st.switch_page("pages/page2.py")



