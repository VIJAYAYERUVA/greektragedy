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


# colors
VADER_Sentiment = {'positive': '#43ad65',
                   'negative': '#f79647'
                   }

BERT_Emotions = {'anger': '#b44a1c',
                 'fear': '#ed9619',
                 'joy': '#1c9674',
                 'neutral': '#48596e',
                 'sadness': '#35afcf'
                 }

Dominant_Topic = {'Topic 1': '#4573a7',
                  'Topic 2': '#aa4644',
                  'Topic 3': '#89a54e',
                  'Topic 4': '#71588f'
                  }

authors_color = {
    'Aeschylus': '#cddafd',
    'Euripides': '#bee1e6',
    'Sophocles': '#fad2e1'
}
# labels
labels = {
    "AuthorName": "Authors",
    "Dominant_Topic": "Topic",
    "PercentageOfDialogues": "% of Dialogues",
    'NoOfDialogues': '#Dialogues',
    "VADER_Score": "VADER Sentiment",
    "TK_inDialogue": "Topic_Keywords in the Dialogue",
    'Dominant_Topic_1': "Dominant_Topic",
    'Topic_Keywords_1': 'Topic_Keywords'
}
# Orders
Emotion_Order = {'BERT_Emotion': ['neutral', 'joy', 'sadness', 'fear', 'anger']}
Topic_Order = {"Dominant_Topic_1": ["Topic 1", "Topic 2", "Topic 3", "Topic 4"]}
