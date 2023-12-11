# coding: utf-8
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class HistoryStockKDatum(Base):
    __tablename__ = 'history_stock_k_data'

    id = Column(Integer, primary_key=True)
    code = Column(String(255))
    date = Column(String(255))
    time = Column(String(255))
    open = Column(Float(asdecimal=True))
    high = Column(Float(asdecimal=True))
    low = Column(Float(asdecimal=True))
    close = Column(Float(asdecimal=True))
    volume = Column(Integer)
    amount = Column(Float(asdecimal=True))
    adjustflag = Column(String(255))


class ShszAStockList(Base):
    __tablename__ = 'shsz_a_stock_list'

    id = Column(Integer, primary_key=True)
    code = Column(String(255))
    name = Column(String(255))
    exchange = Column(String(255))
    industry = Column(String(255))
