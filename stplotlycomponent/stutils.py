import streamlit.components.v1 as components

def plotly_chart(fig):
    graphJSON = fig.to_json()
    components.html(f"""
        <div id="chart"></div>
        <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
        <script type='text/javascript'>
            var figure = JSON.parse('{graphJSON}');
            Plotly.newPlot("chart", figure);
        </script>
        """, 
        height=fig.layout.height, width=fig.layout.width)
    
def example_component(header="header",text="text"):
        components.html(f"""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
                crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" 
                crossorigin="anonymous"></script>
                        
            <h2 class="p-3 mb-2 bg-primary text-white"">
                {header}
                <div class="pt-3 pb-3 lead">{text}</div>
            </h2>        
        """, height=400, width=800)
