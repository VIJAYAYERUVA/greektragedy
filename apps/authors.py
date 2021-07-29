import pathlib

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

from app import app
from apps import helper_methods

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# ---------- Import and clean data (importing csv into pandas)
data = pd.read_csv(DATA_PATH.joinpath("Authors.csv"))

authors = data['AuthorName'].value_counts().index.tolist()

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H4("Explore the Authors",
                    className='text-center font-weight-bold ml-4 mr-4 mt-4 mb-4')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='authors_dcount', figure={})
        ],
            width={'offset': 1},
            xs=11, sm=11, md=11, lg=5, xl=5),
        dbc.Col([
            dcc.Graph(id='authors_bert', figure={})
        ],
            width={'offset': 1},
            xs=11, sm=11, md=11, lg=5, xl=5
        )
    ]),

    # html.Div([
    #     html.Div(
    #         id="authors_count",
    #         children=[
    #             dcc.Graph(id='authors_dcount', figure={}),
    #         ],
    #         style={'width': '46%', 'display': 'inline-block'}),
    #
    #     html.Div([],
    #              style={'width': '7%', 'display': 'inline-block'}),
    #
    #     html.Div([
    #         dcc.Graph(id='authors_gcdcount', figure={}),
    #     ],
    #         style={'width': '46%', 'float': 'right', 'display': 'inline-block'}),
    # ]),

    html.Div([
        html.Div(
            id="authors_senti",
            children=[
                dcc.Graph(id='authors_vader', figure={}),
            ],
            style={'width': '46%', 'display': 'inline-block'}),

        html.Div([],
                 style={'width': '7%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(id='authors_bert', figure={}),
        ],
            style={'width': '46%', 'float': 'right', 'display': 'inline-block'}),
    ]),

    html.Div([

        html.Div([
            html.Label('Select Author to compare'),
            dcc.Dropdown(id="slct_author1",
                         options=[{'label': a, 'value': a} for a in sorted(authors)],
                         multi=False,
                         value='Aeschylus',
                         style={'width': "100%"}
                         ),
            html.Div(id='output_container1', children=[])
        ],
            style={'width': '46%', 'display': 'inline-block'}),

        html.Div([],
                 style={'width': '7%', 'display': 'inline-block'}),

        html.Div([
            html.Label('Select Author to compare'),
            dcc.Dropdown(id="slct_author2",
                         options=[{'label': a, 'value': a} for a in sorted(authors)],
                         multi=False,
                         value='Euripides',
                         style={'width': "100%"}
                         ),
            html.Div(id='output_container2', children=[])
        ],
            style={'width': '46%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        html.Div([
            dcc.Graph(id='author_sunburst1', figure={}),
            # dcc.Graph(id='author_sunburst1', figure={}, style={'width': '90vh', 'height': '90vh'}),
        ],
            style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

        html.Div([
            dcc.Graph(id='author_sunburst2', figure={}),
            # dcc.Graph(id='author_sunburst2', figure={}, style={'width': '90vh', 'height': '90vh'}),
        ],
            style={'width': '49%', 'display': 'inline-block', 'float': 'right'})
    ], style={}
    ),

],
    fluid=True,
    style={
        'color': 'black'
    },
)


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components

@app.callback(
    [Output(component_id='authors_dcount', component_property='figure'),
     Output(component_id='authors_gcdcount', component_property='figure')],
    [Input(component_id='authors_count', component_property='value')]
)
def update_graph_1(authors_count):
    # fig1 creation
    dff1 = data.copy()
    df1 = (dff1.groupby(['AuthorName']).size()).reset_index()
    df1.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    fig1 = px.bar(df1,
                  x="AuthorName",
                  y="NoOfDialogues",
                  color="AuthorName",
                  labels=helper_methods.labels,
                  hover_name='AuthorName',
                  hover_data={
                      "AuthorName": False,
                  },
                  color_discrete_map=helper_methods.authors_color,
                  text=df1['NoOfDialogues'],
                  )

    fig1.update_xaxes(title_text="")

    fig1.update_layout(
        title='<b>Total #dialogues from three authors</b>',
        legend_title_text='Authors',
    )
    fig1.update_layout(helper_methods.update_layout1)

    # fig2 creation
    authors = sorted(dff1['AuthorName'].unique())
    ## Initialize figure with subplots
    fig2 = make_subplots(
        rows=1, cols=3, subplot_titles=("Gender", "Class", "Divinity")
    )

    # Add traces
    fig2.append_trace(
        go.Bar(
            x=authors,
            y=[18, 74, 15],
            name='Female',
            text=[18, 74, 15],
            textposition='auto',
            marker_color='#d091b5'),
        row=1, col=1)

    fig2.append_trace(
        go.Bar(x=authors,
               y=[30, 111, 43],
               name='Male',
               text=[30, 111, 43],
               textposition='auto',
               marker_color='#aa5986'),
        row=1, col=1)

    fig2.append_trace(
        go.Bar(x=authors,
               y=[15, 77, 23],
               name='Lower',
               text=[15, 77, 23],
               textposition='auto',
               marker_color='#fbd485'),
        row=1, col=2)

    fig2.append_trace(
        go.Bar(x=authors,
               y=[33, 108, 35],
               name='Upper',
               text=[33, 108, 35],
               textposition='auto',
               marker_color='#f79647'),
        row=1, col=2)

    fig2.append_trace(
        go.Bar(x=authors,
               y=[38, 163, 55],
               name='Mortal',
               text=[38, 163, 55],
               textposition='auto',
               marker_color='#2988ad'),
        row=1, col=3)

    fig2.append_trace(
        go.Bar(x=authors,
               y=[10, 22, 3],
               name='Immortal',
               text=[10, 22, 3],
               textposition='auto',
               marker_color='#003c78'),
        row=1, col=3)

    fig2.update_yaxes(title_text="#Characters", row=1, col=1)

    # Update title and height
    fig2.update_layout(
        title='<b>Total #characters from three authors including Gender, Class, Divinity</b>',
    )
    fig2.update_layout(helper_methods.update_layout1)
    return fig1, fig2


@app.callback(
    [Output(component_id='authors_vader', component_property='figure'),
     Output(component_id='authors_bert', component_property='figure')],
    [Input(component_id='authors_senti', component_property='value')]
)
def update_graph_2(authors_count):
    # fig1 creation

    dff2 = data.copy()

    df2 = (dff2.groupby(['AuthorName', 'VADER_Label']).size()).reset_index()
    df2.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df2 = df2.groupby(['AuthorName', 'VADER_Label']).agg({'NoOfDialogues': 'sum'})
    df2['PercentageOfDialogues'] = df2.groupby(level=0).apply(helper_methods.percentage)
    df2 = df2.reset_index()

    fig1 = px.bar(df2,
                  x="AuthorName",
                  y="PercentageOfDialogues",
                  color="VADER_Label",
                  labels={
                      "VADER_Label": "VADER Sentiment",
                      "AuthorName": "Authors",
                      "PercentageOfDialogues": "% of Dialogues"
                  },
                  hover_name='AuthorName',
                  hover_data={
                      "AuthorName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.VADER_Sentiment,
                  category_orders={
                      "VADER_Label": ["positive", "negative"]
                  },
                  # text=df['VADER_Label']
                  text=df2['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig1.update_xaxes(title_text="")

    fig1.update_layout(
        title='<b>Distribution of Sentiments in Authors</b>',
        legend_title_text='VADER Sentiment',
    )
    fig1.update_layout(helper_methods.update_layout1)

    dff3 = data.copy()

    df3 = (dff3.groupby(['AuthorName', 'BERT_Emotion']).size()).reset_index()
    df3.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df3 = df3.groupby(['AuthorName', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    df3['PercentageOfDialogues'] = df3.groupby(level=0).apply(helper_methods.percentage)
    df3 = df3.reset_index()

    fig2 = px.bar(df3,
                  x="AuthorName",
                  y="PercentageOfDialogues",
                  color="BERT_Emotion",
                  labels={
                      "BERT_Emotion": "BERT Emotion",
                      "AuthorName": "Authors",
                      "PercentageOfDialogues": "% of Dialogues"
                  },
                  hover_name='AuthorName',
                  hover_data={
                      "AuthorName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.BERT_Emotions,
                  category_orders={
                      "BERT_Emotion": ["neutral", "joy", "sadness", "fear", "anger"]
                  },
                  # text=df['BERT_Emotion']
                  text=df3['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig2.update_xaxes(title_text="")

    fig2.update_layout(
        title='<b>Distribution of Emotions in Authors</b>',
        legend_title_text='BERT Emotions',
    )
    fig2.update_layout(helper_methods.update_layout1)

    return fig1, fig2


@app.callback(
    [Output(component_id='output_container1', component_property='children'),
     Output(component_id='author_sunburst1', component_property='figure'),
     Output(component_id='output_container2', component_property='children'),
     Output(component_id='author_sunburst2', component_property='figure')],
    [Input(component_id='slct_author1', component_property='value'),
     Input(component_id='slct_author2', component_property='value')]
)
def update_graph_3(option_slctd1, option_slctd2):
    print('Author1: ', option_slctd1)
    container1 = "The Author chosen by user was: {}".format(option_slctd1)

    dff1 = data.copy()

    authordf1 = dff1.loc[dff1['AuthorName'] == option_slctd1]
    playDistribution1 = np.array_split(authordf1, 10)

    tempauthordf1 = []
    for i, part in enumerate(playDistribution1):
        part['PofPlay'] = (i + 1) * 10
        part['PofPlay'] = part['PofPlay'].apply(helper_methods.percentagelabel)
        tempauthordf1.append(part)
    tempauthordf1 = pd.concat(tempauthordf1)

    authordf1 = tempauthordf1

    # Get all plays from each author
    dfff1 = (authordf1.groupby(['PofPlay', 'BERT_Emotion']).size()).reset_index()
    dfff1.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    dfff1 = dfff1.groupby(['PofPlay', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    dfff1['PercentageOfDialogues'] = dfff1.groupby(level=0).apply(helper_methods.percentage)
    dfff1 = dfff1.reset_index()

    # Plotly Express
    # Stacked Bar plot with Author's play vs. BERT Emotions
    fig1 = px.bar(dfff1,
                  x="PofPlay",
                  y="PercentageOfDialogues",
                  color="BERT_Emotion",
                  labels={
                      "BERT_Emotion": "BERT Emotion",
                      "PofPlay": "Percentage of Play",
                      "PercentageOfDialogues": "% of Dialogues"
                  },
                  hover_name='PofPlay',
                  hover_data={
                      "PofPlay": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.BERT_Emotions,
                  category_orders=helper_methods.Emotion_Order
                  # text=dfff1['BERT_Emotion']
                  # text=df['PercentageOfDialogues'].apply(lambda x: '{0:1.2f}%'.format(x))
                  )

    fig1.update_xaxes(title_text="")

    fig1.update_layout(
        title='<b>Distribution of Emotions in Author(' + option_slctd1 + ')</b>',
        legend_title_text='Emotions',
        legend=dict(
            orientation="h",
            x=0,
            y=-0.25, )
    )
    fig1.update_layout(helper_methods.update_layout1)

    print('Author2: ', option_slctd2)
    container2 = "The Author chosen by user was: {}".format(option_slctd2)

    dff2 = data.copy()

    authordf2 = dff2.loc[dff2['AuthorName'] == option_slctd2]
    playDistribution2 = np.array_split(authordf2, 10)

    tempauthordf2 = []
    for i, part in enumerate(playDistribution2):
        part['PofPlay'] = (i + 1) * 10
        part['PofPlay'] = part['PofPlay'].apply(helper_methods.percentagelabel)
        tempauthordf2.append(part)
    tempauthordf2 = pd.concat(tempauthordf2)

    authordf2 = tempauthordf2

    # Get all plays from each author
    dfff2 = (authordf2.groupby(['PofPlay', 'BERT_Emotion']).size()).reset_index()
    dfff2.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    dfff2 = dfff2.groupby(['PofPlay', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    dfff2['PercentageOfDialogues'] = dfff2.groupby(level=0).apply(helper_methods.percentage)
    dfff2 = dfff2.reset_index()

    # Plotly Express
    # Stacked Bar plot with Author's play vs. BERT Emotions
    fig2 = px.bar(dfff2,
                  x="PofPlay",
                  y="PercentageOfDialogues",
                  color="BERT_Emotion",
                  labels={
                      "BERT_Emotion": "BERT Emotion",
                      "PofPlay": "Percentage of Play",
                      "PercentageOfDialogues": "% of Dialogues"
                  },
                  hover_name='PofPlay',
                  hover_data={
                      "PofPlay": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.BERT_Emotions,
                  category_orders=helper_methods.Emotion_Order
                  # text=dfff2['BERT_Emotion']
                  # text=df['PercentageOfDialogues'].apply(lambda x: '{0:1.2f}%'.format(x))
                  )

    fig2.update_xaxes(title_text="")

    fig2.update_layout(
        title='<b>Distribution of Emotions in Author(' + option_slctd2 + ')</b>',
        legend_title_text='Emotions',
        legend=dict(
            orientation="h",
            x=0,
            y=-0.25, )
    )
    fig2.update_layout(helper_methods.update_layout1)

    return container1, fig1, container2, fig2
