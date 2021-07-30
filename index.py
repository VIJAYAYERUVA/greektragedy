import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
from apps import about, authors, plays, characters, topics

app.layout = html.Div(
    [
        dcc.Location(
            id="url",
            pathname="/apps/about"
        ),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Home", href="/apps/about", active="exact"),
                dbc.NavLink("Authors", href="/apps/authors", active="exact"),
                dbc.NavLink("Plays", href="/apps/plays", active="exact"),
                dbc.NavLink("Characters", href="/apps/characters", active="exact"),
                dbc.NavLink("Topics", href="/apps/topics", active="exact"),
            ],
            brand="Classical Greek Tragedy",
            brand_style={
                'font-size': '20px'
            },
            color="dark",
            dark=True,
            style={
                'font-size': '20px'
            },
        ),
        dbc.Container(
            id="page-content",
            className="pt-4",
            fluid=True),
    ]
)


@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/apps/about':
        return about.layout
    if pathname == '/apps/authors':
        return authors.layout
    if pathname == '/apps/plays':
        return plays.layout
    if pathname == '/apps/characters':
        return characters.layout
    if pathname == '/apps/topics':
        return topics.layout

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=False)
