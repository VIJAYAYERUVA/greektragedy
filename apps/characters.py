import pathlib

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
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
                    html.H2("Explore the Characters", className='text-center font-weight-bold ml-4 mr-4 mt-4 mb-4')
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12,
                )
            ],
            justify='center',
            align='center',
            # className='mb-4'
            ),
    dbc.Row(id='characters_gcd',
            children=[
                dbc.Col([
                    dcc.Graph(id='gcd_count', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=6, xl=6
                ),
                dbc.Col([
                    dcc.Graph(id='gcd_s', figure={}, config=helper_methods.config),
                ],
                    xs=12, sm=12, md=12, lg=6, xl=6
                ),
            ],
            justify='center',
            align='center',
            className='mb-4',
            ),
],
    fluid=True)


@app.callback(
    [Output(component_id='gcd_count', component_property='figure'),
     Output(component_id='gcd_s', component_property='figure')],
    [Input(component_id='characters_gcd', component_property='value')]
)
def update_row_2(characters_gcd):
    # fig1 creation
    # Initialize figure with subplots
    fig1 = make_subplots(
        rows=1, cols=3, subplot_titles=("Gender", "Class", "Divinity")
    )
    # Add traces
    fig1.append_trace(
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

    fig1.append_trace(
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

    fig1.append_trace(
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

    fig1.append_trace(
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

    fig1.append_trace(
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

    fig1.append_trace(
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

    fig1.update_yaxes(title_text="#Characters", row=1, col=1)
    fig1.update_layout(
        title='<b>Total #characters from three authors including Gender, Class, Divinity</b>',
    )
    fig1.update_layout(helper_methods.update_layout3)

    # fig2 creation
    # Initialize figure with subplots
    fig2 = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=("Gender", "Class", "Divinity")
    )

    # Gender - Female
    fig2.append_trace(
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

    fig2.append_trace(
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
    fig2.append_trace(
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

    fig2.append_trace(
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
    fig2.append_trace(
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

    fig2.append_trace(
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
    fig2.append_trace(
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

    fig2.append_trace(
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
    fig2.append_trace(
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

    fig2.append_trace(
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
    fig2.append_trace(
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

    fig2.append_trace(
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

    fig2.update_yaxes(title_text="% of Dialogues", row=1, col=1)
    fig2.update_layout(
        title='<b>% of Dialogues from three authors including including <br />'
              'Gender, Class, Divinity and "Sentiment"</b>',
    )
    fig2.update_layout(helper_methods.update_layout3)
    return fig1, fig2
