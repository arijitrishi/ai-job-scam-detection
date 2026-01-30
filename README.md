# 🕵️‍♂️ AI-Based Job Scam Detection System

An AI-powered web application that detects fake or scam job postings using Machine Learning.  
The system analyzes job descriptions and predicts whether a posting is **legitimate or fraudulent**, along with confidence scores and indicators.

This project is built with a **FastAPI backend**, **React frontend**, and **ML-based prediction logic**, designed for real-world usage and scalability.

---

## 🚀 Features

- 🔍 Detects fake/scam job postings using AI
- 📊 Confidence score with prediction indicators
- ⚡ FastAPI backend with REST API
- 🧠 Machine Learning model integration
- 🗄️ Database storage of predictions
- 🌐 React-based frontend (API-driven)
- 🔐 Secure environment configuration using `.env`

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **FastAPI**
- **SQLAlchemy**
- **Uvicorn**
- **Machine Learning (custom model / logic)**

### Frontend
- **React**
- **Axios**
- **HTML / CSS / JavaScript**

### Database
- **SQLite / PostgreSQL / MySQL** (configurable)

---

## 📁 Project Structure

job-scam-detection/
│
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI entry point
│ │ ├── models.py # Database models
│ │ ├── schemas.py # Pydantic schemas
│ │ ├── crud.py # DB operations
│ │ ├── ml_utils.py # ML prediction logic
│ │ ├── dependencies.py # DB dependency
│ │ └── database.py # DB configuration
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ ├── public/
│ ├── package.json
│ └── .env.example
│
├── .gitignore
└── README.md


---

## ⚙️ Environment Setup

### Backend `.env`
Create a `.env` file inside `backend/`:

```env
DATABASE_URL=sqlite:///./job_scam.db
Frontend .env
Create a .env file inside frontend/:

REACT_APP_API_URL=http://127.0.0.1:8000
▶️ How to Run the Project
🔹 Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
Backend will run at:

http://127.0.0.1:8000
Swagger Docs:

http://127.0.0.1:8000/docs
🔹 Frontend Setup
cd frontend
npm install
npm start
Frontend will run at:

http://localhost:3000
🔗 API Endpoint
Predict Job Scam
POST /api/predict
Request Body
{
  "job_text": "We are hiring freshers. Pay registration fee to apply."
}
Response
{
  "prediction": "Scam",
  "confidence": 92.5,
  "indicators": [
    "Registration fee",
    "Unrealistic salary"
  ]
}
🧪 Use Cases
Job portals filtering fake job postings

HR & recruitment platforms

Cyber fraud prevention systems

Educational AI/ML projects

🔒 Security Notes
.env files are ignored from GitHub

CORS handled via FastAPI

Secure dependency injection for DB sessions

📌 Future Improvements
User authentication & roles

Admin dashboard with analytics

Advanced NLP models (BERT, GPT-based)

Deployment using Docker & Cloud

Job URL analysis support

👨‍💻 Author
Arijit Ghosh
Backend Developer | Java | Python | FastAPI | Spring Boot
📍 India

⭐ Support
If you find this project useful:

⭐ Star the repository

🐞 Open issues for improvements

🤝 Fork & contribute

