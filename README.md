# 🔮 Vedic Astrology API

A comprehensive Vedic astrology application with AI-powered interpretations, built with FastAPI backend and React frontend.

## 🌟 Features

- **Planetary Chart Analysis** - Accurate calculations using Swiss Ephemeris
- **AI-Powered Interpretations** - GPT-3.5-turbo for cost-effective insights
- **8 Different Analysis Types**:
  - Planetary predictions and interpretations
  - Career analysis and guidance
  - Vimshottari Dasa timeline
  - Yogas and doshas detection
  - Life purpose analysis
  - Detailed Dasa-Bhukti analysis
  - Marriage and relationship analysis
  - Indu Dasa analysis

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- OpenAI API key

### Backend Setup
```bash
cd astro-backend/astro-backend
pip install -r requirements.txt
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend Setup
```bash
cd astro-frontend
npm install
npm run dev
```

### Environment Variables
Create `.env` file in `astro-backend/astro-backend/`:
```
OPENAI_API_KEY=your_openai_api_key_here
```

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