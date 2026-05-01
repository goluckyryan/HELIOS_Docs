# 2025 Watwood et al. -- Valence 1s-0d proton vacancy of the 32Si ground state

**Citation:** N. Watwood et al., Phys. Rev. C **112**, 054304 (2025)
**DOI:** 10.1103/4lzs-mv3l
**PDF:** `~/publications/2025_Watwood_Valence_1s0d_proton_vacancy.pdf`
**Documented:** 2026-04-18

---

## Key Information

- **Reaction studied:** 32Si(3He,d)33P in inverse kinematics at 6.3 MeV/u
- **Facility:** SOLARIS solenoidal spectrometer + ReA6 reaccelerator at NSCL (Michigan State)
- **Beam:** Long-lived 32Si, ~10^5 pps, ~90% pure (dominant contaminant: 32S isobar)
- **Target:** Few ug/cm2 of 3He trapped in 400 ug/cm2 titanium lattice (from tritium decay, T1/2 ~12.3 y)
- **B-field:** 3 T (SOLARIS solenoid)
- **Array position:** -570 to -220 cm upstream of target
- **Recoil telescope:** 80.5 cm downstream; 53 um dE + 150 um Eres square silicon detectors
- **Resolution:** ~470 keV FWHM (dominated by energy loss/straggling in Ti lattice target)

---

## Authors (selected HELIOS-relevant)

- N. Watwood (ANL, now TAMU) -- contact author
- C. R. Hoffman (ANL) -- contact author
- B. P. Kay (ANL)
- I. A. Tolstukhin (ANL)
- J. Chen (SUSTech, Shenzhen)
- T. L. Tang (ANL) -- **Ryan**
- H. Jayatissa (ANL)
- A. H. Wuosmaa (UConn)

---

## Physics Goal

Extract the **proton 1s-0d shell vacancy** of the 32Si ground state by combining:
1. Single-proton-adding data: 32Si(3He,d)33P (this work) -- populates T< states
2. Single-neutron-adding data: 32Si(d,p) from Ref. [6] -- provides T> analog information

This probes:
- Proton 0d5/2 - 1s1/2 (Z=14) subshell closure persistence
- Neutron distribution of 2 neutron holes within the N=20 shell gap (0d3/2 - 0f7/2)
- Evidence for smooth vs abrupt structural changes across even-A Si isotopes (28,30,32,34Si)

---

## States Observed in 33P

| Ex (MeV) | J-pi | n-l-j | Transfer l | Notes |
|----------|------|-------|------------|-------|
| 0.000 | 1/2+ | 1s1/2 | 0 | g.s. |
| 1.431 | 3/2+ | 0d3/2 | 2 | |
| 1.847 | 5/2+ | 0d5/2 | 2 | |
| 2.538 | 3/2+ | 0d3/2 | 2 | |
| 3.4(1) | -- | -- | -- | Unassigned; near 3.276 (3/2+) and 3.491 (5/2+); excluded from vacancy analysis |
| 4.23 | 7/2- | 0f7/2 | 3 | Lowest 0f7/2 proton fragment; yield at single angle only |

---

## DWBA Analysis

- Code: PTOLEMY
- Optical model parameters: Global models from Refs. [26,27] for 3He and deuteron channels
- 3He-d overlap form factor: Green's function Monte Carlo (GFMC) results of Ref. [28]
- Bound-state: Woods-Saxon, r0 = 1.25 fm, a = 0.65 fm, depth adjusted to match binding energy
- Systematic uncertainties: 5% for l>0 relative C2S; 15% for l=0 g.s. (more sensitive to OMP)

### Isospin Decomposition

- 32Si has T=2, Tz=2 (neutron-rich) -- proton adding splits strength into T< and T> states
- T< states: directly populated in (3He,d), below ~4.5 MeV in 33P
- T> states: accessed via neutron-adding analog data from 32Si(d,p) [Ref. 6]
- Relation: C2 = 2T/(2T+1) = 4/5 for T< states

### Normalization

- Macfarlane-French sum rules: total proton vacancy across entire 1s-0d shell fixed to 6 (assuming Z=8 and Z=20 closures)

---

## Spectroscopic Factors (32Si, this work + Ref. [6])

### 32Si(3He,d)33P (proton adding, T<):
| Ex (MeV) | J-pi | n-l-j | S |
|----------|------|-------|---|
| 0.00 | 1/2+ | 1s1/2 | 1.06(21) |
| 1.43 | 3/2+ | 0d3/2 | 0.67(15) |
| 1.85 | 5/2+ | 0d5/2 | 0.16(5) |
| 2.54 | 3/2+ | 0d3/2 | 0.31(11) |

### 32Si(d,p) (neutron adding, T> analogs, Ref. [6]):
| Ex (MeV) | J-pi | n-l-j | S |
|----------|------|-------|---|
| 0.00 | 3/2+ | 0d3/2 | 0.37(4) |
| 1.01 | 1/2+ | 1s1/2 | 0.25(5) |

---

## Key Results: 32Si Ground-State Proton Vacancy

| Orbital | Vacancy | Occupancy (of 2j+1) |
|---------|---------|---------------------|
| 0d5/2 | 0.9(4) | ~5.1 / 6 |
| 1s1/2 | 2.2(5) | ~-0.2 / 2 (consistent with empty) |
| 0d3/2 | 2.9(6) | ~1.1 / 4 |

**The proton 1s1/2 orbital in 32Si is consistent with being empty (vacancy ~2).**

---

## Systematics: Trends Across 28,30,32,34Si

The paper includes reanalysis of 28Si and 30Si data using consistent DWBA parameters. Key findings:

1. **Both proton and neutron vacancy data show gradual changes** -- no abrupt structural transition
2. **Proton 1s1/2 is empty in both 32Si and 34Si** -- the Z=14 subshell gap (0d5/2 - 1s1/2) persists
3. **Neutron occupancies evolve smoothly** toward N=20 -- the 0d3/2 orbital empties gradually
4. **Shell-model calculations** (USDB, SDPF-MU) constrained to 1s-0d space describe the data well
5. The ground-state wave function of 32Si is **well contained within the sd shell** -- no significant pf-shell intrusion, unlike 34Si where N=20 erosion is debated

---

## Relevance to h096 (31Si(d,p)32Si)

This paper is **directly complementary** to our current experiment:
- They measured 32Si(3He,d)33P -- proton adding on the same nucleus
- We measure 31Si(d,p)32Si -- neutron adding on the neighbor
- Their neutron-adding reference data is from 32Si(d,p) [Ref. 6] -- this is exactly the reaction in the h096 proposal motivation
- The spectroscopic factors from Ref. [6] (0d3/2 g.s. S=0.37, 1s1/2 1.01 MeV S=0.25) are the T> analog complements
- Our h096 experiment measures 31Si(d,p)32Si spectroscopic factors for the SAME final nucleus (32Si) but accessed from a different initial state
- The 32Si states of interest (0+1 g.s., 2+1 at 1.94 MeV, 2+2 at 4.23 MeV, 0+2 at 4.98 MeV) probe configuration mixing that this paper's vacancy analysis constrains

### Shell Model Interactions Referenced
- USDB (Brown & Richter, PRC 2006)
- SDPF-MU (Utsuno et al., PRC 2012)

---

## Experimental Technique Notes (relevant to HELIOS/SOLARIS)

- Same solenoidal spectrometer concept as HELIOS
- PSD array upstream, recoil telescope downstream -- standard HELIOS-like setup
- Heavy-ion recoil PID via dE-Eres telescope discriminates Z=14 (Si), Z=15 (P), Z=16 (S)
- Timing coincidence (FWHM ~20 ns) separates deuterons from protons via cyclotron period T_cyc ~ A/q
- 20-ns timing gate selects single-orbit deuterons, discriminates against 32Si(3He,p)34P protons
- Resolution limited by Ti lattice target (470 keV vs ~100 keV for standard CD2)

---

## References of Note

- [6] = Previous 32Si(d,p) neutron-adding data -- source of T> analog spectroscopic factors
- [23,24] = 28Si(3He,d) and 30Si(3He,d) data used in systematics
- [25] = PTOLEMY code
- [26,27] = Global OMP sets (3He, deuteron)
- [28] = GFMC form factor for 3He-d overlap
