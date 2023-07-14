import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

#---------------------------------#
#STYLING




#---------------------------------#
#APP
app = dash.Dash(__name__, use_pages=True)

#---------------------------------#
#APPLICATION LAYOUT
app.layout = html.Div([
	html.H1('Sino Ka?!'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ],
        style={'display': 'flex', 'flex-direction': 'row', 'align-items': 'center'}
    ),

	dash.page_container
])


#---------------------------------#
if __name__ == '__main__':
    app.run_server(debug=True)