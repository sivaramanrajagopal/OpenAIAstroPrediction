# Google APIs Setup for Vedic Astrology App

## Required Google APIs

To enable enhanced location services and precise timezone detection, you'll need to set up these Google APIs:

### 1. Google Geocoding API
- **Purpose**: Convert coordinates to addresses and addresses to coordinates
- **Documentation**: https://developers.google.com/maps/documentation/geocoding

### 2. Google Timezone API  
- **Purpose**: Get precise timezone information for any coordinates
- **Documentation**: https://developers.google.com/maps/documentation/timezone

### 3. Google Places API (Autocomplete)
- **Purpose**: Provide city/location search suggestions
- **Documentation**: https://developers.google.com/maps/documentation/places

## Setup Steps

### Step 1: Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable billing (required for API access)

### Step 2: Enable Required APIs
Enable these APIs in your Google Cloud Console:
- **Geocoding API**
- **Timezone API** 
- **Places API**
- **Maps JavaScript API** (for frontend integration)

### Step 3: Create API Credentials
1. Go to **APIs & Services > Credentials**
2. Click **Create Credentials > API Key**
3. Copy the generated API key
4. Optionally, restrict the API key to specific APIs and domains for security

### Step 4: Configure Environment Variables

Create both `.env.local` (for development) and configure environment variables on your production platform:

**.env.local** (Development):
```env
# Google APIs (Server-side only - more secure)
GOOGLE_API_KEY=your_google_api_key_here

# Existing environment variables  
NEXT_PUBLIC_BACKEND_URL=https://proactive-manifestation-production.up.railway.app
OPENAI_API_KEY=your_openai_api_key
```

**Production Environment Variables**:
Set these on your hosting platform (Vercel, Railway, etc.):
- `GOOGLE_API_KEY` - Your Google API key (server-side only)
- `NEXT_PUBLIC_BACKEND_URL` - Your backend URL
- `OPENAI_API_KEY` - Your OpenAI API key

### Step 5: API Key Security (Important!)

For production, implement these security measures:

1. **Restrict API Key by HTTP Referrer**:
   - Add your domain(s) to the API key restrictions
   - Example: `https://yourdomain.com/*`

2. **Restrict API Key by API**:
   - Only enable the specific APIs you need
   - Geocoding API, Timezone API, Places API

3. **Monitor Usage**:
   - Set up billing alerts
   - Monitor API usage in Google Cloud Console

## API Pricing (As of 2024)

- **Geocoding API**: $5.00 per 1000 requests
- **Timezone API**: $5.00 per 1000 requests  
- **Places API Autocomplete**: $2.83 per 1000 requests

Google provides $200 in free credits monthly which covers significant usage.

## Security Architecture

This implementation uses **secure server-side API routes** instead of direct client-side API calls:

### Server-Side API Routes Created:
- `/api/google-geocode` - Handles geocoding and reverse geocoding
- `/api/google-timezone` - Manages timezone detection  
- `/api/google-places` - Provides location search functionality

### Security Benefits:
✅ **API Key Protection** - Google API key stays server-side, never exposed to browsers
✅ **Request Validation** - Server validates all requests before calling Google APIs
✅ **Rate Limiting** - Easier to implement usage controls on server-side
✅ **Error Handling** - Proper error handling and user-friendly messages
✅ **CORS Prevention** - No cross-origin issues since APIs run on same domain

## Implementation Features

With Google APIs enabled, your app will have:

✅ **Enhanced Location Detection**
- Precise reverse geocoding from GPS coordinates
- Professional address formatting
- City and country identification

✅ **Intelligent City Search**
- Real-time city/location autocomplete
- Global location database
- Structured address formatting

✅ **Precise Timezone Detection**
- Automatic timezone identification from coordinates
- Daylight Saving Time (DST) handling
- Historical timezone data for any date

✅ **Professional User Experience**
- Google-quality location services
- Fast, accurate location lookup
- Seamless integration with existing astrology calculations

## Testing Your Setup

1. Add your API key to `.env.local`
2. Restart your development server
3. Test the location features:
   - Auto-detect current location
   - Search for cities (try "Chennai", "New York", "London")
   - Verify timezone detection shows correct values

## Troubleshooting

**Common Issues:**

1. **API Key not working**: Check that all required APIs are enabled
2. **CORS errors**: Ensure HTTP referrer restrictions include your domain
3. **Quota exceeded**: Monitor usage in Google Cloud Console
4. **Invalid results**: Verify API key has proper permissions

## Fallback Behavior

The app includes fallback mechanisms:
- If Google APIs fail, it falls back to basic longitude-based timezone estimation
- Manual coordinate input always available
- Basic location detection still works without API key

This ensures your astrology app continues to function even if Google APIs encounter issues.