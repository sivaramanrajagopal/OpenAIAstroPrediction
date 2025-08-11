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

# Test data - matching your current output vs expected
print("DEBUGGING MOON CALCULATION DISCREPANCY")
print("="*60)

# Current calculation approach
dob = "1978-09-18"
tob = "17:35"
tz_offset = 5.5

local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)

print(f"Birth details: {dob} {tob} (TZ offset: {tz_offset})")
print(f"Local time: {local_dt}")
print(f"UTC time: {utc_dt}")
print(f"Julian Day: {jd:.8f}")

# Calculate Moon with current method
FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED
moon_calc = swe.calc_ut(jd, swe.MOON, FLAGS)
current_moon_long = moon_calc[0][0]

print(f"\nCurrent Moon longitude: {current_moon_long:.8f}° (showing as {current_moon_long:.2f}°)")
print(f"Expected Moon longitude: 354.14°")
print(f"Difference: {abs(current_moon_long - 354.14):.4f}°")

# Try different timezone approach - maybe IST should be 5:30 not 5.5?
print("\n" + "-"*40)
print("TESTING DIFFERENT TIMEZONE CALCULATIONS:")

timezone_tests = [5.5, 5.0833333, 5.25, 5.333333]  # 5.5, 5:05, 5:15, 5:20

for i, tz in enumerate(timezone_tests):
    utc_test = local_dt - datetime.timedelta(hours=tz)
    jd_test = swe.julday(utc_test.year, utc_test.month, utc_test.day, utc_test.hour + utc_test.minute / 60.0)
    moon_test = swe.calc_ut(jd_test, swe.MOON, FLAGS)[0][0]
    
    print(f"TZ {tz:8.4f}h: UTC {utc_test}, Moon {moon_test:.4f}°")
    
    if abs(moon_test - 354.14) < 0.1:
        print(f"    ✅ MATCHES expected 354.14°!")

# Test pada calculation for both values
print("\n" + "-"*40)
print("PADA CALCULATION TEST:")

def calculate_pada(longitude):
    """Calculate pada from longitude"""
    nakshatra_length = 360 / 27  # 13.333333...
    longitude_in_nakshatra = longitude % nakshatra_length
    pada_length = nakshatra_length / 4  # 3.333333...
    pada = int((longitude_in_nakshatra / pada_length) + 1)
    return pada, longitude_in_nakshatra, pada_length

test_values = [353.26, 354.14]
for val in test_values:
    pada, long_in_nak, pada_len = calculate_pada(val)
    print(f"\nLongitude {val}°:")
    print(f"  Longitude in nakshatra: {long_in_nak:.6f}°")
    print(f"  Pada calculation: ({long_in_nak:.6f} / {pada_len:.6f}) + 1 = {(long_in_nak / pada_len) + 1:.6f}")
    print(f"  Pada (int): {pada}")
    
    if val == 354.14:
        print(f"  ✅ Expected pada: 3, Calculated: {pada}")
    else:
        print(f"  Current result pada: {pada}")

# Check if there's a precision issue in the calculation
print("\n" + "-"*40)
print("PRECISION ANALYSIS:")

# Test with higher precision Julian Day calculation
precise_utc = local_dt - datetime.timedelta(hours=5, minutes=30, seconds=0)  # Exact IST
precise_jd = swe.julday(precise_utc.year, precise_utc.month, precise_utc.day, 
                       precise_utc.hour + precise_utc.minute/60.0)

print(f"Precise UTC (5:30 exact): {precise_utc}")
print(f"Precise Julian Day: {precise_jd:.10f}")

precise_moon = swe.calc_ut(precise_jd, swe.MOON, FLAGS)[0][0]
print(f"Precise Moon longitude: {precise_moon:.10f}°")

precise_pada, _, _ = calculate_pada(precise_moon)
print(f"Precise Moon pada: {precise_pada}")

if abs(precise_moon - 354.14) < 0.01:
    print("✅ PRECISE CALCULATION MATCHES EXPECTED VALUE!")
    
# Test boundary cases around the pada transition
print("\n" + "-"*40)
print("PADA BOUNDARY TEST:")

# Revati nakshatra spans from 346.67° to 360°
# Pada boundaries in Revati: 
# Pada 1: 346.67° - 350.00°
# Pada 2: 350.00° - 353.33°  
# Pada 3: 353.33° - 356.67°  ← This is where 354.14° should fall
# Pada 4: 356.67° - 360.00°

revati_start = 346.67
revati_length = 13.33333
pada_boundaries = [revati_start + i * (revati_length / 4) for i in range(5)]

print("Revati pada boundaries:")
for i, boundary in enumerate(pada_boundaries[:-1]):
    print(f"  Pada {i+1}: {boundary:.2f}° - {pada_boundaries[i+1]:.2f}°")
    
print(f"\n353.26° falls in pada: {calculate_pada(353.26)[0]} (current result)")
print(f"354.14° falls in pada: {calculate_pada(354.14)[0]} (expected result)")