import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd

#---------------------------------#
#DATASETS

proof = pd.read_csv("Processed Datasets/proof_cleaned.csv")
select = pd.read_csv("Processed Datasets/select.csv")
spam = pd.read_csv("Processed Datasets/spam.csv")

#---------------------------------#
#DATAFRAMES

proof_type = pd.DataFrame(proof['type'].value_counts()).reset_index()
proof_type.rename(columns = {proof_type.columns[0]:'type', proof_type.columns[1]:'count'}, inplace = True)

number = pd.DataFrame(select['network'].value_counts()).reset_index()
number.rename(columns = {number.columns[0]:'network', number.columns[1]:'count'}, inplace = True)

spam['day'] = pd.to_datetime(spam['Date']).dt.day_name()
spam_day = pd.DataFrame(spam['day'].value_counts()).reset_index()
spam_day.rename(columns = {spam_day.columns[0]:'day', spam_day.columns[1]:'count'}, inplace = True)

spam['Time'] = pd.to_datetime(spam['Time'])
spam['Time'] = spam['Time'].dt.time
spam['time_of_day'] = spam['Time'].apply(lambda dt: dt.replace(minute=0, second=0, microsecond=0))
spam_time = pd.DataFrame(spam['time_of_day'].value_counts()).reset_index()
spam_time.rename(columns = {spam_time.columns[0]:'time_of_day', spam_time.columns[1]:'count'}, inplace = True)
spam_time = spam_time.sort_values(by = 'time_of_day')

#---------------------------------#
#proof_fig

proof_fig = px.pie(proof_type, values='count', names='type', title='Proof Type')

proof_fig.update_layout(height=600)

proof_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font_color="white",  
    font_family="'Space Grotesk', sans-serif",  # Font family
)

proof_colors = ["#e3ff83", "#758467", "#819171", "#9CAF88", "#CBD5C0", "#DFE6DA"] #6 colors

proof_fig.update_traces(marker_colors=proof_colors)

#---------------------------------#
#number_fig

number_fig = px.bar(number, x = 'network', y = 'count', title = 'Number of Incidents by Network')

number_fig.update_layout(height= 500)

number_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  #plot area
    paper_bgcolor='rgba(0, 0, 0, 0)',  #background for the entire graph
    font_color = "white",
    font_family="'Space Grotesk', sans-serif",
)

number_fig.update_traces(marker=dict(color="#fff347"))

#---------------------------------#
#time_fig

time_fig = px.line(spam_time, x = 'time_of_day', y = 'count', title = 'Time of Day')


time_fig.update_xaxes(
    tickvals=[0, 6, 12, 18],  # Choose the tick positions
    ticktext=['12 AM', '6 AM', '12 PM', '6 PM'],  # Choose the tick labels
    tickmode='array'  # Use an array of ticks
)

time_fig.update_layout(height=500)

time_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  #plot area
    paper_bgcolor='rgba(0, 0, 0, 0)',  #background for the entire graph
    font_color = "white",
    font_family="'Space Grotesk', sans-serif",
    xaxis=dict(gridwidth=0.1), 
    yaxis=dict(gridwidth=0.1),  
)

time_fig.update_traces(line=dict(color="#aae906"))
time_fig.update_traces(line=dict(width=4))

#---------------------------------#
#day_fig

day_fig = px.pie(spam_day, values='count', names='day', title='Proof Type')

day_fig.update_layout(height=600)

day_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font_color="white",  
    font_family="'Space Grotesk', sans-serif",  # Font family
)

day_colors = ["#fff347", "#758467", "#819171", "#9CAF88", "#CBD5C0", "#DFE6DA", "white"] #7 colors

day_fig.update_traces(marker_colors=day_colors)


#---------------------------------#

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
Spam texts are considered to be the unsolicited and unwanted messages we receive. Oftentimes, messages like these may contain job offers, business opportunities, and lotto/gambling opportunities. (PNP Bares Ways Scammers Get Personal Info of Spam Text Recipients, n.d.)
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

                    html.H2("types of spam messages", style={
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

                            html.Div(
                                html.P(
                                    """
In the original Google Sheet, there are more than 20+ labels for the texts and to better see everything, the labels were narrowed down to 6 - with ‘Others’, which contains labels that didn’t fit the other five and had the lowest counts.
                                    """
                                ), style={
                                        "border": "1px", 
                                        "whiteSpace": "pre-wrap",
                                        "padding-left": "10px",
                                        "width": "80%",
                                        "margin-left": "auto",
                                        "margin-right": "auto",
                                        "color": "white",
                                        "margin-top":"30px"
                                    },
                            ),
                        ]
                    ),
                    width=4,  # Adjust the width of the first column
                ),

#Right Column
                dbc.Col( 
                    html.Div([
                        
                        dcc.Graph(figure = proof_fig)

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
                    [
                        
                        dcc.Graph(figure = number_fig, style = {"padding":"10px"})

                    ], width=7
                ),

#Right column
                dbc.Col(
                    html.Div(
                        [

                            html.Br(),
                            html.Div(
                                [

                            html.P([
"The Google Sheets dataset contained the phone numbers of the senders and due to inconsistencies in the Google Sheet with identifying the networks for each number. A dictionary was made from ",
html.A('Network Prefixes', href='https://www.prefix.ph/prefixes/2023-complete-list-of-philippine-mobile-network-prefixes/', style={"color":"white"}),
" to re-label the numbers to make them accurate."
                            ])

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
                            html.H1('networks present in the dataset',
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


#Content Row 3
        dbc.Row(
            children=[
                html.Div([

                    dcc.Graph(figure = time_fig, style = {"padding":"10px"})

                ], style={"text-align": "center",
                          "padding": "20px"}
            )
        ]),

        html.Br(),

#Content Row 4
        dbc.Row(
            children=[
                html.Div([

                    html.P(
                        """
In this graph, we see the average time of day that scammers send their messages. Here we can see the count of each post per hour with the peak at 6:00 AM. Do note that this graph comes from a Kaggle dataset and the data is only from one user.
                        """, style={
                            "margin-top": "-50px",
                            'text-align': 'center', 
                            'font-size': '15px',
                            "font-family": "'Roboto', serif",
                            "padding": "5px",
                            "width": "80%",
                            "margin-left": "auto",
                            "margin-right": "auto",
                            "color": "white"
                            }),
                ])
            ]
        ),

        html.Br(),

#Content Row 5
        dbc.Row(
            children=[
                
                html.Div([

                    html.H2("days most active", style={
                                "text-align": "right",
                                "font-family": "'Press Start 2P', display",
                                "width": "90%",
                                "margin-left": "auto",
                                "margin-right": "60px",
                                "color": "#E9CA06"
                                })
                ]),

#Left Column                
                dbc.Col( 
                    html.Div([

                            html.Div(
                                html.P(
                                    """
Not to be confused with the ideal time for posting, but from the secondary dataset, the days with the most number of texts were on Saturday, and the least count on Thursday.
                                    """
                                ), style={
                                        "border": "1px", 
                                        "whiteSpace": "pre-wrap",
                                        "padding-left": "10px",
                                        "width": "80%",
                                        "margin-left": "auto",
                                        "margin-right": "auto",
                                        "color": "white",
                                        "margin-top":"30px"
                                    },
                            ),
                        ]
                    ),
                    width=4,  # Adjust the width of the first column
                ),

#Right Column
                dbc.Col( 
                    html.Div([
                        
                        dcc.Graph(figure = day_fig, style = {"margin-right":"20px"})

                    ]),
                    width=8,  # Adjust the width of the second column
                    #className="mt-4",
                ),
            ]
        ),

        html.Br(),


    ]
)