### Code to accompany the article:

# [Simple Surveys with Streamlit](https://towardsdatascience.com/simple-surveys-with-streamlit-and-databutton-d027586f1c71)
Streamlit’s user interface components made constructing simple surveys easy

We create a simple survey with Streamlit, present it and show the results.

This is structured as multipage Streamit app and demonstrates how Streamlit UI components can be used to create and present a survey. Data storage is local (see the article) and so the app is not suitable for deployment in the Streamlit cloud (all data will be lost when the app terminates).


The code here is a complete Streamlit app formatted as four pages including an index.

- index.py - the starting point
- pages/edit_survey.py - create or edit a survey by adding questions
- -pages/present_survey.py - show the survey and store response to questions
- pages/see_results.py - a very simple analysis of the results plus the ability to download them as CSV


---
### If you find this content useful, please consider one or more of the following:

-  ### Sign up for [Medium](https://medium.com/@alan-jones/membership) where you can read all my articles along with thousands of others for $5 a month (_affiliate link_).  
-  ### [Buy a book](https://alanjones.gumroad.com/)
-  ### Subscribe to my [free newsletter](https://technofile.substack.com/)
-  ### Visit my [web page](alanjones2.github.io)