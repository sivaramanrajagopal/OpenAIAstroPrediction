# Vedic Astrology Frontend

Frontend for the Vedic Astrology application built with Next.js and Tailwind CSS.

## 🚀 Quick Deploy Options

### Option 1: Vercel (Recommended)
1. Fork the repository
2. Connect to Vercel
3. Deploy automatically with `vercel.json` configuration

### Option 2: Netlify  
1. Connect repository to Netlify
2. Uses `netlify.toml` configuration
3. Deploys automatically

### Option 3: Railway
1. Create a new Railway project
2. Connect your GitHub repository
3. Set environment variables in Railway dashboard

## 🔧 Environment Variables

Set in your deployment platform:

```bash
NEXT_PUBLIC_BACKEND_URL=https://openaiastroprediction-production.up.railway.app
```

## 🛠️ Local Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## 📁 Project Structure

```
frontend/
├── pages/          # Next.js pages
├── styles/         # CSS styles
├── vercel.json     # Vercel deployment config
├── netlify.toml    # Netlify deployment config
└── package.json    # Dependencies
```

## 🌐 Backend Integration

The frontend automatically connects to your Railway backend:
- **Backend URL:** https://openaiastroprediction-production.up.railway.app
- **API Health:** https://openaiastroprediction-production.up.railway.app/health

## 📝 Features

- ✅ Responsive design with Tailwind CSS
- ✅ Real-time astrological calculations  
- ✅ AI-powered interpretations
- ✅ Multiple analysis types (Career, Life Purpose, etc.)
- ✅ Environment-aware backend URL configuration