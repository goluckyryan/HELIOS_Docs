# HELIOS Armory Code Reference

Notes on key analysis library files across the digios pipeline.
**Coverage: 43/47 files documented** (2026-04-29). Remaining 4 are trivial .C entry-point wrappers for documented .h files: Apollo.C, Cali_e_trace.C, Cali_littleTree_trace.C, Check_caliResult.C.

## Files Covered

| File | Location | Role |
|---|---|---|
| `AnalysisLibrary.h` | `Armory/` | Core data structures + utility functions |
| `Apollo.h` | `Armory/` | TSelector stub -- reads Cleopatra kinematics tree |
| `Cali_e_trace.h` | `Armory/` | Main calibration TSelector (reads raw gen_tree) |
| `Cali_littleTree_trace.h` | `Armory/` | Pre-calibration quick-look TSelector |
| `AutoFit.C` | `Armory/` | Spectral peak fitting library (fitNGaussPol, clickFit*, etc.) |
| `Check_e_x.C` | `Armory/` | Visual E-vs-X diagnostic per detector (called after temp.root generation) |
| `Cali_compareF.C` | `Armory/` | Kinematic auto-calibration: Monte Carlo (a1,a0) search against fxList kinematic lines |
| `Cali_xf_xn.C` | `Armory/` | Alpha source calibration: energy (correction_e_alpha.dat) + xf/xn gain match (correction_xf_xn.dat) |
| `Cali_xf_xn_to_e.C` | `Armory/` | XF+XN -> E linearity calibration (correction_xfxn_e.dat); fits `e = slope*(xf+xn) + intercept` per det |
| `Cali_scale_x.C` | `Armory/` | X position scale calibration (correction_scaleX.dat); scales x to full (-1,1) range |
| `AutoCalibrationTrace.C` | `working/` | Master calibration launcher (9-option menu; wraps all Armory cal routines) |
| `Cali_coinTime_alpha.C` | `Armory/` | Automated coinTime vs X correction using alpha source: fits pol7 per det (option 8; requires trace data) |
| `GetCoinTimeCorrectionCutG.C` | `Armory/` | Manual coinTime vs X correction: user draws graphical cut on coinTimeUC vs X, fits pol7, writes correction_coinTime.dat (option 6; reads calibrated tree) |
| `Cali_e_single.C` | `Armory/` | Single-detector alpha re-calibration (option 4): interactive per-detector energy cal; uses FindMatchingPair for 228Th peak matching; user manually saves result (no auto-write) |
| `Analyzer.h` / `Analyzer.C` | `working/` | Final physics analysis TSelector (reads calibrated tree) |
| `rootlogon.C` | `working/` | ROOT style configuration (auto-loaded on startup) |
| `PACE4.C` | `Armory/` | Fusion-evaporation background simulator: reads PACE4 yield table, 10M-event MC through HELIOS geometry, produces E-Z + Ex plots |
| `Penetrability_proton.C` | `Armory/` | Coulomb barrier penetrability T_l + shift factor S_l via GSL Coulomb wave functions (p+10Be example, Iliadis 2015) |
| `Penetrability_simple.C` | `Armory/` | Simplified penetrability calculator (no GSL) |
| `Penetrability_Bessel.C` | `Armory/` | Penetrability via Bessel function method |
| `ExpXsecToRoot.C` | `Armory/` | Convert text experimental Xsec (angle/xsec/errors) to ROOT TGraphErrors in xList |
| `FitXsec.C` | `Armory/` | Fit experimental angular dist with DWBA (1 or 2 components) to extract SF (C²S); chi²/ndf output |
| `runsCheck2.C` | `Armory/` | Run summary table: reads timing TMacro from gen_run*.root, prints #events/size/duration per run, saves run_Summary.txt |
| `FCUP_converter.C` | `Armory/` | ~~Convert FCUP current log to ROOT TTree~~ **RELIC** -- hardcoded 207Hg offsets, not maintained. Dismiss. |
| `script_Ex.C` | `Armory/` | Main physics display: 6-panel canvas (E-Z, Ex spectrum+fit, thetaCM dist); TSpectrum peak find + multi-Gaussian fit |
| `script_ComXsec.C` | `Armory/` | Compare two experimental angular distributions (xList format) on log-scale canvas |
| `Check_rdtGate.C` | `Armory/` | Verify RDT dE-E cuts: 4-panel 2D histograms with TCutG overlaid per RDT pair |
| `readCaliResult.C` | `Armory/` | Inspect caliResult.root for single detector: raw/corrected E-col + TGraph2D distance distribution |
| `SaveTH1IntoText.C` | `Armory/` | Utility: dump TH1F to 2-column text file (bin center, content) |
| `FitCoinTime.C` | `Armory/` | Research: agglomerative single-linkage clustering for coinTime band separation (prototype, not production) |
| `Check_alignment.C` | `Armory/` | E-Z alignment checker: overlay alpha data vs simulation per detector column to find Z-offset issues |
| `Monitors_Util.C` | `Armory/` | ~30 named display functions for interactive monitoring (rawe, ecal, eCalVz, excite, ExThetaCM, recoils, etc.) |
| `Check_Xsec.C` | `Armory/` | Overlay exp thetaCM vs DWBA text table; 1 or 2 component fit; requires checkResult.root from Check_e_z.C |
| `generateHistogram.C` | `Armory/` | Synthetic 12-peak test spectrum for AutoFit.C unit testing (not production) |
| `script_alpha.C` | `Armory/` | Legacy 901-line standalone alpha calibration pipeline -- predecessor to AutoCalibrationTrace; [!!] hardcoded, use AutoCali instead |
| `Cali_ex.C` | `Armory/` | X-dependent energy flatness correction: divides strip into 10 sections, fits pol2 vs X, writes correction_e_flat.dat |
| `Cali_gamma.C` | `Armory/` | Gamma detector (HPGe+NaI) energy calibration; TSpectrum peak match to reference lines; gamma coincidence experiments only |
| `script_FCUP.C` | `Armory/` | ~~Display FCUP beam current vs time~~ **RELIC** -- hardcoded 207Hg run table, not maintained. Dismiss. |
| `readTrace_S.C` | `Armory/` | Raw trace waveform reader/visualizer for diagnostic trace inspection |

## `Cali_xf_xn_to_e.C` -- XF+XN → E Linearity Calibration

`~/digios/analysis/Armory/Cali_xf_xn_to_e.C` (209 lines). AutoCalibrationTrace option 1.

**Purpose:** Ensures XF+XN sum equals the measured energy E (linearity correction).

**Requires:** `correction_xf_xn.dat` + `detectorGeo.txt`

**Algorithm:**
1. For each detector: plot 2D histogram: x=(xf + xn*xnCorr), y=e
2. Fit directly with `pol1`: `e = slope*(xf+xn) + intercept`
3. User prompted to confirm before saving
4. **Output:** `correction_xfxn_e.dat` -- intercept and slope per detector

**Key:**
- Fit is on raw 2D histogram, not a profile -- may have noise from off-diagonal events
- Typical slope: 0.95-1.05; significant deviation = problem with xnCorr or gain mismatch
- Without this correction: single-ended events (XF-only or XN-only) get wrong energy estimates
- Det 11 included but has no data -- fit may fail gracefully

## `Cali_scale_x.C` -- X Position Scale Calibration

`~/digios/analysis/Armory/Cali_scale_x.C` (281 lines). AutoCalibrationTrace option 5.

**Purpose:** Scale x position to full [-1, 1] range (corrects for detector edge effects and physical extent).

**Requires:** `correction_xf_xn.dat` (loaded first)

**Algorithm:**
1. For each detector: plot x-position distribution (1D histogram)
2. Fit distribution edges (using TSpectrum + Gaussian fit)
3. `scaleX[i] = |fit_slope|` -- scales distribution width to unit range
4. **Special:** det 11 hardcoded to `scaleX=1.0` (always dead -- no data to fit)
5. **Output:** `correction_scaleX.dat` -- one value per detector

**Key:** After this correction, `x_corrected = x_raw / scaleX[i]` should range from -1 to +1.
If peaks appear at edges (|x|>0.95) after correction: scaleX may be too large -- check raw distribution.

## `Cali_compareF.C` -- Kinematic Auto-Calibration (Monte Carlo)

`~/digios/analysis/Armory/Cali_compareF.C` (522 lines). Called by `AutoCalibrationTrace.C` option 2 step 3.

**Purpose:** Find best energy calibration (a1, a0) by minimizing distance between data points and theoretical kinematic lines.

**Call:** `Cali_compareF(expTree, refFile, a1Min, a1Max, a0Min, a0Max, nTrial, option, eThreshold)`
- `expTree`: TTree from `temp.root` (Cali_littleTree output)
- `refFile`: `transfer.root` opened as TFile
- `a1Min/Max`: search range for energy gain (default 220-320 ch/MeV)
- `a0Min/Max`: search range for energy offset (default -1.0 to +1.0 MeV)
- `nTrial`: number of Monte Carlo trials (default 800; use 2000+ for precision)
- `option`: detector index (-1 = all detectors)
- `eThreshold`: minimum raw energy to consider

**Algorithm (Monte Carlo minimization per detector):**
1. Load `fxList` from `transfer.root` -- kinematic lines as TGraphs (E vs Z per state)
2. For each trial (up to nTrial):
   - Draw random (a1, a0) uniformly from search ranges
   - For each event: compute `e_cal = e/a1 + a0`
   - Find minimum distance from (z, e_cal) to nearest kinematic line
   - Accumulate total sum-of-residuals (`totalMinDist`)
3. Keep (a1, a0) that minimizes `totalMinDist` AND maximizes event count
4. Second pass: fine-tune with smaller range around best
5. Output: `correction_e_KE.dat`

**Key details:**
- `distThreshold = 0.01` MeV² -- events farther than this contribute a capped penalty
- `skipEveryNEvent` -- auto-set to skip events for speed with large trees
- Optional `cut.root` with `cutEZ` TCutG gate on E-Z
- Optional coinTime gate: `|coinTime - 19| < 30`
- Progress printed every nTrial/5 steps

**Output files:**
- `correction_e_KE.dat` -- calibration coefficients (a1, a0 per detector)
- After running: `ln -sf correction_e_KE.dat correction_e.dat`

## `Check_e_x.C` -- E vs X Visual Diagnostic

`~/digios/analysis/Armory/Check_e_x.C` (168 lines). Called by `AutoCalibrationTrace.C` option 2 (step 1) after generating `temp.root`.

**Purpose:** Quick visual check of calibration quality -- shows E vs X (position) per detector.

**Usage:** `Check_e_x("temp.root", eThreshold=400)`

**Output:** Two canvases:
1. **cCheck** (6×4 grid): E vs X for each of 24 detectors. Red horizontal line = eThreshold.
   - Good calibration: events cluster along a horizontal band (uniform energy vs position)
   - Bad calibration: tilted band = xnCorr or xfxneCorr needs adjustment
2. **cCheck2**: E vs Z (the key E-Z kinematic plot). Kinematic lines should be visible if beam data.

**Optional:** Loads `cut.root` with `cutEZ` TCutG for E-Z gating if present.

**Geometry:** Reads `detectorGeo.txt` for detector positions (same as Cali_e_trace).

## `AutoFit.C` -- Spectral Peak Fitting Library

`~/digios/analysis/Armory/AutoFit.C` (3114 lines). Header-only ROOT macro library for fitting peaks in histograms. Included by `Simulation_Helper.C` (`fitAuto`) and usable interactively.

### Global output variables (populated after any fit)
```cpp
std::vector<double> BestFitMean;   // peak centroids [MeV]
std::vector<double> BestFitCount;  // peak areas (counts)
std::vector<double> BestFitSigma;  // peak widths (sigma)
```

### Fitting functions

| Function | Description | Key args |
|---|---|---|
| `fitGaussPol(hist, mean, sigmaMax, degPol, xMin, xMax)` | 1 Gaussian + polynomial BG | Manual mean guess |
| `fit2GaussP1(hist, ...)` | 2 Gaussians + pol-1 BG | -- |
| `fitGF3Pol(hist, mean, sigmaMax, ratio, beta, step, degPol, xMin, xMax)` | GF3 peak shape + pol BG | GF3 = Gaussian + low-energy tail |
| `fitNGauss(hist, bgEst, fitFile)` | N Gaussians, estimated BG | Reads peaks from `AutoFit_para.txt` |
| `fitNGaussSub(hist, bgEst, degPol, fitFile)` | Subtract pol BG first, then N Gauss | -- |
| `fitNGaussPol(hist, degPol, fitFile, xMin, xMax)` | N Gaussians + polynomial BG | Most common |
| `fitNGaussPolSub(hist, degPol, fitFile, xMin, xMax)` | Subtract pol BG, fit N Gauss | -- |
| `clickFitNGaussPol(hist, degPol, sigmaMax, meanRange)` | Interactive: click peaks on canvas | Mouse-driven |
| `clickFitNGaussPolSub(hist, ...)` | Interactive BG-subtracted version | Mouse-driven |
| `clickFitPol(hist2D, degPol)` | Click-fit polynomial to 2D histogram | For E-Z calibration |
| `clickFitCut(hist2D, detID, degPol, fileName)` | Click to define cut on 2D histogram | For coinTime cuts |

### Parameter file format (`AutoFit_para.txt`)
One peak per line: `mean sigma count` (initial guesses).
- `SaveFitPara(isBestFit, fileName)` -- saves current fit parameters to file
- Load with `loadFitParameters(fitParaFile)` -- reads into global BestFit vectors

### `fitAuto(hist, detID)` (used in Simulation_Helper)
- Called from Simulation_Helper "AutoFit ExCal" button on `hExCal`
- Finds peaks automatically via TSpectrum, fits N Gaussians
- Stores results in global BestFitMean/Count/Sigma

### Utilities
- `GoodnessofFit(hist, fit)` -- computes chi2/NDF, prints result
- `PlotResidual(hist, fit)` -- draws (data-fit)/sigma residuals
- `ScaleAndDrawHist(hist, xMin, xMax)` -- scale-to-range helper
- `RGBWheel(ang)` -- color wheel for multi-peak coloring
- `nPeaks = 16` (global) -- max peaks for N-Gauss fits
- `nPols = 1` (global) -- default polynomial degree for BG

### Typical interactive workflow
```
root -l
.L Armory/AutoFit.C
chain->Process("Analyzer.C+")   // produces hEx, hExi etc.
fitNGaussPol(hEx, 1, "AutoFit_para.txt", -1, 5)  // fit Ex spectrum
SaveFitPara(true)  // save best fit
BestFitMean  // check peak centroids
```

## `rootlogon.C` -- ROOT Style Configuration

`~/digios/analysis/working/rootlogon.C` -- auto-loaded by ROOT on startup from `working/`.
Sets the global style for all plots in the HELIOS analysis session.

**Key settings:**
- Style: "Plain" (white background)
- Stats box: `"nemruoi"` (name, entries, mean, RMS, underflow, overflow, integral)
- Fit box: `1111` (all fit parameters shown)
- Grid: X and Y grids on all pads
- Tick marks on all 4 axes
- Date stamp on plots: lower-left corner, font 62, size 0.02
- Histogram line width: 2
- Frame fill: color 10 (light gray)
- Title fill: color 33 (blue-ish)
- `SetHistMinimumZero(true)` -- prevents histogram zero-suppression (y-axis always starts at 0)
- Palette: `SetPalette(1,0)` -- "Pretty" rainbow for 2D histograms

**Note:** `SetHistMinimumZero(true)` can cause confusion when looking at difference histograms -- bins below zero may be clipped. Override per-histogram with `hist->SetMinimum(-1)` if needed.

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

---

## PACE4.C -- Evaporation Residue Background Simulator

**Source:** `Armory/PACE4.C` (253 lines, ROOT macro)
**Purpose:** Simulate the E-Z distribution of evaporation residues (from fusion-evaporation) that can contaminate HELIOS transfer data.

### What it does
1. Reads a **PACE4 output table** (`pace4_82Se_12C_short.txt`) -- PACE4 is a statistical model code that predicts evaporation residue yields as a function of lab angle (0-180 deg, 10 deg bins) and energy (MeV)
2. Builds a 2D histogram + TGraph2D of yield(theta, KE) and creates a TF2 interpolator (`paceDist`)
3. Runs a **10M-event MC** sampling from the PACE4 distribution:
   - Samples (theta, KE) from the PACE4 yield distribution
   - Passes each event through `HELIOS::CalArrayHit()` + `DetAcceptance()`
   - For accepted hits: reconstructs Ex and thetaCM via `CalExThetaCM()`
4. Produces output in `PACE4.root`: E-Z plot, Ex spectrum, Ex vs thetaCM -- showing where evaporation residues appear in HELIOS data space

### Physics context
- Used to check whether fusion-evaporation background from beam+target overlaps with transfer reaction peaks in Ex
- Example: 82Se + 12C fusion products mimicking (d,p) protons
- PACE4 code: statistical evaporation model (similar to GEMINI, HIVAP)
- Input file format: energy bins × angle bins table, pipe-delimited

### Inputs
- `pace4_82Se_12C_short.txt` -- PACE4 output (experiment-specific)
- `reactionConfig.txt` + `detectorGeo.txt` -- standard HELIOS config

### Output
- `PACE4.root` -- 6-panel canvas: PACE4 dist, smoothed dist, generated angles, E-Z, Ex-thetaCM, Ex

---

## Penetrability_proton.C / Penetrability_simple.C / Penetrability_Bessel.C -- Coulomb Barrier Penetrability Calculators

**Source:** `Armory/Penetrability_proton.C` (142 lines), `Penetrability_simple.C` (121 lines), `Penetrability_Bessel.C` (131 lines)
**Purpose:** Calculate proton Coulomb barrier penetrability T_l(E) and shift factor S_l(E) for R-matrix/resonance analysis.

### Penetrability_proton.C (full Coulomb wave function method)
**Reaction hardcoded:** p + 10Be → 11B (Sp = 11.228 MeV, r = 4.1 fm, Z1=1, Z2=4)
**Energy range:** Ex = 11.23 to 14.40 MeV (proton energy above Sp)
**Method:** Uses **GSL** (`gsl_sf_coulomb_wave_FG_e`) to compute F_l(η,ρ) and G_l(η,ρ) exactly

Key formulas (Iliadis 2015 conventions):
```
k   = sqrt(2 * μ * E) / (ℏc)          [wave number, fm⁻¹]
η   = 0.1574854 * Z1*Z2 * sqrt(μ/E)   [Sommerfeld parameter]
ρ   = 0.218735 * r * sqrt(μ*E)         [dimensionless radius]
T_l = k*r / (F_l² + G_l²)             [penetrability]
S_l = r * (F_l*F_l' + G_l*G_l') / (F_l² + G_l²)  [shift factor]
```

**Output:** Two ROOT canvases -- T_l(E) (log scale) and S_l(E) for L=0,1,2,3

### Use case
R-matrix analysis of resonances near proton threshold. Essential for:
- Computing partial widths: Γ_p = 2*P_l * γ_p²
- Boundary condition shifts in R-matrix fits
- Astrophysical reaction rate calculations near threshold

_PACE4.C and Penetrability files documented: 2026-04-27._

---

## ExpXsecToRoot.C -- Experimental Cross-Section Converter

**Source:** `Armory/ExpXsecToRoot.C` (98 lines, ROOT macro)
**Purpose:** Convert a plain-text experimental cross-section file into a ROOT file containing a `TObjArray` of `TGraphErrors` (same format as Ptolemy DWBA output from `ExtractXSec`).

### Input file format
Text file with `#` delimiters separating states, 4 columns per point:
```
# (start new state/TGraph)
// comment lines ignored
theta_CM   dtheta_CM   xsec   dxsec
...
```
Note: angular errors are read but forced to 0 (avoids strange chi-square in fitting).

### Output
Saves `<inputfile>.root` with `TObjArray* xList` containing one `TGraphErrors` per state.

### Use case
Pre-processing step before `FitXsec.C` — converts published experimental data into the same ROOT format as DWBA calculations so they can be directly compared/fitted.

---

## FitXsec.C -- DWBA Spectroscopic Factor Extractor

**Source:** `Armory/FitXsec.C` (211 lines, ROOT macro)
**Purpose:** Fit experimental angular distributions with DWBA calculations to extract spectroscopic factors (SF = C²S).

### Call signature
```
FitXsec(expXsec, ID, ptolemy, [ID2=-1], [ID3=-1])
```
- `expXsec` -- ROOT file from `ExpXsecToRoot.C` (contains `xList`)
- `ID` -- which state in xList to fit (0-based)
- `ptolemy` -- ROOT file from `ExtractXSec` (contains `qList` of DWBA TGraphs)
- `ID2`, `ID3` -- optional: fit with 1 or 2 DWBA components

### Fitting procedure
**Single-component fit:** minimize χ² of `data = SF * DWBA(θ)` over SF ∈ [0,10]
- Uses ROOT `TF1` with 1 free parameter (SF)
- Reports: SF ± dSF, χ²/ndf per DWBA curve

**Two-component fit** (when ID2+ID3 specified, or n=2 curves):
- Fits `data = A * f1(θ) + B * f2(θ)` with 2 free SFs
- Used for **configuration mixing**: A = sd-shell fraction, B = pf-shell fraction
- Reports A, B, χ²/ndf

### Output
Canvas with log-scale angular distribution plot, overlaid DWBA curves scaled by SF, LaTeX labels with SF values.

### Physics context
- **Primary use:** Extract C²S from (d,p) angular distributions
- **Two-component use:** Quantify sd/pf shell mixing (e.g., h096 32Si 0⁺ states)
- χ²/ndf warning printed if Xsec errors are zero (common for old published data)
- `qList` (not `gList`) -- note different TObjArray name from ExtractXSec default

_ExpXsecToRoot.C + FitXsec.C documented: 2026-04-27._

---

## runsCheck2.C -- Run Summary Table Generator

**Source:** `Armory/runsCheck2.C` (111 lines, ROOT macro)
**Purpose:** Read timing metadata from `gen_runNNN.root` files and print/save a summary table of all runs.

### Call signature
```
runsCheck2([prefix="gen"], [runID=-1])
```
- `prefix` -- file prefix (only `"gen"` supported; trace not implemented)
- `runID=-1` -- all runs; `runID>0` -- single run

### What it does
1. Lists `../root_data/gen_run*.root` files via shell `ls`
2. Opens each ROOT file, reads embedded `TMacro* timing` object (3 lines: firstTS, lastTS, nEvents)
3. Converts timestamps (units: 10 ns ticks → seconds) and computes duration
4. Prints table: filename, #events, size(MB), start-TS, end-TS, duration(s/min/hr)
5. If `runID=-1`: saves full table to `run_Summary.txt`

### Key detail
- Timestamps stored as `ULong64_t` in 10 ns units (divide by 1e8 for seconds)
- `timing` TMacro is embedded in ROOT file by the DAQ sort step
- Exits ROOT after completion (`gROOT->ProcessLine(".q")`)

### Use case
Quick audit of a run campaign: which runs were how long, how many events, any suspiciously short runs.

---

## FCUP_converter.C -- Faraday Cup Log Converter

**Source:** `Armory/FCUP_converter.C` (83 lines, ROOT macro)
**Purpose:** Convert a plain-text Faraday Cup (FCUP) current log into a ROOT TTree with synchronized timestamps.

### Call signature
```
FCUP_converter(FCUPFile)
```

### Input format
Text file with lines: `<timestamp> <current_value>` where timestamp is a date-time string (variable format: 26-char or 18-char depending on day).

### What it does
1. Parses each line: splits at character 26 (or 18 for single-digit days) into timestamp + fCup value
2. Converts date-time string to absolute 10 ns timestamp units
3. Applies a **hardcoded offset** to align FCUP timestamps with DAQ timestamps (calibrated for 207Hg experiment, run41 reference point)
4. Fills ROOT TTree with branches: `f_t` (ULong64_t timestamp) + `f` (Float_t fCup current)
5. Saves as `<inputfile>.root`

### [!!] Important note
- The timestamp offset is **hardcoded for 207Hg experiment** (`offset1` + `offset2` anchored to run41)
- For other experiments, this offset must be recalibrated before use
- Only fills entries where `day >= 10` (filters early/test data from that run)

### Use case
Synchronize beam current (FCUP) with DAQ events for integrated charge normalization and cross-section calculation.

_runsCheck2.C + FCUP_converter.C documented: 2026-04-28._

---

## script_Ex.C -- Main Physics Display Script

**Source:** `Armory/script_Ex.C` (226 lines, ROOT macro)
**Purpose:** Master display script for final physics analysis -- produces 6-panel canvas with E-Z plot, Ex spectrum, peak fitting, and thetaCM distributions.

### Inputs
- `A_gen_run<N>.root` -- calibrated analysis tree (from `Analyzer.C`)
- `transfer.root` -- Cleopatra simulation (provides `fxList` kinematic lines + `gList` DWBA curves)
- `rdtCuts.root` -- RDT graphical cuts (`cutList` TObjArray of `TCutG`)

### Canvas layout (2x3)
| Panel | Content |
|---|---|
| 1 | rdtID vs detID (2D, with RDT gate applied) |
| 2 | Ex spectrum (background-subtracted, TSpectrum peak find) |
| 3 | E vs Z plot with kinematic lines (fxList + gList overlaid) |
| 4 | Background-subtracted Ex with multi-Gaussian fit |
| 5 | thetaCM distributions for first 3 peaks (±3σ gate) |
| 6 | (unused) |

### Peak fitting
- Uses `TSpectrum::Search()` (sigma=1, threshold=0.1) to find up to 16 peaks
- `TSpectrum::Background()` for background estimation (40 iterations)
- Multi-Gaussian fit (`fpeaks`): 3 params per peak (norm, mean, sigma)
- Prints: count, Ex position ± error, sigma ± error per peak

### Gate structure
```
gate_RDT = "(cut0||cut1||cut2||cut3) && -20 < coin_t && coin_t < 40"
detGate  = "&& detID != 11"  // exclude dead detector
```

### Key design
- `fxList` = kinematic lines from transfer.root (TF1 array, one per Ex state)
- `gList` = DWBA angular distribution curves
- thetaCM gated at ±3σ around each fitted peak
- Hardcoded file names (experiment-specific -- edit per run)

---

## script_ComXsec.C -- Compare Two Experimental Cross-Sections

**Source:** `Armory/script_ComXsec.C` (78 lines, ROOT macro)
**Purpose:** Overlay two experimental angular distributions (from different publications/datasets) for comparison.

### Call signature
```
script_ComXsec(id)
```
- `id` -- index into xList (which state/peak to compare)

### Hardcoded inputs (209Pb example)
- `Xsec209Pb_NPA.root` -- first dataset (NPA publication)
- `Xsec209Pb_PR.root` -- second dataset (PR publication)
- Both must contain `xList` TObjArray of `TGraphErrors` (from ExpXsecToRoot)

### Output
Log-scale canvas with both datasets overlaid, auto-ranged axes, legend.

### Use case
Check consistency between published datasets before fitting with DWBA.

_script_Ex.C + script_ComXsec.C documented: 2026-04-28._

---

## Check_rdtGate.C -- RDT Cut Verification Display

**Source:** `Armory/Check_rdtGate.C` (105 lines, ROOT macro)
**Purpose:** Visual check that RDT graphical cuts are correctly placed on the dE-E PID plots.

### Call signature
```
Check_rdtGate(dataList, rdtCut, [eRange=6000], [deRange=4000], [treeName="gen_tree"], [gate=""])
```
- `dataList` -- ROOT file glob (e.g. `"../root_data/gen_run*.root"`)
- `rdtCut` -- ROOT file with `cutList` TObjArray of `TCutG` objects

### Output
4-panel canvas (2×2): one panel per RDT detector pair (rdt[0]/rdt[1], rdt[2]/rdt[3], rdt[4]/rdt[5], rdt[6]/rdt[7]) showing dE vs E 2D histogram with the corresponding graphical cut overlaid.

### Use case
After creating cuts with `RDTCutCreator.C` or `CutCreator.C`, verify they sit correctly on the data before using in physics analysis.

---

## readCaliResult.C -- Calibration Result Inspector

**Source:** `Armory/readCaliResult.C` (35 lines, ROOT macro)
**Purpose:** Display calibration result for a single detector from `caliResult.root`.

### Call signature
```
readCaliResult(detID)
```

### Output
3-panel canvas: (1) raw E vs column plot, (2) corrected E vs column with kinematic line overlay, (3) TGraph2D distance distribution (top-view) used by `Cali_compareF.C` MC search.

### Use case
Diagnose why a specific detector's kinematic auto-calibration succeeded or failed.

---

## SaveTH1IntoText.C -- Histogram to Text Exporter

**Source:** `Armory/SaveTH1IntoText.C` (24 lines, ROOT macro)
**Purpose:** Utility function -- dump a TH1F to a two-column text file (bin center, bin content).

### Call signature
```
SaveTH1IntoText(hist, fileName)
```

### Output format
```
  x_center    content
  ...         ...
```
14.8f tab 9.6f per line. Used to export Ex spectra or rate histograms for external plotting tools.

_Check_rdtGate.C + readCaliResult.C + SaveTH1IntoText.C documented: 2026-04-28._

---

## FitCoinTime.C -- Coincidence Time Clustering Algorithm (Research Tool)

**Source:** `Armory/FitCoinTime.C` (233 lines, ROOT macro)
**Purpose:** Research/development tool for agglomerative single-linkage clustering of coincidence time data. Used to separate overlapping coinTime bands (e.g., two states at different coinTime offsets).

### Algorithm
1. Generates test data: parabolic coinTime vs X distribution with Gaussian smearing + discrete offset outliers
2. Builds N×N distance matrix D between data points
3. Applies **agglomerative single-linkage clustering**: iteratively merges closest pair, reduces matrix
4. Helper functions: `PrintD()` (matrix display), `ReduceDMatrix()` (merge step), `FindMin()` (find closest pair)

**Status:** Research prototype -- not part of production pipeline. Actual coinTime correction uses `GetCoinTimeCorrectionCutG.C` or `Cali_coinTime_alpha.C`.

---

## Check_alignment.C -- E-Z Alignment Checker (Alpha + Simulation)

**Source:** `Armory/Check_alignment.C` (119 lines, ROOT macro)
**Purpose:** Verify detector Z-position alignment by overlaying alpha source E-Z data with simulation kinematic lines.

### Call signature
```
Check_alignment(rootfileAlpha)
```
- `rootfileAlpha` -- calibrated alpha run tree (e.g. `A_gen_run107.root`)
- Also reads `transfer.root` (hardcoded) for simulation comparison

### Output
Multi-panel canvas (6×1 default, 4×1 for single detector): each panel shows E vs Z for one detector column (4 rows overlaid in different colors) from alpha data. Simulation tree overlaid for comparison.

### Use case
Detect Z-offset mismatches or column-to-column shifts before kinematic calibration. If alpha peaks don't align at the expected Z positions, there's a geometry or mapping issue.

**Mode options:** `mode=0` (all detectors), `mode=1` (single detID)

---

## Monitors_Util.C -- Interactive Monitoring Utility Library

**Source:** `Armory/Monitors_Util.C` (557 lines, ROOT macro)
**Purpose:** Collection of ~30 named display functions for interactive ROOT session monitoring. Loaded alongside `Monitors.C` for quick histogram inspection.

### Function catalogue

| Function | Displays |
|---|---|
| `rawID()` | Raw detector ID distribution |
| `rawe([logy])` | Raw energy per channel |
| `rawring([logy])` | Raw ring detector signals |
| `rawxf/rawxn([logy])` | Raw XF/XN position signals |
| `eVring()` | Energy vs ring |
| `xfVxn()` | XF vs XN (position correlation) |
| `eVxs()` | Energy vs X_sum (xf+xn) |
| `ecal()` / `ecal2()` | Calibrated energy |
| `xfCalVxnCal()` | Calibrated XF vs XN |
| `eVx()` | Energy vs X position |
| `ringVx()` | Ring vs X |
| `eCalVxCal()` / `eCalVxCalG()` | Calibrated E vs X (with/without gate) |
| `eCalVzRowG()` | E vs Z per row (gated) |
| `excite()` | Ex spectrum |
| `ExThetaCM()` | Ex vs thetaCM |
| `ExVxCal()` | Ex vs calibrated X |
| `elum()` | ELUM detector |
| `apollo()` | Apollo (Cleopatra kinematics overlay) |
| `recoils([logz])` | RDT recoil plots |
| `tac()` | TAC timing signals |
| `ic()` | Ion chamber signals |
| `eCalVz()` | E-Z plot (final calibrated) |

**Utility functions:** `newCanvas()`, `FindBesCanvasDivision(nPad)`, `listDraws()`, `Count1DH()`

**Design:** All functions assume a pre-loaded TTree named `tree` in the current ROOT session (from Monitors.C workflow).

_FitCoinTime.C + Check_alignment.C + Monitors_Util.C documented: 2026-04-28._

---

## Check_Xsec.C -- Angular Distribution Cross-Section Checker

**Source:** `Armory/Check_Xsec.C` (158 lines, ROOT macro)
**Purpose:** Overlay experimental thetaCM distribution with DWBA predictions from a text table, with optional 2-component fit.

### Inputs (hardcoded)
- `checkResult.root` -- must be pre-generated by `Check_e_z.C` (contains `hThetaList` TObjArray + ExPos/ExSigma arrays)
- DWBA text table (Xsec.txt format from Ptolemy/ExtractXSec)

### Key parameters (edit in script)
- `ExID` -- which state to display (0-based index into hThetaList)
- `scale` -- scale factor for DWBA curves (manual normalization)
- `fitCol[2]` -- which columns in Xsec.txt to use as f1, f2

### Output
Canvas: experimental thetaCM histogram + 1 or 2 DWBA curves overlaid. For 2-component fit: reports A, B coefficients.

**Note:** Predecessor to `FitXsec.C` -- less automated, requires manual `checkResult.root` input.

---

## generateHistogram.C -- Synthetic Spectrum Generator (Test/Demo)

**Source:** `Armory/generateHistogram.C` (38 lines, ROOT macro)
**Purpose:** Generate a synthetic multi-peak spectrum using `AutoFit.C`'s `nGaussPol` function for testing the fitting library.

**Hardcoded:** 12 Gaussians with known positions (0.0 to 6.609 MeV) and sigma=0.05 MeV. Samples a TH1F from the TF1 and calls `clickFit` for interactive fitting.

**Use case:** Unit test / demo for `AutoFit.C` fitting routines. Not used in production analysis.

---

## script_alpha.C -- Legacy Alpha Calibration Script (Pre-AutoCalibrationTrace)

**Source:** `Armory/script_alpha.C` (901 lines, ROOT macro)
**Purpose:** Earlier self-contained alpha calibration pipeline -- predecessor to the modular `AutoCalibrationTrace.C` + Armory system.

### Architecture
Standalone script with its own calibration loaders and Ex reconstruction:

| Function | Purpose |
|---|---|
| `LoadDetGeoAndReactionConfigFile()` | Read detectorGeo.txt + reactionConfig.txt |
| `LoadECorr()` / `LoadXFXNCorr()` etc. | Load all correction files (same format as Armory) |
| `LoadReactionPars()` | Compute kinematic constants (alpha, beta, gamma, mass) |
| `CalExTheta(Hit&)` | Inline Ex/thetaCM reconstruction (same math as HELIOS_LIB.h) |
| `PlotKELines()` | Draw kinematic lines on E-Z plot |
| `script_alpha()` | Main: chains alpha ROOT files, applies corrections, plots E-Z + Ex |
| `Check(id)` | Single-detector check plot |
| `DrawGraph(id)` / `DrawCut(id)` | Graphical utilities |

**Status:** Legacy -- superseded by `AutoCalibrationTrace.C` + modular Armory. Kept for reference and single-shot debugging.

**[!!] Difference from production:** Contains hardcoded corrections and global variables that must be manually updated per experiment. Use `AutoCalibrationTrace.C` for standard workflow.

_Check_Xsec.C + generateHistogram.C + script_alpha.C documented: 2026-04-28._

---

## Cali_ex.C -- Energy Flatness Calibration (X-dependent correction)

**Source:** `Armory/Cali_ex.C` (343 lines, ROOT macro)
**Purpose:** Correct residual energy non-flatness as a function of X position (energy "tilt" across the detector strip).

**Input:** `temp.root` (from Cali_e_trace/littleTree), known reference energies (e.g. 0.00, 0.798, 1.242 MeV for a specific reaction).
**Output:** `correction_e_flat.dat` -- per-detector X-dependent energy correction coefficients.
**Method:** Divides each detector's X range into `numSec=10` sections, fits peak position per section, fits pol2 vs X, writes correction. Uses `AutoFit.C` peak fitting.
**Note:** Step for experiments where E-X flatness matters (high-resolution runs). Not always needed.

---

## Cali_gamma.C -- Gamma Detector Energy Calibration

**Source:** `Armory/Cali_gamma.C` (409 lines, ROOT macro)
**Purpose:** Calibrate gamma detectors (HPGe + NaI) against known gamma energies.

**Call signature:** `Cali_gamma(tree, [runID=0], [threshold=0.05])`
**Hardcoded detectors:** 4 detectors (HPGe-1/2/3 + NaI), linear calibration coefficients per detector, energy range 20-7200 keV.
**Method:** TSpectrum peak finding on gamma spectra, match to reference lines, display calibrated vs raw.
**Use case:** HELIOS gamma coincidence experiments (e.g. with NaI or HPGe arrays in coincidence with silicon). Not standard for pure transfer reactions.

---

## script_FCUP.C -- Faraday Cup Rate vs Run Display

**Source:** `Armory/script_FCUP.C` (200 lines, ROOT macro)
**Purpose:** Display beam current (FCUP) as a function of time for a given run, using pre-loaded run timing table.

**Call signature:** `script_FCUP([runID=41])`
**Hardcoded:** `runTime[40][2]` array with {duration, startTime} for runs 25-64 (207Hg experiment). Uses `FCUP_converter.C` output.
**Use case:** Beam current monitoring and integrated charge calculation for cross-section normalization. [!!] Timing table is experiment-specific -- must be recalibrated for new experiments.

---

## readTrace_S.C -- Raw Trace Reader / Visualizer

**Source:** `Armory/readTrace_S.C` (287 lines, ROOT macro)
**Purpose:** Read and display raw digitizer traces from trace ROOT files for diagnostic purposes.

**Call signature:** `readRawTrace(fileName, [minDetID=0], [maxDetID=1000], [print=false])`
**Input:** Trace ROOT file (trace_runNNN.root format)
**Output:** Canvas with raw waveforms per detector; optional text printout of trace values.
**Use case:** Debug trace acquisition, verify trace lengths, check pulse shapes, diagnose trace fitting issues before running `Cali_coinTime_alpha.C`.

_Cali_ex.C + Cali_gamma.C + script_FCUP.C + readTrace_S.C documented: 2026-04-28._

---

## FitCoinTime2.C -- Coincidence Time Clustering v2 (Least Squares)

**Source:** `Armory/FitCoinTime2.C` (384 lines, ROOT macro)
**Purpose:** Second iteration of coinTime clustering algorithm -- uses least-squares (Lsq struct) instead of agglomerative distance matrix.

**Algorithm:** Generates 500-point test data (linear coinTime + Gaussian noise + discrete offset). Defines `Lsq` struct tracking chi-square, count, mean-square per cluster. Applies `BubbleSort` on cluster quality, iterates up to `maxIteration=1000` times with `threshold=0.02` distance cutoff.
**Status:** Research prototype -- not production. Superseded by `GetCoinTimeCorrectionCutG.C` and `Cali_coinTime_alpha.C` for actual use.

---

## Cali_gamma_histogram.C -- Gamma Histogram Calibration Helper

**Source:** `Armory/Cali_gamma_histogram.C` (228 lines, ROOT macro)
**Purpose:** Helper function called by `Cali_gamma.C` -- processes a single gamma histogram for peak finding and calibration display.

**Call signature:** `Cali_gamma_histogram(hist, [threshold=0.1])`
**Input:** Pre-filled `TH1F*` gamma spectrum
**Output:** 3-panel canvas (1 column × 3 rows): raw spectrum, background-subtracted, fitted peaks with TSpectrum.
**Note:** Companion to `Cali_gamma.C`; not called directly in normal workflow.

---

## Check_Simulation.C -- Transfer Simulation Output Viewer

**Already documented in:** `HELIOS_Simulation_Cleopatra.md` (Check_Simulation section).

Summary: 650-line ROOT macro; visualizes `transfer.root` output in 15-panel canvas (E-Z, recoil XY/RZ, thetaCM, ExCal, ELUM, hitID). Called by `Simulation_Helper.C` "Plot Simulation" button and by `Transfer.C` with `isPlot=1`.

---

## testTraceFit.C -- Trace Fitting Algorithm Tester

**Source:** `Armory/testTraceFit.C` (355 lines, ROOT macro)
**Purpose:** Development/test script for digital pulse shaping algorithms on raw digitizer traces.

**Implements:**
- `TrapezoidFilter(TGraph* trace)` -- trapezoidal shaping filter (Jordanov & Knoll 1994, NIM A353): baseline correction → moving difference → accumulator → trapezoid output. Parameters: riseTime=10 ch, flatTop=4 ch, decayTime=2000 ch, baseLineEnd=80.
- Tests filter on real trace data from trace ROOT files
- Compares trapezoid energy vs standard trace energy

**Use case:** Evaluate alternative energy extraction from traces (vs standard peak/CFD methods). Research tool -- not in production calibration pipeline.

_FitCoinTime2.C + Cali_gamma_histogram.C + Check_Simulation.C (ref) + testTraceFit.C documented: 2026-04-29. Armory coverage now 43/47 (.C companions Apollo.C, Cali_e_trace.C, Cali_littleTree_trace.C, Check_caliResult.C all trivial entry-point wrappers for documented .h files)._
