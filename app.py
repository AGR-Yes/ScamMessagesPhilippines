import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px

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
app = dash.Dash(__name__, use_pages=True, 
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP, 
                    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap", 
                    "https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap"
                    ]
            )

#---------------------------------#
# APPLICATION LAYOUT
app.layout = html.Div(

    children=[

        # Location component to set default page
        dcc.Location(id='url', refresh=False, pathname='/home'),

        dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/home")),
            dbc.NavItem(dbc.NavLink("Content", href="/content")),
            dbc.NavItem(dbc.NavLink("About", href="/about")),
            # Add more NavItems as needed
        ],
        
        brand="Sino 'To?!",
        brand_href="/home",
        color="black",
        dark=True,
        style={
            "font-family": "'Press Start 2P', cursive",
            "font-size": "10px",
            "padding": "20px",
        }
    ),

    dash.page_container,



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
    app.run_server(debug=True
                   #comment this out when deploying the final app
                   )