import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

#---------------------------------#
ref_style ={"font-family" : "'Roboto', serif",
            "padding" : "5px",
            "color" : "white"}

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
                'padding': '20px',             
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

#Row 6- References
    dbc.Row(
        children=[
            html.Div([
                html.P('references',
                    style={
                        "text-align": "center",
                        "padding": "30px",
                        'font-size': '20px',
                        "font-family": "'Press Start 2P', display",
                        "color":"#E9CA06",
                        "text-shadow": "1px 1px 5px #a39904",
                        "margin-top":"20px",
                        }
                ),
            ]), 

            dbc.Col(width = 1),

            dbc.Col([
                html.Div([
                    html.P([
                        "Dev, P. P. (2023, February 7). 2023 Complete list of Philippine mobile network prefixes. PreFIX PH. ",
                        html.A("www.prefix.ph/prefixes/2023-complete-list-of-philippine-mobile-network-prefixes/ ",
                            href="https://www.prefix.ph/prefixes/2023-complete-list-of-philippine-mobile-network-prefixes/"),
                    ]),

                    html.P([
                        "DOH denies contact tracing behind recent surge in text scams. (n.d.). Cnn. ",
                        html.A("www.cnnphilippines.com/news/2022/9/12/DOH-contact-tracing-scams-subscribers-names.html",
                            href="https://www.cnnphilippines.com/news/2022/9/12/DOH-contact-tracing-scams-subscribers-names.html"),
                    ]),

                    html.P([
                        "Gregorio, X. (2022, September 7). Scam texts got your name? These apps may have been the source. Philstar.com. ",
                        html.A("www.philstar.com/business/2022/09/07/2208049/scam-texts-got-your-name-these-apps-may-have-been-source",
                            href="https://www.philstar.com/business/2022/09/07/2208049/scam-texts-got-your-name-these-apps-may-have-been-source"),
                    ]),

                    html.P([
                        "Gübür, K. T. (2022). NLTK Tokenize: How to Tokenize Words and Sentences with NLTK? - Holistic SEO. Holistic SEO. ",
                        html.A("www.holisticseo.digital/python-seo/nltk/tokenization",
                            href="https://www.holisticseo.digital/python-seo/nltk/tokenization"),
                    ]),

                    html.P([
                        "Gutierrez, J. (2010, June 16). Philippine wrestles with “Jejemon” cyber-dialect. The Sydney Morning Herald. ",
                        html.A("www.smh.com.au/technology/philippine-wrestles-with-jejemon-cyberdialect-20100616-yf7s.html",
                            href="https://www.smh.com.au/technology/philippine-wrestles-with-jejemon-cyberdialect-20100616-yf7s.html"),
                    ]),

                    html.P([
                        "Inocencio, S. (2022, September 4) PNP bares ways scammers get personal info of spam text recipients. CNN. ",
                        html.A("www.cnnphilippines.com/news/2022/9/4/scammers-personal-info-scam-messages.html",
                            href="https://www.cnnphilippines.com/news/2022/9/4/scammers-personal-info-scam-messages.html"),
                    ]),
                    
                    html.P([
                        "Job Manahan, ABS-CBN News. (2022, September 2). NTC: Text scammers may have used contact-tracing data. ABS-CBN News. ",
                        html.A("www.news.abs-cbn.com/news/09/02/22/ntc-text-scammers-may-have-used-contact-tracing-dat",
                            href="https://www.news.abs-cbn.com/news/09/02/22/ntc-text-scammers-may-have-used-contact-tracing-dat"),
                    ]),
                    
                    html.P([
                        "National Privacy Commission. (2022, February 12). Republic Act 10173 - Data Privacy Act of 2012 - National Privacy Commission. ",
                        html.A("privacy.gov.ph/data-privacy-act/",
                            href="https://privacy.gov.ph/data-privacy-act/"),
                    ]),
                    
                    html.P([
                        "McManus, M. (2023, February 8). How to create a multipage Dash App - Michael McManus - Medium. Medium. ",
                        html.A("medium.com/@mcmanus_data_works/how-to-create-a-multipage-dash-app-261a8699ac3f",
                            href="https://medium.com/@mcmanus_data_works/how-to-create-a-multipage-dash-app-261a8699ac3f"),
                    ]),
                    
                    html.P([
                        "Philippine News Agency. (2022, June 9). ",
                        html.A("www.pna.gov.ph/articles/1176291",
                            href="https://www.pna.gov.ph/articles/1176291"),
                    ]),
                    
                    html.P([
                        "Placehold | A simple, fast and free image placeholder service. (n.d.). ",
                        html.A("placehold.co/",
                            href="https://placehold.co/"),
                    ]),
                    
                    html.P([
                        "Rathi, P. (2022, May 21). Creating a multi-page Dash Application - Level Up Coding. Medium. ",
                        html.A("levelup.gitconnected.com/creating-a-multi-page-dash-application-ab38b4b91bf5",
                            href="https://levelup.gitconnected.com/creating-a-multi-page-dash-application-ab38b4b91bf5"),
                    ]),
                    
                    html.P([
                        "Regalado, P. (2023). Added to Yet Another Viber Group? Here Are Anti-Spam Tips. SPOT.PH. ",
                        html.A("www.spot.ph/newsfeatures/adulting/104999/how-to-avoid-spam-getting-added-to-viber-groups-a4832-20230529",
                            href="https://www.spot.ph/newsfeatures/adulting/104999/how-to-avoid-spam-getting-added-to-viber-groups-a4832-20230529"),
                    ]),
                    
                    html.P([
                        "Santos, R. (2021, December 1). Why You’re Getting Spam Texts, According to a Cybersecurity Expert. VICE. ",
                        html.A("www.vice.com/en/article/epxxmk/why-spam-texts-philippines-cybersecurity-expert-tips",
                            href="https://www.vice.com/en/article/epxxmk/why-spam-texts-philippines-cybersecurity-expert-tips"),
                    ]),
                    
                    html.P([
                        "Stopwords-Iso. (n.d.). stopwords-tl/raw/genediazjr-tagalog.txt at master · stopwords-iso/stopwords-tl. GitHub. ",
                        html.A("github.com/stopwords-iso/stopwords-tl/blob/master/raw/genediazjr-tagalog.txt",
                            href="https://github.com/stopwords-iso/stopwords-tl/blob/master/raw/genediazjr-tagalog.txt"),
                    ]),
                    
                    html.P([
                        "Team, R. (2022). Why is My Viber Name on Text Spam? Some Twitter Users Asks. SPOT.PH. ",
                        html.A("www.spot.ph/newsfeatures/trending/100686/viber-name-spam-text-trending-what-happened-a4671-20220906",
                            href="https://www.spot.ph/newsfeatures/trending/100686/viber-name-spam-text-trending-what-happened-a4671-20220906"),
                    ]),
                ], style = ref_style),
                ], width = 10),

            dbc.Col(width = 1),
        ], 
        style={

        }
    ),

    html.Br(),
    html.Br(),

    ]
)



#Continue as needed