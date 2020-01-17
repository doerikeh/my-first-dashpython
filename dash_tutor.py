import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('Dash'),
    dcc.Graph(id='example',
            figure={
                'data': [
                    {'x': [1,2,3,4,5,6], 'y': [1,2,3,4,5,6], 'type':'line', 'name':'data'},
                    {'x': [1,2,3,4,5,6], 'y': [1,2,3,4,5,6], 'type':'bar', 'name':'object'}
                    ],
                'layout':{
                    'title': 'Basic dash example'
                }
            })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)