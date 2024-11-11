202211202329

Status: #idea
Tags: [[Lakes]] [[Hydrology]] [[Electricity]] [[Darcy's Law]] [[Ohm's Law]]


Imagine we had a perfect record of discharge into a lake, and a perfect record of lake level, in the sense that it is high resolution and high accuracy. Since the flow of mass (water) is conserved, there should exist a function $f(Q) = h$  that performs a continuous transformation from the inflow signal $Q$ to the lake level $h$ (or volume, or area.) If this is true, how do we uncover that function? From definitions, as they lead to mathematic clues.

A valid question to ask: *What **is** a lake?* 

 A lake is a reservoir of water. By definition there must be some force resisting the flow of the reservoir water to the ocean (otherwise the lake would not exist). Additionally, the magnitude of that resistance to flow (small drain pipe versus an outlet channel) determines the volume of water within the reservoir, which itself sits inside a larger topographic depression. However, not all topographic depressions are alike, some are wide and shallow while others are narrow and deep. At some point, the volume of water in the basin will overtop its container and drain into adjacent watersheds.The topography of a lake basin determines how much available space for water, or the capacity, there is for a given volume of water in the basin (and a given resistance force). 

These two simple concepts, a resisting force to flow and the capacity of a system to store that resisted flow, are quite common to the electrical engineer, for they constitute a simple circuit.

In fact, appealing to the analogy between electricty and water is not new. Most students in high school or college physics will encounter a tank of water with a valve on it designed to teach about the flow of voltage through a circuit. Indeed, Maxwell himself omitted hydrodynamics from his work, but he was fascinated by the flow of water. What's more, the isomorphism between [[Darcy's Law]] and [[Ohm's Law]] is well known (cite a lot) and is used effectively across disciplines (cite a lot):


$$
q = -k \cdot \frac{dh}{dl} \equiv i = \frac{1}{R} \cdot \frac{\Delta V}{L} \tag{1}
$$


Both equations can be represented in their "electric" form:

$$
V = I \cdot R \equiv P = Q\cdot R \tag{2}
$$
where:
- $Q =$ *discharge* $\frac{m^3}{s} \frac{[L^3]}{[T]}$
- $R$ = *hydraulic resistance* $\frac{kg}{m^{4}s}\frac{[M]}{[L^{4}][T]}$ 
- $P$ = *pressure* $\frac{kg}{m s^{2}} \frac{[M]}{[L] [T^{2}]}$ 

Transition here.

The first question to ask is whether there are legitimate units for hydraulic resistance and hydraulic capacitance: 

Hydraulic Resistance is the ratio between pressure in the lake and discharge *out of the lake* which takes the direct units for acoustic impedence, and can be conceptualized as the inverse of hydraulic conductivity.
$$
R = \frac{\Delta P}{\Delta Q} = \frac{kg}{m^4 s} \equiv \frac{\Delta V}{\Delta I} = \Omega \tag{3}
$$
From now on I will refer to the units of resistance as hydraulic ohms to bolster the analogy in the reader's mind, denoted by $\Omega_H$.

Hydraulic capacitance is also a unit, though it is, as far as I can surmise, used cheifly in hydraulic machinery and industrial control settings. Nonetheless, hydraulic capacitance is defined as the ratio of volume of water to the pressure—in the same way an electrical capacitor is defined by the ratio of charge to voltage.

$$
C = \frac{\Delta V}{\Delta P} = \frac{m^4s^2}{kg} \equiv \frac{\Delta Q}{\Delta V} = F \tag{4}
$$
luckily for us, water is basically incompressible, so this reduces to 
$$
\frac{A}{\rho g} \tag{5}
$$
This means the capacitance of any body of water is only related to it's *area*! We will revisit this finding later. The units of electric capacitance are Farads, for convenience, we will refer to these as hydraulic Farads, denoted by $F_H$.  




[[Proof of Lake Smoothing]]

Applying [[Darcy's Law]] to the lake circuit gives
$$
P_{in} - P_{out} = R \cdot Q \tag{1}
$$
Our volume equation (2)
$$
V_L(t) = C \cdot P_{out}(t) \tag{2}
$$
Our discharge equation (3)
$$
Q(t) = \frac{dV_L }{dt} \tag{3}
$$
substituting (2) into (3):
$$
Q(t) = C\frac{dP_{out}}{dt} \tag{4}
$$
which can substituted into (1):

$$
P_{in} - P_{out} = R \cdot C\frac{dP_{out}}{dt} \tag{5}
$$
discretizing this equation:

$$
x_i - y_i = RC\frac{y_i-y_{i-1}}{\Delta t} \tag{6}
$$
we can see the recurrence relation in this equation where the x term includes the input contribution at the given time step, and the y term gives the inertia from the previous output.

$$
y_i = x_i (\frac{\Delta t}{RC + \Delta t}) + y_{i-1}(\frac{RC}{RC+\Delta t}) \tag{7}
$$
from (7) we can reformulate the discrete-time implementation of the RC low-pass filter as an exponential smoothing function:

$$
y_i = \alpha x_i + (1-\alpha)y_{i-1} \tag{8}
$$


taking a parameter $\alpha$ at each timestep:
$$
\alpha := \frac{\Delta t}{RC + \Delta t} \tag{9}  
$$






If we can suspend our skepticism for a second: 

1. the time constant $\tau = R \cdot C$  should characterize the overall time dependent behavior of flow through the lake system based on its topography and the system's resistance to flow

2. The ordinary differential equations that describe the flow of electrons through circuit elements should also describe the flow of water molecules through a connected river and lake system.

The key to this analogy is to recognize that the flow of water in a lake catchment is driven by hydraulic head, or pressure. 

Extra:
		2. distribution of elevation increases positively or stays constant in all directions from the bottom of the lake until some arbitrary height $h$ above the bottom. (monotonically increasing hypsometric relation).
	3.  any one time, this term is defined as the   or, of the reservoir (within the physical limits of the topography).  In order for reservoir of water to exist above mean sea level, several things need to be true:
		1. There must be be a topographic depression
		3. There must be some source of water, either infiltrating from below or more commonly flowing in from higher elevations.
		4. the volume of water inflow is greater than water outflow at least once over some time interval T (otherwise there is no standing water).

use half life instead of residence time because we are making no claims about the residence time of a molecule of water or the mixing regime of the lake, only the volumetric flow of water.

Idea: use machine learning to find parameters to fit the function. You can assume C is good. if tau describes the system, you have figured out the resistance of the drainage network.


Something interesting: Hydraulic Resistance per unit time is equivalent to $\frac{dp}{dz}$ which is equivalent to $-\rho g$  

---
# {{References}}

Mason, Huybers, Hubbard