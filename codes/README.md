# HELIOS_MD/codes/ -- Analysis Utilities

Small standalone Python scripts for nuclear structure calculations related to the HELIOS program.

---

## tbme_estimator.py

**Purpose:** Extract diagonal two-body matrix elements (TBMEs) of the residual nucleon-nucleon interaction from experimental data.

**Reference:** J.P. Schiffer & W.W. True, Rev. Mod. Phys. **48**, 191 (1976)

**Requirements:** `numpy`, `scipy`, optional `sympy` (for Pandya transform and exact angular coefficients)

```bash
python3 tbme_estimator.py
```

### Method

Based on Eq. (I.1) of Schiffer-True 1976:

```
eps(j) = B(core+j) - B(core)          [single-particle binding energy]
V_gs   = eps(j1) + eps(j2) - [B(core+2) - B(core)]   [TBME for g.s. J member]
V(J)   = V_gs + E_J(exc)              [TBME for each J member]
M0     = Σ(2J+1)*V(J) / Σ(2J+1)      [monopole = J-weighted average]
```

All binding energies from AME (positive, in MeV). Excitation energies in MeV above the two-nucleon ground state.

### Key features

- **Single excitation energies:** `excitations = {J: E_exc}` — dominant state only
- **Fragmented strength (centroid):** `excitations = {J: [(E1, C2S1), (E2, C2S2), ...]}` — computes spectroscopic-factor-weighted centroid before extracting TBME
- **Coulomb correction:** set `proton_pair = True` — uses harmonic oscillator radial wave functions (Slater integrals F^k) to compute J-dependent Coulomb correction for pp T=1 pairs. Requires `n, l, j` of the orbital and `A_coulomb`.
- **Pandya transform:** `pandya_transform(j1, j2, V_hp)` — converts hole-particle matrix elements to particle-particle via Eq. (I.2) of Schiffer-True. Requires `sympy`.
- **Monopole:** automatically computed for any set of J members provided

### Inputs to edit

In the `system` dict at the bottom of the script:

| Key | Type | Description |
|-----|------|-------------|
| `name` | str | Human-readable label |
| `j1`, `j2` | str | Orbital labels (e.g. `"1d5/2"`) |
| `T` | int | Isospin of two-nucleon state (0 or 1) |
| `B_core` | float | B(core nucleus) in MeV |
| `B_core_j1` | float | B(core + one nucleon in j1) in MeV |
| `B_core_j2` | float | B(core + one nucleon in j2) in MeV |
| `B_core_2` | float | B(two-nucleon nucleus) in MeV |
| `excitations` | dict | `{J: E_exc}` or `{J: [(E,C2S),...]}` |
| `proton_pair` | bool | Apply Coulomb correction? |
| `n1, l1, j1_val` | int,int,float | Quantum numbers for Coulomb correction |
| `A_coulomb` | int | Mass number for oscillator length |

### Example: reproducing Schiffer-True Table I

For (1d5/2)² T=1 in ¹⁸O from ¹⁷O(d,p)¹⁸O:

```
System: 16O core + two 1d5/2 neutrons -> 18O
B(16O) = 127.619 MeV
B(17O) = 131.763 MeV   => eps(d5/2) = 4.144 MeV
B(18O) = 139.808 MeV

V(0) = -3.901 MeV    [paper: -3.65 MeV -- paper uses centroid over multiple 0+ states]
V(2) = -1.919 MeV    [paper: -1.06 MeV -- paper uses centroid]
V(4) = -0.346 MeV    [paper: +0.81 MeV -- paper includes 4+ state at 7.1 MeV]
M0   = -1.107 MeV    [paper: ~-1.5 MeV]
```

Discrepancies from the paper are due to centroid averaging (multiple states with same J^pi carry partial strength). Feed in `[(E1,C2S1),(E2,C2S2),...]` lists per J to match paper results.

### Coulomb correction details

For a proton-proton T=1 pair in the same orbital (n,l,j):

```
ΔV_C(J) = e² * Σ_k  A_k(j,j,J) * F^k(nl,nl)
```

where:
- `F^k` = Slater radial integral (computed numerically with oscillator wave functions)
- `A_k` = angular coefficient from Wigner 6j + Clebsch-Gordan (requires `sympy`)
- Only even k contribute: k = 0, 2, ..., 2l

The Coulomb correction is subtracted from the raw TBME to obtain the hadronic matrix element:

```
V_hadronic(J) = V_raw(J) - ΔV_C(J)
```

### Connection to Schiffer 2022

The monopole M0 computed here is directly related to the ESPE slopes in:
J.P. Schiffer, B.P. Kay, J. Chen, Phys. Rev. C **105**, L041302 (2022)

The inset of Fig. 2 in that paper plots M0 values from the 1976 survey on the same axes as modern ESPE slopes — showing they are the same physics. The 1976 paper establishes the pattern at closed shells; the 2022 paper shows it is universal across A=16-208.

---

## woods_saxon.py

**Purpose:** Solve the radial Schrödinger equation with Woods-Saxon potential numerically. Find bound-state energies and wave functions; compute Coulomb energy of an added proton from WS charge distribution.

**Reference:** Ryan Tang's blog (nukephysik101.wordpress.com, 2020-2021); ~/HELIOS_MD/Coulomb_Displacement_Energy.md

**Requirements:** `numpy`, `scipy`, `matplotlib`

**Status:** Framework implemented. Known limitation: for deep WS wells (many bound states), the state selector needs a node counter to reliably find the physical state. The Coulomb potential precomputation and integration are correct.

### Method

```
Radial SE: d²u/dr² = f(r,E)*u(r)
f(r,E) = (2m/hbar²)*(V(r)-E) + l(l+1)/r²

V(r) = V_WS(r) + V_SO(r) [+ V_C(r) for protons]
V_WS = -V0 / (1 + exp((r-R0)/a))
V_SO = Vso*(hbar/m_pi*c)²*(1/r)*dV_WS/dr*(l·s)
```

Solve by Numerov outward integration + log-derivative matching to asymptotic exp(-kappa*r).
Adjust V0 via bisection to reproduce experimental binding energy.

### Coulomb energy

```python
E_C = integral |u(r)|^2 * V_C(r) dr
```

where V_C(r) is computed from a normalized WS charge distribution (not uniform sphere).
Both WS and uniform sphere results are printed for comparison.

### Key functions

| Function | Description |
|---|---|
| `R_osc(r, n, l, b)` | Harmonic oscillator radial wave function (for comparison) |
| `oscillator_length(A)` | Compute b [fm] from standard hbar*omega formula |
| `precomputed_coulomb_potential(Z, R0, a)` | V_C(r) grid from WS charge distribution |
| `numerov_outward(r, f)` | Numerov integrator (O(h^6)) |
| `find_bound_state(...)` | Find bound state energy + wave function |
| `adjust_V0(target_E, ...)` | Find V0 to reproduce binding energy |
| `coulomb_energy_WS(u, r, Z, R0, a)` | Coulomb energy from WS charge |
| `pandya_transform(j1, j2, V_hp)` | Hole-particle -> particle-particle (in tbme_estimator.py) |

---

_Created: 2026-04-29 | Author: Master HELIOS_
