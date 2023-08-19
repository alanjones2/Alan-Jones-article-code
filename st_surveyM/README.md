### Code to accompany the article:

# [Streamlit and MongoDB: Storing Your Data in the Cloud]()

Deploying your Streamlit app to the Cloud means that any data that you create with that app disappears when the app terminates - unless you use third-party storage like the NoSQL database MongoDB

This is structured as multipage Streamit app and demonstrates how Streamlit UI components can be used to create and present a survey using MongoDB for data storage.

The code here is a complete Streamlit app formatted as four pages including an index.

- index.py - the starting point
- -pages/present_survey.py - show the survey and store response to questions
- pages/see_results.py - a very simple analysis of the results plus the ability to download them as CSV
- DBUtils2.py - some library routines for accessing MongoDB

---
### If you find this content useful, please consider one or more of the following:

-  ### Sign up for [Medium](https://medium.com/) where you can read all my articles along with thousands of others for $5 a month.  
-  ### [Buy a book](https://alanjones.gumroad.com/)
-  ### Subscribe to my [free newsletter](https://technofile.substack.com/)
-  ### Visit my [web page](alanjones2.github.io)