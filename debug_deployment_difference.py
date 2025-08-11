import requests
import sys
import os
sys.path.insert(0, 'backend')

# Test local vs deployed calculation
print("🔍 DEBUGGING LOCAL vs DEPLOYED CALCULATION DIFFERENCE")
print("="*70)

# Local calculation
print("1. LOCAL CALCULATION:")
try:
    from backend.modules.astrology import get_planet_positions
    dob, tob = "1978-09-18", "17:35"
    lat, lon, tz_offset = 13.08333333, 80.28333333, 5.5
    
    local_result, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
    local_moon = local_result['Moon']
    
    print(f"   Moon longitude: {local_moon['longitude']:.8f}°")
    print(f"   Moon pada: {local_moon['pada']}")
    print(f"   ✅ LOCAL WORKING CORRECTLY")
    
except Exception as e:
    print(f"   ❌ Local calculation failed: {e}")

# Deployed calculation
print("\n2. DEPLOYED CALCULATION:")
try:
    params = {
        'dob': '1978-09-18', 'tob': '17:35',
        'lat': 13.08333333, 'lon': 80.28333333, 'tz_offset': 5.5
    }
    
    response = requests.get("https://openaiastroprediction.onrender.com/predict", params=params, timeout=30)
    if response.status_code == 200:
        deployed_data = response.json()
        deployed_moon = deployed_data['chart']['Moon']
        
        print(f"   Moon longitude: {deployed_moon['longitude']:.8f}°")
        print(f"   Moon pada: {deployed_moon['pada']}")
        print(f"   ❌ DEPLOYED RETURNING OLD VALUES")
        
        # Calculate the difference
        local_long = local_moon['longitude']
        deployed_long = deployed_moon['longitude']
        difference = abs(local_long - deployed_long)
        
        print(f"\n3. COMPARISON:")
        print(f"   Local:    {local_long:.6f}° (pada {local_moon['pada']})")
        print(f"   Deployed: {deployed_long:.6f}° (pada {deployed_moon['pada']})")
        print(f"   Difference: {difference:.6f}°")
        
        if difference > 0.5:
            print(f"   🚨 SIGNIFICANT DIFFERENCE - This suggests different:")
            print(f"      - Swiss Ephemeris files")
            print(f"      - Timezone calculation")
            print(f"      - Julian Day calculation")
            print(f"      - Or using different code path")
        
    else:
        print(f"   ❌ Deployed API error: {response.status_code}")
        
except Exception as e:
    print(f"   ❌ Deployed calculation failed: {e}")

print(f"\n4. POTENTIAL CAUSES:")
print(f"   • Different Swiss Ephemeris data files in cloud")
print(f"   • Timezone handling difference")
print(f"   • Still calling old cached code")
print(f"   • Import path issues causing fallback calculations")

print(f"\n5. NEXT STEPS TO TRY:")
print(f"   • Check if get_planet_positions is being called correctly")
print(f"   • Verify Swiss Ephemeris files are identical")
print(f"   • Add debug logging to see which code path executes")
print(f"   • Check if modules are importing correctly")