import streamlit.components.v1 as components


def bs():
    cdn = """
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    """
    return cdn

def header(text,c='black',s=1, height=50):

    html = f"""
        {bs()}
        <h{s} style='color:{c}'>{text}</h{s}>"""
    return  components.html(html, height=height)

def display(text,c='black',s=1, height=70):

    html = f"""
        {bs()}
        <h1 class='display-{s}' style='color:{c}'>{text}</h1>"""
    return  components.html(html, height=height)

def lead(text,c='black', height=50):
    html = f"""
        {bs()}
        <p class='lead' style='color:{c}'>{text}</p>"""
    return  components.html(html, height=height)

def alert(text,type='alert-primary'):
    html = f"""
    {bs()}
    <div class="alert {type}" role="alert">
        {text}
    </div>
    """
    return  components.html(html)

def write(text,c='black', height=50):
    html = f"""
        {bs()}
        <p style='color:{c}'>{text}</p>"""
    return  components.html(html, height=height)