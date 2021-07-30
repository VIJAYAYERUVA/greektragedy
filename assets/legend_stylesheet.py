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
        "selector": ".center-right",
        "style": {
            "text-valign": "center",
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
        'selector': ".gender-male",
        'style': {
            'background-color': '#ffffff',
            'width': 53,
            'height': 53,
            'background-image': ['/assets/male.png'],
        }
    },
    {
        'selector': '.gender-female',
        'style': {
            'background-color': '#ffffff',
            'width': 53,
            'height': 53,
            'background-image': ['/assets/female.png'],
        }
    },
    # shape: https://js.cytoscape.org/#style/node-body
    {
        'selector': '.class-upper',
        'style': {
            # 'shape': 'diamond',
            'background-color': '#f79647',
        }
    },
    {
        'selector': '.class-lower',
        'style': {
            # 'shape': 'star',
            'background-color': '#fbd485'
        }
    },
    {
        'selector': '.divinity-immortal',
        'style': {
            # 'shape': 'star',
            'background-color': '#ffffff',
            'border-color': '#003c78',
            "border-width": 6,
        }
    },
    {
        'selector': '.divinity-mortal',
        'style': {
            # 'shape': 'diamond',
            'background-color': '#ffffff',
            'border-color': '#2988ad',
            "border-width": 3,
        }
    },
    # https://js.cytoscape.org/#style/labels
    {
        'selector': '.emotion-anger',
        'style': {
            'color': '#b44a1c',
        }
    },
    {
        'selector': '.emotion-fear',
        'style': {
            'color': '#ed9619',
        }
    },
    {
        'selector': '.emotion-joy',
        'style': {
            'color': '#1c9674',
        }
    },
    {
        'selector': '.emotion-neutral',
        'style': {
            'color': '#48596e',
        }
    },
    {
        'selector': '.emotion-sadness',
        'style': {
            'color': '#35afcf'
        }
    }
]
