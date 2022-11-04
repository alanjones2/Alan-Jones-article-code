function createSelect(parent, options,  callback=null, callbackEvent = "change", id = null){
    
    opt = JSON.parse(options);

    select = document.createElement("select");
    select.setAttribute("class", "form-control")
    
    for (o in opt){
        alert(opt[o].caption);
        option = document.createElement("option");
        option.append(opt[o].caption);
        option.setAttribute("value",opt[o].value);
        select.append(option);
    }

    if (id){
        select.setAttribute("id", id)
    }

    if (callback){
        e.addEventListener(callbackEvent, callback);
    }

    e = document.getElementById(parent);
    e.append(select);
}