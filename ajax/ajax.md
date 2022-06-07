# Modern AJAX Programming With JavaScript ``fetch`` and ``await``

## Goodbye XMLHttpRequest, hello fetch, asynch and await

Demo app - image by author, data from the BBC, used with permission


Fundamentally, AJAX is a set of techniques to update the data on a web page without refreshing the whole page by requesting data from a server in the background.

It  has been a bit of a misnomer for some time - it stands for Asynchronous JavaScript And XML meaning that an asynchronous JavaScript function makes a call to a server which returns XML data. However, while they are, of course asynchronous, most AJAX applications use JSON as the data format rather than XML and in the past relied on the function XMLHttpRequest - a rather awkward name and rather awkward to use, as well.

JavaScript libraries such as JQuery made life much simpler by providing a wrapper around ``XMLHttpRequest`` but the relatively new additions to JavaScript that we will use, make life much simpler.

We are going to look at JavaScript's ``fetch``, ``asynch`` and ``await``  build a weather forecast web page where we can change the data using a dropdown menu but without refreshing the page. We'll use a simple Python Flask app to serve the data.

An asynchronous call using fetch looks something like this:
````Python
async function foo(){
   let response = await fetch("someurl");
   if (response.ok) {
      let result = await response.json();  
      // now do something with the result
   } else {
      alert(response.status);
   }
}
````

We have a function called ``foo``, which is labelled as ``asynch``. This means that when the function is called the program flow continues after the function call while the function does it's own thing in its own time. (This asynchronous behaviour is known as a promise in JavaScript, it's basically a function that is not resolved immediately. Promises have their own syntax but I prefer the more obvious - to me, anyway - syntax using ``asynch`` and ``await``.)

Within the function we see that we use fetch to get a response from ``someurl`` and assign it to the local variable ``response`` (this is the simplest use of ``fetch`` to perform a GET request). The ``await`` means that this is not done immediately but only when the function has completed (or the promise has been resolved).

The response is then checked to see if it is ok and then we can do something with the data in the response.

### Fetch the weather

We are going to get weather information from the BBC RSS feed and display it on a web page like the one you see above. We have the choice of a few cities and when we select one the data on the page will update.
You can see a gist of a complete web page below but, first, let's focus on the function that will get the data.

It follows the same pattern as above except a parameter - the city for which we want the data- is passed to the function. That parameter is passed on the the url. If the reponse is ok, the data (in JSON format) is assigned to the variable weatherJson and various fields in the data are written to elements within the html, for example, the source of the icon is updated in the ``<img>`` tag with the id "feedImage" from weatherJson.feed.image.
Below, is a complete web page that includes the function above and html code that contains the data and the dropdown menu that can be used to select a new city weather forecast. When the selection from the dropdown changes it calls the fetchweather function with the value of the city that has been selected.
It's also worth noting that default values for the fields are set directly from the server side Flask app via its templating feature, e.g.
``<img id="feedImage" src="{{weatherData.feed.image.href}}" />``
Here weatherData.feed.image.href refers to a Python variable - we'll see this shortly.

This is a simplified page that will look like this:
A simplified app - image by authorI'll include a gist of the complete page at the end of this article and a link to a live version of the app.
Now we need to look briefly at the Python Flask app that supplies the data to the web page. If you are not familiar with Flask, I written a very brief introduction here:
How to Create and Run a Flask App
This is a brief introduction to creating and running a Flask app, the use of HTML templates and how to create…alan-jones.medium.com
There are two routes in the app, the index page which is loaded on start-up and another called fetchweather which is the function that is called from the JavaScript on the webpage. They both use the function getweather which downloads the BBC Weather RSS feed for the required city and constructs the data for the webpage.
The index page passes this data as a parameter to render_template and this takes the file simpleindex.html and inserts the data into it.
The fetchweather function does the same thing but passes back the data as JSON to be consumed by the fetch function in the webpage.

You can see a live version of the web page here:
Fetch the Weather
Maximum Temperature: 30°C (86°F), Minimum Temperature: 21°C (71°F), Wind Direction: South Westerly, Wind Speed: 12mph…ajapps.herokuapp.com
And the gist of the code for the complete webpage and Flask app is right at the end of this article.
Thanks for reading and I hope this has been useful. If you'd like to know when I publish other articles, please consider subscribing to my free and occasional newsletter, Technofile.

---

Here is the complete code.
Web page:

Flask app: