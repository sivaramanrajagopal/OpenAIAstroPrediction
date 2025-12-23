import swisseph as swe
import datetime
from collections import OrderedDict
from openai import OpenAI
import os

# --- Load OpenAI API Key ---
# Only create client when needed, not at import time
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return OpenAI(api_key=api_key)
    return None

# --- CONSTANTS ---
nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

rasis = [
    "Mesha", "Rishaba", "Mithuna", "Kataka", "Simha", "Kanni",
    "Thula", "Vrischika", "Dhanus", "Makara", "Kumbha", "Meena"
]

planets = {
    0: "Sun", 1: "Moon", 2: "Mars", 3: "Mercury", 4: "Jupiter",
    5: "Venus", 6: "Saturn", 7: "Uranus", 8: "Neptune", 9: "Pluto"
}

# Nakshatra lords cycle
nakshatra_lords = (
    ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"] * 3
)

dasa_durations = OrderedDict([
    ("Ketu", 7), ("Venus", 20), ("Sun", 6), ("Moon", 10),
    ("Mars", 7), ("Rahu", 18), ("Jupiter", 16), ("Saturn", 19), ("Mercury", 17)
])

# --- SWISS EPHEMERIS SETUP ---
swe.set_ephe_path('./ephe')
swe.set_sid_mode(swe.SIDM_LAHIRI)

# --- HELPER FUNCTIONS ---
def get_chart_info(longitude, speed=None):
    """Return planet's chart info."""
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else False,
        'rasi': rasis[int(longitude // 30)],
        'nakshatra': nakshatras[int((longitude % 360) // (360 / 27))],
        'pada': int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1),
    }

def get_planet_positions(jd, lat, lon):
    """Return planetary positions for given Julian Day."""
    FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED
    results = {}
    swe.set_topo(lon, lat, 0)

    for pid in range(0, 10):
        name = planets[pid]
        lonlat = swe.calc_ut(jd, pid, FLAGS)[0]
        results[name] = get_chart_info(lonlat[0], lonlat[3])

    # Rahu & Ketu - Use MEAN_NODE as per Parasara principles
    # Mean nodes are traditional in Vedic astrology
    rahu = swe.calc_ut(jd, swe.MEAN_NODE, FLAGS)[0]
    results['Rahu'] = get_chart_info(rahu[0], rahu[3])
    ketu_lon = (rahu[0] + 180.0) % 360.0
    ketu_info = get_chart_info(ketu_lon, rahu[3])
    ketu_info['retrograde'] = True
    results['Ketu'] = ketu_info

    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'O', flags=FLAGS)
    results['Ascendant'] = get_chart_info(ascmc[0])
    return results, ascmc[0], cusps

def get_nakshatra(longitude):
    """Return nakshatra, pada, and index for a given longitude."""
    nakshatra_index = int((longitude % 360) // (360 / 27))
    pada = int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1)
    return nakshatras[nakshatra_index], pada, nakshatra_index

def calculate_dasa_start(moon_longitude):
    """Calculate starting dasa and remaining years."""
    nakshatra, pada, nakshatra_index = get_nakshatra(moon_longitude)
    nakshatra_length = 360 / 27
    remainder = moon_longitude % nakshatra_length
    portion_completed = remainder / nakshatra_length

    current_dasa_lord = nakshatra_lords[nakshatra_index]
    total_dasa_years = dasa_durations[current_dasa_lord]
    remaining_years = total_dasa_years * (1 - portion_completed)

    return nakshatra, pada, current_dasa_lord, remaining_years

def generate_dasa_table(jd, moon_longitude, total_years=120):
    """Generate full Vimshottari Dasa table."""
    nakshatra, pada, current_dasa_lord, remaining_years = calculate_dasa_start(moon_longitude)
    start_year, start_month, start_day = swe.revjul(jd)[:3]
    start_date = datetime.datetime(start_year, start_month, start_day)

    dasa_table = []
    current_year = 0
    current_index = list(dasa_durations.keys()).index(current_dasa_lord)

    while current_year < total_years:
        for i in range(current_index, current_index + len(dasa_durations)):
            planet = list(dasa_durations.keys())[i % len(dasa_durations)]
            duration = dasa_durations[planet]
            if i == current_index:
                duration = remaining_years

            end_year = current_year + duration
            if current_year >= total_years:
                break

            end_date = start_date + datetime.timedelta(days=duration * 365.25)
            dasa_table.append({
                "planet": planet,
                "start_age": round(current_year, 2),
                "end_age": round(end_year, 2),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "duration": round(duration, 2)
            })

            current_year = end_year
            start_date = end_date
        current_index = 0

    return dasa_table

def generate_dasa_bhukti_table(jd, moon_longitude):
    """Generate Dasa Bhukti table with sub-periods."""
    # First get the main dasa periods
    main_dasa_table = generate_dasa_table(jd, moon_longitude, total_years=120)

    # For each main dasa, calculate bhukti (sub-periods)
    bhukti_table = []

    for main_period in main_dasa_table:  # Show ALL main periods (was [:5])
        maha_dasa_planet = main_period['planet']
        maha_dasa_duration = main_period['duration']
        
        # Calculate bhukti periods within this maha dasa
        bhukti_durations = dasa_durations.copy()
        current_bhukti_index = list(bhukti_durations.keys()).index(maha_dasa_planet)
        
        current_date = datetime.datetime.strptime(main_period['start_date'], "%Y-%m-%d")
        remaining_duration = maha_dasa_duration
        
        for i in range(len(bhukti_durations)):
            bhukti_planet = list(bhukti_durations.keys())[(current_bhukti_index + i) % len(bhukti_durations)]
            bhukti_duration = bhukti_durations[bhukti_planet]
            
            # Calculate proportional duration within maha dasa
            proportional_duration = (bhukti_duration / sum(bhukti_durations.values())) * maha_dasa_duration
            
            if remaining_duration <= 0:
                break
                
            if proportional_duration > remaining_duration:
                proportional_duration = remaining_duration
            
            end_date = current_date + datetime.timedelta(days=proportional_duration * 365.25)
            
            bhukti_table.append({
                "maha_dasa": maha_dasa_planet,
                "bhukti": bhukti_planet,
                "start_date": current_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "duration": round(proportional_duration, 2)
            })
            
            current_date = end_date
            remaining_duration -= proportional_duration
    
    return bhukti_table

# --- GPT INTERPRETATION ---
def ask_gpt_dasa_prediction(birth_info, dasa_table, planet_data):
    """
    Ask GPT to interpret Dasa-Bhukti timeline and planetary chart.
    """
    prompt = f"""
    Provide an interpretation of the Vimshottari Dasa-Bhukti for:
    DOB: {birth_info['dob']} TOB: {birth_info['tob']} Place: {birth_info['place']}

    Planetary Positions:
    {planet_data}

    Dasa Table:
    {dasa_table}

    Provide insights on:
    1. Key life periods and transitions.
    2. Career, health, relationships during each Dasa.
    3. Spiritual guidance and remedies.
    """
    client = get_openai_client()
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"GPT Error: {str(e)}"
    else:
        return "OpenAI API key not set."