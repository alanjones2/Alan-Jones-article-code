import streamlit as st
import streamlit.components.v1 as components

def bs():
    cdn = """
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    """
    return cdn

def header(text,c,s=1):

    html = f"""
        {bs()}
        <h{s} style='color:{c}'>{text}<h{s}>"""
    return  components.html(html)

def alert(text,type='alert-primary'):
    html = f"""
    {bs()}
    <div class="alert {type}" role="alert">
        {text}
    </div>
    """

    return  components.html(html)



header("hello","green",2)

alert("alert!!!!","alert-secondary")








