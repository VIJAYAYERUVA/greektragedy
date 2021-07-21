import pathlib

import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

BERT_Emotions = {'anger': '#b44a1c',
                 'fear': '#ed9619',
                 'joy': '#1c9674',
                 'neutral': '#48596e',
                 'sadness': '#35afcf'
                 }

Emotion_Order = {'BERT_Emotion': ['neutral', 'joy', 'sadness', 'fear', 'anger']}


# function to calculate %
def percentage(x):
    return 100 * x / float(x.sum())


# function  to create label
def percentagelabel(x):
    if x == 10:
        return '(0-10)% of the play'
    elif x == 20:
        return '(10-20)% of the play'
    elif x == 30:
        return '(20-30)% of the play'
    elif x == 40:
        return '(30-40)% of the play'
    elif x == 50:
        return '(40-50)% of the play'
    elif x == 60:
        return '(50-60)% of the play'
    elif x == 70:
        return '(60-70)% of the play'
    elif x == 80:
        return '(70-80)% of the play'
    elif x == 90:
        return '(80-90)% of the play'
    elif x == 100:
        return '(90-100)% of the play'
    else:
        pass


# ---------- Import and clean data (importing csv into pandas)
data = pd.read_csv(DATA_PATH.joinpath("Authors.csv"))

authors = data['AuthorName'].value_counts().index.tolist()

layout = html.Div([
    html.H1("Data from Authors", style={'text-align': 'center'}),
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
            style={'width': '49%', 'display': 'inline-block'}),

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
            style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ],
        style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px',
            'font_family': 'Rockwell'
        }),

    html.Div([
        dcc.Graph(id='author_sunburst1', figure={}),
        # dcc.Graph(id='author_sunburst1', figure={}, style={'width': '90vh', 'height': '90vh'}),
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dcc.Graph(id='author_sunburst2', figure={}),
        # dcc.Graph(id='author_sunburst2', figure={}, style={'width': '90vh', 'height': '90vh'}),
    ], style={'display': 'inline-block', 'width': '49%'})
], style={'font-family': 'Rockwell'})


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container1', component_property='children'),
     Output(component_id='author_sunburst1', component_property='figure'),
     Output(component_id='output_container2', component_property='children'),
     Output(component_id='author_sunburst2', component_property='figure')],
    [Input(component_id='slct_author1', component_property='value'),
     Input(component_id='slct_author2', component_property='value')]
)
def update_graph(option_slctd1, option_slctd2):
    print('Author1: ', option_slctd1)
    container1 = "The Author chosen by user was: {}".format(option_slctd1)

    dff1 = data.copy()

    authordf1 = dff1.loc[dff1['AuthorName'] == option_slctd1]
    playDistribution1 = np.array_split(authordf1, 10)

    tempauthordf1 = []
    for i, part in enumerate(playDistribution1):
        part['PofPlay'] = (i + 1) * 10
        part['PofPlay'] = part['PofPlay'].apply(percentagelabel)
        tempauthordf1.append(part)
    tempauthordf1 = pd.concat(tempauthordf1)

    authordf1 = tempauthordf1

    # Get all plays from each author
    dfff1 = (authordf1.groupby(['PofPlay', 'BERT_Emotion']).size()).reset_index()
    dfff1.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    dfff1 = dfff1.groupby(['PofPlay', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    dfff1['PercentageOfDialogues'] = dfff1.groupby(level=0).apply(percentage)
    dfff1 = dfff1.reset_index()

    # Plotly Express
    # Stacked Bar plot with Author's play vs. BERT Emotions
    sbarfig1 = px.bar(dfff1,
                      x="PofPlay",
                      y="PercentageOfDialogues",
                      color="BERT_Emotion",
                      labels={
                          "BERT_Emotion": "BERT Emotion",
                          "PofPlay": "Percentage of Play",
                          "PercentageOfDialogues": "% of BERT Emotion"
                      },
                      hover_name='PofPlay',
                      hover_data={
                          "PofPlay": False,
                          "PercentageOfDialogues": ':.2f'
                      },
                      color_discrete_map=BERT_Emotions,
                      category_orders=Emotion_Order
                      # text=dfff1['BERT_Emotion']
                      # text=df['PercentageOfDialogues'].apply(lambda x: '{0:1.2f}%'.format(x))
                      )

    sbarfig1.update_layout(
        title='<b>Distribution of Emotions in Author(' + option_slctd1 + ')</b>',
        title_x=0.5,
        font_size=12,
        font_family='Rockwell',
        margin=dict(l=0, r=0, b=0),
        hoverlabel=dict(
            # bgcolor="white",
            font_size=12,
            font_family="Rockwell"),
        legend_title_text='Emotions',
        autotypenumbers="strict",
        hoverlabel_align='right',
        template="ggplot2"
    )

    print('Author2: ', option_slctd2)
    container2 = "The Author chosen by user was: {}".format(option_slctd2)

    dff2 = data.copy()

    authordf2 = dff2.loc[dff2['AuthorName'] == option_slctd2]
    playDistribution2 = np.array_split(authordf2, 10)

    tempauthordf2 = []
    for i, part in enumerate(playDistribution2):
        part['PofPlay'] = (i + 1) * 10
        part['PofPlay'] = part['PofPlay'].apply(percentagelabel)
        tempauthordf2.append(part)
    tempauthordf2 = pd.concat(tempauthordf2)

    authordf2 = tempauthordf2

    # Get all plays from each author
    dfff2 = (authordf2.groupby(['PofPlay', 'BERT_Emotion']).size()).reset_index()
    dfff2.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    dfff2 = dfff2.groupby(['PofPlay', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    dfff2['PercentageOfDialogues'] = dfff2.groupby(level=0).apply(percentage)
    dfff2 = dfff2.reset_index()

    # Plotly Express
    # Stacked Bar plot with Author's play vs. BERT Emotions
    sbarfig2 = px.bar(dfff2,
                      x="PofPlay",
                      y="PercentageOfDialogues",
                      color="BERT_Emotion",
                      labels={
                          "BERT_Emotion": "BERT Emotion",
                          "PofPlay": "Percentage of Play",
                          "PercentageOfDialogues": "% of BERT Emotion"
                      },
                      hover_name='PofPlay',
                      hover_data={
                          "PofPlay": False,
                          "PercentageOfDialogues": ':.2f'
                      },
                      color_discrete_map=BERT_Emotions,
                      category_orders=Emotion_Order
                      # text=dfff2['BERT_Emotion']
                      # text=df['PercentageOfDialogues'].apply(lambda x: '{0:1.2f}%'.format(x))
                      )

    sbarfig2.update_layout(
        title='<b>Distribution of Emotions in Author(' + option_slctd2 + ')</b>',
        title_x=0.5,
        font_size=12,
        font_family='Rockwell',
        margin=dict(l=0, r=0, b=0),
        hoverlabel=dict(
            # bgcolor="white",
            font_size=12,
            font_family="Rockwell"),
        legend_title_text='Emotions',
        autotypenumbers="strict",
        hoverlabel_align='right',
        template="ggplot2",
    )

    return container1, sbarfig1, container2, sbarfig2
