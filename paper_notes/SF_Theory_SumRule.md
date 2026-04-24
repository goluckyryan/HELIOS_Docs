# Spectroscopic Factor Theory -- Sum Rule

**Source:** https://nukephysik101.wordpress.com/2019/04/07/spectroscopic-factor-revisit/  
**Based on:** Glendenning "Direct Nuclear Reactions" Ch. 7  
**Read:** 2026-04-24

---

## Simple Picture (2016 post)

**Source:** https://nukephysik101.wordpress.com/2016/05/05/spectroscopic-factor-occupation-number/

Start from independent particle model. Nucleus A wavefunction decomposed as:

$$|\Psi_A\rangle = \sum_{ij} \beta_{ij} \left[ |\phi_i\rangle |\Phi_B\rangle_j \right]_J$$

where $\phi_i$ = single particle orbital, $\Phi_B$ = core (B=A-1) wavefunction.

- $\beta_{ij}$ = spectroscopic amplitude
- $\text{SF} = |\beta_{ij}|^2 \times n_i$ = spectroscopic factor
- **Occupation number** $= \sum_j \text{SF}$ = sum over all core states

When nucleon-core interaction = 0: SF = 1, occupation = 1 (pure single-particle).

When off-diagonal terms exist (configuration mixing): mixing spreads strength across states → SF of individual state < 1, but sum rule preserved (unitarity of $\beta$ matrix).

**[!!] Note (2024 update):** The simple $\beta^2 \times n$ definition above is an ad hoc construct. The correct relation is via the sum rule derivation below.

---

## Full Derivation (from LaTeX source, Glendenning Ch.7)

**Step 1:** Spectroscopic amplitude $\beta$ from projection onto CG-coupled states:

$$\beta_{nlj}(B,A) = \sum_{m_A,m} C^{J_B m_B}_{J_A m_A j m} \langle J_B m_B | a^\dagger_{nljm} | J_A m_A \rangle$$

**Step 2:** Wigner-Eckart theorem -- $a^\dagger_{nljm}$ is a spherical tensor of rank $j$, component $m$:

$$\langle J_B m_B | a^\dagger_{nljm} | J_A m_A \rangle = \frac{(-1)^{J_B-m_B}}{\sqrt{2J_B+1}} \begin{pmatrix} J_B & j & J_A \\ -m_B & m & m_A \end{pmatrix} \langle J_B \| a^\dagger \| J_A \rangle$$

All $m$-dependence factored into the 3j symbol; $\langle J_B \| a^\dagger \| J_A \rangle$ is the reduced matrix element ($m$-independent).

Reorder 3j columns: $(J_B\ j\ J_A;\ {-m_B}\ m\ m_A) = (-1)^{J_B+j+J_A}(J_A\ j\ J_B;\ m_A\ m\ {-m_B})$, picking up phase $(-1)^{-m_B-J_A-j}$.

The two phase factors combine as $(-1)^{J_A-J+m_B} \times (-1)^{-m_B-J_A-j} = (-1)^{-2J}$:

$$\beta_{nlj}(B,A) = \sum_{m_A,m} (-1)^{-2J} \sqrt{2J_B+1} \begin{pmatrix} J_A & j & J_B \\ m_A & m & -m_B \end{pmatrix}^2 \langle J_B \| a^\dagger \| J_A \rangle$$

**Step 3:** 3j orthogonality identity:

$$\sum_{m_A,m} \begin{pmatrix} J_A & j & J_B \\ m_A & m & -m_B \end{pmatrix}^2 = \frac{1}{2J_B+1}$$

This kills the sum:

$$\beta_{nlj}(B,A) = \frac{(-1)^{2J}}{\sqrt{2J_B+1}} \langle J_B \| a^\dagger \| J_A \rangle$$

**Step 4:** Invert to express matrix element in terms of $\beta$, multiply by adjoint, sum over $m_B, m$, insert completeness $\sum_{J_B,m_B}|J_B m_B\rangle\langle J_B m_B| = 1$:

$$\sum_{J_B} \frac{2J_B+1}{2J_A+1} \beta^2_{nlj}(B,A) = \langle J_A m_A | \sum_m a_{nljm} a^\dagger_{nljm} | J_A m_A \rangle$$

**Step 5:** Anticommutation relation for fermion operators:

$$a_{nljm} a^\dagger_{nljm} = 1 - a^\dagger_{nljm} a_{nljm}$$

So the RHS becomes:

$$\sum_m \langle J_A | a_{nljm} a^\dagger_{nljm} | J_A \rangle = (2j+1) - \langle J_A | \sum_m a^\dagger_{nljm} a_{nljm} | J_A \rangle = (2j+1) - n_{nlj}(A)$$

where $n_{nlj}(A)$ = occupation number of orbital $nlj$ in nucleus $A$.

---

## Key Result

**Adding** $A(d,p)B$, sum over all final states $J_B$:

$$\sum_{J_B} \frac{2J_B+1}{2J_A+1} \beta^2_{nlj}(B,A) = 2j+1 - n_{nlj}(A)$$

**Removing** $B(p,d)A$, sum over all final states $J_A$:

$$\sum_{J_A} \beta^2_{nlj}(B,A) = n_{nlj}(B)$$

**Combined sum rule** (adding + removing from nucleus $A$):

$$\sum_{J_B} \frac{2J_B+1}{2J_A+1} \beta^2(B,A) + \sum_{J_C} \beta^2(A,C) = 2j+1$$

Total strength (adding + removing) = shell degeneracy $2j+1$. Exact in the independent-particle model.

---

## Physical Meaning

- $C^2S$ = probability that nucleus $B$ looks like core $A$ + one nucleon in orbital $nlj$
- SF = 1.0 → pure single-particle; SF < 1.0 → fragmented (mixing, correlations)
- **Quenching:** $\sum C^2S \approx 0.6$–$0.7 \times (2j+1)$ experimentally. Missing ~30–40% from short-range correlations (SRC).

---

## Connection to HELIOS Analysis

$$C^2S = \frac{\sigma_\text{exp}}{\sigma_\text{DWBA}(C^2S=1)}$$

- $\sigma_\text{DWBA}$ from Ptolemy/PtolmeyCpp
- $\sigma_\text{exp}$ from measured angular distribution (integrated)
- Isospin factor: $C^2S = C^2 \times S$, where $C^2$ from isospin CG coefficients

---

## Assumptions

1. **DWBA validity** -- one-step transfer dominates
2. **OMP accuracy** -- different OMPs → different $\sigma_\text{DWBA}$ → different SF
3. **Bound state geometry** -- $r_0, a$ of bound state WF enter radial integral ($r_0=1.25$, $a=0.65$ conventional)
4. **Single-step** -- no multistep, no core excitation
5. **Sum rule exact in IPM** -- correlations violate it → quenching

## Further Questions

- How sensitive is extracted SF to OMP choice? (Kay 2013 addresses this)
- Is quenching universal or $\Delta_S$-dependent? (See Jiang 2025, Kay 2022)
- What fraction of sum rule is recovered across HELIOS experiments?

_Created: 2026-04-24. Source: nukephysik101.wordpress.com (Ryan's blog, Glendenning Ch.7)_
