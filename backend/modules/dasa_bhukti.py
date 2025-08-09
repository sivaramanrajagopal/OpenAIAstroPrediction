import swisseph as swe
import datetime
from collections import OrderedDict
from openai import OpenAI
import os

# --- Load OpenAI API Key ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    #longitude = longitude % 360
    nakshatra_index = int((longitude % 360) // (360 / 27))
    nakshatra_longitude = (longitude % 360) % (360 / 27)
    pada = int(nakshatra_longitude // (360 / 27 / 4)) + 1
    
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else None,
        'rasi': rasis[int(longitude // 30)],
        'nakshatra': nakshatras[nakshatra_index],
        'pada': pada
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

    # True Rahu & Ketu
    rahu = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0]
    results['Rahu (True)'] = get_chart_info(rahu[0], rahu[3])
    ketu_lon = (rahu[0] + 180.0) % 360.0
    ketu_info = get_chart_info(ketu_lon, rahu[3])
    ketu_info['retrograde'] = True
    results['Ketu (True)'] = ketu_info

    # Mean Rahu & Ketu
    mean_rahu = swe.calc_ut(jd, swe.MEAN_NODE, FLAGS)[0]
    results['Rahu (Mean)'] = get_chart_info(mean_rahu[0], mean_rahu[3])
    mean_ketu_lon = (mean_rahu[0] + 180.0) % 360.0
    mean_ketu_info = get_chart_info(mean_ketu_lon, mean_rahu[3])
    mean_ketu_info['retrograde'] = True
    results['Ketu (Mean)'] = mean_ketu_info

    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'O', FLAGS)
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
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"GPT Error: {str(e)}"