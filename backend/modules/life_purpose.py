import swisseph as swe
import datetime
from openai import OpenAI
import os

# --- OPENAI CONFIG ---
# Load API key from environment variable for security
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
    "Sun": swe.SUN, "Moon": swe.MOON, "Mercury": swe.MERCURY,
    "Venus": swe.VENUS, "Mars": swe.MARS, "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN, "Rahu": swe.MEAN_NODE, "Ketu": swe.MEAN_NODE
}

sign_lords = {
    "Mesha": "Mars", "Rishaba": "Venus", "Mithuna": "Mercury",
    "Kataka": "Moon", "Simha": "Sun", "Kanni": "Mercury",
    "Thula": "Venus", "Vrischika": "Mars", "Dhanus": "Jupiter",
    "Makara": "Saturn", "Kumbha": "Saturn", "Meena": "Jupiter"
}

aspects = {
    "Mars": [4, 7, 8], "Jupiter": [5, 7, 9],
    "Saturn": [3, 7, 10], "Rahu": [5, 7, 9],
    "Ketu": [5, 7, 9]
}

purpose_significators = {
    "Sun": ["Soul purpose", "Leadership", "Self-realization"],
    "Moon": ["Emotional fulfillment", "Nurturing", "Mind's purpose"],
    "Mars": ["Courage", "Action", "Initiative"],
    "Mercury": ["Communication", "Intellect", "Learning"],
    "Jupiter": ["Dharma", "Wisdom", "Teaching"],
    "Venus": ["Relationships", "Creativity", "Beauty"],
    "Saturn": ["Karma", "Service", "Discipline"],
    "Rahu": ["Worldly mission", "Material desires", "Innovation"],
    "Ketu": ["Spiritual liberation", "Past-life talents", "Letting go"],
    "1st": ["Self-identity", "Physical body", "Personality expression"],
    "5th": ["Creative purpose", "Children", "Speculation"],
    "9th": ["Higher purpose", "Spirituality", "Teaching"],
    "10th": ["Career purpose", "Public role", "Legacy"],
    "12th": ["Moksha", "Spiritual liberation", "Hidden talents"]
}

nakshatra_purposes = {
    "Ashwini": ["Healing", "Quick action", "Pioneering"],
    "Rohini": ["Creation", "Material abundance", "Artistic expression"],
    "Mrigashira": ["Searching", "Research", "Curiosity"],
    "Ardra": ["Transformation", "Destruction/rebuilding"],
    "Punarvasu": ["Renewal", "Teaching", "Nurturing"],
    "Pushya": ["Nourishment", "Spiritual growth", "Protection"],
    "Swati": ["Adaptability", "Business", "Diplomacy"],
    "Hasta": ["Skill mastery", "Hands-on work", "Manifestation"],
    "Vishakha": ["Achievement", "Goal orientation", "Competitive success"],
    "Anuradha": ["Collaboration", "Community building"],
    "Uttara Ashadha": ["Invincibility", "Spiritual leadership"],
    "Shravana": ["Listening", "Learning", "Teaching"],
    "Dhanishta": ["Rhythm", "Music", "Financial success"],
    "Shatabhisha": ["Healing", "Innovation", "Breaking norms"],
    "Revati": ["Nurturing", "Compassion", "Spiritual completion"]
}

# --- SWISS EPHEMERIS INIT ---
swe.set_ephe_path('.')
swe.set_sid_mode(swe.SIDM_LAHIRI)

# --- HELPER FUNCTIONS ---
def get_chart_info(longitude, speed=None):
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else False,
        'rasi': rasis[int(longitude // 30)],
        'nakshatra': nakshatras[int((longitude % 360) // (360 / 27))],
        'pada': int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1),
        'degree': longitude % 30
    }

def get_planet_positions(jd, lat, lon):
    FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED
    results = {}
    swe.set_topo(lon, lat, 0)

    for name, pid in planet_ids.items():
        if name in ["Rahu", "Ketu"]:
            continue
        tropical_pos = swe.calc_ut(jd, pid, swe.FLG_SWIEPH | swe.FLG_SPEED)[0]
        sid_pos = swe.calc_ut(jd, pid, FLAGS)[0]
        results[name] = get_chart_info(sid_pos[0], tropical_pos[3])

    rahu = swe.calc_ut(jd, swe.MEAN_NODE, FLAGS)[0]
    results['Rahu'] = get_chart_info(rahu[0], rahu[3])
    results['Ketu'] = get_chart_info((rahu[0] + 180) % 360, rahu[3])
    results['Rahu']['retrograde'] = results['Ketu']['retrograde'] = True

    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'P', flags=FLAGS)
    results['Ascendant'] = get_chart_info(ascmc[0])

    return results, ascmc[0], cusps

def get_house_from_longitude(longitude, asc_deg):
    lagna_rasi = int(asc_deg // 30)
    planet_rasi = int(longitude // 30)
    return (planet_rasi - lagna_rasi) % 12 + 1

def analyze_life_purpose(data, asc_deg, cusps):
    purpose_houses = {1: cusps[0], 5: cusps[4], 9: cusps[8], 10: cusps[9], 12: cusps[11]}
    house_lords = {}
    for house_num, house_deg in purpose_houses.items():
        sign = rasis[int(house_deg // 30)]
        lord = sign_lords.get(sign)
        house_lords[house_num] = {'sign': sign, 'lord': lord, 'position': data.get(lord)}

    planets_in_purpose_houses = {h: [] for h in purpose_houses}
    for planet, info in data.items():
        if planet in planet_ids or planet in ['Rahu', 'Ketu']:
            house = get_house_from_longitude(info['longitude'], asc_deg)
            if house in purpose_houses:
                planets_in_purpose_houses[house].append(planet)

    all_planets = sorted(
        [(p, info['longitude'] % 30) for p, info in data.items() if p in planet_ids and p not in ['Rahu', 'Ketu']],
        key=lambda x: x[1], reverse=True
    )
    atmakaraka = all_planets[0][0] if all_planets else None
    amatyakaraka = all_planets[1][0] if len(all_planets) > 1 else None

    return {
        'house_lords': house_lords,
        'planets_in_purpose_houses': planets_in_purpose_houses,
        'atmakaraka': atmakaraka,
        'amatyakaraka': amatyakaraka,
        'ascendant': data['Ascendant']['rasi'],
        'moon_sign': data['Moon']['rasi'],
        'moon_nakshatra': data['Moon']['nakshatra'],
        'sun_sign': data['Sun']['rasi']
    }

def generate_purpose_report(analysis, data):
    report = "\n🌟 Life Purpose Analysis 🌟\n"
    report += f"\nAscendant: {analysis['ascendant']}"
    report += f"\nMoon Sign: {analysis['moon_sign']}"
    report += f"\nSun Sign: {analysis['sun_sign']}"
    report += f"\nAtmakaraka: {analysis['atmakaraka']}"
    report += f"\nAmatyakaraka: {analysis['amatyakaraka']}"
    
    # Add detailed interpretation using GPT
    prompt = f"""
    Based on this Vedic astrology chart:
    - Ascendant: {analysis['ascendant']}
    - Moon Sign: {analysis['moon_sign']} (Nakshatra: {analysis['moon_nakshatra']})
    - Sun Sign: {analysis['sun_sign']}
    - Atmakaraka (Soul Planet): {analysis['atmakaraka']}
    - Amatyakaraka (Mind Planet): {analysis['amatyakaraka']}
    
    Please provide a comprehensive life purpose analysis including:
    1. Overall life mission and soul purpose
    2. Key strengths and talents to develop
    3. Career paths that align with your dharma
    4. Spiritual growth opportunities
    5. Challenges to overcome for fulfillment
    
    Write in a clear, inspiring, and practical manner suitable for a Vedic astrology reading.
    """
    
    gpt_interpretation = ask_gpt(prompt)
    report += f"\n\n{gpt_interpretation}"
    
    return report

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a wise Vedic astrologer with deep knowledge of Jyotish. Provide insightful, practical, and inspiring interpretations that help people understand their life purpose and dharma."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"GPT Error: {str(e)}"
