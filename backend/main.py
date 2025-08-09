from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import logging
import os
from dotenv import load_dotenv

# Try to import swisseph, fallback if not available
try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
except ImportError:
    SWISSEPH_AVAILABLE = False
    swe = None

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Imports from modules ---
# Temporarily commented out due to swisseph dependency
# from modules.astrology import get_planet_positions, generate_gpt_prompt, get_astrology_interpretation
# from modules.career import analyze_career, generate_career_report, get_planet_positions as get_career_planet_positions
# from modules.allyogas import detect_yogas, get_planet_positions as get_yogas_planet_positions
# from modules.dasa import generate_dasa_table
# from modules.life_purpose import analyze_life_purpose, generate_purpose_report, ask_gpt, get_planet_positions as get_life_purpose_planet_positions
# from modules.dasa_bhukti import get_planet_positions as get_dasa_bhukti_planet_positions, generate_dasa_table as generate_dasa_bhukti_table, ask_gpt_dasa_prediction
# from modules.spouse_analysis import get_planet_positions as get_spouse_planet_positions, get_aspects, analyze_marriage, generate_report, ask_gpt_spouse
# from modules.indu_dasa import get_indu_dasa

# --- FastAPI App ---
app = FastAPI(
    title="Vedic Astrology API",
    description="A comprehensive Vedic astrology API with planetary calculations and AI-powered interpretations",
    version="1.0.0"
)

# --- CORS Settings ---
# Updated for Vercel frontend deployment
origins = [
    "http://localhost:3000",  # Local development
    "https://*.vercel.app",   # All Vercel domains
    "https://vercel.app",     # Vercel main domain
    "*"  # Allow all origins for now (can be restricted later)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=False,  # Changed to False for wildcard origins
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# ---------------- HEALTH CHECK ----------------
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.0"
    }

# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {
        "message": "Vedic Astrology API is running",
        "endpoints": [
            "/predict - Planetary chart and interpretation",
            "/career - Career analysis",
            "/dasa - Vimshottari Dasa timeline",
            "/yogas - Yogas and doshas",
            "/life_purpose - Life purpose analysis",
            "/dasa_bhukti - Detailed Dasa-Bhukti analysis",
            "/spouse - Marriage and relationship analysis",
            "/indu_dasa - Indu Dasa analysis"
        ],
        "docs": "/docs"
    }

# ---------------- PREDICT ----------------
@app.get("/predict")
def predict(dob: str,
            tob: str,
            lat: float,
            lon: float,
            tz_offset: float = 5.5):
    return {
        "status": "under_maintenance",
        "message": "Astrological calculations are temporarily unavailable while we resolve Swiss Ephemeris compatibility issues. Please check back soon!",
        "chart": {},
        "interpretation": "Service temporarily unavailable - Swiss Ephemeris integration in progress."
    }

# Temporarily disabled endpoints - Swiss Ephemeris compatibility in progress
# All astrology endpoints return maintenance message

def maintenance_response():
    return {
        "status": "under_maintenance",
        "message": "Astrological calculations are temporarily unavailable while we resolve Swiss Ephemeris compatibility issues. Please check back soon!",
        "data": {},
        "report": "Service temporarily unavailable - Swiss Ephemeris integration in progress."
    }

@app.get("/career")
def career(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5, gender: str = "Male"):
    return maintenance_response()

@app.get("/dasa") 
def dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    return maintenance_response()

@app.get("/yogas")
def yogas(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    return maintenance_response()

@app.get("/life_purpose")
def life_purpose(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    return maintenance_response()

@app.get("/dasa_bhukti")
def dasa_bhukti(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    return maintenance_response()

@app.get("/spouse")
def spouse(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5, gender: str = "Male"):
    return maintenance_response()

@app.get("/indu_dasa")
def indu_dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    return maintenance_response()

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
