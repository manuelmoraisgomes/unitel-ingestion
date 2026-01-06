from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    host = Column(String(100), index=True)
    service = Column(String(100), index=True)
    level = Column(String(20), index=True)
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
