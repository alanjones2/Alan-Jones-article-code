import plotly.graph_objects as go

def waterfall2(labels,data, title="",  annotation=None,icolor = "Green", dcolor = "Red", tcolor = "Blue", ccolor = 'Dark Grey', color = None, measure = None):
    if measure == None:
        measure = ['relative']*(len(labels)-1)
        measure.append('total')
    if color != None:
        ccolor = icolor = dcolor = tcolor = color
    if annotation == None:
        annotation = data[:-1]
        annotation.append(sum(data))
    fig = go.Figure(go.Waterfall(
        orientation = "v",
        measure = measure,
        textposition = "outside",
        text = annotation,
        y = data,
        x = labels,
        connector = {"line":{"color":ccolor}},
        decreasing = {"marker":{"color":dcolor}},
        increasing = {"marker":{"color":icolor}},
        totals = {"marker":{"color":tcolor}}
    )).update_layout(
        title = title
    )
    return fig

import plotly.graph_objects as go

def waterfall(labels, data, title="", annotation=None, icolor="Green", dcolor="Red", tcolor="Blue", ccolor='Dark Grey', color=None, measure=None):
    """
    Create a waterfall chart using Plotly.

    Parameters:
        labels (list): A list of labels for the data points.
        data (list): A list of numerical values representing the data points.
        title (str, optional): The title of the chart. Defaults to an empty string.
        annotation (list, optional): A list of annotations for each data point. Defaults to None.
        icolor (str, optional): Color for increasing values. Defaults to "Green".
        dcolor (str, optional): Color for decreasing values. Defaults to "Red".
        tcolor (str, optional): Color for the total value. Defaults to "Blue".
        ccolor (str, optional): Connector line color. Defaults to 'Dark Grey'.
        color (str, optional): Common color for all elements. Defaults to None.
        measure (list, optional): A list specifying whether each data point is 'relative' or 'total'. Defaults to None.

    Returns:
        plotly.graph_objs._figure.Figure: A Plotly Figure containing the waterfall chart.
    """
    # Set default measure values if not provided
    if measure is None:
        measure = ['relative'] * (len(labels) - 1)
        measure.append('total')

    # Set default annotation values if not provided
    if annotation is None:
        annotation = data[:-1]
        annotation.append(sum(data))

    # Create the waterfall chart figure
    fig = go.Figure(go.Waterfall(
        orientation="v",
        measure=measure,
        textposition="outside",
        text=annotation,
        y=data,
        x=labels,
        connector={"line": {"color": ccolor}},
        decreasing={"marker": {"color": dcolor}},
        increasing={"marker": {"color": icolor}},
        totals={"marker": {"color": tcolor}}
    )).update_layout(
        title=title
    )

    return fig
