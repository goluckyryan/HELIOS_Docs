# 2022 Ayyad et al. -- Near-Threshold Resonance in 11B

**Full title:** Evidence of a near-threshold resonance in 11B relevant to the β-delayed proton emission of 11Be
**Authors:** Y. Ayyad, W. Mittig, T. Tang, B. Olaizola, G. Potel, N. Rijal, N. Watwood, et al. (ANL, FRIB/MSU, CERN, LLNL, PSI)
**Journal:** arXiv:2205.04973 (May 2022), PRL
**ANL authors:** B.P. Kay (Physics Division), T. Tang

---

## Physics Context

`11Be` is a classic neutron halo nucleus -- single valence neutron bound by only 501.6 keV. This
makes it a textbook open quantum system, weakly coupled to the continuum.

**The exotic decay in question:** β-delayed proton emission (βp) of 11Be:
```
11Be --> 11B* --> 10Be + p
```
This is counter-intuitive -- β-delayed proton emission in a neutron-rich nucleus. It requires:
1. β-decay to populate 11B*
2. 11B* to have a near-threshold resonance above the proton separation energy (Sp)
3. That resonance to decay by proton emission

The branching ratio (bp ~ 1.3×10⁻⁵) was directly measured in 2019 by the same group (Ayyad et al.,
PRL 123, 082501). This 2022 paper independently confirms the resonance via proton resonance
scattering.

---

## The Controversy

Two conflicting prior experimental results:
- **Ayyad 2019** (pATTPC): bp = 1.3(3)×10⁻⁵ (direct, sequential via resonance)
- **Riisager et al.** (mass separator, multiple attempts): bp < 2.2×10⁻⁶ (upper limit, factor ~6 lower)

The 2019 measurement also connected to **neutron dark decay** searches: if 11Be → 10Be+dark particle
occurs, it mimics the βp signature. A precise bp is needed to disentangle.

---

## This Experiment (2022)

**Reaction:** 10Be(p,p) resonance scattering at ReA3/NSCL
**Beam:** 350 A keV 10Be (~10³ pps), from PSI proton-irradiated carbon
**Target:** 9.6 µm CH2 foil (8.64 mg/cm2)
**Detector:** 1 mm thick 35 mm SSSD (Micron MSD035) ~10 cm downstream
**PID:** Time-of-flight vs energy

**Calibration:** Proton beam at multiple energies + 228Th alpha source (same alpha source as HELIOS!)

---

## Key Result

A narrow resonance was directly observed in 11B at:
- **Ex = 11.4 MeV** (just above proton separation energy, Sp = 11.229 MeV)
- **ER = 196(20) keV** above Sp (consistent with 2019 inference)
- **Jπ = 1/2+**
- **Γp = 4.4 keV** (total proton partial width)

This is the first *direct* observation of this state in 11B. Previously it was only inferred from the βp decay.

**R-matrix analysis** also revealed a sizable α-decay partial width -- the 1/2+ state has:
- Dominant proton channel
- Non-negligible 7Li+α channel
- A nearby 3/2+ resonance at ~11.49 MeV (α-dominant) predicted by theory but not resolved here

---

## Significance

1. **Confirms the βp mechanism**: The sequential two-step decay (β → 11B* → 10Be+p) is validated. The resonance exists.
2. **Open quantum systems physics**: Near-threshold resonances in halo nuclei display generic cluster/correlation behavior -- "doorway states" between bound and continuum.
3. **Dark decay constraint**: With bp confirmed at ~1.3×10⁻⁵, the dark decay rate is bounded more tightly.
4. **Cluster formation**: R-matrix shows both proton and α channels sizable -- the 1/2+ state is not a pure proton resonance but has cluster character.

---

## Theoretical Context

Multiple theory approaches tried to predict/explain the resonance:
| Theory | Result | Status |
|---|---|---|
| Baye & Tursunov (cluster model, no resonance) | bp ~ 5×10⁻⁹ | Ruled out |
| Volya (shell model) | No suitable resonance | Ruled out |
| Okołowicz et al. (SMEC) | Resonance predicted, but bp 40× too small | Partially correct structure |
| Elkamhawy et al. (Halo EFT with resonance) | bp reproduced | Consistent |

The tension between theory predictions of bp and the experiment remains -- the R-matrix α width suggests the
SMEC picture may be getting the decay branching right but missing the resonance character.

---

## Connection to HELIOS

- T. Tang and B.P. Kay are co-authors -- core HELIOS team
- The 228Th alpha source calibration method used here is the same as HELIOS alpha calibration
- The physics (halo nuclei, continuum coupling, near-threshold states) is directly relevant to the science program at HELIOS (e.g. h095: 11C(d,p), which also probes neutron-rich halo-adjacent nuclei)
- Demonstrates the reach of low-intensity exotic beam experiments with good detector calibration

---

_Read and noted: 2026-04-17 (Spark). Source: ~/publications/2022_Ayyad_Evidence_of_a_nearthreshold.pdf_
