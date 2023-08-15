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
fig = fig = px.bar(top[:20], x = 'word', y = 'count')

fig.update_layout(height= 400)

fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  #plot area
    paper_bgcolor='rgba(0, 0, 0, 0)',  #background for the entire graph
    font_color = "white",
    font_family="'Space Grotesk', sans-serif",
)

fig.update_traces(marker=dict(color="#aae906"))

#rename x and y axis labels
fig.update_xaxes(title_text='the top 20 words found in the dataset')
fig.update_yaxes(title_text='count of words')


#---------------------------------#
dash.register_page(__name__, path="/")

layout = html.Div(
    style={
        "background-image":"url('https://github.com/AGR-Yes/ScamMessagesPhilippines/blob/main/Images/bg/bg1.png?raw=true')",
        "background-repeat": "no-repeat",
        "background-size": "100%",
        "background-position": "center center",
        "background-color": "black",
        "width":"100%",
        "position":"relative",
        "padding-right":"12px",
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
                                        "margin-top": "20px",
                                        'font-style': 'italic',
                                        "font-family": "'Press Start 2P', display",
                                        'font-size': '50px',
                                        "color": "#E9CA06",
                                        "text-shadow": "1px 1px 5px #a39904",
                                        "padding": "10px"
                            }),
                            html.Div(
                                html.P(
                                    """
This project aims to collate, dig deeper, and visualize datasets of Spam Texts in the Philippines. Backed up by research, the end goal of this project is to create a dashboard that shows data but also tells a story of how data privacy and hacking became a concern during the pandemic.
                                    """
                                ),
                                style={
                                    "margin-top":"-30px",
                                    "font-size": "15px", 
                                    "whiteSpace": "pre-wrap",
                                    'color':'white',
                                    "padding-left": "20px",
                                    "padding-right":"30px",
                                    },
                            ),
                        ], style ={
                            "margin-left":"45px",
                            "margin-top":"40px",
                        }
                    ),
                    width=5,  # Adjust the width of the first column
                ),
                dbc.Col([
                    
                    dcc.Graph(figure=fig, style={"padding":"10px"})

                ],
                    width=7,  # Adjust the width of the second column
                    className="mt-4",
                ),
            ],
        ),

        html.Br(),

        dbc.Row(
            children=[
                dbc.Col(
                    width=1
                ),
                dbc.Col(
                    html.Div(
                        [
                        html.P(
                            '''
In 2020, COVID-19 hit the world, and on January 30, 2020, the first case was confirmed in the Philippines. The World Health Organization (WHO) declared Covid-19 a pandemic in March of the same year.
                            ''', 
                            style = {"padding": "10px",
                                    'color':'white',
                                    'whiteSpace': 'pre-wrap',
                                    "margin-top":"30px"}
                            ),
                            
                            html.Br(),

                    html.Div(
                        [
                        html.H1('Gaining Information',
                                style = {
                                    "text-shadow": "2px 2px 5px #a39904",
                                    "color":"#E9CA06"
                                    }),
                        html.P(
                            '''
Contact tracing was done with offline methods (by pen and a printed form) and online methods such as forms and a QR code per person in each city. (Job Manahan, ABS-CBN News, 2022) 
To get a QR code, citizens would register with their personal data. Data was stored and collected with online and offline means.
                            ''',
                            style = {
                                "color":"white"
                            }
                        )
                    ], style = {"border": "1px white solid",
                                "border-radius": "10px",
                                "padding": "10px",
                                'whiteSpace': 'pre-wrap'}
                    ),
                        ], 
                    ), width=5
                ),
                dbc.Col(
                    html.Div(
                        [
                        html.Br(),
                        html.Div(
                            [
                            html.H1('Tracking People',
                                    style = {
                                    "text-shadow": "2px 2px 5px #a39904",
                                    "color":"#E9CA06"
                                }),
                            html.P(
                                '''
Contact tracing was a method to keep track of people entering establishments; so that if someone tested positive for Covid, people who entered the same establishment at the same period could be notified that they were exposed and get tested as a safety measure. In short, contact tracing was a way to track down positive cases. (Job Manahan, ABS-CBN News, 2022)
                                ''',
                                style = {
                                    "color":"white"
                                }
                            )
                        ], style = {"border": "1px white solid",
                                    "border-radius": "10px",
                                    "padding": "10px",
                                    'whiteSpace': 'pre-wrap'}
                        ),

                        html.Br(),
                        html.Div(
                            [
                            html.H1("What's the Dataset?",
                                    style = {
                                    "text-shadow": "2px 2px 5px #a39904",
                                    "color":"#E9CA06"
                                    }),
                            html.P(
                                '''
The primary dataset used for this project was a Google Sheets file that was open to all kinds of users. The file allowed users to input the text messages they've received as well as the phone number, and the type of message it was (lotto, casino, job offer, etc.). If the message received the recipient's number.
                                ''',
                                    style = {
                                        "color":"white"
                                }
                            )
                        ], style = {"border": "1px white solid",
                                    "border-radius": "10px",
                                    "padding": "10px",
                                    'whiteSpace': 'pre-wrap'}
                            ),
                        ], 
                    ), width=5
                ),
                dbc.Col(
                    width=1
                ),
            ]
        ),
    
        html.Br(),

        dbc.Row(
            children=[
                html.P("how to navigate this website", 
                       style={
                        #"margin-top": "30px",
                        'font-style': 'italic',
                        "font-family": "'Press Start 2P', display",
                        'font-size': '20px',
                        "text-shadow": "1px 1px 5px #a39904",
                        "padding": "10px",
                        "color":"#E9CA06"
                        }
                    ),

                html.P(
                    """
The charts you'll see on this website are interactive - all thanks to Plotly, an open-source module for data visualization. Since the charts are interactive, you may zoom in, hover, and select specific labels you want to see (for pie graphs). To zoom out, just double-click the chart.
                    """,
                    style = {"color":"white"}
                    ),
                

            ], style ={
                "padding":"50px",
                "text-align":"center",
                
            }
        ),

    ]
)