import swisseph as swe
import datetime
from collections import OrderedDict

# --- Setup Swiss Ephemeris ---
swe.set_ephe_path('.')
swe.set_sid_mode(swe.SIDM_LAHIRI)

# --- Nakshatras & Rasis ---
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

rasi_lords = {
    "Mesha": "Mars", "Rishaba": "Venus", "Mithuna": "Mercury",
    "Kataka": "Moon", "Simha": "Sun", "Kanni": "Mercury",
    "Thula": "Venus", "Vrischika": "Mars", "Dhanus": "Jupiter",
    "Makara": "Saturn", "Kumbha": "Saturn", "Meena": "Jupiter"
}

dasa_order = [
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury"
]

dasa_durations = OrderedDict([
    ("Ketu", 7), ("Venus", 20), ("Sun", 6), ("Moon", 10), ("Mars", 7),
    ("Rahu", 18), ("Jupiter", 16), ("Saturn", 19), ("Mercury", 17)
])

nakshatra_lords = [
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu",
    "Jupiter", "Saturn", "Mercury"
] * 3

# --- Indu Lagnam Value Table ---
rasi_values = {
    "Mesha": 6, "Rishaba": 12, "Mithuna": 8, "Kataka": 16,
    "Simha": 30, "Kanni": 8, "Thula": 12, "Vrischika": 6,
    "Dhanus": 10, "Makara": 1, "Kumbha": 1, "Meena": 10
}

def get_chart_info(longitude, speed=None):
    return {
        'longitude': longitude,
        'retrograde': speed < 0 if speed is not None else None,
        'rasi': rasis[int(longitude // 30)],
        'nakshatra': nakshatras[int((longitude % 360) // (360 / 27))],
        'pada': int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1)
    }

def get_planet_positions(jd, lat, lon):
    flags = swe.FLG_SIDEREAL | swe.FLG_SPEED
    results = {}
    swe.set_topo(lon, lat, 0)
    for pid in range(10):
        name = swe.get_planet_name(pid)
        lonlat = swe.calc_ut(jd, pid, flags)[0]
        results[name] = get_chart_info(lonlat[0], lonlat[3])
    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'O', flags=flags)
    results['Ascendant'] = get_chart_info(ascmc[0])
    return results

def find_ninth_house(start_rasi):
    idx = rasis.index(start_rasi)
    return rasis[(idx + 8) % 12]

def calculate_indu_lagnam(asc_rasi, moon_rasi):
    ninth_from_asc = find_ninth_house(asc_rasi)
    ninth_from_moon = find_ninth_house(moon_rasi)
    total = rasi_values[ninth_from_asc] + rasi_values[ninth_from_moon]
    remainder = total % 12
    if remainder == 0:
        remainder = 12
    indu_index = (rasis.index(moon_rasi) + (remainder - 1)) % 12
    return rasis[indu_index]

def find_planets_in_rasi(planet_positions, target_rasi):
    return [planet for planet, details in planet_positions.items() if details.get('rasi') == target_rasi]

def generate_dasa_table(jd, moon_longitude, years=90):
    nak_index = int((moon_longitude % 360) // (360 / 27))
    nak_lord = nakshatra_lords[nak_index]
    portion_completed = (moon_longitude % (360 / 27)) / (360 / 27)
    balance_years = dasa_durations[nak_lord] * (1 - portion_completed)

    start_date = datetime.datetime(*swe.revjul(jd)[:3])
    dasa_table, current_year = [], 0
    current_index = dasa_order.index(nak_lord)

    while current_year < years:
        for i in range(len(dasa_order)):
            planet = dasa_order[(current_index + i) % len(dasa_order)]
            duration = dasa_durations[planet]
            if i == 0:
                duration = balance_years

            end_year = current_year + duration
            end_date = start_date + datetime.timedelta(days=duration * 365.25)
            dasa_table.append({
                'planet': planet,
                'start_date': start_date,
                'end_date': end_date
            })
            current_year, start_date = end_year, end_date
            if current_year >= years:
                break
    return dasa_table

def generate_bhukti_periods(dasa_start, dasa_end, dasa_planet):
    total_days = (dasa_end - dasa_start).days
    bhukti_list = []
    current_start = dasa_start
    for p in dasa_order:
        fraction = dasa_durations[p] / 120.0
        b_end = current_start + datetime.timedelta(days=int(total_days * fraction))
        bhukti_list.append({
            "maha_dasa": dasa_planet,
            "bukti": p,
            "start": current_start,
            "end": b_end
        })
        current_start = b_end
    return bhukti_list

def get_indu_dasa(dob, tob, lat, lon, tz_offset=5.5):
    local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute/60.0)

    planet_positions = get_planet_positions(jd, lat, lon)
    asc_rasi = planet_positions['Ascendant']['rasi']
    moon_rasi = planet_positions['Moon']['rasi']

    indu_lagnam = calculate_indu_lagnam(asc_rasi, moon_rasi)
    indu_lord = rasi_lords[indu_lagnam]
    planets_in_indu = find_planets_in_rasi(planet_positions, indu_lagnam)

    moon_long = planet_positions['Moon']['longitude']
    dasa_table = generate_dasa_table(jd, moon_long)

    relevant_planets = [indu_lord] + planets_in_indu
    filtered_timeline = []
    for d in dasa_table:
        bhukti_periods = generate_bhukti_periods(d['start_date'], d['end_date'], d['planet'])
        for b in bhukti_periods:
            if b['maha_dasa'] in relevant_planets or b['bukti'] in relevant_planets:
                filtered_timeline.append({
                    'maha_dasa': b['maha_dasa'],
                    'bukti': b['bukti'],
                    'start': b['start'].strftime("%Y-%m-%d"),
                    'end': b['end'].strftime("%Y-%m-%d")
                })

    return {
        "ascendant": asc_rasi,
        "moon_rasi": moon_rasi,
        "indu_lagnam": indu_lagnam,
        "indu_lord": indu_lord,
        "planets_in_indu_lagnam": planets_in_indu,
        "timeline": filtered_timeline
    }
