# 2023 Bennett et al. -- Direct Determination of Fission-Barrier Heights via Transfer in Inverse Kinematics

**Full title:** Direct Determination of Fission-Barrier Heights Using Light-Ion Transfer in Inverse Kinematics
**Authors:** S.A. Bennett, K. Garrett, D.K. Sharp, S.J. Freeman, A.G. Smith, T.J. Wright, B.P. Kay, T.L. Tang, I.A. Tolstukhin, Y. Ayyad, J. Chen, P.J. Davies, A. Dolan, L.P. Gaffney, A. Heinz, C.R. Hoffman, C. Muller-Gatermann, R.D. Page, G.L. Wilson
**Institutions:** U. Manchester/CERN, ANL, IGFAE, U. York, U. Liverpool, Chalmers, LSU
**Journal:** PRL (arXiv:2304.10281, Apr 2023)
**ANL authors:** B.P. Kay, T.L. Tang, I.A. Tolstukhin, J. Chen, C.R. Hoffman, C. Muller-Gatermann, G.L. Wilson
**Experiment:** HELIOS at ATLAS/ANL -- novel fission application

---

## Physics Motivation

**Fission data for r-process:** Fission barrier heights, mass/charge yields are crucial inputs
for r-process nucleosynthesis calculations. But most r-process actinides are short-lived --
no fixed targets possible. Fission recycling sets the upper mass limit in r-process and
channels mass to lower-Z nuclei. Recent neutron-star merger observations (kilonovae) suggest
fission is significant -- e.g. 90Sr observed in merger remnants.

**The technique:** (d,pf) in inverse kinematics. Deuteron target + actinide beam:
- Neutron from deuteron transfers to actinide nucleus
- Excites it to near or above the fission barrier
- (d,p) part measured with HELIOS; fission fragments detected separately
- (d,p) acts as a proxy for neutron-induced fission: same compound nucleus formed

**Key equation:** sigma_f^A = sigma_CN^(A+1) * P_f^(A+1)
where (d,p) determines the excitation energy and sigma_CN, fission detectors give P_f.

---

## Experiment -- Novel HELIOS Configuration

**Beam:** 238U at 8.6 MeV/u from ATLAS
**Target:** CD2 (deuterated polyethylene), 228Th alpha calibration
**B field:** 2.5 T

**HELIOS setup (modified for fission):**
- Si array: 350 mm long, end 55 mm upstream of target (detects protons from (d,p))
  - Coverage: Ex ~ 7 MeV, theta_CM ~ 10-30 deg
  - Four-sided array surrounding beam axis (not the standard PSD strips)
- Annular Si: downstream, detects elastically scattered deuterons for absolute normalization
  (theta_CM = 29-29.3 deg -- very narrow range, Rutherford for normalization)
- Faraday cup: downstream for beam current

**Fission detection (downstream, ~1 m from target):**
- Al charge-reset foil 70 mm downstream (minimizes charge state spread in MWPC)
- 4 fission arms: 2 at 15 deg (light fragments) + 2 at 10 deg (heavy fragments)
- Each arm: MWPC (position) + Bragg detector (energy loss/ID)
- In inverse kinematics: fission fragments strongly forward-peaked in lab
  (~15 deg and ~10 deg for light/heavy at 8.6 MeV/u)

**Background:** Carbon target used to subtract multinucleon transfer on C in CD2 target.

---

## Key Results

**239U fission barrier determined** via 238U(d,pf) in inverse kinematics:
- First direct measurement of a fission-barrier height using light-ion transfer in inverse kinematics
- Results consistent with existing neutron-induced fission data for 239U
- **Validates the technique** for future application to exotic actinide beams

**Demonstrator:** 238U is stable -- chosen as proof-of-principle because neutron-induced data exists.
Now technique is validated for exotic beams (238U was just the test case).

---

## Broader Significance

**Three solenoidal spectrometers now exist:**
- HELIOS (ANL) -- this experiment
- ISOLDE Solenoidal Spectrometer (CERN/ISS)
- SOLARIS (FRIB)

All can in principle apply this technique to exotic actinide beams -- opens r-process
fission barrier measurements across wide range of neutron-rich nuclei.

**Future targets:** Neutron-rich actinides from ReA at FRIB, LISA project at ISOLDE.

---

## Connection to HELIOS

- **Direct HELIOS experiment** -- but very different from standard transfer reactions
- **Novel configuration:** Four-sided Si array (not standard PSD strips); fission detectors
  downstream; charge-reset foil; MWPC Bragg detectors
- **Demonstrates HELIOS versatility:** Transfer (standard), inelastic (Chen 2022),
  fission (this work) -- spectrometer applicable to diverse reaction types
- **Same team:** Kay, Tang, Tolstukhin, Hoffman, Chen, Muller-Gatermann -- HELIOS regulars
- **Astrophysical motivation:** r-process fission connects to h096 (31Si) in the sense that
  understanding the full nuclear chart requires both the light (HELIOS transfer) and
  heavy (fission barrier) ends of the mass distribution
- **Technique validation:** The (d,p) surrogate approach for neutron-induced fission is
  a major methodological advance -- HELIOS played the key role

---

_Read and noted: 2026-04-18 (Spark). Source: ~/publications/2023_Bennett_Direct_Determination_of_Fissio.pdf_
