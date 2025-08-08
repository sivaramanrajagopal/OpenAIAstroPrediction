from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import swisseph as swe
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Imports from modules ---
from modules.astrology import get_planet_positions, generate_gpt_prompt, get_astrology_interpretation
from modules.career import analyze_career, generate_career_report, get_planet_positions as get_career_planet_positions
from modules.allyogas import detect_yogas, get_planet_positions as get_yogas_planet_positions
from modules.dasa import generate_dasa_table
from modules.life_purpose import analyze_life_purpose, generate_purpose_report, ask_gpt, get_planet_positions as get_life_purpose_planet_positions
from modules.dasa_bhukti import get_planet_positions as get_dasa_bhukti_planet_positions, generate_dasa_table as generate_dasa_bhukti_table, ask_gpt_dasa_prediction
from modules.spouse_analysis import get_planet_positions as get_spouse_planet_positions, get_aspects, analyze_marriage, generate_report, ask_gpt_spouse
from modules.indu_dasa import get_indu_dasa

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
    try:
        logger.info(f"Predict endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
        prompt = generate_gpt_prompt(data)
        interpretation = get_astrology_interpretation(prompt)
        return {"chart": data, "interpretation": interpretation}
    except Exception as e:
        logger.error(f"Error in predict endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ---------------- CAREER ----------------
@app.get("/career")
def career(dob: str,
           tob: str,
           lat: float,
           lon: float,
           tz_offset: float = 5.5,
           gender: str = "Male"):
    try:
        logger.info(f"Career endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}, gender={gender}")
        # Calculate Julian Day
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
        
        # Get planetary positions first
        data, asc_deg, cusps = get_career_planet_positions(jd, lat, lon)
        # Then analyze career with the planetary data
        analysis = analyze_career(data, asc_deg, cusps, gender)
        report = generate_career_report(analysis, asc_deg)
        return {"career_analysis": analysis, "report": report}
    except Exception as e:
        logger.error(f"Error in career endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ---------------- DASA ----------------
@app.get("/dasa")
def dasa(dob: str,
         tob: str,
         lat: float,
         lon: float,
         tz_offset: float = 5.5):
    try:
        logger.info(f"Dasa endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                        utc_dt.hour + utc_dt.minute / 60.0)
        swe.set_topo(lon, lat, 0)
        moon_longitude = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
        data = generate_dasa_table(jd, moon_longitude)
        return data
    except Exception as e:
        logger.error(f"Error in dasa endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ---------------- YOGAS ----------------
@app.get("/yogas")
def yogas(dob: str,
          tob: str,
          lat: float,
          lon: float,
          tz_offset: float = 5.5):
    try:
        logger.info(f"Yogas endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        # Get planetary positions first
        data = get_yogas_planet_positions(dob, tob, lat, lon, tz_offset)
        # Then detect yogas with the planetary data
        yogas = detect_yogas(data)
        return {"yogas": yogas}
    except Exception as e:
        logger.error(f"Error in yogas endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ---------------- LIFE PURPOSE ----------------
@app.get("/life_purpose")
def life_purpose(dob: str,
                tob: str,
                lat: float,
                lon: float,
                tz_offset: float = 5.5):
    try:
        logger.info(f"Life purpose endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        # Calculate Julian Day
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
        
        # Get planetary positions first
        data, asc_deg, cusps = get_life_purpose_planet_positions(jd, lat, lon)
        # Then analyze life purpose with the planetary data
        analysis = analyze_life_purpose(data, asc_deg, cusps)
        report = generate_purpose_report(analysis, data)
        return {"life_purpose_analysis": analysis, "report": report}
    except Exception as e:
        logger.error(f"Error in life_purpose endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ---------------- DASA BHUKTI ----------------
@app.get("/dasa_bhukti")
def dasa_bhukti(dob: str,
                tob: str,
                lat: float,
                lon: float,
                tz_offset: float = 5.5):
    try:
        logger.info(f"Dasa bhukti endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        # Calculate Julian Day
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
        
        # Get planetary positions
        data, asc_deg, cusps = get_dasa_bhukti_planet_positions(jd, lat, lon)
        # Generate dasa table
        moon_longitude = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
        table = generate_dasa_bhukti_table(jd, moon_longitude)
        return {"dasa_bhukti_analysis": data, "table": table}
    except Exception as e:
        logger.error(f"Error in dasa_bhukti endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ---------------- SPOUSE ----------------
@app.get("/spouse")
def spouse(dob: str,
          tob: str,
          lat: float,
          lon: float,
          tz_offset: float = 5.5,
          gender: str = "Male"):
    try:
        logger.info(f"Spouse endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}, gender={gender}")
        # Calculate Julian Day
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
        
        # Get planetary positions
        data, asc_deg = get_spouse_planet_positions(jd, lat, lon)
        # Get aspects
        aspects = get_aspects(data, asc_deg)
        # Analyze marriage
        analysis = analyze_marriage(data, asc_deg, aspects, gender)
        report = generate_report(analysis)
        return {"spouse_analysis": analysis, "report": report}
    except Exception as e:
        logger.error(f"Error in spouse endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ---------------- INDU DASA ----------------
@app.get("/indu_dasa")
def indu_dasa(dob: str,
              tob: str,
              lat: float,
              lon: float,
              tz_offset: float = 5.5):
    try:
        logger.info(f"Indu dasa endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        data = get_indu_dasa(dob, tob, lat, lon, tz_offset)
        return data
    except Exception as e:
        logger.error(f"Error in indu_dasa endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
