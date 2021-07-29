import dash_html_components as html

layout = html.Div([
    html.H2('Explore the Topics',
            style={
                'text-align': 'center',
                'padding': 25
            }),
    html.Div([
        html.H3('pyLDA Visualization of Topics from Greek Tragedy'),
        html.ObjectEl(
            # To my recollection you need to put your static files in the 'assets' folder
            data='../assets/pyLDAtopics.html',
            type="application/pdf",
            style={"width": "80vw", "height": "100vh"}
        ),
    ]),
    html.Div([
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
    ]),
],
    style={
        'font-family': 'Rockwell',
        'font-size': 'medium',
        'color': 'black',
        'font-weight': 'normal',
    })
