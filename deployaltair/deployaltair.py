import altair as alt
from jinja2 import Template

def deploy(targetfile, templatefile, data):

    # add default vega values to data
    data['vega_version'] = alt.VEGA_VERSION
    data['vegalite_version']=alt.VEGALITE_VERSION
    data['vegaembed_version']=alt.VEGAEMBED_VERSION

    # get the template and render with the data
    with open(templatefile,'r') as f:
        template = f.read()
        j2_template = Template(template)
        t = j2_template.render(data)

    # write the final html
    with open(targetfile, 'w') as f:
        f.write(t)
