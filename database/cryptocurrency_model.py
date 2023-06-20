from sqlalchemy import Column, DateTime, Integer, String

from .db.base_db import Base


class CryptoData(Base):
    __tablename__ = "crypto"

    id = Column(Integer(), primary_key=True)
    open_time = Column(DateTime(), nullable=False)
    open_price = Column(String(255), nullable=False)
    high_price = Column(String(255), nullable=False)
    low_price = Column(String(255), nullable=False)
    close_price = Column(String(255), nullable=False)
    volume = Column(String(255), nullable=False)
    close_time = Column(DateTime(), nullable=False)
    quote_asset_volume = Column(String(255), nullable=False)
    number_of_trades = Column(Integer(), nullable=False)
    taker_buy_base_asset_volume = Column(String(255), nullable=False)
    taker_buy_quote_asset_volume = Column(String(255), nullable=False)
    symbol = Column(String(255), nullable=False)
