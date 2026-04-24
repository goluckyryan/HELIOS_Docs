# Spectroscopic Factor Theory -- Sum Rule

**Source:** https://nukephysik101.wordpress.com/2019/04/07/spectroscopic-factor-revisit/  
**Based on:** Glendenning "Direct Nuclear Reactions" Ch. 7  
**Read:** 2026-04-24

---

## Simple Picture (2016 post)

**Source:** https://nukephysik101.wordpress.com/2016/05/05/spectroscopic-factor-occupation-number/

Start from independent particle model. Nucleus A wavefunction decomposed as:

    |Ψ_A⟩ = Σ β_ij [ |φ_i⟩ |Φ_B⟩_j ]_J

where φ_i = single particle orbital, Φ_B = core (B=A-1) wavefunction.

- **β_ij** = spectroscopic amplitude
- **SF = |β_ij|² × n_i** = spectroscopic factor (probability nucleus looks like core B_j + nucleon in orbital i)
- **Occupation number** = Σ_j SF = sum over all core states

When nucleon-core interaction = 0: SF = 1, occupation = 1 (pure single-particle).

When off-diagonal terms exist (configuration mixing):
- Mixing spreads strength across states → SF of individual state < 1
- Sum rule still holds (unitarity of β matrix)
- In 2-state degenerate system: SF of lower state decreases as mixing increases
- Key: **configuration mixing ≠ quenching** (sum rule preserved), but it fragments strength

**[!!] Note (2024 update):** The simple β² × n definition above is an ad hoc construct. The correct relation between SF and occupation number is via the sum rule derivation (see below and `SF_Theory_SumRule.md`).

---

## Full Derivation (from LaTeX source, Glendenning Ch.7)

**Step 1:** Spectroscopic amplitude β from projection onto CG-coupled states:
```
β_nlj(B,A) = Σ_{m_A,m} C^{J_B m_B}_{J_A m_A j m} ⟨J_B m_B | a†_nljm | J_A m_A⟩
```

**Step 2:** Wigner-Eckart theorem -- a†_nljm is a spherical tensor of rank j, component m:
```
⟨J_B m_B | a†_nljm | J_A m_A⟩
  = [(-1)^{J_B-m_B}/√(2J_B+1)] (J_B j J_A; -m_B m m_A) ⟨J_B||a†||J_A⟩
```
All m-dependence factored into the 3j symbol; ⟨J_B||a†||J_A⟩ is the reduced matrix element (m-independent).

Then reorder 3j columns using symmetry property: (J_B j J_A; -m_B m m_A) = (-1)^{J_B+j+J_A} (J_A j J_B; m_A m -m_B)
→ picks up phase (-1)^{-m_B-J_A-j}.

Substitute back into β expression. The two phase factors combine as (-1)^{J_A-J+m_B} × (-1)^{-m_B-J_A-j} = (-1)^{-2J}:
```
β_nlj(B,A) = Σ_{m_A,m} (-1)^{-2J} √(2J_B+1) (J_A j J_B; m_A m -m_B)² ⟨J_B||a†||J_A⟩
```

**Step 3:** 3j orthogonality identity:
```
Σ_{m_A,m} (J_A j J_B; m_A m -m_B)² = 1/(2J_B+1)
```
This kills the sum:
```
β_nlj(B,A) = [(-1)^{2J}/√(2J_B+1)] ⟨J_B||a†||J_A⟩
```

**Step 4:** Invert to get matrix element in terms of β, multiply by adjoint, sum over m_B,m, insert completeness Σ_{J_B,m_B}|J_B m_B⟩⟨J_B m_B| = 1:
```
Σ_{J_B} (2J_B+1)/(2J_A+1) β²_nlj(B,A) = ⟨J_A m_A | Σ_m a_nljm a†_nljm | J_A m_A⟩
```

**Step 5:** Anticommutation relation for fermion operators:
```
a_nljm a†_nljm = 1 - a†_nljm a_nljm
```
So the RHS becomes:
```
Σ_m ⟨J_A | a_nljm a†_nljm | J_A⟩ = (2j+1) - ⟨J_A | Σ_m a†_nljm a_nljm | J_A⟩
                                    = (2j+1) - n_nlj(A)
```
where n_nlj(A) = occupation number of orbital nlj in nucleus A.

---

## Key Result

For A(d,p)B (adding) reaction, summing over all final states j,m of B:

    Σ C²S(nlj) = N_nlj(A)

where N_nlj(A) = number of neutrons in orbital nlj in nucleus A.

For B(p,d)A (removing) reaction, summing over all final states of A:

    Σ C²S(nlj) = 2j+1 - N_nlj(B)  [i.e. number of holes in nlj in B]

Combined sum rule (adding + removing from nucleus A):

    Σ_add + Σ_remove = 2j+1

This is the **fundamental sum rule**: the total strength (adding + removing) must equal the shell degeneracy.

---

## Derivation Key Steps

1. **Wavefunction:** B = A+1 nucleus written as antisymmetrized product of core A + single nucleon, with CG coefficient from angular coupling. The square root of SF enters naturally from the normalization.

2. **SF extraction:** Integrate out core A → reduced matrix element → Wigner-Eckart theorem → SF as squared reduced matrix element.

3. **Sum rule:** Sum over all final states (exhaust completeness), use CG orthogonality → result is just the occupation number N_nlj.

---

## Physical Meaning

- **C²S** (or SF) = probability that nucleus B looks like nucleus A + one nucleon in orbital nlj
- SF = 1.0 → pure single-particle state (ideal shell model)
- SF < 1.0 → fragmented strength (configuration mixing, correlations)
- **Quenching:** experimentally, Σ C²S from (d,p) + (p,d) is consistently ~60-70% of 2j+1 (sum rule). Missing ~30-40% attributed to short-range correlations, SRC. This is the "quenching puzzle."

---

## Connection to HELIOS Analysis

- Experimental SF: C²S = σ_exp / σ_DWBA (where σ_DWBA is calculated with SF=1)
- σ_DWBA comes from Ptolemy/PtolmeyCpp
- σ_exp is the measured integrated cross section (from angular distribution)
- The isospin factor C² is often folded in: C²S = C² × S, where C² from isospin CG

---

## Assumptions (critical)

1. **DWBA validity** -- assumes one-step transfer dominates; breaks down at low energy or for tightly-bound states
2. **OMP accuracy** -- σ_DWBA depends on incoming/outgoing optical model potentials; different OMPs give different σ_DWBA → different SF
3. **Bound state geometry** -- r₀, a of the bound state WF enters the radial integral; conventionally r₀=1.25, a=0.65 but this is a choice
4. **Single-step assumption** -- no multistep, no core excitation during transfer
5. **The sum rule is exact in the independent-particle model** -- correlations violate it, which is exactly what quenching measures

## Further Questions

- How sensitive is the extracted SF to OMP choice in practice? (Kay 2013 addresses this)
- Is the quenching universal or does it depend on Δ_S (separation energy asymmetry)? (Controversial -- see Jiang 2025)
- For HELIOS experiments: what fraction of the sum rule is typically recovered across all observed states?

_Created: 2026-04-24. Source: nukephysik101.wordpress.com (Ryan's blog, based on Glendenning Ch.7)_
