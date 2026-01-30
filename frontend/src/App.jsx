import React from 'react';
import PredictionForm from './components/PredictionForm';
import './App.css';

function App() {
  return (
    <div className="app-container">
      <div className="card">
        <h1>🛡️ AI Fake Job Detection</h1>
        <p className="subtitle">
          Paste any job description or email and let AI detect scams instantly
        </p>
        <PredictionForm />
      </div>
    </div>
  );
}

export default App;
