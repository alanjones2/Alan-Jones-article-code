import streamlit as st
from pymongo.mongo_client import MongoClient

DB = "survey"
SURVEY_KEY = "survey1"
RESULTS_KEY = "results1"

uri = st.secrets['mongoURI']
client = MongoClient(uri)
db = client[DB]

# Get functions
def get(key):
    coll = db[key]
    item_details = coll.find({},{'_id':False})
    st.write(list(item_details))
    return list(item_details)

def get_survey(key=SURVEY_KEY):
    return get(key)

def get_results(key=RESULTS_KEY):
    return get(key)

# Append results function
def append_results(value):
    coll = db[RESULTS_KEY]
    coll.insert_one(value)
