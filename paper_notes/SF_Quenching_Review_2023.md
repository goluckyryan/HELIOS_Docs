# Quenching of Spectroscopic Factors -- Review Notes

**Source:** https://nukephysik101.wordpress.com/2023/05/20/papers-reading-on-the-recent-progress-of-the-quenching-of-spectroscopic-factor/  
**Author:** Ryan Tang (nukephysik101 blog)  
**Read:** 2026-04-24

---

## Timeline of the Quenching Story

### 1993 -- (e,e'p) confirms quenching
- Udías et al., PRC 48, 2731 (1993): (e,e'p) on ⁴⁰Ca and ²⁰⁸Pb
- Coulomb probe (well-understood) → SF quenched ~30% vs shell model
- Established quenching is not a hadronic probe artifact

### 2001 -- Hadronic and EM probes consistent
- Kramer, Blok, Lapikás, NPA 679, 267 (2001): (e,e'p) and (d,³He) give consistent quenching
- Lee, Tsang, Lynch, PRC 75, 064320 (2007): (d,p) and (p,d) consistent for Z=3–24

### ~2004 -- Theory: SRC + LRC
- Dickhoff & Barbieri, Prog. Part. Nucl. Phys. 52, 377 (2004):
  - **Short-range correlations (SRC):** high-momentum pairs, nucleon briefly "kicked out" of orbital
  - **Long-range correlations (LRC):** coupling to collective excitations
  - Both reduce the single-particle occupancy → quenching

### 2008/2014 -- Gade plot: Δ_S dependence
- Gade et al., PRC 77, 044306 (2008); updated PRC 90, 057602 (2014)
- Systematic knockout data on unstable nuclei at 100 MeV/u on ⁹Be
- **Key finding:** SF quenching scales with Δ_S = S_p - S_n (proton-neutron Fermi surface difference)
  - Weakly bound (small |Δ_S|) → small quenching (Rs ~ 0.9)
  - Deeply bound (large |Δ_S|) → large quenching (Rs ~ 0.4)
- Interpretation: weakly bound nucleon ≈ independent particle (mean-field dominates), so quenching small

### 2018 -- Oxygen chain contradicts Gade
- GSI (p,2p) PRL 120, 052501 (2018) + RIKEN PTEP 2018, 021D01 (2018):
  - ¹⁴O → ²⁴O oxygen chain: quenching nearly **independent of Δ_S**
  - Conflict with Gade plot -- major controversy
- Debates focus on: reaction mechanism differences, ⁹Be target theory completeness, impulse approximation for (p,2p), final state interaction treatment

### 2022/2023 -- Transfer reactions weigh in
- **Kay et al., PRL 129, 152501 (2022):** (d,p) at 10 MeV/u (HELIOS!)
  - Mixed ¹⁴N + ¹⁴C beam → simultaneous (d,p) reactions → eliminates systematic uncertainty
  - Result: quenching **does NOT depend on Δ_S**
  - Transfer reaction mechanism well-understood → reliable SF extraction
- **Pohl et al., PRL 130, 172501 (2023):** (p,pN) on ¹⁴O at 100 MeV/u
  - When inelastic channels (¹⁴O* → p + ¹³N) included: quenching independent of Δ_S
  - Without inelastic: would recover Δ_S dependence
  - Suggests Gade plot used **incomplete reaction theory** (missing inelastic channel)

---

## Current Status (as of 2023)

The weight of recent evidence (Kay 2022, Pohl 2023, Jiang 2025) points toward:
- **Quenching is roughly universal (~60-70%), does NOT strongly depend on Δ_S**
- The Gade plot Δ_S trend was likely an artifact of incomplete reaction theory on ⁹Be knockout
- Transfer reactions (d,p), well understood, give reliable SFs
- Short-range correlations (SRC) are likely the dominant cause of universal ~30-40% quenching

---

## Assumptions to Watch

1. **Reaction mechanism reliability:** Transfer (d,p) at low energy (~10 MeV/u) is considered the most reliable -- well-understood DWBA, clean single-step
2. **OMP sensitivity:** Different OMPs → different σ_DWBA → different SF. Kay 2022 controlled this by simultaneous reactions
3. **Gade plot:** Built on HI knockout at 100 MeV/u on ⁹Be -- reaction theory may be incomplete (Pohl 2023 evidence)
4. **(p,2p) impulse approximation:** Still not fully validated at ~100 MeV/u

## Further Questions

- What is the actual magnitude of SRC contribution vs LRC? Can theory predict the ~30% number from first principles?
- Does quenching depend on nuclear structure (magic numbers, deformation) independently of Δ_S?
- What does HELIOS data on ¹⁵C (Jiang 2025, Rs~0.64) tell us -- consistent with universal quenching?
- Kay 2022 used ¹⁴N+¹⁴C mixed beam -- how was beam composition handled experimentally?

## Related Papers / Notes
- `SF_Theory_SumRule.md` -- sum rule derivation (Glendenning Ch.7)
- `2021_Kay_Consistency_NucleonTransfer_SumRules.md` -- Kay 2021 on sum rules in deformed nuclei
- `2025_Jiang_Quenching_15C_Transfer.md` -- Jiang 2025, Rs~0.64 for ¹⁵C at HELIOS
- Kay et al. PRL 129, 152501 (2022) -- **not yet in ~/publications/** -- request download

---

## Part II: Is SF an Observable? (Jan 2024)

**Source:** https://nukephysik101.wordpress.com/2024/01/01/some-thoughts-on-the-quenching-of-spectroscopic-factor-ii/

### The observability debate

- **Blokhintsev (2022)** and **Jennings (2011):** SF is non-invariant under unitary transformations of nuclear forces → not an observable in the strict sense
- **Duguet et al. (PRC 92, 034313):** "Nonobservable nature of nuclear shell structure" -- worth reading
- Ryan's position: **SF is an observable** once the basis and 1st-order interaction are fixed
  - Analogy: neutrino mass hierarchy is well-defined once neutrino mass is fixed, even if currently unknown
  - The community has converged on consistent quenching despite 50% uncertainty → they've implicitly agreed on basis + interaction range
  - SF is a "quasi-observable" or "extractable" -- will become fully observable when nuclear interaction is fully fixed

### Is it SF or cross-section that's quenched?

- Since σ_exp = C²S × σ_DWBA, if σ_DWBA is the "perfect" theoretical XS with SF=1, then:
  - If σ_DWBA is perfect → SF = σ_exp/σ_DWBA < 1 → SF is quenched
  - If σ_DWBA is not perfect (missing correlations) → the quenching is in the theory, not the nucleus
- Ryan's view: if σ_DWBA were perfectly calculated, SF would be unity and no quenching. The quenching reflects **theory incompleteness** (reaction theory + correlation effects), not a property of the nucleus per se.
- Cross-section is the true observable. SF is the extracted quantity given a theoretical framework.

### Implications

- SF is not "aether" -- it reveals real structure (nucleon configurations, ESPE)
- **ESPE** (effective single-particle energy) = SF-weighted centroid energy of an orbital -- agrees with Woods-Saxon mean field → confirms SF is extracting real physics
- **ANC** has the same non-observability argument (wavefunction not observable) but is clearly physically meaningful
- The 50% uncertainty in extracted SFs = uncertainty in the theoretical framework (OMP, bound state geometry, reaction model), not noise

### Key Assumption Highlighted
- The entire quenching discussion is framework-dependent. A "better" reaction theory or OMP → different σ_DWBA → different SF. This is not a bug, it's the nature of the quantity.

_Created: 2026-04-24. Source: nukephysik101.wordpress.com_
