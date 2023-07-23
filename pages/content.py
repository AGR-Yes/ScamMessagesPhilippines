import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px


#---------------------------------#

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='About'),

    html.Div(children='''
        About!.
    '''),

])