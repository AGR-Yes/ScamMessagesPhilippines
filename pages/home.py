import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px


#---------------------------------#

dash.register_page(__name__)

layout = html.Div(
    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    html.Div(
                        [
                            html.P("'Who is this?!'", style={"margin-top": "10px",
                                                            'font-style': 'italic',
                                                            "font-family": "'Press Start 2P', display",
                                                            "padding": "20px"}),
                            html.Div(
                                html.P(
                                    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada. Donec vehicula tincidunt ante, eu dignissim nisl pharetra ac. Nulla nisi magna, hendrerit eu libero vitae, blandit interdum ipsum. Aenean quis viverra nibh.
                                    """
                                ),
                                style={
                                    "border": "1px", 
                                    "whiteSpace": "pre-wrap",
                                    #add left padding
                                    "padding-left": "20px",
                                    },
                            ),
                        ]
                    ),
                    width=7,  # Adjust the width of the first column
                ),
                dbc.Col(
                    html.Div(
                        html.Img(src='https://placehold.co/500X600', alt='Placeholder Image')
                    ),
                    width=5,  # Adjust the width of the second column
                    className="mt-4",
                ),
            ],
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