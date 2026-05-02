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
- `ptolemy`  --  pre-built x86-32 static binary (NOT compiled locally; runs via QEMU on non-x86)
  - **[!!] Spark**: `qemu-i386` not installed -- ptolemy fails with Exec format error. Fix: `sudo apt install qemu-user`. Workaround: run on Mac2020.
  - **Mac2020**: runs natively (x86-64, no QEMU needed)
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
| `gList` | TObjArray of TGraph | Constant-thetaCM lines on E-Z plot |
| `detectorGeo` | TMacro | Embedded detector geometry (for reproducibility) |
| `ExList` | TMacro | Embedded excitation energy list |
| `DWBA` | TObjArray | Embedded DWBA.root content (if used) |

**`reaction.dat` output format** (key constants for Ex reconstruction in Monitors.C/Cali_e_trace.C):
```
mass_b     // light recoil mass [MeV/c^2]
charge_b   // light recoil charge [e]
betaCM     // CM boost beta
Ecm        // CM total energy [MeV]
mass_B     // heavy recoil mass [MeV/c^2]
alpha      // = slope/betaRect = 299.8*Zb*|B|/(2pi*1000) [MeV/mm]
```
**[!!] Mac2020 reaction.dat must match Spark** -- if stale, Ex reconstruction gives wrong values (2 MeV offset seen in h096).
After running Transfer, SCP/git-sync reaction.dat to keep Spark in sync with Mac2020.

**Known mismatch (2026-04-20):** Spark has 30Si(d,p)31Si reaction.dat (betaCM=0.14609) while Mac2020 has 31Si(d,p)32Si (betaCM=0.13529). Mac2020 is correct for h096. To fix:
```bash
scp -i ~/.ssh/id_rsa_mac2020 heliosdigios@192.168.1.164:~/digios/analysis/working/reaction.dat ~/digios/analysis/working/
```
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
| `alpha.C` | Alpha source MC -- simulates isotropic alpha emission in HELIOS (4 configurable energies, eSigma/zSigma smearing), outputs hit/e/z/x/detID/loop/rho tree. Used to understand acceptance geometry for calibration runs. |
| `knockout.C` | Knockout reaction MC -- A(p,2p)B or A(p,pn)B, uses Knockout class from HELIOS_LIB.h; separation energy from file; normal or inverse kinematics |
| `FindThetaCM` | thetaCM coverage + solid-angle weights per detector -- see HELIOS_LIB_Reference.md |
| `DWBARatio.C` | Ratio of two DWBA distributions: `DWBARatio(id1, id2, "DWBA.root")` -> plots both + returns ratio TGraph. Reads from `qList` TObjArray in DWBA.root |
| `DWBA_compare.C` | Overlay multiple DWBA calculations -- **dead weight** (not in makefile, superseded; see TODO.md) |
| `Transfer.C` | Main entry point for Transfer binary (calls `Transfer()` from Transfer.h) |
| `IsotopeShort.C` | Standalone isotope mass utility for Python web interface |
| `ExtractXSecFromText.C` | Like ExtractXSec but reads from .txt instead of .out |
| `PlotTGraphTObjArray.C/h` | Plots all TGraphs from a TObjArray in a ROOT file (used by Cleopatra pipeline) |
| `nuclear_data.py` | IAEA NuChart API client: `nuclear_data.py <AZ> [maxEx_MeV]` -- fetches nuclear level data. Called by Simulation_Helper GUI "Get Data" button. Requires internet + pandas. API: https://nds.iaea.org/relnsd/v0/data |
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

## DWInFileCreator -- Ptolemy Input for Two-Nucleon Transfer (with TNA)

`~/digios/analysis/Cleopatra/DWInFileCreator.h` -- extends `InFileCreator` for two-nucleon transfer reactions.

### Key difference from InFileCreator
`InFileCreator` handles single-nucleon transfer (+ elastic). `DWInFileCreator` additionally reads
a **TNA file** (Two-Nucleon Amplitude) from a shell-model code (e.g. NuShellX, USDB, SDPF-MU)
to provide structure factors for two-nucleon transfer: (p,t), (t,p), (d,α), (α,d), etc.

### Call signature
```cpp
int DWInFileCreator(readFile, infile, angMin, angMax, angStep, TNAinfile);
```
Additional argument: `TNAinfile` -- path to TNA file from shell-model calculation.

### TNA file format (struct TNA)
```
Ex   overlap1_vals   overlap2_vals   amplitude_vals
```
- `Ex`: excitation energy of state [MeV]
- `overlap1`, `overlap2`: single-particle overlaps (from shell model)
- `amplitude`: two-nucleon transfer amplitude = combination of overlaps
- Parsed by `parseTNAFile()` -> vector of TNA structs + orbital list

### Ptolemy output for two-nucleon transfer
For each state: DWBA block includes the TNA-derived structure coefficients.
Phase calculation uses complex arithmetic -- warns if imaginary components appear
(`DWUCK TNA phase calculations yield imaginary numbers -- check input spin and TNA file`).

### When to use
- (p,t) or (t,p) reactions: two-neutron transfer, need 0+ pair structure
- (d,α) or (α,d) reactions: two-nucleon cluster transfer
- Requires shell-model TNA file -- not needed for single-nucleon (d,p), (p,d)
- Use `InFileCreator` for single-nucleon; `DWInFileCreator` for two-nucleon with structure

---

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
First char = incoming channel, second char = outgoing channel.

**Deuteron potentials (uppercase):**
| Code | Reference | Energy range | Mass range |
|---|---|---|---|
| `A` | An & Cai (2006) | E<183 MeV | 12<A<238 |
| `H` | Han, Shi, Shen (2006) | E<200 MeV | 12<A<209 |
| `D` | Daehnick et al. (1980) REL | 11.8<E<80 | 27<A<238 |
| `C` | Daehnick et al. (1980) non-REL | 11.8<E<80 | 27<A<238 |
| `B` | Bojowald et al. (1988) | 50<E<80 | 27<A<208 |
| `L` | Lohr & Haeberli (1974) | 9<E<13 | 40<A |
| `Q` | Perey & Perey (1963) | 12<E<25 | 40<A |
| `Z` | Zhang, Pang, Lou (2016) | 5<E<170 | A<18 |

**Proton potentials (uppercase):**
| Code | Reference | Energy range | Notes |
|---|---|---|---|
| `K` | Koning & Delaroche (2003) | 0.001<E<200 | Isospin-dep.; default for HELIOS |
| `V` | Varner et al. CH89 (1991) | 16<E<65 | 4<A<209 |
| `G` | Becchetti & Greenlees (1969) | E<50 | 40<A |
| `M` | Menet et al. (1971) | 30<E<60 | 40<A |
| `P` | Perey (1963) | E<20 | 30<A<100 |

**Light ions (lowercase): t=triton, h=3He, p=Pang(3He), b=B&G 3He, s/a=alpha**

**Standard HELIOS combinations:**
- `AK` = An-Cai (d) + Koning-Delaroche (p) -- **default for (d,p)**
- `VK` or `KV` = CH89 + KD -- alternative
- First char = incoming, second = outgoing

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

## Check_Simulation.C / PlotSimulation  --  Transfer Output Viewer

`~/digios/analysis/Armory/Check_Simulation.C` -- visualizes `transfer.root` output.
`~/digios/analysis/Cleopatra/PlotSimulation` -- standalone binary wrapper.

### Usage
```bash
# From ROOT (in Simulation_Helper GUI or directly):
Check_Simulation("transfer.root", "../Armory/Check_Simulation_Config.txt", 500, false)
# Or via binary:
./PlotSimulation transfer.root [config_file]
```

### Config file (`Check_Simulation_Config.txt`)
Lines after `////` header:
1. **Canvas layout**: space-separated list of plot IDs (e.g. `pEZ pExCal pThetaCM pRecoilXY`)
2. **Gate**: TCut string applied to simulation tree (e.g. `hit==1 && loop==1`)
3. **ELUM range**: float [MeV]
4. **thetaCM range**: `min max` [deg]
5. **Show KE lines**: `true`/`false` (overlay constant-KE lines on E-Z plot)
6. **Override Ex range**: `true`/`false`
7. **Ex range**: `min max` [MeV] (used if override=true)

### Available plot IDs
| ID | Name | Content |
|---|---|---|
| 0 | `pEZ` | E vs Z (main kinematic plot, with kinematic lines from gList) |
| 1 | `pRecoilXY` | Recoil detector X-Y transverse position |
| 2,3 | `pRecoilXY1/2` | Recoil X-Y for specific loop/condition |
| 4 | `pRecoilRZ` | Recoil radius vs Z |
| 5 | `pRecoilRTR` | Recoil R vs time |
| 6 | `pTDiffZ` | Time difference vs Z |
| 7 | `pThetaCM` | CM angle distribution |
| 8 | `pThetaCM_Z` | CM angle vs Z |
| 9 | `pExCal` | Reconstructed Ex spectrum (key check -- should show states) |
| 10 | `pRecoilRThetaCM` | Recoil R vs thetaCM |
| 11 | `pArrayXY` | Array hit X-Y |
| 12 | `pInfo` | Reaction info text box |
| 13 | `pHitID` | Hit type distribution |
| 14-16 | `pElum*` | ELUM detector plots |

### Key workflow step
After running `Transfer` -> open Check_Simulation to verify:
1. **E-Z plot** (`pEZ`): kinematic lines should match detector geometry
2. **ExCal** (`pExCal`): reconstructed Ex peaks should appear at correct energies
3. If ExCal looks wrong: check `reaction.dat` constants and detector geometry

## PtolemyGUI -- Standalone GUI Wrapper for DWBA Calculations

**Location:** `~/PtolemyGUI/`
**Reference:** Ptolemy: Macfarlane & Pieper, ANL-76-11 Rev. 1, ANL (1978)

Standalone wrapper around Ptolemy that provides a GUI for DWBA input creation, execution, and result display. Two implementations:

### CERN ROOT version (`PtolemyGUI/CERN_root/`)
- Run: `./PtolemyGUI` from working directory
- Reads DWBA config file, uses `InFileCreator.h` to create `DWBA.in`
- Runs Ptolemy, reads output with `ExtractXsec.h`
- **Output:** `DWBA.in`, `DWBA.output`, `DWBA.Xsec.txt`, `DWBA.Ex.txt`, `DWBA.root`
- Plots result with `PlotTGraphTObjArray.h`
- Uses `Cleopatra/potentials.h` for optical model potentials

### Python version (`PtolemyGUI/PyGUIQt6/`)
- Run: `./PtolemyGUIPy.py` (requires PyQt6 + venv)
- Uses Python `inFileCreator` + `ExtractXsecPy.py` (Python ports of C++ tools)
- Output: `Xsec.txt` -- plotted with Matplotlib
- **Note:** "Does not work anywhere" (per README) -- limited portability

### Mac OS support
- Docker container available: see `Cleopatra/install_ptolemy_mac.txt`
- Core Ptolemy binary is Linux-only

**Relationship to digios workflow:** PtolemyGUI is a standalone tool for quick interactive DWBA calculations. The digios `Cleopatra/` workflow is for batch/scripted DWBA as part of the full analysis pipeline.

---

## transfer_test.C -- Unit Test / Interactive Debugger

**Source:** `Cleopatra/transfer_test.C` (77 lines, ROOT macro, not compiled)

Interactive test harness for `HELIOS_LIB.h`. Call signature:
```
transfer_test(thetaCM_deg, phiCM_deg, bField_T, fromOutside_bool)
```

**Hardcoded reaction:** 14C(d,p)15C at 10 MeV/u, B field = arg.

**What it does:**
1. Sets up `TransferReaction` (A=14C, a=d, b=p, B=15C)
2. Calls `CalReactionConstant()` and prints CM beta, slope (α·β), alpha
3. Calls `reaction.Event(thetaCM, phiCM)` → 4-vectors for b (proton) and B (15C)
4. Calls `helios.CalArrayHit(Pb, 1)` and `helios.CalRecoilHit(PB, 6)`
5. Runs `DetAcceptance()` loop until hitID ≤ 1
6. Prints trajectory via `PrintTrajectory(helios.GetTrajectory_b())`

**Uses:** `../working/detectorGeo.txt` for detector geometry.

**Purpose:** Debug HELIOS_LIB trajectory and acceptance for a single event. Not part of production pipeline.

---

## PlotTGraphTObjArray.C/h -- DWBA Angular Distribution Plotter

**Source:** `Cleopatra/PlotTGraphTObjArray.C` (58 lines entry point) + `PlotTGraphTObjArray.h` (102 lines logic)

**Compilation:**
```bash
g++ PlotTGraphTObjArray.C -o PlotTGraphTObjArray `root-config --cflags --glibs`
```

**Usage:**
```bash
./PlotTGraphTObjArray <root_file> [savePNG]
```

**Input:** Any ROOT file containing a `TObjArray` named `gList` of `TGraph` objects (DWBA.root output from `ExtractXSec`). Also works with `fList` (TF1 fits).

**What it does:** Opens root_file, reads `gList`, plots all member TGraphs in a single canvas. Option `savePNG=1` saves canvas to PNG and exits; without it, opens interactive ROOT TApplication.

**Use case:** Quick visual inspection of DWBA angular distributions from Ptolemy output, without needing to open ROOT interactively and navigate the file.

---

## potentials.h -- Optical Model Potential Library

**Source:** `Cleopatra/potentials.h` (1073 lines)
**Basis:** Equivalent to Kay Ben's `globals_beta_v5` parametrization set.

### Global variables (set by each potential function)
```
v, r0, a         -- real volume (depth MeV, radius fm, diffuseness fm)
vi, ri0, ai      -- imaginary volume
vsi, rsi0, asi   -- imaginary surface (derivative)
vso, rso0, aso   -- real spin-orbit
vsoi, rsoi0, asoi -- imaginary spin-orbit
rc0              -- Coulomb radius
```
All radii are reduced (actual radius = r0 * A^(1/3)).

### Utility functions
- `PrintPotential()` -- print all 15 parameters
- `potentialRef(name)` -- return citation string for a 1-char code
- `CallPotential(name, A, Z, E, Zproj)` -- dispatcher: call the right function by code letter

### Potential catalogue (1-char codes)

**Deuteron potentials:**

| Code | Function | Reference | Energy range | Mass range |
|---|---|---|---|---|
| `A` | `AnCaiPotential` | An & Cai (2006) PRC 73 054605 | E < 183 MeV | 12 < A < 238 |
| `H` | `HSSPotential` | Han, Shi, Shen (2006) PRC 74 044615 | E < 200 MeV | 12 < A < 209 |
| `B` | `BojowaldPotential` | Bojowald et al. (1988) PRC 38 1153 | 50-80 MeV | 27 < A < 208 |
| `D` | `DaehnickPotential` | Daehnick, Childs, Vrcelj (1980) PRC 21 2253 (REL) | 11.8-80 MeV | 27 < A < 238 |
| `C` | `DaehnickPotential` | Daehnick, Childs, Vrcelj (1980) PRC 21 2253 (NON-REL) | 11.8-80 MeV | 27 < A < 238 |
| `L` | `LohrPotential` | Lohr & Haeberli (1974) | 9-13 MeV | A > 40 |
| `Q` | `PereyPereyPotential` | Perey & Perey (1963) | 12-25 MeV | A > 40 |
| `Z` | `ZhangPangLouPotential` | Zhang, Pang, Lou (2016) PRC 94 014619 | 5-170 MeV | A < 18 |

**Proton potentials:**

| Code | Function | Reference | Energy range | Mass range |
|---|---|---|---|---|
| `K` | `KoningPotential` | Koning & Delaroche (2009) | 0.001-200 MeV | 24 < A < 209 |
| `V` | `VarnerPotential` | Varner et al. CH89 (1991) | 16-65 MeV | 4 < A < 209 |
| `M` | `MenetPotential` | Menet et al. (1971) | 30-60 MeV | A > 40 |
| `G` | `BecchettiPotential` | Becchetti & Greenlees (1969) | E < 50 MeV | A > 40 |
| `P` | `PereyPotential` | Perey (1963) | E < 20 MeV | 30 < A < 100 |

**A=3 potentials (³He / triton):**

| Code | Function | Reference |
|---|---|
| `x` | `XuPotential` | Xu, Guo, Han, Shen (2011) |
| `l` | `LiangPotential` | Liang, Li, Cai (2009) |
| `p` | `PangPotential` | Pang et al. (2009), isospin dep. |
| `c` | `LiLiangCaiPotential` | Li, Liang, Cai (2007) -- tritons |
| `t` | `TrostPotential` | Trost et al. (1987) |
| `h` | `HyakutakePotential` | Hyakutake et al. (1980) |
| `b` | `BecchettiA3Potential` | Becchetti & Greenlees (1971), isospin dep. |

**Alpha potentials:**

| Code | Function | Reference |
|---|---|
| `s` | `SuAndHanPotential` | Su & Han (2015) |
| `a` | `AvrigeanuPotential` | Avrigeanu et al. (2009) |
| `f` | `BassaniPicardPotential` | Bassani & Picard (1969), fixed params, A=90 |

**Custom / Bardayan:**

| Code | Function | Notes |
|---|---|
| `X` | `CustomXPotential` | Bardayan PRC 78 052801(R) (2008) |
| `Y` | `CustomYPotential` | Bardayan PRC 78 052801(R) (2008) |

### HELIOS standard combinations
- **AK** = An-Cai (deuteron, code `A`) + Koning-Delaroche (proton, code `K`) -- default for (d,p) at 10 MeV/u
- Codes are combined as 2-char strings in `InFileCreator`: first char = beam/exit OM, second = residual
- `CallPotential()` dispatches by single char; `InFileCreator` splits the 2-char string

## See Also

- `HELIOS_PtolemyPlusPlus.md`  --  **Ptolemy++ C++ DWBA** (<0.01% Fortran error, ~/Ptolemy_AI/); includes bound-state sensitivity study (r0 changes SF by ~3x)
- `HELIOS_Ptolemy_Build_Notes.md`  --  Ptolemy build notes for Spark/ARM64 and Mac2020 (x86-64)
- `HELIOS_Analysis_Workflow.md`  --  full analysis pipeline (where Cleopatra fits in)
- `HELIOS_Calibration.md`  --  exShift iteration, X-scale, and transfer.root usage
- `new_experiment_checklist.md`  --  Cleopatra setup steps at the start of a new experiment
- `expMemory_h095.md` / `expMemory_h094.md`  --  experiment-specific Cleopatra configs and results
- `HELIOS_WoodsSaxon.md`  --  Woods-Saxon bound-state solver (C++, digios) for generating WF inputs to Ptolemy
- `codes/woods_saxon.py`  --  Python WS solver (Numerov) for Coulomb energy calculations
- `HELIOS_Raphael_DWBA.md`  --  Ryan's Python ZR-DWBA implementation (alternative to Ptolemy, development)
- `~/PtolemyGUI/frecsoTools/`  --  FRESCO input file creator (C++, 297 lines) + output extractor (Python, 245 lines); parallel to Ptolemy InFileCreator but for coupled-channels FRESCO code
- `~/PtolemyGUI/dwuck4/`  --  DWUCK4 Fortran code (alternative DWBA, 4 source files + documentation)
