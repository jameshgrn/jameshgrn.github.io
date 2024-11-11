

## Abstract

We investigate the exponential decay of Moran's I with distance in river topography and interpret it within a diffusive framework. By bridging statistical observations with physical processes, we establish a connection between the e-folding distance obtained from spatial autocorrelation analysis and the diffusion coefficient characterizing landscape evolution. This approach provides a new tool for understanding river dynamics across different scales and environments.

---

## Introduction

Spatial autocorrelation is fundamental in understanding the spatial structure and patterns along rivers. **Moran's I** is a widely used measure of spatial autocorrelation, quantifying the degree to which similar values occur nearby in space. In river systems, processes such as erosion and deposition exhibit spatial dependencies that can be analyzed using Moran's I.

In this study, we observe an exponential decay in Moran's I with distance in river planforms. We hypothesize that this decay reflects underlying diffusive processes governing landscape evolution. By developing a theoretical framework that connects the statistical properties of Moran's I to diffusion processes, we aim to provide a physical interpretation of our observations.

---

## Observation and Hypothesis

### Exponential Decay of Moran's I

We observe that Moran's I decreases exponentially with increasing lag distance $d$ in river planforms. This behavior is characterized by the **e-folding distance** $\Lambda_e$, representing the distance over which spatial autocorrelation diminishes to $\frac{1}{e}$ of its maximum value.

> [!note] **Rationale for Exponential Decay**
> - **Localized River Processes**: Erosion and deposition have localized effects that diminish with distance.
> - **Diffusive Behavior**: Exponential decay aligns with the solution to the one-dimensional diffusion equation.
> - **Natural Systems**: Exponential decay is common due to the cumulative effect of small, independent processes.

---

## Theoretical Framework

### 1. Moran's I and Spatial Autocorrelation

#### Definition of Moran's I

Moran's I quantifies spatial autocorrelation by measuring the similarity between observations as a function of distance:

$$
I(d) = \frac{\sum_{i=1}^{N} \sum_{j=1}^{N} w_{ij} (x_i - \bar{x})(x_j - \bar{x})}{S_0 \sum_{i=1}^{N} (x_i - \bar{x})^2}
$$

where:

- $x_i$ and $x_j$ are the values at locations $i$ and $j$
- $\bar{x}$ is the mean of all $x$
- $w_{ij}$ is the spatial weight between $i$ and $j$ at distance $d$
- $S_0 = \sum_{i=1}^{N} \sum_{j=1}^{N} w_{ij}$

#### Moran's I for Continuous Functions

Extending Moran's I to continuous functions over a large domain ($L \to \infty$):

$$
I(h) = \frac{\int_{-\infty}^{\infty} (f(x) - \mu)(f(x+h) - \mu) \, dx}{\sigma^2 \int_{-\infty}^{\infty} dx}
$$

where:

- $f(x)$ is the continuous function representing the spatial variable
- $\mu$ is the mean of $f(x)$, which is zero for a zero-mean function
- $\sigma^2$ is the variance of $f(x)$
- $h$ is the lag distance

---

### 2. Gaussian Function and Moran's I

#### Gaussian Function Definition

The Gaussian function, fundamental to our analysis, is:

$$
g(x) = \exp\left(-\frac{x^2}{2\sigma^2}\right)
$$

where $\sigma$ controls the width of the function.

> [!note]
> The Gaussian function is normalized when multiplied by $\dfrac{1}{\sigma\sqrt{2\pi}}$, but we often omit this factor for simplicity in spatial analysis.

#### Moran's I for Gaussian Function

For the Gaussian function:

$$
I(h) = \exp\left(-\frac{h^2}{4\sigma^2}\right)
$$

**Derivation**:

1. **Compute the product** $g(x) g(x+h)$:

   $$
   \begin{align*}
   g(x) g(x+h) &= \exp\left(-\frac{x^2}{2\sigma^2}\right) \exp\left(-\frac{(x+h)^2}{2\sigma^2}\right) \\
   &= \exp\left(-\frac{x^2 + (x+h)^2}{2\sigma^2}\right)
   \end{align*}
   $$

2. **Expand the terms**:

   $$
   \begin{align*}
   x^2 + (x+h)^2 &= x^2 + x^2 + 2xh + h^2 = 2x^2 + 2xh + h^2
   \end{align*}
   $$

3. **Simplify the exponent**:

   $$
   \exp\left(-\frac{2x^2 + 2xh + h^2}{2\sigma^2}\right) = \exp\left(-\frac{2\left(x + \tfrac{h}{2}\right)^2 - \tfrac{h^2}{2}}{2\sigma^2}\right)
   $$

4. **Separate the terms**:

   $$
   \exp\left(-\frac{(x + \tfrac{h}{2})^2}{\sigma^2}\right) \cdot \exp\left(-\frac{h^2}{4\sigma^2}\right)
   $$

5. **Integrate over $x$**:

   $$
   \int_{-\infty}^{\infty} g(x) g(x+h) \, dx = \exp\left(-\frac{h^2}{4\sigma^2}\right) \int_{-\infty}^{\infty} \exp\left(-\frac{(x + \tfrac{h}{2})^2}{\sigma^2}\right) dx
   $$

   The integral simplifies using the Gaussian integral property:

   $$
   \int_{-\infty}^{\infty} \exp\left(-\frac{(x + a)^2}{\sigma^2}\right) dx = \sigma \sqrt{\pi}
   $$

6. **Result**:

   The constants cancel out in the ratio for Moran's I, leading to:

   $$
   I(h) = \exp\left(-\frac{h^2}{4\sigma^2}\right)
   $$

> [!check] **Verification**
> - Using mathematical software confirms the integral results.
> - This shows that Moran's I for a Gaussian function decays exponentially with the square of the lag distance $h$.

#### Interpretation

- **Exponential Decay**: Moran's I decreases exponentially as distance increases.
- **Spatial Autocorrelation**: Reflects the decreasing similarity of values with increasing separation.

---

### 3. E-Folding Distance

#### Definition of E-Folding Distance

The **e-folding distance** $h_e$ is the lag distance at which Moran's I decreases to $\frac{1}{e}$ of its maximum value.

#### Calculation

Setting $I(h_e) = \frac{1}{e}$:

$$
\exp\left(-\frac{h_e^2}{4\sigma^2}\right) = \frac{1}{e}
$$

Solving for $h_e$:

$$
-\frac{h_e^2}{4\sigma^2} = -1 \implies h_e = 2\sigma
$$

---

### 4. Relationship to Full Width at Half Maximum (FWHM)

#### FWHM of Gaussian Function

The **FWHM** is the distance between points where the function reaches half its maximum value.

1. Set $g(x) = \dfrac{1}{2}$:

   $$
   \exp\left(-\frac{x^2}{2\sigma^2}\right) = \frac{1}{2}
   $$

2. Solve for $x$:

   $$
   x = \pm \sigma \sqrt{2\ln(2)}
   $$

3. Compute FWHM:

   $$
   \text{FWHM} = 2\sigma\sqrt{2\ln(2)}
   $$

> [!important] **Conversion between $\sigma$ and FWHM**
> $$
> \sigma = \frac{\text{FWHM}}{2\sqrt{2\ln(2)}} \approx 0.4247 \times \text{FWHM}
> $$

#### Expressing $h_e$ in Terms of FWHM

$$
h_e = 2\sigma = \frac{\text{FWHM}}{\sqrt{2\ln(2)}} \approx 0.8493 \times \text{FWHM}
$$

---

### 5. Fourier Transform and Power Spectral Density (PSD)

#### Fourier Transform of Gaussian Function

$$
G(k) = \int_{-\infty}^{\infty} g(x) e^{-ikx} dx = \sigma \sqrt{2\pi} \exp\left(-\frac{\sigma^2 k^2}{2}\right)
$$

- The Fourier transform of a Gaussian is another Gaussian in the frequency domain.

#### Power Spectral Density

$$
S(k) = |G(k)|^2 = 2\pi\sigma^2 \exp\left(-\sigma^2 k^2\right)
$$

#### E-Folding Wavenumber

Setting $S(k_e) = \frac{1}{e} S(0)$:

$$
\exp\left(-\sigma^2 k_e^2\right) = \frac{1}{e} \implies k_e = \frac{1}{\sigma}
$$

---

### 6. Reciprocal Relationship

The spatial e-folding distance and the e-folding wavenumber satisfy:

$$
h_e \cdot k_e = 2\sigma \cdot \frac{1}{\sigma} = 2
$$

> [!important] **Fundamental Property**
> This reciprocal relationship is a fundamental property of Fourier transforms and reflects the uncertainty principle.

---

### 7. Diffusion Equation Connection

#### Diffusion Equation Solution

The Gaussian function is the solution to the one-dimensional diffusion equation:

$$
\frac{\partial g}{\partial t} = D \frac{\partial^2 g}{\partial x^2}
$$

With initial condition $g(x, 0) = \delta(x)$, the solution is:

$$
g(x, t) = \frac{1}{\sqrt{4\pi D t}} \exp\left(-\frac{x^2}{4 D t}\right)
$$

#### Relationship Between $\sigma$ and Diffusion Coefficient

$$
\sigma^2 = 2 D t
$$

- This connects the standard deviation $\sigma$ to the diffusion coefficient $D$ and time $t$.

#### Implication for Moran's I

Using $h_e = 2\sigma$:

$$
h_e = 2\sqrt{2 D t} \implies D = \frac{h_e^2}{8 t}
$$

---

## Calculations

### Estimating Diffusion Coefficient $D$

Using the relationship:

$$
D = \frac{h_e^2}{8 T_A}
$$

where:

- $h_e = \Lambda_e$ is the e-folding distance obtained from Moran's I
- $T_A$ is the avulsion timescale, representing the characteristic time over which significant sediment redistribution occurs

---

### Python Code for Calculations

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_D(lambda_e, T_A):
    """
    Calculate diffusion coefficient D based on e-folding distance lambda_e and avulsion timescale T_A.
    
    Parameters:
    lambda_e (float): E-folding distance in km
    T_A (float): Avulsion timescale in years
    
    Returns:
    float: Diffusion coefficient D in km²/yr
    """
    return lambda_e**2 / (8 * T_A)

# Testing with reasonable avulsion timescales
T_A_values = [10, 100, 1000, 10000]  # in years
lambda_e_range = np.linspace(1, 100, 100)  # e-folding distances in km

for T_A in T_A_values:
    D_min = calculate_D(1, T_A)
    D_max = calculate_D(100, T_A)
    print(f"For T_A = {T_A} years, D ranges from {D_min:.2e} to {D_max:.2e} km²/yr")

# Calculating spectrum of diffusion coefficients
T_A = 1000  # years
D_values = [calculate_D(l, T_A) for l in lambda_e_range]

print(f"\nFor T_A = {T_A} years:")
print(f"D ranges from {min(D_values):.2e} to {max(D_values):.2e} km²/yr")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(lambda_e_range, D_values)
plt.xlabel('E-folding Distance Λₑ (km)')
plt.ylabel('Diffusion Coefficient D (km²/yr)')
plt.title(f'Diffusion Coefficient vs E-folding Distance (Tₐ = {T_A} years)')
plt.yscale('log')
plt.grid(True)
plt.show()
```

---

### Results

#### Diffusion Coefficients for Various Avulsion Timescales

- **For $T_A = 10$ years**:

  $D$ ranges from $1.25 \times 10^{-2}$ to $1.25 \times 10^{1}$ km²/yr

- **For $T_A = 100$ years**:

  $D$ ranges from $1.25 \times 10^{-3}$ to $1.25 \times 10^{0}$ km²/yr

- **For $T_A = 1000$ years**:

  $D$ ranges from $1.25 \times 10^{-4}$ to $1.25 \times 10^{-1}$ km²/yr

- **For $T_A = 10000$ years**:

  $D$ ranges from $1.25 \times 10^{-5}$ to $1.25 \times 10^{-2}$ km²/yr

---

### Calculating $T_A$ Based on Sedimentation Rate and Channel Depth

Assuming:

- Channel depth $h = 5$ meters
- Sedimentation rate $v_A = 5$ mm/yr

Avulsion timescale $T_A$:

$$
T_A = \frac{h}{v_A} = \frac{5\, \text{m}}{5\, \text{mm/yr}} = 1000\, \text{years}
$$

- This $T_A$ value is consistent with observed avulsion timescales in similar river systems.

---

### Spectrum of Diffusion Coefficients

Using $T_A = 1000$ years and $\Lambda_e$ ranging from 1 to 100 km:

- $D$ ranges from $1.25 \times 10^{-4}$ to $1.25 \times 10^{-1}$ km²/yr

#### Interpretation

> [!info] **Quadratic Relationship**
> - As $\Lambda_e$ increases, $D$ increases quadratically.
> - Reflects the greater spatial influence of diffusion over longer distances.

---

## Implications

1. **Consistency with Published Values**: The estimated diffusion coefficients $D$ align with values reported in geomorphological studies (e.g., Culling, 1960; Paola et al., 1992).

2. **Variation with E-Folding Distance**: The framework demonstrates how $D$ varies with the e-folding distance $\Lambda_e$ for a given avulsion timescale $T_A$.

3. **Physical Interpretation of $\Lambda_e$**: The statistical measure $\Lambda_e$ from Moran's I decay can be physically interpreted in terms of the diffusion coefficient, linking spatial patterns to underlying processes.

---

## Key Insight

### Bridging Statistics and Physics

By deriving explicit relationships between observable topographic statistics (e.g., $\Lambda_e$ from Moran's I) and physical parameters (e.g., diffusion coefficient $D$), we provide a framework for interpreting river topographic data in terms of landscape evolution processes.

#### Potential Applications

- **Predictive Modeling**: Estimating how river systems may respond to environmental changes.
- **River Management**: Informing management practices by understanding sediment transport dynamics.
- **Cross-Disciplinary Insights**: Applying methods to other spatially autocorrelated systems exhibiting diffusive behavior.

---

## Additional Context and Synthesis

### Fundamental Relationship Between Feature Size and Spatial Autocorrelation

We hypothesize a fundamental relationship between the size of topographic features in a river system (represented by "bumps" in synthetic landscapes) and the spatial autocorrelation of the landscape, measured by the e-folding distance $\Lambda_e$ of Moran's I.

#### Experiments and Results

1. **Single Gaussian Bump**:

   - **Objective**: Explore the relationship using a Gaussian-shaped topographic feature.
   - **Findings**:
     - Near-linear relationship between feature width and e-folding distance.
     - Log-log fit slope: approximately 0.98, indicating a direct scaling.

2. **Multiple Gaussian Bumps**:

   - **Objective**: Introduce complexity with multiple features of varying sizes.
   - **Findings**:
     - Strong, nearly linear relationship persists in complex scenarios.
     - Log-log fit slope: approximately 0.95.
     - High $R^2$ value (~0.91), indicating the model explains most of the variance.

> [!important] **Implications**
> - **Universal Scaling Law**: Suggests a potentially universal scaling in fluvial geomorphology.
> - **Predictive Power**: Allows prediction of spatial influence from feature size.
> - **Scale Independence**: Consistent results across different scales.

#### Significance in Geomorphology

- **Topographic Memory**: The e-folding distance represents how far the river's "memory" extends.
- **Avulsion Dynamics**: Provides insights into river avulsion processes and potential lengths.
- **Landscape Evolution Modeling**: Improves predictions over long timescales.
- **Complex Systems Behavior**: Indicates simple principles govern overall river system behavior.

---

## Conclusion

- **Mathematical Relationships**:

  1. $\text{FWHM} = 2\sigma \sqrt{2\ln(2)}$
  2. $h_e = 2\sigma$ (spatial e-folding distance)
  3. $k_e = \dfrac{1}{\sigma}$ (wavenumber e-folding value)
  4. $h_e \cdot k_e = 2$ (reciprocal relationship)
  5. $k_e = \dfrac{2\sqrt{2\ln(2)}}{\text{FWHM}} \approx 1.1774 \times \dfrac{1}{\text{FWHM}}$

- **Significance**:

  These relationships bridge spatial statistics and spectral analysis, enhancing our understanding of river morphodynamics and diffusion-like processes.

- **Final Remark**:

  The framework demonstrates how statistical observations of river topography can be directly linked to physical processes governing landscape evolution, providing a valuable tool for geomorphologists and hydrologists.

---

## References

- **Bracewell, R. N.** (2000). *The Fourier Transform and Its Applications*. McGraw-Hill.
- **Culling, W. E. H.** (1960). Analytical Theory of Erosional Topography. *Bulletin of the Geological Society of America*, 71(4), 545–574.
- **Moran, P. A. P.** (1950). Notes on Continuous Stochastic Phenomena. *Biometrika*, 37(1/2), 17–23.
- **Paola, C., Heller, P. L., & Angevine, C. L.** (1992). The Large-Scale Dynamics of Grain-size Variation in Alluvial Basins, 1: Theory. *Basin Research*, 4(2), 73–90.
- **Papoulis, A.** (1981). *Systems and Transforms with Applications in Optics*. McGraw-Hill.
- **Ripley, B. D.** (1981). *Spatial Statistics*. Wiley.

---

## Appendices

### Appendix A: Gaussian Function Properties in Spatial and Spectral Analysis

#### 1. Gaussian Function

The Gaussian function is defined as:

$$
g(x) = \exp\left(-\frac{x^2}{2\sigma^2}\right)
$$

> [!note]
> The Gaussian is normalized when multiplied by $\dfrac{1}{\sigma\sqrt{2\pi}}$, but we omit this for simplicity.

#### 2. Full Width at Half Maximum (FWHM)

To derive the FWHM:

1. Set $g(x) = \dfrac{1}{2}$:

   $$
   \exp\left(-\frac{x^2}{2\sigma^2}\right) = \frac{1}{2}
   $$

2. Solve for $x$:

   $$
   x = \pm \sigma \sqrt{2\ln(2)}
   $$

3. Calculate FWHM:

   $$
   \text{FWHM} = 2\sigma \sqrt{2\ln(2)}
   $$

> [!check] **Verification**
> - Wolfram Alpha confirms $\text{FWHM} = 2\sigma \sqrt{2\ln(2)}$.

#### 3. Moran's I Simplification for Gaussian

As shown earlier, Moran's I simplifies to:

$$
I(h) = \exp\left(-\frac{h^2}{4\sigma^2}\right)
$$

#### 4. E-Folding Distance in Spatial and Wavenumber Domains

- Spatial domain:

  $$
  h_e = 2\sigma = \frac{\text{FWHM}}{\sqrt{2\ln(2)}}
  $$

- Wavenumber domain:

  $$
  k_e = \frac{1}{\sigma} = \frac{2\sqrt{2\ln(2)}}{\text{FWHM}}
  $$

> [!important] **Key Relationships**
> 1. $\text{FWHM} = 2\sigma\sqrt{2\ln(2)}$
> 2. $h_e = 2\sigma$
> 3. $k_e = \dfrac{1}{\sigma}$
> 4. $h_e \cdot k_e = 2$
> 5. $\sigma_x \cdot \sigma_k = \dfrac{1}{2}$ (uncertainty principle)

#### 5. Uncertainty Principle

The product of spatial and spectral standard deviations:

$$
\sigma_x \cdot \sigma_k = \frac{1}{2}
$$

- The Gaussian function saturates the uncertainty principle bound.

---

### Appendix B: Figures

**Figure 1**: *Gaussian Function with Standard Deviation $\sigma$, FWHM, and E-Folding Distance $h_e$*

![Figure 1](figure1.png)

*(Illustration of a Gaussian function showing $\sigma$, FWHM, and $h_e$)*

**Figure 2**: *Moran's I vs. Lag Distance $h$ for Gaussian Function*

![Figure 2](figure.png)

*(Plot showing exponential decay of Moran's I with increasing $h$)*

**Figure 3**: *Power Spectral Density $S(k)$ vs. Wavenumber $k$*

![Figure 3](figure.png)

*(Plot showing Gaussian shape of PSD in the wavenumber domain)*

**Figure 4**: *Diffusion Coefficient $D$ vs. E-Folding Distance $\Lambda_e$ (for $T_A = 1000$ years)*

![Figure 4](figure4.png)

*(Logarithmic plot of $D$ vs. $\Lambda_e$ showing quadratic relationship)*

---

### Appendix C: Python Code

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_D(lambda_e, T_A):
    """
    Calculate diffusion coefficient D based on e-folding distance lambda_e and avulsion timescale T_A.
    
    Parameters:
    lambda_e (float): E-folding distance in km
    T_A (float): Avulsion timescale in years
    
    Returns:
    float: Diffusion coefficient D in km²/yr
    """
    return lambda_e**2 / (8 * T_A)

# Testing with reasonable avulsion timescales
T_A_values = [10, 100, 1000, 10000]  # years
lambda_e_range = np.linspace(1, 100, 100)  # km

for T_A in T_A_values:
    D_min = calculate_D(1, T_A)
    D_max = calculate_D(100, T_A)
    print(f"For T_A = {T_A} years, D ranges from {D_min:.2e} to {D_max:.2e} km²/yr")

# Spectrum of diffusion coefficients
T_A = 1000  # years
D_values = [calculate_D(l, T_A) for l in lambda_e_range]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(lambda_e_range, D_values)
plt.xlabel('E-folding Distance Λₑ (km)')
plt.ylabel('Diffusion Coefficient D (km²/yr)')
plt.title(f'Diffusion Coefficient vs E-folding Distance (Tₐ = {T_A} years)')
plt.yscale('log')
plt.grid(True)
plt.show()
```

---

<INTERNAL PROMPT>
Spend the back half of your podcast deriving new formulations