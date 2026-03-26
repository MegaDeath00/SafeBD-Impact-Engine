# SafeBD: Automated Risk Detection Logic (RIMES 2026)
# This script simulates the spatial logic used to isolate the 'Critical 3'

def check_safety(slope, rainfall_intensity, in_flood_sink):
    # Logic: Cross-referencing Geotechnical and Hydrological triggers
    if slope > 30 and rainfall_intensity > 0.8:
        if in_flood_sink:
            return "CRITICAL: Immediate Evacuation Required (Ground Zero)"
        return "HIGH RISK: Landslide Warning"
    return "STABLE: Monitor Weather"

# Result: Pipeline isolated 3 Critical Points from 251 detected objects.
print(check_safety(slope=35, rainfall_intensity=0.9, in_flood_sink=True))
