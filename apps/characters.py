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
])
