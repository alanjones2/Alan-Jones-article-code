# 3 Ways to Create a Multi-Page Streamlit App

## Streamlit may not have been designed for full blown web sites but it is fairly straightforward to create multiple pages in a single app

There are two aspects to creating mutipage apps: how to select then from the user interface and how to select the code to run the apps.

The UI could be option menu, drop down, buttons, etc.

I concentrate on the more technical aspect how to select the code:

 - Use a select statement such as `if else` or 3.10 pattern matching to chosse which page to display. This is the easiest method and works well for a small number of pages.
 - Structure apps as a library package. A more sophisticated way of delivering multiple pages that is also easy to use - just follow the pattern.
 - A generic launcher app for a library of apps. This launcher will automatically pick up the apps stored in a library but is still easy to create and use.


mp1 is simple if/else and inline code
mp2 is like mp1 but with 3.10 pattern matching
mp3 explicitly imports the modules and uses if/else to run them
mp4 reads the module manes from a library function, loads the modules and runs them by matching the strings in the drop down menu