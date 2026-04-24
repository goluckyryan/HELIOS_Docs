# Effective Single Particle Energy (ESPE)

**Source:** https://nukephysik101.wordpress.com/2021/04/15/effective-single-particle-energy/  
**Reference:** Baranger, NPA (1970) -- "A Definition of the single-nucleon potential"  
**Read:** 2026-04-24

---

## Connection to Sum Rule

ESPE is the SF-weighted centroid energy of an orbital -- the practical payoff of the sum rule. While the sum rule counts total strength, ESPE tells you *where* that strength sits energetically, i.e. the mean-field single-particle energy.

---

## Definition

For nucleus $A$, ESPE of orbital $j$ extracted from:
- Adding reaction $A(d,p)B$: states of $B=A+1$, SFs, separation energy $S_n(B)$
- Removal reaction $A(p,d)C$: states of $C=A-1$, SFs, separation energy $S_p(A)$

**Step 1: Spectroscopic strength**

$$G^+ = \sum_i \frac{2J_B+1}{2J_A+1} C^2S_i^+ \qquad G^- = \sum_i C^2S_i^-$$

Sum rule: $G^+ + G^- = 2j+1$ (times quenching factor $R_s$ if applied).

**Step 2: Absolute centroid energies**

$$\mathcal{E}_j^+ = -E_B(A+1) + E_j^+ \qquad \mathcal{E}_j^- = -E_B(A) - E_j^-$$

where $E_j^\pm$ are the centroids of the excited state energies weighted by SF, relative to particle threshold.

**Step 3: ESPE**

$$\epsilon_j = \frac{\mathcal{E}_j^+ G^+ + \mathcal{E}_j^- G^-}{G^+ + G^-}$$

SF-weighted average of adding and removal centroids. Reduces to:
- $\mathcal{E}_j^-$ alone when $G^+ \to 0$ (e.g. p-shell of ${}^{16}$O: can't add to filled shell)
- $\mathcal{E}_j^+$ alone when $G^- \to 0$ (e.g. sd-shell of ${}^{16}$O: nothing to remove)

---

## Example: ${}^{12}$C, $0p_{3/2}$ orbital

From ${}^{12}$C$(d,p){}^{13}$C (adding): $E^*=3.684$ MeV, $J=3/2^-$, $C^2S=0.14$ → $G^+=0.56$

From ${}^{12}$C$(p,d){}^{11}$C (removal): $E^*=0.000$, $C^2S=2.5$ + others → $G^-=2.8475$

Result: $\epsilon(0p_{3/2}) = -16.35$ MeV

| Orbital | ESPE (MeV) | WS fit (MeV) |
|---------|-----------|--------------|
| $0p_{3/2}$ | $-16.36$ | $-16.39$ |
| $0p_{1/2}$ | $-9.42$  | $-9.45$  |
| $1s_{1/2}$ | $-1.87$  | $-1.80$  |
| $0d_{5/2}$ | $-1.22$  | $-1.21$  |

ESPE agrees well with WS mean-field energies → confirms SF extracts real nuclear structure.

WS parameters (neutron mass): $V_0=-60.9$ MeV, $r_0=1.13$ fm, $a_0=0.69$ fm, $V_{SO}=32$ MeV, $r_{SO}=0.77$ fm.

---

## Why ESPE Matters

1. **ESPE = experimental mean-field energy** -- equivalent to WS potential fit to data
2. **ESPE evolution** across isotopic/isotonic chains reveals shell evolution, monopole shifts, tensor force
3. **Robust to quenching** -- $R_s$ cancels in the $G^+/G^-$ ratio → ESPE more reliable than absolute SFs
4. **Validates SF:** ESPE agrees with WS even with quenched SFs → SF is not arbitrary

---

## Assumptions

1. **All relevant states included** -- missing strength above threshold biases centroid
2. **Correct spin assignments** -- wrong $J$ → wrong $(2J_B+1)/(2J_A+1)$ weighting in $G^+$
3. **Accurate SFs** -- OMP dependence propagates into $G$, but cancels in ratio if consistent
4. **Threshold energy known** -- $S_n$ or $S_p$ from AME2020

## Further Questions

- How sensitive is ESPE to OMP choice vs individual SFs?
- For exotic nuclei with fragmented strength, how many states can realistically be measured?
- Does ESPE evolution across Sn chain (Szwec 2021) show tensor force monopole shift clearly?

## Related Notes
- `SF_Theory_SumRule.md` -- sum rule derivation
- `SF_Quenching_Review_2023.md` -- quenching discussion; ESPE mentioned in Part II
- `2021_Szwec_SnIsotopes_Occupancies.md` -- ESPE systematics in Sn chain

_Created: 2026-04-24_
