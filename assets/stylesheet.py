# https://github.com/plotly/dash-cytoscape/blob/master/usage-stylesheet.py
stylesheet = [
    # Group selectors for NODES
    {
        'selector': 'node',
        'style': {
            'label': 'data(label)',
            # 'background-color': 'blue',
            'font-family': 'sans-serif',
            'font-size': 16,
            'font-weight': 'bolder',
        }
    },

    # Group selectors for EDGES
    {
        'selector': 'edge',
        'style': {
            # 'label': 'data(weight)',
            'line-color': 'black',
            # Edge Types: https://js.cytoscape.org/demos/edge-types/
            'curve-style': 'bezier'
        }
    },

    # Class selectors
    {
        "selector": ".bottom-right",
        "style": {
            "text-valign": "bottom",
            "text-halign": "right"
        }
    },

    {
        "selector": ".multiline-manual",
        "style": {
            "text-wrap": "wrap"
        }
    },
    # Conditional Styling
    # this weight class only exists within the EDGES
    {
        'selector': '[weight = 1]',
        'style': {
            'width': 2
        }
    },
    {
        'selector': '[weight = 2]',
        'style': {
            'width': 5
        }
    },
    {
        'selector': '[gender = "Male"]',
        'style': {
            # 'background-color': '#ee5a45',
            'width': 60,
            'height': 60,
            'background-image': ['/assets/male.png'],
        }
    },
    {
        'selector': '[gender = "Female"]',
        'style': {
            # 'background-color': '#0d6d64',
            'width': 60,
            'height': 60,
            'background-image': ['/assets/female.png'],
        }
    },
    # shape: https://js.cytoscape.org/#style/node-body
    {
        'selector': '[class = "Upper"]',
        'style': {
            # 'shape': 'diamond',
            'background-color': '#f79647',
        }
    },
    {
        'selector': '[class = "Lower"]',
        'style': {
            # 'shape': 'star',
            'background-color': '#fbd485'
        }
    },
    {
        'selector': '[divinity = "Immortal"]',
        'style': {
            # 'shape': 'star',
            'border-color': '#003c78',
            "border-width": 6,
        }
    },
    {
        'selector': '[divinity = "Mortal"]',
        'style': {
            # 'shape': 'diamond',
            'border-color': '#2988ad',
            "border-width": 3,
        }
    },
    # https://js.cytoscape.org/#style/labels
    {
        'selector': '[bert_emotion = "anger"]',
        'style': {
            'color': '#b44a1c',
        }
    },
    {
        'selector': '[bert_emotion = "fear"]',
        'style': {
            'color': '#ed9619',
        }
    },
    {
        'selector': '[bert_emotion = "joy"]',
        'style': {
            'color': '#1c9674',
        }
    },
    {
        'selector': '[bert_emotion = "neutral"]',
        'style': {
            'color': '#48596e',
        }
    },
    {
        'selector': '[bert_emotion = "sadness"]',
        'style': {
            'color': '#35afcf'
        }
    }
]
