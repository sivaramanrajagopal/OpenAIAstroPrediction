import swisseph as swe
import datetime
import os
import sys

def comprehensive_diagnostic():
    print("🔬 COMPREHENSIVE SWISS EPHEMERIS DIAGNOSTIC")
    print("=" * 60)
    
    # 1. Version and Environment Info
    print("1. ENVIRONMENT INFO:")
    try:
        print(f"   PySwisseph version: {swe.version}")
    except:
        print("   PySwisseph version: Not available")
    
    print(f"   Python version: {sys.version}")
    print(f"   Platform: {sys.platform}")
    
    # 2. Ephemeris Path Configuration
    print(f"\n2. EPHEMERIS CONFIGURATION:")
    ephe_path = os.path.join('backend', 'ephe')
    print(f"   Ephemeris path: {ephe_path}")
    print(f"   Path exists: {os.path.exists(ephe_path)}")
    
    if os.path.exists(ephe_path):
        swe.set_ephe_path(ephe_path)
        print(f"   ✅ Ephemeris path set")
    else:
        swe.set_ephe_path('.')
        print(f"   ⚠️ Using default path")
    
    # 3. Sidereal Mode Configuration
    print(f"\n3. SIDEREAL MODE:")
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    print(f"   Ayanamsa: LAHIRI")
    
    # Test ayanamsa value for the test date
    test_jd = swe.julday(1978, 9, 18, 12.0)
    ayanamsa = swe.get_ayanamsa(test_jd)
    print(f"   Ayanamsa value for 1978-09-18: {ayanamsa:.8f}°")
    
    # 4. Detailed Julian Day Calculation
    print(f"\n4. JULIAN DAY CALCULATION:")
    
    # Test different JD calculation methods
    methods = [
        ("Standard", lambda: swe.julday(1978, 9, 18, 12 + 5/60)),  # 12:05 UTC
        ("With seconds", lambda: swe.julday(1978, 9, 18, 12, 5, 0)),  # If supported
        ("Decimal hours", lambda: swe.julday(1978, 9, 18, 12.08333333))
    ]
    
    for method_name, jd_func in methods:
        try:
            jd = jd_func()
            print(f"   {method_name:15}: {jd:.10f}")
        except Exception as e:
            print(f"   {method_name:15}: Error - {e}")
    
    # 5. Moon Position with Different Calculation Flags
    print(f"\n5. MOON CALCULATIONS WITH DIFFERENT FLAGS:")
    
    jd = swe.julday(1978, 9, 18, 12.08333333)  # 17:35 IST = 12:05 UTC
    
    flag_tests = [
        ("SIDEREAL only", swe.FLG_SIDEREAL),
        ("SIDEREAL + SPEED", swe.FLG_SIDEREAL | swe.FLG_SPEED),
        ("SIDEREAL + EQUATORIAL", swe.FLG_SIDEREAL | swe.FLG_EQUATORIAL),
        ("TROPICAL", 0),
        ("TROPICAL + SPEED", swe.FLG_SPEED)
    ]
    
    for flag_name, flags in flag_tests:
        try:
            result = swe.calc_ut(jd, swe.MOON, flags)
            longitude = result[0][0]
            
            # Calculate pada
            nakshatra_length = 360 / 27
            longitude_in_nak = longitude % nakshatra_length
            pada = int((longitude_in_nak / (nakshatra_length / 4)) + 1)
            
            print(f"   {flag_name:20}: {longitude:.8f}° (pada {pada})")
            
        except Exception as e:
            print(f"   {flag_name:20}: Error - {e}")
    
    # 6. Time Zone Impact Test
    print(f"\n6. TIMEZONE SENSITIVITY TEST:")
    
    # Test slight timezone variations
    timezone_tests = [
        ("IST 5.5h", 5.5),
        ("IST 5:30", 5.5),
        ("UTC+5:00", 5.0),
        ("UTC+5:20", 5.333333),
        ("UTC+5:25", 5.416667),
        ("UTC+5:35", 5.583333)
    ]
    
    for tz_name, tz_offset in timezone_tests:
        local_dt = datetime.datetime(1978, 9, 18, 17, 35, 0)
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        test_jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, 
                            utc_dt.hour + utc_dt.minute/60.0)
        
        try:
            result = swe.calc_ut(test_jd, swe.MOON, swe.FLG_SIDEREAL | swe.FLG_SPEED)
            longitude = result[0][0]
            
            nakshatra_length = 360 / 27
            longitude_in_nak = longitude % nakshatra_length
            pada = int((longitude_in_nak / (nakshatra_length / 4)) + 1)
            
            status = "✅" if abs(longitude - 354.14) < 0.1 else "❌"
            print(f"   {tz_name:12}: {longitude:.6f}° (pada {pada}) {status}")
            
        except Exception as e:
            print(f"   {tz_name:12}: Error - {e}")
    
    # 7. Recommendations
    print(f"\n7. DIAGNOSTIC RECOMMENDATIONS:")
    print(f"   • Check if cloud deployments use same PySwisseph version")
    print(f"   • Verify ephemeris files are identical (MD5 hashes)")
    print(f"   • Test with different sidereal modes if needed")
    print(f"   • Consider using different Julian Day precision")
    print(f"   • Validate timezone calculation consistency")

if __name__ == "__main__":
    comprehensive_diagnostic()