
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Combined View: Yield Curve & TBL Regressions", style={'textAlign': 'center'}),
    html.Div([
        html.Iframe(
            src="https://augustinecarb.github.io/yield-curve/",
            style={"width": "49%", "height": "500px", "border": "1px solid black"}
        ),
        html.Iframe(
            src="https://augustinecarb.github.io/tbl_regressions/",
            style={"width": "49%", "height": "500px", "border": "1px solid black"}
        )
    ], style={"display": "flex", "justifyContent": "space-between"})
])

if __name__ == "__main__":
    app.run(debug=True)
