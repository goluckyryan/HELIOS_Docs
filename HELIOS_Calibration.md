# HELIOS Silicon Detector Calibration

Complete calibration reference for PSD silicon detectors.
Each step covers: physics, code, and lessons learned.

> **See Also:**
> - `new_experiment_checklist.md` -- required files for new experiments
> - `HELIOS_Analysis_Workflow.md` -- full analysis pipeline context
> - `expMemory_h094.md` / `expMemory_h095.md` / `expMemory_h096.md` -- experiment-specific calibration values

---

## Pipeline Overview

Calibration is launched from `working/`:
```bash
cd $HELIOSANA   # = ~/digios/analysis/working/
root -l "AutoCalibrationTrace.C"
```

The macro reads runs from `ChainMonitors.C` between markers:
```
///**********startMarkerforAutoCalibration.
chain->Add("../root_data/gen_run061.root");
///**********endMarkerforAutoCalibration.
```

### AutoCalibrationTrace Menu Reference

| Option | Name | Script called | Output | Notes |
|---|---|---|---|---|
| 0 | Alpha calibration (e + xf/xn) | `Cali_xf_xn.C` | `correction_e_alpha.dat`, `correction_xf_xn.dat` | Requires 228Th alpha run |
| 1 | xf+xn -> e calibration | `Cali_xf_xn_to_e.C` | `correction_xfxn_e.dat` | Requires opt 0 done first |
| 2 | Auto-cal by kinematics | `Cali_littleTree_trace.C` + `Cali_compareF.C` | `correction_e.dat` (KE) | 3-step: temp.root -> transfer.root -> minimize |
| 3 | Generate calibrated tree | `Cali_e_trace.C` (TSelector) | `<expName>_run<NNN>.root` | Requires transfer.root + all correction files |
| 4 | Single-detector alpha cal | `Cali_e_single.C` | (manual inspect) | For individual det re-calibration |
| 5 | X scaling | `Cali_scale_x.C` | `correction_scaleX.dat` | Scale x to full (-1,1) range |
| 6 | coinTime correction (MANUAL) | `GetCoinTimeCorrectionCutG.C` | `correction_coinTime.dat` | Manual graphical cut per det; reads **calibrated tree** (not temp.root) |
| 7 | Run Cleopatra/Transfer | `../Cleopatra/Transfer` (binary) | `transfer.root`, `reaction.dat` | Checks detectorGeo + reactionConfig + Ex.txt first |
| 8 | coinTime vs X (alpha) | `Cali_coinTime_alpha.C` | `correction_coinTime.dat` | Automated coinTime cal using alpha source |

**Typical full calibration sequence:** 0 -> symlink e_alpha -> 1 -> 5 -> 2 (needs 7 first) -> symlink e_KE -> 6 or 8 -> 3

> [!!] **MANDATORY ORDER -- do not skip or reorder steps:**
> 1. **Energy calibration** -> `correction_e_alpha.dat` (symlink `correction_e.dat`)
> 2. **Xf/Xn gain match** -> `correction_xf_xn.dat`
> 3. **Xs->E linearity** -> `correction_xfxn_e.dat`
> 4. **X scale** -> `correction_scaleX.dat`
>
> Each step depends on the previous one. Running out of order produces wrong results.
> Each stage is a sanity check on the previous one.

---

## Calibration Files Summary

| File | Created by | Used by | Content |
|---|---|---|---|
| `correction_e_alpha.dat` | Step 1 (Option 0) | Step 4 | Energy gain/offset per det (alpha) |
| `correction_xf_xn.dat` | Step 2 (Option 0) | Steps 3,4,5 | XN scale factor per det |
| `correction_xfxn_e.dat` | Step 3 (Option 1) | Steps 4,5 | XF+XN -> E slope/offset per det |
| `correction_scaleX.dat` | Step 4 (Option 5) | Step 5 | X position scale per det |
| `correction_e.dat` | Symlink | Step 4 | -> `correction_e_alpha.dat` or `correction_e_KE.dat` |
| `correction_e_KE.dat` | Step 5 (Option 2) | Step 6 | Kinematically refined energy cal |
| `correction_coinTime.dat` | Step 6 (Option 8) | Step 6 | Trigger time vs X correction (pol7) |
| `correction_rdt.dat` | Manual | Step 6 | RDT energy calibration |

> After Step 1: `ln -sf correction_e_alpha.dat correction_e.dat`
> After Step 5: `ln -sf correction_e_KE.dat correction_e.dat`
> Use symlinks so you always know which calibration is active (`ls -la correction_e.dat`).

---

## Step 1 -- Energy Calibration (Alpha Source)

> **AI shortcut:** Use the `analysis-alpha-cal` skill to run Steps 1-4 automatically via `batch_alpha_cal.C` (symlinked to `working_Helios/`). Skill handles peak-finding, matching, and writing all 4 correction files. Manual steps below for reference/debugging.

### Physics

Each PSD detector converts deposited energy to a charge signal proportional to the alpha particle energy. The relationship is linear: `E(MeV) = e_ch / gain + offset`. We calibrate this using known alpha energies from a 228Th source.

Peak widths are physically informative: broad peaks (e.g. 228Ra at 5.34 MeV) indicate energy straggling in the source material, not detector noise. Sharp peaks (sigma ~5-7 ch) = good detector + thin source. Anomalously broad peaks across all energies = check thresholds and grounding.

### 228Th Alpha Reference Energies

| Isotope | Energy (MeV) | Notes |
|---|---|---|
| 228Ra | 5.34 | Often broad (straggling); may merge with 228Th |
| 228Th | 5.42 | Close to 228Ra -- may be unresolved |
| 224Ra | 5.68 | Typically the tallest peak |
| 212Bi | 6.05 | Smaller (36% branch) |
| 220Rn | 6.29 | |
| 216Po | 6.78 | |
| 212Po | 8.79 | Isolated, high energy -- unmistakable anchor |

### Code -- AutoCalibrationTrace Option 0 (`Cali_xf_xn.C`)

1. Plots raw energy spectrum for each of 24 detectors
2. Finds alpha peaks using **TSpectrum** (method 2) or **Gaussian AutoFit** (method 3)
3. Matches peaks to reference energies:
   - `refID = -2` -> 228Th source (7 peaks above)
   - `refID = -3` -> 148Gd + 244Cm: 3.1828, 5.8048 MeV
   - `refID = X` -> use detector X as reference
   - `refID = -1` -> manual entry
4. Fits linear calibration: `e' = e * a1 + a0`
5. **Saves:** `correction_e_alpha.dat` -- 24 rows of `(1/a1, a0)`

### File Format -- CRITICAL [!!]

Monitors.C formula: `eCal = e_ch / eCorr[0] + eCorr[1]`
- `eCorr[0]` = gain (ch/MeV)
- `eCorr[1]` = offset **in MeV** (must be ~0, typically +/-0.1 MeV)
- **NEVER store raw channel offset** -- gets interpreted as MeV -> completely wrong energies
- If fitting `ch = gain*E + offset_ch`: convert via `offset_MeV = -offset_ch / gain`
- **Best practice: use AutoFit (TSpectrum)** -- fits in MeV space, offsets naturally ~0

### Lessons & Considerations

- **Anchor on 212Po (8.785 MeV) first** -- isolated, always visible, unambiguous
- Use predicted positions from 212Po to verify all other peak identities before fitting
- **5.340 and 5.423 MeV peaks are unreliable** -- straggling tails, often merged/misidentified. Do not force two Gaussians if resolution doesn't support it
- Primary reliable peaks: **5.685, 6.051, 6.288, 6.778, 8.785 MeV**
- For poor-resolution dets: drop unresolvable peaks rather than fit them badly
- **AutoFit (TSpectrum) beats manual Gaussian** -- TSpectrum does background subtraction before peak finding, removes continuum bias. Manual fitting = fallback for TSpectrum failures
- Typical good result: residuals within +/-15-20 keV across full range. Residuals > 50 keV = something wrong (misidentified peak or nonlinearity)
- Slope should be ~3-5 keV/ch (typical HELIOS PSD). Large offset = possible pedestal issue
- **Consistency check:** overlay each det individually vs Det 00 (best reference). Label EvsDet plot with DetID numbers. Print fitted centroids + residuals for every peak
- **Eyes first, automation second** -- always look at the plot before trusting any fitted value. Fitters can latch onto noise, split real peaks, or miss shoulders

---

## Step 2 -- Xf/Xn Gain Matching

### Physics

Each PSD silicon strip has two readout ends: Xf (front) and Xn (back). A particle hit deposits charge that splits between the two ends depending on hit position. Charge conservation requires `Xf + k*Xn = const` at fixed energy, producing an anti-diagonal line on a Xn-vs-Xf plot. The constant `k` is the gain ratio -- if the two electronics chains have different gains (they always do), position reconstruction is systematically biased.

The gain correction `xnCorr` rescales Xn so the position asymmetry `(xf - xn*gn) / (xf + xn*gn)` is centered at zero.

### Code -- AutoCalibrationTrace Option 0 (`Cali_xf_xn.C`, second half)

This runs as part of the same Option 0 as energy calibration:

1. Plots XF vs XN with energy gate around chosen alpha peak
2. Fits profile to get XN scale: `xn_corr = xn * scale` so `xf ~ xn`
3. **Saves:** `correction_xf_xn.dat` -- 24 rows of `xnScale`

### How to Extract xnCorr Manually

1. Gate on **212Po (8.785 MeV)** -- isolated, high energy, best lever arm
2. Plot **Xn vs Xf** -> anti-diagonal stripe
3. Fit line: `Xn = p0 + p1*Xf`
4. **xnCorr = -1 / p1**

### What NOT to Do [!!]

- `mean(Xn)/mean(Xf)` -- gives source position on strip, NOT gain ratio
- `mean(E-Xf)/mean(Xn)` -- biased by pedestals
- Line through origin on Xn-vs-Xf -- pedestal offset makes this wrong

### Lessons & Considerations

- Typical xnCorr range: **~0.92-1.11** (h095). Values far from 1.0 (e.g. >20% correction) -> check cable connections or preamp gain settings
- **Verification:** after applying xnCorr, plot `(Xfcal + Xncal)` vs `E` -- should be a tight diagonal
- Band cuts may be needed for noisy dets (e.g. Det 20 h095: `1900 < Xf+Xn < 2500` for xnCorr fit)
- h094 anomalies (experiment-specific, do NOT generalize):
  - Det 07: xnCorr ~ 2.38 (cable/preamp issue -- usable for energy, position less reliable)
  - Det 08, 09, 10: Xn DEAD -- exclude from xnCorr fits, Xf-only position if needed

---

## Step 3 -- Xs->E Linearity (XF+XN -> Energy Cross-Calibration)

### Physics

Charge conservation on the resistive strip means `Xf + Xn*xnCorr` should equal the energy signal `E`. In practice, electronics offsets and nonlinearity mean the relationship is: `E = slope * (Xf + Xn*xnCorr) + intercept`. This step measures that linear correction so edge recovery (Step 4) works correctly.

Without this correction, the single-signal edge recovery formula `xf_only: X = 2*xfcal/e - 1` will be systematically wrong because the assumed `Xf + Xn = E` identity doesn't hold.

### Code -- AutoCalibrationTrace Option 1 (`Cali_xf_xn_to_e.C`)

**Requires:** `correction_xf_xn.dat`, `detectorGeo.txt`

1. Loads detector geometry from `detectorGeo.txt`
2. For each detector: plots 2D histogram of `(xf + xn*xnCorr)` vs `e`
3. Fits linear profile: `e = slope * (xf+xn) + intercept`
4. **Saves:** `correction_xfxn_e.dat` -- 24 rows of `(intercept, slope)`

### Lessons & Considerations

- This is the step most people skip ("Xf+Xn already equals E, right?"). It doesn't. Typical slope is 0.95-1.05 with a non-zero intercept.
- **Verification:** the 2D (Xf+Xn) vs E plot should show a tight diagonal after correction. Scatter or multiple bands = problem upstream (wrong xnCorr or bad detector)
- Required for edge recovery in Steps 4 and 6 -- without it, single-signal events get wrong positions

---

## Step 4 -- X Position Scale

### Physics

The position coordinate `X = (Xfcal - Xncal) / E` naturally ranges over some detector-dependent interval that doesn't fill [-1, +1]. The scale factor normalizes the threshold boundary to +/-1.

When a particle hits near a strip end, one signal drops below the hardware threshold. These events are recovered using charge conservation:

| Condition | Formula | Pile-up location |
|---|---|---|
| Both Xf & Xn valid | `X = (xfcal - xncal) / e` | Standard reconstruction |
| Only Xf valid | `X = 2*xfcal/e - 1` | Piles at +1 |
| Only Xn valid | `X = 1 - 2*xncal/e` | Piles at -1 |

The edge-recovery events create sharp peaks near +/-1 in the X projection. xScale maps the strongest peak to exactly +/-1.

**Important:** xScale is NOT a physical detector length calibration. It maps the threshold boundary to +/-1 as a convenient normalization. True physical Z calibration requires kinematic lines from a known reaction.

### Code -- AutoCalibrationTrace Option 5 (`Cali_scale_x.C`)

**Requires:** `correction_xf_xn.dat`, `correction_xfxn_e.dat`, `correction_e.dat`

1. Computes `X = (xfC - xnC) / (xfC + xnC)` for each detector event-by-event
2. Plots 1D X-distribution for all 24 detectors
3. Finds the main edge peak using TSpectrum + Gaussian fit
4. Scale factor = `1 / |peak position|`
5. **Saves:** `correction_scaleX.dat` -- 24 rows of `scaleX`

> Note: det 11 (index) is hardcoded to scaleX = 1.0 (dead detector)

### Edge Recovery -- Why It Matters

Without edge recovery, events near strip ends are lost entirely. **Always check what fraction of events you're losing by requiring both signals.** If only 10% of events pass a tight X gate, edge recovery is critical.

The correction files from Steps 1-3 must all exist for Monitors.C to apply edge recovery. Missing any one = 90%+ of events near strip ends are lost.

**Verify `(Xf + Xn) / E` ratio before trusting edge recovery.** Mean ratio should be ~0.97 for both-signal events. If it deviates significantly from 1, the formula breaks down.

### Lessons & Considerations

- **[!!] ALL X calculations must produce X in [-1, +1]**. Monitors.C uses [0, 1] internally -- do NOT copy that convention for calibration work
- Include ALL events (both-signal AND single-signal edge-recovery) when plotting X projection
- **Look at the plot** -- the edge peak is obvious. Gaussian fit to strongest peak -> centroid = xScale
- Use the **peak centroid**, not the 50% level. The 50% level depends on edge slope (threshold- and statistics-dependent). The peak centroid is a stable physical reference with well-defined uncertainty from the Gaussian fit
- After applying xScale: apply `|X| < 0.95` cut to remove events in the edge pile-up region. These events have degraded energy resolution due to bulk charge loss near strip ends
- The `|X| < 0.95` cut removes ~21% of events (h094 det 06: 24,761 -> 19,484). Verify by checking E vs X bands remain flat after the cut
- The raw X distribution shows sharp peaks at the threshold boundary -- these mark where one signal drops below hardware threshold, NOT the physical edge of the silicon. Plot Xf and Xn separately (log scale) to find the actual threshold (~270 ch for det 06)

---

## Step 5 -- Kinematic Auto-Calibration (Optional, Beam Data)

### Physics

The alpha source calibration (Step 1) is accurate but limited to the alpha energy range (~5-9 MeV). For physics analysis, nuclear states produce particles at different energies that may expose small nonlinearities or systematic offsets. Kinematic auto-calibration refines the energy coefficients by matching data points to theoretical kinematic lines from Cleopatra/Transfer.

This is only useful when nuclear states are clearly visible in the data.

### Code -- AutoCalibrationTrace Option 2 (`Cali_compareF.C`)

**Requires:**
- `temp.root` -- smaller tree from `Cali_littleTree_trace.C` (sub-step 1)
- `transfer.root` -- kinematic lines from Cleopatra/Transfer (sub-step 2)

**Algorithm (Monte Carlo minimization):**
1. Generates N random trial pairs `(a1, a0)` within user-specified ranges
2. For each trial: applies `e_calibrated = e/a1 + a0` to each event
3. Computes minimum distance from each data point to nearest kinematic line
4. Accumulates total sum-of-residuals
5. Keeps the `(a1, a0)` that minimizes total distance AND maximizes event count
6. **Saves:** `correction_e_KE.dat`

**User parameters:**
- `a1` range (default 220-320 ch/MeV)
- `a0` range (default -1.0 to +1.0 MeV)
- N trials (default 800; use 2000+ for final calibration)
- Energy threshold (default 400 ch)
- Per-detector or all-detectors mode

**3 sub-steps:**
1. Generate `temp.root` via `Cali_littleTree_trace.C`
2. Generate `transfer.root` via `Cleopatra/Transfer`
3. Run `Cali_compareF.C` minimization

After this step: `ln -sf correction_e_KE.dat correction_e.dat`

### Lessons & Considerations

- More trials = better result but slower. 800 is a starting point
- Only useful when states are clearly distinguishable -- don't run on noisy data
- The Monte Carlo approach is robust but not guaranteed optimal; inspect the result visually
- `transfer.root` must be generated by compiled `Cleopatra/Transfer` binary -- never use `Transfer.h` directly

---

## Step 6 -- Generate Calibrated ROOT File

### Code -- AutoCalibrationTrace Option 3 (`Cali_e_trace.C`, TSelector)

Applies all calibrations and produces a fully calibrated ROOT tree.

**Requires all calibration files:**

| File | Required? |
|---|---|
| `correction_xf_xn.dat` | Yes |
| `correction_xfxn_e.dat` | Yes |
| `correction_e.dat` | Yes (symlink to alpha or KE) |
| `correction_scaleX.dat` | Yes |
| `correction_rdt.dat` | If exists |
| `correction_coinTime.dat` | If trace data exists |
| `reaction.dat` | Yes |
| `detectorGeo.txt` | Yes |
| `rdtCuts.root` | If exists |

**Output branches:**

| Branch | Description |
|---|---|
| `e[nDet]` | Calibrated energy (MeV) |
| `xf[nDet]`, `xn[nDet]` | Calibrated XF/XN |
| `x[nDet]` | Position (-1 to +1) |
| `z[nDet]` | Lab z-position (mm) |
| `Ex` | Excitation energy (MeV) |
| `thetaCM` | CM angle (deg) |
| `thetaLab` | Lab angle (deg) |
| `rdt[NRDT]` | Calibrated recoil detector signals |
| `coinTime` | Corrected coincidence time (if trace) |
| `hitID[nDet]` | 0=E+XF+XN, 1=E+XF, 2=E+XN, 3=E only |
| `multiHit` | Multiplicity |

**Smart features:**
- Gracefully handles missing optional branches (EBIS, TAC, ELUM, EZERO, CRDT, trace)
- Writes all calibration files + geometry into ROOT file as TMacro objects for provenance
- Calculates `Ex`, `thetaCM`, `thetaLab` using `reaction.dat` kinematics

Output file name auto-generated from `expName.sh` + run numbers.

---

## Post-Calibration: exShift Iteration

### Physics

After completing the 4-step pipeline and applying RDT cuts, Ex peaks from individual detectors will have small systematic offsets. These arise from residual energy calibration imperfections, position-dependent effects, and dead layer variations. The `exShift[]` array in `Analyzer.C` applies a per-detector constant correction to the excitation energy.

### Procedure

1. Set all `exShift[i] = 0`, run Monitors.C with RDT cut applied
2. Plot per-detector Ex histograms (`hExi`)
3. Read peak positions:
   - g.s.-only dets: use peak position directly
   - 4.4-only dets (12C): use **weighted cluster mean** over 4.0-5.0 MeV (NOT peak bin)
4. Calculate shifts:
   - g.s. dets: `exShift = 0.000 - observed_peak`
   - 4.4 dets: `exShift = 4.439 - cluster_mean`
5. Update `exShift[]` in Analyzer.C, re-run Monitors.C
6. **Iterate 2-5 times** until converged
7. After convergence, have Ryan verify Ex vs DetID and total Ex plots

### Lessons & Considerations [!!]

- **Cluster mean > peak bin** -- peak-bin picking creates asymmetric tails that prevent convergence. The weighted mean is immune to binning effects
- **Iterative is mandatory** -- binning effects shift apparent peaks; a single pass never fully converges
- **Drop dets with >1 MeV shift** -- this indicates bad energy calibration, not a simple offset. Go back and recalibrate that detector
- Final exShift values should be < 0.5 MeV; cap at 0.15-0.2 MeV if suspect
- **[!!] Lesson:** For reactions with a low-Ex state near g.s., the peak finder may match the first excited state as g.s., giving wrong exShift values. Suspect dets show shifts >0.2 MeV. Fix: identify a well-isolated higher-Ex peak and use that for suspect detectors only. Experiment-specific values go in expMemory.
- Low-stats dets: read by eye (no Gaussian fits on ~50 counts)
- **Peaks must be Gaussian** -- asymmetry/tail/shoulder after convergence = something upstream is wrong
- **Before declaring convergence:** describe the peak shape. Is it Gaussian? Symmetric? False convergence is worse than admitting doubt

### h095 Final Values (iteration 5, for reference)

```
Det 00: +0.17    Det 06:  0.00    Det 12: +0.45    Det 18: +0.15
Det 01: +0.22    Det 07:  SKIP   Det 13: +0.27    Det 19:  0.00
Det 02: -0.08    Det 08: +0.01   Det 14: +0.16    Det 20: -0.01
Det 03: -0.06    Det 09: -0.10   Det 15: -0.07    Det 21: -0.07
Det 04: -0.01    Det 10: -0.24   Det 16: -0.06    Det 22:  SKIP
Det 05: +0.11    Det 11:  SKIP   Det 17:  SKIP    Det 23: +0.06
```
- SKIP: Det07 = h095-specific (no physics signal); Det11 = always dead (hardware); Det17/22 = no convergence
- g.s. FWHM: 193 keV, 4.4 MeV FWHM: 225 keV, g.s./4.4 ratio: 0.64

---

## Post-Calibration: Coincidence Time Correction (Trace Data)

### Physics

The trace trigger time `te_t` (from the PSD silicon strip) has a position-dependent walk: charge propagating along the resistive strip arrives at the electronics at different times depending on hit position. This creates a parabolic arch in the `coinTimeUC = (e_t - rdt_t) + (te_t - trdt_t)` vs X plot.

The arch comes **entirely from `te_t`** (the array strip timing), NOT from the RDT. RDT timing (`trdt_t`) vs X is flat (horizontal band ~100-110 ticks, no X-dependence). This was confirmed in h095 trace data.

### Code -- AutoCalibrationTrace Option 8 (`Cali_coinTime_alpha.C`)

1. Plots `te_t[det]` vs `x[det]` for each detector
2. Fits a **7th-order polynomial** (pol7) to capture the non-linear X-dependence
3. Subtracts polynomial to flatten the time vs X distribution
4. **Saves:** `correction_coinTime.dat` -- 24 rows, each: `detID a0 a1 a2 a3 a4 a5 a6 a7 0.0`

### RDT dE vs E Channel Behavior [!!]

The RDT has dE (thin, even index) and E (thick, odd index) detectors with separate timing channels:

| Index | Signal | ADC range |
|---|---|---|
| `rdt[2i]` / `rdt_t[2i]` | dE (thin) | ~4500 ch max |
| `rdt[2i+1]` / `rdt_t[2i+1]` | E (thick) | ~8500 ch max |

Using dE vs E timestamps for `rdtt_best` produces **different coinTimeUC arch shapes and offsets** -- they are NOT interchangeable. The difference is physical (different cable lengths, rise times, digitizer channels).

- **Monitors.C uses dE (even)** for coincidence: `tdiff = rdt_t[j] - e_t[detID]` where j loops over dE channels `{0,2,4,6}`
- **Always use the same channel consistently** across correction fitting and physics analysis
- If you switch channels: **regenerate the polynomial correction** -- the arch shape changes completely

### Cross-Channel Note

The poly correction shape is channel-independent (because the arch comes from the array strip, not the RDT). A correction fit on coinTime(E) **can be applied** to coinTime(dE) and vice versa -- but the **absolute offset** between dE and E channels remains. Only the arch shape transfers, not the zero point.

When comparing coinTimeUC plots from different scripts, always verify which RDT channel was used. Mismatch = systematic offset of ~50-100 ns (looks like a calibration error but is just a channel choice difference).

---

## General Principles

- **Eyes first, automation second.** Always look at the plot before trusting any fitted value. TSpectrum and automated peak finders are tools, not answers.
- **Every step is a sanity check.** Energy calibration validates peak identification. Gain matching validates position reconstruction. Edge recovery validates event statistics. Residuals validate the linear model.
- **When to be suspicious:**
  - Residuals > 30 keV: wrong peak assignment or nonlinearity
  - xnCorr far from 1.0 (>20% correction): check cables/preamp
  - Very few events passing both-signal requirement: thresholds too high or gain matching off
- **Det 11 is always dead** (hardware). Hardcoded scaleX=1.0 as placeholder. Exclude from all analysis.
- **Never copy Ryan's params** -- generate calibration from scratch for each experiment

---

## Experiment-Specific Records

Calibration results for individual experiments are NOT stored here:
- h094: `expMemory_h094.md`
- h095: `expMemory_h095.md` (+ h095 exShift values above for reference)
- h096: `expMemory_h096.md`
- Per-experiment correction files: `~/digios/analysis/working_Helios/<expName>/`
  (h094/h095: `~/digios_11C_2/analysis/working_Helios/`)

---

## Code-Level Reference for AI Batch Automation

All calibration macros live in `~/digios/analysis/Armory/`. The wrapper `AutoCalibrationTrace.C` runs from `working/` (cwd) and saves correction files there (relative paths). Key functions:

### Cali_xf_xn.C (Option 0)

Two-phase: energy calibration + xf/xn gain matching.

**Energy phase:**
1. Fills `e[i]` histograms (one per det), range configurable (default 1000-2600 ch)
2. Peak finding: method 2 = TSpectrum::Search, method 3 = `fitAuto()` (BG-subtracted Gaussian fit via AutoFit.C)
3. Peak matching via `FindMatchingPair()` (AnalysisLibrary.h) -- finds best R-squared subset match between found peaks and reference energies
4. Linear fit (pol1) of matched pairs: `refEnergy = a1 * foundPeak + a0`
5. Saves `correction_e_alpha.dat`: 24 rows of `(1/a1, a0)` -- i.e., `(gain_ch_per_MeV, offset_MeV)`

**XF/XN phase:**
1. User picks a peak index from refEnergy for gating
2. Plots XF vs XN with energy gate: `|e*a1 + a0 - eGate| < 5%`
3. ProfileX fit (pol1): `xf = para[0] + para[1]*xn`
4. `xnScale = -para[1]` (negative of slope)
5. Saves `correction_xf_xn.dat`: 24 rows of `xnScale`

**Interactive inputs (to automate):** energy range min/max, method choice (2 or 3), refID (-2 for 228Th), peak selection for xf/xn gate, save confirmation.

### AutoFit.C -- fitAuto()

`fitAuto(hist, bgEst=10, peakThreshold=0.05, sigmaMax=0, peakDensity=4)`

1. Uses TSpectrum::Search for initial peak finding (peakDensity controls resolution)
2. Estimates background via TSpectrum::Background, subtracts it
3. If sigmaMax=0: estimates sigma per peak from half-max search (backward+forward from peak bin)
4. Fits n-Gauss (normalized) with limits: each peak bounded by midpoints to neighbors
5. Returns vector of fitted peak positions (centroids)

Key: fitAuto works entirely in histogram space (no explicit reference energies). The matching to 228Th energies happens afterward in Cali_xf_xn.C.

### FindMatchingPair() (AnalysisLibrary.h)

Given two vectors of peak positions (found vs reference), finds the subset combination that maximizes R-squared correlation. Uses brute-force combinatorics (`combination()` helper). Works for nFound != nRef. Returns matched pairs for pol1 fitting.

### Cali_xf_xn_to_e.C (Option 1)

1. Loads `detectorGeo.txt` and `correction_xf_xn.dat`
2. Plots 2D: `e[i]` vs `(xf[i] + xn[i]*xnCorr[i])`
3. Fits pol1 directly on 2D histogram (not profile): `e = slope*(xf+xn) + intercept`
4. Saves `correction_xfxn_e.dat`: 24 rows of `(intercept, slope)`
5. One interactive input: save confirmation only

### Cali_scale_x.C (Option 5)

1. Loads `correction_xf_xn.dat`, `correction_xfxn_e.dat`, `correction_e.dat` (symlink)
2. Event-by-event loop computing calibrated X = (xfC-xnC)/(xfC+xnC) with edge recovery
3. TSpectrum::Search on 1D X-distribution, Gaussian fit to strongest peak
4. `scaleX = |fit mean|` -- peak centroid (NOT the 50% level)
5. Det 11 hardcoded to scaleX=1.0
6. Saves `correction_scaleX.dat`: 24 rows of scaleX
7. One interactive input: save confirmation only

### Path Notes

- **All macros run from `working/` (cwd)** and save correction files there
- Data loaded via `ChainMonitors.C` which references `../root_data/gen_runXXX.root`
- `working_Helios/` has symlinks pointing into `h096_31Si_dp/` subdir -- those are for `Monitors.C`, NOT for calibration macros
- After calibration in `working/`, copy correction files to `working_Helios/<expName>/` for Monitors.C use
- `GeneralSortMapping.h` is `#include`d by `Cali_xf_xn.C` from `../working/GeneralSortMapping.h` (relative to Armory/)

### Batch Automation Feasibility

All interactive inputs are `scanf()` calls -- no GUI interaction required for the core algorithms. A batch ROOT macro can:
1. Open the TChain directly (skip ChainMonitors.C parsing)
2. Call TSpectrum/fitAuto programmatically
3. Call FindMatchingPair with refID=-2 (228Th)
4. Save correction files and PNGs without user input

The only GUI elements are TCanvas drawing -- use `gROOT->SetBatch(true)` to suppress display and `canvas->SaveAs("plot.png")` to capture output.

---

_Consolidated from HELIOS_Calibration_Procedure.md, HELIOS_Calibration_Workflow.md, and calibration_notes.md (2026-04-11)_
_Code-level reference added 2026-04-12 from source analysis of Armory/*.C_

