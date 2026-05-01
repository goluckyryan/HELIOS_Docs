# Raphael -- Python DWBA Implementation

**Location:** `~/PtolemyGUI/Raphael/`
**Author:** Ryan Tang
**Reference:** https://nukephysik101.wordpress.com/2025/02/21/handbook-of-direct-nuclear-reaction-for-retarded-theorist-v1/
**Status:** Research/development -- functional for (d,p)/(p,d) ZR-DWBA, not production-ready

---

## Motivation

Modern Python implementation of Distorted Wave Born Approximation for direct nuclear reactions. Motivation:
1. Ryan's curiosity and learning
2. All existing DWBA codes (Ptolemy, FRESCO, DWUCK4) are Fortran-based, some non-compilable, all with "messy input cards"

---

## Architecture (2152 total lines)

### Foundation layer

| Module | Lines | Purpose |
|---|---|---|
| `assLegendreP.py` | ~36 | Associated Legendre polynomials (positive m) |
| `clebschGordan.py` | 205 | Custom CG coefficients (faster than sympy) |
| `opticalPotentials.py` | 202 | OM potentials: An & Cai (deuteron) + Kronning (proton) |
| `reactionData.py` | 184 | Reaction data storage (masses, kinematics) |
| `coulombWave.py` | 55 | Coulomb wave functions (via mpmath) |

### Physics layer

| Module | Lines | Purpose |
|---|---|---|
| `solveSE.py` | 333 | **Core:** `PotentialFrom` base class (WS, WS_Surface, SO, Coulomb); `SolveSE` class (mass from IAEA, kinematics, radial wavefunction) |
| `boundState.py` | 155 | Bound-state wavefunction (inherits `SolveSE`) |
| `distortedWave.py` | 322 | Distorted wave + scattering matrix; elastic dσ/dΩ (ratio to Rutherford) |

### DWBA layer

| Module | Lines | Purpose |
|---|---|---|
| `dwba_zr.py` | 566 | **Main:** Zero-Range DWBA class -- radial integral + angular summation → dσ/dΩ for transfer |
| `DWBA.py` | 94 | Example/driver script |

### External dependency
- `../Cleopatra/IAEANuclearData.py` -- nuclear mass + spin-parity lookup (IAEA database)

---

## Usage (from DWBA.py examples)

```python
from dwba_zr import DWBA_ZR

# 16O(d,p)17O -- transfer to 1s1/2 ground state
haha = DWBA_ZR("16O", "d", "p", "17O", "1/2+", "1s1/2", 0.0, 10)

haha.FindBoundState()           # solve bound-state WF
haha.CalRadialIntegral()        # precompute ZR radial integral
haha.CalAngDistribution(0, 180, 1)  # angular dist, step=1 deg
haha.PlotAngDist()              # display result
```

---

## `DWBA_ZR.__init__` -- Initialization Chain

When `DWBA_ZR("16O", "d", "p", "17O", "1/2+", "1s1/2", 0.0, 10)` is called:

1. `ReactionData` -- parses nuclei, looks up masses (IAEA), computes kinematics (Q, ELab, Eout)
2. `BoundState(A_c, Z_c, A_x, Z_x, node, l, j, BindingEnergy)` -- WS bound state with default params `(r0=1.10, a=0.65, VSO=-6, rSO=1.25, aSO=0.65, rc=1.30)`
3. **Incoming wave (d channel):** An-Cai potential (`op.AnCai`) → `DistortedWave` with WS + WS_Surface + SpinOrbit + Coulomb
4. **Outgoing wave (p channel):** Koning potential (`op.Koning`) → `DistortedWave` same structure
5. Precompute: `PreCalClebschGordan()`, `PreCalNineJ()` (via sympy)

**Default OM potentials:** An-Cai (deuteron) + Koning (proton) -- same physics as digios AK standard!

## Zero-Range DWBA Algorithm (`dwba_zr.py`)

1. **Kinematics:** compute Ecm, k_in, k_out from masses and lab energy
2. **Bound state:** solve Schrödinger for transferred nucleon in WS potential (`boundState.py`)
3. **Distorted waves:** solve Schrödinger for entrance (d) and exit (p) channels in their respective OM potentials (`distortedWave.py`)
4. **Radial integral:** precompute `I(r) = u_bound(r) * χ†_out(r) * χ_in(r)` on radial grid
5. **Angular summation:** sum over partial waves (l, lz, j, jz, L, M) with CG + 9j coefficients via sympy `wigner_9j`
6. **Cross section:** `dσ/dΩ = (μ_in μ_out)/(ℏ⁴) * |T_fi|² * k_out/k_in`

**Optimization:** radial integral, associated Legendre P, CG coefficients, 9j symbols all **precomputed** (not recomputed per angle).

---

## Performance

| Orbital | Time |
|---|---|
| s-orbital (l=0) | ~10 seconds |
| d-orbital (l=2) | ~30 seconds |

Pure Python, no C extension or GPU acceleration. For comparison, Ptolemy (Fortran) takes ~1 second.

---

## Potential Implementations (`solveSE.py`)

All potentials implement `PotentialForm` base class with `output(r)` method. `setAa(A,a)` sets `R0 = r0*(A^(1/3) + a^(1/3))` (sum-of-radii convention for scattering).

| Class | Formula | Notes |
|---|---|---|
| `WoodsSaxonPot(V0, r0, a)` | `-V0/(1+exp((r-R0)/a))` | Real or complex V0 |
| `SpinOrbit_Pot(VSO, rSO, aSO)` | `4*VSO*exp/[a*(1+exp)²*r]` (Thomas form) | LS factor applied in `SolvingSE` |
| `WS_SurfacePot(V0, r0, a)` | `4*V0*exp/(1+exp)²` | Derivative of WS -- imaginary surface absorption |
| `CoulombPotential(rc)` | `Zq/2R*(3-(r/R)²)` inside, `Zq/r` outside | Uniform sphere, `ee=1.43996 MeV·fm` |

**Radial grid:** `rStart=0, dr=0.05 fm, nStep=3000` (150 fm total) -- sufficient for nuclear + Coulomb asymptotic region.

## Requirements

```
numpy, scipy (gamma, curve_fit, interp1d, simpson)
matplotlib
mpmath (coulombf, coulombg, whittaker)
sympy (wigner_9j)
```

---

## Current Limitations

- **Zero-range only** (no finite-range) -- angular distributions agree with experiment at this level
- **Single-nucleon transfer only** -- (d,p), (p,d); not yet (p,t), (d,α), etc.
- **No inelastic scattering** (yet)
- **No polarization**
- **No coupled channels**
- Performance: Python-speed (~30s for d-orbital); C++ version planned

## Comparison to Ptolemy

| Feature | Raphael (Python) | Ptolemy (Fortran) |
|---|---|---|
| Language | Python 3 | Fortran (1978) |
| ZR-DWBA | ✓ | ✓ |
| Finite-Range | ✗ | ✓ |
| Speed (d-orbital) | ~30s | ~1s |
| Input format | Python API | Text input cards |
| Maintainability | High | Low (legacy Fortran) |
| Status | Development | Production |

---

## See Also

- `HELIOS_Simulation_Cleopatra.md` -- Ptolemy-based production DWBA pipeline
- `HELIOS_WoodsSaxon.md` -- WS bound-state solver (C++ and Python)
- `paper_notes/DWBA_ZR_Mathematics_Reference.md` -- mathematical foundations of ZR-DWBA
- `Coulomb_Displacement_Energy.md` -- Coulomb wave functions (related physics)

---

_Documented: 2026-04-30_
