import React from 'react';
import PredictionForm from './components/PredictionForm';

function App() {
  return (
    <div style={{ fontFamily: 'Arial, sans-serif', maxWidth: '600px', margin: '50px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h1>AI Fake Job / Scam Detection System</h1>
      <PredictionForm />
    </div>
  );
}

export default App;