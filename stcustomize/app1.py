import streamlit as st

def st_setup(header):

    bs = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">'

    st.markdown(bs,unsafe_allow_html=True)

    hide_header = """
        <style>
            #MainMenu {display: none;}
            header {visibility: hidden;}
            footer {display: none;}
            .stApp {background-color: darkgrey;}
            .stApp, h1, h2, h3, h4, h5, h6 {
                color: white;}
     
        </style>
    """
    st.markdown(hide_header, unsafe_allow_html=True)

    head = f"""
    <div class="lead p-3 mb-5 bg-secondary bg-gradient text-white">
    {header} 
    </div>
    """

    st.markdown(head, unsafe_allow_html=True)

##################

st.set_page_config(layout="wide")

st_setup("Custom header")
st.title("title")

col_main1, col_main2 = st.columns((2,1))
with col_main1:
    st.info("# Visualizing 'Brexit Regret'")
    st.markdown("Which way would you vote if there were another Brexit referendum?'")

    st.write("#### We are going to look at the results of a poll that asked 'Which way would you vote if there were another EU referendum'.")
    st.write("This should be viewed in conjunction with the article on [Medium]()")
    st.write("The data used here is a subset of the data derived from the polling data referred to in the article.")
    st.info("### Select one of the tabs below for the results:")


st.markdown("""
<div class="alert alert-dark" role="alert">
  A simple dark alert—check it out!
</div>
""", unsafe_allow_html=True)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
