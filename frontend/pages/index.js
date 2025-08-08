import { useState } from 'react';

export default function Home() {
  const [testResult, setTestResult] = useState('');

  // Backend URL - automatically detects environment
  const backend = process.env.NEXT_PUBLIC_BACKEND_URL || 
                 (process.env.NODE_ENV === 'production' 
                   ? 'https://openaiastroprediction-production.up.railway.app'
                   : 'http://localhost:8000');

  const testBackend = async () => {
    try {
      const response = await fetch(`${backend}/health`);
      const data = await response.json();
      setTestResult(`✅ Backend connected! Status: ${data.status}`);
    } catch (error) {
      setTestResult(`❌ Backend connection failed: ${error.message}`);
    }
  };

  return (
    <div style={{padding: '40px', fontFamily: 'Arial, sans-serif', maxWidth: '800px', margin: '0 auto'}}>
      <div style={{textAlign: 'center', marginBottom: '40px'}}>
        <h1 style={{fontSize: '3em', margin: '0', color: '#333'}}>🔮</h1>
        <h2 style={{color: '#666', margin: '10px 0'}}>Vedic Astrology</h2>
        <p style={{color: '#888'}}>AI-Powered Astrological Insights</p>
      </div>

      <div style={{background: '#f5f5f5', padding: '20px', borderRadius: '8px', marginBottom: '20px'}}>
        <h3>🚀 Deployment Test</h3>
        <p><strong>Backend URL:</strong> {backend}</p>
        <p><strong>Environment:</strong> {process.env.NODE_ENV}</p>
        <button 
          onClick={testBackend}
          style={{
            background: '#007acc', 
            color: 'white', 
            border: 'none', 
            padding: '10px 20px', 
            borderRadius: '5px',
            cursor: 'pointer',
            fontSize: '16px'
          }}
        >
          Test Backend Connection
        </button>
        {testResult && (
          <div style={{marginTop: '10px', padding: '10px', background: 'white', borderRadius: '5px'}}>
            {testResult}
          </div>
        )}
      </div>

      <div style={{background: '#e8f4fd', padding: '20px', borderRadius: '8px'}}>
        <h3>🎯 Quick Setup Guide</h3>
        <ol>
          <li>✅ Frontend deployed on Vercel</li>
          <li>✅ Backend running on Railway</li>
          <li>🔧 Test backend connection above</li>
          <li>📱 Ready to use!</li>
        </ol>
      </div>

      <footer style={{textAlign: 'center', marginTop: '40px', color: '#666'}}>
        <p>Full app will be restored after testing ✨</p>
      </footer>
    </div>
  );
}