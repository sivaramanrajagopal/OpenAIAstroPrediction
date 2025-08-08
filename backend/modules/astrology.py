import swisseph as swe
import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv

# --- Load OpenAI Key ---
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Setup Swiss Ephemeris ---
swe.set_ephe_path('./ephe')  # Use current directory for ephemeris files
swe.set_sid_mode(swe.SIDM_LAHIRI)  # Lahiri ayanamsa (Vedic)

# --- Nakshatras & Rasis ---
nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni",
    "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
    "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana",
    "Dhanishta", "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada",
    "Revati"
]

rasis = [
    "Mesha", "Rishaba", "Mithuna", "Kataka", "Simha", "Kanni", "Thula",
    "Vrischika", "Dhanus", "Makara", "Kumbha", "Meena"
]


# --- Chart Info ---
def get_chart_info(longitude, speed=None):
    #longitude = longitude % 360
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else None,
        'rasi': rasis[int(longitude // 30)],
        'nakshatra': nakshatras[int((longitude % 360) // (360 / 27))],
        'pada': int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1)
    }


# --- Planet Positions ---

def get_planet_positions(dob, tob, lat, lon, tz_offset):
    """
    Returns planetary positions along with Ascendant and house cusps.
    Output: data (dict), ascendant_degree (float), cusps (list)
    """
    print(f"DEBUG: get_planet_positions called with lat={lat}, lon={lon}, tz_offset={tz_offset}")
    local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
    print(f"DEBUG: UTC time: {utc_dt}")
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                    utc_dt.hour + utc_dt.minute / 60.0)
    print(f"DEBUG: Julian Day: {jd}")

    swe.set_topo(lon, lat, 0)
    print(f"DEBUG: Set topocentric coordinates: lon={lon}, lat={lat}")

    FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED
    results = {}

    # Calculate planets
    for pid in range(0, 10):  # Sun to Pluto
        name = swe.get_planet_name(pid)
        lonlat = swe.calc_ut(jd, pid, FLAGS)[0]
        results[name] = get_chart_info(lonlat[0], lonlat[3])

        # Special debug for Moon
        if name == "Moon":
            print(f"DEBUG: Moon longitude: {lonlat[0]}")
            print(f"DEBUG: Moon speed: {lonlat[3]}")

            # Test without topocentric for comparison
            lonlat_geo = swe.calc_ut(jd, pid, swe.FLG_SIDEREAL)[0]  # No topocentric
            print(f"DEBUG: Moon longitude (geocentric): {lonlat_geo[0]}")
            print(f"DEBUG: Difference: {lonlat[0] - lonlat_geo[0]}")

    # Rahu & Ketu
    rahu = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0]
    results['Rahu'] = get_chart_info(rahu[0], rahu[3])
    ketu_lon = (rahu[0] + 180.0) % 360.0
    ketu_info = get_chart_info(ketu_lon, rahu[3])
    ketu_info['retrograde'] = True
    results['Ketu'] = ketu_info

    # Ascendant & Houses
    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'O', FLAGS)
    results['Ascendant'] = get_chart_info(ascmc[0])
    return results, ascmc[0], cusps


# --- GPT Prompt Generator ---
def generate_gpt_prompt(data):
    lines = ["Here is the Vedic astrology birth chart:"]
    lines.append(
        "Please provide interpretation in 4 sections:\n1. Personality\n2. Career\n3. Relationships\n4. Remedies\n"
    )
    for body, info in data.items():
        line = f"- {body}: {info['rasi']}, {info['nakshatra']} Pada {info['pada']}"
        if info.get("retrograde"):
            line += " (Retrograde)"
        lines.append(line)
    return "\n".join(lines)


# --- Get GPT Interpretation ---
def get_astrology_interpretation(prompt_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": prompt_text
            }],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error from OpenAI: {e}"
