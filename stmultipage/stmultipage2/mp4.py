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

import streamlit as st
st.set_page_config(layout = "wide") # optional


import pkgutil
import importlib
import stlib    # default library name for apps

# Global arrays for holding the app names, modules and descriptions of the apps
names = []
filenames = ['countryData', 'continentData']
descriptions = [] 
modules = []

package = stlib # default name for the library containg the apps

# Find the apps and import them
for modname in filenames:
    #print ("Found submodule %s (is a package: %s)" % (modname, ispkg))
    m = importlib.import_module('.'+modname,'stlib')
    names.append(modname)
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
    return descriptions[names.index(name)]


# Display the sidebar with a menu of apps
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',names, format_func=format_func) 

# Run the chosen app
modules[names.index(page)].run()
