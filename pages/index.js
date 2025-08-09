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
  const [activeTab, setActiveTab] = useState('chart');
  const [career, setCareer] = useState(null);
  const [dasa, setDasa] = useState(null);
  const [yogas, setYogas] = useState(null);
  const [lifePurpose, setLifePurpose] = useState(null);
  const [dasaBhukti, setDasaBhukti] = useState(null);
  const [spouseAnalysis, setSpouseAnalysis] = useState(null);
  const [induDasa, setInduDasa] = useState(null);

  // Backend URL - automatically detects environment
  const backend = process.env.NEXT_PUBLIC_BACKEND_URL || 
                 (process.env.NODE_ENV === 'production' 
                   ? 'https://openaiastroprediction.onrender.com'
                   : 'http://localhost:8000');

  console.log('🔧 Environment check:', {
    NODE_ENV: process.env.NODE_ENV,
    NEXT_PUBLIC_BACKEND_URL: process.env.NEXT_PUBLIC_BACKEND_URL,
    backend: backend
  });

  const getPrediction = async () => {
    setLoading(true);
    setError('');
    setResults(null);
    setCareer(null);
    setDasa(null);
    setYogas(null);
    setLifePurpose(null);
    setDasaBhukti(null);
    setSpouseAnalysis(null);
    setInduDasa(null);

    try {
      console.log('🔍 Backend URL:', backend);
      console.log('🔍 Form Data:', formData);
      
      // Test backend connection first
      console.log('🔍 Testing health endpoint...');
      const healthCheck = await fetch(`${backend}/health`).then(res => res.json());
      console.log('🔍 Health check result:', healthCheck);
      
      if (healthCheck.status === "healthy") {
        console.log('✅ Backend is healthy, fetching data...');
        // Get all data from backend in parallel
        const promises = [
          fetch(`${backend}/predict?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
          fetch(`${backend}/career?${new URLSearchParams({ ...formData, gender: formData.gender })}`).then(res => res.json()),
          fetch(`${backend}/dasa?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
          fetch(`${backend}/yogas?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
          fetch(`${backend}/life_purpose?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
          fetch(`${backend}/dasa_bhukti?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
          fetch(`${backend}/spouse?${new URLSearchParams({ ...formData, gender: formData.gender })}`).then(res => res.json()),
          fetch(`${backend}/indu_dasa?${new URLSearchParams({ ...formData })}`).then(res => res.json())
        ];

        const [chartRes, careerRes, dasaRes, yogasRes, lifePurposeRes, dasaBhuktiRes, spouseRes, induDasaRes] = await Promise.all(promises);
        console.log('✅ All API calls completed successfully');
        console.log('📊 Chart response:', chartRes);
        console.log('📊 Dasa response:', dasaRes);
        
        // Set real data from backend
        setResults({
          chart: chartRes.chart || {},
          interpretation: chartRes.interpretation || "Analysis in progress...",
          status: chartRes.status,
          calculation_method: chartRes.calculation_method
        });
        
        setCareer(careerRes.report || "Career analysis in progress...");
        setDasa(dasaRes.dasa_timeline?.[2] || []); // Extract the timeline array from the response
        setYogas(yogasRes.yogas || []);
        setLifePurpose(lifePurposeRes.report || "Life purpose analysis in progress...");
        setDasaBhukti(dasaBhuktiRes.table || []); // Use the table array from the response
        setSpouseAnalysis(spouseRes.spouse_analysis || { gender: "Processing...", lagna: "Processing..." });
        setInduDasa(induDasaRes || { indu_lagnam: "Processing..." });
        
      } else {
        throw new Error("Backend not available");
      }
    } catch (error) {
      console.error('❌ Error in getPrediction:', error);
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

  const tabs = [
    { key: "chart", label: "Planetary Chart", icon: Sun },
    { key: "prediction", label: "Predictions", icon: Moon },
    { key: "career", label: "Career Insights", icon: Briefcase },
    { key: "dasa", label: "Dasa Timeline", icon: Timeline },
    { key: "dasabhukti", label: "Dasa Bhukti", icon: Calendar },
    { key: "yogas", label: "Yogas & Doshas", icon: Zap },
    { key: "lifepurpose", label: "Life Purpose", icon: Heart },
    { key: "spouse", label: "Spouse Analysis", icon: Heart },
    { key: "wealth", label: "Wealth Cycles", icon: DollarSign },
  ];

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
              
              {/* Tab Buttons */}
              <div style={{
                display: 'flex',
                gap: '8px',
                marginBottom: '24px',
                flexWrap: 'wrap',
                overflowX: 'auto',
                padding: '4px'
              }}>
                {tabs.map((tab) => (
                  <button
                    key={tab.key}
                    onClick={() => setActiveTab(tab.key)}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px',
                      padding: '12px 20px',
                      borderRadius: '12px',
                      border: 'none',
                      fontWeight: '500',
                      cursor: 'pointer',
                      transition: 'all 0.3s ease',
                      fontSize: '0.9rem',
                      whiteSpace: 'nowrap',
                      minWidth: 'fit-content',
                      ...(activeTab === tab.key ? {
                        background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
                        color: 'white',
                        boxShadow: '0 4px 15px rgba(99, 102, 241, 0.4)',
                        transform: 'scale(1.02)'
                      } : {
                        background: 'rgba(255, 255, 255, 0.7)',
                        color: '#64748b',
                        backdropFilter: 'blur(10px)'
                      })
                    }}
                  >
                    <tab.icon size={16} color={activeTab === tab.key ? "white" : "#64748b"} />
                    {tab.label}
                  </button>
                ))}
              </div>

              {/* Tab Content */}
              <div style={{
                background: 'linear-gradient(135deg, #f8fafc, rgba(99, 102, 241, 0.05))',
                borderRadius: '16px',
                padding: '24px',
                border: '1px solid #e2e8f0',
                minHeight: '400px'
              }}>
                {activeTab === "chart" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <Sun size={18} color="#f59e0b" />
                      Planetary Positions
                    </h3>
                    <div style={{ overflowX: 'auto' }}>
                      <table style={{
                        width: '100%',
                        borderCollapse: 'collapse',
                        background: 'white',
                        borderRadius: '12px',
                        overflow: 'hidden',
                        boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
                      }}>
                        <thead>
                          <tr>
                            <th style={{
                              background: '#f1f5f9',
                              fontWeight: '600',
                              color: '#374151',
                              padding: '12px 16px',
                              textAlign: 'left',
                              borderBottom: '1px solid #e2e8f0',
                              fontSize: '0.9rem'
                            }}>Planet</th>
                            <th style={{
                              background: '#f1f5f9',
                              fontWeight: '600',
                              color: '#374151',
                              padding: '12px 16px',
                              textAlign: 'left',
                              borderBottom: '1px solid #e2e8f0',
                              fontSize: '0.9rem'
                            }}>Rasi</th>
                            <th style={{
                              background: '#f1f5f9',
                              fontWeight: '600',
                              color: '#374151',
                              padding: '12px 16px',
                              textAlign: 'left',
                              borderBottom: '1px solid #e2e8f0',
                              fontSize: '0.9rem'
                            }}>Nakshatra</th>
                            <th style={{
                              background: '#f1f5f9',
                              fontWeight: '600',
                              color: '#374151',
                              padding: '12px 16px',
                              textAlign: 'left',
                              borderBottom: '1px solid #e2e8f0',
                              fontSize: '0.9rem'
                            }}>Pada</th>
                          </tr>
                        </thead>
                        <tbody>
                          {Object.entries(results.chart || {}).map(([planet, info]) => (
                            <tr key={planet} style={{
                              transition: 'background-color 0.2s ease'
                            }}>
                              <td style={{
                                padding: '12px 16px',
                                borderBottom: '1px solid #f1f5f9',
                                color: '#4b5563',
                                fontSize: '0.9rem',
                                fontWeight: '600'
                              }}>{planet}</td>
                              <td style={{
                                padding: '12px 16px',
                                borderBottom: '1px solid #f1f5f9',
                                color: '#4b5563',
                                fontSize: '0.9rem'
                              }}>{info.rasi}</td>
                              <td style={{
                                padding: '12px 16px',
                                borderBottom: '1px solid #f1f5f9',
                                color: '#4b5563',
                                fontSize: '0.9rem'
                              }}>{info.nakshatra}</td>
                              <td style={{
                                padding: '12px 16px',
                                borderBottom: '1px solid #f1f5f9',
                                color: '#4b5563',
                                fontSize: '0.9rem'
                              }}>{info.pada}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </>
                )}

                {activeTab === "prediction" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <Moon size={18} color="#6366f1" />
                      Cosmic Interpretation
                      {results.calculation_method && (
                        <span style={{fontSize: '0.8rem', color: '#64748b', marginLeft: '8px'}}>
                          ({results.calculation_method})
                        </span>
                      )}
                    </h3>
                    <div style={{
                      background: 'rgba(255, 255, 255, 0.9)',
                      borderRadius: '16px',
                      padding: '24px',
                      border: '1px solid rgba(99, 102, 241, 0.1)',
                      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)'
                    }}>
                      <div style={{
                        color: '#374151',
                        lineHeight: '1.6',
                        fontSize: '1rem',
                        margin: '0',
                        whiteSpace: 'pre-line'
                      }}>
                        {formatText(results.interpretation)}
                      </div>
                    </div>
                  </>
                )}

                {activeTab === "career" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <Briefcase size={18} color="#8b5cf6" />
                      Career Analysis
                    </h3>
                    <div style={{
                      background: 'rgba(255, 255, 255, 0.9)',
                      borderRadius: '16px',
                      padding: '24px',
                      border: '1px solid rgba(139, 92, 246, 0.1)',
                      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)'
                    }}>
                      <div style={{
                        color: '#374151',
                        lineHeight: '1.6',
                        fontSize: '1rem',
                        margin: '0',
                        whiteSpace: 'pre-line'
                      }}>
                        {formatText(career)}
                      </div>
                    </div>
                  </>
                )}

                {activeTab === "dasa" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <Timeline size={18} color="#ef4444" />
                      Vimshottari Dasa Timeline
                    </h3>
                    {dasa && dasa.length > 0 ? (
                      <div style={{ overflowX: 'auto' }}>
                        <table style={{
                          width: '100%',
                          borderCollapse: 'collapse',
                          background: 'white',
                          borderRadius: '12px',
                          overflow: 'hidden',
                          boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
                        }}>
                          <thead>
                            <tr>
                              <th style={{
                                background: '#f1f5f9',
                                fontWeight: '600',
                                color: '#374151',
                                padding: '12px 16px',
                                textAlign: 'left',
                                borderBottom: '1px solid #e2e8f0',
                                fontSize: '0.9rem'
                              }}>Planet</th>
                              <th style={{
                                background: '#f1f5f9',
                                fontWeight: '600',
                                color: '#374151',
                                padding: '12px 16px',
                                textAlign: 'left',
                                borderBottom: '1px solid #e2e8f0',
                                fontSize: '0.9rem'
                              }}>Start Age</th>
                              <th style={{
                                background: '#f1f5f9',
                                fontWeight: '600',
                                color: '#374151',
                                padding: '12px 16px',
                                textAlign: 'left',
                                borderBottom: '1px solid #e2e8f0',
                                fontSize: '0.9rem'
                              }}>End Age</th>
                              <th style={{
                                background: '#f1f5f9',
                                fontWeight: '600',
                                color: '#374151',
                                padding: '12px 16px',
                                textAlign: 'left',
                                borderBottom: '1px solid #e2e8f0',
                                fontSize: '0.9rem'
                              }}>Duration (Years)</th>
                            </tr>
                          </thead>
                          <tbody>
                            {dasa.map((period, index) => (
                              <tr key={index} style={{
                                transition: 'background-color 0.2s ease'
                              }}>
                                <td style={{
                                  padding: '12px 16px',
                                  borderBottom: '1px solid #f1f5f9',
                                  color: '#4b5563',
                                  fontSize: '0.9rem',
                                  fontWeight: '600'
                                }}>{period.planet}</td>
                                <td style={{
                                  padding: '12px 16px',
                                  borderBottom: '1px solid #f1f5f9',
                                  color: '#4b5563',
                                  fontSize: '0.9rem'
                                }}>{period.start_age}</td>
                                <td style={{
                                  padding: '12px 16px',
                                  borderBottom: '1px solid #f1f5f9',
                                  color: '#4b5563',
                                  fontSize: '0.9rem'
                                }}>{period.end_age}</td>
                                <td style={{
                                  padding: '12px 16px',
                                  borderBottom: '1px solid #f1f5f9',
                                  color: '#4b5563',
                                  fontSize: '0.9rem'
                                }}>{period.years}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    ) : (
                      <p style={{color: '#64748b'}}>Loading Dasa timeline...</p>
                    )}
                  </>
                )}

                {activeTab === "yogas" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <Zap size={18} color="#f59e0b" />
                      Yogas & Doshas
                    </h3>
                    <div style={{
                      background: 'rgba(255, 255, 255, 0.9)',
                      borderRadius: '16px',
                      padding: '24px',
                      border: '1px solid rgba(245, 158, 11, 0.1)',
                      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)'
                    }}>
                      {yogas && yogas.length > 0 ? (
                        <ul style={{margin: 0, paddingLeft: '20px'}}>
                          {yogas.map((yoga, index) => (
                            <li key={index} style={{
                              color: '#374151',
                              lineHeight: '1.6',
                              fontSize: '1rem',
                              marginBottom: '12px'
                            }}>
                              {yoga}
                            </li>
                          ))}
                        </ul>
                      ) : (
                        <p style={{color: '#64748b', margin: 0}}>Loading yoga analysis...</p>
                      )}
                    </div>
                  </>
                )}

                {activeTab === "lifepurpose" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <Heart size={18} color="#ec4899" />
                      Life Purpose Analysis
                    </h3>
                    <div style={{
                      background: 'rgba(255, 255, 255, 0.9)',
                      borderRadius: '16px',
                      padding: '24px',
                      border: '1px solid rgba(236, 72, 153, 0.1)',
                      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)'
                    }}>
                      <div style={{
                        color: '#374151',
                        lineHeight: '1.6',
                        fontSize: '1rem',
                        margin: '0',
                        whiteSpace: 'pre-line'
                      }}>
                        {formatText(lifePurpose)}
                      </div>
                    </div>
                  </>
                )}

                {activeTab === "dasabhukti" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <Calendar size={18} color="#06b6d4" />
                      Dasa Bhukti Periods
                    </h3>
                    {dasaBhukti && dasaBhukti.length > 0 ? (
                      <div style={{ overflowX: 'auto' }}>
                        <table style={{
                          width: '100%',
                          borderCollapse: 'collapse',
                          background: 'white',
                          borderRadius: '12px',
                          overflow: 'hidden',
                          boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
                        }}>
                          <thead>
                            <tr>
                              <th style={{
                                background: '#f1f5f9',
                                fontWeight: '600',
                                color: '#374151',
                                padding: '12px 16px',
                                textAlign: 'left',
                                borderBottom: '1px solid #e2e8f0',
                                fontSize: '0.9rem'
                              }}>Period</th>
                              <th style={{
                                background: '#f1f5f9',
                                fontWeight: '600',
                                color: '#374151',
                                padding: '12px 16px',
                                textAlign: 'left',
                                borderBottom: '1px solid #e2e8f0',
                                fontSize: '0.9rem'
                              }}>Start</th>
                              <th style={{
                                background: '#f1f5f9',
                                fontWeight: '600',
                                color: '#374151',
                                padding: '12px 16px',
                                textAlign: 'left',
                                borderBottom: '1px solid #e2e8f0',
                                fontSize: '0.9rem'
                              }}>End</th>
                              <th style={{
                                background: '#f1f5f9',
                                fontWeight: '600',
                                color: '#374151',
                                padding: '12px 16px',
                                textAlign: 'left',
                                borderBottom: '1px solid #e2e8f0',
                                fontSize: '0.9rem'
                              }}>Duration</th>
                            </tr>
                          </thead>
                          <tbody>
                            {dasaBhukti.map((period, index) => (
                              <tr key={index} style={{
                                transition: 'background-color 0.2s ease'
                              }}>
                                <td style={{
                                  padding: '12px 16px',
                                  borderBottom: '1px solid #f1f5f9',
                                  color: '#4b5563',
                                  fontSize: '0.9rem',
                                  fontWeight: '600'
                                }}>
                                  {period.maha_dasa}-{period.bhukti || period.planet}
                                </td>
                                <td style={{
                                  padding: '12px 16px',
                                  borderBottom: '1px solid #f1f5f9',
                                  color: '#4b5563',
                                  fontSize: '0.9rem'
                                }}>{period.start}</td>
                                <td style={{
                                  padding: '12px 16px',
                                  borderBottom: '1px solid #f1f5f9',
                                  color: '#4b5563',
                                  fontSize: '0.9rem'
                                }}>{period.end}</td>
                                <td style={{
                                  padding: '12px 16px',
                                  borderBottom: '1px solid #f1f5f9',
                                  color: '#4b5563',
                                  fontSize: '0.9rem'
                                }}>{period.months || period.duration} {period.months ? 'months' : 'units'}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    ) : (
                      <p style={{color: '#64748b'}}>Loading Dasa Bhukti periods...</p>
                    )}
                  </>
                )}

                {activeTab === "spouse" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <Heart size={18} color="#f43f5e" />
                      Marriage & Spouse Analysis
                    </h3>
                    <div style={{
                      background: 'rgba(255, 255, 255, 0.9)',
                      borderRadius: '16px',
                      padding: '24px',
                      border: '1px solid rgba(244, 63, 94, 0.1)',
                      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)'
                    }}>
                      {spouseAnalysis && Object.keys(spouseAnalysis).length > 0 ? (
                        <div>
                          <div style={{
                            display: 'grid',
                            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                            gap: '16px',
                            marginBottom: '20px'
                          }}>
                            <div><strong>Gender:</strong> {spouseAnalysis.gender}</div>
                            <div><strong>Lagna:</strong> {spouseAnalysis.lagna}</div>
                            <div><strong>7th House:</strong> {spouseAnalysis['7th_house_sign']}</div>
                            <div><strong>7th Lord:</strong> {spouseAnalysis['7th_lord']}</div>
                            <div><strong>Direction:</strong> {spouseAnalysis.spouse_direction}</div>
                          </div>
                          {spouseAnalysis.report && (
                            <div style={{
                              color: '#374151',
                              lineHeight: '1.6',
                              fontSize: '1rem',
                              margin: '0',
                              whiteSpace: 'pre-line'
                            }}>
                              {formatText(spouseAnalysis.report)}
                            </div>
                          )}
                        </div>
                      ) : (
                        <p style={{color: '#64748b', margin: 0}}>Loading spouse analysis...</p>
                      )}
                    </div>
                  </>
                )}

                {activeTab === "wealth" && (
                  <>
                    <h3 style={{
                      fontSize: '1.25rem',
                      fontWeight: '600',
                      color: '#1f2937',
                      marginBottom: '20px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px'
                    }}>
                      <DollarSign size={18} color="#10b981" />
                      Wealth Cycles & Prosperity Periods
                    </h3>
                    {induDasa && Object.keys(induDasa).length > 0 ? (
                      <>
                        <div style={{
                          background: 'rgba(34, 197, 94, 0.05)',
                          borderRadius: '16px',
                          padding: '24px',
                          border: '1px solid rgba(34, 197, 94, 0.2)',
                          marginBottom: '20px'
                        }}>
                          <h4 style={{
                            fontSize: '1.1rem',
                            fontWeight: '700',
                            color: '#15803d',
                            marginBottom: '20px',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '8px'
                          }}>
                            💰 Indu Lagnam Analysis
                          </h4>
                          <div style={{
                            display: 'grid',
                            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                            gap: '16px',
                            marginBottom: '20px'
                          }}>
                            <div style={{
                              display: 'flex',
                              justifyContent: 'space-between',
                              alignItems: 'center',
                              padding: '8px 0',
                              borderBottom: '1px solid rgba(34, 197, 94, 0.1)'
                            }}>
                              <span style={{fontWeight: '600', color: '#374151'}}>Ascendant:</span>
                              <span style={{color: '#15803d', fontWeight: '500'}}>{induDasa.ascendant}</span>
                            </div>
                            <div style={{
                              display: 'flex',
                              justifyContent: 'space-between',
                              alignItems: 'center',
                              padding: '8px 0',
                              borderBottom: '1px solid rgba(34, 197, 94, 0.1)'
                            }}>
                              <span style={{fontWeight: '600', color: '#374151'}}>Moon Rasi:</span>
                              <span style={{color: '#15803d', fontWeight: '500'}}>{induDasa.moon_rasi}</span>
                            </div>
                            <div style={{
                              display: 'flex',
                              justifyContent: 'space-between',
                              alignItems: 'center',
                              padding: '8px 0',
                              borderBottom: '1px solid rgba(34, 197, 94, 0.1)'
                            }}>
                              <span style={{fontWeight: '600', color: '#374151'}}>Indu Lagnam:</span>
                              <span style={{color: '#15803d', fontWeight: '500'}}>{induDasa.indu_lagnam}</span>
                            </div>
                            <div style={{
                              display: 'flex',
                              justifyContent: 'space-between',
                              alignItems: 'center',
                              padding: '8px 0',
                              borderBottom: '1px solid rgba(34, 197, 94, 0.1)'
                            }}>
                              <span style={{fontWeight: '600', color: '#374151'}}>Indu Lord:</span>
                              <span style={{color: '#15803d', fontWeight: '500'}}>{induDasa.indu_lord}</span>
                            </div>
                          </div>

                          {induDasa.planets_in_indu_lagnam && induDasa.planets_in_indu_lagnam.length > 0 && (
                            <div style={{
                              background: 'rgba(255, 255, 255, 0.9)',
                              borderRadius: '12px',
                              padding: '16px',
                              border: '1px solid rgba(34, 197, 94, 0.3)',
                              marginBottom: '20px'
                            }}>
                              <h5 style={{
                                fontSize: '1rem',
                                fontWeight: '600',
                                color: '#15803d',
                                marginBottom: '12px',
                                display: 'flex',
                                alignItems: 'center',
                                gap: '8px'
                              }}>
                                🌟 Planets in Indu Lagnam
                              </h5>
                              <div style={{
                                display: 'flex',
                                flexWrap: 'wrap',
                                gap: '8px'
                              }}>
                                {induDasa.planets_in_indu_lagnam.map((planet, index) => (
                                  <span key={index} style={{
                                    background: 'linear-gradient(135deg, #fbbf24, #f59e0b)',
                                    color: 'white',
                                    padding: '6px 12px',
                                    borderRadius: '20px',
                                    fontSize: '0.85rem',
                                    fontWeight: '500',
                                    boxShadow: '0 2px 4px rgba(245, 158, 11, 0.3)'
                                  }}>
                                    {planet}
                                  </span>
                                ))}
                              </div>
                            </div>
                          )}
                        </div>

                        {induDasa.timeline && induDasa.timeline.length > 0 && (
                          <div style={{
                            background: 'rgba(34, 197, 94, 0.05)',
                            borderRadius: '16px',
                            padding: '24px',
                            border: '1px solid rgba(34, 197, 94, 0.2)'
                          }}>
                            <h4 style={{
                              fontSize: '1.1rem',
                              fontWeight: '700',
                              color: '#15803d',
                              marginBottom: '20px',
                              display: 'flex',
                              alignItems: 'center',
                              gap: '8px'
                            }}>
                              ⏰ Wealth & Prosperity Timeline
                            </h4>
                            <div style={{
                              display: 'grid',
                              gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
                              gap: '16px'
                            }}>
                              {induDasa.timeline.map((period, index) => (
                                <div key={index} style={{
                                  background: 'rgba(255, 255, 255, 0.9)',
                                  borderRadius: '12px',
                                  padding: '16px',
                                  border: '1px solid rgba(34, 197, 94, 0.3)',
                                  transition: 'all 0.3s ease',
                                  cursor: 'pointer'
                                }}>
                                  <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: '8px',
                                    marginBottom: '8px'
                                  }}>
                                    <div style={{
                                      fontSize: '1rem',
                                      fontWeight: '700',
                                      color: '#15803d'
                                    }}>{period.maha_dasa}</div>
                                    <div style={{
                                      fontSize: '0.9rem',
                                      color: '#16a34a',
                                      fontWeight: '500'
                                    }}>• {period.bukti}</div>
                                  </div>
                                  <div style={{
                                    fontSize: '0.85rem',
                                    color: '#6b7280',
                                    marginBottom: '4px'
                                  }}>
                                    {period.start} to {period.end}
                                  </div>
                                  <div style={{
                                    fontSize: '0.8rem',
                                    color: '#15803d',
                                    fontWeight: '600',
                                    background: 'rgba(34, 197, 94, 0.1)',
                                    padding: '2px 8px',
                                    borderRadius: '12px',
                                    display: 'inline-block'
                                  }}>
                                    {Math.round(((new Date(period.end) - new Date(period.start)) / (365.25 * 24 * 60 * 60 * 1000)) * 10) / 10} years
                                  </div>
                                </div>
                              ))}
                            </div>
                          </div>
                        )}
                      </>
                    ) : (
                      <p style={{color: '#64748b', margin: 0}}>Loading wealth analysis...</p>
                    )}
                  </>
                )}
              </div>
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