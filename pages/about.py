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
                        "about the project", style={
                        "text-align": "center",
                        "padding": "30px",
                        'font-size': '30px',
                        "font-family": "'Press Start 2P'",
                        "color":"#E9CA06",
                        "text-shadow": "1px 1px 5px #a39904",
                        "margin-top":"15px"
                        
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
                                            "margin-right": "auto",
                                            "box-shadow": "0px 0px 7px white"}),
                        ]), width = 6, 
                    ),
                    

    #Column 2
                    dbc.Col(
                        html.Div([
                            html.Div([

                                #Content 
                                html.P("what is this?!", style={
                                        "margin-top": "30px",
                                        'font-size': '20px',
                                        "font-family": "'Press Start 2P', display",
                                        #"padding": "5px",
                                        "color": "#E9CA06 ",

                                        }),  
                                
                                html.P(
                                        """
Sino 'To?! (Who is this?!) This project visualizes spam texts in the Philippines. This data came from a Google Sheets file that was made public to Filipino Netizens (Internet Citizens) to record the texts they received.
                                        """,
                                        style={
                                            "color": "white",
                                        }
                                ), 
                                
                                #Content 
                                html.P('project goal', style={
                                        "margin-top": "30px",
                                        'font-size': '20px',
                                        "font-family": "'Press Start 2P', display",
                                        #"padding": "5px",
                                        "color": "#E9CA06 "
                                        }),  
                                
                                html.P(
                                        """
The goal of this project was to clean the datasets gathered from the internet and make the data understandable for the general public through charts.
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

#Row 2 - About author 1
    dbc.Row(
        children = [

            html.Div([
                html.H1("about the author", style={
                    "text-align": "center",
                    "padding": "30px",
                    'font-size': '30px',
                    "font-family": "'Press Start 2P', display",
                    "color":"#aae906",
                    "text-shadow": "1px 1px 5px #e3ff83",
                    "margin-top":"20px",
                    
                })
            ]),

            dbc.Col(width = 1),

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
                                "box-shadow": "0px 0px 7px white",
                            })

                ]),
                width=2),

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
                                "color" : "#aae906"
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
                            "color" : "white"
                    })


                ]), width = 7, 
            ),

            dbc.Col(width = 1)
        ]
    ),

#Row 3 - About author 2
    dbc.Row(
        children = [
            
            dbc.Col(width = 1),

            dbc.Col( 
                html.Div([    
                    html.P(
                        """
In data science, he aspires to make an impact and add more to the field, particularly in the Philippine context. Anton has been involved in a few group and personal projects that involved data preprocessing, Natural Language Processing (NLP), and visualization. 
                        """, style={
                                    "margin-top": "60px",
                                    "text-align":"right",
                                    "font-family": "'Roboto', serif",
                                    "padding": "5px",
                                    "color": "white"
                            }),
                    
                     html.P(
                        """
With his passion for continuous learning and his interdisciplinary approach, Anton seeks to leverage his skills and knowledge to drive innovation and create meaningful solutions in data science.
                        """, style={
                                    #"margin-top": "60px",
                                    "text-align":"right",
                                    "font-family": "'Roboto', serif",
                                    "padding": "5px",
                                    "color": "white"
                            }),



                    
                    ]), width = 7, 
                ),

            dbc.Col( 
                html.Div([    
                    html.Img(src='https://github.com/AGR-Yes/ScamMessagesPhilippines/blob/main/Images/IMG_20230720_190918.jpg?raw=true', alt='Placeholder Image', 
                                style={"align": "right",
                                        "position": "relative", 
                                        "margin-top":"60px",
                                        "position":"relative",
                                        "width":"100%",
                                        "box-shadow": "0px 0px 7px #e3ff83",
                                    }),
                    ]), width = 3, 
                ),

            dbc.Col(width = 1),

        ]
    ),

#Row 4 - Contact
    dbc.Row(
        children=[
            html.Div([
                
                html.P('contact me', style = {
                                        "text-align": "center",
                                        "padding": "30px",
                                        'font-size': '20px',
                                        "font-family": "'Press Start 2P'",
                                        "color":"#E9CA06",
                                        "text-shadow": "1px 1px 5px #a39904",
                                        "margin-top":"10px"
                                        }
                    ),
    
                html.A("Personal Instagram",
                    href="https://www.instagram.com/ant0nreyes/",
                    style={'margin-right': '10px', 'font-family':"'Space Grotesk', sans-serif'", 'color':'white'  }),
                
                html.A("2nd Instagram",
                    href="https://www.instagram.com/agrsworkspace/",
                    style={'margin-right': '10px', 'font-family':"'Space Grotesk', sans-serif'", 'color':'white'  }),
                
                html.A("Github",
                    href="https://github.com/agr-Yes/",
                    style={'margin-right': '10px', 'font-family':"'Space Grotesk', sans-serif'", 'color':'white'  }),
                
                html.A("LinkedIn",
                    href="https://www.linkedin.com/in/antongreyes/",
                    style={'font-family':"'Space Grotesk', sans-serif'", 'color':'white'  }),


                        ], style={
                            'position': 'relative', 
                            'bottom': 0, 
                            'width': '100%', 
                            'text-align': 'center', 
                            'padding': '20px'            
                            }
            )
        ]
    ),

#Row 5 - Collaboration
    dbc.Row(
        children=[
            html.Div([
                html.P(
                    """
Under the Philippine Internet Archive, this project is in collaboration with Kakakompyuter Mo Yan!
                    """,
                    style={
                                "margin-top": "60px",
                                'text-align': 'center', 
                                'font-size': '16px',
                                "font-family": "'Roboto', serif",
                                "padding": "5px",
                                "width": "80%",
                                "margin-left": "auto",
                                "margin-right": "auto",
                                "color": "#E9CA06"
                                }
                ),
            ])
        ]
    ),
 
    html.Br(),
    html.Br(),

    ]
)



#Continue as needed