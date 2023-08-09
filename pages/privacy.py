import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd

#---------------------------------#
#DATASET
proof = pd.read_csv("Processed Datasets/proof_cleaned.csv")

#---------------------------------#
#DATAFRAMES

proof_name = pd.DataFrame(proof['name'].value_counts()).reset_index()
proof_name.rename(columns = {proof_name.columns[0]:'type', proof_name.columns[1]:'count'}, inplace = True)
proof_name['type'] = proof_name['type'].replace([False, True], ['No name', 'Includes name'])

nametype = pd.DataFrame(proof[['type']][proof['name'] == True].value_counts()).reset_index()
nametype.rename(columns = {nametype.columns[0]:'type', nametype.columns[1]:'count'}, inplace = True)

#---------------------------------#
#name_fig

name_fig = px.pie(proof_name, values = 'count', names = 'type', title = 'Proof Name')

name_fig.update_layout(height=600)

name_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font_color="#C8F9E7",  
    font_family="'Space Grotesk', sans-serif",  # Font family
)

name_colors = ["#C8F9E7", "#c8daf9"]

name_fig.update_traces(marker_colors=name_colors)

#---------------------------------#
#nametype_fig

nametype_fig = px.pie(nametype, values = 'count', names = 'type', title = 'Proof Name Type')

nametype_fig.update_layout(height=600)

nametype_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font_color="#C8F9E7",  
    font_family="'Space Grotesk', sans-serif",  # Font family
)

nametype_colors = ["#C8F9E7", "#c8daf9", "#f9c8da", "#f9e7c8", "#cfc8f9", "#f3f9c8"]

nametype_fig.update_traces(marker_colors=nametype_colors)

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
                    html.P('Privacy Concerns', style={
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
                        
                        dcc.Graph(figure = name_fig)

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
                           
                            dcc.Graph(figure = nametype_fig)


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