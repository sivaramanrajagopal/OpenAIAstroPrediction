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

const Calendar2 = ({ size = 16, color = "currentColor" }) => (
  <svg width={size} height={size} fill="none" stroke={color} viewBox="0 0 24 24" strokeWidth="2" style={{ display: 'inline-block', verticalAlign: 'middle' }}>
    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
    <line x1="16" y1="2" x2="16" y2="6"/>
    <line x1="8" y1="2" x2="8" y2="6"/>
    <line x1="3" y1="10" x2="21" y2="10"/>
    <path d="M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01M16 18h.01"/>
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
    dob: "",
    tob: "",
    lat: "",
    lon: "",
    tz_offset: "5.5",
    gender: "Male",
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [activeTab, setActiveTab] = useState("chart");
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

  const getPrediction = async () => {
    setLoading(true);
    try {
      // Test backend connection first
      const healthCheck = await fetch(`${backend}/health`).then(res => res.json());
      
      if (healthCheck.status === "healthy") {
        // Get predictions from backend
        const chartRes = await fetch(`${backend}/predict?${new URLSearchParams({ ...formData })}`).then(res => res.json());
        
        setResult({
          chart: {
            Sun: { rasi: "Gemini", nakshatra: "Punarvasu", pada: "1" },
            Moon: { rasi: "Scorpio", nakshatra: "Anuradha", pada: "3" },
            Mars: { rasi: "Leo", nakshatra: "Magha", pada: "2" },
            Mercury: { rasi: "Gemini", nakshatra: "Ardra", pada: "4" },
            Jupiter: { rasi: "Pisces", nakshatra: "Revati", pada: "1" },
            Venus: { rasi: "Taurus", nakshatra: "Rohini", pada: "2" },
            Saturn: { rasi: "Aquarius", nakshatra: "Dhanishta", pada: "3" },
            Rahu: { rasi: "Aries", nakshatra: "Bharani", pada: "1" },
            Ketu: { rasi: "Libra", nakshatra: "Chitra", pada: "4" }
          },
          interpretation: chartRes.message || "Backend is online! Full astrological calculations are coming soon. The Swiss Ephemeris integration is in progress to provide accurate planetary positions and detailed cosmic interpretations."
        });
        
        // Set demo data for other features
        setCareer("Career analysis feature is coming soon! This will include professional strengths, ideal career paths, and timing for career changes.");
        setDasa([]);
        setYogas(["Demo Yoga: This is where detected yogas will appear"]);
        setLifePurpose("Life purpose analysis is coming soon! This will reveal your soul's journey and spiritual path.");
        setDasaBhukti([]);
        setSpouseAnalysis({ gender: "Coming soon", lagna: "Coming soon" });
        setInduDasa({ indu_lagnam: "Coming soon" });
      } else {
        throw new Error("Backend not available");
      }
    } catch (error) {
      console.error('Error:', error);
      // Provide fully functional demo experience
      setResult({
        chart: {
          Sun: { rasi: "Gemini", nakshatra: "Punarvasu", pada: "1" },
          Moon: { rasi: "Scorpio", nakshatra: "Anuradha", pada: "3" },
          Mars: { rasi: "Leo", nakshatra: "Magha", pada: "2" },
          Mercury: { rasi: "Gemini", nakshatra: "Ardra", pada: "4" },
          Jupiter: { rasi: "Pisces", nakshatra: "Revati", pada: "1" },
          Venus: { rasi: "Taurus", nakshatra: "Rohini", pada: "2" },
          Saturn: { rasi: "Aquarius", nakshatra: "Dhanishta", pada: "3" },
          Rahu: { rasi: "Aries", nakshatra: "Bharani", pada: "1" },
          Ketu: { rasi: "Libra", nakshatra: "Chitra", pada: "4" }
        },
        interpretation: "🌟 Welcome to your Vedic Astrology Analysis! This is a demo showing the beautiful interface and features. The backend calculation engine is being deployed. Your planetary positions above show a sample birth chart with the Sun in Gemini (communication, versatility) and Moon in Scorpio (emotional depth, transformation). This combination suggests a person with great communicative abilities and deep emotional intelligence."
      });
      
      // Set meaningful demo data
      setCareer("🎯 CAREER ANALYSIS DEMO: Your chart suggests strong potential in technology, communication, and creative fields. The Sun in Gemini indicates excellent writing and teaching abilities, while the Moon in Scorpio gives you research and analytical skills. Best career periods: Age 28-32 and 35-40.");
      setDasa([
        { planet: "Sun", start_age: 25, end_age: 31, start_date: "2024-01-01", end_date: "2030-01-01" },
        { planet: "Moon", start_age: 31, end_age: 41, start_date: "2030-01-01", end_date: "2040-01-01" }
      ]);
      setYogas([
        "Gaja Kesari Yoga: Jupiter and Moon connection brings wisdom and prosperity",
        "Budh Aditya Yoga: Sun-Mercury conjunction enhances intelligence and communication",
        "Raja Yoga: Combination of benefic planets in kendras brings leadership qualities"
      ]);
      setLifePurpose("🌟 LIFE PURPOSE DEMO: Your soul's journey involves bridging communication and transformation. With Sun in Gemini and Moon in Scorpio, you're meant to help others through teaching, writing, or healing. Your Atmakaraka suggests spiritual growth through service to others.");
      setDasaBhukti([
        { planet: "Mercury-Venus", start: "2024-03-01", end: "2024-09-01", duration: 6 },
        { planet: "Mercury-Sun", start: "2024-09-01", end: "2025-01-01", duration: 4 }
      ]);
      setSpouseAnalysis({ 
        gender: "Compatible", 
        lagna: "Libra", 
        "7th_house_sign": "Sagittarius",
        "7th_lord": "Jupiter",
        spouse_direction: "North-East"
      });
      setInduDasa({ 
        indu_lagnam: "Taurus",
        indu_lord: "Venus",
        planets_in_indu_lagnam: ["Venus", "Mercury"]
      });
    } finally {
      setLoading(false);
    }
  };

  const tabs = [
    { key: "chart", label: "Planetary Chart", icon: Sun },
    { key: "prediction", label: "Predictions", icon: Moon },
    { key: "career", label: "Career Insights", icon: Briefcase },
    { key: "dasa", label: "Dasa Timeline", icon: Timeline },
    { key: "dasabhukti", label: "Dasa Bhukti", icon: Calendar2 },
    { key: "yogas", label: "Yogas & Doshas", icon: Zap },
    { key: "lifepurpose", label: "Life Purpose", icon: Heart },
    { key: "spouse", label: "Spouse Analysis", icon: Heart },
    { key: "wealth", label: "Wealth Cycles", icon: DollarSign },
  ];

  const styles = {
    container: {
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #fefce8, #fef3c7, #fed7aa)',
      padding: '20px',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      position: 'relative'
    },
    backgroundOrb1: {
      position: 'fixed',
      top: '-160px',
      right: '-160px',
      width: '320px',
      height: '320px',
      background: 'radial-gradient(circle, rgba(251, 191, 36, 0.3), rgba(245, 158, 11, 0.3))',
      borderRadius: '50%',
      filter: 'blur(60px)',
      pointerEvents: 'none',
      zIndex: 0
    },
    backgroundOrb2: {
      position: 'fixed',
      bottom: '-160px',
      left: '-160px',
      width: '320px',
      height: '320px',
      background: 'radial-gradient(circle, rgba(245, 158, 11, 0.3), rgba(217, 119, 6, 0.3))',
      borderRadius: '50%',
      filter: 'blur(60px)',
      pointerEvents: 'none',
      zIndex: 0
    },
    mainContainer: {
      maxWidth: '1200px',
      margin: '0 auto',
      position: 'relative',
      zIndex: 1
    },
    header: {
      textAlign: 'center',
      marginBottom: '40px'
    },
    logoContainer: {
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      width: '60px',
      height: '60px',
      background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
      borderRadius: '50%',
      marginBottom: '16px',
      boxShadow: '0 10px 25px rgba(99, 102, 241, 0.3)'
    },
    title: {
      fontSize: '3rem',
      fontWeight: 'bold',
      background: 'linear-gradient(135deg, #4f46e5, #7c3aed)',
      WebkitBackgroundClip: 'text',
      WebkitTextFillColor: 'transparent',
      backgroundClip: 'text',
      marginBottom: '8px',
      margin: '0 0 8px 0'
    },
    subtitle: {
      color: '#64748b',
      fontSize: '1.125rem',
      maxWidth: '600px',
      margin: '0 auto'
    },
    card: {
      background: 'rgba(255, 255, 255, 0.9)',
      backdropFilter: 'blur(20px)',
      borderRadius: '24px',
      boxShadow: '0 25px 50px rgba(0, 0, 0, 0.1)',
      border: '1px solid rgba(255, 255, 255, 0.2)',
      overflow: 'hidden'
    },
    cardContent: {
      padding: '40px'
    },
    sectionHeader: {
      fontSize: '1.5rem',
      fontWeight: '600',
      color: '#1e293b',
      marginBottom: '24px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    formGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
      gap: '24px',
      marginBottom: '32px'
    },
    inputGroup: {
      display: 'flex',
      flexDirection: 'column',
      gap: '8px'
    },
    label: {
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      fontSize: '0.875rem',
      fontWeight: '500',
      color: '#374151'
    },
    input: {
      width: '100%',
      padding: '12px 16px',
      borderRadius: '12px',
      border: '1px solid #d1d5db',
      background: 'rgba(255, 255, 255, 0.7)',
      fontSize: '1rem',
      transition: 'all 0.3s ease',
      outline: 'none',
      boxSizing: 'border-box'
    },
    button: {
      width: '100%',
      padding: '16px 24px',
      background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
      color: 'white',
      border: 'none',
      borderRadius: '12px',
      fontSize: '1rem',
      fontWeight: '600',
      cursor: 'pointer',
      transition: 'all 0.3s ease',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      gap: '8px',
      boxShadow: '0 4px 15px rgba(99, 102, 241, 0.4)'
    },
    buttonDisabled: {
      opacity: 0.5,
      cursor: 'not-allowed'
    },
    spinner: {
      width: '20px',
      height: '20px',
      border: '2px solid rgba(255, 255, 255, 0.3)',
      borderTop: '2px solid white',
      borderRadius: '50%',
      animation: 'spin 1s linear infinite'
    },
    tabContainer: {
      borderTop: '1px solid #e2e8f0',
      padding: '32px 40px'
    },
    tabButtons: {
      display: 'flex',
      gap: '8px',
      marginBottom: '24px',
      flexWrap: 'wrap',
      overflowX: 'auto',
      padding: '4px'
    },
    tabButton: {
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
      minWidth: 'fit-content'
    },
    tabButtonActive: {
      background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
      color: 'white',
      boxShadow: '0 4px 15px rgba(99, 102, 241, 0.4)',
      transform: 'scale(1.02)'
    },
    tabButtonInactive: {
      background: 'rgba(255, 255, 255, 0.7)',
      color: '#64748b',
      backdropFilter: 'blur(10px)'
    },
    tabContent: {
      background: 'linear-gradient(135deg, #f8fafc, rgba(99, 102, 241, 0.05))',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid #e2e8f0',
      minHeight: '400px'
    },
    tabHeader: {
      fontSize: '1.25rem',
      fontWeight: '600',
      color: '#1e293b',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    table: {
      width: '100%',
      borderCollapse: 'collapse',
      background: 'white',
      borderRadius: '12px',
      overflow: 'hidden',
      boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
    },
    tableHeader: {
      background: '#f1f5f9',
      fontWeight: '600',
      color: '#374151',
      padding: '12px 16px',
      textAlign: 'left',
      borderBottom: '1px solid #e2e8f0',
      fontSize: '0.9rem'
    },
    tableCell: {
      padding: '12px 16px',
      borderBottom: '1px solid #f1f5f9',
      color: '#4b5563',
      fontSize: '0.9rem'
    },
    tableRow: {
      transition: 'background-color 0.2s ease'
    },
    footer: {
      textAlign: 'center',
      marginTop: '32px',
      color: '#94a3b8',
      fontSize: '0.875rem'
    },
  };

  return (
    <>
      <style jsx>{`
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>

      <div style={styles.container}>
        <div style={styles.backgroundOrb1}></div>
        <div style={styles.backgroundOrb2}></div>

        <div style={styles.mainContainer}>
          <div style={styles.header}>
            <div style={styles.logoContainer}>
              <Star size={24} color="white" />
            </div>
            <h1 style={styles.title}>Vedic Astrology</h1>
            <p style={styles.subtitle}>
              Comprehensive cosmic insights through ancient Vedic wisdom
            </p>
          </div>

          <div style={styles.card}>
            <div style={styles.cardContent}>
              <h2 style={styles.sectionHeader}>
                <Sparkles size={20} color="#6366f1" />
                Birth Details
              </h2>

              <div style={styles.formGrid}>
                <div style={styles.inputGroup}>
                  <label style={styles.label}>
                    <Calendar size={16} color="#6366f1" />
                    Date of Birth
                  </label>
                  <input
                    type="date"
                    style={styles.input}
                    value={formData.dob}
                    onChange={(e) => setFormData({ ...formData, dob: e.target.value })}
                  />
                </div>

                <div style={styles.inputGroup}>
                  <label style={styles.label}>
                    <Clock size={16} color="#6366f1" />
                    Time of Birth
                  </label>
                  <input
                    type="time"
                    style={styles.input}
                    value={formData.tob}
                    onChange={(e) => setFormData({ ...formData, tob: e.target.value })}
                  />
                </div>

                <div style={styles.inputGroup}>
                  <label style={styles.label}>
                    <MapPin size={16} color="#6366f1" />
                    Latitude
                  </label>
                  <input
                    type="text"
                    placeholder="e.g., 13.08"
                    style={styles.input}
                    value={formData.lat}
                    onChange={(e) => setFormData({ ...formData, lat: e.target.value })}
                  />
                </div>

                <div style={styles.inputGroup}>
                  <label style={styles.label}>
                    <MapPin size={16} color="#6366f1" />
                    Longitude
                  </label>
                  <input
                    type="text"
                    placeholder="e.g., 80.28"
                    style={styles.input}
                    value={formData.lon}
                    onChange={(e) => setFormData({ ...formData, lon: e.target.value })}
                  />
                </div>
              </div>

              <button
                onClick={getPrediction}
                disabled={loading}
                style={{
                  ...styles.button,
                  ...(loading ? styles.buttonDisabled : {})
                }}
              >
                {loading ? (
                  <>
                    <div style={styles.spinner}></div>
                    Calculating Cosmic Alignments...
                  </>
                ) : (
                  <>
                    <Star size={20} color="white" />
                    Generate Complete Analysis
                  </>
                )}
              </button>
            </div>

            {result && (
              <div style={styles.tabContainer}>
                <div style={styles.tabButtons}>
                  {tabs.map((tab) => (
                    <button
                      key={tab.key}
                      onClick={() => setActiveTab(tab.key)}
                      style={{
                        ...styles.tabButton,
                        ...(activeTab === tab.key ? styles.tabButtonActive : styles.tabButtonInactive)
                      }}
                    >
                      <tab.icon size={16} color={activeTab === tab.key ? "white" : "#64748b"} />
                      {tab.label}
                    </button>
                  ))}
                </div>

                <div style={styles.tabContent}>
                  {activeTab === "chart" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <Sun size={18} color="#f59e0b" />
                        Planetary Positions
                      </h3>
                      <div style={{ overflowX: 'auto' }}>
                        <table style={styles.table}>
                          <thead>
                            <tr>
                              <th style={styles.tableHeader}>Planet</th>
                              <th style={styles.tableHeader}>Rasi</th>
                              <th style={styles.tableHeader}>Nakshatra</th>
                              <th style={styles.tableHeader}>Pada</th>
                            </tr>
                          </thead>
                          <tbody>
                            {Object.entries(result.chart).map(([planet, info]) => (
                              <tr key={planet} style={styles.tableRow}>
                                <td style={{...styles.tableCell, fontWeight: '600'}}>{planet}</td>
                                <td style={styles.tableCell}>{info.rasi}</td>
                                <td style={styles.tableCell}>{info.nakshatra}</td>
                                <td style={styles.tableCell}>{info.pada}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </>
                  )}

                  {activeTab === "prediction" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <Moon size={18} color="#6366f1" />
                        Cosmic Interpretation
                      </h3>
                      <div style={{
                        background: 'rgba(255, 255, 255, 0.9)',
                        borderRadius: '16px',
                        padding: '24px',
                        border: '1px solid rgba(99, 102, 241, 0.1)',
                        boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)'
                      }}>
                        <p style={{
                          color: '#374151',
                          lineHeight: '1.6',
                          fontSize: '1rem',
                          margin: '0',
                          whiteSpace: 'pre-line'
                        }}>
                          {result.interpretation}
                        </p>
                      </div>
                    </>
                  )}
                </div>
              </div>
            )}
          </div>

          <div style={styles.footer}>
            <p>Powered by ancient Vedic wisdom and modern technology</p>
          </div>
        </div>
      </div>
    </>
  );
}