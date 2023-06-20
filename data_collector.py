import argparse

from os import getcwd
from os.path import join, isfile

import pandas as pd
import numpy as np
import requests

from database.db.base_db import engine
from utils_script import agent, columns, insert_data, symbol_name


parser = argparse.ArgumentParser()

parser.add_argument(
    "-s",
    "--symbol",
    help="Set cryptocurrency symbol, by default: BTCUSDT"
)
parser.add_argument(
    "-i",
    "--interval",
    help="set interval (2h, 8h, 1d) in hours or days, by default: 4h"
)
args = parser.parse_args()


class BinanceRequsts:
    def __init__(self, symbol="BTCUSDT", interval="4h", limit=500):
        self._base_url = 'https://api4.binance.com'
        self._get_data = '/api/v3/klines'
        self._params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
        self._url = self._base_url + self._get_data

    def response_data(self):
        """
        Send request to Binance and get response about
        cryptocurrency by relevant interval time.
        """
        return requests.get(
            url=self._url,
            params=self._params,
            headers=agent()
        ).json()


if args.symbol and args.interval:
    data_parser = BinanceRequsts(
        symbol=args.symbol,
        interval=args.interval
    )
    symbol_name = args.symbol
elif args.symbol:
    data_parser = BinanceRequsts(
        symbol=args.symbol
    )
    symbol_name = args.symbol
elif args.interval:
    data_parser = BinanceRequsts(
        interval=args.interval
    )
else:
    data_parser = BinanceRequsts()


data = [x[:-1] + [symbol_name] for x in data_parser.response_data()]

df = pd.DataFrame(data=np.array(data), columns=columns)

if not isfile(join(getcwd(), 'candlestick_data.csv')):
    df.to_csv('candlestick_data.csv', index=False)
else:
    df.to_csv(
        'candlestick_data.csv', mode='a', index=False, header=False
    )

insert_data(engine=engine, df=df)
