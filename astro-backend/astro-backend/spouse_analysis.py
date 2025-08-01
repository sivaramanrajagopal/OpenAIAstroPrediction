import swisseph as swe
import datetime
from openai import OpenAI
import os

# --- CONFIGURE OPENAI ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- CONSTANTS ---
rasis = [
    "Mesha", "Rishaba", "Mithuna", "Kataka", "Simha", "Kanni",
    "Thula", "Vrischika", "Dhanus", "Makara", "Kumbha", "Meena"
]

nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

planet_ids = {
    "Sun": 0, "Moon": 1, "Mars": 2, "Mercury": 3, "Jupiter": 4, "Venus": 5,
    "Saturn": 6, "Uranus": 7, "Neptune": 8, "Pluto": 9
}

sign_lords = {
    "Mesha": "Mars", "Rishaba": "Venus", "Mithuna": "Mercury",
    "Kataka": "Moon", "Simha": "Sun", "Kanni": "Mercury",
    "Thula": "Venus", "Vrischika": "Mars", "Dhanus": "Jupiter",
    "Makara": "Saturn", "Kumbha": "Saturn", "Meena": "Jupiter"
}

direction_map = {
    1: "East", 2: "East", 3: "North-East", 4: "North", 
    5: "North", 6: "North-West", 7: "West", 8: "West",
    9: "South-West", 10: "South", 11: "South", 12: "South-East"
}

swe.set_ephe_path('./ephe')
swe.set_sid_mode(swe.SIDM_LAHIRI)

# --- FUNCTIONS ---
def get_chart_info(longitude, speed=None):
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else None,
        'rasi': rasis[int(longitude // 30)],
        'nakshatra': nakshatras[int((longitude % 360) // (360 / 27))],
        'pada': int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1)
    }

def get_planet_positions(jd, lat, lon):
    FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED
    results = {}
    swe.set_topo(lon, lat, 0)

    for pid in range(0, 10):
        name = swe.get_planet_name(pid)
        lonlat = swe.calc_ut(jd, pid, FLAGS)[0]
        results[name] = get_chart_info(lonlat[0], lonlat[3])

    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'O', FLAGS)
    results['Ascendant'] = get_chart_info(ascmc[0])
    return results, ascmc[0]

def get_house_from_longitude(longitude, asc_deg):
    return int(((longitude - asc_deg) % 360) // 30) + 1

def get_aspects(data, asc_deg):
    house_aspects = {}
    for planet, info in data.items():
        if planet == 'Ascendant':
            continue
        planet_deg = info['longitude']
        planet_house = get_house_from_longitude(planet_deg, asc_deg)
        aspects = [(planet_house + 6 - 1) % 12 + 1]
        house_aspects[planet] = sorted(set(aspects))
    return house_aspects

def analyze_marriage(data, asc_deg, aspects, gender):
    lagna_rasi = data['Ascendant']['rasi']
    rasi_seq = rasis[rasis.index(lagna_rasi):] + rasis[:rasis.index(lagna_rasi)]
    seventh_rasi = rasi_seq[6]
    seventh_lord = sign_lords.get(seventh_rasi)
    seventh_house_deg = (asc_deg + 180) % 360
    spouse_direction = direction_map.get(int(seventh_house_deg // 30) + 1, "Unknown")

    return {
        "gender": gender,
        "lagna": lagna_rasi,
        "7th_house_sign": seventh_rasi,
        "7th_lord": seventh_lord,
        "spouse_direction": spouse_direction,
        "aspects": aspects
    }

def generate_report(analysis):
    return (
        f"💍 Spouse Analysis:\n"
        f"Gender: {analysis['gender']}\n"
        f"Ascendant: {analysis['lagna']}\n"
        f"7th House: {analysis['7th_house_sign']}\n"
        f"7th Lord: {analysis['7th_lord']}\n"
        f"Spouse Direction: {analysis['spouse_direction']}\n"
    )

def ask_gpt_spouse(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert Vedic astrologer specializing in marriage and spouse prediction."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"GPT Error: {str(e)}"
