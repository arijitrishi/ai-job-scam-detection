import React, { useState } from 'react';
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

function PredictionForm() {
  const [jobText, setJobText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await axios.post(`${API_BASE_URL}/api/predict`, {
        job_text: jobText
      });
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Something went wrong');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <textarea
          value={jobText}
          onChange={(e) => setJobText(e.target.value)}
          placeholder="Paste job description or suspicious email here..."
          rows="6"
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? 'Analyzing...' : 'Analyze Job'}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className={`result-box ${result.prediction.toLowerCase()}`}>
          <h3>{result.prediction}</h3>
          <p>Confidence: <strong>{result.confidence}%</strong></p>

          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{ width: `${result.confidence}%` }}
            />
          </div>

          <p className="indicator-title">⚠️ Scam Indicators</p>
          <ul>
            {result.indicators.length > 0
              ? result.indicators.map((i, idx) => <li key={idx}>{i}</li>)
              : <li>No suspicious indicators found</li>}
          </ul>
        </div>
      )}
    </>
  );
}

export default PredictionForm;
