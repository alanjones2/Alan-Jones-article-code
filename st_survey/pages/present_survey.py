import pandas as pd
import streamlit as st

import DButils

st.info("## Select the answer to each question and then click on 'Submit'")
questions = DButils.get_survey()

responses = {}

for q in questions:
    response = st.radio(label=q['text'], options=q['responses'].split(","))
    responses[q['text']] = response.strip()

if st.button("Submit"):
    entry = responses
    DButils.append_results(entry)

    st.write("Updated")
