import os
import json

SURVEY_KEY = "survey.json"
RESULTS_KEY = "results.json"

def save_dict(value, key=SURVEY_KEY):
    print(f"Saving: {value}")
    #return None
    out_file = open(key, "w")
    json.dump(value,out_file)
    out_file.close()

def save_results(value):
    save_dict(value,RESULTS_KEY)

def save_survey(value):
    save_dict(value, SURVEY_KEY)

def retrieve(key):
    # file exists read it and return array of dict
    if os.path.isfile(key):
        in_file = open(key, "r")
        result = json.load(in_file)
        in_file.close()
        return result
    else:
        # File does not exist return an empty array
        return []

def get_survey(key=SURVEY_KEY):
    return retrieve(key)

def get_results(key=RESULTS_KEY):
    return retrieve(key)

def append_results(value):
    results = get_results()
    results.append(value)
    save_results(results)