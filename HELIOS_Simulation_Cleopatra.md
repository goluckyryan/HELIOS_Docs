# HELIOS Cleopatra Simulation Reference

**Source:** Mac2020 `~/digios/analysis/Cleopatra/`
**Generated:** 2026-03-12
**Author:** Ryan (Tsz Leung) Tang (goluckyryan@gmail.com)

---

## Overview

Cleopatra is the simulation framework for HELIOS. It has two main components:

| Program | Purpose |
|---|---|
| `Cleopatra` | DWBA cross-section calculator  --  wraps `ptolemy` for (d,p), (p,d), (p,p), (d,d) |
| `Transfer` | Monte Carlo simulation of transfer reaction kinematics in HELIOS geometry |

**Workflow:**
```
reactionConfig.txt + detectorGeo.txt + Ex.txt
         ?
  [Cleopatra] -> DWBA.root (thetaCM distributions)
         ?
  [Transfer]  -> transfer.root (kinematic lines + simulated events)
         ?
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
Bfield [T]         -> magnetic field (negative = pointing upstream)
bore [mm]          -> solenoid bore diameter
distance_from_axis -> detector radius from beam axis [mm]
width [mm]         -> detector width
length [mm]        -> detector length
recoil_position    -> recoil detector z-position [mm] (+ = downstream)
recoil inner/outer radius [mm]
isCoincidentWithRecoil
recoilPos1, recoilPos2  -> extra recoil positions (0 = disabled)
elumPos1, elumPos2      -> ELUM positions (0 = disabled)
blocker_length [mm]
firstPos [mm]      -> first detector position (+ = upstream from target, - = downstream)
energy_resolution [MeV]
position_resolution [mm]
facing Out/In
nDet               -> number of detectors at different positions (per side)
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

## `Cleopatra`  --  DWBA Calculator

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
- `ptolemy`  --  DWBA code (compiled locally)
- `dwuck4`  --  alternative DWBA code
- `DWInFileCreator`  --  creates Ptolemy input files

**Output:** `DWBA.root` with `pList` TObjArray of TF1 distributions (one per state)

---

## `Transfer`  --  Monte Carlo Simulation

**Usage:**
```bash
./Transfer [reactionConfig.txt detectorGeo.txt Ex.txt DWBA.root transfer.root reaction.dat plot]
```

All arguments are optional  --  defaults to filenames above.

**Key physics in `HELIOS_LIB.h`:**

### `TransferReaction` class
- Reads `reactionConfig.txt` -> sets A(a,b)B
- Uses nuclear masses from `Isotope.h` (AME2016 database: `mass16.txt`, `mass20.txt`)
- Computes relativistic kinematics: boost beta, gamma, CM momentum, Q-value
- `Event(thetaCM, phiCM)` -> generates one event using Lorentz boosts

**Key derived quantities:**
| Variable | Formula | Description |
|---|---|---|
| `slope` | `299.792 * zb * |B| * beta / (2pi * 1000)` | E-Z slope [MeV/mm] |
| `intercept (y0)` | `?(mb2 + kCM2)/gamma - mb` | E-Z intercept at ground state |
| `alpha` | `slope / beta` | Cyclotron parameter |
| `G` | `alpha * gamma * beta * a` | Geometric factor |

**Inverse mapping `CalExThetaCM(e, z, B, a)`:**
- Given measured (e, z), reconstruct (Ex, thetaCM) using Newton's method
- This is what `Analyzer.C` / `Cali_e_trace.C` use to calculate `Ex` branch

### `HELIOS` class  --  Trajectory Calculator
- `CalArrayHit(Pb, Zb)` -> computes where light recoil hits the silicon array
- `CalRecoilHit(PB, ZB)` -> computes where heavy recoil hits recoil detector
- `DetAcceptance()` -> returns hit code (see below)
- Handles multiple loops (up to 3), blocker, ELUM, extra recoil detectors
- Beam position offset support (xOff, yOff)

**Hit codes from `DetAcceptance()`:**
| Code | Meaning |
|---|---|
| +1 | Light recoil hit array & heavy recoil hit recoil [OK] |
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
- Loads SRIM stopping power tables (MeV/mm, keV/um, or MeV/(mg/cm2))
- Integrates energy loss through target depth via Runge-Kutta-like stepping
- Used when `isTargetScattering = true` in `reactionConfig.txt`

### `Decay` class
- Handles sequential decay: B -> d + D (e.g. 1?Ne -> 1?O + alpha)
- Isotropic decay in rest frame of B, boosted to lab
- Activated when `isDecay = true` in `reactionConfig.txt`

---

## `Transfer` Output: `transfer.root`

> [!!] **`transfer.root` must be generated by the compiled `Cleopatra/Transfer` binary.**
> Do NOT load or `#include Transfer.h` directly in ROOT macros  --  it will not work correctly.
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

## E-Z Plot  --  The Key Physics Observable

In HELIOS, the key observable is the **E-Z plot**: detected energy (E) vs z-position along the beam axis.

For each excitation state Ex_i, the kinematic line in E-Z space is approximately:
```
E ~ slope * z + y0_i
```
Where `y0_i = ?(mb2 + kCM_i2)/gamma - mb` depends on Ex_i.

This linear relationship is what makes HELIOS powerful  --  excitation energy is extracted directly from the z-position measurement (via the position-sensitive detectors).

The finite-size correction (`fxList`) accounts for the fact that the detector is at a fixed radius `a` from the beam axis, not at the beam axis.

---

## Simulation Usage in Calibration

1. **`Cali_compareF.C`** loads `fxList` from `transfer.root` and minimizes the distance between data points and kinematic lines -> energy calibration
2. **`Monitors.C`** overlays `fList` or `fxList` kinematic lines on the E-Z histogram for visual inspection
3. **`Cali_littleTree_trace.C`** creates a compact `temp.root` from data for faster calibration iteration

---

## Other Cleopatra Tools

| Tool | Purpose |
|---|---|
| `alpha.C` | Alpha source kinematics for calibration |
| `knockout.C` | Knockout reaction simulation |
| `FindThetaCM` | thetaCM coverage + solid-angle weights per detector -- see HELIOS_LIB_Reference.md |
| `DWBARatio.C` | Compare DWBA cross-section ratios |
| `DWBA_compare.C` | Overlay multiple DWBA calculations -- **dead weight** (not in makefile, superseded; see TODO.md) |
| `nuclear_data.py` | Python nuclear data utility |
| `potentials.h` | Optical model potential parameters |
| `Isotope.h/.C` | Nuclear mass table (AME2020, mass20.txt) -- see HELIOS_LIB_Reference.md |

---

## Notes

- `Transfer` uses `isRedo=true` mode to re-draw events until `hit==1`  --  guarantees all events in tree are detector-accepted (more efficient for statistics)
- Decay simulation is isotropic in the parent rest frame  --  for anisotropic decay, edit `f1` in `Decay` class
- `Knockout` class also exists for knockout reactions (A(a,a'2)B type)  --  not commonly used at HELIOS
- SRIM files must be pre-generated with correct beam/target combination and placed in `SRIM/` subfolder relative to `working/`
- The `reaction.dat` output file contains pre-computed kinematic constants used by `Cali_e_trace.C` for on-the-fly Ex reconstruction

---

## ExtractXSec -- Ptolemy Output Parser

`~/digios/analysis/Cleopatra/ExtractXSec.h` (.C for main)
Compiled binary: `../Cleopatra/ExtractXSec`

### Purpose
Parses Ptolemy `.out` file → extracts differential cross sections → saves:
- `DWBA.Xsec.txt` -- angle vs. dσ/dΩ table per reaction (human-readable)
- `DWBA.Ex.txt` -- excitation energies + total 4π cross sections
- `DWBA.root` -- TGraphs in TObjArray `gList`; TF1 array `fList` (sin-weighted integrals)

### Call signature
```cpp
int ExtractXSec(string readFile, int indexForElastic = 1);
// indexForElastic: 1=Ratio to Rutherford, 2=Total XSec, 3=Rutherford only
// (only applies to elastic/inelastic channels; transfer always extracts total)
```

### Parsing logic
Reads Ptolemy output line by line, state-machine style:

| Trigger string | Action |
|---|---|
| `$============================================` | New reaction block; extract Ex from title |
| `0INPUT... CHANNEL` | Elastic/inelastic channel (reactionFlag=1) |
| `REACTION:` | Transfer channel (reactionFlag=2) |
| `0 C.M. REACTION ...` | Start extracting (d,p)-type XSec table |
| `C.M. LAB RUTHERFORD` | Start extracting elastic XSec table |
| `0TOTAL:` | End of transfer block; store total XSec |
| `0TOTAL REACTION CROSS SECTION =` | End of elastic block |
| `anglemin=...anglemax=...anglestep=` | Parse angle grid |

### Output ROOT objects
- `gList` (TObjArray): one TGraph per state -- angle [deg] vs. dσ/dΩ [mb/sr]
- `fList` (TObjArray): one TF1 per state -- `dσ/dΩ * sin(θ)` for solid-angle-weighted integration
- `distfunct()`: evaluator function used by fList -- `gList->At(i)->Eval(theta) * sin(theta_rad)`
- Total cross section = integral of `distfunct` from angleMin to angleMax * 2π

### Notes
- `isFloat()` helper: checks if a string is a valid non-negative float (used to skip Ptolemy header lines in XSec table)
- `-404` sentinel: used for missing/malformed data points (same convention as Isotope class)
- Elastic extraction mode (indexForElastic): column offsets differ -- ratio at col 15, total at col 30, Rutherford at col 57
- Transfer extraction: col 0-7 = angle, col 7-26 = XSec

## InFileCreator -- Ptolemy Input Generator

`~/digios/analysis/Cleopatra/InFileCreator.h` (.C for main)
Compiled binary: `../Cleopatra/InFileCreator` (x86-64) / built separately on Spark if needed.

### Input file format (one reaction per line)
```
<Target>(<beam>,<ejectile>)<Residual>(<orbital> <ExState>) <gsSpinParity> <ELAB> <potential>
```
Example:
```
30Si(d,p)31Si 0+ 0d3/2 3/2+ 0.000 11.5MeV/u AK
```

Field breakdown:
| Field | Example | Notes |
|---|---|---|
| Target(beam,ejectile)Residual | `30Si(d,p)31Si` | Standard nuclear notation |
| Ground-state spin-parity of target | `0+` | Used for angular momentum checks |
| Orbital | `0d3/2` | node + l-letter + j; for 2-nucleon: `L=N` format |
| Final state spin-parity | `3/2+` | Parity and j conservation checked vs. orbital |
| Excitation energy [MeV] | `0.000` | Ground state = 0.000 |
| Beam energy | `11.5MeV/u` or `23MeV` | MeV/u auto-multiplied by beam A |
| Optical potential code | `AK` | 2-char code (see below) |

Comments: lines starting with `#` ignored. Blank/short lines ignored.

### Supported reactions
- Single-nucleon transfer: (p,d), (d,p), (d,t), (t,d), (p,n), (n,p), (3He,d), (d,3He), (3He,t), (t,3He)
- Two-nucleon transfer: (p,t), (t,p), (d,a), (a,d), etc.
- Elastic/inelastic scattering: same beam=ejectile mass (e.g. (p,p), (d,d))
- **NOT supported:** 3+ nucleon transfer (e.g. (p,a), (a,p)), proton-neutron exchange (same A, different Z)

### Optical potential codes (2-char)
| Code | Projectile | Ejectile | Reference |
|---|---|---|---|
| `AK` | Deuteron (An-Cai) | Proton (Koning-Delaroche) | Standard for (d,p) at HELIOS |
| `KK` | Proton (KD) | Proton (KD) | (p,p) elastic |
| `AA` | Deuteron (An-Cai) | Deuteron (An-Cai) | (d,d) |
| `CH` | Deuteron (CH89) | Proton (CH89) | Alternative for (d,p) |
| others | various | various | See potentials.h for full list |

First char = incoming channel, second = outgoing channel.

### Validation checks (before writing output)
1. Reaction supported (beam+ejectile A,Z ≤ 4, not 3+ nucleon transfer)
2. A and Z conservation: `A_target + A_beam = A_residual + A_ejectile`
3. Parity conservation: `(-1)^l = gsParityTarget * finalStateParity`
4. Angular momentum: `|gsJ - j_orbital|` ≤ finalJ ≤ `gsJ + j_orbital`
5. Mass table lookup: warns if isotope not found (Mass=-404)

### Output (Ptolemy DWBA.in format)
For each valid reaction line: one Ptolemy input block with:
- `PARAMETERSET dpsb r0target` (d/p) or `alpha3 r0target` (t,3He)
- PROJECTILE: wavefunction `av18` (d,p) or `phiffer` (t,3He)
- INCOMING/OUTGOING: OM potential parameters (auto-computed from `CallPotential()`)
- BOUND STATE: Woods-Saxon r0=1.28, a=0.65, Vso=6 MeV (hardcoded)
- TRANSFER section with L, spectroscopic factor template
- Angle grid from angMin to angMax in angStep increments

### [!!] Known issue
- **InFileCreator segfaults on Pi** (documented in expMemory_h096) -- was Pi-specific issue; needs testing on Spark. Use Mac2020 as fallback.
- The binary must be compiled (`make InFileCreator` in Cleopatra/) -- not a ROOT script

## Simulation_Helper GUI

`~/digios/analysis/working/Simulation_Helper.C` -- interactive ROOT GUI (TGMainFrame) that wraps the full simulation + DWBA workflow.

Launch: `root -l Simulation_Helper.C` from `working/` directory. Requires ROOT with GUI support (Xvfb or display).

### Panels

**Kinematics Simulation panel:**
- Edit `reactionConfig.txt`, `detectorGeo.txt`, `Ex.txt` in built-in text editor
- "Simulate" button: calls `Transfer()` then `Check_Simulation()` -> produces `transfer.root` + `reaction.dat`
- Optional: "Sim with DWBA" checkbox -- uses `DWBA.root` + `DWBA.Ex.txt` as angular distribution weight
- "Plot Simulation" -- re-runs `Check_Simulation()` without re-simulating
- "AutoFit ExCal" -- runs `fitAuto(hExCal, -1)` on the current excitation energy histogram

**DWBA Calculation panel:**
- Edit `DWBA` settings file in editor
- Set angle range (angMin/Max/Step) for cross-section calculation
- Checkboxes: Create inFile -> Run Ptolemy -> Extract Xsec -> Plot (can run any subset)
- Ptolemy binary: `../Cleopatra/ptolemy` (Linux) or `../Cleopatra/ptolemy_mac` (macOS) -- OS auto-detected
- Output files: `DWBA.in`, `DWBA.out`, `DWBA.Xsec.txt`, `DWBA.Ex.txt`, `DWBA.root`
- Extract modes: Total Xsec (default) / Ratio to Rutherford / Rutherford only

**Nuclear Data panel:**
- Enter nucleus name + max Ex -> calls `../Cleopatra/nuclear_data.py <name> <Ex>`
- Fetches nuclear level data from external API

### File map (editor tabs)
| Button | File edited |
|---|---|
| reaction Config | `reactionConfig.txt` |
| detector Geo. | `detectorGeo.txt` |
| Ex List | `Ex.txt` |
| DWBA setting | `DWBA` (no extension) |
| InFile | `DWBA.in` (read-only) |
| OutFile | `DWBA.out` (read-only) |
| X-Sec | `DWBA.Xsec.txt` (read-only) |
| Config Simulation Plot | `../Armory/Check_Simulation_Config.txt` |

### Notes
- File is auto-saved before any button action (including Help)
- Requires ROOT >= 6.26/00 (warns if older)
- `InFileCreator` segfaults on Pi -- use Mac2020 or Spark for DWBA infile creation
- GUI not usable headlessly (needs display) -- run on Mac2020 or via X11 forwarding

## See Also

- `HELIOS_Ptolemy_Build_Notes.md`  --  Ptolemy build notes for Spark/ARM64 and Mac2020 (x86-64)
- `HELIOS_Analysis_Workflow.md`  --  full analysis pipeline (where Cleopatra fits in)
- `HELIOS_Calibration.md`  --  exShift iteration, X-scale, and transfer.root usage
- `new_experiment_checklist.md`  --  Cleopatra setup steps at the start of a new experiment
- `expMemory_h095.md` / `expMemory_h094.md`  --  experiment-specific Cleopatra configs and results
