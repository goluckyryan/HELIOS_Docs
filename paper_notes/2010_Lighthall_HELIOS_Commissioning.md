# Commissioning of the HELIOS Spectrometer

**Authors:** J.C. Lighthall, B.B. Back, S.I. Baker, S.J. Freeman, H.Y. Lee, B.P. Kay, S.T. Marley,
K.E. Rehm, J.E. Rohrer, J.P. Schiffer, D.V. Shetty, A.W. Vann, J.R. Winkelbauer, A.H. Wuosmaa
**Journal:** Nuclear Instruments and Methods in Physics Research A 622 (2010) 97--106
**DOI:** 10.1016/j.nima.2010.06.220
**Received:** 22 May 2010 | **Accepted:** 16 June 2010
**PDF:** `~/publications/Lighthall2010_HELIOS_Commissioning_NIM_A622.pdf`

---

## Why This Paper Matters

This is the **founding document of HELIOS** -- the first publication describing the instrument,
its physics concept, technical implementation, and proof-of-principle commissioning result.
Everything built on top of HELIOS (all subsequent experiments) traces back to this paper.

---

## The HELIOS Concept

HELIOS solves a fundamental problem in inverse kinematics transfer reactions:
**kinematic compression** -- excited states that are well-separated in the CM frame get
compressed together in the lab frame at backward angles, making them hard to resolve.

Key insight: in a uniform solenoidal magnetic field B, all emitted light ions (e.g. protons)
of a given mass/charge return to the solenoid axis after exactly one cyclotron period:

```
T_cyc = (2pi/B)(m/qe)
```

This fixes the time-of-flight regardless of emission angle. The return position z along the
axis then has a **linear relationship** to both lab energy E_lab and CM energy E_cm:

```
E_lab = E_cm - (1/2)mV_cm^2 + mV_cm * (z / T_cyc)
```

This means: at fixed z, the separation between excited states in the lab equals the CM separation.
**Kinematic compression is eliminated.** The angle measurement becomes a position measurement.

Additionally, T_cyc = (2pi/B)(m/q) gives mass-to-charge ratio directly from time of flight --
solving the light-ion particle identification problem at low energies.

---

## The Solenoid

- Repurposed MRI superconducting magnet (decommissioned)
- Bore: 92 cm inner diameter, 235 cm length
- Maximum central field: **2.86 T** (operated at 2.0 T for commissioning)
- Field homogeneity: < 0.05% deviation within 90 cm diameter sphere at center
- Field deviation < 3% within cylindrical region z < +/-50 cm, r < 40 cm
- Axial field drops to 10% of central value at z ~ +/-150 cm from center
- Ends sealed with aluminum flanges (vacuum vessel); feedthroughs for signals, cooling

---

## The Silicon Detector Array

- 24 position-sensitive silicon detectors (PSDs) on a 16 mm square aluminum rod
- 6 detectors per side, 4 sides
- Active area per detector: 9 mm x 50.5 mm, thickness 700 um
- Position sensitivity via resistive charge division
- Position resolution: ~0.5 mm FWHM at 5 MeV protons, ~1.2 mm FWHM at 2 MeV
- Energy resolution: 25--55 keV FWHM (detector-dependent)
- Detector radius r_0 = 11.4 mm from solenoid axis
- Separation between detectors: 2.4 mm

Note: the non-zero detector radius causes a correction to the return distance z (the "knee"
feature in z vs. E_lab plots at shallow angles). For most orbits where orbit radius r >> r_0,
the correction is negligible. The approximate correction for shallow orbits:
```
z ~ z_0 - r_0 / tan(theta_lab)
```

---

## Commissioning Reaction: d(28Si, p)29Si

- **Reaction:** 28Si beam on CD2 target, detecting protons (inverse kinematics)
- **Beam energy:** 6 MeV/u (168 MeV total)
- **B-field:** 2.0 T
- **Purpose:** Proof of principle -- verify linear z vs. E relationship, demonstrate resolution

Results confirmed:
- Linear relationship between z and E_lab (and E_cm) as predicted by theory
- Excited states in 29Si cleanly resolved
- Particle identification via cyclotron period T_cyc demonstrated
- Position resolution adequate for nuclear spectroscopy

---

## Key Equations

**Return distance (finite detector radius):**
```
z = (v_0 cos(theta_cm) + V_cm) * [r_p^2 - 2*arcsin(r_0 / 2r)] / (v_0 sin(theta_cm))
```
where v_0 = CM velocity, V_cm = CM velocity in lab, r_0 = detector radius, r = cyclotron orbit radius

**Linear E_lab vs z (idealized):**
```
E_lab = E_cm - (1/2)mV_cm^2 + mV_cm * (z / T_cyc)
```

**Cyclotron period:**
```
T_cyc = (2pi/B)(m/qe)    [gives m/q from TOF]
```

---

## Connections to Current HELIOS

- The solenoid described here **is our solenoid** -- same magnet, now operated up to 2.85 T
- The prototype Si array (24 PSDs on square rod) has since been replaced/upgraded
- RDT (recoil detector telescope) was not used in commissioning but referenced as future work --
  now standard in HELIOS experiments
- The ATLAS accelerator facility at ANL remains the beam source

---

## Notes

- This paper is the standard reference to cite when describing the HELIOS spectrometer
- Theory basis (the HELIOS concept) originally proposed in refs [3--5] within this paper;
  the key theory paper is Wuosmaa et al. (ref [5])
- Subsequent HELIOS papers build on this foundation -- see `~/publications/HELIOS_Publications_Summary.md`

---

_Notes written: 2026-04-17 by HELIOS AI_
