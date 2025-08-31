import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Log(Base):
    __tablename__ = "logs"

    id  = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    prompt = Column(String, index=True)