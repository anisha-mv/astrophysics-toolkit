import numpy as np
from scipy import constants

def calculate_escape_velocity(mass_kg, radius_m):
    """
    Calculates the escape velocity of a celestial body.
    Formula: v = sqrt(2 * G * M / R)
    """
    # constants.G is the gravitational constant
    velocity = np.sqrt((2 * constants.G * mass_kg) / radius_m)
    return velocity

if __name__ == "__main__":
    # Example: Earth
    earth_mass = 5.972e24  # kg
    earth_radius = 6371000 # meters
    
    v_escape = calculate_escape_velocity(earth_mass, earth_radius)
    
    # Convert to km/s for readability
    print(f"Earth's escape velocity is approximately {v_escape / 1000:.2f} km/s")