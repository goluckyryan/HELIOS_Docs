# 2025 Jiang et al. -- Quenching of Single-Particle Strength in 15C Transfer Reactions

**Full title:** Quenching of single-particle strength inferred from nucleon-removal transfer reactions on 15C
**Authors:** Y.C. Jiang, J. Chen, B.P. Kay, C.R. Hoffman, T.L. Tang, I.A. Tolstukhin, M.R. Xie, J.G. Li, N. Michel, M.L. Avila, Y. Ayyad, D. Bazin, S. Bennett, J.A. Clark, S.J. Freeman, H. Jayatissa, G. Li, W.P. Liu, J.L. Lou, A. Munoz-Ramos, C. Muller-Gatermann, T. Nathan, D. Santiago-Gonzalez, D.K. Sharp, Y.P. Shen, A.H. Wuosmaa, C.X. Yuan
**Institutions:** ANL, SUSTech, CIAE, IMP/CAS, IGFAE, FRIB/MSU, U. Manchester, CERN, Peking U., U. Connecticut, Sun Yat-Sen U.
**Journal:** Physics Letters B (arXiv:2506.03685, Aug 2025)
**ANL authors:** J. Chen, B.P. Kay, C.R. Hoffman, T.L. Tang, I.A. Tolstukhin, M.L. Avila, J.A. Clark, D. Santiago-Gonzalez, C. Muller-Gatermann
**Experiment:** HELIOS at ATLAS/ANL

---

## The Quenching Puzzle

The "quenching factor" Rs = sigma_exp / sigma_DWBA measures how much single-particle strength
is reduced compared to the independent-particle model prediction.

**Known facts (stable nuclei):**
- Rs ~ 0.6 universally from (e,e'p), transfer reactions, (p,2p) reactions
- Independent of mass, orbital, orbital angular momentum

**The controversy (exotic nuclei):**
Heavy-ion (HI) induced knockout reactions show a STRONG dependence of Rs on Delta_S:
```
Delta_S = Sp - Sn   (proton vs neutron separation energy difference)
```
- Delta_S ~ 0 (symmetric): Rs ~ 0.6
- Delta_S ~ -20 MeV (neutron-rich halo): Rs ~ 0.9-1.0 (HI knockout barely quenches!)
- Delta_S ~ +20 MeV (proton-rich): Rs ~ 0.2 (HI knockout hugely quenched)

But (p,2p) and transfer reactions do NOT show this strong dependence -- Rs stays ~0.6.
This is the "quenching asymmetry dependence puzzle" -- different probes give different answers.

---

## 15C: The Most Extreme Test Case

15C = 14C core + valence neutron in 2s1/2
- Delta_S = -19.86 MeV (extremely neutron-rich, most extreme value reached by transfer)
- Shell model: SF ~ 1.0 (almost pure single-particle state)
- HI knockout (Terry 2004, revised Lee 2006): Rs = 0.96(4) -- barely quenched
- Previous transfer 14C(d,p)15C (Kay 2022): Rs = 0.64(15) -- standard quenching!
  Factor ~1.5 discrepancy between HI knockout and transfer

**This paper:** Does the discrepancy persist for REMOVAL reactions (15C(p,d) and 15C(d,t))?
Removal has the same reaction direction as HI knockout -- if mechanism matters, removal might
give different Rs than adding.

---

## Experiment at HELIOS

**Beam:** 15C secondary beam at 7.1 MeV/u from ATLAS in-flight (RAISOR)
- Produced via 14C(d,p)15C at 8 MeV/u, 200 pnA primary
- ~10^6 pps, <1% contamination

**Targets:** (CD2)n at 363 µg/cm2 for (d,t); (CH2)n at 387 µg/cm2 for (p,d)

**HELIOS setup:** B = 2.5 T
- Silicon array: 24 PSDs, z = 332-702 mm (downstream of target)
- RDT: 4 x ΔE-E telescopes, ~62 mm upstream of silicon array
- Cylindrical plastic blocker around RDT to block multi-loop particles
- Coincidence time between silicon and RDT for particle ID

**Two reactions measured:**
- 15C(p,d)14C -- neutron removal, l=0, 2s1/2
- 15C(d,t)14C -- neutron removal, l=0, 2s1/2

---

## Key Results

**Rs from this work:**
- 15C(p,d)14C: Rs consistent with ~0.64
- 15C(d,t)14C: Rs consistent with ~0.64
- Both consistent with each other and with the adding reaction Kay 2022

**Main conclusion:** The quenching factor from transfer reactions (both adding AND removing)
is Rs ~ 0.64 -- standard transfer value, independent of reaction direction.

This **contradicts** the HI knockout value of Rs = 0.96.

**Implication:** The strong Delta_S dependence of Rs seen in HI knockout is:
- NOT present in transfer reactions (adding or removing)
- NOT an artifact of reaction direction
- Specific to the HI knockout reaction mechanism

Transfer reactions give consistent, physics-based quenching independent of Delta_S.
HI knockout may have systematic issues (core excitation, reaction model limitations) at extreme Delta_S.

---

## Physics Significance

- Most extreme Delta_S (-19.86 MeV) ever reached by transfer reactions
- First simultaneous adding AND removing comparison at such extreme Delta_S
- Strongly supports: quenching (Rs~0.6) is an intrinsic nuclear property, not reaction-dependent
- Challenges the HI knockout asymmetry-dependence interpretation
- Connects to Kay 2021 (sum rules in deformed nuclei) -- both papers probe nuclear correlations

---

## Connection to HELIOS Program

- **Directly at HELIOS** -- this is a HELIOS result using the standard setup
- B = 2.5 T (compare h096: B = 2.85 T), same 24-PSD array configuration
- **RDT blocker** -- cylindrical plastic blocker around RDTs (relevant for future setups)
- **RAISOR** -- in-flight secondary beam production, connected to Hoffman 2022 (16N isomer paper)
- **15C + HELIOS** = inverse kinematics transfer at its best; exotic beam + solenoidal spectrometer
- Authors include the core HELIOS team (Kay, Tang, Hoffman, Avila, Clark, Tolstukhin)
- Most recent HELIOS publication in the library (2025)

---

_Read and noted: 2026-04-18 (Spark). Source: ~/publications/2025_Jiang_Quenching_of_singleparticle_st.pdf_
