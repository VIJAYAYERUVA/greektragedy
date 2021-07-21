import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server
# Connect to your app pages
from apps import authors, characters

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Authors|', href='/apps/authors'),
        dcc.Link('Characters', href='/apps/characters'),
    ], className="row"),
    html.Div(id='page-content',
             children=[])
],
    style={'font-family': 'Rockwell'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/authors':
        return authors.layout
    if pathname == '/apps/characters':
        return characters.layout
    else:
        return "Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)
