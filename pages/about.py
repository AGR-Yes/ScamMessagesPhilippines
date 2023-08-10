import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

#---------------------------------#
dash.register_page(__name__)

layout = html.Div(
    style={
        "background-color": "black",
        "margin-left": "auto",
        "margin-right": "auto",
    },
    
    children=[
        
#Title
    dbc.Row( 
            children=[ 
                    
                    html.Div([
                        html.H1("About the Project", style={
                            "text-align": "center",
                            "padding": "30px",
                            'font-size': '30px',
                            "font-family": "'Press Start 2P', display",
                            "color":"#DCC2FF",
                            "text-shadow": "1px 1px 5px white",
                            
                        })
                    ]),



#Column 1
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
                                        "color": "#C8F9E7",

                                        }),  
                                
                                html.P(
                                        """
'Sino `To?!' is a project that aims to visualize the spam texts in the Philippines.
                                        """,
                                        style={
                                            "color": "#C8F9E7",
                                        }
                                ), 
                                
                                #Content 
                                html.P('Increase in Number', style={
                                        "margin-top": "30px",
                                        'font-size': '20px',
                                        "font-family": "'Press Start 2P', display",
                                        #"padding": "5px",
                                        "color": "#C8F9E7"
                                        }),  
                                
                                html.P(
                                        """
From mail to electronic mail, our own phone numbers aren't even safe anymore. How bad is the spam in the country?
                                        """,
                                        style={
                                            "color": "#C8F9E7",
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

                    html.Img(src='https://github.com/AGR-Yes/ScamMessagesPhilippines/blob/main/Images/anton.jpeg?raw=true', alt='Placeholder Image',
                             style={
                                "align": "right",
                                "position": "relative",
                                "width": "100%",
                                "margin-left": "30px",
                                "margin-right": "auto",
                                "margin-bottom":"30px"})

                ]),
                width=3),

            dbc.Col( 
                html.Div([            
                    
                    html.P("Anton Reyes (`AGR`)", 
                           style={
                                "font-family": "'Press Start 2P', display",
                                "font-size": "20px",
                                #"padding": "20px",
                                "margin-top" : "30px",
                                "margin-left" : "30px",
                                "padding" : "5px",
                                "color" : "#C8F9E7"
                           }),
                    
                    html.P(
                    """

○

○

○

                    """,
                    style={
                            "margin-top" : "30px",
                            "margin-left" : "30px",
                            "font-family" : "'Roboto', serif",
                            "padding" : "5px",
                            "color" : "#C8F9E7"
                    })
                ]), width = 6, 
            ),

            dbc.Col(width = 3)
        ], style = {"border": "1px white solid",
                    "border-radius": "10px",
                    "padding": "10px",
                    'color':'#DCC2FF',
                    }
    ),

#Row 4
    dbc.Row(
        children = [
            dbc.Col( 
                html.Div([    
                    html.P(
                    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida vel ipsum in luctus. Sed rhoncus sagittis tellus, vitae egestas orci. Mauris interdum iaculis eros et dignissim.
                    """,
                    style={
                            "margin-top": "60px",
                            "text-align":"right",
                            "font-family": "'Roboto', serif",
                            "padding": "5px",
                            "color": "#C8F9E7"
                    })
                ]), width = 8, 
            ),


            dbc.Col( 
                    html.Div([    
                        html.Img(src='https://placehold.co/300X200', alt='Placeholder Image', 
                                    style={"align": "right",
                                            "position": "relative", 
                                            "margin-top":"60px"}),
                    ]), width = 4, 
                ),


        ]
    ),




    ]
)



#Continue as needed