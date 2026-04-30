# HELIOS Woods-Saxon Solver Reference

**Source:** `~/digios/analysis/Woods-Saxon/`
**Author:** Ryan Tang (2019-01-31)
**Purpose:** Numerical solution of the Woods-Saxon (WS) potential to find single-particle eigen-energies and wavefunctions. Used to generate bound-state wavefunctions for DWBA calculations and to fit WS parameters to known level schemes.

---

## Physics Background

The Woods-Saxon potential with spin-orbit coupling:
```
V(r) = -V0 / (1 + exp((r-R0)/a0))
     + VSO * (l·s) * (1/r) * dVSO/dr   [spin-orbit]
     + V_Coulomb(r)                      [proton only]
```
Parameters: V0 (depth), R0 = r0 * A^(1/3) (radius), a0 (diffuseness), VSO, RSO, aSO, rc (Coulomb radius).

Eigen-energies found by RK4 integration: wavefunction diverges when energy ≠ eigenvalue → scan energy until wavefunction at large r changes sign → bisect to find eigenvalue.

---

## Core Classes

### RK4.h -- Runge-Kutta 4th Order Solver (Base)
Solves the radial Schrödinger equation numerically. `WoodsSaxon` inherits from `RKFourth`.

### WoodsSaxon (WS.h, 803 lines)
Main class. Inherits RK4.

**Key methods:**
| Method | Purpose |
|---|---|
| `SetNucleus(A, Z)` | Set target nucleus |
| `IsNeutron()` / `IsProton()` | Set particle type (sets reduced mass μ) |
| `SetWSPars(V0, r0, a0, VSO, rSO, aSO, rc)` | Set all WS parameters |
| `SetAngularMomentum(L, J)` | Set orbital L and total J for calculation |
| `CalWSEnergies(useBarrier, maxL, uTorr, eTorr, maxLoop, dKE, debug)` | Find all eigen-energies up to maxL |

**Output vectors (after CalWSEnergies):**
- `energy[]` -- eigen-energies in MeV
- `Lvalue[]` -- orbital angular momentum
- `Jvalue[]` -- total angular momentum J
- `orbString[]` -- orbital label (e.g. "0d5/2")
- `UatMaxdist[]` -- wavefunction value at boundary (should → 0 for bound states)

**Reduced radius convention:** `R0 = r0 * A^(1/3)` -- WS.h uses both R0 (absolute) and r0 (reduced); setters accept either.

---

## Programs

| Program | Source | Purpose |
|---|---|---|
| `WSCal` | (implied) | Simple single WS calculation: given V0, R0, a0 → compute level energies |
| `WSRange` | `WSRange.cpp` (272 lines) | Compute WS energies over a range of parameters (for plotting) |
| `WSCompare` | `WSCompare.cpp` (307 lines) | Compare WS levels to experimental data without parameter search |
| `WSFit` | `WSFit.cpp` (378 lines) | Fit WS parameters to match experimental levels (chi-square minimization) |
| `WSSearch` | `WSSearch.cpp` (394 lines) | Grid search over WS parameter space |
| `WSSearch2` | `WSSearch2.cpp` (440 lines) | Extended parameter search v2 |
| `WSMakeTree` | `WSMakeTree.cpp` (281 lines) | Save WS search results to ROOT TTree |
| `WSProof.C` | `WSProof.C` (299 lines) | ROOT PROOF parallel search (multi-core grid search) |

---

## Energy reference files

Pre-computed or experimental level energies for specific nuclei:

| File | Nucleus | Use |
|---|---|---|
| `energy12C.dat` | 12C | |
| `energy14C.dat` | 14C | |
| `energy15C.dat` | 15C | |
| `energy17O.dat` | 17O | |
| `energy207Hg.dat` | 207Hg | |
| `energy209Pb.dat` | 209Pb | |
| `energy211Po.dat` | 211Po | |
| `energy41Ca.dat` | 41Ca | |
| `energy49Ca.dat` | 49Ca | |

---

## LCRC Parallel Search

`ProofSlurm.sh` + `slurm.sh` -- submit WSSearch as SLURM batch jobs on LCRC cluster for large parameter space searches. `ProofWSSearch.C` / `ProofWSSearch2.C` -- ROOT PROOF versions for local multi-core.

---

## Compilation

```bash
cd ~/digios/analysis/Woods-Saxon/
make
```

Builds all programs. Requires ROOT + C++17.

---

## Use in HELIOS Analysis

1. Fit WS parameters to known experimental levels of target/residual nucleus
2. Use fitted parameters to generate single-particle wavefunctions
3. Pass wavefunctions to Ptolemy (via InFileCreator) for DWBA cross-section calculation
4. The bound-state wavefunction determines the radial integral → spectroscopic factor sensitivity

**Key:** WS parameters affect DWBA shape and normalization. Standard practice: use global optical model potentials (AK) for entrance/exit channels, and WS for bound-state wavefunctions.

---

## C++ vs Python Implementation Comparison

| Feature | `digios/Woods-Saxon/` (C++) | `codes/woods_saxon.py` (Python) |
|---|---|---|
| Integration method | RK4 (4th order) | Numerov (6th order -- more accurate) |
| Spin-orbit | Full WS+SO | Full WS+SO |
| Coulomb | Via WS.h (analytical/numerical) | From WS charge distribution (grid) |
| Coulomb energy | Not directly computed | Explicitly computed ∫\|ψ\|²V_C dr |
| Parameter fitting | WSFit/WSSearch (C2 minimization) | `adjust_V0()` (bisection for single orbital) |
| Parallel search | SLURM/PROOF multi-core | Single-threaded |
| Primary use | DWBA wavefunction generation | CDE / Coulomb energy calculation |

**When to use which:**
- Need wavefunctions for Ptolemy DWBA → use C++ `WSCal`/`WSFit`
- Need Coulomb energy of added proton (CDE analysis) → use Python `woods_saxon.py`
- Need to search WS parameter space → use C++ `WSSearch` (much faster)

## See Also

- `HELIOS_Simulation_Cleopatra.md`  --  Ptolemy/DWBA pipeline (uses WS wavefunctions as input)
- `codes/woods_saxon.py`  --  Python implementation of WS solver with Coulomb energy (Numerov method)
- `Coulomb_Displacement_Energy.md`  --  CDE theory, isospin decomposition, TBME Coulomb correction
- `HELIOS_LIB_Reference.md`  --  HELIOS_LIB.h TargetScattering (uses SRIM, separate from WS)

_Documented: 2026-04-29_
