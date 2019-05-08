#!/usr/bin/env python
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
    html.H1(children='Proteomics QC Dashboard'),
    html.Div(children='''
        A dashboard for proteomics quality control.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Example Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(port=8889, debug=True)