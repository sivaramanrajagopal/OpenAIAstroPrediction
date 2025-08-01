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
  const [activeTab, setActiveTab] = useState("predict");

  // TODO: Update this URL for production deployment
  // For Railway: https://your-backend-name.railway.app
  // For local development: http://localhost:8000
  const backend = "http://localhost:8000";

  const getPrediction = async () => {
    setLoading(true);
    try {
      const [chartRes, careerRes, dasaRes, yogaRes, lifePurposeRes, dasaBhuktiRes, spouseRes, induDasaRes] = await Promise.all([
        fetch(`${backend}/predict?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
        fetch(`${backend}/career?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
        fetch(`${backend}/dasa?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
        fetch(`${backend}/yogas?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
        fetch(`${backend}/life_purpose?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
        fetch(`${backend}/dasa_bhukti?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
        fetch(`${backend}/spouse?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
        fetch(`${backend}/indu_dasa?${new URLSearchParams({ ...formData })}`).then(res => res.json()),
      ]);

      setResult(chartRes);
      setCareer(careerRes.career_report);
      setDasa(dasaRes.dasa_table);
      setYogas(yogaRes.yogas);
      setLifePurpose(lifePurposeRes);
      setDasaBhukti(dasaBhuktiRes);
      setSpouseAnalysis(spouseRes);
      setInduDasa(induDasaRes);
    } catch (error) {
      console.error('Error:', error);
      alert("Error fetching data. Please try again.");
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

  const formatText = (text) => {
    if (!text) return null;

    // Special handling for career insights with structured data
    if (text.includes('Advanced Career Analysis') || text.includes('Career Significator Planets')) {
      return formatCareerInsights(text);
    }

    // Special handling for cosmic interpretation with numbered sections
    if (text.includes('**1. Personality**') || text.includes('**2. Career**') || 
        text.includes('**3. Relationships**') || text.includes('**4. Remedies**')) {
      return formatCosmicInterpretation(text);
    }

    // Special handling for life purpose analysis
    if (text.includes('Life Purpose Analysis') || text.includes('Atmakaraka') || text.includes('Amatyakaraka')) {
      return formatLifePurpose(text);
    }

    // Special handling for dasa bhukti analysis - check for the specific format
    if (text.includes('Key Life Periods and Transitions') || text.includes('Career, Health, Relationships') || 
        text.includes('Spiritual Guidance and Remedies') || text.includes('Mercury Dasa') || text.includes('Interpretation:')) {
      return formatDasaBhukti(text);
    }

    const sections = text.split('###').filter(section => section.trim());

    if (sections.length <= 1) {
      return (
        <div style={styles.simpleTextContainer}>
          <p style={styles.simpleText}>{text}</p>
        </div>
      );
    }

    return (
      <div style={styles.interpretationContainer}>
        {sections.map((section, index) => {
          const lines = section.trim().split('\n').filter(line => line.trim());
          const title = lines[0]?.trim();
          const content = lines.slice(1);

          if (!title) return null;

          return (
            <div key={index} style={styles.sectionCard}>
              <h4 style={styles.sectionTitle}>{title}</h4>
              <div style={styles.sectionContent}>
                {content.map((line, lineIndex) => {
                  const trimmedLine = line.trim();
                  if (!trimmedLine) return null;

                  if (trimmedLine.startsWith('- **')) {
                    const match = trimmedLine.match(/- \*\*(.*?)\*\*:(.*)/);
                    if (match) {
                      return (
                        <div key={lineIndex} style={styles.bulletPoint}>
                          <div style={styles.bulletHeader}>
                            <div style={styles.bulletDot}></div>
                            <span style={styles.bulletTitle}>{match[1]}</span>
                          </div>
                          <div style={styles.bulletDescription}>
                            {match[2].trim()}
                          </div>
                        </div>
                      );
                    }
                  }

                  return (
                    <p key={lineIndex} style={styles.paragraph}>
                      {trimmedLine}
                    </p>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    );
  };

  const formatDasaBhukti = (text) => {
    const lines = text.split('\n').filter(line => line.trim());
    const sections = [];
    let currentSection = null;

    lines.forEach(line => {
      const trimmed = line.trim();
      if (!trimmed) return;

      // Skip "Interpretation:" header
      if (trimmed === 'Interpretation:') return;

      // Check for numbered sections like "1. Key Life Periods and Transitions:"
      const sectionMatch = trimmed.match(/^(\d+)\.\s*(.+):/);
      if (sectionMatch) {
        if (currentSection) sections.push(currentSection);
        currentSection = {
          number: sectionMatch[1],
          title: sectionMatch[2].trim(),
          content: []
        };
      }
      // Check for dasa period descriptions
      else if (trimmed.includes('Dasa') && (trimmed.includes('from') || trimmed.includes('lasted') || trimmed.includes('brings') || trimmed.includes('usually'))) {
        if (currentSection) {
          currentSection.content.push({
            type: 'dasa_period',
            text: trimmed
          });
        }
      }
      // Regular content
      else if (currentSection && trimmed.length > 10) {
        currentSection.content.push({
          type: 'text',
          text: trimmed
        });
      }
    });

    if (currentSection) sections.push(currentSection);

    const getSectionIcon = (title) => {
      if (title.toLowerCase().includes('life periods') || title.toLowerCase().includes('transitions')) return '🌅';
      if (title.toLowerCase().includes('career') || title.toLowerCase().includes('health') || title.toLowerCase().includes('relationships')) return '🏥';
      if (title.toLowerCase().includes('spiritual') || title.toLowerCase().includes('guidance') || title.toLowerCase().includes('remedies')) return '🙏';
      return '⏰';
    };

    const getSectionColor = (title) => {
      if (title.toLowerCase().includes('life periods') || title.toLowerCase().includes('transitions')) return '#8b5cf6';
      if (title.toLowerCase().includes('career') || title.toLowerCase().includes('health') || title.toLowerCase().includes('relationships')) return '#059669';
      if (title.toLowerCase().includes('spiritual') || title.toLowerCase().includes('guidance') || title.toLowerCase().includes('remedies')) return '#d97706';
      return '#6366f1';
    };

    return (
      <div style={styles.dasaBhuktiContainer}>
        {sections.map((section, index) => {
          const sectionColor = getSectionColor(section.title);
          const sectionIcon = getSectionIcon(section.title);

          return (
            <div key={index} style={{
              ...styles.dasaBhuktiSection,
              borderLeft: `4px solid ${sectionColor}`
            }}>
              <h4 style={{
                ...styles.dasaBhuktiSectionTitle,
                color: sectionColor
              }}>
                <span style={styles.dasaBhuktiIcon}>{sectionIcon}</span>
                <span style={styles.dasaBhuktiNumber}>{section.number}.</span>
                {section.title}
              </h4>

              <div style={styles.dasaBhuktiContent}>
                {section.content.map((item, itemIndex) => {
                  if (item.type === 'dasa_period') {
                    return (
                      <div key={itemIndex} style={styles.dasaPeriod}>
                        <div style={styles.dasaPeriodText}>
                          {item.text}
                        </div>
                      </div>
                    );
                  } else {
                    return (
                      <p key={itemIndex} style={styles.dasaBhuktiText}>
                        {item.text}
                      </p>
                    );
                  }
                })}
              </div>
            </div>
          );
        })}
      </div>
    );
  };

  const formatLifePurpose = (text) => {
    const lines = text.split('\n').filter(line => line.trim());
    const sections = [];
    let currentSection = null;
    let titleText = '';

    lines.forEach(line => {
      const trimmed = line.trim();
      if (!trimmed) return;

      // Check for main title
      if (trimmed.includes('🌟 Life Purpose Analysis')) {
        titleText = trimmed;
      }
      // Check for key astrological components
      else if (trimmed.includes('Ascendant:') || 
               trimmed.includes('Moon Sign:') || 
               trimmed.includes('Sun Sign:') || 
               trimmed.includes('Atmakaraka:') || 
               trimmed.includes('Amatyakaraka:')) {

        const parts = trimmed.split(' - ');
        const header = parts[0].trim();
        const description = parts.length > 1 ? parts.slice(1).join(' - ').trim() : '';

        sections.push({
          type: 'component',
          header: header,
          description: description
        });
      }
      // Check for overall summary
      else if (trimmed.toLowerCase().includes('overall')) {
        sections.push({
          type: 'summary',
          text: trimmed
        });
      }
      // Regular content
      else if (trimmed.length > 20) {
        sections.push({
          type: 'text',
          text: trimmed
        });
      }
    });

    const getComponentIcon = (header) => {
      if (header.includes('Ascendant')) return '🌅';
      if (header.includes('Moon Sign')) return '🌙';
      if (header.includes('Sun Sign')) return '☀️';
      if (header.includes('Atmakaraka')) return '✨';
      if (header.includes('Amatyakaraka')) return '💼';
      return '⭐';
    };

    const getComponentColor = (header) => {
      if (header.includes('Ascendant')) return '#f59e0b';
      if (header.includes('Moon Sign')) return '#6366f1';
      if (header.includes('Sun Sign')) return '#dc2626';
      if (header.includes('Atmakaraka')) return '#8b5cf6';
      if (header.includes('Amatyakaraka')) return '#059669';
      return '#64748b';
    };

    return (
      <div style={styles.lifePurposeContainer}>
        <div style={styles.lifePurposeTitle}>
          <Heart size={20} color="#e11d48" />
          {titleText.replace(/🌟/g, '').trim()}
        </div>

        <div style={styles.lifePurposeGrid}>
          {sections.filter(s => s.type === 'component').map((section, index) => {
            const componentColor = getComponentColor(section.header);
            const componentIcon = getComponentIcon(section.header);

            return (
              <div key={index} style={{
                ...styles.lifePurposeCard,
                borderTop: `4px solid ${componentColor}`
              }}>
                <div style={styles.lifePurposeCardHeader}>
                  <span style={styles.lifePurposeIcon}>{componentIcon}</span>
                  <span style={{
                    ...styles.lifePurposeCardTitle,
                    color: componentColor
                  }}>
                    {section.header}
                  </span>
                </div>
                {section.description && (
                  <div style={styles.lifePurposeCardDescription}>
                    {section.description}
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {sections.filter(s => s.type === 'text' || s.type === 'summary').map((section, index) => (
          <div key={index} style={styles.lifePurposeSummary}>
            <p style={styles.lifePurposeSummaryText}>
              {section.text}
            </p>
          </div>
        ))}
      </div>
    );
  };

  const formatCosmicInterpretation = (text) => {
    const lines = text.split('\n').filter(line => line.trim());
    const sections = [];
    let currentSection = null;
    let introText = [];

    lines.forEach(line => {
      const trimmed = line.trim();
      if (!trimmed) return;

      // Check for numbered section headers like **1. Personality**
      const sectionMatch = trimmed.match(/\*\*(\d+)\.\s*([^*]+)\*\*/);
      if (sectionMatch) {
        if (currentSection) sections.push(currentSection);
        currentSection = { 
          number: sectionMatch[1], 
          title: sectionMatch[2].trim(), 
          content: [] 
        };
      }
      // Check for bullet points with astrological data
      else if (trimmed.startsWith('- **') && trimmed.includes(':**')) {
        const bulletMatch = trimmed.match(/- \*\*(.*?)\*\*:(.*)/);
        if (bulletMatch && currentSection) {
          currentSection.content.push({
            type: 'astrological',
            placement: bulletMatch[1].trim(),
            interpretation: bulletMatch[2].trim()
          });
        }
      }
      // Regular content
      else if (currentSection) {
        currentSection.content.push({ type: 'text', text: trimmed.replace(/\*\*/g, '') });
      } else {
        // Intro text before sections
        introText.push(trimmed.replace(/\*\*/g, ''));
      }
    });

    if (currentSection) sections.push(currentSection);

    const getSectionIcon = (title) => {
      if (title.toLowerCase().includes('personality')) return '👤';
      if (title.toLowerCase().includes('career')) return '💼';
      if (title.toLowerCase().includes('relationship')) return '💕';
      if (title.toLowerCase().includes('remedies')) return '🕉️';
      return '⭐';
    };

    const getSectionColor = (title) => {
      if (title.toLowerCase().includes('personality')) return '#8b5cf6';
      if (title.toLowerCase().includes('career')) return '#059669';
      if (title.toLowerCase().includes('relationship')) return '#dc2626';
      if (title.toLowerCase().includes('remedies')) return '#d97706';
      return '#6366f1';
    };

    return (
      <div style={styles.cosmicContainer}>
        {introText.length > 0 && (
          <div style={styles.cosmicIntro}>
            {introText.map((text, index) => (
              <p key={index} style={styles.cosmicIntroText}>
                {text}
              </p>
            ))}
          </div>
        )}

        {sections.map((section, index) => {
          const sectionColor = getSectionColor(section.title);
          const sectionIcon = getSectionIcon(section.title);

          return (
            <div key={index} style={{
              ...styles.cosmicSection,
              borderLeft: `4px solid ${sectionColor}`
            }}>
              <h4 style={{
                ...styles.cosmicSectionTitle,
                color: sectionColor
              }}>
                <span style={styles.cosmicSectionIcon}>{sectionIcon}</span>
                <span style={styles.cosmicSectionNumber}>{section.number}.</span>
                {section.title}
              </h4>

              <div style={styles.cosmicContent}>
                {section.content.map((item, itemIndex) => {
                  if (item.type === 'astrological') {
                    return (
                      <div key={itemIndex} style={styles.astrologicalPoint}>
                        <div style={styles.astrologicalHeader}>
                          <div style={{
                            ...styles.astrologicalDot,
                            background: sectionColor
                          }}></div>
                          <span style={styles.astrologicalPlacement}>
                            {item.placement}
                          </span>
                        </div>
                        <div style={styles.astrologicalInterpretation}>
                          {item.interpretation}
                        </div>
                      </div>
                    );
                  } else {
                    return (
                      <p key={itemIndex} style={styles.cosmicText}>
                        {item.text}
                      </p>
                    );
                  }
                })}
              </div>
            </div>
          );
        })}
      </div>
    );
  };

  const formatCareerInsights = (text) => {
    const lines = text.split('\n').filter(line => line.trim());
    const sections = [];
    let currentSection = null;

    lines.forEach(line => {
      const trimmed = line.trim();
      if (!trimmed) return;

      // Check for main headers
      if (trimmed.includes('Advanced Career Analysis') || 
          trimmed.includes('General Career Tendencies') ||
          trimmed.includes('Key Career Houses Analysis') ||
          trimmed.includes('Career Significator Planets')) {
        if (currentSection) sections.push(currentSection);
        currentSection = { title: trimmed.replace(/💼|🏢|📊|⭐/g, '').trim(), content: [] };
      }
      // Check for sub-headers (house analysis)
      else if (trimmed.includes('House (Sign:') || trimmed.includes('House (') || trimmed.match(/^\d+(st|nd|rd|th) House/)) {
        currentSection?.content.push({ type: 'house', text: trimmed });
      }
      // Check for planet analysis
      else if (trimmed.includes(' in ') && trimmed.includes('(House ') && trimmed.includes('Potential Careers:')) {
        const parts = trimmed.split('Potential Careers:');
        currentSection?.content.push({ 
          type: 'planet', 
          planet: parts[0].trim(),
          careers: parts[1] ? parts[1].trim() : ''
        });
      }
      // Regular content
      else {
        currentSection?.content.push({ type: 'text', text: trimmed });
      }
    });

    if (currentSection) sections.push(currentSection);

    return (
      <div style={styles.careerContainer}>
        {sections.map((section, index) => (
          <div key={index} style={styles.careerSection}>
            <h4 style={styles.careerSectionTitle}>
              <Briefcase size={16} color="#059669" />
              {section.title}
            </h4>
            <div style={styles.careerContent}>
              {section.content.map((item, itemIndex) => {
                if (item.type === 'house') {
                  return (
                    <div key={itemIndex} style={styles.houseAnalysis}>
                      <div style={styles.houseHeader}>
                        <div style={styles.houseDot}></div>
                        <span style={styles.houseTitle}>{item.text}</span>
                      </div>
                    </div>
                  );
                } else if (item.type === 'planet') {
                  return (
                    <div key={itemIndex} style={styles.planetAnalysis}>
                      <div style={styles.planetHeader}>
                        <Star size={12} color="#f59e0b" />
                        <span style={styles.planetName}>{item.planet}</span>
                      </div>
                      <div style={styles.careerFields}>
                        {item.careers.split(',').map((career, careerIndex) => (
                          <span key={careerIndex} style={styles.careerTag}>
                            {career.trim()}
                          </span>
                        ))}
                      </div>
                    </div>
                  );
                } else {
                  return (
                    <p key={itemIndex} style={styles.careerText}>
                      {item.text}
                    </p>
                  );
                }
              })}
            </div>
          </div>
        ))}
      </div>
    );
  };

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
    interpretationContainer: {
      display: 'flex',
      flexDirection: 'column',
      gap: '20px'
    },
    simpleTextContainer: {
      background: 'rgba(255, 255, 255, 0.9)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(99, 102, 241, 0.1)',
      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)'
    },
    simpleText: {
      color: '#374151',
      lineHeight: '1.6',
      fontSize: '1rem',
      margin: '0',
      whiteSpace: 'pre-line'
    },
    sectionCard: {
      background: 'rgba(255, 255, 255, 0.9)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(99, 102, 241, 0.1)',
      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)',
      transition: 'all 0.3s ease'
    },
    sectionTitle: {
      fontSize: '1.25rem',
      fontWeight: '700',
      color: '#4f46e5',
      marginBottom: '16px',
      padding: '0 0 8px 0',
      borderBottom: '2px solid #e0e7ff'
    },
    sectionContent: {
      display: 'flex',
      flexDirection: 'column',
      gap: '12px'
    },
    bulletPoint: {
      background: 'rgba(99, 102, 241, 0.05)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(99, 102, 241, 0.1)'
    },
    bulletHeader: {
      display: 'flex',
      alignItems: 'center',
      gap: '10px',
      marginBottom: '8px'
    },
    bulletDot: {
      width: '8px',
      height: '8px',
      borderRadius: '50%',
      background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
      flexShrink: 0
    },
    bulletTitle: {
      fontWeight: '600',
      color: '#1e293b',
      fontSize: '1rem'
    },
    bulletDescription: {
      color: '#475569',
      lineHeight: '1.6',
      fontSize: '0.95rem',
      paddingLeft: '18px'
    },
    paragraph: {
      color: '#374151',
      lineHeight: '1.6',
      fontSize: '1rem',
      margin: '0'
    },
    yogaList: {
      background: 'rgba(255, 255, 255, 0.9)',
      borderRadius: '16px',
      padding: '20px',
      border: '1px solid rgba(99, 102, 241, 0.1)',
      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.05)'
    },
    yogaItem: {
      padding: '12px 16px',
      margin: '8px 0',
      background: 'rgba(99, 102, 241, 0.05)',
      borderRadius: '8px',
      border: '1px solid rgba(99, 102, 241, 0.1)',
      color: '#374151',
      fontSize: '0.95rem',
      lineHeight: '1.5'
    },
    footer: {
      textAlign: 'center',
      marginTop: '32px',
      color: '#94a3b8',
      fontSize: '0.875rem'
    },
    careerContainer: {
      display: 'flex',
      flexDirection: 'column',
      gap: '24px'
    },
    careerSection: {
      background: 'rgba(255, 255, 255, 0.95)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(5, 150, 105, 0.2)',
      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.08)',
      transition: 'all 0.3s ease'
    },
    careerSectionTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#059669',
      marginBottom: '16px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      padding: '0 0 12px 0',
      borderBottom: '2px solid #a7f3d0'
    },
    careerContent: {
      display: 'flex',
      flexDirection: 'column',
      gap: '16px'
    },
    houseAnalysis: {
      background: 'rgba(5, 150, 105, 0.05)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(5, 150, 105, 0.15)'
    },
    houseHeader: {
      display: 'flex',
      alignItems: 'center',
      gap: '10px'
    },
    houseDot: {
      width: '10px',
      height: '10px',
      borderRadius: '50%',
      background: 'linear-gradient(135deg, #059669, #10b981)',
      flexShrink: 0
    },
    houseTitle: {
      fontWeight: '600',
      color: '#047857',
      fontSize: '1rem',
      lineHeight: '1.4'
    },
    planetAnalysis: {
      background: 'rgba(245, 158, 11, 0.05)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(245, 158, 11, 0.2)'
    },
    planetHeader: {
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      marginBottom: '12px'
    },
    planetName: {
      fontWeight: '600',
      color: '#d97706',
      fontSize: '1rem'
    },
    careerFields: {
      display: 'flex',
      flexWrap: 'wrap',
      gap: '8px'
    },
    careerTag: {
      background: 'linear-gradient(135deg, #fbbf24, #f59e0b)',
      color: 'white',
      padding: '4px 12px',
      borderRadius: '20px',
      fontSize: '0.85rem',
      fontWeight: '500',
      whiteSpace: 'nowrap',
      boxShadow: '0 2px 4px rgba(245, 158, 11, 0.3)'
    },
    careerText: {
      color: '#374151',
      lineHeight: '1.6',
      fontSize: '1rem',
      margin: '0',
      padding: '8px 0'
    },
    cosmicContainer: {
      display: 'flex',
      flexDirection: 'column',
      gap: '24px'
    },
    cosmicIntro: {
      background: 'rgba(99, 102, 241, 0.05)',
      borderRadius: '16px',
      padding: '20px',
      border: '1px solid rgba(99, 102, 241, 0.1)',
      marginBottom: '8px'
    },
    cosmicIntroText: {
      color: '#4f46e5',
      fontSize: '1rem',
      lineHeight: '1.6',
      margin: '0 0 8px 0',
      fontWeight: '500'
    },
    cosmicSection: {
      background: 'rgba(255, 255, 255, 0.95)',
      borderRadius: '16px',
      padding: '24px',
      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.08)',
      transition: 'all 0.3s ease'
    },
    cosmicSectionTitle: {
      fontSize: '1.4rem',
      fontWeight: '700',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '12px',
      padding: '0 0 12px 0',
      borderBottom: '2px solid rgba(0, 0, 0, 0.1)'
    },
    cosmicSectionIcon: {
      fontSize: '1.5rem'
    },
    cosmicSectionNumber: {
      fontSize: '1.2rem',
      fontWeight: '800'
    },
    cosmicContent: {
      display: 'flex',
      flexDirection: 'column',
      gap: '16px'
    },
    astrologicalPoint: {
      background: 'rgba(0, 0, 0, 0.02)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(0, 0, 0, 0.08)'
    },
    astrologicalHeader: {
      display: 'flex',
      alignItems: 'center',
      gap: '10px',
      marginBottom: '8px'
    },
    astrologicalDot: {
      width: '8px',
      height: '8px',
      borderRadius: '50%',
      flexShrink: 0
    },
    astrologicalPlacement: {
      fontWeight: '600',
      color: '#1e293b',
      fontSize: '1rem'
    },
    astrologicalInterpretation: {
      color: '#475569',
      lineHeight: '1.6',
      fontSize: '0.95rem',
      paddingLeft: '18px'
    },
    cosmicText: {
      color: '#374151',
      lineHeight: '1.6',
      fontSize: '1rem',
      margin: '0'
    },
    lifePurposeContainer: {
      display: 'flex',
      flexDirection: 'column',
      gap: '24px'
    },
    lifePurposeTitle: {
      background: 'linear-gradient(135deg, #fecaca, #fde68a)',
      borderRadius: '16px',
      padding: '20px',
      border: '1px solid rgba(239, 68, 68, 0.2)',
      display: 'flex',
      alignItems: 'center',
      gap: '12px',
      fontSize: '1.5rem',
      fontWeight: '700',
      color: '#be123c',
      textAlign: 'center',
      justifyContent: 'center'
    },
    lifePurposeGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
      gap: '20px'
    },
    lifePurposeCard: {
      background: 'rgba(255, 255, 255, 0.95)',
      borderRadius: '16px',
      padding: '20px',
      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.08)',
      transition: 'all 0.3s ease'
    },
    lifePurposeCardHeader: {
      display: 'flex',
      alignItems: 'center',
      gap: '10px',
      marginBottom: '12px'
    },
    lifePurposeIcon: {
      fontSize: '1.5rem'
    },
    lifePurposeCardTitle: {
      fontSize: '1.1rem',
      fontWeight: '700'
    },
    lifePurposeCardDescription: {
      color: '#475569',
      lineHeight: '1.6',
      fontSize: '0.95rem'
    },
    lifePurposeSummary: {
      background: 'rgba(139, 92, 246, 0.05)',
      borderRadius: '16px',
      padding: '20px',
      border: '1px solid rgba(139, 92, 246, 0.2)',
      marginTop: '8px'
    },
    lifePurposeSummaryText: {
      color: '#374151',
      lineHeight: '1.6',
      fontSize: '1rem',
      margin: '0',
      fontStyle: 'italic'
    },
    dasaBhuktiContainer: {
      display: 'flex',
      flexDirection: 'column',
      gap: '32px'
    },
    birthInfoCard: {
      background: 'rgba(99, 102, 241, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(99, 102, 241, 0.2)'
    },
    birthInfoTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#4f46e5',
      marginBottom: '16px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    birthInfoGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
      gap: '16px'
    },
    birthInfoItem: {
      display: 'flex',
      flexDirection: 'column',
      gap: '4px'
    },
    birthInfoLabel: {
      fontSize: '0.875rem',
      fontWeight: '600',
      color: '#6366f1',
      textTransform: 'uppercase',
      letterSpacing: '0.5px'
    },
    birthInfoValue: {
      fontSize: '1rem',
      fontWeight: '500',
      color: '#1e293b'
    },
    planetaryPositionsCard: {
      background: 'rgba(16, 185, 129, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(16, 185, 129, 0.2)'
    },
    planetaryPositionsTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#059669',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    planetaryGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
      gap: '16px'
    },
    planetCard: {
      background: 'rgba(255, 255, 255, 0.9)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(16, 185, 129, 0.3)',
      transition: 'all 0.3s ease'
    },
    planetName: {
      fontSize: '1.1rem',
      fontWeight: '700',
      color: '#047857',
      marginBottom: '8px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    planetDetails: {
      fontSize: '0.9rem',
      color: '#6b7280',
      marginBottom: '4px'
    },
    nakshatraInfo: {
      background: 'rgba(16, 185, 129, 0.1)',
      padding: '8px 12px',
      borderRadius: '8px',
      marginTop: '8px'
    },
    nakshatraText: {
      fontSize: '0.85rem',
      color: '#047857',
      fontWeight: '500'
    },
    dasaTimelineCard: {
      background: 'rgba(245, 158, 11, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(245, 158, 11, 0.2)'
    },
    dasaTimelineTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#d97706',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    dasaTimelineGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
      gap: '16px'
    },
    dasaPeriodCard: {
      background: 'rgba(255, 255, 255, 0.9)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(245, 158, 11, 0.3)',
      transition: 'all 0.3s ease',
      cursor: 'pointer'
    },
    dasaPlanetName: {
      fontSize: '1.1rem',
      fontWeight: '700',
      color: '#92400e',
      marginBottom: '8px'
    },
    dasaAgeRange: {
      fontSize: '0.9rem',
      color: '#78716c',
      marginBottom: '4px'
    },
    dasaDateRange: {
      fontSize: '0.85rem',
      color: '#57534e',
      marginBottom: '4px'
    },
    dasaDuration: {
      fontSize: '0.8rem',
      color: '#a16207',
      fontWeight: '600',
      background: 'rgba(245, 158, 11, 0.1)',
      padding: '2px 8px',
      borderRadius: '12px',
      display: 'inline-block'
    },
    gptInterpretationCard: {
      background: 'rgba(139, 92, 246, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(139, 92, 246, 0.2)'
    },
    gptInterpretationTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#7c3aed',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    dasaBhuktiSection: {
      background: 'rgba(255, 255, 255, 0.95)',
      borderRadius: '16px',
      padding: '24px',
      boxShadow: '0 4px 15px rgba(0, 0, 0, 0.08)',
      transition: 'all 0.3s ease'
    },
    dasaBhuktiSectionTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      marginBottom: '16px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      padding: '0 0 12px 0',
      borderBottom: '2px solid rgba(0, 0, 0, 0.1)'
    },
    dasaBhuktiIcon: {
      fontSize: '1.3rem'
    },
    dasaBhuktiNumber: {
      fontSize: '1.1rem',
      fontWeight: '800'
    },
    dasaBhuktiContent: {
      display: 'flex',
      flexDirection: 'column',
      gap: '12px'
    },
    dasaPeriod: {
      background: 'rgba(59, 130, 246, 0.05)',
      borderRadius: '8px',
      padding: '12px',
      border: '1px solid rgba(59, 130, 246, 0.2)'
    },
    dasaPeriodText: {
      color: '#1e40af',
      fontSize: '0.95rem',
      lineHeight: '1.5',
      fontWeight: '500'
    },
    dasaBhuktiText: {
      color: '#374151',
      lineHeight: '1.6',
      fontSize: '1rem',
      margin: '0'
    },
    spouseContainer: {
      display: 'flex',
      flexDirection: 'column',
      gap: '32px'
    },
    spouseChartCard: {
      background: 'rgba(239, 68, 68, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(239, 68, 68, 0.2)'
    },
    spouseChartTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#dc2626',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    spouseChartGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
      gap: '16px'
    },
    spouseChartItem: {
      background: 'rgba(255, 255, 255, 0.9)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(239, 68, 68, 0.3)',
      transition: 'all 0.3s ease'
    },
    spousePlanetName: {
      fontSize: '1rem',
      fontWeight: '700',
      color: '#dc2626',
      marginBottom: '8px',
      display: 'flex',
      alignItems: 'center',
      gap: '6px'
    },
    spousePlanetDetail: {
      fontSize: '0.85rem',
      color: '#6b7280',
      marginBottom: '4px'
    },
    spouseReportCard: {
      background: 'rgba(219, 39, 119, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(219, 39, 119, 0.2)'
    },
    spouseReportTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#be185d',
      marginBottom: '16px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    spouseReportContent: {
      display: 'flex',
      flexDirection: 'column',
      gap: '8px'
    },
    spouseReportLine: {
      background: 'rgba(255, 255, 255, 0.7)',
      padding: '12px 16px',
      borderRadius: '8px',
      color: '#374151',
      fontSize: '0.95rem',
      fontWeight: '500'
    },
    spouseInterpretationCard: {
      background: 'rgba(168, 85, 247, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(168, 85, 247, 0.2)'
    },
    spouseInterpretationTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#7c3aed',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    wealthContainer: {
      display: 'flex',
      flexDirection: 'column',
      gap: '32px'
    },
    induAnalysisCard: {
      background: 'rgba(245, 158, 11, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(245, 158, 11, 0.2)'
    },
    induAnalysisTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#d97706',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    induAnalysisGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
      gap: '16px',
      marginBottom: '20px'
    },
    induAnalysisItem: {
      display: 'flex',
      flexDirection: 'column',
      gap: '4px'
    },
    induLabel: {
      fontSize: '0.875rem',
      fontWeight: '600',
      color: '#d97706',
      textTransform: 'uppercase',
      letterSpacing: '0.5px'
    },
    induValue: {
      fontSize: '1rem',
      fontWeight: '500',
      color: '#1e293b'
    },
    planetsInInduCard: {
      background: 'rgba(255, 255, 255, 0.7)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(245, 158, 11, 0.3)'
    },
    planetsInInduTitle: {
      fontSize: '1rem',
      fontWeight: '600',
      color: '#92400e',
      marginBottom: '12px'
    },
    planetsInInduList: {
      display: 'flex',
      flexWrap: 'wrap',
      gap: '8px'
    },
    planetTag: {
      background: 'linear-gradient(135deg, #fbbf24, #f59e0b)',
      color: 'white',
      padding: '6px 12px',
      borderRadius: '20px',
      fontSize: '0.85rem',
      fontWeight: '500',
      boxShadow: '0 2px 4px rgba(245, 158, 11, 0.3)'
    },
    wealthTimelineCard: {
      background: 'rgba(34, 197, 94, 0.05)',
      borderRadius: '16px',
      padding: '24px',
      border: '1px solid rgba(34, 197, 94, 0.2)'
    },
    wealthTimelineTitle: {
      fontSize: '1.3rem',
      fontWeight: '700',
      color: '#15803d',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'center',
      gap: '8px'
    },
    wealthTimelineGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minMax(280px, 1fr))',
      gap: '16px'
    },
    wealthPeriodCard: {
      background: 'rgba(255, 255, 255, 0.9)',
      borderRadius: '12px',
      padding: '16px',
      border: '1px solid rgba(34, 197, 94, 0.3)',
      transition: 'all 0.3s ease',
      cursor: 'pointer'
    },
    wealthPeriodHeader: {
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      marginBottom: '8px'
    },
    wealthMahaDasa: {
      fontSize: '1rem',
      fontWeight: '700',
      color: '#15803d'
    },
    wealthBukti: {
      fontSize: '0.9rem',
      color: '#16a34a',
      fontWeight: '500'
    },
    wealthPeriodDates: {
      fontSize: '0.85rem',
      color: '#6b7280',
      marginBottom: '4px'
    },
    wealthPeriodDuration: {
      fontSize: '0.8rem',
      color: '#15803d',
      fontWeight: '600',
      background: 'rgba(34, 197, 94, 0.1)',
      padding: '2px 8px',
      borderRadius: '12px',
      display: 'inline-block'
    }
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
                      {formatText(result.interpretation)}
                    </>
                  )}

                  {activeTab === "career" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <Briefcase size={18} color="#059669" />
                        Career Insights
                      </h3>
                      {formatText(career)}
                    </>
                  )}

                  {activeTab === "dasa" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <Timeline size={18} color="#dc2626" />
                        Dasa Timeline
                      </h3>
                      {dasa && (
                        <div style={{ overflowX: 'auto' }}>
                          <table style={styles.table}>
                            <thead>
                              <tr>
                                <th style={styles.tableHeader}>Planet</th>
                                <th style={styles.tableHeader}>Start Age</th>
                                <th style={styles.tableHeader}>End Age</th>
                                <th style={styles.tableHeader}>Start Date</th>
                                <th style={styles.tableHeader}>End Date</th>
                              </tr>
                            </thead>
                            <tbody>
                              {dasa.map((d, i) => (
                                <tr key={i} style={styles.tableRow}>
                                  <td style={{...styles.tableCell, fontWeight: '600'}}>{d.planet}</td>
                                  <td style={styles.tableCell}>{d.start_age}</td>
                                  <td style={styles.tableCell}>{d.end_age}</td>
                                  <td style={styles.tableCell}>{d.start_date}</td>
                                  <td style={styles.tableCell}>{d.end_date}</td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>
                      )}
                    </>
                  )}

                  {activeTab === "dasabhukti" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <Calendar2 size={18} color="#3b82f6" />
                        Comprehensive Dasa Bhukti Analysis
                      </h3>
                      {dasaBhukti && (
                        <div style={styles.dasaBhuktiContainer}>
                          {dasaBhukti.birth_info && (
                            <div style={styles.birthInfoCard}>
                              <h4 style={styles.birthInfoTitle}>
                                📍 Birth Information
                              </h4>
                              <div style={styles.birthInfoGrid}>
                                <div style={styles.birthInfoItem}>
                                  <span style={styles.birthInfoLabel}>Date:</span>
                                  <span style={styles.birthInfoValue}>{dasaBhukti.birth_info.dob}</span>
                                </div>
                                <div style={styles.birthInfoItem}>
                                  <span style={styles.birthInfoLabel}>Time:</span>
                                  <span style={styles.birthInfoValue}>{dasaBhukti.birth_info.tob}</span>
                                </div>
                                <div style={styles.birthInfoItem}>
                                  <span style={styles.birthInfoLabel}>Place:</span>
                                  <span style={styles.birthInfoValue}>{dasaBhukti.birth_info.place}</span>
                                </div>
                              </div>
                            </div>
                          )}

                          {dasaBhukti.planetary_positions && (
                            <div style={styles.planetaryPositionsCard}>
                              <h4 style={styles.planetaryPositionsTitle}>
                                🌟 Detailed Planetary Positions
                              </h4>
                              <div style={styles.planetaryGrid}>
                                {Object.entries(dasaBhukti.planetary_positions).map(([planet, info]) => (
                                  <div key={planet} style={styles.planetCard}>
                                    <div style={styles.planetName}>
                                      <Star size={14} color="#047857" />
                                      {planet}
                                    </div>
                                    <div style={styles.planetDetails}>
                                      Longitude: {info.longitude.toFixed(2)}°
                                    </div>
                                    <div style={styles.planetDetails}>
                                      Retrograde: {info.retrograde ? 'Yes' : 'No'}
                                    </div>
                                    <div style={styles.nakshatraInfo}>
                                      <div style={styles.nakshatraText}>
                                        {info.nakshatra} • Pada {info.pada}
                                      </div>
                                    </div>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}

                          {dasaBhukti.dasa_table && (
                            <div style={styles.dasaTimelineCard}>
                              <h4 style={styles.dasaTimelineTitle}>
                                ⏰ Mahadasa Timeline
                              </h4>
                              <div style={styles.dasaTimelineGrid}>
                                {dasaBhukti.dasa_table.map((period, index) => (
                                  <div key={index} style={styles.dasaPeriodCard}>
                                    <div style={styles.dasaPlanetName}>{period.planet}</div>
                                    <div style={styles.dasaAgeRange}>
                                      Age {period.start_age} - {period.end_age}
                                    </div>
                                    <div style={styles.dasaDateRange}>
                                      {period.start_date} to {period.end_date}
                                    </div>
                                    <div style={styles.dasaDuration}>
                                      {period.duration} years
                                    </div>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}

                          {dasaBhukti.gpt_prediction && (
                            <div style={styles.gptInterpretationCard}>
                              <h4 style={styles.gptInterpretationTitle}>
                                🔮 Detailed Life Analysis
                              </h4>
                              {formatText(dasaBhukti.gpt_prediction)}
                            </div>
                          )}
                        </div>
                      )}
                    </>
                  )}

                  {activeTab === "yogas" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <Zap size={18} color="#7c3aed" />
                        Yogas & Doshas
                      </h3>
                      {yogas && (
                        <div style={styles.yogaList}>
                          {yogas.map((yoga, i) => (
                            <div key={i} style={styles.yogaItem}>
                              {yoga}
                            </div>
                          ))}
                        </div>
                      )}
                    </>
                  )}

                  {activeTab === "lifepurpose" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <Heart size={18} color="#e11d48" />
                        Life Purpose Analysis
                      </h3>
                      {lifePurpose && formatText(lifePurpose.interpretation)}
                    </>
                  )}

                  {activeTab === "spouse" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <Heart size={18} color="#e11d48" />
                        Spouse Analysis
                      </h3>
                      {spouseAnalysis && (
                        <div style={styles.spouseContainer}>
                          {spouseAnalysis.chart && (
                            <div style={styles.spouseChartCard}>
                              <h4 style={styles.spouseChartTitle}>
                                🌟 Planetary Positions for Spouse Analysis
                              </h4>
                              <div style={styles.spouseChartGrid}>
                                {Object.entries(spouseAnalysis.chart).map(([planet, info]) => (
                                  <div key={planet} style={styles.spouseChartItem}>
                                    <div style={styles.spousePlanetName}>
                                      <Star size={12} color="#e11d48" />
                                      {planet}
                                    </div>
                                    <div style={styles.spousePlanetDetail}>Rasi: {info.rasi}</div>
                                    <div style={styles.spousePlanetDetail}>Nakshatra: {info.nakshatra}</div>
                                    <div style={styles.spousePlanetDetail}>Pada: {info.pada}</div>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}

                          {spouseAnalysis.report && (
                            <div style={styles.spouseReportCard}>
                              <h4 style={styles.spouseReportTitle}>
                                💍 Quick Spouse Profile
                              </h4>
                              <div style={styles.spouseReportContent}>
                                {spouseAnalysis.report.split('\n').map((line, index) => {
                                  if (line.trim()) {
                                    return (
                                      <div key={index} style={styles.spouseReportLine}>
                                        {line.replace('💍 Spouse Analysis:', '').trim()}
                                      </div>
                                    );
                                  }
                                  return null;
                                })}
                              </div>
                            </div>
                          )}

                          {spouseAnalysis.interpretation && (
                            <div style={styles.spouseInterpretationCard}>
                              <h4 style={styles.spouseInterpretationTitle}>
                                🔮 Detailed Spouse Analysis
                              </h4>
                              {formatText(spouseAnalysis.interpretation)}
                            </div>
                          )}
                        </div>
                      )}
                    </>
                  )}

                  {activeTab === "wealth" && (
                    <>
                      <h3 style={styles.tabHeader}>
                        <DollarSign size={18} color="#f59e0b" />
                        Wealth Cycles & Prosperity Periods
                      </h3>
                      {induDasa && (
                        <div style={styles.wealthContainer}>
                          <div style={styles.induAnalysisCard}>
                            <h4 style={styles.induAnalysisTitle}>
                              💰 Indu Lagnam Analysis
                            </h4>
                            <div style={styles.induAnalysisGrid}>
                              <div style={styles.induAnalysisItem}>
                                <span style={styles.induLabel}>Ascendant:</span>
                                <span style={styles.induValue}>{induDasa.ascendant}</span>
                              </div>
                              <div style={styles.induAnalysisItem}>
                                <span style={styles.induLabel}>Moon Rasi:</span>
                                <span style={styles.induValue}>{induDasa.moon_rasi}</span>
                              </div>
                              <div style={styles.induAnalysisItem}>
                                <span style={styles.induLabel}>Indu Lagnam:</span>
                                <span style={styles.induValue}>{induDasa.indu_lagnam}</span>
                              </div>
                              <div style={styles.induAnalysisItem}>
                                <span style={styles.induLabel}>Indu Lord:</span>
                                <span style={styles.induValue}>{induDasa.indu_lord}</span>
                              </div>
                            </div>

                            {induDasa.planets_in_indu_lagnam && induDasa.planets_in_indu_lagnam.length > 0 && (
                              <div style={styles.planetsInInduCard}>
                                <h5 style={styles.planetsInInduTitle}>
                                  🌟 Planets in Indu Lagnam
                                </h5>
                                <div style={styles.planetsInInduList}>
                                  {induDasa.planets_in_indu_lagnam.map((planet, index) => (
                                    <span key={index} style={styles.planetTag}>
                                      {planet}
                                    </span>
                                  ))}
                                </div>
                              </div>
                            )}
                          </div>

                          {induDasa.timeline && (
                            <div style={styles.wealthTimelineCard}>
                              <h4 style={styles.wealthTimelineTitle}>
                                ⏰ Wealth & Prosperity Timeline
                              </h4>
                              <div style={styles.wealthTimelineGrid}>
                                {induDasa.timeline.map((period, index) => (
                                  <div key={index} style={styles.wealthPeriodCard}>
                                    <div style={styles.wealthPeriodHeader}>
                                      <div style={styles.wealthMahaDasa}>{period.maha_dasa}</div>
                                      <div style={styles.wealthBukti}>• {period.bukti}</div>
                                    </div>
                                    <div style={styles.wealthPeriodDates}>
                                      {period.start} to {period.end}
                                    </div>
                                    <div style={styles.wealthPeriodDuration}>
                                      {Math.round(((new Date(period.end) - new Date(period.start)) / (365.25 * 24 * 60 * 60 * 1000)) * 10) / 10} years
                                    </div>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}
                        </div>
                      )}
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