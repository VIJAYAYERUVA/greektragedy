import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

List = ['https://en.wikipedia.org/wiki/Greek_tragedy',
        'https://www.pbs.org/empires/thegreeks/background/24c.html']

layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            dcc.Markdown('''
        _This dashboard is to help to navigate the **"Classical Greek Tragedy literature analytics"**._
        ''',
                         className='text-center mb-4'
                         ),
            width=12
        )
    ),
    dbc.Row(
        dbc.Col(
            html.H1("Greek Literature",
                    className='font-weight-bold mb-4'),
            width=12)
    ),
    dbc.Row(
        dbc.Col(
            html.P(
                'The Ancient Greeks took their entertainment very seriously and used drama to investigate the world '
                'they lived in and what it meant to be human.',
            ),
            width=12)
    ),
    dbc.Row(
        dbc.Col(
            dcc.Markdown('''
        The three genres of drama were _**comedy**_, _**satyr plays**_, and most important of all, _**tragedy**_.
        ''',
                         className='mb-4'),
            width=12)
    ),
    dbc.Row(
        dbc.Col(
            html.P(children=[
                html.Strong('Comedy:'),
                html.P(
                    'The first comedies were mainly satirical and mocked men in power for their vanity and '
                    'foolishness. The first master of comedy was the playwright Aristophanes. Much later, '
                    'Menander wrote comedies about ordinary people and made his plays more like sitcoms.'
                )
            ]),
            width=12)
    ),
    dbc.Row(
        dbc.Col(
            html.P(children=[
                html.Strong('Tragedy:'),
                dcc.Markdown('''
                Tragedy dealt with the big themes of love, loss, pride, the abuse of power, and the 
                fraught relationships between men and gods. Typically the main protagonist of a tragedy commits some 
                terrible crime without realizing how foolish and arrogant he has been. Then, as he slowly realizes 
                his error, the world crumbles around him. The three great playwrights of tragedy were **Aeschylus, 
                Euripides, and Sophocles**.
                ''')
            ]),
            width=12)
    ),
    dbc.Row(
        dbc.Col(
            html.P(children=[
                html.Strong('Satyr Plays:'),
                html.P(
                    'The first comedies were mainly satirical and mocked men in power for their vanity and '
                    'foolishness. The first master of comedy was the playwright Aristophanes. Much later, '
                    'Menander wrote comedies about ordinary people and made his plays more like sitcoms.'
                )
            ]),
            width=12)
    ),
    dbc.Row(
        dbc.Col(
            html.H2("Greek Tragedy",
                    className='font-weight-bold mb-4'),
            width=12)
    ),
    dbc.Row([

        dbc.Col([
            html.Img(src='assets/Dionysos_mask.jpg',
                     alt="Dionysos's Mask",
                     title="Dionysos's Mask",
                     style={'height': '100px', 'width': '80px'}
                     )

        ], xs=12, sm=12, md=12, lg=1, xl=1),

        dbc.Col([
            dcc.Markdown('''
            Greek tragedy is widely believed to be an extension of the ancient rites carried out 
            honor of Dionysus. It heavily influenced the theatre of Ancient Rome and the Renaissance. Tragic plots 
            were most often based upon myths from the oral traditions of archaic epics. In tragic theatre, however, 
            these narratives were presented by actors. The most acclaimed Greek tragedians are **Aeschylus, 
            Euripides, and Sophocles**. These tragedians often explored many themes around human nature, mainly as a 
            way of connecting with the audience and bringing the audience into the play.
            ''',
                         )
        ], xs=12, sm=12, md=12, lg=11, xl=11),
    ],
        className='mb-4',
        no_gutters=False,
        justify='start'),
    dbc.Row(
        dbc.Col(
            html.H4("Greek Tragedy Authors: Aeschylus, Euripides, and Sophocles",
                    className='font-weight-bold'),
            width=12)
    ),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(
                        src='assets/Aeschylus.JPG',
                        title='Aeschylus',
                        top=True,
                        style={'height': '13rem', 'width': '11rem'}
                    ),
                    dbc.CardBody(
                        [
                            html.H4("Aeschylus", className="card-title"),
                        ]
                    ),
                ],
                style={'height': '17rem', 'width': '11rem', 'display': 'inline-block'},

            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src='assets/Euripides.jpg',
                        title='Euripides',
                        top=True,
                        style={'height': '13rem', 'width': '11rem'}
                    ),
                    dbc.CardBody(
                        [
                            html.H4("Euripides", className="card-title"),
                        ]
                    ),
                ],
                style={'height': '17rem', 'width': '11rem', 'display': 'inline-block'},
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src='assets/Sophocles.jpg',
                        title='Sophocles',
                        top=True,
                        style={'height': '13rem', 'width': '11rem'}
                    ),
                    dbc.CardBody(
                        [
                            html.H4("Sophocles", className="card-title"),
                        ]
                    ),
                ],
                style={'height': '17rem', 'width': '11rem', 'display': 'inline-block'},
            )
        ], width=12),
    ],
        className='mb-4',
        justify="start"),
    dbc.Row([
        dbc.Col(
            html.H5("References:",
                    className='font-weight-bold'),
            width=12)

    ]),
    dbc.Row([
        dbc.Col([
            html.Ol(id='my-list',
                    children=[html.Li(dcc.Link(href=i, target='_blank')) for i in List]),

        ],
            width=12)
    ])

],
    fluid=True,
    style={
        'color': 'black'
    }
)

# # Images Encoding
# Dionysos_mask_encoded = base64.b64encode(open('../assets/Dionysos_mask.jpg', 'rb').read())
# Aeschylus_encoded = base64.b64encode(open('../assets/Aeschylus.JPG', 'rb').read())
# Euripides_encoded = base64.b64encode(open('../assets/Euripides.jpg', 'rb').read())
# Sophocles_encoded = base64.b64encode(open('../assets/Sophocles.jpg', 'rb').read())
#
# src='data:image/png;base64,{}'.format(Euripides_encoded.decode())
