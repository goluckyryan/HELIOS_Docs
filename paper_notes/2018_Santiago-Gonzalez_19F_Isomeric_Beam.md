# 2018 Santiago-Gonzalez et al. -- Single-Particle Character of 19F Rotational Band via Isomeric Beam

**Full title:** Probing the single-particle character of rotational states in 19F using a short-lived isomeric beam
**Authors:** D. Santiago-Gonzalez, K. Auranen, M.L. Avila, A.D. Ayangeakaa, B.B. Back, S. Bottoni, M.P. Carpenter, J. Chen, C.M. Deibel, A.A. Hood, C.R. Hoffman, R.V.F. Janssens, C.L. Jiang, B.P. Kay, S.A. Kuvin, A. Lauer, J.P. Schiffer, J. Sethi, R. Talwar, I. Wiedenhover, J. Winkelbauer, S. Zhu
**Institutions:** ANL, LSU, U. Connecticut, U. Maryland, FSU, LANL
**Journal:** PRL (arXiv:1801.02667, Jan 2018)
**ANL authors:** Large ANL contingent -- Kay, Hoffman, Avila, Carpenter, Chen, Janssens, Jiang, Schiffer, Talwar, Zhu, Ayangeakaa, Back, Bottoni, Santiago-Gonzalez
**Experiment:** HELIOS at ATLAS/ANL, B = 2.85 T

---

## Physics Context

**19F: collective-single-particle duality.** 19F is one of the lightest nuclei showing both:
- **Shell model:** 3 valence nucleons outside 16O in sd-shell; max spin = 13/2+ (all aligned 0d5/2)
- **Collective model:** K=1/2 rotational band (prolate deformation), 1/2+ bandhead -> 13/2+ terminator

The band termination at 13/2+ is direct evidence for shell structure -- it's the maximum spin
achievable from 3 sd-shell nucleons. The 13/2+ state is expected to have strong 0d5/2 single-particle character.

**The problem:** To measure the 13/2+ state via (d,p), you need a beam with high enough spin
(J >= 5/2) because angular momentum coupling requires J_beam >= J_final - 1/2.
Normal 18F beam (J=1+) can only reach up to ~5/2+ states.

---

## Key Innovation: Isomeric Beam

**18mF** -- isomeric state of 18F at J=5+ (162 ns half-life)
- Consists of two maximally-aligned 0d5/2 nucleons outside 16O
- Can reach 13/2+ in 19F via (d,p) adding one more 0d5/2 neutron

**Beam composition:** 18F at 14 MeV/u via in-flight technique at ATLAS
- Production: 2H(17O,18F)n at 15 MeV/u, 17O primary at 60 pnA
- At production: 18mF/18gF = 0.56(8)
- At HELIOS station: 18mF/18gF = 0.11(2) (decay during transport)
- Both ground state AND isomer present simultaneously -- measured together

---

## HELIOS Configuration

- B = 2.85 T (same as h096!)
- Target: CD2, 400 µg/cm2, near center of field
- Silicon array: upstream, on-axis, detects protons
- Recoil detector: fast-counting segmented IC, 0 deg, detects 19F recoils
- Coincidence: proton-recoil time difference for event selection
- Coverage: Ex up to ~5 MeV, theta_CM ~ 10-35 deg
- Protons from isomeric reactions appear shifted by -1.07 MeV (Q-value difference: 18mF(d,p) Q=9.328 vs 18gF(d,p) Q=8.259 MeV)

**Note:** This is an early HELIOS paper -- the array was upstream of target (not downstream as in h096/h095). The protons complete a single orbit from target to array.

---

## Key Results

**States in 19F ground-state rotational band (K=1/2):**

| State | Jpi | Populated from | l | SF |
|---|---|---|---|---|
| 1/2+_1 (g.s.) | 1/2+ | 18gF | l=0 | measured |
| 5/2+_1 | 5/2+ | 18gF | l=2 | measured |
| 3/2+_1 | 3/2+ | 18gF | l=2 | measured |
| 7/2+_1 | 7/2+ | 18gF | l=2 | measured |
| 13/2+_1 | 13/2+ | 18mF | l=2 | measured -- single-particle! |

**13/2+ result:** Strong single-particle character confirmed -- spectroscopic factor consistent
with shell-model prediction. The 13/2+ state is dominantly a (0d5/2)^3 configuration.

**Agreement with shell model:** sd-shell interaction calculations reproduce the spectroscopic factors
for all band members, confirming the collective-single-particle duality picture of 19F.

---

## Physics Significance

1. **First measurement of 13/2+ spectroscopic factor** via transfer in a single experiment
2. **Confirms band termination** is a genuinely single-particle phenomenon
3. **Validates isomeric beam technique** for accessing high-spin states via transfer
4. **Single-particle/collective duality** experimentally confirmed in one experiment -- both
   aspects of 19F structure measured simultaneously with the same probe

---

## Connection to HELIOS Program

- **Direct HELIOS result** -- one of the landmark HELIOS papers
- **B = 2.85 T** -- same field as h096 experiment
- **Isomeric beam technique**: pioneered here for HELIOS; relevant to future experiments
  (e.g. 18mF -> 19F) -- connects to Hoffman 2022 (16N isomer beam paper)
- **In-flight production via RAISOR** -- same system used for Jiang 2025 (15C)
- Angular distribution analysis with DWBA: l=0 vs l=2 discrimination at theta_CM=10-35 deg
- **Q-value shift from isomer** (-1.07 MeV) is an important analysis consideration when
  mixed beam (isomer + g.s.) is used -- must separate peaks by Q-value offset

---

_Read and noted: 2026-04-18 (Spark). Source: ~/publications/2018_Santiago-Gonzalez_Probing_the_singleparticle_cha.pdf_
