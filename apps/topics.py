import dash_bootstrap_components as dbc
import dash_html_components as html

layout = dbc.Container([
    dbc.Row(id='title',
            children=[
                dbc.Col([
                    html.H2("Explore the Topics", className='text-center font-weight-bold ml-4 mr-4 mt-4 mb-4')
                ],
                    align='center',
                    xs=12, sm=12, md=12, lg=12, xl=12,
                )
            ],
            justify='center',
            align='center',
            ),
    dbc.Row([
        dbc.Col([
            html.H3('pyLDA Visualization of Topics from Greek Tragedy'),
            html.ObjectEl(
                # To my recollection you need to put your static files in the 'assets' folder
                data='../assets/pyLDAtopics.html',
                type="application/pdf",
                style={"width": "80vw", "height": "100vh"},
            ),
        ],
            align='center',
            xs=12, sm=12, md=12, lg=12, xl=12, )
    ],
        justify='center',
        align='center',
    ),
    dbc.Row([
        dbc.Col([
            html.H3('Word clouds of Topics from Greek Tragedy'),
            html.Div([
                html.H6('Topic 1'),
                html.Img(src='../assets/Topic1_wordcloud.png'),
                html.H6('Topic 3'),
                html.Img(src='../assets/Topic0_wordcloud.png'),

            ],
                style={'width': '46%', 'display': 'inline-block'}),
            html.Div([
                html.H6('Topic 2'),
                html.Img(src='../assets/Topic2_wordcloud.png'),
                html.H6('Topic 4'),
                html.Img(src='../assets/Topic3_wordcloud.png'),
            ],
                style={'width': '46%', 'float': 'right', 'display': 'inline-block'}),

        ],
            align='center',
            xs=12, sm=12, md=12, lg=12, xl=12,
        )
    ],
        justify='center',
        align='center',
    )
],
    fluid=True)
