import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

#---------------------------------#

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='About'),

    html.Div(children='''
        This is our Home page content.
    '''),

])