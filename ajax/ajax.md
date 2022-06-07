# Modern AJAX Programming With JavaScript ``fetch`` and ``await``

## Goodbye XMLHttpRequest, hello fetch, asynch and await

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/ajax/fetchweather.png)
_Demo app - image by author, data from the BBC, used with permission_


Fundamentally, AJAX is a set of techniques to update the data on a web page without refreshing the whole page. This is achieved by requesting data from a server in the background and updating parts of the web page with that data.

AJAX has been a bit of a misnomer for some time - it stands for Asynchronous JavaScript And XML meaning that a JavaScript function makes an asynchronous call to a server which then returns XML data. However, while they are asynchronous, most AJAX applications use JSON as the data format rather than XML and in the past they relied on the function ``XMLHttpRequest ``- a rather awkward as a name and rather awkward to use as a function, as well.

JavaScript libraries such as JQuery made life much simpler by providing a wrapper around ``XMLHttpRequest`` but the relatively new additions to JavaScript that we will use, make life simpler still.

We are going to look at JavaScript's ``fetch``, ``asynch`` and ``await``  to build a weather forecast web page where we can change the data using a dropdown menu but without refreshing the page. We'll use a simple Python Flask app to serve the data but the focus of this artiel is on the web page that uses the data.

An asynchronous call using ``fetch`` looks something like this:

````Python
async function foo(){
   let response = await fetch("some_url");
   if (response.ok) {
      let result = await response.json();  
      // now do something with the result
   } else {
      alert(response.status);
   }
}
````

In the code above we have a function called ``foo``, which is labelled as ``asynch``. This means that when the function is called the program does not wait for the function to complete but continues with the code following the function call. Meanwhile the function does it's own thing in its own time.

Within the function ``foo`` we see that we use ``fetch`` to get a response from ``some_url`` and assign it to the local variable ``response``. This is the simplest use of ``fetch`` to perform an HTTP GET request. 

The ``await``causes the function to pause at this point and it only continues when the ``fetch`` function has completed its job.

The ``response`` is then checked to see if it is ok and, if it is, we can do something with the data in the response.

If the response returns anything other than _ok_ then we just display that response in an alert box.

So, that is the basic use of asynchronous functions. Now we will use them in a real application.

### Fetch the weather
 
We are going to get weather information from the BBC RSS feed and display it on a web page like the one you see above. We have the choice of a few cities and when we select one, the data on the page will update.

You can see a gist of a complete web page below but, first, let's focus on the function that will get the data.

It follows the same pattern as above except a parameter - the city for which we want the data - is passed to the function and that parameter is passed on the the url. 

If the reponse is ok, the data (in JSON format) is assigned to the variable ``weatherJson`` and various fields in the data are written to elements within the html, for example, the source of the icon is updated in the ``<img>`` tag with the id "feedImage" from the JSON ``weatherJson.feed.image``.

Below, is a complete web page that includes the function above and html code that contains the data and the dropdown menu that can be used to select a new city weather forecast. 

When the selection from the dropdown changes it calls the ``fetchweather`` function with the value of the city that has been selected.

It's also worth noting that default values for the fields are set directly from the server side Flask app via its templating feature, e.g.
``<img id="feedImage" src="{{weatherData.feed.image.href}}" />``
Here ``weatherData.feed.image.href`` refers to a Python variable - we'll see this shortly.

This is a simplified page that will look like this:

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/ajax/simplefetchweather.png)

_A simplified app - image by author_

I'll include a gist of the complete page at the end of this article and a link to a live version of the app.

Now we need to look briefly at the Python Flask app that supplies the data to the web page. If you are not familiar with Flask, I have written a very brief introduction here:

[How to Create and Run a Flask App](https://alan-jones.medium.com/how-to-create-and-run-a-flask-app-533b7b101c86)


There are two routes in the app, the index page which is loaded on start-up and another called ``fetchweather`` which is the function that is called from the JavaScript on the webpage. 

They both use the function ``getweather`` which downloads the BBC Weather RSS feed for the required city and constructs the data for the webpage.
The index page passes this data as a parameter to ``render_template`` and this takes the file ``simpleindex.html`` and inserts the data into it.

The ``fetchweather`` function does the same thing but passes back the data as JSON to be consumed by the fetch function in the webpage.

You can see a live version of the web page here:

[Fetch the Weather](http://ajapps.herokuapp.com/weather/)

The gist of the code for the complete webpage and Flask app is at 
the end of this article.


Thanks for reading and I hope this has been useful. You cab see my other work on my [Github webpage](alanjones2.github.io) and if you'd like to know when I publish other articles, please consider subscribing to my free, occasional newsletter, [Technofile](technofile.substack.com).

---

### Here is the complete code in two gists.

Web page:

https://gist.github.com/7ac70c6cafd9b538f977e7bbfa462dce.git


Flask app:

https://gist.github.com/6ad650854e152ed918d157987bd7be3f.git
