# Effective Single Particle Energy (ESPE)

**Source:** https://nukephysik101.wordpress.com/2021/04/15/effective-single-particle-energy/  
**Reference:** Baranger, NPA (1970) -- "A Definition of the single-nucleon potential"  
**Read:** 2026-04-24

---

## Connection to Sum Rule

The ESPE is the SF-weighted centroid energy of an orbital -- it is the *practical payoff* of the sum rule calculation. While the sum rule counts the total strength, the ESPE tells you *where* that strength sits energetically, which is the mean-field single-particle energy.

---

## Definition

For nucleus A (e.g. ¹²C), ESPE of orbital j extracted from:
- Adding reaction A(d,p)B: states of B=A+1, SFs, separation energy S_n(B)
- Removal reaction A(p,d)C: states of C=A-1, SFs, separation energy S_p(A)

**Step 1: Spectroscopic strength (G)**

```
G⁺ = Σ_i (2J_B+1)/(2J_A+1) × C²S_i⁺    [adding, weighted by degeneracy ratio]
G⁻ = Σ_i C²S_i⁻                           [removing]
```

Sum rule requires: G⁺ + G⁻ = 2j+1 (times quenching factor Rs if applied)

**Step 2: Energy centroids**

```
E_j⁺(i) = E*(i) + S_n(A+1)    [energy of state i relative to A threshold, adding]
E_j⁻(i) = E*(i) + S_p(A)      [energy of state i relative to A threshold, removal]
```

Wait -- more carefully:
```
ε_j⁺ = -E_B(A+1) + E_j⁺    [centroid of orbital in A+1, relative to vacuum]
ε_j⁻ = -E_B(A) - E_j⁻      [centroid of orbital in A-1, relative to vacuum]
```

**Step 3: ESPE**

```
ESPE = (ε_j⁺ × G⁺ + ε_j⁻ × G⁻) / (G⁺ + G⁻)
```

SF-weighted average of adding and removal centroids. Reduces to:
- ε_j⁻ alone when G⁺ → 0 (e.g. p-shell of ¹⁶O: can't add to filled p-shell)
- ε_j⁺ alone when G⁻ → 0 (e.g. sd-shell of ¹⁶O: nothing to remove)

---

## Example: ¹²C, 0p3/2 orbital

From ¹²C(d,p)¹³C (adding): E*=3.684 MeV, J=3/2-, C²S=0.14 → G⁺=0.56, E⁺G⁺ = 2.063
From ¹²C(p,d)¹¹C (removal): E*=0.000, C²S=2.5 + others → G⁻=2.8475, E⁻G⁻ = ...

Result: **ESPE(0p3/2) = -16.35 MeV**  
WS fit (neutron mass): V₀=-60.9 MeV, r₀=1.13 fm, a₀=0.69 fm agrees.

| Orbital | ESPE (MeV) | WS fit (MeV) |
|---|---|---|
| 0p3/2 | -16.36 | -16.39 |
| 0p1/2 | -9.42  | -9.45  |
| 1s1/2 | -1.87  | -1.80  |
| 0d5/2 | -1.22  | -1.21  |

ESPE agrees well with WS mean-field energies → confirms SF is extracting real nuclear structure.

---

## Why ESPE Matters

1. **ESPE = experimental mean-field energy.** It's what you'd get from a Woods-Saxon potential fit to the data.
2. **ESPE evolution** across isotopic/isotonic chains reveals shell evolution, monopole shifts, tensor force effects -- the key observable for nuclear structure systematics.
3. **Validates SF:** If ESPE agreed with WS even though individual SFs are quenched (60-70%), the mean-field picture is self-consistent. This is why SF is not "aether" even if it's quenched.
4. **Connection to quenching:** The quenching factor Rs appears in G⁺ + G⁻ = Rs × (2j+1). But ESPE is robust to quenching -- it cancels in the weighted average. So ESPE is more reliable than absolute SFs.

---

## Assumptions

1. **All relevant states included** -- must sum over all states up to the particle threshold. Missing strength biases the centroid.
2. **Correct spin assignments** -- wrong J → wrong (2J_B+1)/(2J_A+1) weighting in G⁺
3. **Accurate SFs** -- OMP/reaction model dependence propagates into G, but cancels in ESPE ratio if consistent framework used
4. **Threshold energy known** -- S_n or S_p must be accurate (AME2020)

## Further Questions

- How sensitive is ESPE to the OMP choice? (More robust than individual SFs?)
- For exotic nuclei with fragmented strength, how many states can realistically be measured?
- Does ESPE evolution across Sn chain (Szwec 2021) show tensor force monopole shift clearly?

## Related Notes
- `SF_Theory_SumRule.md` -- sum rule derivation
- `SF_Quenching_Review_2023.md` -- quenching discussion, ESPE mentioned in Part II
- `2021_Szwec_SnIsotopes_Occupancies.md` -- ESPE systematics in Sn chain

_Created: 2026-04-24_
