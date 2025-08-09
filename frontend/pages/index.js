import { useState } from "react";

// Custom SVG Icons
const Star = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill={color} viewBox="0 0 24 24" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
  </svg>
);

const Clock = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill="none" stroke={color} viewBox="0 0 24 24" strokeWidth="2" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <circle cx="12" cy="12" r="10"/>
    <polyline points="12,6 12,12 16,14"/>
  </svg>
);

const MapPin = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill="none" stroke={color} viewBox="0 0 24 24" strokeWidth="2" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
    <circle cx="12" cy="10" r="3"/>
  </svg>
);

const Calendar = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill="none" stroke={color} viewBox="0 0 24 24" strokeWidth="2" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
    <line x1="16" y1="2" x2="16" y2="6"/>
    <line x1="8" y1="2" x2="8" y2="6"/>
    <line x1="3" y1="10" x2="21" y2="10"/>
  </svg>
);

const Sparkles = ({ size = 18, color = "currentColor" }) => (
  <svg width={size} height={size} fill={color} viewBox="0 0 24 24" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <path d="M12 0l1.68 6.32L20 8l-6.32 1.68L12 16l-1.68-6.32L4 8l6.32-1.68L12 0z"/>
    <path d="M19 3l.5 2L22 5.5l-2.5.5L19 8l-.5-2L16 5.5l2.5-.5L19 3z"/>
    <path d="M19 16l.5 2L22 18.5l-2.5.5L19 21l-.5-2L16 18.5l2.5-.5L19 16z"/>
  </svg>
);

const Sun = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill={color} viewBox="0 0 24 24" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <circle cx="12" cy="12" r="5"/>
    <line x1="12" y1="1" x2="12" y2="3" stroke={color} strokeWidth="2"/>
    <line x1="12" y1="21" x2="12" y2="23" stroke={color} strokeWidth="2"/>
    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" stroke={color} strokeWidth="2"/>
    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" stroke={color} strokeWidth="2"/>
    <line x1="1" y1="12" x2="3" y2="12" stroke={color} strokeWidth="2"/>
    <line x1="21" y1="12" x2="23" y2="12" stroke={color} strokeWidth="2"/>
    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" stroke={color} strokeWidth="2"/>
    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" stroke={color} strokeWidth="2"/>
  </svg>
);

const Moon = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill={color} viewBox="0 0 24 24" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
  </svg>
);

const Briefcase = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill="none" stroke={color} viewBox="0 0 24 24" strokeWidth="2" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
  </svg>
);

const Timeline = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill="none" stroke={color} viewBox="0 0 24 24" strokeWidth="2" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <line x1="12" y1="2" x2="12" y2="22"/>
    <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
  </svg>
);

const Zap = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill={color} viewBox="0 0 24 24" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
  </svg>
);

const Heart = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill={color} viewBox="0 0 24 24" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
  </svg>
);

const DollarSign = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill="none" stroke={color} viewBox="0 0 24 24" strokeWidth="2" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <line x1="12" y1="1" x2="12" y2="23"/>
    <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
  </svg>
);

export default function Home() {
  const [formData, setFormData] = useState({
    dob: '',
    tob: '',
    lat: '',
    lon: '',
    tz_offset: '5.5',
    gender: 'Male'
  });

  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  // Backend URL - automatically detects environment
  const backend = process.env.NEXT_PUBLIC_BACKEND_URL || 
                 (process.env.NODE_ENV === 'production' 
                   ? 'https://openaiastroprediction.onrender.com'
                   : 'http://localhost:8000');

  const getPrediction = async () => {
    setLoading(true);
    setError('');
    setResults(null);

    try {
      const response = await fetch(`${backend}/predict?${new URLSearchParams({
        dob: formData.dob,
        tob: formData.tob,
        lat: formData.lat,
        lon: formData.lon,
        tz_offset: formData.tz_offset
      })}`);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setResults(data);
    } catch (error) {
      setError(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  const formatText = (text) => {
    if (!text) return '';
    
    return text.split('\n').map((line, index) => {
      if (line.trim() === '') return <br key={index} />;
      
      // Check for headers (lines starting with numbers or special characters)
      if (/^[0-9]+\.\s/.test(line) || /^[🌟✨💫🔮💼💑💰🎯]/g.test(line)) {
        return <h3 key={index} style={{color: '#2563eb', marginTop: '20px', marginBottom: '10px'}}>{line}</h3>;
      }
      
      // Check for bold text (wrapped in **)
      if (/\*\*(.*?)\*\*/.test(line)) {
        const parts = line.split(/(\*\*.*?\*\*)/g);
        return (
          <p key={index} style={{margin: '8px 0', lineHeight: '1.6'}}>
            {parts.map((part, partIndex) => {
              if (part.startsWith('**') && part.endsWith('**')) {
                return <strong key={partIndex} style={{color: '#059669'}}>{part.slice(2, -2)}</strong>;
              }
              return part;
            })}
          </p>
        );
      }
      
      return <p key={index} style={{margin: '8px 0', lineHeight: '1.6'}}>{line}</p>;
    });
  };

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      padding: '20px',
      fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, sans-serif'
    }}>
      <div style={{
        maxWidth: '1200px',
        margin: '0 auto',
        background: 'white',
        borderRadius: '20px',
        boxShadow: '0 20px 40px rgba(0,0,0,0.1)',
        overflow: 'hidden'
      }}>
        {/* Header */}
        <div style={{
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          color: 'white',
          padding: '40px',
          textAlign: 'center'
        }}>
          <div style={{fontSize: '4em', marginBottom: '10px'}}>🔮</div>
          <h1 style={{fontSize: '2.5em', margin: '0 0 10px 0', fontWeight: 'bold'}}>
            Vedic Astrology AI
          </h1>
          <p style={{fontSize: '1.2em', opacity: 0.9, margin: 0}}>
            Discover Your Cosmic Blueprint with AI-Powered Insights
          </p>
        </div>

        {/* Form */}
        <div style={{padding: '40px'}}>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
            gap: '20px',
            marginBottom: '30px'
          }}>
            <div>
              <label style={{display: 'block', marginBottom: '8px', fontWeight: '600', color: '#374151'}}>
                <Calendar size={16} color="#6b7280" /> Date of Birth
              </label>
              <input
                type="date"
                value={formData.dob}
                onChange={(e) => setFormData({...formData, dob: e.target.value})}
                style={{
                  width: '100%',
                  padding: '12px',
                  border: '2px solid #e5e7eb',
                  borderRadius: '8px',
                  fontSize: '16px',
                  transition: 'border-color 0.3s'
                }}
                onFocus={(e) => e.target.style.borderColor = '#667eea'}
                onBlur={(e) => e.target.style.borderColor = '#e5e7eb'}
              />
            </div>

            <div>
              <label style={{display: 'block', marginBottom: '8px', fontWeight: '600', color: '#374151'}}>
                <Clock size={16} color="#6b7280" /> Time of Birth
              </label>
              <input
                type="time"
                value={formData.tob}
                onChange={(e) => setFormData({...formData, tob: e.target.value})}
                style={{
                  width: '100%',
                  padding: '12px',
                  border: '2px solid #e5e7eb',
                  borderRadius: '8px',
                  fontSize: '16px',
                  transition: 'border-color 0.3s'
                }}
                onFocus={(e) => e.target.style.borderColor = '#667eea'}
                onBlur={(e) => e.target.style.borderColor = '#e5e7eb'}
              />
            </div>

            <div>
              <label style={{display: 'block', marginBottom: '8px', fontWeight: '600', color: '#374151'}}>
                <MapPin size={16} color="#6b7280" /> Latitude
              </label>
              <input
                type="number"
                step="0.000001"
                placeholder="e.g., 13.0827"
                value={formData.lat}
                onChange={(e) => setFormData({...formData, lat: e.target.value})}
                style={{
                  width: '100%',
                  padding: '12px',
                  border: '2px solid #e5e7eb',
                  borderRadius: '8px',
                  fontSize: '16px',
                  transition: 'border-color 0.3s'
                }}
                onFocus={(e) => e.target.style.borderColor = '#667eea'}
                onBlur={(e) => e.target.style.borderColor = '#e5e7eb'}
              />
            </div>

            <div>
              <label style={{display: 'block', marginBottom: '8px', fontWeight: '600', color: '#374151'}}>
                <MapPin size={16} color="#6b7280" /> Longitude
              </label>
              <input
                type="number"
                step="0.000001"
                placeholder="e.g., 80.2707"
                value={formData.lon}
                onChange={(e) => setFormData({...formData, lon: e.target.value})}
                style={{
                  width: '100%',
                  padding: '12px',
                  border: '2px solid #e5e7eb',
                  borderRadius: '8px',
                  fontSize: '16px',
                  transition: 'border-color 0.3s'
                }}
                onFocus={(e) => e.target.style.borderColor = '#667eea'}
                onBlur={(e) => e.target.style.borderColor = '#e5e7eb'}
              />
            </div>
          </div>

          <button
            onClick={getPrediction}
            disabled={loading || !formData.dob || !formData.tob || !formData.lat || !formData.lon}
            style={{
              width: '100%',
              padding: '16px',
              background: loading ? '#9ca3af' : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
              color: 'white',
              border: 'none',
              borderRadius: '12px',
              fontSize: '18px',
              fontWeight: '600',
              cursor: loading ? 'not-allowed' : 'pointer',
              transition: 'all 0.3s',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '10px'
            }}
          >
            {loading ? (
              <>
                <div style={{
                  width: '20px',
                  height: '20px',
                  border: '2px solid #ffffff',
                  borderTop: '2px solid transparent',
                  borderRadius: '50%',
                  animation: 'spin 1s linear infinite'
                }} />
                Analyzing Your Cosmic Blueprint...
              </>
            ) : (
              <>
                <Sparkles size={20} color="white" />
                Get Your Astrological Reading
              </>
            )}
          </button>

          {error && (
            <div style={{
              marginTop: '20px',
              padding: '15px',
              background: '#fef2f2',
              border: '1px solid #fecaca',
              borderRadius: '8px',
              color: '#dc2626'
            }}>
              {error}
            </div>
          )}
        </div>

        {/* Results */}
        {results && (
          <div style={{
            padding: '0 40px 40px',
            borderTop: '1px solid #e5e7eb'
          }}>
            <div style={{
              background: '#f8fafc',
              borderRadius: '16px',
              padding: '30px',
              marginBottom: '30px'
            }}>
              <h2 style={{
                fontSize: '1.8em',
                margin: '0 0 20px 0',
                color: '#1f2937',
                display: 'flex',
                alignItems: 'center',
                gap: '10px'
              }}>
                <Sparkles size={24} color="#667eea" />
                Your Birth Chart Analysis
              </h2>
              
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                gap: '15px',
                marginBottom: '30px'
              }}>
                {Object.entries(results.chart || {}).map(([planet, data]) => (
                  <div key={planet} style={{
                    background: 'white',
                    padding: '15px',
                    borderRadius: '12px',
                    border: '1px solid #e5e7eb',
                    textAlign: 'center'
                  }}>
                    <div style={{
                      fontSize: '1.2em',
                      fontWeight: '600',
                      color: '#374151',
                      marginBottom: '5px'
                    }}>
                      {planet}
                    </div>
                    <div style={{color: '#6b7280', fontSize: '0.9em'}}>
                      {data.rasi} • {data.nakshatra} Pada {data.pada}
                    </div>
                  </div>
                ))}
              </div>

              {results.interpretation && (
                <div style={{
                  background: 'white',
                  padding: '25px',
                  borderRadius: '12px',
                  border: '1px solid #e5e7eb'
                }}>
                  <h3 style={{
                    fontSize: '1.4em',
                    margin: '0 0 15px 0',
                    color: '#1f2937',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '8px'
                  }}>
                    <Star size={20} color="#667eea" />
                    Cosmic Interpretation
                  </h3>
                  <div style={{color: '#374151', lineHeight: '1.7'}}>
                    {formatText(results.interpretation)}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}
      </div>

      <style jsx>{`
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}