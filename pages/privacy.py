import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

#---------------------------------#
#Duplicate this as needed, but this is the template for the content 

dash.register_page(__name__)

layout = html.Div(
    style={
        "background-color": "black",
    },

    children=[
        
#Title
        dbc.Row( 
            children=[
                html.Div([ 
                    
                    html.Br(),
                    html.P('Title', style={
                                "margin-top": "60px",
                                'text-align': 'center', 
                                'font-size': '50px',
                                "font-family": "'Press Start 2P', display",
                                "padding": "5px",
                                "color": "#C8F9E7"
                                }), 
                    html.Br(),
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
                                "color": "#C8F9E7"
                                }),

                    ]), 
                ], 
        ),
        
        html.Br(),
        
#Content Row 1        
        dbc.Row(
            children=[
                
                html.Div([

                    html.H2("Chart Title", style={
                                "text-align": "right",
                                "font-family": "'Press Start 2P', display",
                                "width": "90%",
                                "margin-left": "auto",
                                "margin-right": "60px",
                                "color": "#C8F9E7"
                                })
                ]),

#Left Column                
                dbc.Col( 
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
                                        "width": "80%",
                                        "margin-left": "auto",
                                        "margin-right": "auto",
                                        "color": "#C8F9E7"
                                    },
                            ),
                        ]
                    ),
                    width=5,  # Adjust the width of the first column
                ),

#Right Column
                dbc.Col( 
                    html.Div([
                        
                        html.Img(src='https://placehold.co/650X300', alt='Placeholder Image', 
                                 style={"align": "right",
                                        "position": "relative"})

                    ]),
                    width=7,  # Adjust the width of the second column
                    className="mt-4",
                ),
            ]
        ),

        html.Br(),


#Content Row 2
        dbc.Row(
            children=[

#Left column
                dbc.Col(
                    html.Div(
                        [
                           
                            html.Img(src='https://placehold.co/500X350', alt='Placeholder Image', 
                                 style={"align": "right",
                                        "position": "relative"}),


                        ] 
                    ), width=7
                ),

#Right column
                dbc.Col(
                    html.Div(
                        [

                            html.Br(),
                            html.Div(
                                [

                                html.P(
                                    '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada.
                                    '''
                                )

                            ], style = {"border": "1px black solid",
                                        "border-radius": "10px",
                                        "padding": "10px",
                                        'whiteSpace': 'pre-wrap',
                                        #"width": "80%",
                                        "margin-left": "auto",
                                        "margin-right": "auto",
                                        "color": "#C8F9E7"},                                
                            ),
                            html.Br(),
                            html.H1('Test',
                                    style={
                                        "font-family": "'Press Start 2P', display",
                                        "color": "#C8F9E7",
                                    })

                        ], 
                    ), width=5
                )
            ], style = {
                        "padding": "20px",
                        "width": "80%",
                        "margin-left": "auto",
                        "margin-right": "auto",}

        ),

        html.Br(),


#Content Row 3
        dbc.Row(
            children=[
                html.Div([

                    html.P(
                        """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada. Donec vehicula tincidunt ante, eu dignissim nisl pharetra ac. Nulla nisi magna, hendrerit eu libero vitae, blandit interdum ipsum. Aenean quis viverra nibh.
                        """, style={
                            "margin-top": "5px",
                            'text-align': 'center', 
                            'font-size': '12px',
                            "font-family": "'Roboto', serif",
                            "padding": "5px",
                            #"width": "80%",
                            "margin-left": "auto",
                            "margin-right": "auto",
                            "color": "#C8F9E7"
                            }),
                ])
            ]
        ),

        html.Br(),

#Content Row 4
        dbc.Row(
            children=[
                html.Div([

                    html.Img(src='https://placehold.co/800X300', alt='Placeholder Image')

                ], style={"text-align": "center",
                          "padding": "20px"}
            )
        ])

    ]
)

#Continue as needed