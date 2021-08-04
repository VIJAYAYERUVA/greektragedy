import pathlib

import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output

from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# ---------- Import and clean data (importing csv into pandas)
df = pd.read_csv(DATA_PATH.joinpath("Authors.csv"))
df.drop(['VADER_Score', 'BERT_Sentiment', 'Topic_Keywords_1'], axis=1, inplace=True)
df.rename(
    columns={'AuthorName': 'Author', 'PlayName': 'Play', 'ParagraphNumber': 'Paragraph Number',
             'CharacterName': 'Character', 'VADER_Label': 'Sentiment', 'BERT_Emotion': 'Emotion',
             'Dominant_Topic_1': 'Dominant Topic'}, inplace=True)

PAGE_SIZE = 15

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Title("Greek Tragedy Data"),
            html.H1(
                "Greek Tragedy Data",
                style={'text-align': 'center'}
            ),
            html.H6(
                'Hint! Column filtering uses "contains" logic. Filtering with  > < = are also supported. For example '
                '=Female would find entries equal to Female.',
                style={'text-align': 'center', "color": "red"},
            ),
            dash_table.DataTable(
                id='table-sorting-filtering',
                data=df.to_dict('records'),
                columns=[
                    {"name": i, "id": i}
                    if i == 'Dialogue'
                    else {"name": i, "id": i, "hideable": True}
                    for i in df.columns
                ],
                # Tool tip
                tooltip_header={
                    'Dialogue': 'Dialogue from the Play',
                },

                tooltip={i: {
                    'value': i,
                    'use_with': 'both'  # both refers to header & data cell
                } for i in df.columns},

                css=[{
                    'selector': '.dash-table-tooltip',
                    'rule': 'background-color: gray; font-family: sans-serif;'
                }],

                page_current=0,
                page_size=PAGE_SIZE,
                page_action='custom',

                filter_action='custom',
                filter_query='',

                sort_action='custom',
                sort_mode='multi',
                sort_by=[],

                style_header={
                    'backgroundColor': 'gray',
                    'fontWeight': 'bold',
                    'border': '1px solid black',
                    'font-family': 'sans-serif',
                    'whiteSpace': 'normal',
                },

                style_cell={
                    'minWidth': 50, 'maxWidth': 50, 'width': 50,
                    'textAlign': 'left',
                    'padding': '5px',
                    'border': '1px solid black',
                    'font-family': 'sans-serif',
                    'whiteSpace': 'normal',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'height': 'auto',
                },
                style_cell_conditional=[
                    {'if': {'column_id': 'Dialogue'},
                     'minWidth': 150, 'maxWidth': 150, 'width': 150, },
                ],
                style_data={  # overflow cells' content into multiple lines
                    'whiteSpace': 'normal',
                    'height': 'auto'
                },
                tooltip_delay=0,
                tooltip_duration=None
            ),
        ])
    ])
], fluid=True)

operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


@app.callback(
    Output('table-sorting-filtering', 'data'),
    Input('table-sorting-filtering', "page_current"),
    Input('table-sorting-filtering', "page_size"),
    Input('table-sorting-filtering', 'sort_by'),
    Input('table-sorting-filtering', 'filter_query'))
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = df
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')
