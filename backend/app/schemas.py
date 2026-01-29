from pydantic import BaseModel
from typing import List

class PredictRequest(BaseModel):
    job_text: str

class PredictResponse(BaseModel):
    prediction: str  # 'REAL' or 'SCAM'
    confidence: float
    indicators: List[str]