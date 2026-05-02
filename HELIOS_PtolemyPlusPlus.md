# Ptolemy++ -- C++ DWBA Nuclear Reaction Code

**Location:** `~/Ptolemy_AI/`
**Author:** Ryan Tang
**Binary:** `~/Ptolemy_AI/ptolemy++`
**Status:** Production-quality -- validated to <0.01% vs Fortran Ptolemy for DWBA

---

## What It Is

A C++ translation/reimplementation of the Fortran [Ptolemy](https://www.phy.anl.gov/theory/research/ptolemy/) DWBA code (Macfarlane & Pieper, ANL-76-11, 1978). Computes differential cross sections for:
- **Elastic scattering** (optical model)
- **DWBA transfer reactions** (d,p), (d,n), (p,d)

---

## Validation

| Comparison | Result |
|---|---|
| Elastic vs Raphael (Python) | < 0.15% at all angles |
| Elastic vs Fortran Ptolemy | < 1.5% at forward angles |
| DWBA vs Fortran Ptolemy | **0.01% mean DCS error** (206Hg benchmark) |

---

## Features

### Elastic Scattering ✅
- Spin-0, 1/2, 1 projectiles (α, p/n, d/t/³He)
- Full OM potential: WS + surface + spin-orbit + Coulomb
- Output: dσ/dΩ(θ), σ/σ_Ruth (Rutherford ratio), total reaction σ, S-matrix (|S_LJ|, phase)
- Validated against Raphael Python and Fortran Ptolemy

### DWBA Transfer Reactions ✅
- Single-step (d,p), (d,n), (p,d)
- AV18 deuteron bound-state wavefunction
- Target bound state: automatic WS depth search with spin-orbit
- Distorted waves: Numerov integration + Coulomb matching
- Radial integrals: GRDSET/InelDc (3D grid, faithful Fortran translation)
- SFROMI transfer S-matrix with 9J coupling
- XSECTN differential cross sections (CM frame)

### Known Limitations
- Single-step only (no coupled channels, no multi-step)
- CM frame output only (no lab-frame Jacobian yet)
- No tensor analyzing powers (elastic)
- Relativistic vs non-relativistic kinematics difference vs Fortran: ~1% at forward angles
- **Elastic solver: no epsilon algorithm** (Wynn/Shanks acceleration) -- causes poor convergence at backward angles (θ > 90°). Fortran Ptolemy has this; C++ implementation pending. For HELIOS (forward angles θ_CM < 50°), this is not an issue.

---

## Codebase (16,500 lines total)

### Source structure (`src/`)

| File | Lines | Purpose |
|---|---|---|
| `dwba/grdset_ineldc_faithful.cpp` | 2393 | **Core:** radial integral grid (GRDSET) + InelDc -- faithful C++ translation of Fortran |
| `dwba/ineldc.cpp` | 1786 | Inelastic/distorted wave coupling integrals |
| `dwba/coulin.cpp` | 886 | Coulomb + nuclear wave function matching |
| `dwba/bound.cpp` | 847 | Bound-state wavefunction calculation |
| `input/Potentials.cpp` | 732 | OM potential evaluation (WS, SO, Coulomb, surface) |
| `input/PtolemyParser.cpp` | 681 | Ptolemy input file parser (reads standard .in format) |
| `dwba/xsectn.cpp` | 677 | Cross-section computation (XSECTN) |
| `dwba/wavelj.cpp` | 549 | Distorted waves per (L,J) |
| `elastic/elastic.cpp` | 540 | Elastic scattering S-matrix |
| `dwba/rcwfn.cpp` | 444 | Regular + irregular Coulomb wave functions |
| `dwba/setup.cpp` | 439 | Reaction setup (kinematics, channel parameters) |
| `dwba/wavelj_ZR.cpp` | 344 | Zero-range distorted waves |
| `dwba/ineldc_zr.cpp` | 320 | Zero-range InelDc |
| `include/ptolemy_mass_table.h` | 3209 | AME mass table (header-only) |

---

## Build

```bash
cd ~/Ptolemy_AI/
make          # builds ptolemy++ binary
```
Requires: C++17, no external dependencies. Optional: gfortran (for reference Fortran binary comparison).

---

## Usage

Same input format as Fortran Ptolemy:
```bash
./ptolemy++ < reaction.in > reaction.out
```

Input file format identical to Ptolemy (GRDSET, InelDc namelist cards).

**[!!] r0target convention:** Always specify `r0target` in PARAMETERSET when using Cleopatra-generated inputs. Cleopatra always writes `r0target` (radius = r0 × A_target^(1/3)). Without it, Ptolemy uses R0DEFAULT (sum-of-radii), giving different cross sections for heavy projectiles. For (d,p) this makes no difference (A_d=2), but always include it for consistency.

```
PARAMETERSET dpsb r0target lstep=1 lmin=0 lmax=40 asymptopia=30
```

---

## Documentation (`~/Ptolemy_AI/docs/`)

| File | Lines | Contents |
|---|---|---|
| `PTOLEMY_CODE_MAP.md` | 321 | **Subroutine map + full math reference**: CONTRL→DATAIN→BOUND→WAVSET→GRDSET→INELDC→SFROMI→XSECTN flow, all formulas (SFROMI, BETCAL, A12, CUBMAP), reference kinematics for 16O(d,p)17O |
| `PTOLEMY_MANUAL.md` | 934 | Full user manual (input card format, all keywords, examples) |
| `PTOLEMY_THEORY.md` | 645 | Theoretical background (DWBA derivation, ZR vs FR) |
| `PTOLEMY_INELASTIC.md` | 844 | Inelastic scattering extension |
| `PTOLEMY_OUTPUT.md` | 508 | Output format reference |
| `EPSILON_ALGORITHM.md` | 249 | Numerical epsilon/convergence algorithm |

**Key formula from CODE_MAP.md:**
```
SFROMI = FACTOR × ATERM × i^(Li+Lo+2Lx+1) / √(2Li+1) × I(Li,Lo,Lx)
FACTOR = 2√(k_a·k_b / Ecm_a·Ecm_b)
```

**[!!] VSO deuteron convention (from MANUAL §11.1):** Ptolemy divides L·S coupling by 2S (doubled spin). For deuterons (S=1), VSO is effectively halved. Published AK parametrizations have this baked in — do NOT double-correct.

## Additional Files

| File/Dir | Contents |
|---|---|
| `bound_state_sensitivity_report.md` | WS bound-state sensitivity analysis |
| `bound_state_sweep.py` | Python script to sweep WS parameters |
| `bound_state_sweep_results.csv` | Parameter sweep results |
| `data/` | Benchmark/test data |
| `docs/` | Documentation |
| `fortran/` | Reference Fortran Ptolemy source |
| `compare64/` | 64-bit comparison utilities |
| `mass_lookup.cpp` | Mass table lookup utility |

---

## Zero-Range vs Finite-Range (from PTOLEMY_THEORY.md §5)

| Aspect | Zero-Range (Raphael/DWUCK4) | Finite-Range (Ptolemy/Ptolemy++) |
|---|---|---|
| Integral | 1D radial | 2D radial + angular |
| Projectile structure | Point (D₀δ) | Full φ_P(r) wavefunction |
| Computational cost | N_r | N_r² × N_θ |
| Recoil effects | Approximate | Exact |
| Accuracy for (d,p) | **10-30% off** | Correct |

**For HELIOS (d,p) reactions: always use finite-range (Ptolemy++)**, not zero-range approximation.

## Relationship to Other DWBA Tools

| Tool | Language | Type | Status | Location |
|---|---|---|---|---|
| **Ptolemy++** | C++ | FR-DWBA | Production (<0.01% error) | `~/Ptolemy_AI/` |
| Fortran Ptolemy | Fortran | FR-DWBA | Legacy reference | `~/PtolemyGUI/fortran/` |
| **Raphael** | Python | ZR-DWBA | Development (~30s/calc) | `~/PtolemyGUI/Raphael/` |
| FRESCO | Fortran | CC+DWBA | External | `/usr/local/bin/fresco` |
| DWUCK4 | Fortran | ZR-DWBA | Legacy | `~/PtolemyGUI/dwuck4/` |

**Ptolemy++ is the preferred modern replacement for Fortran Ptolemy for HELIOS analysis.**

---

## Reading Ptolemy Output (from PTOLEMY_OUTPUT.md)

Key output columns in the angular distribution table:

| Column | Meaning |
|---|---|
| **C.M. ANGLE** | CM scattering angle θ (degrees) |
| **C.M. MB** | Transfer dσ/dΘ (mb/sr) -- **the main result** |
| **/RUTH** | Transfer dσ/dΘ / Rutherford |
| HIGH L % ERROR | Estimated truncation error from L > Lmax |
| Lx = N columns | DCS by transferred L -- shows which L dominates |

**TOTAL:** = integrated transfer σ (mb)

**Bound state depth search:** If V is not fixed, Ptolemy iterates V until correct B.E. + node count. Lines: `FOR V = XX, E = YY, WAVEFUNCTION HAS N NODES BUT M ARE DESIRED. WILL TRY A NEW V:`

**Full output guide:** `~/Ptolemy_AI/docs/PTOLEMY_OUTPUT.md` (508 lines)

---

## Bound State Sensitivity Study (2026-04-27)

**Source:** `~/Ptolemy_AI/bound_state_sensitivity_report.md`
**Reaction:** ³⁰Si(d,p)³¹Si g.s., 10 MeV/u, AK potentials, 42 (r0,a) combinations

### Key Result

The single-particle DWBA cross section σ_sp is **extremely sensitive** to the bound-state geometry (r0, a, V₀):

| r0 change | σ_DWBA change | SF_extracted change |
|---|---|---|
| 1.25 → 1.30 (Δr0=+0.05) | −65% | **+186%** |
| 1.25 → 1.20 (Δr0=−0.05) | +146% | **−60%** |
| a: 0.65 → 0.70 | −15% | +18% |

**Bottom line: choosing r0=1.20 vs r0=1.30 changes the extracted SF by nearly a factor of 3.**

### Why so large?

σ_DWBA ∝ |ANC|² (asymptotic normalization) in the peripheral regime. Changing r0 by 0.05 fm shifts the nuclear surface by ΔR = 0.05 × A^(1/3) ≈ 0.16 fm. The direct tail suppression (exp(-2κΔR) with κ=0.554 fm⁻¹ for B=6.587 MeV) gives ~29%, but the V₀ refit amplifies this to ~65% because a larger R requires a smaller V₀, further reducing the surface wavefunction amplitude.

### Recommendations for HELIOS Analysis
1. **r0=1.25, a=0.65 is the standard convention** (consistent with Kay, Tang HELIOS papers)
2. **Quote as systematic:** SF ± (r0 uncertainty) using r0=1.20–1.30 range
3. **ANC constraint:** if experimental ANC is available, it constrains valid (r0,a,V₀)
4. **r0=1.10 unreliable** (severe grid clipping) -- avoid extrapolating below r0=1.20

### Sweep files
- `~/Ptolemy_AI/bound_state_sweep_results.csv` -- full 42-point (r0,a) grid
- `~/Ptolemy_AI/bound_state_sweep.py` -- sweep script

---

## See Also

- `HELIOS_Simulation_Cleopatra.md` -- digios Cleopatra/Ptolemy pipeline (uses Fortran Ptolemy or Ptolemy++)
- `HELIOS_Raphael_DWBA.md` -- Python ZR-DWBA (Ryan's development implementation)
- `HELIOS_WoodsSaxon.md` -- WS bound-state solver (C++ digios)
- `paper_notes/DWBA_ZR_Mathematics_Reference.md` -- mathematical foundations

---

_Documented: 2026-05-01_
