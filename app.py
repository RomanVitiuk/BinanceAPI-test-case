from datetime import datetime

from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from utils_app import form_data_pie_plot


app = Dash(__name__)

# ------form pie chart data------------------
pie_df = form_data_pie_plot()
pie_fig = px.pie(
    pie_df, values='market_caps',
    names='symbol'
)
# ------form candlestick chart data----------
candl_df = pd.read_csv('candlestick_data.csv')
candl_df.open_time = candl_df.open_time.apply(
    lambda x: datetime.fromtimestamp(int(x) / 1000)
)
candl_fig = go.Figure(
    data=[
        go.Candlestick(
            x=candl_df.open_time, open=candl_df.open_price,
            high=candl_df.high_price, low=candl_df.low_price,
            close=candl_df.close_price
        )
    ]
)

candl_fig.update_layout(xaxis_rangeslider_visible=False)


app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Binance candlestick chart'),
        dcc.Graph(
            id='graph1',
            figure=candl_fig
        ),
    ]),
    # pie chart
    html.Div([
        html.H1(children='Pie chart of Market Capitalization'),
        dcc.Graph(
            id='graph2',
            figure=pie_fig
        ),
    ]),
])


if __name__ == "__main__":
    app.run_server(debug=True)
