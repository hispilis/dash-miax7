import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

import api_bme_handler as abh 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
external_stylesheets=external_stylesheets)

markets = ['IBEX', 'DAX', 'EUROSTOXX']

ah = abh.APIBMEHandler(market='IBEX')

ticker_master = ah.get_ticker_master()
tcks = list(ticker_master.ticker)
ticker_dropdown_values = [{'label': t, 'value': t} for t in tcks]

data = ah.get_close_data_ticker(ticker='SAN')

fig = px.line(data)

app.layout = html.Div(children=[
    html.H1(children='MIAX Data Explorer'),


    html.H5(children='''
        mIAx API
    '''),

    html.H6("Markets:"),
        dcc.Dropdown(
            id='market-dropdown',
            options=[
                {'label': market, 'value': market} for market in markets                                
            ],
            value=markets[0]
        ),            

    html.H6("Tickers:"),
        dcc.Dropdown(
            id='ticker-dropdown',
            options=ticker_dropdown_values            
        ),    

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output('ticker-dropdown','options'),
    Input('market-dropdown','value'))
def update_figure(selected_market):
        ah.market = selected_market
        ticker_master = ah.get_ticker_master()
        tcks = list(ticker_master.ticker)
        ticker_dropdown_values = [{'label': t, 'value': t} for t in tcks]                        
        return ticker_dropdown_values

if __name__ == '__main__':
    app.run_server(debug=True)