// pages/api/google-geocode.js
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { lat, lng, address, placeId } = req.query;
  const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;

  if (!GOOGLE_API_KEY) {
    return res.status(500).json({ error: 'Google API key not configured' });
  }

  try {
    let response;

    if (placeId) {
      // Get place details by place ID
      response = await fetch(
        `https://maps.googleapis.com/maps/api/place/details/json?place_id=${placeId}&fields=geometry,formatted_address,address_components&key=${GOOGLE_API_KEY}`
      );
    } else if (lat && lng) {
      // Reverse geocoding
      response = await fetch(
        `https://maps.googleapis.com/maps/api/geocoding/json?latlng=${lat},${lng}&key=${GOOGLE_API_KEY}`
      );
    } else if (address) {
      // Forward geocoding
      response = await fetch(
        `https://maps.googleapis.com/maps/api/geocoding/json?address=${encodeURIComponent(address)}&key=${GOOGLE_API_KEY}`
      );
    } else {
      return res.status(400).json({ error: 'Missing required parameters' });
    }

    const data = await response.json();

    if (data.status === 'OK') {
      res.status(200).json(data);
    } else {
      res.status(400).json({ error: data.status, message: data.error_message });
    }
  } catch (error) {
    console.error('Geocoding API error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
}