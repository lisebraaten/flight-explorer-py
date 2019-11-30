import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from view import jitter_bar_fatality_chart


def return_incident_jitter_boxplot_result(value=None):
    """
    Returns the html div to be rendered into the counts of different categories tab.
    Parameters
    ----------
    value: the value passed in by the drop-down button.

    Returns
    -------
    an html div of the jitter/boxplot to be rendered inside the tab.

    """
    value = 'incident' if value is None else value

    tab2_result = dbc.Container([
        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id='dd_incident_selection',
                options=[
                    {'label': 'Incidents', 'value': 'incident'},
                    {'label': 'Fatal incidents', 'value': 'fatal_accident'},
                    {'label': 'Fatalities', 'value': 'fatalities'},
                    {'label': 'Lethality', 'value': 'lethality'},

                ],
                value='incident',
                searchable=False,
                clearable=False,
                style=dict(width='60%',
                           verticalAlign="middle")
            ),
                width="4"),
            dbc.Col(html.Iframe(
                sandbox='allow-scripts',
                id='jitter_bar_chart',
                height='1000',
                width='1500',
                style={'border-width': '0'},
                srcDoc=jitter_bar_fatality_chart.return_jitter_bar_fatality_chart(value).to_html()
            ),
                width="8")
        ])
    ],
        fluid=True)
    #
    # tab2_result = html.Div([
    #     dcc.Dropdown(
    #         id='dd_incident_selection',
    #         options=[
    #             {'label': 'Incidents', 'value': 'incident'},
    #             {'label': 'Fatal incidents', 'value': 'fatal_accident'},
    #             {'label': 'Fatalities', 'value': 'fatalities'},
    #             {'label': 'Lethality', 'value': 'lethality'},
    #
    #         ],
    #         value='incident',
    #         searchable=False,
    #         clearable=False,
    #         style=dict(width='45%',
    #                    verticalAlign="middle")
    #     ),
    #
    #     html.Iframe(
    #         sandbox='allow-scripts',
    #         id='jitter_bar_chart',
    #         height='1000',
    #         width='1500',
    #         style={'border-width': '0'},
    #         srcDoc=jitter_bar_fatality_chart.return_jitter_bar_fatality_chart(value).to_html()
    #     ),
    #
    # ])
    return tab2_result