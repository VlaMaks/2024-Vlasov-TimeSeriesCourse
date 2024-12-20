import numpy as np
import pandas as pd

# for visualization
import plotly
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
import plotly.express as px
plotly.offline.init_notebook_mode(connected=True)


def plot_ts_set(ts_set: np.ndarray, title: str = 'Input Time Series Set') -> None:
    """
    Plot the time series set

    Parameters
    ----------
    ts_set: time series set
    title: title of plot
    """

    ts_num, m = ts_set.shape

    fig = go.Figure()

    for i in range(ts_num):
        fig.add_trace(go.Scatter(x=np.arange(m), y=ts_set[i], line=dict(width=3), name="Time series " + str(i)))

    fig.update_xaxes(showgrid=False,
                     title='Time',
                     title_font=dict(size=22, color='black'),
                     linecolor='#000',
                     ticks='outside',
                     tickfont=dict(size=18, color='black'),
                     linewidth=2,
                     tickwidth=2)
    fig.update_yaxes(showgrid=False,
                     title='Values',
                     title_font=dict(size=22, color='black'),
                     linecolor='#000',
                     ticks='outside',
                     tickfont=dict(size=18, color='black'),
                     zeroline=False,
                     linewidth=2,
                     tickwidth=2)
    fig.update_layout(title=title,
                      title_font=dict(size=24, color='black'),
                      plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='rgba(0,0,0,0)',
                      legend=dict(font=dict(size=20, color='black'))
                      )

    fig.show(renderer="colab")


def mplot2d(x: np.ndarray, y: np.ndarray, plot_title: str = None, x_title: str = None, y_title: str = None, trace_titles: np.ndarray = None) -> None:
    """
    Multiple 2D Plots on figure for different experiments

    Parameters
    ----------
    x: values of x axis of plot
    y: values of y axis of plot
    plot_title: title of plot
    x_title: title of x axis of plot
    y_title: title of y axis of plot
    trace_titles: titles of plot traces (lines)
    """

    fig = go.Figure()

    for i in range(y.shape[0]):
        fig.add_trace(go.Scatter(x=x, y=y[i], line=dict(width=3), name=trace_titles[i]))

    fig.update_xaxes(showgrid=False,
                     title=x_title,
                     title_font=dict(size=22, color='black'),
                     linecolor='#000',
                     ticks='outside',
                     tickfont=dict(size=18, color='black'),
                     linewidth=2,
                     tickwidth=2,
                     tickvals=x)
    fig.update_yaxes(showgrid=False,
                     title=y_title,
                     title_font=dict(size=22, color='black'),
                     linecolor='#000',
                     ticks='outside',
                     tickfont=dict(size=18, color='black'),
                     zeroline=False,
                     linewidth=2,
                     tickwidth=2)
    fig.update_layout(title={'text': plot_title, 'x': 0.5, 'xanchor': 'center'},
                      title_font=dict(size=24, color='black'),
                      plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='rgba(0,0,0,0)',
                      legend=dict(font=dict(size=20, color='black')),
                      width=1000,
                      height=600
                      )

    fig.show(renderer="colab")


def plot_bestmatch_data(ts: np.ndarray, query: np.ndarray) -> None:
    """
    Visualize the input data (time series and query) for the best match task

    Parameters
    ----------
    ts: time series
    query: query
    """

    query_len = query.shape[0]
    ts_len = ts.shape[0]

    fig = make_subplots(rows=1, cols=2, column_widths=[0.1, 0.9], subplot_titles=("Query", "Time Series"), horizontal_spacing=0.04)

    fig.add_trace(go.Scatter(x=np.arange(query_len), y=query, line=dict(color=px.colors.qualitative.Plotly[1])),
                row=1, col=1)
    fig.add_trace(go.Scatter(x=np.arange(ts_len), y=ts, line=dict(color=px.colors.qualitative.Plotly[0])),
                row=1, col=2)

    fig.update_annotations(font=dict(size=24, color='black'))

    fig.update_xaxes(showgrid=False,
                     linecolor='#000',
                     ticks="outside",
                     tickfont=dict(size=18, color='black'),
                     linewidth=1,
                     tickwidth=1,
                     mirror=True)
    fig.update_yaxes(showgrid=False,
                     linecolor='#000',
                     ticks="outside",
                     tickfont=dict(size=18, color='black'),
                     zeroline=False,
                     linewidth=1,
                     tickwidth=1,
                     mirror=True)

    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)",
                      paper_bgcolor='rgba(0,0,0,0)',
                      showlegend=False,
                      title_x=0.5)

    fig.show(renderer="colab")


def plot_bestmatch_results(ts: np.ndarray, query: np.ndarray, bestmatch_results: dict) -> None:
    """
    Visualize the best match results

    Parameters
    ----------
    ts: time series
    query: query
    bestmatch_results: output data found by the best match algorithm
    """

    # INSERT YOUR CODE
    query_len = query.shape[0]
    ts_len = ts.shape[0]

    # Create subplots for query and time series
    fig = make_subplots(rows=1, cols=2, column_widths=[0.1, 0.9],
                        subplot_titles=("Query", "Time Series"),
                        horizontal_spacing=0.04)

    # Plot the query
    fig.add_trace(go.Scatter(x=np.arange(query_len), y=query,
                             line=dict(color=px.colors.qualitative.Plotly[1], width=4)),
                  row=1, col=1)

    # Plot the time series
    fig.add_trace(go.Scatter(x=np.arange(ts_len), y=ts,
                             line=dict(color=px.colors.qualitative.Plotly[0], width=2)),
                  row=1, col=2)

    # Highlight topK best matching subsequences on the time series
    for idx in bestmatch_results['indices']:
        # Extract the best matching subsequence from the time series
        best_match = ts[idx:idx + query_len]

        # Plot the matching subsequence with the same color as the query
        fig.add_trace(go.Scatter(x=np.arange(idx, idx + query_len), y=best_match,
                                 line=dict(color=px.colors.qualitative.Plotly[1], width=3),
                                 mode='lines+markers'),
                      row=1, col=2)

    # Update annotations for the plot
    fig.update_annotations(font=dict(size=24, color='black'))

    # Update axes styles
    fig.update_xaxes(showgrid=False, linecolor='#000', ticks="outside",
                     tickfont=dict(size=18, color='black'), linewidth=1,
                     tickwidth=1, mirror=True)
    fig.update_yaxes(showgrid=False, linecolor='#000', ticks="outside",
                     tickfont=dict(size=18, color='black'), zeroline=False,
                     linewidth=1, tickwidth=1, mirror=True)

    # Update layout settings
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor='rgba(0,0,0,0)',
                      showlegend=False, title_x=0.5)

    # Show the plot
    fig.show(renderer="colab")


def pie_chart(labels: np.ndarray, values: np.ndarray, plot_title='Pie chart') -> None:
    """
    Build the pie chart

    Parameters
    ----------
    labels: sector labels
    values: values
    """

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    fig.update_traces(textfont_size=20)
    fig.update_layout(title={'text': plot_title, 'x': 0.5, 'xanchor': 'center'},
                      title_font=dict(size=24, color='black'),
                      legend=dict(font=dict(size=20, color='black')),
                      width=700,
                      height=500
                      )

    fig.show(renderer="colab")
