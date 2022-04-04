# Packages
from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc

# Initiate app
external_stylesheets = [dbc.themes.LUMEN]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Here it is!'
server = app.server

# Layout
app.layout = dbc.Container([
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5(id='question',
                                       children='Is it working?',
                                       style={'text-align': 'center'})),
                dbc.CardBody([
                    dcc.Dropdown(id='dropdown',
                                 options=['Yes.', 'No.', 'Not sure!'],
                                 value='Not sure!'),
                    html.Hr(),
                    dcc.Markdown(id='answer',
                                 children=[],
                                 style={'text-align': 'center'}),
                ]),
            ])
        ], width=4)
    ], justify='center'),
])


@app.callback(
    Output(component_id='answer', component_property='children'),
    Input(component_id='dropdown', component_property='value'))
def display_answer(value):
    if value == 'Yes.':
        return f'**Great!** '
    elif value == 'No.':
        return f'**Opps! Looks like it\'s working.**'
    else:
        return f'**No worries! Looks like it\'s working.**'


if __name__ == '__main__':
    app.run_server(debug=True)
