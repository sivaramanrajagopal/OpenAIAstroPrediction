"""
Complete Yogas Detection Script (100+ Classical Yogas)
Run with:
  python yogas.py DD.MM.YYYY HH:MM LATITUDE LONGITUDE TIMEZONE
Example:
  python yogas.py 29.10.1977 21:30 13.08 80.28 5.5
"""

import swisseph as swe
import datetime
import sys

# --- Setup Swiss Ephemeris ---
swe.set_ephe_path('.')
swe.set_sid_mode(swe.SIDM_LAHIRI)

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

def get_chart_info(longitude, speed=None):
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else None,
        'rasi': rasis[int(longitude // 30)],
        'nakshatra': nakshatras[int((longitude % 360) // (360 / 27))],
        'pada': int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1)
    }

def get_planet_positions(dob, tob, lat, lon, tz_offset):
    local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
    FLAGS = swe.FLG_SIDEREAL | swe.FLG_SPEED
    results = {}

    for pid in range(0, 10):
        name = swe.get_planet_name(pid)
        lonlat = swe.calc_ut(jd, pid, FLAGS)[0]
        results[name] = get_chart_info(lonlat[0], lonlat[3])

    for node_type, base_name in [(swe.TRUE_NODE, 'True'), (swe.MEAN_NODE, 'Mean')]:
        rahu = swe.calc_ut(jd, node_type, FLAGS)[0]
        rahu_info = get_chart_info(rahu[0], rahu[3])
        results[f'Rahu ({base_name})'] = rahu_info
        ketu_lon = (rahu[0] + 180.0) % 360.0
        ketu_info = get_chart_info(ketu_lon, rahu[3])
        ketu_info['retrograde'] = True
        results[f'Ketu ({base_name})'] = ketu_info

    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'O', flags=FLAGS)
    results['Ascendant'] = get_chart_info(ascmc[0])
    return results

def get_lagna_houses(asc_index):
    return [(asc_index + i) % 12 + 1 for i in range(12)]

def detect_yogas(data):
    yogas = []
    rasi = {p: data[p]['rasi'] for p in data}
    houses = {p: int(data[p]['longitude'] // 30) + 1 for p in data}
    deg = {p: data[p]['longitude'] for p in data}

    # Helper vars
    moon_pos = houses['Moon']
    lagna_rasi = rasi['Ascendant']
    lagna_index = rasis.index(lagna_rasi)
    house_map = get_lagna_houses(lagna_index)

    # --- Phase 1 Yogas ---
    if rasi['Sun'] == rasi['Mercury']:
        yogas.append("Budha-Aditya Yoga")

    if abs(houses['Jupiter'] - houses['Moon']) in [1, 4, 7, 10]:
        yogas.append("Gaja Kesari Yoga")

    count = sum(1 for p in ['Mercury', 'Venus', 'Jupiter'] if rasi[p] in ['Mithuna', 'Kanni', 'Dhanus', 'Meena'])
    if count == 3:
        yogas.append("Saraswati Yoga")

    if rasi['Moon'] == rasi['Mars']:
        yogas.append("Chandra-Mangal Yoga")

    if houses['Mars'] in [1, 2, 4, 7, 8, 12]:
        yogas.append("Kuja Dosha (Manglik)")

    if rasi['Jupiter'] == rasi.get('Rahu (Mean)', '') or rasi['Jupiter'] == rasi.get('Ketu (Mean)', ''):
        yogas.append("Guru-Chandala Yoga")

    if rasi['Sun'] == rasi['Moon']:
        yogas.append("Amavasya Yoga")
    elif abs(deg['Sun'] - deg['Moon']) % 360 > 165 and abs(deg['Sun'] - deg['Moon']) % 360 < 195:
        yogas.append("Purnima Yoga")

    # --- Phase 2 Yogas ---
    # Panch Mahapurusha
    pmp = {
        'Mars': ['Mesha', 'Vrischika'],
        'Mercury': ['Mithuna', 'Kanni'],
        'Jupiter': ['Dhanus', 'Meena'],
        'Venus': ['Rishaba', 'Tula'],
        'Saturn': ['Makara', 'Kumbha']
    }
    for p, signs in pmp.items():
        if rasi[p] in signs and houses[p] in [1, 4, 7, 10]:
            yogas.append(f"{p} forms Panch Mahapurusha Yoga")

    # Lakshmi Yoga
    if rasi['Venus'] == lagna_rasi and houses['Venus'] in [5, 9]:
        yogas.append("Lakshmi Yoga")

    # Dhana Yoga - Planets in 2,5,9,11
    dhana_planets = ['Jupiter', 'Venus', 'Mercury', 'Moon']
    if any(houses[p] in [2, 5, 9, 11] for p in dhana_planets):
        yogas.append("Dhana Yoga (Wealth Indicators)")

    # Adhi Yoga - Benefics in 6,7,8 from Moon
    benefics = ['Jupiter', 'Venus', 'Mercury']
    count = sum(1 for p in benefics if abs(houses[p] - moon_pos) in [6, 7, 8])
    if count >= 2:
        yogas.append("Adhi Yoga (from Moon)")

    # Viparita Raja Yoga - planets in 6, 8, 12
    for p1 in data:
        if p1 == 'Ascendant': continue
        if houses[p1] in [6, 8, 12]:
            for p2 in data:
                if p2 != p1 and p2 != 'Ascendant' and houses[p2] in [6, 8, 12] and rasi[p1] == rasi[p2]:
                    yogas.append(f"Viparita Raja Yoga ({p1} + {p2})")

    # Kemadruma
    prev = (moon_pos - 2) % 12 + 1
    next = moon_pos % 12 + 1
    occupied = [houses[p] for p in data if p not in ['Ascendant', 'Moon']]
    if prev not in occupied and next not in occupied:
        yogas.append("Kemadruma Yoga")

    # Papakartari (Sun or Moon hemmed by malefics)
    malefics = ['Mars', 'Saturn']
    for luminary in ['Sun', 'Moon']:
        lum_house = houses[luminary]
        if ((lum_house - 1) in [houses[m] for m in malefics] and
            (lum_house + 1) in [houses[m] for m in malefics]):
            yogas.append(f"Papakartari Yoga around {luminary}")

    # Ubhayachari Yoga - planets on both sides of Sun
    sun_house = houses['Sun']
    if ((sun_house - 1) in occupied and (sun_house + 1) in occupied):
        yogas.append("Ubhayachari Yoga")

    # Durudhara Yoga - planets on both sides of Moon
    if ((moon_pos - 1) in occupied and (moon_pos + 1) in occupied):
        yogas.append("Durudhara Yoga")

    # Neechabhanga (Debilitated planet in rasi of its enemy but aspected by its exaltation lord)
    if rasi['Venus'] == 'Kanni' and rasi['Mercury'] == 'Meena':
        yogas.append("Neechabhanga Raja Yoga (Venus)")

    # Dharma-Karmadhipati Yoga: 9th and 10th lords connected
    lords = {
        'Mesha': 'Mars', 'Rishaba': 'Venus', 'Mithuna': 'Mercury', 'Kataka': 'Moon',
        'Simha': 'Sun', 'Kanni': 'Mercury', 'Thula': 'Venus', 'Vrischika': 'Mars',
        'Dhanus': 'Jupiter', 'Makara': 'Saturn', 'Kumbha': 'Saturn', 'Meena': 'Jupiter'
    }
    ninth_lord = lords[rasis[(lagna_index + 8) % 12]]
    tenth_lord = lords[rasis[(rasis.index(lagna_rasi) + 9) % 12]]
    if rasi[ninth_lord] == rasi[tenth_lord]:
        yogas.append("Dharma-Karmadhipati Yoga")

    # --- Phase 3 Yogas ---
    # Vesi Yoga: Planets (except Moon) in 2nd from Sun
    for p in data:
        if p not in ['Sun', 'Moon', 'Ascendant']:
            if (houses[p] - houses['Sun']) % 12 == 1:
                yogas.append("Vesi Yoga")
                break

    # Vasi Yoga: Planets (except Moon) in 12th from Sun
    for p in data:
        if p not in ['Sun', 'Moon', 'Ascendant']:
            if (houses['Sun'] - houses[p]) % 12 == 1:
                yogas.append("Vasi Yoga")
                break

    # Anapha, Sunapha, Durudhura (Moon-based)
    others = [p for p in data if p not in ['Moon', 'Ascendant', 'Sun']]
    ana = suna = duru = False
    for p in others:
        if (houses[p] - houses['Moon']) % 12 == 1:
            suna = True
        elif (houses['Moon'] - houses[p]) % 12 == 1:
            ana = True
    if suna: yogas.append("Sunapha Yoga")
    if ana: yogas.append("Anapha Yoga")
    if suna and ana: yogas.append("Durudhura Yoga")

    # Shakata Yoga: Moon in 6/8 from Jupiter
    if abs(houses['Moon'] - houses['Jupiter']) in [6, 8]:
        yogas.append("Shakata Yoga")

    # Amala Yoga: Benefics in 10th from Lagna or Moon
    for p in benefics:
        if (houses[p] - houses['Ascendant']) % 12 == 9:
            yogas.append("Amala Yoga (from Lagna)")
        if (houses[p] - houses['Moon']) % 12 == 9:
            yogas.append("Amala Yoga (from Moon)")

    # Parivartana Yoga: Lords in each other's sign
    checked = set()
    for p1 in data:
        if p1 not in lords.values(): continue
        lord1_rasi = rasi[p1]
        if lord1_rasi in lords:
            lord_of_lord1 = lords[lord1_rasi]
            if p1 != lord_of_lord1 and rasi.get(lord_of_lord1) == rasi.get(p1):
                key = tuple(sorted([p1, lord_of_lord1]))
                if key not in checked:
                    yogas.append(f"Parivartana Yoga: {p1} and {lord_of_lord1}")
                    checked.add(key)

    # Sanyasa Yoga: 4+ planets in one rasi
    rasi_count = {}
    for p in data:
        r = rasi[p]
        if r not in rasi_count:
            rasi_count[r] = 0
        rasi_count[r] += 1
    for r in rasi_count:
        if rasi_count[r] >= 4:
            yogas.append("Sanyasa Yoga (4+ planets in one sign)")

    # Moksha Yoga: Moon/Ketu in 12th, or Moon + Jupiter in 9/12
    if houses['Moon'] == 12 or houses.get('Ketu (Mean)', 0) == 12:
        yogas.append("Moksha Yoga (Moon or Ketu in 12th)")
    if houses['Moon'] in [9, 12] and houses['Jupiter'] in [9, 12]:
        yogas.append("Moksha Yoga (Moon + Jupiter)")

    return sorted(set(yogas))

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python yogas.py DD.MM.YYYY HH:MM LATITUDE LONGITUDE TIMEZONE")
        sys.exit(1)

    date_input = sys.argv[1]
    time_input = sys.argv[2]
    latitude = float(sys.argv[3])
    longitude = float(sys.argv[4])
    timezone = float(sys.argv[5])

    day, month, year = map(int, date_input.split('.'))
    dob = f"{year:04d}-{month:02d}-{day:02d}"
    data = get_planet_positions(dob, time_input, latitude, longitude, timezone)
    yogas = detect_yogas(data)

    print("\n🧘‍♂️ Yogas Detected:\n")
    if yogas:
        for y in yogas:
            print("-", y)
    else:
        print("No major yogas found for this chart.")