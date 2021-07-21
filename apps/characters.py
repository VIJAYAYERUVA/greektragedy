import pathlib

import dash_core_components as dcc
import dash_cytoscape as cyto
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input

from app import app
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

# Read Nodes data
nodes = pd.read_csv(DATA_PATH.joinpath("Authors_N.csv"))
nodes['Label'] = nodes.apply(lambda n:
                             label(n.CharacterName, n.Gender, n.Class, n.Divinity, n.BERT_Emotion),
                             axis=1)
nodes.columns = map(str.lower, nodes.columns)

# Read Edges data
edges = pd.read_csv(DATA_PATH.joinpath("Authors_E.csv"))
edges.columns = map(str.lower, edges.columns)

authors = nodes['authorname'].value_counts().index.tolist()
plays = nodes['playname'].value_counts().index.tolist()

my_elements = [
    # Nodes elements
    {'data': {'id': 44, 'label': 'A Danaid'}},
    {'data': {'id': 45, 'label': 'Chorus'}},
    {'data': {'id': 46, 'label': 'Danaus'}},
    {'data': {'id': 47, 'label': 'Herald'}},
    {'data': {'id': 48, 'label': 'King'}},
    # Edge elements
    {'data': {'source': 45, 'target': 46, 'weight': 1}},
    {'data': {'source': 45, 'target': 47, 'weight': 1}},
    {'data': {'source': 45, 'target': 48, 'weight': 2}},
    {'data': {'source': 46, 'target': 45, 'weight': 2}},
    {'data': {'source': 46, 'target': 48, 'weight': 1}},
    {'data': {'source': 47, 'target': 45, 'weight': 1}},
    {'data': {'source': 47, 'target': 48, 'weight': 1}},
    {'data': {'source': 48, 'target': 45, 'weight': 2}},
    {'data': {'source': 48, 'target': 46, 'weight': 1}},
    {'data': {'source': 48, 'target': 47, 'weight': 1}}
]

legend_elements = [
    # Nodes data
    {'data': {'id': 'male', 'label': 'Male'},
     'classes': 'gender-male center-right'},
    {'data': {'id': 'female', 'label': 'Female'},
     'classes': 'gender-female center-right'},
    {'data': {'id': 'upper', 'label': 'Upper'},
     'classes': 'class-upper center-right'},
    {'data': {'id': 'lower', 'label': 'Lower'},
     'classes': 'class-lower center-right'},
    {'data': {'id': 'immortal', 'label': 'Immortal'},
     'classes': 'divinity-immortal center-right'},
    {'data': {'id': 'mortal', 'label': 'Mortal'},
     'classes': 'divinity-mortal center-right'},
    {'data': {'id': 'anger', 'label': 'Anger'},
     'classes': 'emotion-anger center-right'},
    {'data': {'id': 'fear', 'label': 'Fear'},
     'classes': 'emotion-fear center-right'},
    {'data': {'id': 'joy', 'label': 'Joy'},
     'classes': 'emotion-joy center-right'},
    {'data': {'id': 'neutral', 'label': 'Neutral'},
     'classes': 'emotion-neutral center-right'},
    {'data': {'id': 'sadness', 'label': 'Sadness'},
     'classes': 'emotion-sadness center-right'}
]

layout = html.Div([
    html.H1("Data from Authors", style={'text-align': 'center'}),
    html.Div([

        html.Div([
            html.Label('Select Author'),
            dcc.Dropdown(id="slct_author",
                         options=[{'label': a, 'value': a} for a in sorted(authors)],
                         multi=False,
                         value='Aeschylus',
                         style={'width': "100%"}
                         ),
            html.Div(id='output_container1', children=[])
        ],
            style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            html.Label('Select Play'),
            dcc.Dropdown(id="slct_play",
                         options=[{'label': p, 'value': p} for p in sorted(plays)],
                         multi=False,
                         value='Agamemnon',
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
        html.Div([
            cyto.Cytoscape(
                id='characters',
                minZoom=0.2,
                maxZoom=2,
                layout={'name': 'circle',  # grid
                        'animate': True},
                elements=my_elements,
                style={'width': '90vw', 'height': '90vh'},
                stylesheet=stylesheet.stylesheet
            )
        ], style={'width': '80%', 'display': 'inline-block'}),
        html.Div([
            cyto.Cytoscape(
                id='legends',
                minZoom=0.5,
                maxZoom=2,
                layout={'name': 'grid',
                        'rows': 11,
                        'animate': True},
                elements=legend_elements,
                style={'height': '98vh'},
                stylesheet=legend_stylesheet.stylesheet
            )
        ], style={'width': '18%', 'display': 'inline-block'}),
    ],
        className='twelve columns'),
],
    style={'font-family': 'Rockwell'},
    className='row',
)


@app.callback(Output("characters", "elements"),
              [Input(component_id='slct_author', component_property='value'),
               Input(component_id='slct_play', component_property='value')])
def update_layout(author, play):
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
    return all_elements
