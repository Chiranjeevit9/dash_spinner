import dash_spinner
from dash import Dash, callback, html, Input, Output
import dash_bootstrap_components as dbc
from dash import html

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([html.Div(html.H3("Dash Spinners", style={"text-align": "center",
                                                                "font-size": "-webkit-xxx-large"})), html.Br(), dbc.Row(
    [
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#00ff89',
                    spinner_type="PushSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#00ff89',
                    spinner_type="BallSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#686769',
                    spinner_type="ClapSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#686769',
                    spinner_type="BarsSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#686769',
                    spinner_type="CircleSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#686769',
                    spinner_type="ClassicSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=100,
                    Color='#686769',
                    spinner_type="CombSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#00ff89',
                    spinner_type="CubeSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=100,
                    Color='#686769',
                    spinner_type="DominoSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#00a699',
                    spinner_type="FillSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#d63384',
                    spinner_type="FireworkSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#0dcaf0',
                    spinner_type="FlagSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#686769',
                    spinner_type="FlapperSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#00ff89',
                    spinner_type="GooSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="GridSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=30,
                    Color='#686769',
                    spinner_type="GuardSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#bf250c',
                    spinner_type="HeartSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#198754',
                    spinner_type="HoopSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="ImpulseSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#00ff89',
                    spinner_type="JellyfishSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="MagicSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="MetroSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="PongSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="PulseSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="RainbowSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#00ff89',
                    spinner_type="RingSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="RotateSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="SequenceSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="SphereSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="SpiralSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="SwapSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center", "height": "4rem"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#00ff89',
                    spinner_type="SwishSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="TraceSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#0d6efd',
                    spinner_type="WaveSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        dbc.Col(dbc.Card(
            [dbc.CardBody(
                [dash_spinner.DashSpinner(
                    Size=40,
                    Color='#686769',
                    spinner_type="WhisperSpinner",
                    loading=True
                )])
             ], style={"width": "12rem", "align-items": "center"},)),
        html.Div(id='output')
    ], style={"margin-inline-start": "auto"}, align="center", className="row row-cols-2 row-cols-lg-6 g-2 g-lg-3")])


# @callback(Output('output', 'children'), Input('input', 'value'))
# def display_output(value):
#     return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
