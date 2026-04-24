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

## Assumptions

1. **Collective (deformed rotor) model assumed valid throughout.** The inelastic cross section is calculated with DWBA using a collective form factor (deformation parameter βd). The shape of the angular distribution is fit to extract δd. This assumes the nucleus deforms coherently -- valid for well-deformed nuclei, but questionable for a halo system like ¹⁵C where one loosely-bound 2s₁/₂ neutron dominates.

2. **Optical model potential (OMP) dependence.** Five global OPs were tested for elastic scattering (An, Han, Daehnick, Schiffer, DA1p). DA1p gave the best fit -- it was derived specifically for 1p-shell nuclei. The same OMP is then used for inelastic. The OP uncertainty propagates into βd (they estimate ~25% sensitivity at forward angles, larger at back angles).

3. **bn/bp = 1 for deuterons (isoscalar probe).** This is a standard assumption used to relate δd to Mn/Mp via Bernstein 1981. It is well-established that deuterons are isoscalar, but the underlying bn/bp for nucleons (needed to separate neutron/proton deformation lengths) is still model-dependent.

4. **Inert ¹⁴C core assumed.** The analysis uses Mp′ ≈ 0 (proton valence contribution negligible), which requires the ¹⁴C core to be truly inert. Shell model (YSOX) supports this (Mp′ = 0.44 fm² vs Mn′ = 5.19 fm²), but it is an assumption.

5. **B(E2) taken from lifetime measurement (Alburger & Millener 1979).** Mp is extracted from B(E2), not measured directly in this experiment. If that B(E2) is wrong, Mp and hence Mn/Mp shift.

6. **Coupled channels only partially addressed.** Standard DWBA (one-step) is used. Coupled channel (CC) calculation was also done -- the CC result for δd agrees within uncertainty (βd = 0.35(4) vs 0.29(3)), but the paper notes that at large angles, continuum coupling, 3-body, and 4-body effects may not be captured. The angular range where OP sensitivity is acceptable is ~25–45° CM.

---

## Further Questions

- **Would a microscopic DWBA (using shell-model transition density) fit the angular distribution equally well?** The paper only uses a collective form factor. A microscopic calculation might give a different shape -- or be indistinguishable at this angular coverage. If distinguishable, which is preferred?

- **Is the collective model self-consistent for a halo nucleus?** The 2s₁/₂ halo neutron is spatially extended and not deforming the core in the usual rotor sense. The Mn/Mp framework assumes coherent deformation -- does that picture apply here, or is it just a convenient parametrization?

- **What does the data constrain at large angles?** The OP calculations fail at back angles (core excitation, continuum, 3-body effects). Is there information content there, or is it all contamination?

- **How sensitive is Mn/Mp to the B(E2) input?** Mp is taken from Alburger 1979. A newer or more precise B(E2) would shift the result -- is the present Mn/Mp limited by the nuclear structure input or the scattering measurement?

- **Would ¹⁹C or ¹¹Li (larger halo, larger matter radius) show a stronger core decoupling in Mn/Mp?** The paper suggests studying these as future work. If Mn/Mp/(N/Z) increases with matter radius, that would be a clean halo signature.

- **Is the NCCI convergence of Mn/Mp robust?** The B(E2) is NOT well converged in the NCCI calculation (factor ~2 off from experiment), but Mn/Mp appears converged. Is that physically meaningful or a cancellation of errors?

---

## Related Papers

**Same 15C beam / ANL program:**
- **Kay 2022** (PRC) -- 15C(d,p) neutron adding, spectroscopic factors -- same ATLAS beam
- **Jiang 2025** (PLB) -- 15C(p,d)+(d,t) quenching, Rs~0.64 -- closes the 15C picture with removal
- Together these three form a complete structural picture of 15C via transfer + inelastic

**Mn/Mp framework & theory:**
- **Bernstein, Brown & Madsen 1983** (Comments Nucl. Part. Phys.) -- original Mn/Mp formalism used throughout this paper [Ref 13]
- **Bernstein, Brown & Madsen 1979** (PRL) -- 17O Mn/Mp measurement [Ref 19] -- the key comparison nucleus

**Other nuclei measured with same method:**
- **Elekes et al. 2009** (PRC) -- 20O Mn/Mp via (d,d') -- same analysis chain [Ref 20]
- **Wiedeking et al. 2008** (PRL) -- 16C B(E2) remeasurement, revised Mn/Mp = 1.4x(N/Z) [Ref 25] -- shows how earlier measurements can be wrong

**Halo structure context:**
- **Tanihata et al. 1985** (PRL) -- original halo discovery via interaction cross sections [Ref 1]
- Any (p,p') or (d,d') measurement on 19C, 22C, 11Li -- would test whether larger halo -> stronger Mn/Mp enhancement

**Ab initio:**
- **Daejeon16 interaction** (Maris et al.) -- used for NCCI in this paper; fits p-shell but not yet sd-shell; future improvement needed for 15C excited state energy and B(E2)

---

_Read and noted: 2026-04-18 (Spark). Updated: 2026-04-23 (full re-read + assumptions/questions/related papers added). Source: ~/publications/2022_Chen_Probing_the_quadrupole_transit.pdf_
