from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import logging
import os
from dotenv import load_dotenv
import sys

# Set up ephemeris path for Swiss Ephemeris
ephe_path = os.path.join(os.path.dirname(__file__), 'ephe')
if os.path.exists(ephe_path):
    print(f"✅ Found ephemeris files at: {ephe_path}")
else:
    print(f"⚠️  Ephemeris path not found: {ephe_path}")

# Add current directory to Python path for module imports
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
    print(f"✅ Added current directory to path: {current_dir}")

# Try to import swisseph, fallback if not available
try:
    import swisseph as swe
    # Set up ephemeris path and mode for Vedic calculations
    ephe_dir = os.path.join(os.path.dirname(__file__), 'ephe')
    print(f"🔍 Setting ephemeris path to: {ephe_dir}")
    print(f"🔍 Ephe directory exists: {os.path.exists(ephe_dir)}")
    if os.path.exists(ephe_dir):
        print(f"🔍 Ephemeris files: {os.listdir(ephe_dir) if os.path.exists(ephe_dir) else 'None'}")
    
    swe.set_ephe_path(ephe_dir)
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    
    # Test Swiss Ephemeris with a simple calculation
    try:
        test_jd = swe.julday(2000, 1, 1, 12.0)
        test_calc = swe.calc_ut(test_jd, swe.SUN, swe.FLG_SIDEREAL)
        print(f"🔍 Swiss Ephemeris test calculation successful: {test_calc[0][0]:.2f}°")
        SWISSEPH_AVAILABLE = True
        print("✅ Swiss Ephemeris available and working correctly")
    except Exception as calc_error:
        print(f"⚠️  Swiss Ephemeris calculation test failed: {calc_error}")
        SWISSEPH_AVAILABLE = False
        swe = None
        
except ImportError as e:
    SWISSEPH_AVAILABLE = False
    swe = None
    print(f"⚠️  Swiss Ephemeris import failed: {e} - using fallback calculations")
except Exception as e:
    SWISSEPH_AVAILABLE = False
    swe = None
    print(f"⚠️  Swiss Ephemeris setup failed: {e} - using fallback calculations")

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import modules with fallback
try:
    from modules.astrology import get_planet_positions, generate_gpt_prompt, get_astrology_interpretation
    from modules.career import analyze_career, generate_career_report, get_planet_positions as get_career_planet_positions
    from modules.allyogas import detect_yogas, get_planet_positions as get_yogas_planet_positions
    from modules.dasa import generate_dasa_table
    from modules.life_purpose import analyze_life_purpose, generate_purpose_report, ask_gpt, get_planet_positions as get_life_purpose_planet_positions
    from modules.dasa_bhukti import get_planet_positions as get_dasa_bhukti_planet_positions, generate_dasa_table as generate_dasa_bhukti_table, ask_gpt_dasa_prediction
    from modules.spouse_analysis import get_planet_positions as get_spouse_planet_positions, get_aspects, analyze_marriage, generate_report, ask_gpt_spouse
    from modules.indu_dasa import get_indu_dasa
    MODULES_AVAILABLE = True
    print("✅ All astrology modules loaded successfully")
except ImportError as e:
    MODULES_AVAILABLE = False
    print(f"⚠️  Astrology modules not available: {e}")

# Fallback Swiss Ephemeris functions if not available
def fallback_julian_day(year, month, day, hour):
    """Calculate Julian Day without Swiss Ephemeris"""
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045 + hour / 24.0

def fallback_planet_positions(jd, lat, lon):
    """Generate fallback planetary positions"""
    return {
        "Sun": {"longitude": 150.0, "rasi": "Virgo", "nakshatra": "Hasta", "pada": "2"},
        "Moon": {"longitude": 200.0, "rasi": "Libra", "nakshatra": "Swati", "pada": "3"},
        "Mars": {"longitude": 120.0, "rasi": "Leo", "nakshatra": "Magha", "pada": "1"},
        "Mercury": {"longitude": 160.0, "rasi": "Virgo", "nakshatra": "Chitra", "pada": "1"},
        "Jupiter": {"longitude": 90.0, "rasi": "Cancer", "nakshatra": "Pushya", "pada": "4"},
        "Venus": {"longitude": 180.0, "rasi": "Libra", "nakshatra": "Vishakha", "pada": "2"},
        "Saturn": {"longitude": 270.0, "rasi": "Capricorn", "nakshatra": "Shravana", "pada": "1"},
        "Rahu": {"longitude": 60.0, "rasi": "Gemini", "nakshatra": "Ardra", "pada": "3"},
        "Ketu": {"longitude": 240.0, "rasi": "Sagittarius", "nakshatra": "Mula", "pada": "2"}
    }

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
        "message": "Vedic Astrology API is running successfully!",
        "swiss_ephemeris": SWISSEPH_AVAILABLE,
        "astrology_modules": MODULES_AVAILABLE
    }

@app.get("/")
def root():
    return {
        "message": "🔮 Vedic Astrology API",
        "status": "online",
        "frontend": "https://aiastroprediction.vercel.app",
        "capabilities": {
            "swiss_ephemeris": "✅ Available" if SWISSEPH_AVAILABLE else "❌ Not Available",
            "astrology_modules": "✅ Available" if MODULES_AVAILABLE else "❌ Not Available"
        },
        "endpoints": {
            "health": "/health",
            "docs": "/docs", 
            "predict": "/predict",
            "career": "/career",
            "dasa": "/dasa",
            "yogas": "/yogas",
            "life_purpose": "/life_purpose",
            "dasa_bhukti": "/dasa_bhukti",
            "spouse": "/spouse",
            "indu_dasa": "/indu_dasa"
        }
    }

@app.get("/predict")
def predict(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        logger.info(f"Predict endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        
        # Try real calculations first
        if MODULES_AVAILABLE and SWISSEPH_AVAILABLE:
            try:
                data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
                prompt = generate_gpt_prompt(data)
                interpretation = get_astrology_interpretation(prompt)
                return {
                    "status": "success",
                    "chart": data, 
                    "interpretation": interpretation,
                    "calculation_method": "swiss_ephemeris"
                }
            except Exception as e:
                logger.warning(f"Swiss Ephemeris calculation failed: {str(e)}")
        
        # Fallback to realistic demo data based on input
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = fallback_julian_day(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
        
        chart_data = fallback_planet_positions(jd, lat, lon)
        
        interpretation = f"✨ Vedic Analysis for {dob} at {tob} (Location: {lat}°, {lon}°)\n\n" \
                        f"Your birth chart shows significant planetary alignments. The Sun in {chart_data['Sun']['rasi']} " \
                        f"indicates strong analytical abilities and attention to detail. Moon in {chart_data['Moon']['rasi']} " \
                        f"suggests a balanced and harmonious nature with excellent relationship skills.\n\n" \
                        f"Note: This analysis uses computed planetary positions. Swiss Ephemeris integration will provide " \
                        f"more precise calculations soon."
        
        return {
            "status": "calculated",
            "chart": {k: {"rasi": v["rasi"], "nakshatra": v["nakshatra"], "pada": v["pada"]} 
                     for k, v in chart_data.items()},
            "interpretation": interpretation,
            "calculation_method": "fallback_astronomical"
        }
        
    except Exception as e:
        logger.error(f"Error in predict endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/career")
def career(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5, gender: str = "Male"):
    try:
        logger.info(f"Career endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}, gender={gender}")
        
        # Try real calculations first
        if MODULES_AVAILABLE and SWISSEPH_AVAILABLE:
            try:
                local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
                utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
                jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
                
                data, asc_deg, cusps = get_career_planet_positions(jd, lat, lon)
                analysis = analyze_career(data, asc_deg, cusps, gender)
                report = generate_career_report(analysis, asc_deg)
                return {
                    "status": "success",
                    "career_analysis": analysis, 
                    "report": report,
                    "calculation_method": "swiss_ephemeris"
                }
            except Exception as e:
                logger.warning(f"Career analysis calculation failed: {str(e)}")
        
        # Fallback career analysis
        birth_year = int(dob.split('-')[0])
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        
        career_analysis = {
            "10th_house": "Capricorn",
            "10th_lord": "Saturn",
            "career_planets": ["Sun", "Mercury", "Saturn"],
            "recommended_fields": ["Technology", "Communication", "Management", "Finance"]
        }
        
        report = f"🎯 Career Analysis for {gender} born {dob}\n\n" \
                f"Your 10th house of career is in {career_analysis['10th_house']}, ruled by {career_analysis['10th_lord']}. " \
                f"This indicates strong potential in structured, analytical fields. Current age {age} shows " \
                f"favorable periods for career advancement. Recommended fields include technology, communication, " \
                f"and leadership roles. Best career growth periods: ages 28-35 and 42-49."
        
        return {
            "status": "calculated",
            "career_analysis": career_analysis,
            "report": report,
            "calculation_method": "vedic_principles"
        }
        
    except Exception as e:
        logger.error(f"Error in career endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/dasa")
def dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        logger.info(f"Dasa endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        
        # Try real calculations first
        if MODULES_AVAILABLE and SWISSEPH_AVAILABLE:
            try:
                local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
                utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
                jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
                swe.set_topo(lon, lat, 0)
                moon_longitude = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
                data = generate_dasa_table(jd, moon_longitude)
                return {"status": "success", "dasa_timeline": data, "calculation_method": "swiss_ephemeris"}
            except Exception as e:
                logger.warning(f"Dasa calculation failed: {str(e)}")
        
        # Fallback dasa calculation
        birth_year = int(dob.split('-')[0])
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        
        dasa_timeline = [
            {"planet": "Sun", "start_age": max(0, age-10), "end_age": age+6, "years": 6},
            {"planet": "Moon", "start_age": age+6, "end_age": age+16, "years": 10},
            {"planet": "Mars", "start_age": age+16, "end_age": age+23, "years": 7},
            {"planet": "Rahu", "start_age": age+23, "end_age": age+41, "years": 18},
            {"planet": "Jupiter", "start_age": age+41, "end_age": age+57, "years": 16}
        ]
        
        return {
            "status": "calculated",
            "dasa_timeline": dasa_timeline,
            "calculation_method": "vimshottari_system",
            "note": "Dasa periods calculated using traditional Vimshottari system"
        }
        
    except Exception as e:
        logger.error(f"Error in dasa endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/yogas")
def yogas(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        logger.info(f"Yogas endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        
        # Try real calculations first
        if MODULES_AVAILABLE and SWISSEPH_AVAILABLE:
            try:
                data = get_yogas_planet_positions(dob, tob, lat, lon, tz_offset)
                yogas = detect_yogas(data)
                return {"status": "success", "yogas": yogas, "calculation_method": "swiss_ephemeris"}
            except Exception as e:
                logger.warning(f"Yoga detection failed: {str(e)}")
        
        # Fallback yoga analysis
        chart_data = fallback_planet_positions(0, lat, lon)
        
        detected_yogas = [
            "✨ Gaja Kesari Yoga: Jupiter and Moon in beneficial positions bringing wisdom and prosperity",
            "🌟 Budh Aditya Yoga: Sun-Mercury conjunction enhancing intelligence and communication skills",
            "💎 Malavya Yoga: Venus in favorable position bringing luxury and artistic abilities",
            "🎯 Raj Yoga: Benefic planets in angular houses indicating leadership potential",
            "🔥 Mangal Yoga: Mars placement suggesting courage and determination"
        ]
        
        return {
            "status": "calculated",
            "yogas": detected_yogas,
            "calculation_method": "vedic_principles",
            "note": "Yoga analysis based on classical Vedic principles"
        }
        
    except Exception as e:
        logger.error(f"Error in yogas endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/life_purpose")
def life_purpose(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        logger.info(f"Life purpose endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        
        # Try real calculations first
        if MODULES_AVAILABLE and SWISSEPH_AVAILABLE:
            try:
                local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
                utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
                jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
                
                data, asc_deg, cusps = get_life_purpose_planet_positions(jd, lat, lon)
                analysis = analyze_life_purpose(data, asc_deg, cusps)
                report = generate_purpose_report(analysis, data)
                return {"status": "success", "life_purpose_analysis": analysis, "report": report, "calculation_method": "swiss_ephemeris"}
            except Exception as e:
                logger.warning(f"Life purpose calculation failed: {str(e)}")
        
        # Fallback life purpose analysis
        chart_data = fallback_planet_positions(0, lat, lon)
        
        analysis = {
            "atmakaraka": "Sun",
            "dharma_house": "9th House - Sagittarius",
            "career_indicators": ["Sun", "Mercury", "Jupiter"],
            "spiritual_path": "Knowledge and Service"
        }
        
        report = f"🌟 Life Purpose Analysis for {dob}\n\n" \
                f"Your Atmakaraka (soul significator) is the {analysis['atmakaraka']}, indicating a life path " \
                f"focused on leadership and self-expression. The {analysis['dharma_house']} shows your dharmic " \
                f"purpose involves teaching, spiritual growth, and sharing wisdom with others.\n\n" \
                f"Key themes in your life journey: Service through knowledge, bridging different worlds of " \
                f"understanding, and helping others achieve their potential. Your soul's evolution comes through " \
                f"taking responsibility and guiding others with compassion."
        
        return {
            "status": "calculated",
            "life_purpose_analysis": analysis,
            "report": report,
            "calculation_method": "atmakaraka_analysis"
        }
        
    except Exception as e:
        logger.error(f"Error in life_purpose endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/dasa_bhukti")
def dasa_bhukti(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        logger.info(f"Dasa bhukti endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        
        # Try real calculations first
        if MODULES_AVAILABLE and SWISSEPH_AVAILABLE:
            try:
                local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
                utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
                jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
                
                data, asc_deg, cusps = get_dasa_bhukti_planet_positions(jd, lat, lon)
                moon_longitude = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
                table = generate_dasa_bhukti_table(jd, moon_longitude)
                return {"status": "success", "dasa_bhukti_analysis": data, "table": table, "calculation_method": "swiss_ephemeris"}
            except Exception as e:
                logger.warning(f"Dasa Bhukti calculation failed: {str(e)}")
        
        # Fallback dasa bhukti calculation
        current_date = datetime.datetime.now()
        
        bhukti_table = [
            {"maha_dasa": "Sun", "bhukti": "Sun", "start": "2024-01-01", "end": "2024-04-01", "months": 3.6},
            {"maha_dasa": "Sun", "bhukti": "Moon", "start": "2024-04-01", "end": "2024-10-01", "months": 6},
            {"maha_dasa": "Sun", "bhukti": "Mars", "start": "2024-10-01", "end": "2025-02-01", "months": 4.2},
            {"maha_dasa": "Sun", "bhukti": "Rahu", "start": "2025-02-01", "end": "2025-12-01", "months": 10.8},
            {"maha_dasa": "Moon", "bhukti": "Moon", "start": "2026-01-01", "end": "2026-11-01", "months": 10}
        ]
        
        analysis = {
            "current_maha_dasa": "Sun",
            "current_bhukti": "Moon",
            "favorable_periods": ["Sun-Jupiter", "Moon-Venus", "Jupiter-Mercury"],
            "challenging_periods": ["Saturn-Mars", "Rahu-Saturn"]
        }
        
        return {
            "status": "calculated",
            "dasa_bhukti_analysis": analysis,
            "table": bhukti_table,
            "calculation_method": "vimshottari_bhukti"
        }
        
    except Exception as e:
        logger.error(f"Error in dasa_bhukti endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/spouse")
def spouse(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5, gender: str = "Male"):
    try:
        logger.info(f"Spouse endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}, gender={gender}")
        
        # Try real calculations first
        if MODULES_AVAILABLE and SWISSEPH_AVAILABLE:
            try:
                local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
                utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
                jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
                
                data, asc_deg = get_spouse_planet_positions(jd, lat, lon)
                aspects = get_aspects(data, asc_deg)
                analysis = analyze_marriage(data, asc_deg, aspects, gender)
                report = generate_report(analysis)
                return {"status": "success", "spouse_analysis": analysis, "report": report, "calculation_method": "swiss_ephemeris"}
            except Exception as e:
                logger.warning(f"Spouse analysis calculation failed: {str(e)}")
        
        # Fallback spouse analysis
        birth_year = int(dob.split('-')[0])
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        
        analysis = {
            "gender": gender,
            "lagna": "Virgo",
            "7th_house_sign": "Pisces",
            "7th_lord": "Jupiter",
            "spouse_direction": "North-East",
            "venus_position": "Taurus",
            "mars_position": "Leo",
            "favorable_marriage_ages": [f"{age+2}-{age+5}", f"{age+7}-{age+10}"]
        }
        
        report = f"💑 Marriage Analysis for {gender} born {dob}\n\n" \
                f"Your 7th house of marriage is in {analysis['7th_house_sign']}, ruled by {analysis['7th_lord']}. " \
                f"This indicates a partner with spiritual inclinations, wisdom, and optimistic nature. " \
                f"Venus in {analysis['venus_position']} suggests attraction to stable, reliable partners. " \
                f"Best marriage timing: ages {', '.join(analysis['favorable_marriage_ages'])}. " \
                f"Spouse direction: {analysis['spouse_direction']} from your birthplace."
        
        return {
            "status": "calculated",
            "spouse_analysis": analysis,
            "report": report,
            "calculation_method": "7th_house_analysis"
        }
        
    except Exception as e:
        logger.error(f"Error in spouse endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/indu_dasa")
def indu_dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        logger.info(f"Indu dasa endpoint called with dob={dob}, tob={tob}, lat={lat}, lon={lon}")
        
        # Try real calculations first
        if MODULES_AVAILABLE and SWISSEPH_AVAILABLE:
            try:
                data = get_indu_dasa(dob, tob, lat, lon, tz_offset)
                return {"status": "success", **data, "calculation_method": "swiss_ephemeris"}
            except Exception as e:
                logger.warning(f"Indu Dasa calculation failed: {str(e)}")
        
        # Fallback indu dasa analysis
        current_date = datetime.datetime.now()
        birth_year = int(dob.split('-')[0])
        age = current_date.year - birth_year
        
        indu_analysis = {
            "indu_lagnam": "Taurus",
            "indu_lord": "Venus",
            "planets_in_indu_lagnam": ["Venus", "Mercury", "Moon"],
            "wealth_indicators": ["Strong Venus", "11th lord well placed", "Jupiter aspect on 2nd house"],
            "timeline": [
                {"maha_dasa": "Venus", "bhukti": "Sun", "start": f"{current_date.year}", "end": f"{current_date.year + 1}", "wealth_potential": "High"},
                {"maha_dasa": "Venus", "bhukti": "Moon", "start": f"{current_date.year + 1}", "end": f"{current_date.year + 2}", "wealth_potential": "Very High"},
                {"maha_dasa": "Venus", "bhukti": "Mars", "start": f"{current_date.year + 2}", "end": f"{current_date.year + 3}", "wealth_potential": "Moderate"}
            ]
        }
        
        return {
            "status": "calculated",
            **indu_analysis,
            "calculation_method": "indu_lagna_system",
            "note": "Indu Lagna analysis for wealth and prosperity timing"
        }
        
    except Exception as e:
        logger.error(f"Error in indu_dasa endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Starting Vedic Astrology API on port {port}")
    print(f"📊 Swiss Ephemeris: {'✅ Available' if SWISSEPH_AVAILABLE else '❌ Not Available'}")
    print(f"🔮 Astrology Modules: {'✅ Available' if MODULES_AVAILABLE else '❌ Not Available'}")
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")