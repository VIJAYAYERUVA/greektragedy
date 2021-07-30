import pathlib

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_cytoscape as cyto
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from textwrap3 import wrap

from app import app
from apps import helper_methods
from assets import stylesheet, legend_stylesheet

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()


# function to create Label
def label(char, g, c, d, be):
    # cs = 'Charactername: ' + char + '\nGender: ' + g + '\nClass: ' + c + '\nDivinity: ' + d + '\nBERT_Emotion: ' + be
    cs = char + '\nEmotion: ' + be
    s = char + '; ' + g + '; ' + c + '; ' + d + '; ' + be
    return cs


# ---------- Import and clean data (importing csv into pandas)
data = pd.read_csv(DATA_PATH.joinpath("Authors.csv"))

# Read Nodes data
nodes = pd.read_csv(DATA_PATH.joinpath("Authors_N.csv"))
nodes['Label'] = nodes.apply(lambda n:
                             label(n.CharacterName, n.Gender, n.Class, n.Divinity, n.BERT_Emotion),
                             axis=1)
nodes.columns = map(str.lower, nodes.columns)

# Read Edges data
edges = pd.read_csv(DATA_PATH.joinpath("Authors_E.csv"))
edges.columns = map(str.lower, edges.columns)

authors = sorted(nodes['authorname'].value_counts().index.tolist())
plays = sorted(nodes['playname'].value_counts().index.tolist())

my_elements = helper_methods.my_elements
legend_elements = helper_methods.legend_elements

play_list = {
    'Aeschylus': ['Agamemnon', 'Eumenides', 'LibationBearers', 'Persians', 'PrometheusBound', 'SevenAgainst',
                  'SuppliantWomen'],
    'Euripides': ['Alcestis', 'Andromache', 'Bacchae', 'Cyclops', 'Electra', 'Hecuba', 'Helen', 'Heracleidae',
                  'Heracles', 'Hippolytus', 'Ion', 'IphigeniainAulis', 'IphigeniainTauris', 'Medea', 'Orestes',
                  'Phoenissae', 'Rhesus', 'TheSuppliants', 'TheTrojanWomen'],
    'Sophocles': ['Ajax', 'Antigone', 'Electra', 'OedipusTyrannus', 'OedipusatColonus', 'Philoctetes', 'Trachiniae']
}

layout = dbc.Container([
    dbc.Row(id='title',
            children=[
                dbc.Col([
                    html.H1("Explore the Plays", className='text-center font-weight-bold ml-4 mr-4 mt-4 mb-4')
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12,
                )
            ],
            justify='center',
            align='center',
            className='mb-4'
            ),
    dbc.Row(id='plays_set_character',
            children=[
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author and Play to check'),
                        html.Strong(' Sentiment '),
                        html.Label('in each character')]
                    ),
                    dcc.Dropdown(id="author_s_character",
                                 options=[{'label': a, 'value': a} for a in play_list.keys()],
                                 multi=False,
                                 value='Aeschylus',
                                 ),
                    dcc.Dropdown(id="play_s_character",
                                 multi=False,
                                 ),
                    html.Div(id='container_s_character', children=[]),
                    dcc.Graph(id='plays_vader_character', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author and Play to check'),
                        html.Strong(' Emotions '),
                        html.Label('in each character')]
                    ),
                    dcc.Dropdown(id="author_e_character",
                                 options=[{'label': a, 'value': a} for a in play_list.keys()],
                                 multi=False,
                                 value='Aeschylus'
                                 ),
                    dcc.Dropdown(id="play_e_character",
                                 multi=False,
                                 ),
                    html.Div(id='container_e_character', children=[]),
                    dcc.Graph(id='plays_bert_character', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
                dbc.Col([
                    html.Label(children=[
                        html.Label('Select Author and Play to check'),
                        html.Strong(' Topics '),
                        html.Label('in each character')]
                    ),
                    dcc.Dropdown(id="author_t_character",
                                 options=[{'label': a, 'value': a} for a in play_list.keys()],
                                 multi=False,
                                 value='Aeschylus'
                                 ),
                    dcc.Dropdown(id="play_t_character",
                                 multi=False,
                                 ),
                    html.Div(id='container_t_character', children=[]),
                    dcc.Graph(id='plays_topic_character', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=4, xl=4
                ),
            ],
            justify='center',
            align='center',
            className='mb-4',
            ),
    dbc.Row(id='network_title',
            children=[
                dbc.Col([
                    html.H3("Play's network from Greek Tragedy literature",
                            className='text-center font-weight-bold ml-4 mr-4 mt-4 mb-4')
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12,
                )
            ],
            justify='center',
            align='center',
            className='mb-4'
            ),
    dbc.Row(id='network_dropdown',
            children=[
                dbc.Col([
                    html.Div([
                        html.Div([
                            html.Label('Select Author'),
                            dcc.Dropdown(id="author_network",
                                         options=[{'label': a, 'value': a} for a in authors],
                                         multi=False,
                                         value='Aeschylus',
                                         style={'width': "100%"}
                                         ),
                            html.Div(id='container_a_network', children=[])
                        ],
                            style={'width': '49%', 'display': 'inline-block'}),

                        html.Div([
                            html.Label('Select Play'),
                            dcc.Dropdown(id="play_network",
                                         options=[{'label': p, 'value': p} for p in plays],
                                         multi=False,
                                         value='Agamemnon',
                                         style={'width': "100%"}
                                         ),
                            html.Div(id='container_p_network', children=[])
                        ],
                            style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
                    ]),
                ])
            ],
            justify='center',
            align='center',
            ),
    dbc.Row(id='network_content',
            children=[
                dbc.Col([
                    cyto.Cytoscape(
                        id='characters',
                        minZoom=0.5,
                        maxZoom=1,
                        layout={'name': 'circle',  # grid
                                'animate': True},
                        elements=my_elements,
                        style={'width': '90vw', 'height': '70vh'},
                        stylesheet=stylesheet.stylesheet
                    )

                ],
                    xs=10, sm=10, md=10, lg=10, xl=10
                ),
                dbc.Col([
                    cyto.Cytoscape(
                        id='legends',
                        minZoom=1,
                        maxZoom=1,
                        layout={'name': 'grid',
                                'rows': 11,
                                'animate': True},
                        elements=legend_elements,
                        style={'height': '70vh'},
                        stylesheet=legend_stylesheet.stylesheet
                    )
                ],
                    xs=2, sm=2, md=2, lg=2, xl=2
                ),
            ],
            justify='center',
            align='center',
            className='mb-4',
            ),
    dbc.Row(id='character_s',
            children=[
                dbc.Col([
                    dcc.Graph(id='play_vader', figure={}),
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12)
            ],
            justify='center',
            align='center',
            className='mb-4',
            ),
], fluid=True)


# Dropdown for sentiment in characters
@app.callback(
    dash.dependencies.Output('play_s_character', 'options'),
    [dash.dependencies.Input('author_s_character', 'value')])
def set_play_options_s_c(selected_author):
    return [{'label': i, 'value': i} for i in play_list[selected_author]]


@app.callback(
    dash.dependencies.Output('play_s_character', 'value'),
    [dash.dependencies.Input('play_s_character', 'options')])
def set_play_values_s_c(available_options):
    return available_options[0]['value']


# Dropdown for emotions in characters
@app.callback(
    dash.dependencies.Output('play_e_character', 'options'),
    [dash.dependencies.Input('author_e_character', 'value')])
def set_play_options_e_c(selected_author):
    return [{'label': i, 'value': i} for i in play_list[selected_author]]


@app.callback(
    dash.dependencies.Output('play_e_character', 'value'),
    [dash.dependencies.Input('play_e_character', 'options')])
def set_play_values_e_c(available_options):
    return available_options[0]['value']


# Dropdown for topics in characters
@app.callback(
    dash.dependencies.Output('play_t_character', 'options'),
    [dash.dependencies.Input('author_t_character', 'value')])
def set_play_options_t_c(selected_author):
    return [{'label': i, 'value': i} for i in play_list[selected_author]]


@app.callback(
    dash.dependencies.Output('play_t_character', 'value'),
    [dash.dependencies.Input('play_t_character', 'options')])
def set_play_values_t_c(available_options):
    return available_options[0]['value']


@app.callback(
    [Output(component_id='container_s_character', component_property='children'),
     Output(component_id='plays_vader_character', component_property='figure'),
     Output(component_id='container_e_character', component_property='children'),
     Output(component_id='plays_bert_character', component_property='figure'),
     Output(component_id='container_t_character', component_property='children'),
     Output(component_id='plays_topic_character', component_property='figure')],
    [Input(component_id='author_s_character', component_property='value'),
     Input(component_id='play_s_character', component_property='value'),
     Input(component_id='author_e_character', component_property='value'),
     Input(component_id='play_e_character', component_property='value'),
     Input(component_id='author_t_character', component_property='value'),
     Input(component_id='play_t_character', component_property='value')
     ]
)
def update_row_2(author_s_character, play_s_character, author_e_character, play_e_character, author_t_character,
                 play_t_character):
    # fig1 creation
    # print(f'Author: {author_s_character}, Play:{play_s_character}')
    container_s_character = f"The options selected by user was: {author_s_character}, {play_s_character}"

    dff1 = data.copy()

    authordf1 = dff1.loc[dff1['AuthorName'] == author_s_character]
    playdf1 = authordf1.loc[authordf1['PlayName'] == play_s_character]

    # Get all characters from each play
    df1 = (playdf1.groupby(['CharacterName', 'VADER_Label']).size()).reset_index()
    df1.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df1 = df1.groupby(['CharacterName', 'VADER_Label']).agg({'NoOfDialogues': 'sum'})
    df1['PercentageOfDialogues'] = df1.groupby(level=0).apply(helper_methods.percentage)
    df1 = df1.reset_index()

    # Stacked Bar plot with Play's character vs. VADER Sentiment
    fig1 = px.bar(df1,
                  x="CharacterName",
                  y="PercentageOfDialogues",
                  color="VADER_Label",
                  labels=helper_methods.labels,
                  hover_name='CharacterName',
                  hover_data={
                      "CharacterName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.vader_color,
                  category_orders=helper_methods.vader_order,
                  # text=df1['VADER_Label']
                  # text=df1['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig1.update_xaxes(title_text="")
    fig1.update_traces(cliponaxis=False)
    fig1.update_layout(
        title='<b>Distribution of Sentiments in <br />Author(' + author_s_character + ')->Play(' + play_s_character + ')</b>',
        legend_title_text='Sentiment',
    )
    fig1.update_layout(helper_methods.update_layout4)

    # fig2 creation
    # print(f'Author: {author_e_character}, Play:{play_e_character}')
    container_e_character = f"The options selected by user was: {author_e_character}, {play_e_character}"

    dff2 = data.copy()

    authordf2 = dff2.loc[dff2['AuthorName'] == author_e_character]
    playdf2 = authordf2.loc[authordf2['PlayName'] == play_e_character]

    # Get all characters from each play
    df2 = (playdf2.groupby(['CharacterName', 'BERT_Emotion']).size()).reset_index()
    df2.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df2 = df2.groupby(['CharacterName', 'BERT_Emotion']).agg({'NoOfDialogues': 'sum'})
    df2['PercentageOfDialogues'] = df2.groupby(level=0).apply(helper_methods.percentage)
    df2 = df2.reset_index()

    # Stacked Bar plot with Play's character vs. VADER Sentiment
    fig2 = px.bar(df2,
                  x="CharacterName",
                  y="PercentageOfDialogues",
                  color="BERT_Emotion",
                  labels=helper_methods.labels,
                  hover_name='CharacterName',
                  hover_data={
                      "CharacterName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.bert_color,
                  category_orders=helper_methods.bert_order,
                  # text=df2['BERT_Emotion']
                  # text=df2['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig2.update_xaxes(title_text="")
    fig2.update_traces(cliponaxis=False)
    fig2.update_layout(
        title='<b>Distribution of Emotions in <br />Author(' + author_e_character + ')->Play(' + play_e_character + ')</b>',
        legend_title_text='Emotions',
    )
    fig2.update_layout(helper_methods.update_layout4)

    # fig3 creation
    # print(f'Author: {author_t_character}, Play:{play_t_character}')
    container_t_character = f"The options selected by user was: {author_t_character}, {play_t_character}"

    dff3 = data.copy()

    authordf3 = dff3.loc[dff3['AuthorName'] == author_t_character]
    playdf3 = authordf3.loc[authordf3['PlayName'] == play_t_character]

    # Get all characters from each play
    df3 = (playdf3.groupby(['CharacterName', 'Dominant_Topic_1']).size()).reset_index()
    df3.rename(columns={0: 'NoOfDialogues'}, inplace=True)

    df3 = df3.groupby(['CharacterName', 'Dominant_Topic_1']).agg({'NoOfDialogues': 'sum'})
    df3['PercentageOfDialogues'] = df3.groupby(level=0).apply(helper_methods.percentage)
    df3 = df3.reset_index()

    # Stacked Bar plot with Play's character vs. VADER Sentiment
    fig3 = px.bar(df3,
                  x="CharacterName",
                  y="PercentageOfDialogues",
                  color="Dominant_Topic_1",
                  labels=helper_methods.labels,
                  hover_name='CharacterName',
                  hover_data={
                      "CharacterName": False,
                      "PercentageOfDialogues": ':.2f'
                  },
                  color_discrete_map=helper_methods.topic_color,
                  category_orders=helper_methods.topic_order,
                  # text=df3['Dominant_Topic_1']
                  # text=df3['PercentageOfDialogues'].apply(lambda z: '{0:1.2f}%'.format(z)),
                  )

    fig3.update_xaxes(title_text="")
    fig3.update_traces(cliponaxis=False)
    fig3.update_layout(
        title='<b>Distribution of Topics in'
              '<br />Author(' + author_e_character + ')->Play(' + play_e_character + ')</b>',
        legend_title_text='Topics',
    )
    fig3.update_layout(helper_methods.update_layout4)

    return container_s_character, fig1, container_e_character, fig2, container_t_character, fig3


# Dropdown for sentiment in timeline
@app.callback(
    dash.dependencies.Output('play_s_timeline', 'options'),
    [dash.dependencies.Input('author_s_timeline', 'value')])
def set_timeline_options_s_c(selected_author):
    return [{'label': i, 'value': i} for i in play_list[selected_author]]


@app.callback(
    dash.dependencies.Output('play_s_timeline', 'value'),
    [dash.dependencies.Input('play_s_timeline', 'options')])
def set_timeline_values_s_c(available_options):
    return available_options[0]['value']


# Dropdown for emotions in timeline
@app.callback(
    dash.dependencies.Output('play_e_timeline', 'options'),
    [dash.dependencies.Input('author_e_timeline', 'value')])
def set_timeline_options_e_c(selected_author):
    return [{'label': i, 'value': i} for i in play_list[selected_author]]


@app.callback(
    dash.dependencies.Output('play_e_timeline', 'value'),
    [dash.dependencies.Input('play_e_timeline', 'options')])
def set_timeline_values_e_c(available_options):
    return available_options[0]['value']


# Dropdown for topics in timeline
@app.callback(
    dash.dependencies.Output('play_t_timeline', 'options'),
    [dash.dependencies.Input('author_t_timeline', 'value')])
def set_timeline_options_t_c(selected_author):
    return [{'label': i, 'value': i} for i in play_list[selected_author]]


@app.callback(
    dash.dependencies.Output('play_t_timeline', 'value'),
    [dash.dependencies.Input('play_t_timeline', 'options')])
def set_timeline_values_t_c(available_options):
    return available_options[0]['value']


# Update network
@app.callback([Output("characters", "elements"),
               Output(component_id='container_a_network', component_property='children'),
               Output(component_id='container_p_network', component_property='children'), ],
              [Input(component_id='author_network', component_property='value'),
               Input(component_id='play_network', component_property='value')])
def update_network(author, play):
    container_a_network = "The Author selected by user was: {}".format(author)
    container_p_network = "The Play selected by user was: {}".format(play)
    filterNodes = nodes[(nodes['authorname'] == author) & (nodes['playname'] == play)]
    tempNodes = filterNodes[['id', 'label', 'gender', 'class', 'divinity', 'bert_emotion']]
    node2dic = tempNodes.to_dict('index')
    values = list(node2dic.values())
    finalnodes = [{'data': v, 'classes': 'bottom-right multiline-manual'} for v in values]

    filterEdges = edges[(edges['authorname'] == author) & (edges['playname'] == play)]
    tempEdges = filterEdges[['source', 'target', 'weight']]
    node2dic = tempEdges.to_dict('index')
    # keys = list(node2dic.keys())
    values = list(node2dic.values())
    finaledges = [{'data': v} for v in values]

    all_elements = finalnodes + finaledges
    return all_elements, container_a_network, container_p_network


@app.callback(
    Output(component_id='play_vader', component_property='figure'),
    [Input(component_id='author_network', component_property='value'),
     Input(component_id='play_network', component_property='value')])
def update_row_5(author, play):
    # fig7 creation
    dff7 = data.copy()
    dff7["Dialogue"] = dff7["Dialogue"].apply(lambda t: "<br>".join(wrap(t)))

    # print('\n Author: ', author)
    authordf7 = dff7.loc[dff7['AuthorName'] == author]

    playdf7 = authordf7.loc[authordf7['PlayName'] == play]
    playdf7.reset_index(drop=True, inplace=True)

    # Bar plot with VADER Sentiment vs Topics
    fig7 = px.bar(playdf7,
                  x="ParagraphNumber",
                  y="VADER_Score",
                  color="Dominant_Topic_1",
                  labels=helper_methods.labels,
                  hover_data={"CharacterName": True,
                              "Dialogue": True,
                              "BERT_Emotion": True,
                              "Dominant_Topic_1": True,
                              "Topic_Keywords_1": True,
                              # "TK_inDialogue": True
                              },
                  color_discrete_map=helper_methods.topic_color,
                  category_orders=helper_methods.topic_order,
                  title='<b>Author(' + author + ')->Play(' + play + '): ' + 'VADER Sentiment and topics in each '
                                                                            'dialogue</b>')
    fig7.update_layout(legend_title_text='Topics: ')
    fig7.update_layout(helper_methods.update_layout5)

    return fig7
