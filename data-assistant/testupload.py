import streamlit as st
if 'count' not in st.session_state:
    st.session_state['count'] = 0
else:
    st.session_state['count'] = st.session_state['count'] + 1
st.header(f"Run: {st.session_state.count}")
st.write(st.session_state) 




if 'data_file' not in st.session_state:
    st.write("You need to upload a file")
    if data_file := st.file_uploader("Upload a file"):
        st.session_state.data_file = data_file

else: st.session_state.data_file