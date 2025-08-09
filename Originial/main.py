
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from astrology import get_planet_positions, generate_gpt_prompt, get_astrology_interpretation
import swisseph as swe
import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper function to convert date/time to Julian Day
def get_julian_day(dob, tob, tz_offset=5.5):
    date_obj = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    date_obj = date_obj - datetime.timedelta(hours=tz_offset)
    jd = swe.julday(date_obj.year, date_obj.month, date_obj.day, 
                    date_obj.hour + date_obj.minute/60.0)
    return jd

@app.get("/")
def read_root():
    return {"message": "Vedic Astrology API"}

@app.get("/predict")
def predict(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
        prompt = generate_gpt_prompt(data)
        interpretation = get_astrology_interpretation(prompt)
        return {"chart": data, "interpretation": interpretation}
    except Exception as e:
        return {"error": str(e)}

@app.get("/career")
def career(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        # For now, return a placeholder career analysis
        career_report = f"Career analysis for {dob} at {tob} (Lat: {lat}, Lon: {lon})"
        return {"career_report": career_report}
    except Exception as e:
        return {"error": str(e)}

@app.get("/dasa")
def dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        # For now, return a placeholder dasa timeline
        dasa_table = [
            {"planet": "Sun", "start_age": 0, "end_age": 6, "start_date": "1977-10-29", "end_date": "1983-10-29"},
            {"planet": "Moon", "start_age": 6, "end_age": 16, "start_date": "1983-10-29", "end_date": "1993-10-29"}
        ]
        return {"dasa_table": dasa_table}
    except Exception as e:
        return {"error": str(e)}

@app.get("/yogas")
def yogas(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        # For now, return placeholder yogas
        yogas_list = ["Gajakesari Yoga", "Amala Yoga", "Kemadruma Yoga"]
        return {"yogas": yogas_list}
    except Exception as e:
        return {"error": str(e)}

@app.get("/life_purpose")
def life_purpose(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        # For now, return a placeholder life purpose analysis
        life_purpose_analysis = {
            "interpretation": f"Life purpose analysis for {dob} at {tob} (Lat: {lat}, Lon: {lon})"
        }
        return life_purpose_analysis
    except Exception as e:
        return {"error": str(e)}

@app.get("/dasa_bhukti")
def dasa_bhukti(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        # For now, return a placeholder dasa bhukti analysis
        dasa_bhukti_analysis = {
            "birth_info": {"dob": dob, "tob": tob, "place": f"Lat: {lat}, Lon: {lon}"},
            "planetary_positions": {},
            "dasa_table": [],
            "gpt_prediction": f"Dasa bhukti analysis for {dob} at {tob}"
        }
        return dasa_bhukti_analysis
    except Exception as e:
        return {"error": str(e)}

@app.get("/spouse")
def spouse(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5, gender: str = "Male"):
    try:
        # For now, return a placeholder spouse analysis
        spouse_analysis = {
            "chart": {},
            "report": f"Spouse analysis for {gender} born on {dob} at {tob}",
            "interpretation": f"Detailed spouse analysis for {gender} born on {dob} at {tob}"
        }
        return spouse_analysis
    except Exception as e:
        return {"error": str(e)}

@app.get("/indu_dasa")
def indu_dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    try:
        # For now, return a placeholder indu dasa analysis
        indu_dasa_analysis = {
            "ascendant": "Aries",
            "moon_rasi": "Taurus", 
            "indu_lagnam": "Gemini",
            "indu_lord": "Mercury",
            "planets_in_indu_lagnam": ["Sun", "Venus"],
            "timeline": [
                {"maha_dasa": "Sun", "bukti": "Sun", "start": "1977-10-29", "end": "1983-10-29"},
                {"maha_dasa": "Moon", "bukti": "Moon", "start": "1983-10-29", "end": "1993-10-29"}
            ]
        }
        return indu_dasa_analysis
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
