import requests
import pandas as pd
import numpy as np


SYMBOLS = '["BTCUSDT","BTCBUSD","BTCEUR","ETHEUR","WBTCBTC","BNBBTC","LTCBTC","ETHBTC","LTCUSDT","RNDRUSDT"]'
KEYS = ["symbol", "weightedAvgPrice", "volume"]


def form_data_pie_plot():
    url = 'https://api4.binance.com/api/v3/ticker/24hr'
    params = {
        "symbols": SYMBOLS
    }
    response = requests.get(url=url, params=params).json()
    df = pd.DataFrame(
        data=[x.values() for x in response], columns=response[0].keys()
    )
    df = df[KEYS]
    df.weightedAvgPrice = df.weightedAvgPrice.astype(np.float64)
    df.volume = df.volume.astype(np.float64)
    market_caps = round(df.weightedAvgPrice, 2) * round(df.volume, 2)
    df["market_caps"] = market_caps
    return df
