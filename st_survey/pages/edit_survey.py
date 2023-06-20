import streamlit as st
import DButils

st.set_page_config(layout="wide")

if 'survey' not in st.session_state:
    st.session_state['survey'] = DButils.get_survey()

st.title("Questionaire editor")
st.write(
    """Type in the question text in the field below and then add a list of possible responses 
            (or you can leave, or edit, the default responses)."""
)



# with st.form("survey_form"):
default_response = (
    "Strongly agree,Agree,Neither agree not disagree,Disagree,Strongly disagree"
)

st.header("Question")
q_text = st.text_input("Question text")
q_responses = st.text_input(
    "A comma separated list of responses", value=default_response
)

submitted = st.button("Add question to survey")

if submitted:
    st.session_state['survey'].append(
        {
            "text": q_text,
            "responses": q_responses,
        }
    )

st.write("You can also edit the questions and response directly in the table.")

edited_df = st.data_editor(st.session_state['survey'], num_rows="dynamic")

save = st.button("Save changes")
if save:
    DButils.save_survey(edited_df)
    st.success(f"Changes saved")
