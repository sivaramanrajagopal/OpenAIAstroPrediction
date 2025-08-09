import swisseph as swe
import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv

# --- CONFIGURE OPENAI ---
load_dotenv()
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

career_significators = {
    "Sun": ["Leadership", "Government", "Administration", "Medicine", "Gold"],
    "Moon": ["Psychology", "Nursing", "Hospitality", "Water-related", "Real Estate"],
    "Mars": ["Engineering", "Military", "Sports", "Police", "Manufacturing"],
    "Mercury": ["Writing", "IT", "Teaching", "Accounting", "Marketing"],
    "Jupiter": ["Education", "Law", "Finance", "Spirituality", "Consulting"],
    "Venus": ["Arts", "Fashion", "Entertainment", "Luxury Goods", "Beauty"],
    "Saturn": ["Mining", "Construction", "Oil/Gas", "Elder Care", "History"],
    "Rahu": ["Technology", "Research", "Aviation", "Pharmaceuticals", "Unconventional"],
    "Ketu": ["Spirituality", "Mysticism", "Alternative Healing", "Isolation Fields"],
    "2nd": ["Finance", "Banking", "Food Industry", "Family Business"],
    "6th": ["Healthcare", "Service Industry", "Competitive Fields", "Pets"],
    "10th": ["CEO", "Public Figure", "Prestige Careers", "Government"],
    "11th": ["Networking", "Social Media", "Group Enterprises", "Astrology"]
}

sign_careers = {
    "Mesha": ["Entrepreneurship", "Sports", "Military", "Mechanical"],
    "Rishaba": ["Banking", "Arts", "Agriculture", "Luxury Goods"],
    "Mithuna": ["Media", "Writing", "Sales", "Teaching"],
    "Kataka": ["Real Estate", "History", "Psychology", "Hotels"],
    "Simha": ["Entertainment", "Politics", "Management", "Gold"],
    "Kanni": ["Healthcare", "Service", "Accounting", "Editing"],
    "Thula": ["Law", "Fashion", "Diplomacy", "Beauty"],
    "Vrischika": ["Research", "Surgery", "Detective", "Chemistry"],
    "Dhanus": ["Education", "Travel", "Philosophy", "Import/Export"],
    "Makara": ["Construction", "Oil/Gas", "Administration", "Mining"],
    "Kumbha": ["Technology", "Astrology", "Innovation", "Social Work"],
    "Meena": ["Spirituality", "Pharmacy", "Creative Arts", "Charity"]
}

swe.set_ephe_path('.')
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

    rahu = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0]
    results['Rahu'] = get_chart_info(rahu[0], rahu[3])
    ketu_lon = (rahu[0] + 180.0) % 360.0
    ketu_info = get_chart_info(ketu_lon, rahu[3])
    ketu_info['retrograde'] = True
    results['Ketu'] = ketu_info

    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'O', flags=FLAGS)
    results['Ascendant'] = get_chart_info(ascmc[0])
    return results, ascmc[0], cusps


def get_house_from_longitude(longitude, asc_deg):
    lagna_rasi = int(asc_deg // 30)
    planet_rasi = int(longitude // 30)
    return (planet_rasi - lagna_rasi) % 12 + 1


def analyze_career(data, asc_deg, cusps, gender):
    career_houses = {2: cusps[1], 6: cusps[5], 10: cusps[9], 11: cusps[10]}
    house_lords = {}

    for house_num, house_deg in career_houses.items():
        sign_idx = int(house_deg // 30)
        sign = rasis[sign_idx]
        lord = sign_lords.get(sign)
        house_lords[house_num] = {'sign': sign, 'lord': lord, 'position': data.get(lord)}

    planets_in_career_houses = {h: [] for h in career_houses}
    for planet, info in data.items():
        if planet in planet_ids or planet.startswith('Rahu') or planet.startswith('Ketu'):
            house = get_house_from_longitude(info['longitude'], asc_deg)
            if house in career_houses:
                planets_in_career_houses[house].append(planet)

    career_planets = []
    for planet in ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn']:
        if planet in data:
            career_planets.append({
                'planet': planet,
                'house': get_house_from_longitude(data[planet]['longitude'], asc_deg),
                'sign': data[planet]['rasi'],
                'nakshatra': data[planet]['nakshatra']
            })

    yogas = []
    if (get_house_from_longitude(data['Jupiter']['longitude'], asc_deg) == 10 and
        get_house_from_longitude(data['Moon']['longitude'], asc_deg) == 11):
        yogas.append("Gajakesari Yoga (Success in career)")

    return {
        'house_lords': house_lords,
        'planets_in_career_houses': planets_in_career_houses,
        'career_planets': career_planets,
        'yogas': yogas,
        'ascendant': data['Ascendant']['rasi']
    }


def generate_career_report(analysis, asc_deg):
    report = "\n💼 Advanced Career Analysis:\n"
    report += f"\nAscendant: {analysis['ascendant']}"
    report += f"\nGeneral Career Tendencies: {', '.join(sign_careers.get(analysis['ascendant'], []))}"

    report += "\n\nKey Career Houses Analysis:"
    for house_num, info in analysis['house_lords'].items():
        suffix = "th" if house_num not in [1, 2, 3] else {1: "st", 2: "nd", 3: "rd"}[house_num]
        report += f"\n{house_num}{suffix} House (Sign: {info['sign']}, Lord: {info['lord']}):"
        if info['position']:
            report += f" Positioned in {info['position']['rasi']} (House {get_house_from_longitude(info['position']['longitude'], asc_deg)})"
        report += f"\n  Career Fields: {', '.join(career_significators.get(str(house_num)+'th', []))}"
        if analysis['planets_in_career_houses'].get(house_num):
            report += f"\n  Planets in this house: {', '.join(analysis['planets_in_career_houses'][house_num])}"

    report += "\n\nCareer Significator Planets:"
    for planet in analysis['career_planets']:
        report += f"\n{planet['planet']} in {planet['sign']} (House {planet['house']}):"
        report += f"\n  Potential Careers: {', '.join(career_significators.get(planet['planet'], []))}"
    return report
