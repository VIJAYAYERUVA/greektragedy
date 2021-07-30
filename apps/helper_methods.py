# function to calculate %
def percentage(x):
    return 100 * x / float(x.sum())


# function  to create label
def percentagelabel(x):
    if x == 10:
        return '(0-10)%'  # of the narrative
    elif x == 20:
        return '(10-20)%'
    elif x == 30:
        return '(20-30)%'
    elif x == 40:
        return '(30-40)%'
    elif x == 50:
        return '(40-50)%'
    elif x == 60:
        return '(50-60)%'
    elif x == 70:
        return '(60-70)%'
    elif x == 80:
        return '(70-80)%'
    elif x == 90:
        return '(80-90)%'
    elif x == 100:
        return '(90-100)%'
    else:
        pass


# colors
vader_color = {'positive': '#1c9674',
               'negative': '#b44a1c'
               }

bert_color = {'anger': '#b44a1c',
              'fear': '#ed9619',
              'joy': '#1c9674',
              'neutral': '#48596e',
              'sadness': '#35afcf'
              }

topic_color = {'Topic 1': '#48596e',
               'Topic 2': '#1c9674',
               'Topic 3': '#35afcf',
               'Topic 4': '#b44a1c'
               }

author_color = {
    'Aeschylus': '#aa5986',
    'Euripides': '#f79647',
    'Sophocles': '#003c78'
}

# labels
labels = {
    'AuthorName': 'Authors',
    'Dominant_Topic': 'Topic',
    'PercentageOfDialogues': '% of Dialogues',
    'NoOfDialogues': '#Dialogues',
    'VADER_Sentiment': 'VADER Sentiment',
    'VADER_Score': 'VADER Sentiment Score',
    'VADER_Label': 'VADER Label',
    'TK_inDialogue': "Topic's Keywords in the Dialogue",
    'Dominant_Topic_1': "Dominant Topic",
    'Topic_Keywords_1': 'Topic Keywords'
}

# Orders
author_order = {'AuthorName': ['Aeschylus', 'Euripides', 'Sophocles']}
vader_order = {'VADER_Label': ['positive', 'negative']}
bert_order = {'BERT_Emotion': ['neutral', 'joy', 'sadness', 'fear', 'anger']}
topic_order = {'Dominant_Topic_1': ['Topic 1', 'Topic 2', 'Topic 3', 'Topic 4']}

# config
config = {
    'displayModeBar': False
}

# layouts
update_layout1 = dict(
    title_x=0.5,
    font_size=13,
    font_family='sans-serif',
    margin=dict(l=0, r=0, b=0, t=120),
    hoverlabel=dict(
        font_size=12,
        font_family='Rockwell'),
    autotypenumbers="strict",
    hoverlabel_align='right',
    template="simple_white",
    autosize=False,
    # width=800,
    # height=600,
    legend=dict(
        orientation="h",
        x=0,
        y=-0.15, )
)

update_layout2 = dict(
    title_x=0.5,
    font_size=13,
    font_family='sans-serif',
    margin=dict(l=0, r=0, b=0, t=120),
    hoverlabel=dict(
        font_size=12,
        font_family='Rockwell'),
    autotypenumbers="strict",
    hoverlabel_align='right',
    template="simple_white",
    autosize=False,
    # width=800,
    # height=600,
    legend=dict(
        orientation="h",
        x=0,
        y=1.20, )
)

update_layout3 = dict(
    title_x=0.5,
    font_size=13,
    font_family='sans-serif',
    margin=dict(l=0, r=0, b=0, t=120),
    hoverlabel=dict(
        font_size=12,
        font_family='Rockwell'),
    autotypenumbers="strict",
    hoverlabel_align='right',
    template="simple_white",
    autosize=False,
    # width=800,
    height=600,
    legend=dict(
        orientation="h"
    )
)

update_layout4 = dict(
    title_x=0.5,
    font_size=13,
    font_family='sans-serif',
    margin=dict(l=0, r=0, b=0, t=120),
    hoverlabel=dict(
        font_size=12,
        font_family='Rockwell'),
    autotypenumbers="strict",
    hoverlabel_align='right',
    template="simple_white",
    autosize=False,
    # width=800,
    # height=600,
    legend=dict(
        orientation="h",
        x=0,
        y=1.11, )
)
# helper methods for network

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

update_layout5 = dict(
    title_x=0.5,
    font_size=13,
    font_family='sans-serif',
    margin=dict(l=0, r=0, b=0, t=120),
    hoverlabel=dict(
        font_size=12,
        font_family='Rockwell'),
    autotypenumbers="strict",
    hoverlabel_align='right',
    template="plotly_white",
    autosize=False,
    # width=800,
    # height=600,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        itemclick="toggleothers",
        itemdoubleclick="toggle"),
    # xaxis=dict(
    #     tickmode='linear')
)
