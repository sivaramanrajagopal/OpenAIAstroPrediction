from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try importing pyswisseph with error handling
try:
    import pyswisseph as swe
    swe.set_ephe_path('')  # Use built-in ephemeris
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    PYSWISSEPH_AVAILABLE = True
    print("✅ PySwisseph imported successfully")
except ImportError as e:
    print(f"❌ PySwisseph import failed: {e}")
    PYSWISSEPH_AVAILABLE = False
    swe = None

# Import your modules
from astrology import get_planet_positions, generate_gpt_prompt, get_astrology_interpretation
from carear import analyze_career, generate_career_report
from allyogas import detect_yogas
from dasa import generate_dasa_table
from life_purpose import analyze_life_purpose, generate_purpose_report
from dasa_bhukti import get_planet_positions as get_dasa_positions, generate_dasa_table as generate_dasa_bhukti_table
from spouse_analysis import get_planet_positions as get_spouse_positions, get_aspects as get_spouse_aspects, analyze_marriage, generate_report as spouse_report
from indu_dasa import get_indu_dasa

# FastAPI App
app = FastAPI(
    title="Vedic Astrology API",
    description="A comprehensive Vedic astrology API with planetary calculations and AI-powered interpretations",
    version="1.0.0"
)

# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "pyswisseph_available": PYSWISSEPH_AVAILABLE,
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.0"
    }

@app.get("/")
def root():
    return {
        "message": "Vedic Astrology API is running",
        "pyswisseph_status": "Available" if PYSWISSEPH_AVAILABLE else "Not Available",
        "endpoints": [
            "/predict - Planetary chart and interpretation",
            "/career - Career analysis", 
            "/dasa - Vimshottari Dasa timeline",
            "/yogas - Yogas and doshas",
            "/health - Health check"
        ],
        "docs": "/docs"
    }

# Your existing endpoints here...
@app.get("/predict")
def predict(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    if not PYSWISSEPH_AVAILABLE:
        raise HTTPException(status_code=503, detail="PySwisseph not available")
    
    try:
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
        prompt = generate_gpt_prompt(data)
        interpretation = get_astrology_interpretation(prompt)
        return {"chart": data, "interpretation": interpretation}
    except Exception as e:
        logger.error(f"Error in predict endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# Add all your other endpoints...
@app.get("/career")
def career(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5, gender: str = "Male"):
    if not PYSWISSEPH_AVAILABLE:
        raise HTTPException(status_code=503, detail="PySwisseph not available")
    
    try:
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
        analysis = analyze_career(data, asc_deg, cusps, gender)
        report = generate_career_report(analysis)
        return {"analysis": analysis, "report": report}
    except Exception as e:
        logger.error(f"Error in career endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/dasa")
def dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    if not PYSWISSEPH_AVAILABLE:
        raise HTTPException(status_code=503, detail="PySwisseph not available")
    
    try:
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
        # Calculate Julian Day and Moon longitude for dasa
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
        moon_longitude = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
        dasa_table = generate_dasa_table(jd, moon_longitude)
        return {"dasa_table": dasa_table}
    except Exception as e:
        logger.error(f"Error in dasa endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/yogas")
def yogas(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    if not PYSWISSEPH_AVAILABLE:
        raise HTTPException(status_code=503, detail="PySwisseph not available")
    
    try:
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
        yogas = detect_yogas(data)
        return {"yogas": yogas}
    except Exception as e:
        logger.error(f"Error in yogas endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/life_purpose")
def life_purpose(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    if not PYSWISSEPH_AVAILABLE:
        raise HTTPException(status_code=503, detail="PySwisseph not available")
    
    try:
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
        analysis = analyze_life_purpose(data, asc_deg, cusps)
        report = generate_purpose_report(analysis)
        return {"analysis": analysis, "report": report}
    except Exception as e:
        logger.error(f"Error in life_purpose endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/dasa_bhukti")
def dasa_bhukti(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    if not PYSWISSEPH_AVAILABLE:
        raise HTTPException(status_code=503, detail="PySwisseph not available")
    
    try:
        data, asc_deg, cusps = get_dasa_positions(dob, tob, lat, lon, tz_offset)
        # Calculate Julian Day and Moon longitude for dasa bhukti
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
        moon_longitude = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
        dasa_table = generate_dasa_bhukti_table(jd, moon_longitude)
        return {"dasa_bhukti_table": dasa_table}
    except Exception as e:
        logger.error(f"Error in dasa_bhukti endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/spouse")
def spouse(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5, gender: str = "Male"):
    if not PYSWISSEPH_AVAILABLE:
        raise HTTPException(status_code=503, detail="PySwisseph not available")
    
    try:
        data, asc_deg, cusps = get_spouse_positions(dob, tob, lat, lon, tz_offset)
        aspects = get_spouse_aspects(data, asc_deg)
        analysis = analyze_marriage(data, asc_deg, aspects, gender)
        report = spouse_report(analysis)
        return {"analysis": analysis, "report": report}
    except Exception as e:
        logger.error(f"Error in spouse endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/indu_dasa")
def indu_dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    if not PYSWISSEPH_AVAILABLE:
        raise HTTPException(status_code=503, detail="PySwisseph not available")
    
    try:
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
        indu_dasa_data = get_indu_dasa(dob, tob, lat, lon, tz_offset)
        return {"indu_dasa": indu_dasa_data}
    except Exception as e:
        logger.error(f"Error in indu_dasa endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
# Force Railway redeploy - Sat Aug  2 10:59:26 IST 2025
