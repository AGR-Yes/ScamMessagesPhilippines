import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

#---------------------------------#
dash.register_page(__name__)

layout = html.Div(
    style={
        "background-image":"url('https://github.com/AGR-Yes/ScamMessagesPhilippines/blob/main/Images/bg/bg3.png?raw=true')",
        "background-repeat": "no-repeat",
        "background-size": "100%",
        "background-position": "center center",
        "background-color": "black",
        "width":"100%",
        "position":"relative",
        "padding-right":"12px",
    },
    
    children=[
        
#Row 1 - Title
    dbc.Row( 
            children=[ 
                    
                    html.Div([
                        html.H1(
                            "About the Project", style={
                            "text-align": "center",
                            "padding": "30px",
                            'font-size': '30px',
                            "font-family": "'Press Start 2P'",
                            "color":"#E9CA06",
                            "text-shadow": "1px 1px 5px #fff783",
                            
                        })
                    ]),



    #Column 1 - Meme photo
                    dbc.Col( 
                        html.Div([    
                            html.Img(src='https://cdn.vox-cdn.com/thumbor/8rF2keXrhL8sYlEbVbtaJpIC4qs=/0x10:500x291/1600x900/cdn.vox-cdn.com/uploads/chorus_image/image/59741997/n4scgse21iuz.0.jpg', alt='Placeholder Image', 
                                        style={
                                            "align": "right",
                                            "position": "relative", 
                                            #"margin-top":"60px",
                                            "width": "100%",
                                            "margin-left": "auto",
                                            "margin-right": "auto",}),
                        ]), width = 6, 
                    ),
                    

    #Column 2
                    dbc.Col(
                        html.Div([
                            html.Div([

                                #Content 
                                html.P("'Who is this?!'", style={
                                        "margin-top": "30px",
                                        'font-size': '20px',
                                        "font-family": "'Press Start 2P', display",
                                        #"padding": "5px",
                                        "color": "#E9CA06",

                                        }),  
                                
                                html.P(
                                        """
'Sino `To?!' is a project that aims to visualize the spam texts in the Philippines.
                                        """,
                                        style={
                                            "color": "white",
                                        }
                                ), 
                                
                                #Content 
                                html.P('Increase in Number', style={
                                        "margin-top": "30px",
                                        'font-size': '20px',
                                        "font-family": "'Press Start 2P', display",
                                        #"padding": "5px",
                                        "color": "#E9CA06"
                                        }),  
                                
                                html.P(
                                        """
From mail to electronic mail, our own phone numbers aren't even safe anymore. How bad is the spam in the country?
                                        """,
                                        style={
                                            "color": "white",
                                        }
                                ), 

                                
                                
                            ]),
                            ]), width = 5,  # column width
                    ),

                ], 
        ),

#Row 2
    dbc.Row(
        children=[
            html.Div([
                html.P(
                    """
The goal of Sino 'To? (Who is this?!) is to clean the datasets gathered from the internet and make the data understandable for the general public.
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

            html.Div([
                html.H1("About the Author", style={
                    "text-align": "center",
                    "padding": "30px",
                    'font-size': '30px',
                    "font-family": "'Press Start 2P', display",
                    "color":"#DCC2FF",
                    "text-shadow": "1px 1px 5px white",
                    "margin-top":"20px"
                    
                })
            ]),


            dbc.Col(
                html.Div([

                    html.Img(
                        src='https://github.com/AGR-Yes/ScamMessagesPhilippines/blob/main/Images/anton.jpeg?raw=true', #alt='Placeholder Image',
                             style={
                                "align": "right",
                                "position": "relative",
                                "width": "100%",
                                "margin-left": "30px",
                                "margin-right": "auto",
                            })

                ]),
                width=3),

            dbc.Col( 
                html.Div([            
                    
                    html.P("Anton Reyes (`AGR`)", 
                           style={
                                "font-family": "'Press Start 2P', display",
                                "font-size": "20px",
                                #"padding": "20px",
                                "margin-top" : "5px",
                                "margin-left" : "30px",
                                "padding" : "5px",
                                "color" : "#C8F9E7"
                           }),
                    html.Div([
                        html.P(
                        """
Anton, an undergraduate student from De La Salle University - Manila. He is a Marketing Management student with a minor in Data Science. 
                        """),

                        html.P(
                        """
Despite his interest and involvement in both the business and programming fields, he also does creative-related work as well. In the creative industry, he has created graphics, edited videos, print materials, and stages.
                        """),
                        ], style={
                            "margin-top" : "5px",
                            "margin-left" : "30px",
                            "font-family" : "'Roboto', serif",
                            "padding" : "5px",
                            "color" : "#C8F9E7"
                    })


                ]), width = 7, 
            ),

            dbc.Col(width = 2)
        ]
    ),

#Row 4
    dbc.Row(
        children = [
            dbc.Col( 
                html.Div([    
                    
                     html.P(
                        """
In data science, he aspires to make an impact and add more to the field, particularly in the Philippine context. Anton has been involved in a few group and personal projects that involved data preprocessing, Natural Language Processing (NLP), and visualization. With his passion for continuous learning and his interdisciplinary approach, Anton seeks to leverage his skills and knowledge to drive innovation and create meaningful solutions in the data science landscape.
                        """, style={
                                    "margin-top": "60px",
                                    "text-align":"right",
                                    "font-family": "'Roboto', serif",
                                    "padding": "5px",
                                    "color": "#C8F9E7"
                            }),
                    
                    
                ]), width = 8, 
            ),


            dbc.Col( 
                    html.Div([    
                        html.Img(src='https://github.com/AGR-Yes/ScamMessagesPhilippines/blob/main/Images/IMG_20230720_190918.jpg?raw=true', alt='Placeholder Image', 
                                    style={"align": "right",
                                            "position": "relative", 
                                            "margin-top":"60px",
                                            "position":"relative",
                                            "width":"100%"}),
                    ]), width = 4, 
                ),


        ]
    ),




    ]
)



#Continue as needed