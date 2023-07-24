import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px


#---------------------------------#
#Duplicate this as needed, but this is the template for the content 

dash.register_page(__name__)

layout = html.Div(
    children=[
        
#Title
        dbc.Row( 
            children=[
                html.Div([ 
                    
                    html.P('Title', style={
                                "margin-top": "30px",
                                'text-align': 'center', 
                                'font-size': '50px',
                                "font-family": "'Press Start 2P', display",
                                }), 
                    
                    html.P(
                            """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada. Donec vehicula tincidunt ante, eu dignissim nisl pharetra ac. Nulla nisi magna, hendrerit eu libero vitae, blandit interdum ipsum. Aenean quis viverra nibh.
                            """, style={
                                "margin-top": "5px",
                                'text-align': 'center', 
                                'font-size': '12px',
                                "font-family": "'Roboto', serif",
                                "padding": "5px",
                                "width": "80%",
                                "margin-left": "auto",
                                "margin-right": "auto",
                                }),

                    ]), 
                ], 
        ),
        
        
        
#Content Row 1        
        dbc.Row(
            children=[
                
                
                
                dbc.Col( #Left Column
                    html.Div([

                            html.Div(
                                html.P(
                                    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada. Donec vehicula tincidunt ante, eu dignissim nisl pharetra ac. Nulla nisi magna, hendrerit eu libero vitae, blandit interdum ipsum. Aenean quis viverra nibh.
                                    """
                                ), style={
                                        "border": "1px", 
                                        "whiteSpace": "pre-wrap",
                                        "padding-left": "10px",
                                    },
                            ),
                        ]
                    ),
                    width=5,  # Adjust the width of the first column
                ),

                dbc.Col( #Right Column
                    html.Div([
                        
                        html.Img(src='https://placehold.co/600X300', alt='Placeholder Image', 
                                 style={"align": "right",})

                    ]),
                    width=7,  # Adjust the width of the second column
                    className="mt-4",
                ),
            ], style = {
                        "width": "90%",
                        "margin-left": "auto",
                        "margin-right": "auto",}
        ),

        html.Br(),

        dbc.Row(
            children=[
                dbc.Col(
                    #buffer
                    width=2
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.P(
                                '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada.
                                '''
                                ),
                            
                            html.Br(),

                            html.Div(
                                [
                                html.H1('Test'),
                                html.P(
                                    '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada.
                                    '''
                                )
                            ], style = {"border": "1px black solid",
                                        "border-radius": "10px",
                                        "padding": "10px",
                                        'whiteSpace': 'pre-wrap'}
                            ),
                        ], 
                    ), width=4
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.Br(),
                            html.Div(
                                [
                                html.H1('Test'),
                                html.P(
                                    '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada.
                                    '''
                                )
                            ], style = {"border": "1px black solid",
                                        "border-radius": "10px",
                                        "padding": "10px",
                                        'whiteSpace': 'pre-wrap'}
                            ),

                            html.Br(),
                            html.Div(
                                [
                                html.H1('Test'),
                                html.P(
                                    '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada.
                                    '''
                                )
                            ], style = {"border": "1px black solid",
                                        "border-radius": "10px",
                                        "padding": "10px",
                                        'whiteSpace': 'pre-wrap'}
                            ),
                        ], 
                    ), width=4
                ),
                dbc.Col(
                    #buffer
                    width=2
                ),
            ]
        )
    ]
)