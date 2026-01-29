import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.corpus import stopwords
import string
import logging

# Load model and vectorizer
try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    nltk.download('stopwords', quiet=True)
except Exception as e:
    logging.error(f"Failed to load ML model/vectorizer: {e}")
    raise RuntimeError("ML model not available")

# Preprocessing function (matches training)
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Known scam keywords (for indicators)
SCAM_KEYWORDS = [
    "urgent hiring", "pay upfront", "no interview", "send money", "deposit required",
    "work from home high pay", "no experience needed", "instant job", "visa processing fee"
]

def predict_scam(job_text: str) -> dict:
    if not job_text.strip():
        raise ValueError("Job text cannot be empty")
    
    # Preprocess
    processed_text = preprocess_text(job_text)
    
    # Vectorize
    X = vectorizer.transform([processed_text])
    
    # Predict
    prediction_proba = model.predict_proba(X)[0]
    prediction = "SCAM" if prediction_proba[1] > 0.5 else "REAL"  # Assuming 'SCAM' is class 1
    confidence = max(prediction_proba) * 100  # Convert to percentage
    
    # Extract indicators (simple keyword matching)
    indicators = [kw for kw in SCAM_KEYWORDS if kw.lower() in job_text.lower()]
    
    return {
        "prediction": prediction,
        "confidence": round(confidence, 2),
        "indicators": indicators
    }