// pages/api/google-timezone.js
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { lat, lng, timestamp } = req.query;
  const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;

  if (!GOOGLE_API_KEY) {
    return res.status(500).json({ error: 'Google API key not configured' });
  }

  if (!lat || !lng) {
    return res.status(400).json({ error: 'Latitude and longitude are required' });
  }

  try {
    const ts = timestamp || Math.floor(Date.now() / 1000);
    const response = await fetch(
      `https://maps.googleapis.com/maps/api/timezone/json?location=${lat},${lng}&timestamp=${ts}&key=${GOOGLE_API_KEY}`
    );

    const data = await response.json();

    if (data.status === 'OK') {
      res.status(200).json({
        timezone_id: data.timeZoneId,
        timezone_name: data.timeZoneName,
        raw_offset: data.rawOffset / 3600, // Convert to hours
        dst_offset: data.dstOffset / 3600,
        total_offset: (data.rawOffset + data.dstOffset) / 3600
      });
    } else {
      res.status(400).json({ error: data.status, message: data.error_message });
    }
  } catch (error) {
    console.error('Timezone API error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
}