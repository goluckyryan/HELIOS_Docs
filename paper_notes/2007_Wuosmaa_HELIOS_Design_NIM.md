# Paper Notes: Wuosmaa et al. 2007 -- HELIOS Design Paper (NIM)

**Citation:** A.H. Wuosmaa, J.P. Schiffer, B.B. Back, C.J. Lister, K.E. Rehm, NIM A 580, 1290 (2007)
**DOI:** 10.1016/j.nima.2007.07.029
**PDF:** `~/publications/2007_Wuosmaa_HELIOS_Design_NIM.pdf`
**Read:** 2026-04-28 (full PDF)

---

## Summary

The original design paper proposing and describing the solenoidal spectrometer concept that became HELIOS. Describes the physics motivation, charged-particle transport theory, and performance simulations for reactions in inverse kinematics.

---

## Physics Motivation

Inverse kinematics with radioactive beams creates fundamental problems for conventional Si arrays:
- Light particle energies are very low and hard to measure
- Identification at low energies is technically difficult
- Energy varies rapidly with emission angle → poor c.m. resolution and/or multi-valued kinematics
- Significant backgrounds from beam scattering, radioactive decay products, competing reactions

The solenoid approach solves all of these simultaneously.

---

## Core Concept

A large-bore solenoid (B ~ 2–5 T) aligned with the beam axis:
- Charged particles emitted from the target follow helical trajectories
- After one full cyclotron orbit, ALL particles return to the solenoid axis
- Detected by a hollow Si array placed on-axis upstream of the target

### Key Equations

**Cyclotron period (particle ID):**
```
T_cyc = 2π m / (q e B)    [independent of energy and angle]
T_cyc (ns) = 65.6 × A / (q × B[T])
```
- For protons at 3T: T_cyc = 21.9 ns
- d and α²⁺ are degenerate at 43.7 ns; t at 65.6 ns; ³He²⁺ at 32.8 ns
- TOF measurement → mass/charge → particle ID

**Center-of-mass energy from (E_lab, z):**
```
E_cm = E_lab + (m/2)V²_cm - mV_cm × z/T_cyc
```
- E_lab and z measured; T_cyc known from B-field and particle ID
- No kinematic shift correction needed -- z encodes the angle cleanly
- Energy separation between states = excitation energy difference (not kinematically compressed)

**Center-of-mass angle:**
```
cos θ_cm = (v²_lab - V²_cm - v²_0) / (2 v_0 V_cm)
```

### Advantage Over Conventional Arrays

At a fixed lab angle, proton energies from different excited states overlap badly (kinematic compression). At a fixed z (in HELIOS), the energy separation equals the excitation energy difference directly. This is why HELIOS achieves ~100 keV resolution where conventional arrays at comparable kinematics achieve ~300-500 keV.

---

## Simulated Example: d(¹³²Sn,p)¹³³Sn at 8 MeV/u

- Proton trajectories at 110°, 135°, 160° c.m. shown
- Energy vs z plane shows clean, parallel kinematic lines for different states
- Projected spectrum at fixed z shows peaks separated by excitation energy differences
- Compared to conventional energy vs angle: much cleaner separation

---

## Cyclotron Periods (B=3T)

| Particle | T_cyc (ns) |
|----------|-----------|
| p | 21.9 |
| d, α²⁺ | 43.7 |
| t | 65.6 |
| ³He²⁺ | 32.8 |

These differ by tens of ns -- easily distinguished with ~1-2 ns time resolution.

---

## Geometric Acceptance

- All particles with orbits smaller than the solenoid radius are collected
- Full 2π azimuthal acceptance automatically
- With arrays upstream AND downstream of target: approach ~4π solid angle
- Recoiling heavy ions have small perpendicular momentum → exit downstream → detected in heavy-ion array

---

## Significance

- **THE foundational HELIOS design paper** -- everything else references this
- Wuosmaa (Western Michigan), Schiffer, Back, Lister, Rehm (ANL)
- Concept was presented at workshops/conferences before this publication
- Demonstrated in first experiment: Back 2010 (¹²B(d,p)¹³B), Wuosmaa 2010 (¹⁵C(d,p)¹⁶C)
- Commissioning details: Lighthall 2010 NIM A622

---

_Created: 2026-04-28_
