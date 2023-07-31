import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

#---------------------------------#
dash.register_page(__name__)

layout = html.Div(
    style={
        "background-color": "black",
        "margin-left": "auto",
        "margin-right": "auto",
    },
    
    children=[
        
#Title
        dbc.Row( 
            children=[ 
                    
#Column 1
                    dbc.Col( 
                        html.Div([    
                            html.Img(src='https://placehold.co/500X400', alt='Placeholder Image', 
                                        style={"align": "right",
                                                "position": "relative", 
                                                "margin-top":"60px",
                                                "width": "80%",
                                                "margin-left": "auto",
                                                "margin-right": "auto",}),
                        ]), width = 6, 
                    ),
                    

#Column 2
                    dbc.Col(
                        html.Div([
                            html.Div([

                                #Content 
                                html.P('Title', style={
                                        "margin-top": "60px",
                                        'font-size': '30px',
                                        "font-family": "'Press Start 2P', display",
                                        "padding": "5px",
                                        "color": "#C8F9E7"
                                        }),  
                                
                                html.P(
                                        """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus.
                                        """,
                                        style={
                                            "color": "#C8F9E7",
                                        }
                                ), 
                                
                                #Content 
                                html.P('Title', style={
                                        "margin-top": "60px",
                                        'font-size': '30px',
                                        "font-family": "'Press Start 2P', display",
                                        "padding": "5px",
                                        "color": "#C8F9E7"
                                        }),  
                                
                                html.P(
                                        """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus.
                                        """,
                                        style={
                                            "color": "#C8F9E7",
                                        }
                                ), 

                                
                                
                            ]),
                            ]), width = 3,  # column width
                    ),


#Column 3
                    dbc.Col(
                        html.Div([
                            html.Div([
                             #Content 
                                html.P('Title', style={
                                        "margin-top": "60px",
                                        'font-size': '30px',
                                        "font-family": "'Press Start 2P', display",
                                        "padding": "5px",
                                        "color": "#C8F9E7"
                                        }),  
                                
                                html.P(
                                        """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus.
                                        """,
                                        style={
                                            "color": "#C8F9E7",
                                        }
                                ), 
                                
                                #Content 
                                html.P('Title', style={
                                        "margin-top": "60px",
                                        'font-size': '30px',
                                        "font-family": "'Press Start 2P', display",
                                        "padding": "5px",
                                        "color": "#C8F9E7"
                                        }),  
                                
                                html.P(
                                        """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus.
                                        """,
                                        style={
                                            "color": "#C8F9E7",
                                        }
                                ), 
                            ]),
                            ]), width = 3,  # column width
                    ),

                ], 
        ),

#Row 2
    dbc.Row(
        children=[
            html.Div([
                html.P(
                    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada. Donec vehicula tincidunt ante, eu dignissim nisl pharetra ac. Nulla nisi magna, hendrerit eu libero vitae, blandit interdum ipsum. Aenean quis viverra nibh.
                    """,
                    style={
                                "margin-top": "60px",
                                'text-align': 'center', 
                                'font-size': '12px',
                                "font-family": "'Roboto', serif",
                                "padding": "5px",
                                "width": "80%",
                                "margin-left": "auto",
                                "margin-right": "auto",
                                "color": "#C8F9E7"
                                }
                ),
            ])
        ]
    ),

#Row 3
    dbc.Row(
        children = [
            dbc.Col( 
                html.Div([    
                    html.P(
                    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada. Donec vehicula tincidunt ante, eu dignissim nisl pharetra ac. Nulla nisi magna, hendrerit eu libero vitae, blandit interdum ipsum. Aenean quis viverra nibh.
                    """,
                    style={
                            "margin-top" : "60px",
                            "margin-left" : "30px",
                            "font-family" : "'Roboto', serif",
                            "padding" : "5px",
                            "color" : "#C8F9E7"
                    })
                ]), width = 8, 
            ),

            dbc.Col(width=4)
        ]
    ),

#Row 4
    dbc.Row(
        children = [
            dbc.Col( 
                html.Div([    
                    html.P(
                    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim.
                    """,
                    style={
                            "margin-top": "60px",
                            "text-align":"right",
                            "font-family": "'Roboto', serif",
                            "padding": "5px",
                            "color": "#C8F9E7"
                    })
                ]), width = 8, 
            ),


            dbc.Col( 
                    html.Div([    
                        html.Img(src='https://placehold.co/300X200', alt='Placeholder Image', 
                                    style={"align": "right",
                                            "position": "relative", 
                                            "margin-top":"60px"}),
                    ]), width = 4, 
                ),


        ]
    ),




    ]
)

#Continue as needed