import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
import matplotlib.pyplot as plt

cluster_colour_scale = ['#80b1d3', '#ffffb3', '#bebada', '#fb8072', '#8dd3c7']


def apply_standard_graph_styling(fig: go.Figure) -> None:
    """
    Apply standard styling to a plotly graph.
    fig: plotly.graph_objs.Figure -- The graph figure to style
    """
    fig.update_layout(
        xaxis={"showgrid": False},
        height=750,
        width=1400,
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    fig.update_layout(font=dict(size=22))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="LightGrey")
    fig.update_layout(font_family="Arial")

    # add space between y axis labels and y axis (avoid overlap with left most x axis label)
    fig.update_layout(margin=dict(pad=20))


def scatter_chart(data: pd.DataFrame, x_var: str, y_var: str, hover_labels, x_label: str, y_label: str, colour_col: str=None, log_x_axis: bool =False) -> go.Figure:
    fig = px.scatter(
        data_frame=data,
        x=x_var,
        y=y_var, 
        color=colour_col, 
        color_discrete_sequence=cluster_colour_scale,
        hover_data=[hover_labels], 
        log_x=log_x_axis,
        trendline="ols", 
        trendline_scope = "overall",
        trendline_color_override="#969696",
        title="",
        labels={
            x_var: x_label,
            y_var: y_label,
        
        })
        
    apply_standard_graph_styling(fig)
    return fig

