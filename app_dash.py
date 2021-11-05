import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

import api_bme_handler as abh 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
external_stylesheets=external_stylesheets)

ah = abh.APIBMEHandler(market='IBEX')
data = ah.get_close_data_ticker('SAN')

#fig = px.bar(data)
fig = px.line(data)

app.layout = html.Div(children=[
    html.H1(children='Api Handler Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)