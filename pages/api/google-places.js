// pages/api/google-places.js
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { query, type = '(cities)' } = req.query;
  const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;

  // Enhanced debugging
  console.log('🔍 Places API Debug:', {
    hasApiKey: !!GOOGLE_API_KEY,
    apiKeyPrefix: GOOGLE_API_KEY ? GOOGLE_API_KEY.substring(0, 10) + '...' : 'none',
    query,
    type
  });

  if (!GOOGLE_API_KEY) {
    console.error('❌ Google API key not found in environment variables');
    return res.status(500).json({ 
      error: 'Google API key not configured',
      debug: 'GOOGLE_API_KEY environment variable not set'
    });
  }

  if (!query || query.length < 2) {
    return res.status(400).json({ error: 'Query must be at least 2 characters' });
  }

  try {
    const apiUrl = `https://maps.googleapis.com/maps/api/place/autocomplete/json?input=${encodeURIComponent(query)}&types=${type}&key=${GOOGLE_API_KEY}`;
    console.log('🌐 Calling Google Places API...');
    
    const response = await fetch(apiUrl);
    const data = await response.json();

    console.log('📡 Google API Response:', {
      status: data.status,
      resultsCount: data.predictions?.length || 0,
      errorMessage: data.error_message
    });

    if (data.status === 'OK') {
      const suggestions = data.predictions.slice(0, 5).map(prediction => ({
        place_id: prediction.place_id,
        description: prediction.description,
        structured_formatting: prediction.structured_formatting,
        main_text: prediction.structured_formatting?.main_text || prediction.description.split(',')[0],
        secondary_text: prediction.structured_formatting?.secondary_text || prediction.description.split(',').slice(1).join(',').trim()
      }));

      res.status(200).json({ suggestions });
    } else {
      console.error('❌ Google API Error:', data);
      res.status(400).json({ 
        error: data.status, 
        message: data.error_message,
        debug: 'Check Google Cloud Console for API restrictions'
      });
    }
  } catch (error) {
    console.error('❌ Places API error:', error);
    res.status(500).json({ 
      error: 'Internal server error',
      message: error.message,
      debug: 'Network or parsing error'
    });
  }
}