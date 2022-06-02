##################################################
# Mustrapp - Multi-app Streamlit Application
#
#
# Copyright 2021 Alan Jones (https://alanjones2.github.io/)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

# Do not change this code except for the message below
# which can be plain text or any markdown code and will
# be displayed above the selection box
#
# individual apps must be in the library folder 'stlib'
# all modules in the library will be imported unless their
# name begins with the _ character
#

message = """
        __Select an application from the list below__
        """

#import json
import streamlit as st
import importlib
import stlib    # default library name for apps
from stlib import libContents

st.set_page_config(layout = "wide") # optional

st.header("National Statistics")

# Global arrays for holding the app names, modules and descriptions of the apps
moduleNames = libContents.packages()
descriptions = [] 
modules = []

# Find the apps and import them
for modname in moduleNames:
    m = importlib.import_module('.'+modname,'stlib')
    modules.append(m)
    # If the module has a description attribute use that in the select box
    # otherwise use the module name
    try:
        descriptions.append(m.description)
    except:
        descriptions.append(modname)

# Define a function to display the app
# descriptions instead of the module names
# in the selctbox, below
def format_func(name):
    return descriptions[moduleNames.index(name)]


# Display the sidebar with a menu of apps
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',moduleNames, format_func=format_func) 

# Run the chosen app
modules[moduleNames.index(page)].run()

#st.write(f"Modules: {modules}")
#st.write(f"Module Names: {moduleNames}")
#st.write(f"Description: {descriptions}")
