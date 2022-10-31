# Create interactive elements and append to a parent DOM element

# We can specify  callback for an element - defaults to change - and no id will be needed
# but if a different element - say a button - should call the callback then an id will be needed 
# because that other element will use getElementById() 

#from js import document
#from pyodide import create_proxy

def createSelect(parent, options,  callback=None, id = None, callbackEvent = "change"):     

    select = document.createElement("select")
    select.setAttribute("class", "form-control")
    if id:
        select.setAttribute("id", id)

    for o in options:
        opt = document.createElement("option")
        opt.append(o['caption'])
        opt.setAttribute("value",o['value'])
        select.append(opt)

    e = document.getElementById(parent)
    e.append(select)
    if callback:
        change_proxy = create_proxy(callback)
        e.addEventListener(callbackEvent, change_proxy)

    return select