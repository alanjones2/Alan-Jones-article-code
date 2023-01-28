# What's new in PyScript

Since I last wrote about  PyScrypt there has been two updates - versions 2022.09.1 and 2022.12.1 - and we no longer seem to be in _alpha_ territory. 

PyScript is definitely evolving and becoming more useful (and hopefully more stable).

I won't go into all of the detailed changes but will look at some changes that feel the most significant to me. I'll also show you some practical uses of the new features (see __Notes__, below, for more detailed descriptions of the changes).

## Which version of PyScript

In my previous articles I imported the PyScript libraries like this:

```` HTML
<link rel="stylesheet" 
    href="https://pyscript.net/alpha/pyscript.css" />
<script defer 
    src="https://pyscript.net/alpha/pyscript.js">
</script>
````

That was specifiying the _alpha_ version of the ``js`` and ``css`` files. Now you could specify the _latest_ version like this:

```` HTML
<link rel="stylesheet" 
    href="https://pyscript.net/releases/latest/pyscript.css" />
<script defer 
    src="https://pyscript.net/releases/latest/pyscript.js">
</script>
````

While this looks as if it might be a good option, PyScript is moving fast and if you write an application using what is the currently latest version, in (a potentially short) time that will change and you may find that the changes in a new latest version will break your app.

It would be better and safer to specify the particular version that you are using, e.g.

```` HTML
<link rel="stylesheet" 
    href="https://pyscript.net/releases/2022.12.1/pyscript.css" />
<script defer 
    src="https://pyscript.net/releases/2022.12.1/pyscript.js">
</script>
````

## Don't use ``<py-env>``

the ``<py-env>`` section of a PyScript app is going to disappear. Instead we should now use ``<py-config>``


```` HTML
<html>
<head>
    <link rel="stylesheet" href="https://pyscript.net/releases/2022.12.1/pyscript.css" />
    <script defer src="https://pyscript.net/releases/2022.12.1/pyscript.js">
    </script>
</head>

<body>
<div id="output"></div>
    
<py-config type="toml">
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

## PyScript Version 2022.09.1 


<py-env> Will Be Going Away
Previously, the <py-env> tag was where one would specify additional libraries to download from PyPI, as well as URL's to load into the local filesystem. Now, those options are being folded into <py-config>, alongside other options like plugins and runtimes and metadata like the pages name and version number. The use of <py-env> is deprecated and will be removed in a future release.

Additionally, <py-config> can now accept configurations in JSON in addition to TOML. Creators using build systems that strip out whitespace (which isn't very kind to TOML) may find this especially useful.

<py-config>
  packages: ["rich", "faker"]
  paths: ["./data_file.txt"]
</py-config>
py-* Events
The alpha and 2022.06.1 releases supported a couple of special attributes on HTML tags - pys-onClick and pys-onKeyDown - that PyScript hooked into to allow the running of Python code in response to a couple of common browser interactions.

Release 2022.09.1 radically expands this capability with many, many more browser events supported.

The syntax of py-* events has also changed to more closely match JavaScripts event syntax. Previously, you supplied a Callable which was called with no arguments. Now you write a line of code (optionally broken up with ; symbols) which is run when the event triggers. The correct usage is now:

<py-script>
    from js import console as jsconsole
    def say_hi(name):
        jsconsole.log("Hi, " + name)
</py-script>
<p id="my-paragraph" py-mouseover="say_hi('Jeff'); jsconsole.log('I did it!')">Mouse Over Me</p>
Note that, unlike JavaScripts event syntax, the value of the py-* attribute can be any valid Python code, not just a single function call.

Better Input/Output Escaping
Embedding something that looks like HTML inside of Python inside of HTML is... well, even just saying it is a mouthful, and it comes with its own pitfalls. Previously, PyScript tags like the following would fail in a couple of ways:

print("<b>A bold tag!</b>")
tag_name = "i"
print("I'm pretty sure 1 < 2 but 2 > 0")

First, the Browser needs to be prevented from interpretting the <b> tag as internal HTML, and second, the output needs to recognize that the < > symbols are not an HTML tag. These issues have been solved by a pair of changes.

Better Logging

Logging to the Developer Console that PyScript does is now much cleaner, and annotated by what file the log line is generated in. This makes it easier to see what's logged by the user's program and what's being logging by the PyScript mechanisms themselves.

Framework for Multiple Runtimes
The use of a specific version of Pyodide is no longer hardcoded into a PyScript release - users may now opt to supply a URL and name for a 'runtime' in the <py-config> tag. If one is not supplied, the default is still to load the version of Pyodide that PyScript has been most recently tested against, which should be the right option for most users. But this does open the door to future improvements like:

Running py-script blocks in different versions of Pyodide
Running py-script blocks in runtimes that are not Pyodide (Micropython??)
Running py-script blocks in a self-built/custom build of Pyodide for experimentation or demonstrating new features


## Pyscript Version 2022.12.1



## ``print()`` and ``display()``

## Fetching Files with ``<py-config> [[fetch]]``

## events



## Notes

Detailed description of the changes to PyScript can be found on Jeff Glass's blog.

[Jeff Glass's blog entry for version 2022-12-1](https://jeff.glass/post/whats-new-pyscript-2022-12-1/)

[Jeff Glass's blog entry for version 2022-09-1 ](https://jeff.glass/post/whats-new-pyscript-2022-09-1/)
