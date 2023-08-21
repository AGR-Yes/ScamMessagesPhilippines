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
    font_color="white",  
    font_family="'Space Grotesk', sans-serif",  # Font family
)

name_colors = ["#e3ff83", "#758467"]

name_fig.update_traces(marker_colors=name_colors)

#---------------------------------#
#nametype_fig

nametype_fig = px.pie(nametype, values = 'count', names = 'type', title = 'Proof Name Type')

nametype_fig.update_layout(height=600)

nametype_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font_color="white",  
    font_family="'Space Grotesk', sans-serif",  # Font family
)

nametype_colors = ["#e3ff83", "#758467", "#819171", "#9CAF88", "#CBD5C0", "#DFE6DA"]

nametype_fig.update_traces(marker_colors=nametype_colors)

#---------------------------------#
#Duplicate this as needed, but this is the template for the content 

dash.register_page(__name__)

layout = html.Div(
    style={
        "background-image":"url('https://github.com/AGR-Yes/ScamMessagesPhilippines/blob/main/Images/bg/bg2.png?raw=true')",
        "background-repeat": "no-repeat",
        "background-size": "150%",
        "background-position": "center center",
        "background-color": "black",
        "width":"100%",
        "position":"relative",
        "padding-right":"12px",
    },

    children=[
        
#Title
        dbc.Row( 
            children=[
                html.Div([ 
                    
                    html.Br(),
                    html.P('Spam Texts', style={
                                "margin-top": "60px",
                                'text-align': 'center', 
                                'font-size': '50px',
                                "font-family": "'Press Start 2P', display",
                                "padding": "5px",
                                "color": "#E9CA06",
                                "text-shadow": "1px 1px 5px #a39904",
                                }), 
                    html.Br(),
                    html.P(
                            """
The Data Privacy Act of 2012, Chapter 1, Section 2, states that we must protect the fundamental human right of privacy, of communication while ensuring the free flow of information to promote innovation and growth. It also states that information and communication technology has a great contribution to nation-building and that it has an obligation to protect personal information.
                            """, style={
                                "margin-top": "-20px",
                                'margin-bottom':'15px',
                                'text-align': 'center', 
                                'font-size': '15px',
                                "font-family": "'Roboto', serif",
                                "padding": "5px",
                                "width": "80%",
                                "margin-left": "auto",
                                "margin-right": "auto",
                                "color": "white"
                                }),

                    ]), 
                ], 
        ),
        
        html.Br(),
        
#Content Row 1        
        dbc.Row(
            children=[
                
                html.Div([

                    html.H4("how'd they know my name?", style={
                                "text-align": "right",
                                "font-family": "'Press Start 2P', display",
                                "width": "90%",
                                "margin-left": "auto",
                                "margin-right": "60px",
                                "color": "#aae906"
                                })
                ]),

#Left Column                
                dbc.Col( 
                    html.Div([

                            html.Div([
                                html.P(
                                    """
In the dataset, we can see here the number of texts that included the names of the victims or recipients of spam. In the whole dataset, 14.9% of the texts included the recepient's name.
                                    """
                                ), 

                                html.P(
                                    '''
According to PNP-ACG Acting Director, Joel Doria, scammers have found ways to gain personal information aside from the phone number itself. He states that these scammers could've gained more information such as their names through purchasing mobile numbers that sold illegally. This information might have been sourced from social media platforms, online phone directories, filled-up raffle tickets, and even randomly checking numbers on messaging apps such as Viber. (Inocencio, 2022)
                                    ''', style={"margin-top":"-30px"}
                                )

                            ], style={
                                    "border": "1px", 
                                    "whiteSpace": "pre-wrap",
                                    "padding-left": "10px",
                                    "width": "80%",
                                    "margin-left": "auto",
                                    "margin-right": "auto",
                                    "color": "white",
                                    "margin-top":"40px"
                                },
                            ),
                        ]
                    ),
                    width=4,  # Adjust the width of the first column
                ),

#Right Column
                dbc.Col( 
                    html.Div([
                        
                        dcc.Graph(figure = name_fig)

                    ]),
                    width=8,  # Adjust the width of the second column
                    #className="mt-4",
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
Here, we can see the types of labels of the texts that include the name of the recipients.
                                    '''
                                )

                            ], style = {"border": "1px white solid",
                                        "border-radius": "10px",
                                        "padding": "10px",
                                        'whiteSpace': 'pre-wrap',
                                        "margin-top": "50px",
                                        #"margin-left": "auto",
                                        "margin-right": "auto",
                                        "color": "white"},                              
                            ),
                            html.Br(),
                            html.H3('type of texts with names',
                                    style={
                                        "font-family": "'Press Start 2P', display",
                                        "color": "#E9CA06",
                                        "margin-top":"-10px",
                                        "margin-left":"10px"
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


    ]
)

#Continue as needed