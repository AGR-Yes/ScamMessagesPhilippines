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

proof_fig.update_layout(height=500)

proof_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font_color="#C8F9E7",  
    font_family="'Space Grotesk', sans-serif",  # Font family
)

proof_colors = ["#C8F9E7", "#c8daf9", "#f9c8da", "#f9e7c8", "#cfc8f9", "#f3f9c8"]

proof_fig.update_traces(marker_colors=proof_colors)

#---------------------------------#
#number_fig

number_fig = px.bar(number, x = 'network', y = 'count', title = 'Number of Incidents by Network')

number_fig.update_layout(height= 500)

number_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  #plot area
    paper_bgcolor='rgba(0, 0, 0, 0)',  #background for the entire graph
    font_color = "#C8F9E7",
    font_family="'Space Grotesk', sans-serif",
)

number_fig.update_traces(marker=dict(color="#250DAB"))

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
    font_color = "#C8F9E7",
    font_family="'Space Grotesk', sans-serif",
    xaxis=dict(gridwidth=0.1), 
    yaxis=dict(gridwidth=0.1),  
)

time_fig.update_traces(marker=dict(color="#250DAB"))
time_fig.update_traces(line=dict(width=4))

#---------------------------------#
#day_fig

day_fig = px.pie(spam_day, values='count', names='day', title='Proof Type')

day_fig.update_layout(height=500)

day_fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font_color="#C8F9E7",  
    font_family="'Space Grotesk', sans-serif",  # Font family
)

day_colors = ["#C8F9E7", "#c8daf9", "#f9c8da", "#f9e7c8", "#cfc8f9", "#f3f9c8", "#DCC2FF"]

day_fig.update_traces(marker_colors=day_colors)


#---------------------------------#

dash.register_page(__name__)

layout = html.Div(
    style={
        "background-color": "black",
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
                        
                        dcc.Graph(figure = proof_fig)

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

                    dcc.Graph(figure = time_fig, style = {"padding":"10px"})

                ], style={"text-align": "center",
                          "padding": "20px"}
            )
        ]),

        html.Br(),

#Content Row 5
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
                        
                        dcc.Graph(figure = day_fig, style = {"margin-right":"20px"})

                    ]),
                    width=7,  # Adjust the width of the second column
                    className="mt-4",
                ),
            ]
        ),

        html.Br(),


    ]
)