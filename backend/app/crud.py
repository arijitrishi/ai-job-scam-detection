from sqlalchemy.orm import Session
from . import models, schemas

def create_prediction(db: Session, prediction: schemas.PredictResponse, job_text: str):
    db_prediction = models.Prediction(
        job_text=job_text,
        prediction=prediction.prediction,
        confidence=prediction.confidence,
        indicators=prediction.indicators
    )
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction
