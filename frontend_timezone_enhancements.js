// Frontend Timezone Enhancement Recommendations
// Add these features to your pages/index.js

// 1. Add location detection and timezone services
const [locationData, setLocationData] = useState({
  city: '',
  country: '',
  timezone: '',
  detected: false
});

// 2. Add timezone detection function
const detectLocationAndTimezone = async (lat, lon) => {
  try {
    // Use a geolocation API to get city/country info
    const geocodeResponse = await fetch(
      `https://api.opencagedata.com/geocode/v1/json?q=${lat}+${lon}&key=YOUR_API_KEY`
    );
    const geocodeData = await geocodeResponse.json();
    
    if (geocodeData.results && geocodeData.results.length > 0) {
      const result = geocodeData.results[0];
      const timezone = result.annotations?.timezone?.name;
      
      setLocationData({
        city: result.components.city || result.components.town || result.components.village,
        country: result.components.country,
        timezone: timezone,
        detected: true
      });
      
      // Auto-calculate timezone offset
      if (timezone) {
        const now = new Date();
        const timeInTimezone = new Date(now.toLocaleString("en-US", {timeZone: timezone}));
        const timeInUTC = new Date(now.toLocaleString("en-US", {timeZone: "UTC"}));
        const offset = (timeInTimezone - timeInUTC) / (1000 * 60 * 60);
        
        setFormData(prev => ({
          ...prev,
          tz_offset: offset.toString()
        }));
      }
    }
  } catch (error) {
    console.error('Location detection failed:', error);
  }
};

// 3. Add browser geolocation
const getCurrentLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        
        setFormData(prev => ({
          ...prev,
          lat: lat.toString(),
          lon: lon.toString()
        }));
        
        detectLocationAndTimezone(lat, lon);
      },
      (error) => {
        console.error('Geolocation failed:', error);
        alert('Please allow location access or enter coordinates manually');
      }
    );
  } else {
    alert('Geolocation is not supported by this browser');
  }
};

// 4. Add city search functionality
const searchCity = async (cityName) => {
  try {
    const response = await fetch(
      `https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(cityName)}&key=YOUR_API_KEY&limit=5`
    );
    const data = await response.json();
    
    if (data.results && data.results.length > 0) {
      return data.results.map(result => ({
        name: result.formatted,
        lat: result.geometry.lat,
        lng: result.geometry.lng,
        timezone: result.annotations?.timezone?.name
      }));
    }
    return [];
  } catch (error) {
    console.error('City search failed:', error);
    return [];
  }
};

// 5. Enhanced form field components
const LocationInput = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);

  const handleCitySearch = async (value) => {
    setSearchTerm(value);
    if (value.length > 2) {
      const results = await searchCity(value);
      setSuggestions(results);
      setShowSuggestions(true);
    } else {
      setShowSuggestions(false);
    }
  };

  const selectCity = (city) => {
    setFormData(prev => ({
      ...prev,
      lat: city.lat.toString(),
      lon: city.lng.toString()
    }));
    
    setLocationData({
      city: city.name,
      timezone: city.timezone,
      detected: true
    });
    
    if (city.timezone) {
      const now = new Date();
      const offset = (new Date(now.toLocaleString("en-US", {timeZone: city.timezone})) - 
                     new Date(now.toLocaleString("en-US", {timeZone: "UTC"}))) / (1000 * 60 * 60);
      
      setFormData(prev => ({
        ...prev,
        tz_offset: offset.toString()
      }));
    }
    
    setSearchTerm(city.name);
    setShowSuggestions(false);
  };

  return (
    <div style={{ position: 'relative' }}>
      <input
        type="text"
        placeholder="Search city (e.g., Chennai, New York)"
        value={searchTerm}
        onChange={(e) => handleCitySearch(e.target.value)}
        style={{
          width: '100%',
          padding: '12px',
          border: '2px solid #e5e7eb',
          borderRadius: '8px',
          fontSize: '16px'
        }}
      />
      
      {showSuggestions && suggestions.length > 0 && (
        <div style={{
          position: 'absolute',
          top: '100%',
          left: 0,
          right: 0,
          background: 'white',
          border: '1px solid #e5e7eb',
          borderRadius: '8px',
          maxHeight: '200px',
          overflowY: 'auto',
          zIndex: 1000,
          boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
        }}>
          {suggestions.map((city, index) => (
            <div
              key={index}
              onClick={() => selectCity(city)}
              style={{
                padding: '12px',
                cursor: 'pointer',
                borderBottom: index < suggestions.length - 1 ? '1px solid #f3f4f6' : 'none'
              }}
            >
              {city.name}
            </div>
          ))}
        </div>
      )}
      
      <button
        type="button"
        onClick={getCurrentLocation}
        style={{
          position: 'absolute',
          right: '8px',
          top: '50%',
          transform: 'translateY(-50%)',
          background: '#667eea',
          color: 'white',
          border: 'none',
          borderRadius: '6px',
          padding: '6px 10px',
          cursor: 'pointer',
          fontSize: '12px'
        }}
      >
        📍 Auto
      </button>
    </div>
  );
};

// 6. Update backend URL to use Railway
const backend = process.env.NEXT_PUBLIC_BACKEND_URL || 
               (process.env.NODE_ENV === 'production' 
                 ? 'https://proactive-manifestation-production.up.railway.app'  // Updated to Railway
                 : 'http://localhost:8000');

// 7. Add timezone display component
const TimezoneDisplay = () => {
  if (!locationData.detected) return null;
  
  return (
    <div style={{
      background: '#f0f9ff',
      border: '1px solid #0284c7',
      borderRadius: '8px',
      padding: '12px',
      marginTop: '16px'
    }}>
      <div style={{ fontSize: '14px', color: '#0284c7', fontWeight: '600' }}>
        📍 Detected Location
      </div>
      <div style={{ fontSize: '13px', color: '#374151', marginTop: '4px' }}>
        {locationData.city && locationData.country && 
          `${locationData.city}, ${locationData.country}`}
      </div>
      {locationData.timezone && (
        <div style={{ fontSize: '13px', color: '#374151' }}>
          Timezone: {locationData.timezone}
        </div>
      )}
    </div>
  );
};