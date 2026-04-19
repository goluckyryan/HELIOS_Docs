# 2022 Chen et al. -- Quadrupole Transition Strength of 15C via Deuteron Inelastic Scattering

**Full title:** Probing the quadrupole transition strength of 15C via deuteron inelastic scattering
**Authors:** J. Chen, B.P. Kay, T.L. Tang, I.A. Tolstukhin, C.R. Hoffman, H. Li, P. Yin, X. Zhao, P. Maris, J.P. Vary, G. Li, J.L. Lou, M.L. Avila, Y. Ayyad, S. Bennett, D. Bazin, J.A. Clark, S.J. Freeman, H. Jayatissa, C. Muller-Gatermann, A. Munoz-Ramos, D. Santiago-Gonzalez, D.K. Sharp, A.H. Wuosmaa, C.X. Yuan
**Institutions:** ANL, IMP/CAS, Iowa State, Peking U., IGFAE, U. Manchester/CERN, NSCL/MSU, U. Connecticut, Sun Yat-Sen U.
**Journal:** PRC (arXiv:2209.12252, Nov 2022)
**ANL authors:** J. Chen, B.P. Kay, T.L. Tang, I.A. Tolstukhin, C.R. Hoffman, M.L. Avila, J.A. Clark, H. Jayatissa, C. Muller-Gatermann, D. Santiago-Gonzalez
**Experiment:** HELIOS at ATLAS/ANL (same 15C beam as Jiang 2025)

---

## Physics Context

**15C:** One-neutron halo nucleus. gs = 2s1/2 (halo), Ex=0.74 MeV = 1d5/2 (bound excited state).
**Core:** 14C (inert, N=Z=6, closed p-shell).

**Key observable:** Quadrupole transition from g.s. (1/2+) to first excited state (5/2+).
The ratio Mn/Mp = N*delta_n / (Z*delta_p) measures neutron-proton coupling in the transition:
- Mn/Mp = N/Z = 2.33 for strongly coupled (collective) nuclei
- Mn/Mp >> N/Z indicates valence neutron decoupled from proton core (halo effect)

**Question:** Is the 14C core strongly polarized by the halo neutron, or does the
neutron act independently? Core polarization -> small effective charge -> large Mn/Mp.

---

## Experiment

**Beam:** 15C at 7.1 MeV/u (same ATLAS in-flight production as Jiang 2025)
- 14C primary at 8 MeV/u, 200 pnA -> D2 gas cell -> 15C ~10^6 pps, <1% contamination

**Target:** CD2 363 µg/cm2 (inelastic) + CH2 387 µg/cm2 (background subtraction)

**HELIOS setup:**
- Detects scattered deuterons (both elastic and inelastic)
- Si PSD array upstream of target (for forward-angle recoils)
- Recoil: ionization chamber (IC) downstream -- identifies 15C recoils
- Blockers: cylindrical around target
- B-field not specified in excerpt but standard HELIOS configuration

**Reactions measured:**
1. **15C(d,d)15C elastic:** -> optical model analysis, determine OMP for 15C+d
2. **15C(d,d')15C*** (Ex=0.74 MeV): -> inelastic, extract deformation length delta_d

---

## Key Results

**Matter deformation length:** delta_d = 1.04(11) fm
(From differential cross section of inelastic scattering to Ex=0.74 MeV)

**Mn/Mp = 3.6(4)**
- Compare to N/Z = 14/6 = 2.33 (strongly coupled limit)
- Mn/Mp / (N/Z) = 3.6/2.33 = 1.55 -- moderate enhancement above N/Z
- NOT as extreme as some other neutron-rich nuclei (e.g. 16C had controversial large ratio)
- Consistent with **moderate core decoupling** -- similar to 17O (isotone of 15C)

**Neutron effective charge:** Determined from delta_n/delta_d decomposition
- Small effective charge -- valence neutron weakly polarizes the 14C core
- Core-polarization weaker than in normal (non-halo) nuclei

**ab initio comparison:** No-core configuration interaction (NCCI) calculations compared
- Generally consistent with the measured deformation length and Mn/Mp

---

## Physics Significance

1. **Halo-core decoupling quantified:** 15C shows moderate decoupling (not extreme like some).
   Similar to its isotone 17O (also weakly-bound, 2s1/2 valence neutron).
2. **Consistent picture with 15C (d,p) work** (Kay 2022, Jiang 2025):
   15C is well-described as near-pure single-particle state with minimal core perturbation.
3. **Effective charges in exotic nuclei:** Using inelastic scattering to measure
   quadrupole transition complementary to Coulomb excitation and gamma spectroscopy.

---

## Connection to HELIOS

- **Direct HELIOS experiment** using the same 15C beam as Jiang 2025
- **Same ATLAS in-flight production** -- demonstrates reuse of beam setups for multiple experiments
- **Novel HELIOS use:** HELIOS normally measures transfer reactions; here used for elastic +
  inelastic scattering -- demonstrates versatility of the spectrometer
- **Blocked geometry:** Plastic blockers around target (same as Jiang 2025 setup)
- **IC recoil detector:** Ionization chamber for 15C identification (vs. Si RDT telescopes in transfer)
- Connects to broader 15C program at ANL: Jiang 2025 (quenching via (p,d)+(d,t)) +
  this work (structure via inelastic) + Kay 2022 (adding via (d,p)) = complete picture

---

_Read and noted: 2026-04-18 (Spark). Source: ~/publications/2022_Chen_Probing_the_quadrupole_transit.pdf_
