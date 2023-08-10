import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px

import pandas as pd

#register_page = dash.Dash(__name__, path ="/", )

#---------------------------------#
#DATASET

top = pd.read_csv("Processed Datasets/top100_words.csv")

#FIGURE
fig = fig = px.bar(top[:20], x = 'word', y = 'count', title = 'Top 20 Words')

fig.update_layout(height= 400)

fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  #plot area
    paper_bgcolor='rgba(0, 0, 0, 0)',  #background for the entire graph
    font_color = "#C8F9E7",
    font_family="'Space Grotesk', sans-serif",
)

fig.update_traces(marker=dict(color="#250DAB"))


#---------------------------------#
dash.register_page(__name__, path="/")

layout = html.Div(
    style={
        "background-color": "black",
    },

    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    html.Div(
                        [
                            html.Br(className="mt-4"),
                            
                            html.P("'Who is this?!'", 
                                   style={
                                        "margin-top": "10px",
                                        'font-style': 'italic',
                                        "font-family": "'Press Start 2P', display",
                                        'font-size': '50px',
                                        "color": "#C8F9E7",
                                        "text-shadow": "1px 1px 5px white",
                                        "padding": "10px"
                            }),
                            html.Div(
                                html.P(
                                    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada. Donec vehicula tincidunt ante, eu dignissim nisl pharetra ac. Nulla nisi magna, hendrerit eu libero vitae, blandit interdum ipsum. Aenean quis viverra nibh.
                                    """
                                ),
                                style={
                                    "font-size": "15px", 
                                    "whiteSpace": "pre-wrap",
                                    'color':'#C8F9E7',
                                    "padding-left": "20px",
                                    "padding-right":"30px",
                                    },
                            ),
                        ]
                    ),
                    width=6,  # Adjust the width of the first column
                ),
                dbc.Col([
                    
                    dcc.Graph(figure=fig, style={"padding":"10px"})

                ],
                    width=6,  # Adjust the width of the second column
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
                                ''', 
                                style = {"padding": "10px",
                                        'color':'#DCC2FF',
                                        'whiteSpace': 'pre-wrap'}
                                ),
                            
                            html.Br(),

                            html.Div(
                                [
                                html.H1('Test',
                                        style = {"text-shadow": "2px 2px 5px white",}),
                                html.P(
                                    '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada.
                                    '''
                                )
                            ], style = {"border": "1px white solid",
                                        "border-radius": "10px",
                                        "padding": "10px",
                                        'color':'#DCC2FF',
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
                                html.H1('Test',
                                        style = {"text-shadow": "2px 2px 5px white",}),
                                html.P(
                                    '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada.
                                    '''
                                )
                            ], style = {"border": "1px white solid",
                                        "border-radius": "10px",
                                        "padding": "10px",
                                        'color':'#DCC2FF',
                                        'whiteSpace': 'pre-wrap'}
                            ),

                            html.Br(),
                            html.Div(
                                [
                                html.H1('Test',
                                        style = {"text-shadow": "2px 2px 5px white",}),
                                html.P(
                                    '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim. Pellentesque commodo volutpat ex convallis malesuada.
                                    '''
                                )
                            ], style = {"border": "1px white solid",
                                        "border-radius": "10px",
                                        "padding": "10px",
                                        'color':'#DCC2FF',
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