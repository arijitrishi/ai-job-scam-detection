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
      const response = await axios.post(`${API_BASE_URL}/api/predict`, { job_text: jobText });
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <textarea
          value={jobText}
          onChange={(e) => setJobText(e.target.value)}
          placeholder="Paste job description or email content here..."
          rows="6"
          style={{ width: '100%', padding: '10px', marginBottom: '10px', border: '1px solid #ccc', borderRadius: '4px' }}
          required
        />
        <button
          type="submit"
          disabled={loading}
          style={{ padding: '10px 20px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px', cursor: loading ? 'not-allowed' : 'pointer' }}
        >
          {loading ? 'Predicting...' : 'Predict'}
        </button>
      </form>

      {error && <p style={{ color: 'red', marginTop: '10px' }}>{error}</p>}

      {result && (
        <div style={{ marginTop: '20px', padding: '10px', border: '1px solid #ccc', borderRadius: '4px' }}>
          <h3 style={{ color: result.prediction === 'REAL' ? 'green' : 'red' }}>
            Prediction: {result.prediction}
          </h3>
          <p>Confidence: {result.confidence}%</p>
          <div style={{ width: '100%', backgroundColor: '#e0e0e0', borderRadius: '4px', height: '20px' }}>
            <div
              style={{
                width: `${result.confidence}%`,
                backgroundColor: result.prediction === 'REAL' ? 'green' : 'red',
                height: '100%',
                borderRadius: '4px'
              }}
            />
          </div>
          <p><strong>Key Scam Indicators:</strong></p>
          <ul>
            {result.indicators.length > 0 ? result.indicators.map((ind, idx) => <li key={idx}>{ind}</li>) : <li>None detected</li>}
          </ul>
        </div>
      )}
    </div>
  );
}

export default PredictionForm;