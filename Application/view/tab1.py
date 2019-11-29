import dash_html_components as html
import dash_core_components as dcc
from view import chart2

def return_tab1_result(value = "0"):
    tab1_result = html.Div([
                dcc.RadioItems(
                    id = "radio-items",
                    options=[
                    {'label': 'First world', 'value': '0'},
                    {'label': 'Non first world', 'value': '1'},
                    {'label': 'Both', 'value': '2'}
                    ],
                    value='0'),
                html.Iframe(
                        sandbox='allow-scripts',
                        id='plot',
                        height='1000',
                        width='1500',
                        style={'border-width': '0'},
                        
                        srcDoc = chart2.return_plot_2().to_html(value)
            
                        )])
    return tab1_result