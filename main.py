from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# FastAPI App
app = FastAPI(
    title="Vedic Astrology API",
    description="A comprehensive Vedic astrology API",
    version="1.0.0"
)

# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.0",
        "message": "Vedic Astrology API is running successfully!"
    }

@app.get("/")
def root():
    return {
        "message": "🔮 Vedic Astrology API",
        "status": "online",
        "frontend": "https://aiastroprediction.vercel.app",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "predict": "/predict - Coming soon!",
            "career": "/career - Coming soon!",
            "dasa": "/dasa - Coming soon!"
        }
    }

@app.get("/predict")
def predict(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    return {
        "status": "coming_soon",
        "message": "✨ Astrological calculations coming soon! Swiss Ephemeris integration in progress.",
        "input": {
            "date_of_birth": dob,
            "time_of_birth": tob,
            "latitude": lat,
            "longitude": lon,
            "timezone_offset": tz_offset
        },
        "note": "This endpoint will provide complete planetary chart analysis once astronomical calculations are integrated."
    }

@app.get("/career")
def career(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5, gender: str = "Male"):
    return {
        "status": "coming_soon",
        "message": "💼 Career analysis coming soon!",
        "features": ["Career path analysis", "Professional strengths", "Ideal career timing", "Business prospects"]
    }

@app.get("/dasa")
def dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    return {
        "status": "coming_soon", 
        "message": "📈 Dasa timeline coming soon!",
        "features": ["Vimshottari Dasa periods", "Life event timing", "Planetary influences", "Future predictions"]
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Starting Vedic Astrology API on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")