from astropy.coordinates import SkyCoord
import astropy.units as u

def get_star_info(star_name):
    """
    Fetches and formats the celestial coordinates for a given star.
    """
    try:
        # Astropy queries the SIMBAD database for the coordinates
        coord = SkyCoord.from_name(star_name)
        
        print(f"--- Data for {star_name.capitalize()} ---")
        print(f"Right Ascension (RA): {coord.ra.to_string(unit=u.hour, sep='hms')}")
        print(f"Declination (Dec): {coord.dec.to_string(unit=u.degree, sep='dms')}")
        
    except Exception as e:
        print(f"Could not find data for {star_name}. Error: {e}")

if __name__ == "__main__":
    # Example: Look up Sirius, the brightest star in the night sky
    get_star_info("Sirius")