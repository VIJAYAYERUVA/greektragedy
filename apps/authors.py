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

authors = sorted(data['AuthorName'].value_counts().index.tolist())

layout = dbc.Container([
    dbc.Row(id='title',
            children=[
                dbc.Col([
                    html.H2("Explore the Authors", className='text-center font-weight-bold ml-4 mr-4 mt-4 mb-4')
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12,
                )
            ],
            justify='center',
            align='center',
            # className='mb-4'
            ),
    dbc.Row(id='authors_count',
            children=[
                dbc.Col([
                    dcc.Graph(id='authors_dcount', figure={}, config=helper_methods.config)
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12,
                )
            ],
            justify='center',
            align='center',
            className='mb-4'
            ),
    dbc.Row(id='authors_set',
            children=[
                dbc.Col([
                    dcc.Graph(id='authors_vader', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
                dbc.Col([
                    dcc.Graph(id='authors_bert', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
                dbc.Col([
                    dcc.Graph(id='authors_topic', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
            ],
            justify='center',
            align='center',
            className='mb-4',
            ),
    dbc.Row(id='authors_set_play',
            children=[
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author to check'),
                        html.Strong(' Sentiment '),
                        html.Label('in each play')]
                    ),
                    dcc.Dropdown(id="author_s_play",
                                 options=[{'label': a, 'value': a} for a in authors],
                                 multi=False,
                                 value='Aeschylus'
                                 ),
                    html.Div(id='container_s_play', children=[]),
                    dcc.Graph(id='authors_vader_play', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author to check'),
                        html.Strong(' Emotions '),
                        html.Label('in each play')]
                    ),
                    dcc.Dropdown(id="author_e_play",
                                 options=[{'label': a, 'value': a} for a in authors],
                                 multi=False,
                                 value='Aeschylus'
                                 ),
                    html.Div(id='container_e_play', children=[]),
                    dcc.Graph(id='authors_bert_play', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author to check'),
                        html.Strong(' Topics '),
                        html.Label('in each play')]
                    ),
                    dcc.Dropdown(id="author_t_play",
                                 options=[{'label': a, 'value': a} for a in authors],
                                 multi=False,
                                 value='Aeschylus'
                                 ),
                    html.Div(id='container_t_play', children=[]),
                    dcc.Graph(id='authors_topic_play', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
            ],
            justify='center',
            align='center',
            className='mb-4',
            ),
    dbc.Row(id='authors_set_timeline',
            children=[
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author to check'),
                        html.Strong(' Sentiment '),
                        html.Label('along the narrative')]
                    ),
                    dcc.Dropdown(id="author_s_timeline",
                                 options=[{'label': a, 'value': a} for a in authors],
                                 multi=False,
                                 value='Aeschylus'
                                 ),
                    html.Div(id='container_s_timeline', children=[]),
                    dcc.Graph(id='authors_vader_timeline', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author to check'),
                        html.Strong(' Emotions '),
                        html.Label('along the narrative')]
                    ),
                    dcc.Dropdown(id="author_e_timeline",
                                 options=[{'label': a, 'value': a} for a in authors],
                                 multi=False,
                                 value='Aeschylus'
                                 ),
                    html.Div(id='container_e_timeline', children=[]),
                    dcc.Graph(id='authors_bert_timeline', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author to check'),
                        html.Strong(' Topics '),
                        html.Label('along the narrative')]
                    ),
                    dcc.Dropdown(id="author_t_timeline",
                                 options=[{'label': a, 'value': a} for a in authors],
                                 multi=False,
                                 value='Aeschylus'
                                 ),
                    html.Div(id='container_t_timeline', children=[]),
                    dcc.Graph(id='authors_topic_timeline', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
            ],
            justify='center',
            align='center',
            className='mb-4',
            ),
    dbc.Row(id='authors_characters_gcd',
            children=[
                dbc.Col([
                    dcc.Graph(id='authors_gcd_count', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=6, xl=6
                ),
                dbc.Col([
                    dcc.Graph(id='authors_gcd_s', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=6, xl=6
                ),
            ],
            justify='center',
            align='center',
            className='mb-4',
            ),

],
    fluid=True
)


@app.callback(
    Output(component_id='authors_dcount', component_property='figure'),
    [Input(component_id='authors_count', component_property='value')]
)
def update_row_2(authors_count):
    # fig1 creation
    dff1 = data.copy()
    df1 = (dff1.groupby(['AuthorName', 'PlayName', 'CharacterName', 'BERT_Emotion']).size()).reset_index()
    df1.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    fig1 = px.treemap(df1,
                      path=[px.Constant("Three Authors"), 'AuthorName', 'PlayName', 'CharacterName', 'BERT_Emotion'],
                      values='NoOfDialogues',
                      color='BERT_Emotion',
                      color_discrete_map={
                          '(?)': 'lightgrey',
                          'anger': '#b44a1c',
                          'fear': '#ed9619',
                          'joy': '#1c9674',
                          'neutral': '#48596e',
                          'sadness': '#35afcf',
                      },
                      labels=helper_methods.labels,
                      maxdepth=3,
                      )
    fig1.update_layout(
        title='<b>Total #dialogues from three authors including Plays, Characters</b><br />'
              'Click on a tile (Author/Play/Character) to expand and see emotions.',
    )
    fig1.update_layout(helper_methods.update_layout1)

    return fig1


@app.callback([Output(component_id='authors_vader', component_property='figure'),
               Output(component_id='authors_bert', component_property='figure'),
               Output(component_id='authors_topic', component_property='figure')],
              [Input(component_id='authors_set', component_property='value')]
              )
def update_row_3(authors_set):
    # fig2 creation
    dff2 = data.copy()

    df2 = (dff2.groupby(['AuthorName', 'VADER_Label']).size()).reset_index()
    df2.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df2 = df2.groupby(['AuthorName', 'VADER_Label']).agg({'NoOfDialogues': 'sum'})
    df2['PercentageOfDialogues'] = df2.groupby(level=0).apply(helper_methods.percentage)
    df2 = df2.reset_index()

    fig2 = px.bar(df2,
                  x="AuthorName",
                  y="PercentageOfDialogues",
                  color="VADER_Label",
                  labels=helper_methods.labels,
                  hover_name='AuthorName',
                  hover_data={
                      "AuthorName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.vader_color,
                  category_orders=helper_methods.vader_order,
                  # text=df['VADER_Label']
                  text=df2['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig2.update_xaxes(title_text="")
    fig2.update_layout(
        title='<b>Distribution of Sentiments in Authors</b>',
        legend_title_text='Sentiment',
    )
    fig2.update_layout(helper_methods.update_layout1)

    # fig3 creation
    dff3 = data.copy()

    df3 = (dff3.groupby(['AuthorName', 'BERT_Emotion']).size()).reset_index()
    df3.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df3 = df3.groupby(['AuthorName', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    df3['PercentageOfDialogues'] = df3.groupby(level=0).apply(helper_methods.percentage)
    df3 = df3.reset_index()

    fig3 = px.bar(df3,
                  x="AuthorName",
                  y="PercentageOfDialogues",
                  color="BERT_Emotion",
                  labels=helper_methods.labels,
                  hover_name='AuthorName',
                  hover_data={
                      "AuthorName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.bert_color,
                  category_orders=helper_methods.bert_order,
                  # text=df['BERT_Emotion']
                  text=df3['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig3.update_xaxes(title_text="")
    fig3.update_layout(
        title='<b>Distribution of Emotions in Authors</b>',
        legend_title_text='Emotions',
    )
    fig3.update_layout(helper_methods.update_layout1)

    # fig4 creation
    dff4 = data.copy()

    df4 = (dff4.groupby(['AuthorName', 'Dominant_Topic_1']).size()).reset_index()
    df4.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df4 = df4.groupby(['AuthorName', 'Dominant_Topic_1']).agg({'NoOfDialogues': 'sum'})
    df4['PercentageOfDialogues'] = df4.groupby(level=0).apply(helper_methods.percentage)
    df4 = df4.reset_index()

    fig4 = px.bar(df4,
                  x="AuthorName",
                  y="PercentageOfDialogues",
                  color="Dominant_Topic_1",
                  labels=helper_methods.labels,
                  hover_name='AuthorName',
                  hover_data={
                      "AuthorName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.topic_color,
                  category_orders=helper_methods.topic_order,
                  # text=df['BERT_Emotion']
                  text=df4['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig4.update_xaxes(title_text="")
    fig4.update_traces(cliponaxis=False)
    fig4.update_layout(
        title='<b>Distribution of Topics in Authors</b>',
        legend_title_text='Emotions',
    )
    fig4.update_layout(helper_methods.update_layout1)

    return fig2, fig3, fig4


@app.callback(
    [Output(component_id='container_s_play', component_property='children'),
     Output(component_id='authors_vader_play', component_property='figure'),
     Output(component_id='container_e_play', component_property='children'),
     Output(component_id='authors_bert_play', component_property='figure'),
     Output(component_id='container_t_play', component_property='children'),
     Output(component_id='authors_topic_play', component_property='figure')],
    [Input(component_id='author_s_play', component_property='value'),
     Input(component_id='author_e_play', component_property='value'),
     Input(component_id='author_t_play', component_property='value')]
)
def update_row_4(author_s_play, author_e_play, author_t_play):
    # fig5 creation
    # print('Author: ', author_s_play)
    container_s_play = "The Author selected by user was: {}".format(author_s_play)

    dff5 = data.copy()

    authordf_s_play = dff5.loc[dff5['AuthorName'] == author_s_play]

    df5 = (authordf_s_play.groupby(['PlayName', 'VADER_Label']).size()).reset_index()
    df5.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df5 = df5.groupby(['PlayName', 'VADER_Label']).agg({'NoOfDialogues': 'sum'})
    df5['PercentageOfDialogues'] = df5.groupby(level=0).apply(helper_methods.percentage)
    df5 = df5.reset_index()

    # Stacked Bar plot with Author's play vs. VADER Sentiment
    fig5 = px.bar(df5,
                  x="PlayName",
                  y="PercentageOfDialogues",
                  color="VADER_Label",
                  labels=helper_methods.labels,
                  hover_name='PlayName',
                  hover_data={
                      "PlayName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.vader_color,
                  category_orders=helper_methods.vader_order,
                  # text=df5['VADER_Label']
                  # text=df5['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig5.update_xaxes(title_text="")
    fig5.update_traces(cliponaxis=False)
    fig5.update_layout(
        title='<b>Distribution of Sentiment in Author(' + author_s_play + ')</b>',
        legend_title_text='Sentiment',
    )
    fig5.update_layout(helper_methods.update_layout2)

    # fig6 creation
    # print('Author: ', author_e_play)
    container_e_play = "The Author selected by user was: {}".format(author_e_play)

    dff6 = data.copy()

    authordf_e_play = dff6.loc[dff6['AuthorName'] == author_e_play]

    df6 = (authordf_e_play.groupby(['PlayName', 'BERT_Emotion']).size()).reset_index()
    df6.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df6 = df6.groupby(['PlayName', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    df6['PercentageOfDialogues'] = df6.groupby(level=0).apply(helper_methods.percentage)
    df6 = df6.reset_index()

    # Stacked Bar plot with Author's play vs. BERT Emotion
    fig6 = px.bar(df6,
                  x="PlayName",
                  y="PercentageOfDialogues",
                  color="BERT_Emotion",
                  labels=helper_methods.labels,
                  hover_name='PlayName',
                  hover_data={
                      "PlayName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.bert_color,
                  category_orders=helper_methods.bert_order,
                  # text=df6['BERT_Emotion']
                  # text=df6['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig6.update_xaxes(title_text="")
    fig6.update_traces(cliponaxis=False)
    fig6.update_layout(
        title='<b>Distribution of Emotions in Author(' + author_e_play + ')</b>',
        legend_title_text='Emotions',
    )
    fig6.update_layout(helper_methods.update_layout2)

    # fig7 creation
    # print('Author: ', author_t_play)
    container_t_play = "The Author selected by user was: {}".format(author_t_play)

    dff7 = data.copy()

    authordf_t_play = dff7.loc[dff7['AuthorName'] == author_t_play]

    df7 = (authordf_t_play.groupby(['PlayName', 'Dominant_Topic_1']).size()).reset_index()
    df7.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df7 = df7.groupby(['PlayName', 'Dominant_Topic_1']).agg({'NoOfDialogues': 'sum'})
    df7['PercentageOfDialogues'] = df7.groupby(level=0).apply(helper_methods.percentage)
    df7 = df7.reset_index()

    # Stacked Bar plot with Author's play vs. Dominant Topic
    fig7 = px.bar(df7,
                  x="PlayName",
                  y="PercentageOfDialogues",
                  color="Dominant_Topic_1",
                  labels=helper_methods.labels,
                  hover_name='PlayName',
                  hover_data={
                      "PlayName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.topic_color,
                  category_orders=helper_methods.topic_order,
                  # text=df7['Dominant_Topic_1']
                  # text=df7['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig7.update_xaxes(title_text="")
    fig7.update_traces(cliponaxis=False)
    fig7.update_layout(
        title='<b>Distribution of Topics in Author(' + author_t_play + ')</b>',
        legend_title_text='Topics',
    )
    fig7.update_layout(helper_methods.update_layout2)

    return container_s_play, fig5, container_e_play, fig6, container_t_play, fig7


@app.callback(
    [Output(component_id='container_s_timeline', component_property='children'),
     Output(component_id='authors_vader_timeline', component_property='figure'),
     Output(component_id='container_e_timeline', component_property='children'),
     Output(component_id='authors_bert_timeline', component_property='figure'),
     Output(component_id='container_t_timeline', component_property='children'),
     Output(component_id='authors_topic_timeline', component_property='figure')],
    [Input(component_id='author_s_timeline', component_property='value'),
     Input(component_id='author_e_timeline', component_property='value'),
     Input(component_id='author_t_timeline', component_property='value')]
)
def update_row_5(author_s_timeline, author_e_timeline, author_t_timeline):
    # fig8 creation
    # print('Author: ', author_s_timeline)
    container_s_timeline = "The Author selected by user was: {}".format(author_s_timeline)

    dff8 = data.copy()

    authordf_s_timeline = dff8.loc[dff8['AuthorName'] == author_s_timeline]
    playDistribution_s_timeline = np.array_split(authordf_s_timeline, 10)

    tempdf_s_timeline = []
    for i, part in enumerate(playDistribution_s_timeline):
        part['PofPlay'] = (i + 1) * 10
        part['PofPlay'] = part['PofPlay'].apply(helper_methods.percentagelabel)
        tempdf_s_timeline.append(part)
    tempdf_s_timeline = pd.concat(tempdf_s_timeline)

    authordf_s_timeline = tempdf_s_timeline

    # Get all plays from each author
    df8 = (authordf_s_timeline.groupby(['PofPlay', 'VADER_Label']).size()).reset_index()
    df8.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df8 = df8.groupby(['PofPlay', 'VADER_Label']).agg({'NoOfDialogues': 'sum'})
    df8['PercentageOfDialogues'] = df8.groupby(level=0).apply(helper_methods.percentage)
    df8 = df8.reset_index()

    # Stacked Bar plot with Author's play vs. VADER Sentiment
    fig8 = px.bar(df8,
                  x="PofPlay",
                  y="PercentageOfDialogues",
                  color="VADER_Label",
                  labels=helper_methods.labels,
                  hover_name='PofPlay',
                  hover_data={
                      "PofPlay": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.vader_color,
                  category_orders=helper_methods.vader_order
                  # text=df8['VADER_Label']
                  # text=df8['PercentageOfDialogues'].apply(lambda x: '{0:1.2f}%'.format(x))
                  )

    fig8.update_xaxes(title_text="")
    fig8.update_traces(cliponaxis=False)
    fig8.update_layout(
        title='<b>Distribution of Sentiment in Author(' + author_s_timeline + ')</b>',
        legend_title_text='Sentiment',
    )
    fig8.update_layout(helper_methods.update_layout2)

    # fig9 creation
    # print('Author: ', author_e_timeline)
    container_e_timeline = "The Author selected by user was: {}".format(author_e_timeline)

    dff9 = data.copy()

    authordf_e_timeline = dff9.loc[dff9['AuthorName'] == author_e_timeline]
    playDistribution_e_timeline = np.array_split(authordf_e_timeline, 10)

    tempdf_e_timeline = []
    for i, part in enumerate(playDistribution_e_timeline):
        part['PofPlay'] = (i + 1) * 10
        part['PofPlay'] = part['PofPlay'].apply(helper_methods.percentagelabel)
        tempdf_e_timeline.append(part)
    tempdf_e_timeline = pd.concat(tempdf_e_timeline)

    authordf_e_timeline = tempdf_e_timeline

    # Get all plays from each author
    df9 = (authordf_e_timeline.groupby(['PofPlay', 'BERT_Emotion']).size()).reset_index()
    df9.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df9 = df9.groupby(['PofPlay', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    df9['PercentageOfDialogues'] = df9.groupby(level=0).apply(helper_methods.percentage)
    df9 = df9.reset_index()

    # Stacked Bar plot with Author's play vs. BERT Emotion
    fig9 = px.bar(df9,
                  x="PofPlay",
                  y="PercentageOfDialogues",
                  color="BERT_Emotion",
                  labels=helper_methods.labels,
                  hover_name='PofPlay',
                  hover_data={
                      "PofPlay": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.bert_color,
                  category_orders=helper_methods.bert_order
                  # text=df9['BERT_Emotion']
                  # text=df9['PercentageOfDialogues'].apply(lambda x: '{0:1.2f}%'.format(x))
                  )

    fig9.update_xaxes(title_text="")
    fig9.update_traces(cliponaxis=False)
    fig9.update_layout(
        title='<b>Distribution of Emotions in Author(' + author_e_timeline + ')</b>',
        legend_title_text='Emotions',
    )
    fig9.update_layout(helper_methods.update_layout2)

    # fig10 creation
    # print('Author: ', author_t_timeline)
    container_t_timeline = "The Author selected by user was: {}".format(author_t_timeline)

    dff10 = data.copy()

    authordf_t_timeline = dff10.loc[dff10['AuthorName'] == author_t_timeline]
    playDistribution_t_timeline = np.array_split(authordf_t_timeline, 10)

    tempdf_t_timeline = []
    for i, part in enumerate(playDistribution_t_timeline):
        part['PofPlay'] = (i + 1) * 10
        part['PofPlay'] = part['PofPlay'].apply(helper_methods.percentagelabel)
        tempdf_t_timeline.append(part)
    tempdf_t_timeline = pd.concat(tempdf_t_timeline)

    authordf_t_timeline = tempdf_t_timeline

    # Get all plays from each author
    df10 = (authordf_t_timeline.groupby(['PofPlay', 'Dominant_Topic_1']).size()).reset_index()
    df10.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df10 = df10.groupby(['PofPlay', 'Dominant_Topic_1']).agg({'NoOfDialogues': 'sum'})
    df10['PercentageOfDialogues'] = df10.groupby(level=0).apply(helper_methods.percentage)
    df10 = df10.reset_index()

    # Stacked Bar plot with Author's play vs. Dominant Topic
    fig10 = px.bar(df10,
                   x="PofPlay",
                   y="PercentageOfDialogues",
                   color="Dominant_Topic_1",
                   labels=helper_methods.labels,
                   hover_name='PofPlay',
                   hover_data={
                       "PofPlay": False,
                       "PercentageOfDialogues": ':.2f'
                   },
                   color_discrete_map=helper_methods.topic_color,
                   category_orders=helper_methods.topic_order
                   # text=df10['VADER_Label']
                   # text=df10['PercentageOfDialogues'].apply(lambda x: '{0:1.2f}%'.format(x))
                   )

    fig10.update_xaxes(title_text="")
    fig10.update_traces(cliponaxis=False)
    fig10.update_layout(
        title='<b>Distribution of Topics in Author(' + author_t_timeline + ')</b>',
        legend_title_text='Topics',
    )
    fig10.update_layout(helper_methods.update_layout2)

    return container_s_timeline, fig8, container_e_timeline, fig9, container_t_timeline, fig10


@app.callback(
    [Output(component_id='authors_gcd_count', component_property='figure'),
     Output(component_id='authors_gcd_s', component_property='figure')],
    [Input(component_id='authors_characters_gcd', component_property='value')]
)
def update_row_6(authors_characters_gcd):
    # fig11 creation
    # Initialize figure with subplots
    fig11 = make_subplots(
        rows=1, cols=3, subplot_titles=("Gender", "Class", "Divinity")
    )
    # Add traces
    fig11.append_trace(
        go.Bar(
            x=authors,
            y=[18, 74, 15],
            marker=dict(
                color='#d091b5',
            ),
            name='Female',
            text=[18, 74, 15],
            textposition='auto'
        ),
        row=1, col=1)

    fig11.append_trace(
        go.Bar(
            x=authors,
            y=[30, 111, 43],
            marker=dict(
                color='#aa5986',
            ),
            name='Male',
            text=[30, 111, 43],
            textposition='auto'
        ),
        row=1, col=1)

    fig11.append_trace(
        go.Bar(
            x=authors,
            y=[15, 77, 23],
            marker=dict(
                color='#fbd485',
            ),
            name='Lower',
            text=[15, 77, 23],
            textposition='auto'
        ),
        row=1, col=2)

    fig11.append_trace(
        go.Bar(
            x=authors,
            y=[33, 108, 35],
            marker=dict(
                color='#f79647',
            ),
            name='Upper',
            text=[33, 108, 35],
            textposition='auto'
        ),
        row=1, col=2)

    fig11.append_trace(
        go.Bar(
            x=authors,
            y=[38, 163, 55],
            marker=dict(
                color='#2988ad',
            ),
            name='Mortal',
            text=[38, 163, 55],
            textposition='auto'
        ),
        row=1, col=3)

    fig11.append_trace(
        go.Bar(
            x=authors,
            y=[10, 22, 3],
            marker=dict(
                color='#003c78',
            ),
            name='Immortal',
            text=[10, 22, 3],
            textposition='auto'
        ),
        row=1, col=3)

    fig11.update_yaxes(title_text="#Characters", row=1, col=1)
    fig11.update_layout(
        title='<b>Total #characters from three authors including Gender, Class, Divinity</b>',
    )
    fig11.update_layout(helper_methods.update_layout3)

    # fig12 creation
    # Initialize figure with subplots
    fig12 = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=("Gender", "Class", "Divinity")
    )

    # Gender - Female
    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[28, 21, 14],
            marker=dict(
                color='#d091b5',
                pattern_shape="x",
            ),
            name='Female-Positive',
            text=[28, 21, 14],
            textposition='auto',
            offsetgroup=0
        ),
        row=1, col=1)

    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[25, 18, 10],
            marker=dict(
                color='#d091b5',
            ),
            name='Female-Negative',
            text=[25, 18, 10],
            textposition='auto',
            offsetgroup=0,
            base=[28, 21, 14]
        ),
        row=1, col=1)

    # Gender - Male
    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[27, 39, 47],
            marker=dict(
                color='#aa5986',
                pattern_shape="x",
            ),
            name='Male-Positive',
            text=[27, 39, 47],
            textposition='auto',
            offsetgroup=1
        ),
        row=1, col=1)

    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[21, 22, 29],
            marker=dict(
                color='#aa5986',
            ),
            name='Male-Negative',
            text=[21, 22, 29],
            textposition='auto',
            offsetgroup=1,
            base=[27, 39, 47]
        ),
        row=1, col=1)

    # Class - Lower
    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[15, 13, 13],
            marker=dict(
                color='#fbd485',
                pattern_shape="x",
            ),
            name='Lower-Positive',
            text=[15, 13, 13],
            textposition='auto',
            offsetgroup=0
        ),
        row=1, col=2)

    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[15, 11, 10],
            marker=dict(
                color='#fbd485',
            ),
            name='Lower-Negative',
            text=[15, 11, 10],
            textposition='auto',
            offsetgroup=0,
            base=[15, 13, 13]
        ),
        row=1, col=2)

    # Class - Upper
    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[40, 47, 48],
            marker=dict(
                color='#f79647',
                pattern_shape="x",
            ),
            name='Upper-Positive',
            text=[40, 47, 48],
            textposition='auto',
            offsetgroup=1
        ),
        row=1, col=2)

    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[30, 29, 29],
            marker=dict(
                color='#f79647',
            ),
            name='Upper-Negative',
            text=[30, 29, 29],
            textposition='auto',
            offsetgroup=1,
            base=[40, 47, 48]
        ),
        row=1, col=2)

    # Divinity - Mortal
    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[39, 54, 59],
            marker=dict(
                color='#2988ad',
                pattern_shape='x',
            ),
            name='Mortal-Positive',
            text=[39, 54, 59],
            textposition='auto',
            offsetgroup=0
        ),
        row=1, col=3)

    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[33, 36, 38],
            marker=dict(
                color='#2988ad',
            ),
            name='Mortal-Negative',
            text=[33, 36, 38],
            textposition='auto',
            offsetgroup=0,
            base=[39, 54, 59]
        ),
        row=1, col=3)

    # Divinity - Immortal
    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[15, 6, 2],
            marker=dict(
                color='#003c78',
                pattern_shape='x',
            ),
            name='Immortal-Positive',
            text=[15, 6, 2],
            textposition='auto',
            offsetgroup=1,
        ),
        row=1, col=3)

    fig12.append_trace(
        go.Bar(
            x=authors,
            y=[13, 4, 1],
            marker=dict(
                color='#003c78',
            ),
            name='Immortal-Negative',
            text=[13, 4, 1],
            textposition='auto',
            offsetgroup=1,
            base=[15, 6, 2]
        ),
        row=1, col=3)

    fig12.update_yaxes(title_text="% of Dialogues", row=1, col=1)
    fig12.update_layout(
        title='<b>% of Dialogues from three authors including including <br />'
              'Gender, Class, Divinity and "Sentiment"</b>',
    )
    fig12.update_layout(helper_methods.update_layout3)
    return fig11, fig12

