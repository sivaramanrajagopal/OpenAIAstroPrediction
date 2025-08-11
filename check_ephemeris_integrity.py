import os
import hashlib

def check_ephemeris_files():
    ephe_path = os.path.join('backend', 'ephe')
    
    print("🔍 EPHEMERIS FILE INTEGRITY CHECK")
    print("=" * 50)
    
    if not os.path.exists(ephe_path):
        print(f"❌ Ephemeris directory not found: {ephe_path}")
        return
    
    files = os.listdir(ephe_path)
    print(f"📁 Ephemeris files found: {len(files)}")
    
    for file in sorted(files):
        file_path = os.path.join(ephe_path, file)
        if os.path.isfile(file_path):
            # Get file size and hash
            size = os.path.getsize(file_path)
            
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            
            print(f"  {file:15} | {size:8} bytes | MD5: {file_hash}")
    
    print(f"\n🔍 RECOMMENDATIONS:")
    print(f"1. Download official Swiss Ephemeris files from:")
    print(f"   https://www.astro.com/swisseph/")
    print(f"2. Ensure files are complete (not truncated)")
    print(f"3. Use specific ephemeris range for 1978 (semo_00.se1, seas_00.se1)")
    print(f"4. Consider using higher precision files if available")

if __name__ == "__main__":
    check_ephemeris_files()