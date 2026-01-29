import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import stopwords
import string

# Download NLTK stopwords if not already done
nltk.download('stopwords')

# Small synthetic dataset (real vs scam job texts)
data = [
    # Real job texts
    ("We are hiring a software engineer. Requirements: 3 years experience, remote work available. Apply via our website.", "REAL"),
    ("Join our team as a data analyst. Full-time position with benefits. Interview process includes coding test.", "REAL"),
    ("Marketing specialist needed. Competitive salary, health insurance. Send resume to hr@company.com.", "REAL"),
    ("Graphic designer role. Portfolio required. On-site in New York. Equal opportunity employer.", "REAL"),
    ("Customer service rep. Training provided. Flexible hours. Apply now.", "REAL"),
    
    # Scam job texts
    ("Urgent hiring! Pay upfront for training materials. No interview needed. Work from home and earn $5000/week.", "SCAM"),
    ("Fake job alert: Send money for visa processing. Immediate start, no experience required.", "SCAM"),
    ("Scam: Deposit $100 to get hired. High paying job with no skills needed.", "SCAM"),
    ("Beware: Pay for background check. Remote job paying $10k/month instantly.", "SCAM"),
    ("Fraud: Urgent application. No qualifications needed. Send payment to start.", "SCAM"),
]

# Preprocessing function
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Prepare data
texts = [preprocess_text(text) for text, label in data]
labels = [label for text, label in data]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=1000)  # Limit features for simplicity
X = vectorizer.fit_transform(texts)
y = labels

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Evaluate (optional, for logging)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model and vectorizer
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("Model and vectorizer saved.")