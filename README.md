# SafeBD-Impact-Engine
# SafeBD: An Automated Multi-Hazard Impact Engine for Last-Mile Early Warning
**Thematic Areas:** ResilienceAI (Track 1) & Last-Mile Early Warning (Track 2)
**Location:** Chattogram, Bangladesh

## Abstract
Current early warning systems in Bangladesh often suffer from a "Granularity Gap"—official forecasts are too broad, and "Last-Mile" communities in isolated hilly terrains remain disconnected from actionable data. This project presents **SafeBD**, an automated geospatial pipeline developed to bridge this gap by identifying hyper-local impact zones. 

Utilizing **ALOS PALSAR (12.5m)** L-band SAR data and **CHIRPS** 35-year rainfall history, we implemented a **Weighted Intensity Index** ($Slope \times Rainfall$) to analyze 251 detected infrastructure objects. By intersecting these scores with a **Physically-based Topographic Wetness Index (TWI)**, our system successfully isolated **3 "Ground Zero" structures** facing the highest probability of compound landslide and flood impact. 

## Methodology & Automation
The SafeBD engine functions as a three-stage automated decision support system:
1. **Automated Feature Extraction:** Identification of 251 building footprints in high-risk corridors using geospatial databases.
2. **Impact Calculation:** A weighted-index algorithm ($Slope > 30^\circ \times Rainfall Intensity$) to isolate 54 high-risk targets.
3. **Compound Risk Filtering:** Automated spatial intersection with inundation zones to identify the final 3 critical impact coordinates.

## Last-Mile Strategy (Problem 2 Connection)
To solve the communication gap, SafeBD moves beyond broad broadcasts to **Precision Alerting**. By providing the exact coordinates of the 3 most critical structures, we enable local authorities to deploy **targeted, manual intervention** and localized siren triggers, ensuring a 100% evacuation rate where mobile networks and internet services are unreliable.

## Validation
Our methodology was cross-validated against historical geotechnical failures, specifically matching the intensity and slope profiles of the **2015 Tiger Pass event**, providing a high-confidence model for real-world disaster preparedness.
