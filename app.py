import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px

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
        dcc.Location(id='url', refresh=False, pathname='/'),

        dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/", style={"color": "white"})),
        dbc.NavItem(dbc.NavLink("Spam", href="/spam", style={"color": "white"})),
        dbc.NavItem(dbc.NavLink("Privacy", href="/privacy", style={"color": "white"})),
        dbc.NavItem(dbc.NavLink("About", href="/about", style={"color": "white"})),
        # Add more NavItems as needed
        ],
        
        brand="Sino 'To?!",
        brand_href="/",
        color="black",
        dark=True,
        style={
            "font-family": "'Press Start 2P', cursive",
            "font-size": "10px",
            "padding": "20px",
        }
    ),

    dash.page_container,


    html.Div([
        html.A("Repository",
            href="https://github.com/AGR-Yes/ScamMessagesPhilippines",
            style={'margin-right': '10px', 'font-family':"'Space Grotesk', sans-serif'", 'color':'white'  }),
        
        html.A("AGR's Github",
            href="https://github.com/agr-Yes/",
            style={'margin-right': '10px', 'font-family':"'Space Grotesk', sans-serif'", 'color':'white'  }),
        
        html.A("Instagram",
            href="https://www.instagram.com/ant0nreyes/",
            style={'font-family':"'Space Grotesk', sans-serif'", 'color':'white'  }),
            

    ], style={'position': 'relative', 
               'bottom': 0, 
               'width': '100%', 
               'background-color': 'black', 
               'text-align': 'center', 
               'padding': '20px',               
        }
    
    
    )

    ]
)

# ---------------------------------#
if __name__ == '__main__':
    app.run_server(#debug=True
                   #comment this out when deploying the final app
                   )