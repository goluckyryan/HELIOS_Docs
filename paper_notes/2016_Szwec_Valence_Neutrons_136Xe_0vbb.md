# 2016 Szwec et al. -- Rearrangement of Valence Neutrons in 0vββ Decay of 136Xe

**Full title:** Rearrangement of valence neutrons in the neutrinoless double-β decay of 136Xe
**Authors:** S.V. Szwec, B.P. Kay, T.E. Cocolios, J.P. Entwisle, S.J. Freeman, L.P. Gaffney, V. Guimaraes, F. Hammache, P.P. McKee, E. Parr, C. Portail, J.P. Schiffer, N. de Serville, D.K. Sharp, J.F. Smith, I. Stefan
**Institutions:** U. Manchester, ANL, U. West of Scotland, U. Sao Paulo, IPN Orsay
**Journal:** PRC (arXiv:1611.05107, Nov 2016)
**ANL authors:** B.P. Kay, J.P. Schiffer

---

## Physics Motivation

**Neutrinoless double-beta (0vββ) decay:** Process where two neutrons -> two protons with NO neutrinos emitted.
- Would prove lepton number violation and that neutrinos are Majorana fermions
- Rate ~ |M_0v|^2 * m_ββ^2, where M_0v = nuclear matrix element (NME)
- **Problem:** NME calculations from different models disagree by factors 2-3 (order of magnitude in half-life)
- 136Xe is a prime candidate (EXO-200, KamLAND-Zen experiments)
  - Current limit: T1/2 > 1.07e26 y (KamLAND-Zen 2016)
  - Q-value = 2458 keV, natural abundance 8.86%

**Nuclear structure constraint:** NME depends on how neutron occupancies change from 136Xe -> 136Ba.
Measuring these occupancies with transfer reactions provides a direct experimental test of the
nuclear-structure models used to compute NME.

---

## Reactions and Setup

**Facility:** Tandem-Alto at IPN Orsay (two separate experiments)
**Targets:** 134,136Ba (enriched barium oxide, ~50-75 µg/cm2 on carbon backing)

| Reaction | Probes | Energy |
|---|---|---|
| 136Ba(d,p)137Ba | Neutron vacancy (adding) | Ed=15 MeV |
| 136Ba(p,d)135Ba | Neutron occupancy (removing) | Ep=23 MeV |
| 136Ba(α,3He)137Ba | High-j vacancy (l=4,5) | Eα=40.1 MeV |
| 136Ba(3He,α)135Ba | High-j occupancy (l=4,5) | E3He=32 MeV |
| Same on 134Ba | Cross-checks | same |

**Detector:** Enge split-pole spectrometer -- momentum analyze outgoing ions.
Focal plane: position-sensitive gas chamber + ΔE ionization + plastic scintillator.
Resolution: Q-value spectra constructed from position + energy loss.

**Momentum matching strategy:**
- (d,p)/(p,d): best matched for l=0,2 transfer (2s1/2, 1d orbitals)
- (α,3He)/(3He,α): better matched for l=4,5 (0g7/2, 0h11/2 -- high-j orbitals)
Combined dataset gives complete picture of the N=50-82 shell.

---

## Key Physics Results

**Active orbitals** between N=50 and N=82:
0g7/2 (l=4), 1d5/2 (l=2), 2s1/2 (l=0), 1d3/2 (l=2), 0h11/2 (l=5)

**N=82 shell closure:** Confirmed to be a good closed shell in this region -- no negative-parity
(above N=82) strength seen in removal reactions on N=82 isotones. 136Xe neutron configuration
is entirely within the N=50-82 valence space.

**Neutron occupancies extracted for 136Ba:**
The 0vββ decay rearranges neutrons according to changes in these occupancies between 136Xe and 136Ba.
The measured occupancies show **some disagreement** with theoretical calculations (shell model, QRPA, IBM).
- Shell model and QRPA: overestimate some occupancies, underestimate others
- IBM: different pattern of disagreement
- No single model consistently describes all orbitals

**Implication for NME:** The theoretical models that disagree with measured occupancies are the
same ones used to calculate NME. The disagreement in occupancies does NOT resolve the NME
discrepancy but provides a direct experimental constraint that models must satisfy.

---

## Sum Rule Analysis

Macfarlane-French sum rules used throughout:
- Sum of adding + removing strength = (2j+1) * Nj
- Nj ~ 0.6 for spherical nuclei (quenching)
- Consistent normalization applied across all reactions

This is exactly the framework discussed in Kay 2021 (sum rules in deformed nuclei). Here in
spherical/near-spherical 136Xe/136Ba, the standard Nj~0.6 applies.

---

## Connection to HELIOS

- **B.P. Kay** -- primary HELIOS contact at ANL
- **Method directly applicable to HELIOS:** (d,p) in inverse kinematics at HELIOS could
  probe neutron-rich candidates where stable targets are unavailable. HELIOS advantage:
  can use exotic beams on d/p target.
- **Spectroscopic factors + sum rules** -- same framework used for all HELIOS (d,p) analysis
  (h095 11C, h096 31Si, future experiments)
- The (d,p)+(p,d) complementary pair is standard for HELIOS science program
- **High-j orbitals:** The need for (α,3He) to probe high-j states hints at why HELIOS
  experiments often need good momentum matching -- orbital angular momentum matters for
  reaction sensitivity
- **0vββ context:** Several proposed HELIOS experiments target nuclei near double-beta
  decay candidates (neutron-rich region)

---

_Read and noted: 2026-04-18 (Spark). Source: ~/publications/2016_Szwec_Rearrangement_of_valence_neutr.pdf_
