# HELIOS Silicon Detector Calibration Procedure

A methodology guide for manual calibration of PSD silicon detectors using ²²⁸Th alpha sources.
Covers energy calibration, Xf/Xn gain matching, and position reconstruction.

> **See Also:**
> - `HELIOS_Calibration_Workflow.md` — AutoFit/AutoCalibrationTrace scripts, automation pipeline
> - `calibration_notes.md` ⭐ — lessons learned, xnCorr gotchas, exShift iteration procedure
> - `new_experiment_checklist.md` — required files list for new experiments

---

## Overview

> ⚠️ **MANDATORY ORDER — do not skip or reorder steps:**
> 1. **Energy calibration** → `correction_e_alpha.dat` (symlink `correction_e.dat`)
> 2. **Xf/Xn gain match** → `correction_xf_xn.dat`
> 3. **Xs→E linearity** → `correction_xfxn_e.dat`
> 4. **X scale** → `correction_scaleX.dat`
>
> Each step depends on the previous one. Running out of order produces wrong results.

Each stage is a sanity check on the previous one. Nothing is trusted until cross-checked visually and numerically.

---

## Stage 1 — Energy Calibration

### 1.1 Plot the raw energy spectrum first
Before fitting anything, plot the raw channel histogram and *look* at it.
- Count peaks visually and estimate positions by eye
- Check that the detector is working (not dead, not saturated)
- Look for obvious problems: missing peaks, unusual background, dead regions
- This visual inspection sets expectations before any automated analysis

### 1.2 Peak identification before calibration
You must identify *which physical peak is which* before you can calibrate.

For the ²²⁸Th decay chain, the known alpha energies are:

| Isotope | Energy (MeV) | Notes |
|---|---|---|
| ²²⁴Ra | 5.34 | Often broad (energy straggling in source) |
| ²²⁸Th | 5.42 | Close to ²²⁴Ra — may be unresolved |
| ²²⁴Ra | 5.68 | Typically the tallest peak |
| ²¹²Bi | 6.05 | Smaller (36% branch) |
| ²²⁰Rn | 6.29 | |
| ²¹⁶Po | 6.78 | |
| ²¹²Po | 8.79 | Isolated, high energy — unmistakable anchor |

**Start assignment from ²¹²Po (8.79 MeV)** — it is isolated, high energy, and unambiguous. Work inward from there.

Be careful with the 5.34/5.42 MeV pair — they may appear as a single broad peak or a shoulder. Do not force two Gaussians if the resolution doesn't support it.

### 1.3 Fit peaks — don't just eyeball centroids
Fit each peak with a Gaussian to extract the centroid and width (σ).
- Fitted centroids are more accurate than bin maxima
- σ is physically informative: broad peaks (e.g. 5.34 MeV ²²⁴Ra) indicate energy straggling in the source material, not detector noise — that's physics, not a calibration artifact
- Check that fit quality looks reasonable before using centroid values

### 1.4 Linear fit for energy calibration
Alpha sources give a clean linear E vs. channel relationship:
```
E(MeV) = a × ch + b
```
- Use as many well-resolved peaks as possible for the fit
- Check residuals on *all* peaks, including ones not used in the fit
- Residuals reveal: linearity assumption validity, systematic offsets, misidentified peaks
- Typical good result: residuals within ±15–20 keV across the full range

### 1.5 Sanity checks
- Does the slope make physical sense? (~3–5 keV/ch for typical HELIOS PSD setup)
- Is the offset near zero? (large offset may indicate pedestal issue)
- Are peak widths consistent with expected detector resolution?

---

## Stage 2 — Xf/Xn Gain Matching

### 2.1 Why gain matching is needed
Each PSD silicon strip has two readout ends: Xf (front) and Xn (back). Their electronics chains are independent and will not have perfectly matched gains out of the box. If unmatched, the position reconstruction is systematically biased.

### 2.2 Diagnosing gain mismatch
Plot the raw position asymmetry:
```
x_raw = (xf - xn) / (xf + xn)
```
- If gains are matched: distribution is centered at 0
- If shifted: the side with higher gain is pulling the centroid
- The magnitude of the shift tells you the correction needed

### 2.3 Finding xnCorr
Introduce a correction factor `gn` applied to Xn:
```
x = (xf - xn × gn) / (xf + xn × gn)
```
Scan `gn` until the distribution is centered at 0. This is `xnCorr`.

For det 06 (h094): `xnCorr = 0.9263` (Xn gain was ~7.95% high)

### 2.4 E-scale correction
After gain matching, check the E vs. (xf+xn) correlation. If `(xf+xn) ≠ e` systematically, an additional energy scale factor may be needed:
```
xcal = xfcal / (e × scaleE)
```
For det 06 (h094): `scaleE = 1.0263`

---

## Stage 3 — Position Calibration and Edge Recovery

### 3.1 The standard position formula
With both Xf and Xn above threshold:
```
xcal = 0.5 + 0.5 × (xfcal - xncal) / e      [range: 0 to 1, Monitors.C convention]
x    = (xf - xn × gn) / (xf + xn × gn)       [range: -1 to 1, calibration convention]
```

### 3.2 Edge recovery — critical for statistics
When a particle hits near a strip end, one of the two signals may fall below threshold. Without edge recovery, these events are lost. With edge recovery (Monitors.C lines 735–737):

| Condition | Formula | Physical meaning |
|---|---|---|
| Both Xf & Xn valid | `xcal = 0.5 + 0.5*(xfcal-xncal)/e` | Standard reconstruction |
| Only Xf valid (Xn below threshold) | `xcal = xfcal/e` | Particle near XF end |
| Only Xn valid (Xf below threshold) | `xcal = 1 - xncal/e` | Particle near XN end |

**Always check what fraction of events you're losing by requiring both signals.** If only 10% of events pass a tight X gate, edge recovery is critical. The correction files must exist for Monitors.C to apply edge recovery.

### 3.3 Required correction files (in `analysis/working/`)

| File | Format | Description |
|---|---|---|
| `correction_xf_xn.dat` | one value per det | `xnCorr[i]` — Xn gain correction |
| `correction_xfxn_e.dat` | two values per det: offset, slope | E-scale correction |
| `correction_scaleX.dat` | one value per det | X position scale |

Without these files, Monitors.C cannot perform edge recovery and 90%+ of events near strip ends will be lost.

### 3.4 Correct edge recovery formula
When one signal is missing, reconstruct the missing signal from charge conservation (`xf + xn ≈ e`):

```
xn_missing: x = (xf - xn) / e = (xf - (e - xf)) / e = (2*xf - e) / e
xf_missing: x = (xf - xn) / e = ((e - xn) - xn) / e = (e - 2*xn) / e
```

This is exact as long as `xf + xn ≈ e` holds (verified: mean ratio ~0.97 for both-signal events).

**Important:** verify `(xf + xn) / e` before applying edge recovery. If the ratio deviates significantly from 1, the formula breaks down.

### 3.5 Understanding the threshold boundary
The raw X distribution with edge recovery included shows sharp peaks near the physical ends of the detector. These peaks mark where one signal drops below the hardware threshold — NOT the physical edge of the silicon.

- Plot Xf and Xn separately (log scale) to find the actual threshold (~270 ch for det 06)
- The threshold boundary appears as a sharp cliff in the X distribution, with a pile-up peak just inside it
- Below threshold, the missing signal is reconstructed via the edge formula — these events cluster at the threshold X position

### 3.6 xScale calibration — methodology
The X position scale corrects for the fact that the threshold boundary does not naturally fall at ±1.

**Procedure:**
1. Plot the full X projection including edge-recovered events
2. Fit a Gaussian to the edge pile-up peak on each side
3. Use the **largest peak centroid** (highest statistics, most reliable) as the scale reference
4. `xScale = 1.0 / |peak_centroid|`

**Why peak centroid, not 50% level:**
- The 50% level depends on the edge slope, which is threshold- and statistics-dependent
- The peak centroid is a stable physical reference with well-defined uncertainty from the Gaussian fit
- E, Xf, and Xn all have measurement uncertainty; the peak position accounts for this naturally

**Physical note:** xScale is NOT a physical detector length calibration. It maps the threshold boundary to ±1 as a convenient normalization. True physical Z calibration requires independent geometric reference (e.g. kinematic lines from a known reaction).

**For det 06 (h094):** right edge peak at X=0.7439±0.0005, left edge at −0.6683±0.0035, `xScale = 1.3443`

### 3.7 X gate after scaling
After applying xScale, apply an |X| < 0.95 cut to remove events in the edge pile-up region. These events have reconstructed positions from the edge formula and may have degraded energy resolution due to bulk charge loss near the strip ends.

- The |X| < 0.95 cut after scaling removes ~21% of events (det 06: 24,761 → 19,484)
- Verify the cut by checking that the E vs X bands remain flat after the cut
- If bands show energy droop near the cut edge, tighten the cut

---

## General Principles

### Eyes first, automation second
- Always look at the plot *before* trusting any fitted value
- TSpectrum and automated peak finders are tools, not answers
- Fitters can latch onto noise, split real peaks, or miss shoulders
- If TSpectrum disagrees with your eye, trust your eye first, then investigate

### Every step is a sanity check
- Energy calibration validates peak identification
- Gain matching validates position reconstruction
- Edge recovery validates event statistics
- Residuals validate the linear model

### Peak width is physics
- Sharp peaks (σ ~ 5–7 ch): good detector, thin source
- Broad peaks (σ ~ 13 ch): energy straggling in source — not a problem, it's expected
- Anomalously broad peaks across all energies: check thresholds, check grounding

### When to be suspicious
- Residuals > 30 keV: wrong peak assignment or nonlinearity
- xnCorr far from 1.0 (e.g. > 20% correction): check cable connections or preamp gain settings
- Very few events passing both-signal requirement: thresholds too high, or gain matching off

---

## Experiment-Specific Calibration Records

Calibration results for individual experiments are **not** stored here.
- h094 calibration: see `expMemory_h094.md` (channel #h094_19ne_pp)
- h095 calibration: see `expMemory_h095.md` (channel #h095_11c_dp_2) and `calibration_notes.md`
- Per-experiment correction files live in `~/digios_11C_2/analysis/working_Helios/<expName>/`

---

*Last updated: 2026-04-07 — added See Also cross-references; moved stale status to expMemory files*
