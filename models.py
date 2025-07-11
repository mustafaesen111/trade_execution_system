python
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Subscriber(Base):
    __tablename__ = 'subscribers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    broker = Column(String)
    api_key = Column(String)
    match_ratio = Column(Integer)
    max_daily_limit = Column(Float)
    allow_buy = Column(Boolean)
    allow_sell = Column(Boolean)