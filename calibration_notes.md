# calibration_notes.md — HELIOS Alpha Calibration Reference

_Lessons learned from h095 (¹¹C(d,p)) and h094 (¹⁹Ne(p,p))_

---

## 4-Step Pipeline (MANDATORY — in order)

1. **Energy cal** → `correction_e_alpha.dat` (symlink `correction_e.dat`)
2. **Xf/Xn gain match** → `correction_xf_xn.dat`
3. **Xs→E linearity** → `correction_xfxn_e.dat`
4. **X scale** → `correction_scaleX.dat`

Never stop at energy alone. Never copy Ryan's params — generate from scratch.

---

## correction_e_alpha.dat Format (CRITICAL)

Monitors.C formula: `eCal = e_ch / eCorr[0] + eCorr[1]`
- `eCorr[0]` = gain (ch/MeV)
- `eCorr[1]` = offset **in MeV** (must be ~0, typically ±0.1 MeV)
- **NEVER store raw channel offset** — gets interpreted as MeV → completely wrong energies
- If fitting `ch = gain*E + offset_ch`: convert via `offset_MeV = offset_ch / gain`
- **Best practice: use AutoFit (TSpectrum)** — fits in MeV space, offsets naturally ~0

---

## Energy Calibration — Peak Identification

- **Anchor on ²¹²Po (8.785 MeV) first** — isolated, always visible
- Use predicted positions from ²¹²Po to verify all other peak identities before fitting
- **5.340 and 5.423 MeV peaks are unreliable** — straggling tails, often merged/misidentified
- Primary peaks: **5.685, 6.051, 6.288, 6.778, 8.785 MeV**
- 5-peak dets: {5.340, 5.685, 6.288, 6.778, 8.785}
- 4-peak dets: {5.423, 6.288, 6.778, 8.785}
- For poor-resolution dets: drop unresolvable peaks rather than fit them badly
- Residuals > 50 keV on any peak = something wrong

## AutoFit (TSpectrum) beats manual Gaussian

- TSpectrum does background subtraction before peak finding — removes continuum bias
- Manual fitting = fallback for TSpectrum failures (merged peaks, broad dets, low stats)

## Consistency Check

- Overlay **each det individually vs Det 00** (best reference)
- **Label EvsDet plot with DetID numbers**
- Print fitted centroids + residuals for every peak

---

## Xf/Xn Gain Matching — Physics

PSD silicon strip: charge splits between two ends.
- **Charge conservation**: `Xf + k·Xn = const` at fixed energy → anti-diagonal on Xn-vs-Xf plot
- `k = xnCorr` written to `correction_xf_xn.dat`

### Extracting xnCorr
1. Gate on ²¹²Po (8.785 MeV) — isolated, high energy, best lever arm
2. Plot **Xn vs Xf** → anti-diagonal stripe
3. Fit line `Xn = p0 + p1·Xf`
4. **xnCorr = −1 / p1**

### What NOT to Do
- ❌ `mean(Xn)/mean(Xf)` — gives source position on strip, not gain ratio
- ❌ `mean(E−Xf)/mean(Xn)` — biased by pedestals
- ❌ Line through origin on Xn-vs-Xf — pedestal offset makes this wrong

### Verification
- After applying xnCorr: plot `(Xfcal + Xncal)` vs `E` — should be tight diagonal
- h095 xnCorr range: ~0.92–1.11
- Det 20 (h095): band cut `1900 < Xf+Xn < 2500` for xnCorr fit

---

## X Scale Calibration

### Physical Model (use X in [−1, +1])
- Both signals: `X = (xfcal − xncal) / e_raw`
- xf only: `X = 2·xfcal/e − 1` → piles at +1
- xn only: `X = 1 − 2·xncal/e` → piles at −1
- **xScale = position of the strongest edge peak** from X projection

### ⚠️ X Range Rule (MANDATORY)
- ALL X calculations must produce X in **[−1, +1]**
- Monitors.C uses [0, 1] internally — this is wrong convention, do NOT copy it

### Method
1. Include ALL events (both-signal AND single-signal edge-recovery)
2. Plot X projection per det
3. **Look at the plot** — peak is obvious
4. Gaussian fit to strongest edge peak → centroid = xScale

---

## exShift Calibration — Method

### Procedure
1. Set all exShift = 0, run Monitors with RDT cut
2. Plot per-detector Ex histograms (hExi)
3. Read peak positions by eye (low stats → no Gaussian fits)
4. g.s.-only dets: `exShift = 0.000 − observed_peak`
5. 4.4-only dets: use **cluster mean** (weighted mean 4.0–5.0 MeV), NOT peak bin; `exShift = 4.439 − cluster_mean`
6. Iterate 2–5 times until converged
7. After convergence, have Ryan check Ex vs DetID and total Ex plots

### Key Rules
- **Cluster mean > peak bin** — peak-picking creates asymmetric tails
- **Iterative** — binning effects shift apparent peaks
- **Drop dets with >1 MeV shift** — bad energy calibration, not simple offset
- exShift should be < 0.5 MeV

---

## h095 Final exShift Values (iteration 5)

```
Det 00: +0.17    Det 06:  0.00    Det 12: +0.45    Det 18: +0.15
Det 01: +0.22    Det 07:  SKIP   Det 13: +0.27    Det 19:  0.00
Det 02: -0.08    Det 08: +0.01   Det 14: +0.16    Det 20: -0.01
Det 03: -0.06    Det 09: -0.10   Det 15: -0.07    Det 21: -0.07
Det 04: -0.01    Det 10: -0.24   Det 16: -0.06    Det 22:  SKIP
Det 05: +0.11    Det 11:  SKIP   Det 17:  SKIP    Det 23: +0.06
```
- g.s. FWHM: 193 keV, 4.4 MeV FWHM: 225 keV, g.s./4.4 ratio: 0.64

---

---

## RDT Coincidence Timing — dE vs E Channel Behavior (Maybe General — Found in h095)

_Observed 2026-04-03 in h095 trace_run014 (Plots 015–018). May apply generally but not yet confirmed in other experiments._

### RDT Branch Layout
- `rdt[2i]`   = **dE** (thin detector, even index, ADC max ~4500 ch)
- `rdt[2i+1]` = **E**  (thick detector, odd index, ADC max ~8500 ch)
- `rdt_t[2i]` / `trdt_t[2i]`   = dE timing (even)
- `rdt_t[2i+1]` / `trdt_t[2i+1]` = E timing (odd)

### dE vs E Give Different coinTimeUC Distributions
- Using **dE (even)** vs **E (odd)** timestamps for `rdtt_best` produces **different coinTimeUC arch shapes and offsets** — they are NOT interchangeable.
- The difference is physical: dE and E are separate detectors with different cable lengths, signal rise times, and digitizer channels.
- **Always use the same channel consistently** across correction fitting and physics analysis.

### Which Channel to Use
- **Monitors.C uses dE (even)** for the coincidence gate: `tdiff = rdt_t[j] - e_t[detID]` where j loops over dE channels `{0,2,4,6}`.
- For coinTimeUC (trace-based): use **dE (even)** to match Monitors.C convention.
- If you switch channels: **regenerate the poly correction coefficients** — the arch shape changes completely.

### Source of the coinTimeUC Arch (Confirmed in h095)
- **`te_r` (array trace timing) vs X** → shows clear parabolic arch — this IS the position walk
- **`trdt_t(dE)` vs X** → flat, no arch (horizontal band ~100–110 ticks, no X-dependence)
- **Conclusion: the arch comes entirely from `te_r` (PSD silicon strip), NOT from the RDT**
- The RDT timing is X-independent; the walk is purely a strip charge-propagation effect

### Cross-Channel Correction (Observed in h095)
- The poly correction fit on coinTime(E) **can be applied to coinTime(dE)** and vice versa — the X-dependent arch shape is shared between channels.
- Physical reason: the arch is caused by position-dependent signal propagation along the PSD silicon strip (array property), not the RDT. Both dE and E see the same array timing, so the walk correction is channel-independent.
- The absolute offset between dE and E remains — only the arch shape transfers, not the zero point.

### Practical Check
- When comparing coinTimeUC plots generated by different scripts, always verify which RDT channel was used for `rdtt_best`.
- Mismatch = systematic offset of ~50–100 ns between scripts — looks like a calibration error but is just a channel choice difference.

---

_Updated: 2026-04-03_
