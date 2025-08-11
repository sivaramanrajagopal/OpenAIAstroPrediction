import swisseph as swe
import datetime
import os

# Set up Swiss Ephemeris
ephe_path = os.path.join(os.path.dirname(__file__), 'backend', 'ephe')
if os.path.exists(ephe_path):
    swe.set_ephe_path(ephe_path)
    print(f"✅ Using ephemeris path: {ephe_path}")
else:
    swe.set_ephe_path('.')
    print(f"⚠️ Using default ephemeris path")

swe.set_sid_mode(swe.SIDM_LAHIRI)

# Test data
dob = "1978-09-18"
tob = "17:35"
lat = 13.08333333
lon = 80.28333333
tz_offset = 5.5

print(f"Testing birth details: {dob} {tob} at lat={lat}, lon={lon}, tz_offset={tz_offset}")

# Calculate Julian Day - different approaches
local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
print(f"Local datetime: {local_dt}")

utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
print(f"UTC datetime: {utc_dt}")

# Method 1: Current calculation
jd1 = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
print(f"Julian Day (current method): {jd1}")

# Method 2: More precise calculation
jd2 = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, 
                 utc_dt.hour, utc_dt.minute, utc_dt.second)
print(f"Julian Day (precise method): {jd2}")

# Method 3: Using UTC with seconds
total_seconds = utc_dt.hour * 3600 + utc_dt.minute * 60 + utc_dt.second
decimal_hour = total_seconds / 3600.0
jd3 = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, decimal_hour)
print(f"Julian Day (decimal hour): {jd3}")

# Calculate Moon position with different methods
FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED

print("\n" + "="*60)
print("MOON CALCULATIONS:")

for i, jd in enumerate([jd1, jd2, jd3], 1):
    try:
        moon_calc = swe.calc_ut(jd, swe.MOON, FLAGS)
        moon_longitude = moon_calc[0][0]
        moon_speed = moon_calc[0][3]
        
        # Calculate nakshatra and pada
        nakshatra_length = 360 / 27  # 13.333...
        nakshatra_index = int((moon_longitude % 360) // nakshatra_length)
        
        # Pada calculation
        longitude_in_nakshatra = moon_longitude % nakshatra_length
        pada_length = nakshatra_length / 4  # 3.333...
        pada = int((longitude_in_nakshatra / pada_length) + 1)
        
        # Rasi
        rasi_index = int(moon_longitude // 30)
        degrees_in_rasi = moon_longitude % 30
        
        print(f"\nMethod {i} (JD: {jd:.8f}):")
        print(f"  Moon Longitude: {moon_longitude:.8f}°")
        print(f"  Moon Speed: {moon_speed:.8f}°/day")
        print(f"  Nakshatra Index: {nakshatra_index} (longitude in nak: {longitude_in_nakshatra:.8f}°)")
        print(f"  Pada: {pada}")
        print(f"  Rasi Index: {rasi_index}, Degrees in Rasi: {degrees_in_rasi:.2f}°")
        
        # Check if this matches expected values
        expected_long = 354.14
        expected_pada = 3
        
        if abs(moon_longitude - expected_long) < 0.1:
            print(f"  ✅ MATCHES expected longitude ({expected_long}°)")
        else:
            print(f"  ❌ Differs from expected longitude ({expected_long}°) by {abs(moon_longitude - expected_long):.2f}°")
            
        if pada == expected_pada:
            print(f"  ✅ MATCHES expected pada ({expected_pada})")
        else:
            print(f"  ❌ Expected pada {expected_pada}, got {pada}")
            
    except Exception as e:
        print(f"\nMethod {i} ERROR: {e}")

# Test with known reference calculation
print("\n" + "="*60)
print("REFERENCE CALCULATION TEST:")

# Try using the exact same method as reference code might use
ref_local_dt = datetime.datetime(1978, 9, 18, 17, 35, 0)
ref_utc_dt = ref_local_dt - datetime.timedelta(hours=5, minutes=30)  # IST is +5:30
print(f"Reference UTC: {ref_utc_dt}")

ref_jd = swe.julday(ref_utc_dt.year, ref_utc_dt.month, ref_utc_dt.day, 
                   ref_utc_dt.hour + ref_utc_dt.minute/60.0 + ref_utc_dt.second/3600.0)
print(f"Reference JD: {ref_jd:.8f}")

ref_moon = swe.calc_ut(ref_jd, swe.MOON, FLAGS)
ref_moon_long = ref_moon[0][0]
print(f"Reference Moon Longitude: {ref_moon_long:.8f}°")

# Calculate pada for reference
ref_nak_length = 360 / 27
ref_long_in_nak = ref_moon_long % ref_nak_length
ref_pada = int((ref_long_in_nak / (ref_nak_length / 4)) + 1)
print(f"Reference Pada: {ref_pada}")

print("\n" + "="*60)
print("DEBUGGING PADA CALCULATION:")

# Test specific longitude values
test_longitudes = [353.26, 354.14, 354.0, 353.5]

for test_long in test_longitudes:
    nakshatra_length = 360 / 27  # 13.333333...
    longitude_in_nakshatra = test_long % nakshatra_length
    pada_length = nakshatra_length / 4  # 3.333333...
    pada = int((longitude_in_nakshatra / pada_length) + 1)
    
    print(f"Longitude {test_long}°:")
    print(f"  Longitude in nakshatra: {longitude_in_nakshatra:.8f}°")
    print(f"  Pada length: {pada_length:.8f}°")
    print(f"  Pada calculation: ({longitude_in_nakshatra:.8f} / {pada_length:.8f}) + 1 = {(longitude_in_nakshatra / pada_length) + 1:.8f}")
    print(f"  Pada (int): {pada}")
    print()