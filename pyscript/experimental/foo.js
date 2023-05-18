function createSelect(parent, options,  callback=null, callbackEvent = "change", id = null){
    
    opt = JSON.parse(options);

    e = document.getElementById(parent);

    select = document.createElement("select");
    select.setAttribute("class", "form-control")
    
    for (o in opt){
        //alert(opt[o].caption);
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

    e.append(select);
}

function createDiv(parent, content, id){

    e = document.getElementById(parent);

    div = document.createElement("div");
    div.innerHTML = content;

    if (id){
        div.setAttribute("id", id);
    }

    e.append(div);
}