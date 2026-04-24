# h096 Proposal Notes -- ATLAS Exp 2214

**Title:** Configuration mixing in 0+ and 2+ states in 32Si
**PI:** Matthew Martin (matthew.martin@anl.gov), ANL
**PAC cycle:** Oct/27, 2025 | **Submitted:** Sep 22, 2025
**File:** `~/HELIOS_MD/proposals/2214_Martin.pdf`
**Days approved:** 3 (continuous run, in-flight beam)

---

## Physics Goal

**32Si lies at the edge of the N=20 island of inversion.** The island of inversion (centered
at 32Mg) is a region where the spherical shell-model shell closures break down and
multi-particle-multi-hole (np-nh) cross-shell excitations dominate the ground state.

**Key observations motivating the experiment:**
- 34Si (one proton pair more): 0+2 and 2+1 states dominated by pf-shell (intruder) configurations
- 32Si (sd-shell neighbor): predicted to have PURE sd-shell ground state
- But: B(E2; 2+1->0+g.s.) from Coulomb excitation (Heery 2024) is LOWER than shell model
  predictions (FSU, SDPF-MU, USDB) -- suggests MORE pf-shell mixing than expected
- Ab initio VS-IMSRG calculations agree with the lower B(E2) value
- Discrepancy between Heery Coulex and Williams DSAM measurements (1.4 sigma tension)
- 5- isomer in 32Si (Williams 2023, confirmed by Hoffman HELIOS, Ref[23]) has dominant
  (d3/2)^-1 (f7/2)^1 configuration -- pf-shell already present at higher Ex

**Goal:** Directly measure configuration mixing via 31Si(d,p)32Si spectroscopic factors.
- Extract C^2S for the lowest 0+ and 2+ states (sd vs pf contributions)
- Target states: 0+g.s. (0 keV), 2+1 (1941.7 keV), 2+2 (4231.0 keV), 0+2 (4984.2 keV)
- Differentiate between FSU, SDPF-MU, USDB, and VS-IMSRG predictions

---

## Experimental Setup

**Beam:** 31Si at 10 MeV/u (310 MeV), 4x10^5 pps, ~5% purity (RAISOR in-flight)
**Target:** CD2, 100 µg/cm2
**B-field:** 2.85 T
**Si array:** 35 cm long, z in [-600, -250] mm (upstream of target)
**Coverage:** theta_CM = 10-40 deg, Ex = 0-6 MeV
**Resolution:** ~100 keV FWHM (from previous h096-type run experience)

**Rate estimates (3 days):**
- 2+1 and 2+2 peaks: ~2800 counts each (few % stat uncertainty)
- 0+g.s.: ~1500 counts
- 0+2: ~6 counts (only limits possible)

**Previous run:** Same setup, 2x10^4 pps, 3 days (intermediate Ex, lower stats, referenced as Ref[23])
-- That was the earlier h096 running period.

---

## Connection to Current h096 Run

- **This is the proposal for h096** -- 31Si(d,p)32Si at HELIOS with 2.85 T
- States of interest: g.s., 2+1 at 1.942 MeV, 2+2 at 4.231 MeV, 0+2 at 4.984 MeV
- The 5- isomer (Hoffman 2026 paper, same reaction) populated at higher Ex
- **SDPF-MU** and **FSU** are the key shell model interactions for comparison
- Note: "31Si beam" at 10 MeV/u means ELAB = 23 MeV (A_target=2 -> E_per_u * A_target)
  which matches HELIOS InFileCreator convention: `31Si(d,p)32Si 0+ 0d3/2 3/2+ 0.000 10MeV/u AK`

## Physics Context

**N=20 island of inversion:**
- 32Mg center: 2p2h and 4p4h dominate g.s. (well-established)
- 30Mg, 34Si: intruder 0+ states nearby
- 32Si: sd-shell predicted for g.s., but B(E2) anomaly suggests otherwise
- This experiment will directly quantify the sd/pf mixing fraction

**32Si spectroscopy history:**
- 1972, 1982, 1998: 30Si(t,p) and (t,pγ) -- old data, poor quality
- 2023: Williams -- 5- isomer confirmed spin-trapped, pf-shell character
- 2024: Heery -- Coulex B(E2) suppressed vs theory
- 2025: Williams -- intruder structures (ongoing analysis)
- 2025: Watwood -- 32Si(3He,d)33P proton vacancy (SOLARIS) -- 1s1/2 empty
- 2026: Hoffman -- 31Si(d,p) HELIOS, 5- isomer C2S=1.00 (draft)
- **This run (h096):** higher-stats 31Si(d,p), focus on 0+ and 2+ config mixing

---

_Notes created: 2026-04-19 (Spark). Source: ~/HELIOS_MD/proposals/2214_Martin.pdf_
