import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server
# Connect to your app pages
from apps import authors, characters, topics

app.layout = html.Div([
    html.Div([
        dcc.Tabs(id='tabs', value='authors', children=[
            dcc.Tab(label='Authors', value='authors'),
            dcc.Tab(label='Characters', value='characters'),
            dcc.Tab(label='Topics', value='topics'),
        ])
    ], className="row"),
    html.Div(id='page-content',
             children=[])
],
    style={'font-family': 'Rockwell',
           'font-size': '1.2em',
           'color': 'red',
           'font-weight': 'bold',
           })


@app.callback(Output('page-content', 'children'),
              [Input('tabs', 'value')])
def display_page(tab):
    if tab == 'authors':
        return authors.layout
    if tab == 'characters':
        return characters.layout
    if tab == 'topics':
        return topics.layout
    else:
        return "Please choose a tab"


if __name__ == '__main__':
    app.run_server(debug=False)
