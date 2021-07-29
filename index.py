import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import about, authors, plays, characters, topics

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Tabs(id='tabs', value='about', children=[
                dcc.Tab(label='About', value='about'),
                dcc.Tab(label='Authors', value='authors'),
                dcc.Tab(label='Plays', value='plays'),
                dcc.Tab(label='Characters', value='characters'),
                dcc.Tab(label='Topics', value='topics'),
            ])
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id='page-content',
                     children=[])
        ])
    ])
],
    fluid=True,
    style={
        'font-size': '1.2em',
        'color': 'red',
    }
)


@app.callback(Output('page-content', 'children'),
              [Input('tabs', 'value')])
def display_page(tab):
    if tab == 'about':
        return about.layout
    if tab == 'authors':
        return authors.layout
    if tab == 'plays':
        return plays.layout
    if tab == 'characters':
        return characters.layout
    if tab == 'topics':
        return topics.layout
    else:
        return "Please choose a tab"


if __name__ == '__main__':
    app.run_server(debug=False)
