import os
import urllib.request
import pyswisseph as swe

# Correct URLs for ephemeris files
EPHE_FILES = {
    "seas_18.se1": "https://www.astro.com/ftp/swisseph/ephe/seas_18.se1",
    "sepl_18.se1": "https://www.astro.com/ftp/swisseph/ephe/sepl_18.se1",
    "semo_18.se1": "https://www.astro.com/ftp/swisseph/ephe/semo_18.se1"
}


def download_ephe_files():
    """
    Download ephemeris files if not already present.
    """
    ephe_dir = "ephe"
    if not os.path.exists(ephe_dir):
        os.makedirs(ephe_dir)

    for filename, url in EPHE_FILES.items():
        file_path = os.path.join(ephe_dir, filename)
        if not os.path.exists(file_path):
            print(f"Downloading {filename}...")
            try:
                urllib.request.urlretrieve(url, file_path)
                print(f"Downloaded: {filename}")
            except Exception as e:
                print(f"Error downloading {filename}: {e}")

    return ephe_dir


def setup_swiss_ephemeris():
    """
    Sets up Swiss Ephemeris with correct path.
    """
    ephe_dir = download_ephe_files()
    swe.set_ephe_path(ephe_dir)
    print(f"Swiss Ephemeris path set to: {ephe_dir}")


# Automatically set up Swiss Ephemeris when imported
setup_swiss_ephemeris()
