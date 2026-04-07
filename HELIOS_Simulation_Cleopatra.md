# HELIOS Cleopatra Simulation Reference

**Source:** Mac2020 `~/digios/analysis/Cleopatra/`
**Generated:** 2026-03-12
**Author:** Ryan (Tsz Leung) Tang (goluckyryan@gmail.com)

---

## Overview

Cleopatra is the simulation framework for HELIOS. It has two main components:

| Program | Purpose |
|---|---|
| `Cleopatra` | DWBA cross-section calculator — wraps `ptolemy` for (d,p), (p,d), (p,p), (d,d) |
| `Transfer` | Monte Carlo simulation of transfer reaction kinematics in HELIOS geometry |

**Workflow:**
```
reactionConfig.txt + detectorGeo.txt + Ex.txt
         ↓
  [Cleopatra] → DWBA.root (thetaCM distributions)
         ↓
  [Transfer]  → transfer.root (kinematic lines + simulated events)
         ↓
  Monitors.C / Cali_compareF.C (overlay with data)
```

---

## Input Files (all experiment-specific, in `working/`)

### `reactionConfig.txt`
Defines the reaction: beam, target, light recoil, energy, target properties, SRIM files
```
beam_A, beam_Z, target_A, target_Z, recoil_light_A, recoil_light_Z
beam_energy [MeV/u], sigma, angle [mrad], emittance
beam_offset_x, beam_offset_y [mm]
numEvents
isTargetScattering, density [g/cm3], thickness [cm]
SRIM files: beam, light recoil, heavy recoil
isDecay, decayNucleus_A, decayNucleus_Z
isRedo, excitation_energy_of_A
```

### `detectorGeo.txt`
Physical geometry of the spectrometer:
```
Bfield [T]         → magnetic field (negative = pointing upstream)
bore [mm]          → solenoid bore diameter
distance_from_axis → detector radius from beam axis [mm]
width [mm]         → detector width
length [mm]        → detector length
recoil_position    → recoil detector z-position [mm] (+ = downstream)
recoil inner/outer radius [mm]
isCoincidentWithRecoil
recoilPos1, recoilPos2  → extra recoil positions (0 = disabled)
elumPos1, elumPos2      → ELUM positions (0 = disabled)
blocker_length [mm]
firstPos [mm]      → first detector position (+ = upstream from target, - = downstream)
energy_resolution [MeV]
position_resolution [mm]
facing Out/In
nDet               → number of detectors at different positions (per side)
detector positions [mm] (one per line, relative to firstPos)
```

### `Ex.txt`
List of excitation energy levels to simulate:
```
Ex[MeV]   Xsec   SF   Width[MeV]
0.000     1.0    1.0  0.000
1.554     0.5    0.3  0.010
...
#===== end of file
```

---

## `Cleopatra` — DWBA Calculator

**Usage:**
```bash
./Cleopatra input_file [angMin angMax [angStep]]
```

**Pipeline:**
1. Reads reaction definition file (similar format to `reactionConfig.txt`)
   - Format: `206Hg(d,p)207Hg(1s1/2 0.000) 10MeV/u AK`
   - Optical potential keywords: `AK`, etc. (see `InFileCreator.h`)
2. Generates Ptolemy input file (`input_file.in`) via `InFileCreator`
3. Runs `./ptolemy < input_file.in > input_file.out`
4. Extracts cross-sections via `ExtractXSec`
5. Saves: `input_file.root`, `input_file.txt`
6. Plots result via `PlotTGraphTObjArray`

**Key binaries:**
- `ptolemy` — DWBA code (compiled locally)
- `dwuck4` — alternative DWBA code
- `DWInFileCreator` — creates Ptolemy input files

**Output:** `DWBA.root` with `pList` TObjArray of TF1 distributions (one per state)

---

## `Transfer` — Monte Carlo Simulation

**Usage:**
```bash
./Transfer [reactionConfig.txt detectorGeo.txt Ex.txt DWBA.root transfer.root reaction.dat plot]
```

All arguments are optional — defaults to filenames above.

**Key physics in `HELIOS_LIB.h`:**

### `TransferReaction` class
- Reads `reactionConfig.txt` → sets A(a,b)B
- Uses nuclear masses from `Isotope.h` (AME2016 database: `mass16.txt`, `mass20.txt`)
- Computes relativistic kinematics: boost β, γ, CM momentum, Q-value
- `Event(thetaCM, phiCM)` → generates one event using Lorentz boosts

**Key derived quantities:**
| Variable | Formula | Description |
|---|---|---|
| `slope` | `299.792 * zb * |B| * β / (2π * 1000)` | E-Z slope [MeV/mm] |
| `intercept (y0)` | `√(mb² + kCM²)/γ - mb` | E-Z intercept at ground state |
| `alpha` | `slope / β` | Cyclotron parameter |
| `G` | `α * γ * β * a` | Geometric factor |

**Inverse mapping `CalExThetaCM(e, z, B, a)`:**
- Given measured (e, z), reconstruct (Ex, thetaCM) using Newton's method
- This is what `Analyzer.C` / `Cali_e_trace.C` use to calculate `Ex` branch

### `HELIOS` class — Trajectory Calculator
- `CalArrayHit(Pb, Zb)` → computes where light recoil hits the silicon array
- `CalRecoilHit(PB, ZB)` → computes where heavy recoil hits recoil detector
- `DetAcceptance()` → returns hit code (see below)
- Handles multiple loops (up to 3), blocker, ELUM, extra recoil detectors
- Beam position offset support (xOff, yOff)

**Hit codes from `DetAcceptance()`:**
| Code | Meaning |
|---|---|
| +1 | Light recoil hit array & heavy recoil hit recoil ✅ |
| 0 | No detector hit |
| -1 | Light recoil goes opposite side of array |
| -2 | Light recoil exceeds detector width |
| -3 | Light recoil beyond array range |
| -4 | Light recoil hits blocker |
| -10 | Orbit radius too big (hits bore wall) |
| -11 | Orbit radius too small |
| -12 | Light recoil blocked by recoil detector |
| -13 | More than 3 loops |
| -14 | Heavy recoil misses recoil detector |
| -15 | Cannot find hit on array |
| -20 | Unknown |

### `TargetScattering` class
- Loads SRIM stopping power tables (MeV/mm, keV/µm, or MeV/(mg/cm²))
- Integrates energy loss through target depth via Runge-Kutta-like stepping
- Used when `isTargetScattering = true` in `reactionConfig.txt`

### `Decay` class
- Handles sequential decay: B → d + D (e.g. ¹⁹Ne → ¹⁵O + α)
- Isotropic decay in rest frame of B, boosted to lab
- Activated when `isDecay = true` in `reactionConfig.txt`

---

## `Transfer` Output: `transfer.root`

> ⚠️ **`transfer.root` must be generated by the compiled `Cleopatra/Transfer` binary.**
> Do NOT load or `#include Transfer.h` directly in ROOT macros — it will not work correctly.
> Always `make` the binary first: `cd ~/digios/analysis/Cleopatra && make`
> Then run: `./Transfer reactionConfig.txt detectorGeo.txt Ex.txt ...`

**Contains:**

| Object | Type | Description |
|---|---|---|
| `tree` | TTree | Simulated events |
| `fList` | TObjArray of TF1 | E-Z kinematic lines (infinite-small detector) |
| `fxList` | TObjArray of TGraph | E-Z kinematic lines (finite-size detector correction) |
| `txList` | TObjArray of TGraph | thetaCM-Z curves |
| `gList` | TObjArray of TF1 | Constant thetaCM lines |
| `reactionConfig` | TMacro | Copy of input config |
| `detGeo` | TMacro | Copy of detector geometry |
| `ExList` | TMacro | Copy of Ex.txt |
| `DWBA` | TObjArray | Copy of DWBA distributions |

**Key tree branches:**
| Branch | Description |
|---|---|
| `hit` | Acceptance code (+1 = good) |
| `e` | Light recoil energy [MeV] |
| `z` | Z-position on array [mm] |
| `x` | Detector x-position (-1 to +1) |
| `thetaCM` | CM angle [deg] |
| `Ex` | True excitation energy [MeV] |
| `ExCal` | Reconstructed Ex from (e,z) [MeV] |
| `detID` | Detector index hit |
| `loop` | Number of cyclotron loops |
| `rho` | Orbit radius [mm] |
| `depth` | Reaction depth in target (if scattering on) |
| `decayTheta` | Decay angle change (if decay on) |

---

## E-Z Plot — The Key Physics Observable

In HELIOS, the key observable is the **E-Z plot**: detected energy (E) vs z-position along the beam axis.

For each excitation state Ex_i, the kinematic line in E-Z space is approximately:
```
E ≈ slope * z + y0_i
```
Where `y0_i = √(mb² + kCM_i²)/γ - mb` depends on Ex_i.

This linear relationship is what makes HELIOS powerful — excitation energy is extracted directly from the z-position measurement (via the position-sensitive detectors).

The finite-size correction (`fxList`) accounts for the fact that the detector is at a fixed radius `a` from the beam axis, not at the beam axis.

---

## Simulation Usage in Calibration

1. **`Cali_compareF.C`** loads `fxList` from `transfer.root` and minimizes the distance between data points and kinematic lines → energy calibration
2. **`Monitors.C`** overlays `fList` or `fxList` kinematic lines on the E-Z histogram for visual inspection
3. **`Cali_littleTree_trace.C`** creates a compact `temp.root` from data for faster calibration iteration

---

## Other Cleopatra Tools

| Tool | Purpose |
|---|---|
| `alpha.C` | Alpha source kinematics for calibration |
| `knockout.C` | Knockout reaction simulation |
| `FindThetaCM` | Given E and Z, find thetaCM |
| `DWBARatio.C` | Compare DWBA cross-section ratios |
| `DWBA_compare.C` | Overlay multiple DWBA calculations |
| `nuclear_data.py` | Python nuclear data utility |
| `potentials.h` | Optical model potential parameters |
| `Isotope.h/.C` | Nuclear mass table (AME2016) |

---

## Notes

- `Transfer` uses `isRedo=true` mode to re-draw events until `hit==1` — guarantees all events in tree are detector-accepted (more efficient for statistics)
- Decay simulation is isotropic in the parent rest frame — for anisotropic decay, edit `f1` in `Decay` class
- `Knockout` class also exists for knockout reactions (A(a,a'2)B type) — not commonly used at HELIOS
- SRIM files must be pre-generated with correct beam/target combination and placed in `SRIM/` subfolder relative to `working/`
- The `reaction.dat` output file contains pre-computed kinematic constants used by `Cali_e_trace.C` for on-the-fly Ex reconstruction

---

## See Also

- `HELIOS_Analysis_Workflow.md` — full analysis pipeline (where Cleopatra fits in)
- `HELIOS_Calibration_Workflow.md` — exShift iteration using Cleopatra kinematics overlay
- `calibration_notes.md` — lessons on X-scale, exShift, and transfer.root usage
- `new_experiment_checklist.md` — Cleopatra setup steps at the start of a new experiment
- `expMemory_h095.md` / `expMemory_h094.md` — experiment-specific Cleopatra configs and results
