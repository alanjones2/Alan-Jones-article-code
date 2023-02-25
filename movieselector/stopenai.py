import model

import streamlit as st
import os

actor = st.text_input("Enter an actor:")
prompt = model.generate_prompt(actor)

result = model.generate_response(prompt)
st.write(result)



