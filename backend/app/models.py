from sqlalchemy import Column, Integer, String, Text, DECIMAL, TIMESTAMP, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    job_text = Column(Text, nullable=False)
    prediction = Column(String(4), nullable=False)  # 'REAL' or 'SCAM'
    confidence = Column(DECIMAL(5, 2), nullable=False)
    indicators = Column(JSON, nullable=True)  # List of strings as JSON
    created_at = Column(TIMESTAMP, server_default=func.now())