---
author_profile: true
layout: single
permalink: /random-musings/new-resistance
title: New Resistance
---

To derive the hydraulic resistance R for an open channel flow (such as a lake outlet), we start with Manning's equation and the definition of hydraulic resistance:

Manning's equation:
$$
v = \frac{1}{n} R_h^{2/3} S^{1/2} \tag{3a}
$$

Discharge:
$$
Q = vA \tag{3b}
$$

Pressure difference:
$$
\Delta P = \rho g \Delta h = \rho g S L \tag{3c}
$$

Hydraulic resistance:
$$
R = \frac{\Delta P}{\Delta Q} \tag{3d}
$$

Substituting (3a) and (3b) into (3d):

$$
R = \frac{\rho g S L}{(1/n) R_h^{2/3} S^{1/2} A} \tag{3e}
$$

Simplifying:

$$
R = \frac{\rho g n S^{1/2} L}{R_h^{2/3} A} \tag{3f}
$$

This gives us the correct expression for hydraulic resistance R in terms of channel geometry, fluid properties, and roughness:

$$
R = \frac{\rho g n S^{1/2} L}{R_h^{2/3} A} \quad [\frac{kg}{m^4 s}] \tag{3g}
$$

where:
- ρ is the density of water (kg/m³)
- g is the acceleration due to gravity (m/s²)
- n is Manning's roughness coefficient
- S is the slope of the channel
- L is the length of the channel (m)
- R_h is the hydraulic radius (m)
- A is the cross-sectional area of the channel (m²)