# 🔮 Vedic Astrology API & Frontend

A comprehensive Vedic astrology application with AI-powered interpretations using OpenAI GPT-3.5-turbo.

## ✨ Features

- **Planetary Chart Analysis** - Complete birth chart with planets, signs, nakshatras
- **Career Insights** - AI-powered career analysis based on planetary positions
- **Dasa Timeline** - Vimshottari Dasa periods with predictions
- **Yogas & Doshas** - Detection of astrological combinations
- **Life Purpose Analysis** - Dharmic insights and spiritual guidance
- **Spouse Analysis** - Marriage compatibility and spouse predictions
- **Wealth Cycles** - Indu Dasa for prosperity timing

## 📁 Project Structure

```
OpenAI-AstroProject/
├── backend/                 # FastAPI backend
│   ├── modules/            # Astrology calculation modules
│   │   ├── astrology.py    # Core planetary calculations
│   │   ├── career.py       # Career analysis (renamed from carear.py)
│   │   ├── life_purpose.py # Life purpose & dharma
│   │   ├── dasa_bhukti.py  # Dasa period analysis
│   │   └── ...
│   ├── ephe/              # Swiss Ephemeris data files
│   ├── main.py            # FastAPI app entry point
│   ├── requirements.txt   # Python dependencies
│   └── Procfile          # Railway deployment config
├── frontend/              # Next.js frontend
│   ├── pages/            # Next.js pages
│   ├── styles/           # CSS styles
│   └── package.json      # Node dependencies
├── .env.example          # Environment variables template
└── railway.json          # Railway deployment configuration
```

## 🚀 Quick Setup

### Prerequisites

- Python 3.9+
- Node.js 16+
- OpenAI API Key

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp ../.env.example .env
   # Edit .env and add your OpenAI API key
   ```

4. **Start the backend server:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.local.example .env.local
   # Edit .env.local if needed (defaults to localhost:8000)
   ```

4. **Start the development server:**
   ```bash
   npm run dev
   ```

5. **Open your browser:**
   Visit `http://localhost:3000`

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | API information and available endpoints |
| `GET /health` | Health check endpoint |
| `GET /predict` | Planetary chart and AI interpretation |
| `GET /career` | Career analysis and guidance |
| `GET /dasa` | Vimshottari Dasa timeline |
| `GET /yogas` | Yogas and doshas detection |
| `GET /life_purpose` | Life purpose analysis |
| `GET /dasa_bhukti` | Detailed Dasa-Bhukti analysis |
| `GET /spouse` | Marriage and relationship analysis |
| `GET /indu_dasa` | Indu Dasa analysis |

### Example Usage
```bash
curl "http://localhost:8000/predict?dob=1990-01-01&tob=12:00&lat=13.08&lon=80.28&tz_offset=5.5"
```

## 🏗️ Architecture

- **Backend**: FastAPI with Swiss Ephemeris for astronomical calculations
- **Frontend**: Next.js with React and Tailwind CSS
- **AI**: OpenAI GPT-3.5-turbo for interpretations
- **Deployment**: Railway-ready configuration

## 🔧 Railway Deployment

### Backend Deployment
1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard:
   - `OPENAI_API_KEY`
3. Railway will automatically detect and deploy the FastAPI app

### Frontend Deployment
1. Deploy frontend to Railway or Vercel
2. Update the backend URL in `astro-frontend/pages/index.js`
3. Set environment variables if needed

## 📊 Cost Optimization

- Uses GPT-3.5-turbo instead of GPT-4 for 90% cost savings
- Estimated cost: ~$0.0015 per request vs $0.015 with GPT-4

## 🔒 Security Considerations

- CORS configured for production domains
- Input validation and error handling
- Environment variable protection
- Rate limiting recommended for production

## 📝 License

MIT License - see LICENSE file for details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues and questions, please open an issue on GitHub. 