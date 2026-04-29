# Paper Notes: Schiffer et al. 2012 -- Test of Sum Rules in Nucleon Transfer

**Citation:** J.P. Schiffer, C.R. Hoffman, B.P. Kay et al., PRL 108, 022501 (2012)
**DOI:** 10.1103/PhysRevLett.108.022501
**PDF:** `~/publications/2012_Schiffer_NiSumRules.pdf`
**Read:** 2026-04-25 (notes); PDF obtained 2026-04-28

---

## Physics

- **Reactions:** (d,p), (p,d) neutron transfer + (α,³He), (³He,α) + (³He,d), (α,t) proton-adding on ⁵⁸⁶⁰⁶²⁶⁴Ni
- **Facility:** Yale tandem accelerator + Enge split-pole spectrograph (NOT HELIOS -- conventional kinematics)
- **Beam energies:** 10 MeV deuterons, 28 MeV protons, 38 MeV α, 25 MeV ³He, 18 MeV ³He
- **Targets:** 200 μg/cm² isotopically enriched Ni foils
- **Goal:** Quantitative test of Macfarlane-French sum rules using adding+removal on same targets

## Macfarlane-French Sum Rule

```
n_j (occupancy from removal) + v_j (vacancy from adding) = 2j+1
```
Equivalently: ΣG⁺ S_adding + ΣG⁻ S_removal = (2j+1)
where G± are isospin Clebsch-Gordan coefficients.

**Normalization procedure:** Fix overall normalization N so that sum adds to 2j+1. Different N for each ℓ value, but consistent across isotopes.

## Key Quantitative Results

**Normalization factors (quenching ~0.5):**
| Nucleus | N(ℓ=1) | N(ℓ=3, n) | N(ℓ=3, α,³He) |
|---------|---------|-----------|---------------|
| ⁵⁸Ni | 0.527 | 0.528 | 0.518 |
| ⁶⁰Ni | 0.548 | 0.503 | 0.464 |
| ⁶²Ni | 0.558 | 0.554 | 0.471 |
| ⁶⁴Ni | 0.566 | 0.480 | 0.433 |
| **Mean** | **0.550±0.015** | **0.517±0.028** | **0.471±0.030** |

~0.5-0.6 normalization consistent with (e,e'p) quenching results -- confirms universal ~50% quenching.

**Neutron occupancies (1p3/2 + 0f5/2 + 1p1/2 + 0g9/2):**
| Nucleus | 1p3/2 | 0f5/2 | 1p1/2 | 0g9/2 | Total |
|---------|-------|-------|-------|-------|-------|
| ⁵⁸Ni | 0.96 | 0.67 | 0.40 | 0 | 2.03 |
| ⁶⁰Ni | 1.74 | 1.61 | 0.71 | 0 | 4.06 |
| ⁶²Ni | 2.31 | 2.31 | 0.93 | 0.34 | 5.89 |
| ⁶⁴Ni | 3.17 | 3.41 | 1.07 | 0.66 | 8.31 |
| Expected | | | | | 2,4,6,8 |

- Agreement with expected values < 5% deviation
- All three pf-shell orbits fill roughly in parallel (not sequential)
- 0g9/2 appears only in ⁶²Ni and ⁶⁴Ni; likely underestimated (states at high Ex)

**Proton vacancies:** ~12.0(3) across all four isotopes (Z=28 closed shell, should be constant) ✓

**Missed strength:** ~2.8% above 3.5 MeV (estimated from Lorentzian fit) -- small correction

## Key Conclusion

Spectroscopic factors from transfer reactions **do** provide self-consistent, meaningful occupancy information, despite debate over whether they are rigorous observables. Internal consistency checks:
1. Sum rules satisfied to <5% across isotopes with changing neutron number
2. Proton vacancies remain constant (as expected) across all four isotopes
3. Normalization ~0.5-0.6 is consistent with (e,e'p) quenching -- not a free parameter

## Relevance

- **Direct validation** of the SF extraction method used for h096 ³¹Si(d,p)³²Si
- Same team: Schiffer, Hoffman, Kay
- For h096: sum rule check — ΣC²S(adding) + ΣC²S(removal) should = 2j+1 for each orbital
- Universal quenching ~0.5-0.6: does NOT depend on ΔS (isospin asymmetry) -- contradicts some claims
- Foundation for Kay 2022 (consistency in deformed nuclei) and h096 analysis framework
- The Macfarlane-French sum rule: n_j + v_j = 2j+1

_Created: 2026-04-25 | Updated with full details: 2026-04-28_
