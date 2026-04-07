# HELIOS Calibration Workflow Reference

**Source:** Mac2020 `~/digios/analysis/Armory/` + `working/AutoCalibrationTrace.C`
**Generated:** 2026-03-12

---

## Overview

Calibration is launched interactively from the `working/` directory:

```bash
cd $HELIOSANA   # = ~/digios/analysis/working/
root -l "AutoCalibrationTrace.C"
```

The macro reads the run file list from `ChainMonitors.C` between two special markers:
```
///**********startMarkerforAutoCalibration.
chain->Add("../root_data/gen_run061.root");
///**********endMarkerforAutoCalibration.
```

---

## Typical Calibration Sequence

> ⚠️ **MANDATORY ORDER — do not skip or reorder steps:**
> 1. **Energy** → `correction_e_alpha.dat` (Option 0)
> 2. **Xf/Xn gain match** → `correction_xf_xn.dat` (Option 0)
> 3. **Xs→E linearity** → `correction_xfxn_e.dat` (Option 1)
> 4. **X scale** → `correction_scaleX.dat` (Option 5)
>
> See `calibration_notes.md` for lessons learned and known issues per experiment.

### For Alpha Source Runs:
1. **Option 0** — XF/XN position + energy calibration (alpha peaks)
2. **Option 5** — X-scale normalization to (−1, +1)

### For Beam Runs:
3. **Option 1** — XF+XN → Energy cross-calibration
4. **Option 3** — Generate final calibrated ROOT file

### Optional (if states are clearly visible):
5. **Option 2** — Kinematic auto-calibration using `transfer.root`

---

## Option 0 — `Cali_xf_xn.C` — Alpha Calibration

**Purpose:** Energy calibration + XF/XN relative gain matching using alpha source

**Inputs:** Raw gen_tree branches: `e[det]`, `xf[det]`, `xn[det]`

**Steps:**
1. Plots raw energy spectrum for each of 24 detectors
2. Finds alpha peaks using **TSpectrum** (method 2) or **Gaussian AutoFit** (method 3)
3. Matches peaks to reference energies — built-in options:
   - `refID = -2` → ²²⁸Th source: 5.34, 5.42, 5.69, 6.05, 6.29, 6.78, 8.79 MeV
   - `refID = -3` → ¹⁴⁸Gd + ²⁴⁴Cm: 3.1828, 5.8048 MeV
   - `refID = X` → use detector X as reference
   - `refID = -1` → manual entry
4. Fits linear calibration: `e' = e * a1 + a0`
5. **Saves:** `correction_e_alpha.dat` — 24 rows of `(1/a1, a0)`
6. Plots XF vs XN with energy gate around chosen peak
7. Fits profile to get XN scale: `xn_corr = xn * scale` so xf ≈ xn
8. **Saves:** `correction_xf_xn.dat` — 24 rows of `xnScale`

**Output files:**
- `correction_e_alpha.dat` — energy calibration (from alpha)
- `correction_xf_xn.dat` — XN scale correction

---

## Option 5 — `Cali_scale_x.C` — X Position Scaling

**Purpose:** Scale the position coordinate x = (xf−xn)/(xf+xn) to fill the full (−1, +1) range uniformly

**Requires:** `correction_xf_xn.dat`, `correction_xfxn_e.dat`, `correction_e.dat` loaded first

**Steps:**
1. Computes `x = (xfC − xnC) / (xfC + xnC)` for each detector event-by-event
2. Plots 1D x-distribution for all 24 detectors
3. Finds the main alpha peak position in x using TSpectrum + Gaussian fit
4. Scale factor = `1 / |peak position|`
5. **Saves:** `correction_scaleX.dat` — 24 rows of `scaleX`

> Note: det 11 (index) is hardcoded to scaleX = 1.0

**Output:** `correction_scaleX.dat`

---

## Option 1 — `Cali_xf_xn_to_e.C` — XF+XN → Energy

**Purpose:** Ensure `xf + xn = e` (energy conservation across the resistive layer)

**Requires:** `correction_xf_xn.dat`, `detectorGeo.txt`

**Steps:**
1. Loads detector geometry from `detectorGeo.txt`
2. For each detector: plots 2D histogram of `(xf + xn*xnCorr)` vs `e`
3. Fits linear profile: `e = slope * (xf+xn) + intercept`
4. **Saves:** `correction_xfxn_e.dat` — 24 rows of `(intercept, slope)`

**Output:** `correction_xfxn_e.dat`

---

## Option 3 — `Cali_e_trace.C` (TSelector) — Generate Calibrated ROOT File

**Purpose:** Apply all calibrations and produce a fully calibrated ROOT tree

**Requires all calibration files:**
| File | Content |
|---|---|
| `correction_xf_xn.dat` | XN scale correction |
| `correction_xfxn_e.dat` | XF+XN → E correction |
| `correction_e.dat` | Energy calibration coefficients |
| `correction_scaleX.dat` | X position scale |
| `correction_rdt.dat` | RDT energy calibration (if exists) |
| `correction_coinTime.dat` | Coincidence time correction (if trace exists) |
| `reaction.dat` | Reaction kinematics parameters |
| `detectorGeo.txt` | Physical detector geometry |
| `rdtCuts.root` | RDT particle ID graphical cuts (if exists) |

**Output branches in calibrated tree:**
| Branch | Description |
|---|---|
| `e[nDet]` | Calibrated energy (MeV) |
| `xf[nDet]`, `xn[nDet]` | Calibrated XF/XN |
| `x[nDet]` | Position (−1 to +1) |
| `z[nDet]` | Lab z-position (mm) |
| `Ex` | Excitation energy (MeV) |
| `thetaCM` | CM angle (deg) |
| `thetaLab` | Lab angle (deg) |
| `rdt[NRDT]` | Calibrated recoil detector signals |
| `coinTime` | Corrected coincidence time (if trace) |
| `hitID[nDet]` | 0=E+XF+XN, 1=E+XF, 2=E+XN, 3=E only |
| `multiHit` | Multiplicity |

**Output file name:** Auto-generated from `expName.sh` + run numbers, e.g. `h094_19Ne_pp_gen_run061.root`

**Smart features:**
- Gracefully handles missing optional branches (EBIS, TAC, ELUM, EZERO, CRDT, trace)
- Writes all calibration files + geometry into ROOT file as TMacro objects for provenance
- Calculates `Ex`, `thetaCM`, `thetaLab` using `reaction.dat` kinematics

---

## Option 2 — `Cali_compareF.C` — Kinematic Auto-Calibration

**Purpose:** Fine-tune energy calibration by matching data to kinematic lines from Cleopatra/Transfer

**When to use:** When nuclear states are clearly visible/distinguishable in the data

**Requires:**
- `temp.root` — smaller tree from `Cali_littleTree_trace.C` (step 1)
- `transfer.root` — kinematic lines from Cleopatra/Transfer (step 2)

**Algorithm (Monte Carlo minimization):**
1. Generates N random trial pairs `(a1, a0)` within user-specified ranges
2. For each trial: applies `e_calibrated = e/a1 + a0` to each event
3. Computes minimum distance from each data point to the nearest kinematic line
4. Accumulates total sum-of-residuals
5. Keeps the `(a1, a0)` that minimizes total distance AND maximizes event count
6. **Saves:** `correction_e_KE.dat` — kinematically calibrated coefficients

**User parameters:**
- `a1` range (default 220–320 ch/MeV)
- `a0` range (default −1.0 to +1.0 MeV)
- N trials (default 800)
- Energy threshold (default 400 ch)
- Per-detector or all-detectors mode

**3 sub-steps:**
1. Generate `temp.root` (smaller tree, faster iteration) via `Cali_littleTree_trace.C`
2. Generate `transfer.root` kinematic lines via `Cleopatra/Transfer`
3. Run `Cali_compareF.C` minimization

**Output:** `correction_e_KE.dat` (replaces `correction_e.dat` in final analysis)

---

## Option 8 — `Cali_coinTime_alpha.C` — Trigger Time vs X Correction

**Purpose:** Correct the position-dependent timing offset of the trace trigger time

**Requires:** Trace data (`te_t` branch must exist in tree)

**Steps:**
1. Plots `te_t[det]` vs `x[det]` for each detector (trigger time vs position)
2. Fits a **7th-order polynomial** (pol7) to capture the non-linear x-dependence
3. Subtracts polynomial to flatten the time vs x distribution
4. **Saves:** `correction_coinTime.dat` — 24 rows, each: `detID a0 a1 a2 a3 a4 a5 a6 a7 0.0`

**Output:** `correction_coinTime.dat`

---

## Calibration Files Summary

| File | Created by | Used by | Content |
|---|---|---|---|
| `correction_e_alpha.dat` | Option 0 | Option 3 | Energy gain/offset per det (alpha) |
| `correction_xf_xn.dat` | Option 0 | Options 1,3,5 | XN scale factor per det |
| `correction_xfxn_e.dat` | Option 1 | Options 3,5 | XF+XN → E slope/offset per det |
| `correction_e.dat` | Manual copy | Option 3 | Final energy calibration (copy from alpha or KE) |
| `correction_scaleX.dat` | Option 5 | Option 3 | X position scale per det |
| `correction_e_KE.dat` | Option 2 | Option 3 | Kinematically refined energy calibration |
| `correction_coinTime.dat` | Option 8 | Option 3 | Trigger time vs X correction (pol7, 9 params) |
| `correction_rdt.dat` | Manual | Option 3 | RDT energy calibration |

> After Option 0: `ln -sf correction_e_alpha.dat correction_e.dat`
> After Option 2: `ln -sf correction_e_KE.dat correction_e.dat`
> Use symlinks so you always know which calibration file is active (`ls -la correction_e.dat`).

---

## Notes

- All 24 detectors indexed 0–23, matching `GeneralSortMapping.h`
- **Det index 11 is always disabled — it is a broken/dead detector.** Hardcoded scaleX=1.0 in `Cali_scale_x.C` as a placeholder. Exclude from all analysis.
- `Cali_compareF.C` uses Monte Carlo — more trials = better result but slower. 800 is a starting point, use 2000+ for final calibration
- Coincidence time correction requires trace data (`te_t` branch) — only available if EventBuilder run with trace mode (`isBuild >= 2`)
- `reaction.dat` holds pre-computed relativistic kinematics parameters (mass, charge, beta, Et) — generated by Cleopatra/Transfer

---

## Step 5 — exShift Iteration (Post-Calibration, in Monitors.C)

After completing the 4-step calibration pipeline and applying RDT cuts, Ex peaks from individual detectors will have small systematic offsets. Correct these with `exShift[]` in `Analyzer.C`.

**Procedure:**
1. Set all `exShift[i] = 0`, run Monitors.C with RDT cut applied
2. Plot per-detector Ex histograms (`hExi`)
3. Read peak positions (use weighted cluster mean, NOT peak bin — see below)
4. g.s.-only dets: `exShift = 0.000 − observed_peak`
5. 4.4-only dets (¹²C): `exShift = 4.439 − cluster_mean` (weighted mean over 4.0–5.0 MeV)
6. Iterate 2–5 times until converged

**Key rules:**
- **Use cluster mean, not peak bin** — peak-bin picking creates asymmetric tails that prevent convergence
- Iterative — binning effects shift apparent peaks; single-pass never fully converges
- **Drop dets with >1 MeV shift** — indicates bad energy calibration, not a simple offset; recalibrate
- Final exShift values should be < 0.5 MeV
- After convergence, have Ryan verify Ex vs DetID and total Ex plots
- Full lessons and h095 final values in `calibration_notes.md`

---

## See Also

- `calibration_notes.md` — Detailed lessons, coinTime arch, xnCorr, exShift convergence records ⭐
- `HELIOS_Calibration_Procedure.md` — Manual calibration procedure (step-by-step)
- `new_experiment_checklist.md` — New experiment setup (calibration phase)
- `HELIOS_Analysis_Workflow.md` — Full analysis pipeline context
- `expMemory_h094.md` / `expMemory_h095.md` — Experiment-specific calibration values
