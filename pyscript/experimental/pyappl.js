/*
CreateSelect works reasonably but the rest needs work :)
*/

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
/*
function createCheckBox(parent, labels,  callback=null, callbackEvent = "change", id = null){

    //   <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
    //   <label class="form-check-label">
    
    labs = JSON.parse(labels);

    e = document.getElementById(parent);

    form = document.createElement("label");
    select.setAttribute("class", "form-check-label")
    
    for (o in labs){
        lab = document.createElement("input");
        lab.setAttribute("class", "form-check-input")
        lab.setAttribute("type", "checkbox")
        lab.setAttribute("value", "")

TK
        
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

*/



function createDiv(parent, content, id){

    e = document.getElementById(parent);

    div = document.createElement("div");
    div.innerHTML = content;

    if (id){
        div.setAttribute("id", id);
    }

    e.append(div);
}