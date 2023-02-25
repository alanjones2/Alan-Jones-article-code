import openai
import streamlit as st

openai.api_key = st.secrets["openai_api_key"]

def generate_response(actor):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(actor),
            temperature=0.6,
            max_tokens=256
        )
        print(response.choices)
        return response.choices[0].text


def generate_prompt(actor):
    return f"""List all films starring {actor} that have been released in the last 10 years
"""
    

