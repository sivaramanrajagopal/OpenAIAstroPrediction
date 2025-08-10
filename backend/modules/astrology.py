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

# Enhanced ephemeris configuration for deployment consistency
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # Go up one level to backend root
ephe_path = os.path.join(parent_dir, 'ephe')  # Point to backend/ephe directory

print(f"🔍 EPHEMERIS SETUP:")
print(f"   Current directory: {current_dir}")
print(f"   Parent directory: {parent_dir}")
print(f"   Ephemeris path: {ephe_path}")
print(f"   Ephemeris path exists: {os.path.exists(ephe_path)}")

if os.path.exists(ephe_path):
    # Verify critical ephemeris files exist
    critical_files = ['semo_00.se1', 'seas_00.se1', 'sepl_00.se1']
    missing_files = [f for f in critical_files if not os.path.exists(os.path.join(ephe_path, f))]
    
    if missing_files:
        print(f"⚠️ Missing ephemeris files: {missing_files}")
        print(f"⚠️ Using default ephemeris path as fallback")
        swe.set_ephe_path('.')
    else:
        swe.set_ephe_path(ephe_path)
        print(f"✅ Set ephemeris path to: {ephe_path}")
        
        # Verify ephemeris files are loaded correctly
        try:
            # Test calculation to ensure ephemeris files work
            test_jd = swe.julday(2000, 1, 1, 12.0)
            test_calc = swe.calc_ut(test_jd, swe.SUN, swe.FLG_SIDEREAL)
            print(f"✅ Ephemeris files validated (Sun at J2000: {test_calc[0][0]:.2f}°)")
        except Exception as e:
            print(f"⚠️ Ephemeris validation failed: {e}")
            swe.set_ephe_path('.')
else:
    print(f"⚠️ Ephemeris path not found, using default")
    swe.set_ephe_path('.')

# Set sidereal mode with validation
swe.set_sid_mode(swe.SIDM_LAHIRI)
print(f"✅ Sidereal mode set to LAHIRI")

# Log PySwisseph version for debugging
try:
    print(f"✅ PySwisseph version: {swe.version}")
except:
    print(f"⚠️ PySwisseph version not available")

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
    # Calculate nakshatra (matching reference code exactly)
    nakshatra_index = int((longitude % 360) // (360 / 27))
    
    # Calculate pada (matching reference code exactly)
    pada = int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1)
    
    # Calculate rasi
    rasi_index = int(longitude // 30)
    
    # Calculate degrees in rasi
    degrees_in_rasi = longitude % 30
    
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else None,
        'rasi': rasis[rasi_index],
        'rasi_lord': rasi_lords.get(rasis[rasi_index], 'Unknown'),
        'nakshatra': nakshatras[nakshatra_index],
        'nakshatra_lord': nakshatra_lords[nakshatra_index % 9],
        'pada': pada,
        'degrees_in_rasi': degrees_in_rasi
    }

# --- Planet Positions ---
def get_planet_positions(dob, tob, lat, lon, tz_offset):
    """Calculate planetary positions using enhanced method from working repository"""
    
    # CRITICAL FIX 1: Proper timezone handling with pytz
    import pytz
    
    local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    
    print(f"🔍 ENHANCED CALCULATION: {dob} {tob} at {lat}, {lon}")
    print(f"🔍 Original local time: {local_dt}")
    
    # CRITICAL FIX 2: Use pytz for accurate timezone conversion
    if tz_offset == 5.5:  # IST
        timezone_name = "Asia/Calcutta"
        tz = pytz.timezone(timezone_name)
        local_dt = tz.localize(local_dt)
        utc_dt = local_dt.astimezone(pytz.UTC)
        print(f"🔍 Using pytz Asia/Calcutta timezone")
    else:
        # Fallback for other timezones
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        utc_dt = utc_dt.replace(tzinfo=pytz.UTC)
    
    print(f"🔍 UTC time with pytz: {utc_dt}")

    # CRITICAL FIX 3: Enhanced Julian Day calculation
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                    utc_dt.hour + utc_dt.minute / 60.0)
    
    print(f"🔍 Julian Day: {jd:.10f}")
    
    # CRITICAL FIX 4: Set topocentric coordinates (missing from our original code!)
    swe.set_topo(lon, lat, 0)
    print(f"🔍 Topocentric coordinates set: lon={lon}, lat={lat}")

    # CRITICAL FIX 5: Consistent sidereal flags
    SIDEREAL_FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED
    results = {}

    # Calculate traditional planets (0-6: Sun through Saturn, excluding outer planets for Vedic)
    traditional_planets = [0, 1, 2, 3, 4, 5, 6]  # Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn
    for pid in traditional_planets:
        name = swe.get_planet_name(pid)
        lonlat = swe.calc_ut(jd, pid, SIDEREAL_FLAGS)[0]
        results[name] = get_chart_info(lonlat[0], lonlat[3])
        
        # Debug specific Moon calculation
        if name == "Moon":
            print(f"🌙 MOON DEBUG - Longitude: {lonlat[0]:.10f}°")
            print(f"🌙 MOON DEBUG - Speed: {lonlat[3]:.10f}°/day")

    # Rahu/Ketu - True Node with consistent flags
    rahu = swe.calc_ut(jd, swe.TRUE_NODE, SIDEREAL_FLAGS)[0]
    rahu_info = get_chart_info(rahu[0], rahu[3])
    results['Rahu'] = rahu_info

    ketu_lon = (rahu[0] + 180.0) % 360.0
    ketu_info = get_chart_info(ketu_lon, rahu[3])
    ketu_info['retrograde'] = True  # Ketu is always retrograde in Vedic astrology
    results['Ketu'] = ketu_info

    # Ascendant (Lagna) with consistent flags
    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'O', SIDEREAL_FLAGS)
    results['Ascendant'] = get_chart_info(ascmc[0])

    return results, ascmc[0], cusps


# --- GPT Prompt Generator ---
def generate_gpt_prompt(data):
    lines = ["Here is the Vedic astrology birth chart:"]
    lines.append(
        "Please provide interpretation in 4 sections:\n1. Personality\n2. Career\n3. Relationships\n4. Remedies\n"
    )
    for body, info in data.items():
        try:
            # Safe access to all dictionary keys
            longitude = info.get('longitude', 0)
            retrograde_status = info.get('retrograde', False)
            rasi = info.get('rasi', 'Unknown')
            nakshatra = info.get('nakshatra', 'Unknown')
            pada = info.get('pada', 1)
            
            retrograde = "Retrograde" if retrograde_status else "Direct"
            
            # Safe nakshatra lord calculation
            try:
                nakshatra_index = nakshatras.index(nakshatra)
                nakshatra_lord = nakshatra_lords[nakshatra_index % 9]
            except (ValueError, IndexError):
                nakshatra_lord = "Unknown"
            
            lines.append(
                f"{body}: {longitude:.2f}° ({retrograde}) | "
                f"{rasi} (Lord: {rasi_lords.get(rasi, 'Unknown')}) | "
                f"{nakshatra} (Lord: {nakshatra_lord}) | "
                f"Pada {pada} | {longitude % 30:.2f}° in {rasi}"
            )
        except Exception as e:
            # If any planet data is malformed, skip it with a safe fallback
            lines.append(f"{body}: [Data processing error: {str(e)}]")
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
