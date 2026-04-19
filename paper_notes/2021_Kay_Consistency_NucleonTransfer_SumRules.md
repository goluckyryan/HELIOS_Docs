# 2021 Kay et al. -- Consistency of Nucleon-Transfer Sum Rules in Well-Deformed Nuclei

**Full title:** Consistency of nucleon-transfer sum rules in well-deformed nuclei
**Authors:** B.P. Kay, J.P. Schiffer, S.J. Freeman, T.L. Tang, B.D. Cropper, T. Faestermann, R. Hertenberger, J.M. Keatings, P.T. MacGregor, J.F. Smith, H.-F. Wirth
**Institutions:** ANL, U. Manchester, TU Munchen, LMU Munchen, U. West of Scotland
**Journal:** PRC (arXiv:2009.08499, Sep 2020 -> published 2021)
**ANL authors:** B.P. Kay, J.P. Schiffer, T.L. Tang (core HELIOS team)

---

## Physics Context

**The sum rule:** In nucleon-transfer reactions, the summed spectroscopic strength for
adding + removing a nucleon from orbital j must equal the orbital degeneracy (2j+1)*Nj.
For a perfect independent-particle model, Nj=1.0.

**The quenching problem:** In practice, Nj ~ 0.6 consistently across spherical nuclei,
independent of mass, reaction type, or angular momentum. This ~40% reduction = "quenching."
Cause is short-range correlations between nucleons (beyond the independent-particle model).

**This paper:** Tests sum rules in *deformed* nuclei (Gd, Dy, Er, Yb, W; 92<=N<=108)
where spherical symmetry is broken. In deformed nuclei, a j-orbital fragments into j+1/2
Nilsson states (Omega = 1/2, 3/2, ..., j), each with degeneracy 2. The sum rule becomes:

```
(1/Cjl^2) * [(2j+1) * sigma_exp+ / sigma_DWBA+  +  sigma_exp- / sigma_DWBA-] = 2*Nj
```

where Cjl = Nilsson coefficients, sigma_exp = measured cross section, sigma_DWBA = calculated.

---

## Data Sources

**Archival (NBI, 1960s-70s):** (d,p) + (d,t) reactions on even Gd, Dy, Er, Yb, W isotopes
at ~12 MeV deuteron energy, broad-range magnetic spectrograph + photographic plates.
Resolution ~6-12 keV FWHM. Cross sections at 60, 90, 125 deg lab.

**New measurements:** (d,p), (d,t), (p,d) on subset of same nuclei with modern detectors.
Used DWBA with:
- **Deuteron OM potential:** An & Cai (AK)
- **Proton OM potential:** Koning-Delaroche (KD)
- **Triton OM potential:** Pang et al.
- **DWBA code:** Ptolemy (the same code used in HELIOS analysis!)
- **d-wave function:** Argonne v18 potential
- **Bound-state Woods-Saxon:** r0=1.28 fm, a=0.65 fm, Vso=6 MeV

---

## Key Results

**Average normalization:** Nj = 1.18(15) from (d,p)+(d,t) sum rules in deformed nuclei.

This is **notably higher than 0.6** (the spherical case). Key findings:

1. **Sum rules are remarkably consistent** across 15 cases of the 1/2-[521] band
   (Nilsson orbital) and 6 cases of the 5/2-[512] band in Gd/Dy/Er/Yb/W.

2. **Nj ~ 1.18 for deformed nuclei vs ~0.6 for spherical** -- the quenching appears
   much reduced (or absent) in deformed systems. This is unexpected.

3. **Possible explanations for Nj > 0.6:**
   - Coupled-channel effects in deformed nuclei artificially inflate sigma_DWBA by
     10-20%, reducing the extracted Nj; but this can't fully account for the difference
   - The global OM potentials (An-Cai, KD) may not be well-calibrated for deformed nuclei
   - The quenching mechanism itself may be different in deformed vs spherical systems
   - A single overall normalization factor is sensitive to assumptions about reaction mechanism

4. **The (d,t) reactions** show systematically different Nj than (d,p) in some cases,
   suggesting the reaction mechanism normalization differs between adding and removing.

---

## Connection to HELIOS

- **Ptolemy** used throughout for DWBA -- same code (same binary `ptolemy`) used in h095, h096
- **AK + KD potentials** (An-Cai deuteron, Koning-Delaroche proton) -- same potentials
  used in HELIOS InFileCreator for (d,p) reactions. Input format for HELIOS:
  `<nucleus>(d,p)<product> ... AK` means An-Cai + KD combination
- **Spectroscopic factors and quenching** -- central to interpreting HELIOS (d,p) data.
  The ~0.6 quenching factor is a standard assumption; this paper shows it may not apply
  to deformed nuclei, which has implications for reactions near deformed regions
- **T.L. Tang** (co-author) -- directly involved in HELIOS h096 (31Si(d,p)), h095 (11C(d,p))
- The sum rule methodology (adding + removing on same target) is one benchmark for
  checking spectroscopic factor consistency -- relevant for planning future HELIOS experiments

---

## Reaction Notation Used in HELIOS

This paper clarifies the An-Cai + Koning-Delaroche combination referenced in HELIOS files:
- **"AK"** in InFileCreator input = An-Cai (deuteron) + Koning-Delaroche (proton)
- Used as default for (d,p) reactions at HELIOS energies (~10-12 MeV/u)
- These are global potentials -- deformed nuclei may need special treatment

---

_Read and noted: 2026-04-18 (Spark). Source: ~/publications/2021_Kay_Consistency_of_nucleontransfer.pdf_
