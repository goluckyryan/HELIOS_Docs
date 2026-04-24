# ZR-DWBA Mathematical Reference

**Source:** `~/PtolemyGUI/Raphael/ZR_DWBA_Mathematics.md`
**Code:** `~/PtolemyGUI/Raphael/dwba_zr.py` (Python ZR-DWBA implementation)
**Author:** Ryan (Tsz Leung) Tang (PtolemyGUI project)

This is a Python implementation of Zero-Range DWBA -- educational/prototyping code
complementary to the Fortran `ptolemy` binary used in production HELIOS analysis.

---

## Physics Summary

### What ZR-DWBA Calculates

Differential cross section d(sigma)/d(Omega) for single-nucleon transfer A(a,b)B:
```
d(sigma)/d(Omega) = (mu_I * mu_O)/(2*pi*hbar^4) * (k_O/k_I^3) * S * sum|T_fi|^2
```

**Key inputs:**
- Spectroscopic factor S (= C^2S, the single-particle strength)
- Bound state wave function u_nlj(r) of transferred nucleon (Woods-Saxon potential)
- Incoming distorted wave chi_a^(+): solved with incoming OM potential
- Outgoing distorted wave chi_b^(-): solved with outgoing OM potential

**Zero-range approximation:** Interaction = D_0 * delta(r_a - r_x) * delta(r_b - r_x)
- D_0 = 1.55e4 MeV*fm^3 for (d,p)
- Simplifies 3D integral to 1D radial integral x angular coupling

### The Radial Integral (core computation)

```
I(L1,J1,L2,J2) = int_0^inf u_nlj(r) * u_L1J1^in(r) * u_L2J2^out(r) * exp(i*phases) dr
```

**[!!] Critical detail: mass rescaling**
For (d,p): incoming has larger reduced mass than outgoing. Must rescale radial mesh:
- rpos_out = rpos_in * massFactor (where massFactor = sqrt(mu_in/mu_out))
- Without this: incorrect overlap integral -> wrong angular distribution shape

### Angular Coupling: The Gamma Function

Contains:
- One Wigner 9j-symbol: {j,l,s; J1,L1,s_a; J2,L2,s_b}
- Four Clebsch-Gordan coefficients
- Phase factors: (-1)^m * i^(L1-L2-l)
- Selection rule: L1 + L2 + l must be EVEN (parity conservation)

The differential cross section is obtained by:
1. For each angle theta: compute Beta(m, ma, mb) for all valid (L1,J1,L2,J2)
2. Sum |Beta|^2 over all (m, ma, mb)
3. Multiply by scaling factor (masses, wave numbers, spin factor)
4. Convert fm^2 -> mb (x10)

---

## Key Physical Constants

| Constant | Value | Units |
|---|---|---|
| D_0 | 1.55e4 | MeV*fm^3 (ZR normalization) |
| hbar*c | 197.326979 | MeV*fm |
| m_n | 939.56539 | MeV/c^2 |
| amu | 931.494 | MeV/c^2 |
| e^2 | 1.43996 | MeV*fm |

---

## Optical Potentials Used

Same as Ptolemy/Cleopatra/InFileCreator:
- **Deuterons:** An-Cai global parametrization
- **Protons:** Koning-Delaroche global parametrization
(This is what "AK" means in InFileCreator input)

Potential form:
```
U(r) = -V*f(r) - iW*f_I(r) - i*4*W_s*(d/dr)f_s(r) - V_SO*(1/r)*(d/dr)f_SO(r)*L*S + V_C(r)
```

---

## Bound State Solution

Woods-Saxon potential with depth V_0 found by iterating until:
1. Correct number of radial nodes (= node quantum number n)
2. Wave function vanishes at large r (bound state condition)

From the asymptotic solution, extracts:
- **ANC (Asymptotic Normalization Coefficient)** = amplitude of Whittaker function tail
- ANC^2 is directly related to the spectroscopic factor C^2S

Radial Schrodinger equation solved by RK4:
```
d^2u/dr^2 + [2*mu/hbar^2 * (E - V(r)) - l(l+1)/r^2] * u = 0
```

---

## Selection Rules (Enforced in Code)

1. **Parity:** L1 + L2 + l must be even
2. **Triangle inequalities:** |J_A - J_B| <= j <= J_A + J_B, etc.
3. **Magnetic:** |m| <= L2
4. **Spin projections:** |m-mb+ma| <= j, |mb-m| <= J2

---

## Performance

- s-wave transfer: ~10 sec per angular distribution
- d-wave transfer: ~30 sec
- Pre-calculations (9j, CG, Legendre): ~0.1-0.5 sec
- Main bottleneck: distorted wave + radial integral calculation

---

## Limitations vs Ptolemy (Production Code)

| Feature | ZR Python | Ptolemy Fortran |
|---|---|---|
| Approximation | Zero-range | Finite-range |
| Speed | ~30 sec | <1 sec |
| Accuracy | Good shape, ~10-20% normalization | Production quality |
| Two-nucleon | Not supported | (p,t),(t,p) via TNA |
| Coupled channels | Not supported | Not supported |
| Use case | Education/prototyping | Production analysis |

**ZR vs FR:** Zero-range is good for angular distribution SHAPES but absolute magnitudes
may differ by 10-20% from finite-range results. For extracting spectroscopic factors,
always use Ptolemy (finite-range) for final results.

---

## Connection to HELIOS Analysis

- Same OM potentials (AK = An-Cai + KD) used in InFileCreator -> Ptolemy pipeline
- Same selection rules enforced in InFileCreator.h (L1+L2+l even parity check)
- The 9j-symbol and CG structure here IS what Ptolemy computes internally
- Understanding this code deeply explains WHY certain angular distributions have their shape
- ANC from bound state connects to: spectroscopic factor, sum rules, occupancies

## Usage (from DWBA.py examples)
```python
from dwba_zr import DWBA_ZR
haha = DWBA_ZR("16O", "d", "p", "17O", "1/2+", "1s1/2", 0.0, 10)  # nucleus, beam, ejectile, residual, J_B, orbital, Ex, EperU
haha.FindBoundState()
haha.CalRadialIntegral()
haha.CalAngDistribution(0, 180, 1)
haha.PlotAngDist()
```

## Elastic Scattering (DistortedWave class)
```python
from distortedWave import DistortedWave
kaka = DistortedWave("148Sm", "a", 50)  # nucleus, projectile, Elab
kaka.AddPotential(WoodsSaxonPot(V_complex, r0, a), False)
kaka.AddPotential(CoulombPotential(r_C), False)
kaka.CalScatteringMatrix()
kaka.CalAngDistribution(180, 0.5, None, False)
kaka.PlotDCSUnpolarized()
```

## Requirements
- numpy, scipy, matplotlib, mpmath (Coulomb waves), sympy (9j-symbols)
- Location: `~/PtolemyGUI/Raphael/`
- NOT used in production analysis -- Ptolemy Fortran binary is faster and more accurate (FR)

_Documented: 2026-04-19 (Spark). Source: ~/PtolemyGUI/Raphael/ZR_DWBA_Mathematics.md_
