import swisseph as swe
import datetime
import os
from openai import OpenAI
import logging

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set sidereal mode
swe.set_sid_mode(swe.SIDM_LAHIRI)

# 27 Nakshatras and 12 Rasis
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

# Rasi Lords mapping
rasi_lords = {
    "Mesha": "Mars", "Rishaba": "Venus", "Mithuna": "Mercury", "Kataka": "Moon",
    "Simha": "Sun", "Kanni": "Mercury", "Thula": "Venus", "Vrischika": "Mars",
    "Dhanus": "Jupiter", "Makara": "Saturn", "Kumbha": "Saturn", "Meena": "Jupiter"
}

# Nakshatra Lords (9 lords in sequence)
nakshatra_lords = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

# --- Chart Info ---
def get_chart_info(longitude, speed=None):
    """Return Rasi, Nakshatra, Pada, and retrograde status."""
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else None,
        'rasi': rasis[int(longitude // 30)],
        'nakshatra': nakshatras[int((longitude % 360) // (360 / 27))],
        'pada': int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1)
    }

# --- Planet Positions ---
def get_planet_positions(dob, tob, lat, lon, tz_offset):
    local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    utc_dt = local_dt - datetime.timedelta(hours=tz_offset)

    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                    utc_dt.hour + utc_dt.minute / 60.0)

    FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED
    results = {}
    # swe.set_topo(lon, lat, 0)  # Temporarily comment out topocentric setting

    # All planets 0-9
    for pid in range(0, 10):
        name = swe.get_planet_name(pid)
        lonlat = swe.calc_ut(jd, pid, FLAGS)[0]
        results[name] = get_chart_info(lonlat[0], lonlat[3])

    # Rahu/Ketu - True & Mean Node
    for node_type, base_name in [(swe.TRUE_NODE, 'True'), (swe.MEAN_NODE, 'Mean')]:
        rahu = swe.calc_ut(jd, node_type, FLAGS)[0]
        rahu_info = get_chart_info(rahu[0], rahu[3])
        results[f'Rahu ({base_name})'] = rahu_info

        ketu_lon = (rahu[0] + 180.0) % 360.0
        ketu_info = get_chart_info(ketu_lon, rahu[3])  # same speed (direction doesn't matter for chart info)
        ketu_info['retrograde'] = True  # Force retrograde = True
        results[f'Ketu ({base_name})'] = ketu_info

    # Ascendant (Lagna)
    cusps_result, ascmc = swe.houses_ex(jd, lat, lon, b'O', flags=FLAGS)
    cusps = cusps_result[1:]  # Extract cusps from the result
    results['Ascendant'] = get_chart_info(ascmc[0])
    return results, ascmc[0], cusps


# --- GPT Prompt Generator ---
def generate_gpt_prompt(data):
    lines = ["Here is the Vedic astrology birth chart:"]
    lines.append(
        "Please provide interpretation in 4 sections:\n1. Personality\n2. Career\n3. Relationships\n4. Remedies\n"
    )
    for body, info in data.items():
        retrograde = "Retrograde" if info['retrograde'] else "Direct"
        lines.append(
            f"{body}: {info['longitude']:.2f}° ({retrograde}) | "
            f"{info['rasi']} (Lord: {rasi_lords[info['rasi']]}) | "
            f"{info['nakshatra']} (Lord: {nakshatra_lords[nakshatras.index(info['nakshatra'])]}) | "
            f"Pada {info['pada']} | {info['longitude'] % 30:.2f}° in {info['rasi']}"
        )
    return "\n".join(lines)


# --- Get GPT Interpretation ---
def get_astrology_interpretation(prompt_text):
    try:
        response = client.chat.completions.create(model="gpt-4o",
                                                  messages=[{
                                                      "role":
                                                      "user",
                                                      "content":
                                                      prompt_text
                                                  }],
                                                  temperature=0.7)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error from OpenAI: {e}"
