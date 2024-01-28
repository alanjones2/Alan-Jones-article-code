import streamlit as st
import pandas
from openai import OpenAI

import time

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


client = OpenAI(api_key = st.text_input("API key"))

chosen_file = st.file_uploader("Choose a file")

# Upload a file with an "assistants" purpose
file = client.files.create(
  file=chosen_file,
  purpose='assistants'
)

# Create an assistant using the file ID
assistant = client.beta.assistants.create(
  instructions="You are a data analyst",
  model="gpt-4-1106-preview",
  tools=[{"type": "code_interpreter"}],
  file_ids=[file.id]
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="List the columns in the data file"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
)


#run = client.beta.threads.runs.retrieve(
#  thread_id=thread.id,
#  run_id=run.id
#)

if st.button("Run"): run = wait_on_run(run, thread)
st.json(run.model_dump_json())
#st.write(run)

messages = client.beta.threads.messages.list(thread_id=thread.id)
st.json(messages.model_dump_json())
#st.write(messages)






