import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://admin:admin@localhost:5432/iot_db")

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Real-Time IoT Analytics Dashboard"),

    dcc.Interval(
        id='interval',
        interval=5000,
        n_intervals=0
    ),

    html.Div([
        html.Div(id="device-count"),
        html.Div(id="avg-temp")
    ]),

    dcc.Graph(id="temp_graph"),

    dcc.Graph(id="humidity_graph"),

    dcc.Graph(id="alert_graph"),

    html.H3("Latest Sensor Data"),

    html.Div(id="table")
])


@app.callback(
    [
        Output("temp_graph","figure"),
        Output("humidity_graph","figure"),
        Output("alert_graph","figure"),
        Output("device-count","children"),
        Output("avg-temp","children"),
        Output("table","children")
    ],
    [Input("interval","n_intervals")]
)

def update_dashboard(n):

    query = """
    SELECT *
    FROM iot_analytics
    ORDER BY processed_at DESC
    LIMIT 500
    """

    df = pd.read_sql(query, engine)

    if df.empty:
        return {}, {}, {}, "No data", "No data", ""

    # Temperature over time
    fig_temp = px.line(
        df,
        x="processed_at",
        y="temperature",
        title="Temperature Over Time"
    )

    # Humidity distribution
    fig_humidity = px.histogram(
        df,
        x="humidity",
        title="Humidity Distribution"
    )

    # Alerts
    alert_counts = df["status"].value_counts().reset_index()
    alert_counts.columns = ["status","count"]

    fig_alert = px.pie(
        alert_counts,
        names="status",
        values="count",
        title="Alert Distribution"
    )

    device_count = f"Active Devices: {df['device_id'].nunique()}"
    avg_temp = f"Average Temperature: {round(df['temperature'].mean(),2)}"

    table = html.Table([

        html.Tr([html.Th(col) for col in df.columns])

    ] + [

        html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ])

        for i in range(min(len(df),10))
    ])

    return fig_temp, fig_humidity, fig_alert, device_count, avg_temp, table


if __name__ == "__main__":
    app.run(debug=True)