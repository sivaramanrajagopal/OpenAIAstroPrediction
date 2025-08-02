import os
import glob

# Swiss Ephemeris setup to add to all files
swe_setup = '''
# --- Setup Swiss Ephemeris ---
swe.set_ephe_path('./ephe')  # Use ephemeris files
swe.set_sid_mode(swe.SIDM_LAHIRI)  # Lahiri ayanamsa (Vedic)
'''

# Find all Python files that might use Swiss Ephemeris
python_files = ['dasa_bhukti.py', 'spouse_analysis.py', 'dasa.py', 'indu_dasa.py']

for filename in python_files:
    if os.path.exists(filename):
        print(f"🔧 Updating {filename}...")

        with open(filename, 'r') as f:
            content = f.read()

        # Look for existing Swiss Ephemeris setup
        if 'swe.set_ephe_path' in content:
            print(f"   ✅ {filename} already has ephemeris setup")
        else:
            print(f"   ⚠️  {filename} needs ephemeris setup - please update manually")

print("\n📋 Manual updates needed:")
print("1. Add 'swe.set_ephe_path('./ephe')' to the top of each module")
print("2. Restart your FastAPI server")
print("3. Test all endpoints")