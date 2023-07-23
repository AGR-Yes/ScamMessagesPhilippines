import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
#from home import layout as home_layout

#---------------------------------#
#STYLING

external_stylesheets = [
    {
        'href': 'file.css', 
        'rel':'stylesheet',
        'integrity':'sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor',
        'crossorigin':'anonymous'
     }
]

#CONTENT STYLE
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'backgroundColor':'#faeeeb',
}

#HEADER STYLE
HEADER_STYLE = {
    "textAlign":"center",
    "margin-bottom":"25px",
    'background-color': '#1f2630', 
    'text-align': 'center', 
    'padding': '4px'

}


#---------------------------------#
#APP
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap"])

#---------------------------------#
# APPLICATION LAYOUT
app.layout = html.Div(
    style={
        "position": "absolute",
        "left": "50%",
        "top": "50%",
        "transform": "translate(-50%, -50%)",
        "width": "90%",
        "height": "100vh"
    },

    children=[
        dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/home")),
        dbc.NavItem(dbc.NavLink("Content", href="/content")),
    ],
    brand="Sino 'To?!",
    brand_href="/home",
    color="black",
    dark=True,
    style={
        "font-family": "'Press Start 2P', display",  # Use Press Start 2P font
        "font-size": "10px",
        "padding": "20px",
    }
),
        
        

        # Horizontal centering of page content
        html.Div(
            dash.page_container,
        ),

        # Location component to set default page
        dcc.Location(id='url', refresh=False)
    ]
)

#---------------------------------#
# CALLBACKS
@app.callback(Output('url', 'pathname'), [Input('url', 'pathname')])
def set_default_page(pathname):
    if pathname is None or pathname == '/':
        return '/home'
    return pathname

# ---------------------------------#
if __name__ == '__main__':
    app.run_server(debug=True)