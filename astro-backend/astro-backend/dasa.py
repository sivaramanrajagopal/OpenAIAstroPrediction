import swisseph as swe
import datetime
from collections import OrderedDict

# -------------------------
# CONSTANTS
# -------------------------
NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni",
    "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
    "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana",
    "Dhanishta", "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada",
    "Revati"
]

# Nakshatra lords (cycle of 9 planets repeated)
NAKSHATRA_LORDS = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"] * 3

# Dasa order & their durations in years
DASA_ORDER = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
DASA_DURATIONS = OrderedDict([
    ("Ketu", 7), ("Venus", 20), ("Sun", 6), ("Moon", 10), 
    ("Mars", 7), ("Rahu", 18), ("Jupiter", 16), ("Saturn", 19), ("Mercury", 17)
])

# -------------------------
# HELPER FUNCTIONS
# -------------------------

def get_nakshatra(longitude):
    """
    Given a longitude, return:
    - Nakshatra name
    - Pada (1-4)
    - Nakshatra index (0-26)
    """
    nakshatra_index = int((longitude % 360) // (360 / 27))
    pada = int(((longitude % (360 / 27)) / (360 / 27 / 4)) + 1)
    return NAKSHATRAS[nakshatra_index], pada, nakshatra_index


def calculate_dasa_start(moon_longitude):
    """
    Determine the starting Dasa based on Moon's position.
    Returns:
    - Birth Nakshatra
    - Pada
    - Current Dasa Lord
    - Remaining years in the current Maha Dasa
    """
    nakshatra, pada, nakshatra_index = get_nakshatra(moon_longitude)
    nakshatra_length = 360 / 27
    remainder = moon_longitude % nakshatra_length
    portion_completed = remainder / nakshatra_length

    current_dasa_lord = NAKSHATRA_LORDS[nakshatra_index]
    total_years = DASA_DURATIONS[current_dasa_lord]
    remaining_years = total_years * (1 - portion_completed)

    return nakshatra, pada, current_dasa_lord, remaining_years


def generate_dasa_table(jd, moon_longitude, total_years=120):
    """
    Generate Vimshottari Dasa table up to total_years.
    Returns:
    - Birth Nakshatra
    - Pada
    - List of Dasa periods (each as a dict)
    """
    nakshatra, pada, current_dasa_lord, remaining_years = calculate_dasa_start(moon_longitude)

    # Initialize timeline
    start_date = datetime.datetime(*swe.revjul(jd)[:3])
    dasa_table = []
    current_age = 0
    current_index = DASA_ORDER.index(current_dasa_lord)

    while current_age < total_years:
        for i in range(len(DASA_ORDER)):
            planet = DASA_ORDER[(current_index + i) % len(DASA_ORDER)]
            duration = DASA_DURATIONS[planet]
            if i == 0:
                duration = remaining_years  # Adjust for the first Dasa

            end_age = current_age + duration
            if current_age >= total_years:
                break

            end_date = start_date + datetime.timedelta(days=duration * 365.25)
            dasa_table.append({
                "planet": planet,
                "start_age": round(current_age, 2),
                "end_age": round(end_age, 2),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "duration": round(duration, 2)
            })

            current_age = end_age
            start_date = end_date

        current_index = 0  # Reset after completing the cycle

    return nakshatra, pada, dasa_table

# -------------------------
# MAIN (Standalone Testing)
# -------------------------
def main():
    dob = "1977-10-29"
    tob = "21:30"
    lat, lon, tz_offset = 13.08333333, 80.28333333, 5.5

    try:
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)

        moon_long = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
        birth_nakshatra, birth_pada, dasa_table = generate_dasa_table(jd, moon_long)

        print(f"\nBirth Nakshatra: {birth_nakshatra} (Pada {birth_pada})")
        print("\nVimshottari Dasa Table:")
        print("-" * 80)
        print(f"{'Planet':<10}{'Start Age':<12}{'End Age':<12}{'Duration':<12}{'Start Date':<15}{'End Date':<15}")
        print("-" * 80)
        for period in dasa_table[:12]:
            print(
                f"{period['planet']:<10}{period['start_age']:<12.2f}{period['end_age']:<12.2f}"
                f"{period['duration']:<12.2f}{period['start_date']:<15}{period['end_date']:<15}"
            )

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    swe.set_ephe_path('./ephe')
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    main()
