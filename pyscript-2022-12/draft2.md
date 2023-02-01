# What's new in PyScript

Since I last wrote about  PyScrypt there has been two updates - versions 2022.09.1 and 2022.12.1 - and we no longer seem to be in _alpha_ territory. 

I won't go into all of the detailed changes but will look at some changes that feel the most significant to me. I'll also show you some practical uses of the new features (see __Notes__, below, for more detailed descriptions of the changes).

The new developmwnta that I will cover are:
- How version of PyScript are specified
- The demise of ``<py-env>`` and how to access external resources
- ``display()`` and ``print()``
- ``py-events``

## Which version of PyScript

In my previous articles I imported the PyScript libraries like this:

```` HTML
<link rel="stylesheet" 
    href="https://pyscript.net/alpha/pyscript.css" />
<script defer 
    src="https://pyscript.net/alpha/pyscript.js">
</script>
````

That was specifiying the _alpha_ version of the ``js`` and ``css`` files. Since then you've been able to specify the _latest_ version like this:

```` HTML
<link rel="stylesheet" 
    href="https://pyscript.net/releases/latest/pyscript.css" />
<script defer 
    src="https://pyscript.net/releases/latest/pyscript.js">
</script>
````

While this looks as if it might be a good option, PyScript is moving fast and if you write an application using what is the currently latest version, in (a potentially short) time that will change and you may find that the changes in a new latest version will break your app.

So, in his blog (see __Notes__,below), Jeff Glass suggests you specify the particular version that you are using, e.g.

```` HTML
<link rel="stylesheet" 
    href="https://pyscript.net/releases/2022.12.1/pyscript.css" />
<script defer 
    src="https://pyscript.net/releases/2022.12.1/pyscript.js">
</script>
````

However, the PyScript website still seems to recommend using ``latest``, so we'll carry on with that for now.

## Don't use ``<py-env>``

The ``<py-env>`` section of a PyScript app is going to disappear. This was where we specified local files to load into the virtual files system and packages to load from PyPI. Now, we should use ``<py-config>``, instead.

Here is an example of the way we can load packages from PyPI and use them. The packages to load are specified in  ``<py-config>`` and are later imported in the python code.


```` HTML
<html>
    <head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    </head>

  <body>
    <h1>Let's plot make a plot</h1>
    <div id="plot"></div>
    <py-config>
        packages = ["pandas", "matplotlib"]
    </py-config>
    <py-script>
      import matplotlib.pyplot as plt
      import pandas as pd
      df = pd.DataFrame()
      df['x'] = [1,2,3,4,5,6,7,8,9]
      df['y'] = [1,2,3,4,5,6,7,8,9]
      fig, ax = plt.subplots()
      df.plot("x", "y", ax=ax)
      display(fig, target="plot")
    </py-script>
  </body>
</html>
````
As you can see, we simply assign a list of PyPI packages to ``packages``.

You can run this code in a browser and you will get a simple straight line graph displayed in the ``<div>`` with the ``id`` "plot".

To load a module from a local filesystem we use ``[[fetch]]`` and we can specify where to read the files from, which files are to be loaded, and where they will be located in the virtual file system using ``from``, ``files`` and ``to_folder``.

Here is a simple example that loads a local module called ``test.py`` which contains a function ``say_hello()`` that simply returns the string ``"Hello"``.

```` HTML
<html>
<head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>

<body>
<div id="output"></div>
    
<py-config>
    [[fetch]]
    from = './my_package/'
    files = ['test.py']
    to_folder = 'local_package'
</py-config>
    <py-script>
        from local_package import test 
        display(test.say_hello(), target="output")
    </py-script>
</body>
</html>
````

Here, in the ``<py-config>`` section we have ``[[fetch]]`` followed by the folder where the files will be found, the list of files to be fetched, and the destination folder in the virtual filesystem.

To use the _fetched_ package in Python we use a normal ``import`` statement the gets the module ``test`` from the folder where we put it (``local_package``).

Running this code will simply display "Hello" in the browser.

Note, that to get this working you need add a sub-folder in the source code called ``my_package`` that contains the file ``test.py``:

```` Python
def say_hello():
    return "Hello"
````
You should also include an empty ``__init__.py`` in the same folder.

## ``print()``

``print()`` sends its output to ``<py-terminal>`` unless you specify otherwise, this tag is automatically created the first time ``print`` is used. You can also manually include the tag in your code.

So in the following code a new terminal is automatically created.

```HTML
<html>
<head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
    <py-script>
        print("Hello from py-terminal")
    </py-script>
</body>
</html>
````

But in the next program, the manually inserted ternimal is used.

```` HTML
<html>
<head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
    <py-script>
        print("Hello from py-terminal")
    </py-script>
    <div>
    The Python Termianl will appear below here...
    </div>
    <py-terminal></py-terminal>
    <div>
    ...but above here
    </div>
</body>
</html>
````

## ``display()``

This is the method for displaying stuff in a HTML tag, such as a ``<div>`` - the ``<py-script>``, ``output``, attribute is deprecated.

``display()`` takes a first parameter the data to be displayed and ``target`` which is the ``id`` of an HTML tag. It can be used to write several types of content. Here is a fragment that displays some text in a ``<div>``:

```` HTML 
<div id="output"></div>
<py-script>
    display("Hello", target="output")
</py-script>
````

In the example above it was used to display a ``matplotlib`` figure.

## py-* Events

Previosly, the PyScript supported a couple of special attributes on HTML tags - ``pys-onClick`` and ``pys-onKeyDown`` - that allowed the running of Python code in response to ``onClick`` and ``onKeyDown`` events. Now, there are many more of these events that are supported.

Here is an example of its usage:

```` HTML
    <py-script>
        import js
        def say_hi(name):
            js.alert("Hi, " + name)
    </py-script>
    <p id="my-p" py-mouseover="say_hi('Alan')" style="border-style:solid">
        Mouse Over Me
    </p>
````

This code will display a box that will pop up an alert box when the mouse is run over it.



## Notes

Detailed description of the changes to PyScript can be found on Jeff Glass's blog.

[Jeff Glass's blog entry for version 2022-12-1](https://jeff.glass/post/whats-new-pyscript-2022-12-1/)

[Jeff Glass's blog entry for version 2022-09-1 ](https://jeff.glass/post/whats-new-pyscript-2022-09-1/)


```` HTML
<html>

<head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
    
    <py-config>
        packages = ['pandas','matplotlib','plotly']
    </py-config>
</head>

<body>
    <div class="jumbotron">
        <h1>Weather Data</h1>
        <p class="lead">
            Some graphs about the weather in London in 2020
        </p>
    </div>

    <div class="row">
        <div class="col-sm-2 p-2 ml-4 mb-1">
            <button type="button" class="btn btn-secondary">Select chart from list:</button>
        </div>
        <div class="col-sm-4 p-2 mr-4 mb-1">
            <select class="form-control" id="select" py-change="selectChange()">
                <option value="Tmax">Maximum Temperature</option>
                <option value="Tmin">Minimum Temperature</option>
                <option value="Sun">Sun</option>
                <option value="Rain">Rain</option>            
            </select>
        </div>
    </div>

    <div class="row">
        <div class="col-sm-6 p-2 m-4 bg-white">
            <div id="chart1"></div>
        </div>
    </div>

    <py-script>
        # Import libraries
        import pandas as pd
        import js
        import json
        import plotly
        import plotly.express as px

        ## Get the data
        from pyodide.http import open_url
        
        url = 'https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv'
        url_content = open_url(url)

        df = pd.read_csv(url_content)
        df = df[df['Year']==2020]

        def plot(chart):
            fig = px.line(df,
            x="Month", y=chart,
            width=800, height=400)
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            js.Plotly.newPlot("chart1", js.JSON.parse(graphJSON))
                
        def selectChange():
            choice = js.document.getElementById("select").value
            plot(choice)

        plot('Tmax')
    </py-script>
</body>

</html>
````