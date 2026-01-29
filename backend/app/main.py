from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import logging

from . import schemas, crud, ml_utils
from .dependencies import get_db

# ----------------------------------
# Logging configuration
# ----------------------------------
logging.basicConfig(level=logging.INFO)

# ----------------------------------
# FastAPI app
# ----------------------------------
app = FastAPI(title="AI Fake Job / Scam Detection System")

# ----------------------------------
# CORS Middleware (FIXES 405 OPTIONS ERROR)
# ----------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],  # POST, OPTIONS, etc.
    allow_headers=["*"],
)

# ----------------------------------
# API Endpoint
# ----------------------------------
@app.post("/api/predict", response_model=schemas.PredictResponse)
def predict_job_scam(
    request: schemas.PredictRequest,
    db: Session = Depends(get_db)
):
    try:
        # ML Prediction
        result = ml_utils.predict_scam(request.job_text)
        prediction_response = schemas.PredictResponse(**result)

        # Save prediction to DB
        crud.create_prediction(db, prediction_response, request.job_text)

        logging.info(
            f"Prediction saved: {prediction_response.prediction} "
            f"with confidence {prediction_response.confidence}%"
        )

        return prediction_response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
