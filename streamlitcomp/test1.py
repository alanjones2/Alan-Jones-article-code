from urllib.request import AbstractBasicAuthHandler
import streamlit as st
import bs4st.content as bs 

for i in [1,2,3,4,5,6]:
    bs.header("hello","green",i)

for i in ["alert-primary","alert-secondary"]:
    bs.alert("alert!!!!",i)

for i in [1,2,3,4,5,6]:
    bs.display("hello","red",i)


bs.lead("lead text")

bs.write("bs write text")
st.write("st write text")


