# HELIOS Armory Code Reference

Notes on the analysis library files in `~/digios/analysis/Armory/`.

## Files

| File | Role |
|---|---|
| `AnalysisLibrary.h` | Core data structures + utility functions for analysis macros |
| `Apollo.h` | TSelector stub auto-generated from `transfer.root` -- reads Cleopatra kinematics tree |
| `Cali_e_trace.h` | Energy + trace calibration selector |
| `Cali_littleTree_trace.h` | Little-tree trace calibration selector |

## Working Directory: `Analyzer.h` / `Analyzer.C`

Live in `~/digios/analysis/working/` (experiment-specific). The **final analysis step** after
calibration -- reads the calibrated tree (`<expName>_run<NNN>.root`) and fills histograms.

### Input branches (from Cali_e_trace output)
| Branch | Type | Notes |
|---|---|---|
| `e[30]`, `x[30]`, `z[30]` | Float_t | Calibrated energy, position, z per hit |
| `ring[30]` | Float_t | Ring detector signal |
| `detID`, `hitID[30]`, `multiHit` | Int_t | Detector index, coincidence flags, multiplicity |
| `Ex`, `thetaCM`, `thetaLab` | Float_t | Pre-calculated excitation energy + angles |
| `rdt[8]`, `rdt_t[8]`, `rdtID[8]` | Float_t/ULong64t/Int_t | Calibrated RDT signals |
| `coin_t` | Int_t | Coincidence time (raw) |
| `coinTime` | Float_t | Corrected coinTime (if trace) |
| `te[30]`, `te_r[30]`, `te_t[30]` | Float_t | Trace energy/risetime/time (optional) |
| `trdt[8]`, `trdt_r[8]`, `trdt_t[8]` | Float_t | Trace RDT (optional) |
| `ebis_t` | ULong64_t | EBIS timestamp (commented out in h096) |

### User-configurable parameters (edit in Analyzer.C)
```cpp
double rangeEx[3]  = {50, -1, 8};     // resolution [keV], Ex_low, Ex_high
double rangeCM[3]  = {1, 0, 45};      // resolution [deg], CM_low, CM_high
bool isExOffset    = false;            // apply per-detector exShift corrections
double ExOffset[30] = {...};           // exShift values per detector [MeV]
int nBadDet;                           // number of excluded detectors
int listOfBadDet[] = {...};            // indices of bad detectors to skip
TString rdtCutFile = "";               // rdtCuts.root file (or empty = no cut)
```

### Histogram outputs (filled in Process())
| Histogram | Content |
|---|---|
| `hEx` | Ex spectrum (all good detectors) |
| `hExi[numDet]` | Ex per detector |
| `hExc[numCol]` | Ex per column (summed over rows) |
| `hExr[numRow]` | Ex per row |
| `hExT` | Ex vs thetaCM (2D) |
| `hez` | e vs z (E-Z plot, 2D) |
| `heza` | e vs z with |x|<0.9 gate |
| `hT` | thetaCM spectrum |
| `hei[numDet]`, `hxi[numDet]` | e and x per detector |
| `hexi[numDet]` | e vs x per detector |
| `hTz` | thetaCM vs z |
| `hMultiHit` | Multiplicity distribution |
| `hRun` | Run ID distribution |

### Event selection cuts (in Process())
1. `|x[i]| < 0.95` -- position cut (5% dead zone)
2. `thetaCM >= 10 deg` -- forward-angle cut
3. `i != listOfBadDet[p]` -- exclude dead/noisy detectors
4. Optional: `ExOffset` correction per detector (isExOffset flag)
5. Optional: RDT graphical cut (cutG from rdtCutFile)

### Detector indexing
- `numRow = 6, numCol = 5, numDet = 30` (hardcoded in file)
- Row = `i / numCol`, Column = `i % numCol`
- Column histograms show angular distribution; row histograms show systematic checks

### Notes
- `isTraceDataExist` flag: coinTime branch only connected if trace data present
- `ebis_t` branch commented out in current version
- `ExOffset[i] = 1000` means detector excluded from exShift correction (sentinel value)
- Progress printed every 10 real-seconds during processing
- Run with: `chain->Process("working/Analyzer.C+")` from analysis macro

---

## AnalysisLibrary.h

Header-only library. No .cxx counterpart. Included by analysis macros.

### Structs

#### `DetGeo`
Detector geometry descriptor. Loaded from a TMacro embedded in ROOT files.

Key fields:
- `Bfield` (T), `BfieldSign`, `BfieldTheta` (rad) -- magnetic field
- `detPerpDist`, `detWidth`, `detLength` -- array geometry (mm)
- `recoilPos`, `recoilInnerRadius`, `recoilOuterRadius` -- annular recoil detector
- `elumPos1/2`, `recoilPos1/2` -- imaginary/auxiliary detectors for DWBA comparison
- `blocker`, `firstPos` -- blocker and first active detector position (mm)
- `eSigma` (MeV), `zSigma` (mm) -- intrinsic resolutions
- `pos` (vector) -- relative detector positions; `detPos` computed from `firstPos + pos`
- `nDet` = number of unique positions; `mDet` = number of detectors per position
- `detFaceOut` -- whether detector faces outward (bool)
- `zMin`, `zMax` -- computed z-range of the array

**Note:** `BfieldTheta != 0` is **not supported** (pure axial field assumed).

#### `ReactionConfig`
Reaction descriptor. Loaded from a TMacro embedded in ROOT files.

Key fields:
- Beam/target/light-recoil A, Z
- `beamEnergy` (MeV/u), `beamEnergySigma`, `beamAngle` (mrad), `beamAngleSigma`
- `beamX`, `beamY` -- beam offset (mm)
- `numEvents` -- Monte Carlo event count
- `isTargetScattering` -- whether energy loss in target is simulated
- `targetDensity` (g/cm³), `targetThickness` (cm)
- Stopping power file paths (beam, light recoil, heavy recoil)
- `isDecay` -- whether heavy recoil decays; `heavyDecayA/Z`
- `isRedo` -- re-simulate until particle hits array
- `beamEx` (vector<float>) -- excitation energies of beam-like states [MeV]
- `recoilHeavyA/Z` derived: `beamA + targetA - recoilLightA` etc.

### Utility Functions

#### `SplitStr(line, splitter, shift=0)`
Tokenizes a string by a delimiter, strips leading/trailing spaces. Used to parse TMacro lines.

#### `LoadFitParameters(fileName, print=false)`
Loads calibration fit parameters from a CSV file. Format: `detID, p0, p1, p2, ...`
Returns `vector<vector<float>>` indexed by detID.

#### `LoadDetectorGeo(TMacro*)`
Parses TMacro line-by-line (positional, not key=value) to fill `DetGeo`.
Lines 0-19 are fixed fields; lines 20+ are detector positions (appended to `pos` vector).
Computes `detPos` = absolute positions = `firstPos ± pos[nDet-1-id]`.
Computes `zMin`/`zMax` accounting for `detLength` and `firstPos` sign.

#### `PrintDetGeo(DetGeo)`
Prints a formatted summary of detector geometry to stdout.

#### `LoadReactionConfig(TMacro*)`
Parses TMacro line-by-line (positional) to fill `ReactionConfig`.
Lines 0-22 are fixed; lines 23+ are `beamEx` entries.

#### `PrintReactionConfig(ReactionConfig)`
Prints a formatted reaction summary to stdout.

#### `combination(arr, r)`
Returns all C(n,r) subsets of `arr` as `vector<vector<double>>`.
Uses `std::prev_permutation` on a bitmask. Used by `FindMatchingPair`.

#### `sumMeanVar(data)`
Returns static `double[3]` = {sum, mean, variance}. **[!!] Not thread-safe (static buffer).**

#### `fitSlopeIntercept(dataX, dataY)`
Linear regression (OLS slope + intercept). Returns static `double[2]` = {slope, intercept}. **[!!] Not thread-safe.**

#### `FindMatchingPair(enX, enY)`
Finds the best-matching subset pairing between two energy lists (unequal sizes).
Algorithm:
1. If |enX| > |enY|: enumerate all C(nX, nY) subsets of enX, pick the one with R² closest to 1 vs enY.
2. If |enX| < |enY|: reverse (enumerate subsets of enY).
3. If equal: return as-is (may miss partial matches).
Returns `vector<vector<double>>` = {fitEnergy, refEnergy}.
Used in alpha calibration to match observed peaks to known source energies.

---

## Apollo.h

Auto-generated TSelector (ROOT 6.26, Feb 2023) from `transfer.root`.
Acts as a **skeleton** for post-transfer analysis: reads Cleopatra kinematics and writes a reduced output tree (`hahaApollo.root`).

### Input branches (from transfer.root)

| Branch variable | Physical meaning |
|---|---|
| `thetab`, `phib`, `Tb` | Light recoil lab angle (rad), phi, kinetic energy (MeV) |
| `thetaB`, `phiB`, `TB` | Heavy recoil lab angle, phi, KE |
| `thetaCM` | CM angle (rad) |
| `e` / `b_energy_light` | Light recoil energy at detector |
| `x` / `b_detector_x` | Detector x-position (strip) |
| `z` / `b_array_hit_z` | z-position along array (mm) |
| `z0` / `b_z_cycle` | z at start of cyclotron orbit |
| `t` / `b_cycle_time_light` | Cyclotron period for light recoil |
| `tB` / `b_recoil_hit_time` | Heavy recoil hit time |
| `detID`, `detRowID` | Detector and row indices |
| `loop` | Cyclotron loop number |
| `rho`, `rhoB` | Orbit radius light/heavy (mm) |
| `ExAID`, `ExA` | Beam excitation index + energy (MeV) |
| `ExID`, `Ex` | State index + excitation energy (MeV) |
| `ExCal`, `thetaCMCal` | Calibrated Ex, CM angle (from reconstruction) |
| `beamTheta`, `beamPhi`, `beamKEA` | Beam angle/energy per event (for beam spread) |
| `xArray`, `yArray`, `rhoArray` | Array hit transverse position |
| `xRecoil`, `yRecoil`, `rhoRecoil` | Recoil detector transverse position |

### Output tree (hahaApollo.root)
Reduced set: `x`, `y`, `z` (Float_t), `i`, `j` (Int_t), `theta`, `phi`, `e`, `thetaCM`, `rho` (Double_t).
Purpose: downstream analysis that doesn't need full kinematics tree.

### Notes
- This is a skeleton -- actual `Process()`, `Begin()`, `Terminate()` logic lives in a `.cxx` file not present in Armory.
- The output file name `hahaApollo.root` is hardcoded in `Init()` -- a development artifact.

---

---

## Cali_e_trace.h

TSelector for calibrated tree production. Auto-generated skeleton (ROOT 6.10, Jul 2018) from `gen_run11.root`.
This is the **main calibration step** -- reads raw gen_tree, applies all corrections, writes calibrated tree.

### Input branches (raw gen_tree)

| Variable | Type | Meaning |
|---|---|---|
| `e[100]` | Float_t | Raw energy (silicon array, up to 100 channels) |
| `xf[100]`, `xn[100]` | Float_t | Position signals (far/near end) |
| `ring[100]` | Float_t | Ring detector signals |
| `rdt[50]` | Float_t | Recoil detector signals |
| `crdt[50]` | Float_t | Cathode RDT (optional) |
| `tac[10]` | Float_t | TAC signals (optional) |
| `elum[50]`, `ezero[50]` | Float_t | Auxiliary detectors (optional) |
| `e_t[100]`, `rdt_t[50]`, etc. | ULong64_t | Timestamps for each signal |
| `EBIS_t` | ULong64_t | EBIS gate timestamp (optional) |
| `te[100]`, `te_r[100]`, `te_t[100]` | Float_t | Trace energy, rise time, time (optional) |
| `trdt[50]`, `tcrdt[50]` | Float_t | Trace RDT / cathode RDT (optional) |

Optional branches are detected at runtime (`FindObject`) -- graceful fallback if missing.

### Calibration correction files loaded in Init()

All loaded from the working directory. Each is also written into the output ROOT file as a TMacro.

| File | Applied to | Format | Default if missing |
|---|---|---|---|
| `detectorGeo.txt` | Geometry (positions, B-field) | TMacro positional | Fatal -- terminates |
| `correction_xf_xn.dat` | xn scale (xn = xf condition) | 1 value/det | xnCorr = 1.0 |
| `correction_xfxn_e.dat` | xf/xn → e scale (2 params/det) | a b per line | identity (0,1) |
| `correction_e.dat` | Energy linear cal (2 params/det) | a b per line | identity (1,0) |
| `correction_e2.dat` | Secondary energy correction | a b per line | identity (1,0) |
| `correction_scaleX.dat` | x position scale per det | 1 value/det | xCorr = 1.0 |
| `correction_rdt.dat` | RDT energy calibration | a b per line | identity (1,0) |
| `correction_coinTime.dat` | Coincidence time correction (pol7) | 9 params/det | all zeros |
| `rdtCuts.root` | RDT 2D graphical cuts | TCutG list | no cut applied |
| `reaction.dat` | Kinematics params (mass, q, beta, Et, massB) | line-by-line | isReaction=false |

**coinTime correction:** Uses a 7th-order polynomial (`pol7`) per detector, fit with 8 coefficients + 1 offset. TF1 array `f7[numDet]` created and stored in output.

**Key physics formula (from reaction.dat):**
```
alpha = 299.792458 * |B| * q / (2*pi) / 1000    [MeV/mm -- cyclotron momentum scale]
G = alpha * gamma * beta * perpDist              [MeV -- used in Ex reconstruction]
```

### Output tree branches

| Branch | Type | Notes |
|---|---|---|
| `e[numDet]` | Float_t | Calibrated energy (eC) |
| `xf[numDet]`, `xn[numDet]` | Float_t | Calibrated position signals |
| `x[numDet]` | Float_t | Unadjusted position (-1,1) |
| `z[numDet]` | Float_t | z-position along array (mm) |
| `detID` | Int_t | Detector index with hit |
| `hitID[numDet]` | Int_t | Flags: e+xf+xn all fired? |
| `multiHit` | Int_t | Multiplicity of z |
| `Ex`, `thetaCM`, `thetaLab` | Float_t | Reconstructed excitation energy + angles |
| `rdt[NRDT]`, `rdt_t[NRDT]` | Float_t / ULong64_t | Calibrated RDT + timestamps |
| `nDEHit`, `rdtID[4]` | Int_t | RDT multiplicity + hit indices |
| `coin_t[nDEHit]` | Int_t | Coincidence time (timestamp difference) |
| `coinTimeUC`, `coinTime` | Float_t | Uncorrected and corrected coincidence times |
| `te[numDet]`, `te_r`, `te_t` | Float_t | Trace energy/risetime/time (if trace exists) |
| `ebis_t`, `elum`, `ezero`, `tac`, `crdt` | various | Optional detectors (if present in input) |

### Output filename logic
Parsed from input file names + `expName.sh`:
- Format: `<expName>_<prefix>_run<NNN>.root`
- Consecutive run numbers collapsed: e.g. `run001-003.root`
- Terminates if saveFileName resolves to `.root` (expName load failure)

### Feature flags (set in Init, used in Process)
- `isRunIDExist` -- multi-run merging support
- `isEBISExist` -- beam gate timing available  
- `isTraceDataExist` -- trace-based timing (coinTime) active
- `isCRDTExist` -- cathode RDT available
- `isReaction` -- kinematic reconstruction (Ex, thetaCM) active
- `isRDTCutExist` -- graphical RDT particle ID cuts loaded

### Key design notes
- Array size [100]/[50] must be >= source file array sizes (comment in header)
- `numDet = detGeo.nDet * detGeo.mDet` -- total active channels
- All correction files embedded in output ROOT as TMacro objects for reproducibility
- `NRDT`, `NCRDT` constants come from `GeneralSortMapping.h`

---

_First documented: 2026-04-17 (Spark migration day). Source: read of Armory/*.h files._
_Cali_e_trace.h added: 2026-04-17._

---

## Cali_littleTree_trace.h

TSelector for **pre-calibration gating / quick-look** -- produces a lightweight `temp.root` for
inspection before running the full `Cali_e_trace` calibration. Runs on raw gen_tree.

> Purpose (from header comment): "gating before AutoCalibration -- if correction_coinTime.dat exists
> => calculate coinTime, else gives uncorrected coinTime"

### Key differences from Cali_e_trace.h

| Feature | Cali_littleTree_trace | Cali_e_trace |
|---|---|---|
| Output file | `temp.root` (hardcoded) | `<expName>_run<NNN>.root` (auto-named) |
| Output tree | Single-hit flattened (1 entry/hit) | Multi-hit arrays (eC[30], etc.) |
| Energy correction | No `correction_e.dat` loaded | Full e, e2 correction applied |
| RDT correction | No `correction_rdt.dat` | Full RDT correction applied |
| Kinematics | No Ex/thetaCM | Full kinematic reconstruction |
| expName.sh | Not loaded | Loaded for output filename |
| Embedding corrections | Not embedded in output | All .dat files embedded as TMacros |
| RDT cuts | Loaded (optional) | Loaded (optional) |
| coinTime | Optional (if trace + coinTime.dat) | Optional (if trace + coinTime.dat) |
| Purpose | Quick-look, gating | Production calibrated tree |

### Correction files loaded

| File | Applied | Default if missing |
|---|---|---|
| `detectorGeo.txt` | Geometry | Fatal |
| `correction_xf_xn.dat` | xn scale | xnCorr = 1.0 |
| `correction_xfxn_e.dat` | xf/xn -> e | identity (0,1) |
| `correction_scaleX.dat` | x scale | xScale = 1.0 |
| `correction_coinTime.dat` | coinTime pol7 (only if trace) | all zeros -> coinTimeUC only |
| `rdtCuts.root` | RDT graphical cuts | no cut |

### Output tree branches

| Branch | Type | Notes |
|---|---|---|
| `eventID` | Int_t | Sequential event counter |
| `e` (eTemp) | Double_t | Raw energy (no e correction) |
| `x` (xTemp) | Double_t | Position (-1,1) |
| `z` (zTemp) | Double_t | z along array (mm) |
| `detID` | Int_t | Detector index |
| `hitID` | Int_t | e+xf+xn coincidence flag |
| `multiHit` | Int_t | z multiplicity |
| `coinTimeUC` | Float_t | Uncorrected coinTime (if trace) |
| `coinTime` | Float_t | Corrected coinTime (if coinTime.dat loaded) |

### Design notes
- No `expName.sh` parsing -- output is always `temp.root` (disposable)
- `isTraceDataExist` requires **all 3** of `te_t`, `trdt`, `trdt_t` present (vs. Cali_e_trace which only needs `te_t`)
- `isCoinTimeLoaded` flag: if coinTime.dat loads, writes `coinTime` branch + embeds `fList` in output
- coinTime correction format: `det_idx a0 a1 a2 a3 a4 a5 a6 a7 a8` (9 coefficients: 8 for pol7 + 1 offset)
- Flattened output (one entry per hit) is faster to scroll/gate than multi-hit arrays
- **Typical workflow:** `Cali_littleTree_trace` -> inspect temp.root -> adjust cuts/params -> `Cali_e_trace`

_Cali_littleTree_trace.h added: 2026-04-18._
