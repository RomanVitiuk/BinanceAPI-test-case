#!/bin/sh

cd ~/BinanceAPI
source venv/bin/activate
python db_init.py
python data_collector.py

sleep 3

python app.py
