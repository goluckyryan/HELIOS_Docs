# Paper Notes: Hoffman et al. (2026) — ³²Si Jπ=5⁻ Isomeric State

**Title:** "Observation of a dominant 0f₇/₂ neutron configuration in the ³²Si Jπ=5⁻ isomeric state"
**Authors:** C. R. Hoffman, G. L. Wilson, J. Chen, B. P. Kay, T. L. Tang, S. R. Carmichael, M. Gott, S. Lesher, M. S. Martin, G. E. Morgan, J. Wu
**Date:** Draft dated February 20, 2026 (pre-publication)
**Affiliation:** ANL Physics Division + LSU, Notre Dame, Wisconsin-La Crosse
**Status:** [!!] Draft — not yet published. Handle with discretion.

---

## Relevance to h096

**This paper IS h096's direct predecessor.** It uses HELIOS + ATLAS in-flight to study ³²Si via
³¹Si(d,p)³²Si at **9.6 MeV/u** — the same reaction, same beam, same energy as h096.

Key differences from h096:
- This paper focused on the **5⁻ isomeric state** and yrast 3⁻ level specifically
- ³¹Si beam: 2×10⁴ pps on target, ~30% ³²Si purity (30Si¹³⁺ contamination)
- Target: **150 μg/cm² CD₂**
- Q-value resolution: ~300 keV
- Array: -52 cm to -17 cm upstream (30 detectors, 6 sides)
- RDT: 1100 cm downstream, 4× ΔE-E Si sets (50 μm ΔE + 1000 μm E), inner r=9 mm, outer r=48 mm
- B-field: 2.5 T

h096 uses: **214 μg/cm² CD₂**, B=2.85 T, RDT at 1100 mm (same), array at -200 mm

---

## Physics Background

### The ³²Si 5⁻ Spin-Trap Isomer

- **Z=14, N=18 nucleus** — 1s-0d shell
- Jπ=5⁻ isomeric state at **Ex=5.505 MeV**, mean lifetime τ=46.9(5) ns
- Decays >99% via **hindered E3 transition** (3562.84 keV) to 2⁺₁
  - B(E3; 5⁻→2⁺₁) = 0.0841(10) W.u. — strongly hindered
  - Bypasses the nearby 3⁻₁ level (Ex=5.288 MeV) via what would be a 0.217 MeV γ
  - B(E2; 5⁻₁→3⁻₁) < 0.053 W.u. — extremely hindered
- In ³⁴S and ³⁶Ar: B(E2, 5⁻→3⁻) ≈ 0.5–1 W.u. (not nearly as hindered)

### N=18 Isotone Systematics

The 5⁻ level appears across N=18 isotones (³²Si Z=14, ³⁴S Z=16, ³⁶Ar Z=18):
- Ex(5⁻) stays roughly **constant** across isotones — consistent with single-particle
  (0d₃/₂)¹(0f₇/₂)¹ neutron cross-shell excitation tracking the 0f₇/₂−0d₃/₂ energy difference
- Ex(4⁺₁) **rises** as Z decreases — proton participation hindered at Z=14 due to robust
  Z=14 sub-shell gap (0d₅/₂−1s₁/₂)
- Ex(3⁻₁) **rises** with decreasing Z — reduced octupole collectivity at lower Z
- B(E2, 2⁺₁→0⁺₁) is reduced in ³²Si vs ³⁴S/³⁶Ar — evidence for Z=14 sub-shell gap

### Why is the 5⁻→3⁻ E2 so hindered in ³²Si?

Previous shell-model (FSU interaction) calculations reproduced the hindered B(E2) and found
a ~0.2 nucleon change in 0f₇/₂ neutron occupancy between 5⁻₁ and 3⁻₁.

But there's a tension: ³²Si should have the **least mixed** 3⁻₁ among the isotones, yet has
the **smallest** B(E2, 5⁻→3⁻). This paper's conclusion:

> **The hinderance is NOT primarily due to differing neutron configurations.**
> Instead, **lack of proton participation** in the transition is the driving mechanism.

---

## Experimental Method

- **Facility:** ATLAS in-flight, ANL
- **Primary beam:** ³⁰Si at 11.5 MeV/u → gas cell (D₂, 90 K, 1050 Torr) → ³¹Si¹⁴⁺ at 9.6 MeV/u
- **³¹Si rate:** ~2×10⁴ pps on target; ~30% purity (main contaminant: ³⁰Si¹³⁺ at ~9 MeV/u)
- **HELIOS:** 2.5 T solenoid, proton-recoil coincidences
- **Proton selection:** relative time (proton–recoil ΔT) = cyclotron period tag
- **Recoil selection:** ΔE-E Si telescope combination
- **Q-value resolution:** ~300 keV (dominated by beam energy spread)
- **DWBA:** finite-range PTOLEMY, global OMP sets (Refs [33,34])
  - Deuteron: Argonne v18 bound-state potential
  - Neutron: Woods-Saxon, r₀=1.25 fm, a=0.65 fm, Vso=5.0 MeV, rso=1.1 fm, aso=0.65 fm
  - Systematic C²S uncertainty: 10% (OMP sensitivity)

---

## Key Results

### Excitation Spectrum (Ex = 3.5–8.5 MeV)

Peaks identified (Gaussian fits, FWHM=300 keV fixed):

| Ex (MeV, fit) | Jπ | ℓ | C²S (normalized) | Notes |
|---|---|---|---|---|
| 4.26(3) | 2⁺ | 2 | 0.48(20) | ℓ=0 also allowed |
| 5.28(3) | 3⁻ | 3 | 0.44(11) | yrast 3⁻₁; ℓ=0 also < 0.1 |
| **5.50(3)** | **5⁻** | **3** | **≡ 1.00(11)** | **Isomer — dominant ℓ=3** |
| 5.78(3) | 3(⁻) | 1+3 | 0.53/0.38 | possible multiple states |
| 6.36(4) | 4(⁻) | 3 | < 0.4 | |
| 6.63(4) | — | — | — | |
| ~6.8 | (4⁻,5⁻) / (2,3) / (3⁻) | — | — | multiple possible states |

- No significant yield near Ex≈5.97 MeV (3⁻ suggested by (t,p) not confirmed)
- ℓ=1 contribution to 5.505-MeV state: < 10% (upper limit)

### Angular Distributions & DWBA

- 5.505-MeV state: clean **ℓ=3** angular distribution — unambiguous 0f₇/₂ neutron transfer
- No ℓ<3 features — confirms pure (0d₃/₂)¹(0f₇/₂)¹ neutron configuration
- 3⁻₁ at 5.288 MeV: C²S(3⁻)/C²S(5⁻) ≈ **0.44** (cf. ³⁴S ratio ≈ 0.25)
  - 3⁻₁ in ³²Si is less mixed than in ³⁴S, consistent with reduced collectivity at Z=14

### Main Conclusion

The 5⁻ isomeric state has **dominant single-particle ν0f₇/₂ character** (large C²S, pure ℓ=3).
The 3⁻₁ has ~44% the single-neutron strength of the 5⁻. The reduced B(E2,5⁻→3⁻) in ³²Si
is proposed to arise from **lack of proton participation**, not neutron wave-function mismatch.

---

## Relevance to h096 Analysis

1. **Same kinematics:** 9.6 MeV/u ³¹Si(d,p)³²Si — use this paper's Ex values as reference peaks
2. **Target thickness:** They used 150 μg/cm² CD₂; h096 uses 214 μg/cm² — thicker target,
   more yield but worse Q-value resolution (already ~300 keV, will be worse)
3. **5⁻ isomer at Ex=5.505 MeV** is the dominant peak — watch for it in h096 spectrum
4. **3⁻₁ at Ex=5.288 MeV** is the second ℓ=3 state — partially overlaps 5⁻ in low-res data
4. **DWBA parameters:** Directly usable for h096 angular distribution fits (same reaction)
5. **Beam contamination:** ³⁰Si¹³⁺ at ~9 MeV/u is the main background (same as h096)
   - They validated analysis using ³⁰Si(d,p)³¹Si contaminant data vs known C²S values
6. **RDT geometry:** 1100 cm downstream — same as h096 (RDT at 1100 mm in run_state.json)

---

## Authors & Affiliations

- C. R. Hoffman (calemhoffman) — ANL, corresponding author
- B. P. Kay (benkay2482) — ANL
- T. L. Tang (goluckyryan/Ryan) — ANL
- J. Chen — formerly ANL, now SUSTech Shenzhen
- G. L. Wilson, G. E. Morgan — LSU
- S. R. Carmichael — Notre Dame (now ANL)
- M. Gott — ANL (now ORNL)
- S. Lesher — Wisconsin-La Crosse (now NC A&T)
- J. Wu — ANL (now BNL)
