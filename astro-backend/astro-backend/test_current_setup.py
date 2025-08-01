from astrology import get_planet_positions

# Test with your original case
print("🧪 Testing current setup...")
data, asc_deg, cusps = get_planet_positions(
    "1978-09-18", "17:35", 
    13.08333333, 80.28333333, 5.5
)

moon_info = data['Moon']
print(f"\n📊 Results:")
print(f"Moon longitude: {moon_info['longitude']:.6f}°")
print(f"Nakshatra: {moon_info['nakshatra']}")
print(f"Pada: {moon_info['pada']}")

print(f"\n🎯 Target Check:")
print(f"Expected: 354.14° (Revati Pada 3)")
print(f"Got: {moon_info['longitude']:.2f}° ({moon_info['nakshatra']} Pada {moon_info['pada']})")

if abs(moon_info['longitude'] - 354.14) < 0.1 and moon_info['pada'] == 3:
    print("🎉 PERFECT MATCH!")
elif abs(moon_info['longitude'] - 354.14) < 0.5:
    print("✅ VERY CLOSE!")
else:
    print("❌ Still needs adjustment")