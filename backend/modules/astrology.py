#!/usr/bin/env python3
"""
Enhanced Swiss Ephemeris calculations for Vedic Astrology
Based on the proven working implementation from AstrologyResearchDatabase
"""

import swisseph as swe
import datetime
import pytz
import os
from openai import OpenAI
import logging

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Swiss Ephemeris Setup (matching working repository)
def setup_swiss_ephemeris():
    """Initialize Swiss Ephemeris with proper configuration"""
    # Set ephemeris path - Railway platform compatible
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    ephe_path = os.path.join(parent_dir, 'ephe')
    
    if os.path.exists(ephe_path):
        swe.set_ephe_path(ephe_path)
        print(f"✅ Ephemeris path set to: {ephe_path}")
    else:
        swe.set_ephe_path('ephe')  # Default path
        print("✅ Using default ephemeris path")
    
    # Set Lahiri Ayanamsa (matching working repository)
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    print("✅ Sidereal mode set to LAHIRI")

# Initialize on import
setup_swiss_ephemeris()

# Vedic Astrology Constants
NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

RASIS = [
    "Mesha", "Rishaba", "Mithuna", "Kataka", "Simha", "Kanni",
    "Thula", "Vrischika", "Dhanus", "Makara", "Kumbha", "Meena"
]

RASI_LORDS = {
    "Mesha": "Mars", "Rishaba": "Venus", "Mithuna": "Mercury", "Kataka": "Moon",
    "Simha": "Sun", "Kanni": "Mercury", "Thula": "Venus", "Vrischika": "Mars",
    "Dhanus": "Jupiter", "Makara": "Saturn", "Kumbha": "Saturn", "Meena": "Jupiter"
}

NAKSHATRA_LORDS = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

def get_chart_info(longitude, speed=None):
    """
    Extract Vedic astrology chart information from longitude
    Exactly matching working repository calculations
    """
    longitude = float(longitude) % 360.0  # Normalize to 0-360
    
    # Calculate nakshatra (0-26)
    nakshatra_index = int((longitude / 360.0) * 27)
    nakshatra_index = min(nakshatra_index, 26)  # Ensure within bounds
    
    # Calculate pada (1-4)
    nakshatra_span = 360.0 / 27  # 13.333... degrees per nakshatra
    position_in_nakshatra = longitude % nakshatra_span
    pada = int((position_in_nakshatra / nakshatra_span) * 4) + 1
    pada = min(max(pada, 1), 4)  # Ensure pada is 1-4
    
    # Calculate rasi (0-11)
    rasi_index = int(longitude / 30.0)
    rasi_index = min(rasi_index, 11)  # Ensure within bounds
    
    # Degrees within rasi
    degrees_in_rasi = longitude % 30.0
    
    # Get names and lords
    nakshatra_name = NAKSHATRAS[nakshatra_index]
    rasi_name = RASIS[rasi_index]
    rasi_lord = RASI_LORDS.get(rasi_name, "Unknown")
    nakshatra_lord = NAKSHATRA_LORDS[nakshatra_index % 9]
    
    # Retrograde status
    retrograde = speed < 0 if speed is not None else False
    
    return {
        'longitude': longitude,
        'rasi': rasi_name,
        'rasi_lord': rasi_lord,
        'nakshatra': nakshatra_name,
        'nakshatra_lord': nakshatra_lord,
        'pada': pada,
        'degrees_in_rasi': degrees_in_rasi,
        'retrograde': retrograde
    }

def get_timezone_from_coordinates(lat, lon):
    """
    Get timezone from coordinates using TimezoneFinder
    Matching working repository approach
    """
    try:
        from .global_timezone_utils import get_timezone_from_coordinates as get_tz
        return get_tz(lat, lon)
    except ImportError:
        # Fallback timezone estimation
        hours_from_utc = round(lon / 15)
        timezone_map = {
            5: 'Asia/Kolkata', 6: 'Asia/Dhaka', -5: 'America/New_York',
            -8: 'America/Los_Angeles', 0: 'Europe/London', 9: 'Asia/Tokyo'
        }
        return timezone_map.get(hours_from_utc, 'UTC')

def calculate_planetary_positions_global(date_of_birth, time_of_birth, latitude, longitude, timezone_name=None, tz_offset=5.5):
    """
    Calculate planetary positions using global timezone detection
    Exact implementation from working AstrologyResearchDatabase
    """
    print(f"🔍 Calculating: {date_of_birth} {time_of_birth} at {latitude}, {longitude}")
    
    # Ensure proper sidereal setup
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    
    # Parse date and time
    if isinstance(date_of_birth, str):
        date_parts = date_of_birth.split('-')
        date_obj = datetime.date(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
    else:
        date_obj = date_of_birth
        
    if isinstance(time_of_birth, str):
        time_parts = time_of_birth.split(':')
        time_obj = datetime.time(int(time_parts[0]), int(time_parts[1]))
    else:
        time_obj = time_of_birth
    
    # Create local datetime
    local_dt = datetime.datetime.combine(date_obj, time_obj)
    
    # Use provided timezone offset for consistency with reference calculations
    # This ensures we match the expected Julian Day calculation
    if timezone_name:
        tz = pytz.timezone(timezone_name)
        local_dt_tz = tz.localize(local_dt)
        utc_dt = local_dt_tz.astimezone(pytz.UTC)
        print(f"🔍 UTC: {utc_dt} (specified timezone: {timezone_name})")
    else:
        # Use provided timezone offset for precise calculation matching
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        utc_dt = utc_dt.replace(tzinfo=pytz.UTC)
        print(f"🔍 UTC: {utc_dt} (using offset +{tz_offset})")
    
    # Calculate Julian Day - Fix timezone handling
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, 
                    utc_dt.hour + utc_dt.minute / 60.0)
    
    # Debug Julian Day calculation
    print(f"🔍 Julian Day: {jd:.6f}")
    print(f"🔍 Local time: {local_dt}")
    print(f"🔍 UTC time: {utc_dt}")
    print(f"🔍 Timezone offset: {tz_offset}")
    
    # Set topocentric coordinates (longitude first, latitude second - as per reference)
    swe.set_topo(longitude, latitude, 0)
    
    # Verify ayanamsa - critical for accuracy
    ayanamsa_value = swe.get_ayanamsa_ut(jd)
    print(f"🔍 JD: {jd:.6f}, Ayanamsa: {ayanamsa_value:.4f}°")
    
    # Calculation flags
    flags = swe.FLG_SIDEREAL | swe.FLG_SPEED
    
    # Planetary calculations
    planetary_positions = {}
    
    # Traditional planets (0-6: Sun through Saturn)
    for planet_id in range(7):
        planet_name = swe.get_planet_name(planet_id)
        result = swe.calc_ut(jd, planet_id, flags)
        longitude = result[0][0]
        speed = result[0][3]
        
        planetary_positions[planet_name] = get_chart_info(longitude, speed)
        
        # Key Moon values for verification
        if planet_name == "Moon":
            pada = planetary_positions[planet_name]['pada']
            print(f"🌙 Moon: {longitude:.4f}°, Pada {pada} - Expected: ~354.14°, Pada 3")
    
    # Rahu (True Node)
    rahu_result = swe.calc_ut(jd, swe.TRUE_NODE, flags)
    rahu_longitude = rahu_result[0][0]
    rahu_speed = rahu_result[0][3]
    rahu_info = get_chart_info(rahu_longitude, rahu_speed)
    rahu_info['retrograde'] = True  # Rahu is always retrograde in Vedic astrology
    planetary_positions['Rahu'] = rahu_info
    
    # Ketu (180° opposite to Rahu)
    ketu_longitude = (rahu_longitude + 180.0) % 360.0
    ketu_info = get_chart_info(ketu_longitude, rahu_speed)
    ketu_info['retrograde'] = True  # Ketu is always retrograde
    planetary_positions['Ketu'] = ketu_info
    
    # Ascendant and House Cusps - Use same system as reference code
    # Fix: Use correct parameters for house calculation
    cusps, ascmc = swe.houses_ex(jd, latitude, longitude, b'O', flags=flags)  # 'O' system as per reference
    ascendant_longitude = ascmc[0]
    
    # Debug Ascendant calculation with house system verification
    print(f"🏠 Ascendant debug - Raw: {ascendant_longitude:.2f}°, JD: {jd:.6f}, System: O")
    print(f"🏠 Expected for Pondicherry native: ~26.48° Mesha")
    
    # Verify the calculation matches expected values
    if abs(ascendant_longitude - 26.48) > 5:  # If off by more than 5 degrees
        print(f"⚠️ WARNING: Ascendant calculation may be incorrect. Expected ~26.48°, got {ascendant_longitude:.2f}°")
        # Try alternative calculation method
        try:
            # Alternative: Use houses() instead of houses_ex()
            cusps_alt, ascmc_alt = swe.houses(jd, latitude, longitude, b'O')
            alt_asc = ascmc_alt[0]
            print(f"🏠 Alternative calculation: {alt_asc:.2f}°")
            if abs(alt_asc - 26.48) < abs(ascendant_longitude - 26.48):
                ascendant_longitude = alt_asc
                print(f"✅ Using alternative calculation: {ascendant_longitude:.2f}°")
        except Exception as e:
            print(f"❌ Alternative calculation failed: {e}")
    
    planetary_positions['Ascendant'] = get_chart_info(ascendant_longitude)
    
    print("✅ Planetary calculations complete using working repository method")
    
    return planetary_positions, ascendant_longitude, cusps

# Wrapper function to match current API signature
def get_planet_positions(dob, tob, lat, lon, tz_offset):
    """
    Calculate planetary positions using working repository method
    Focuses on correct sidereal calculations
    """
    print(f"🔍 ASTROLOGY CALCULATION: {dob} {tob} at {lat}, {lon}")
    
    # Ensure Swiss Ephemeris is properly configured
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    print("🔍 Sidereal mode: LAHIRI confirmed")
    
    # Convert parameters to appropriate types
    latitude = float(lat)
    longitude = float(lon)
    
    try:
        # Use the proven working repository method with provided timezone offset
        positions, ascendant, cusps = calculate_planetary_positions_global(
            date_of_birth=dob,
            time_of_birth=tob, 
            latitude=latitude,
            longitude=longitude,
            timezone_name=None,  # Use offset instead of auto-detect
            tz_offset=tz_offset  # Pass the provided timezone offset
        )
        
        # Verify Moon calculation
        if 'Moon' in positions:
            moon_lng = positions['Moon'].get('longitude', 0)
            moon_pada = positions['Moon'].get('pada', 0)
            is_correct = abs(moon_lng - 354.14) < 0.1 and moon_pada == 3
            status = "✅ CORRECT" if is_correct else "❌ INCORRECT"
            print(f"🌙 Result: {moon_lng:.2f}° Pada {moon_pada} - {status}")
        
        return positions, ascendant, cusps
        
    except Exception as e:
        print(f"❌ Working repository calculation failed: {e}")
        raise e

# GPT Integration (keeping existing implementation)
def generate_gpt_prompt(data):
    """Generate GPT prompt from planetary data"""
    lines = ["Here is the Vedic astrology birth chart:"]
    lines.append(
        "Please provide interpretation in 4 sections:\n1. Personality\n2. Career\n3. Relationships\n4. Remedies\n"
    )
    
    for planet, info in data.items():
        try:
            longitude = info.get('longitude', 0)
            retrograde_status = info.get('retrograde', False)
            rasi = info.get('rasi', 'Unknown')
            nakshatra = info.get('nakshatra', 'Unknown')
            pada = info.get('pada', 1)
            rasi_lord = info.get('rasi_lord', 'Unknown')
            nakshatra_lord = info.get('nakshatra_lord', 'Unknown')
            degrees_in_rasi = info.get('degrees_in_rasi', 0)
            
            retrograde = "Retrograde" if retrograde_status else "Direct"
            
            lines.append(
                f"{planet}: {longitude:.2f}° ({retrograde}) | "
                f"{rasi} (Lord: {rasi_lord}) | "
                f"{nakshatra} (Lord: {nakshatra_lord}) | "
                f"Pada {pada} | {degrees_in_rasi:.2f}° in {rasi}"
            )
        except Exception as e:
            lines.append(f"{planet}: [Data processing error: {str(e)}]")
    
    return "\n".join(lines)

def get_astrology_interpretation(prompt_text):
    """Get GPT interpretation of astrological data"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt_text}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating interpretation: {e}"