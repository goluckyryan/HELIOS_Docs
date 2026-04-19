# 2022 Hoffman — In-flight production of an isomeric beam of 16N

**Citation:** C.R. Hoffman, T.L. Tang, M. Avila, et al., NIM A (2022), arXiv:2202.01981
**File:** `~/publications/2022_Hoffman_Inflight_production_of_an.pdf`

## Key Results

- Produced 16N beam via 15N(d,p)16N in inverse kinematics at the upgraded ATLAS in-flight system
- Measured isomer fraction (0- state at 120 keV, T1/2 ~ 5 us):
  - **40(5)%** at 7.9(3) MeV/u
  - **24(2)%** at 13.2(2) MeV/u
- Measurement done ~30 m downstream of production target using Al stopping foil + HPGe Clover detector

## Physics

- 16N has 4 bound states: g.s. (2-), 0.120 MeV (0-, isomer), 0.298 MeV (3-), 0.397 MeV (1-)
- Ground state (2-) and 3- state populated via l=2 neutron transfer
- Isomer (0-) and 1- state populated via l=0 neutron transfer
- Different l values give different angular distributions -> angular acceptance controls isomer fraction
- DWBA calculations (Ptolemy) used to estimate relative yields with two OMP parameter sets
- Key finding: Theta_cm^max ~ 10 deg reproduced experimental station data, but RAISOR focal plane consistent with larger acceptance

## ATLAS In-Flight System & RAISOR Hardware

- Primary beam: 15N from ATLAS linac, up to 150 pnA, at 8.1 and 13.5 MeV/u
- Production target: cryogenically-cooled D2 gas cell (90 K, 1400 mbar, HAVAR windows 1.9 mg/cm2)
  - 6-T solenoid focuses primary beam onto gas cell
  - Also supports self-supported solid foil targets
- **RAISOR** (magnetic achromat separator): 4 dipoles + bookend quadrupole doublets (symmetric chicane)
  - Max dipole field: 1.75 T | Max quadrupole field: 1 T
  - Angular acceptance: 75 mrad (15 cm inner beamline at first quad)
  - Energy acceptance: delta_E/E up to 10%
  - Energy dispersion at midplane: 1.3 mm/%, magnification 0.6, 30 cm off-axis displacement
  - Ion flight path: ~7 m | Production target to focal plane: 6.6 m (linear)
  - Adjustable water-cooled slits at midplane: Brho selection + primary beam stopping
  - Optimal secondary beam: delta_Brho = +2.5% above reference from degraded primary beam
  - Momentum acceptance: delta_P/P ~2% (midplane slit spacing ~5 mm)
- Downstream of focal plane: 2 superconducting RF resonators + RF Sweeper (half-frequency transverse E field);
  NOT used in this experiment -- RAISOR slits alone gave >50% purity
- Si dE-E telescopes at focal plane and experimental station for beam ID and rate monitoring
- Largest beam contaminant: 15N6+ (analogous to 30Si14+ issue in h096)

## [!!] Gas Cell Heating -- Beam Intensity Limit

The gas cell is cryo-cooled (90 K) specifically to handle higher primary beam currents.
If primary beam power exceeds the cooling capacity:
  D2 gas heats -> density drops -> effective target thickness decreases
  -> secondary beam rate saturates or drops despite more primary current.

This is the physical origin of Calem's warning during h096 (2026-04-18):
  "beam increase does not = more rate for certain (probably 1.4-1.5x instead of x2)"

**Practical rule (h096):** Increase primary beam current incrementally. Watch 31Si rate
at RAISOR focal plane. If rate stops scaling linearly, you've hit the thermal limit -- stop.

## Relevance to HELIOS

- Demonstrates ATLAS in-flight capability for producing exotic/isomeric beams for HELIOS experiments
- Same (d,p) reaction used in many HELIOS experiments
- DWBA approach (Ptolemy) same toolchain as Cleopatra
- Angular acceptance as a degree of freedom for controlling beam composition
- Brho scan method (systematic scan while monitoring dE-E rate) is how optimal secondary beam settings are found
- 30Si14+ contaminant in h096 is directly analogous to 15N6+ here -- same physics
- Co-authors include T.L. Tang (Ryan), B.P. Kay (Ben), and other HELIOS collaborators
- Read in context of h096 beam intensity optimization discussion, 2026-04-18
