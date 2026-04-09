# HELIOS Detector Geometry Reference

> ⚠️ **WARNING: This geometry is experiment-dependent.**
> Each experiment may have a different detector configuration, channel mapping, and number of active detectors.
> Always verify against `digios/analysis/working/GeneralSortMapping.h` for the current experiment.
>
> **Source for this document:** `GeneralSortMapping.h` + `HELIOSThresholds.edl` (read 2026-03-11)

---

## Detector Type Codes (`idDetMap`)

| Prefix | Type |
|---|---|
| 0XX | PSD silicon array (position-sensitive) |
| 1XX | Recoil detector (RDT) — dE must be odd ID |
| 2XX | ELUM (luminosity monitor) |
| 3XX | EZERO |
| 4XX | TAC & RF timing |
| 5XX | Circular recoil (CRDT) |
| 6XX | APOLLO |

## Signal Kind Codes (`idKindMap`)

| Value | Meaning |
|---|---|
| 0 | Energy (E) |
| 1 | XF (front position) |
| 2 | XN (back position) |
| -1 | Not in use |

## Signal Polarities

| Detector type | Polarity |
|---|---|
| PSD (XF/XN) | +1 |
| Recoil (RDT) | **−1** |
| ELUM | +1 |
| EZERO | +1 |
| CRDT | +1 |
| APOLLO | +1 |

---

## Current Geometry (as of 2026-03-11)

### RDT — Recoil Detectors
**VME01:MDIG1, channels 0–7**
Single-channel silicon detectors, 4 E-dE telescope pairs.

| Channel | Det ID | Kind | Notes |
|---|---|---|---|
| 0 | 100 | E | Recoil energy |
| 1 | 101 | dE | Recoil dE (thin) |
| 2 | 102 | E | Recoil energy |
| 3 | 103 | dE | Recoil dE (thin) |
| 4 | 104 | E | Recoil energy |
| 5 | 105 | dE | Recoil dE (thin) |
| 6 | 106 | E | Recoil energy |
| 7 | 107 | dE | Recoil dE (thin) |

> VME01:MDIG2, MDIG3, MDIG4 — not in use

---

### Silicon PSD Array — 24 detectors, 4 sides

Each detector has 3 signals: **E (energy)**, **XF (front position)**, **XN (back position)**

#### Left Side (Det 0–5)
| Channel | VME:MDIG | Det | Kind |
|---|---|---|---|
| ch7 | VME02:MDIG1 | 0 | E |
| ch6 | VME02:MDIG1 | 1 | E |
| ch5 | VME02:MDIG1 | 2 | E |
| ch4 | VME02:MDIG1 | 3 | E |
| ch3 | VME02:MDIG1 | 4 | E |
| ch2 | VME02:MDIG1 | 5 | E |
| ch7 | VME02:MDIG1 | 0 | XF |
| ch6 | VME02:MDIG1 | 1 | XF |
| ch5 | VME02:MDIG1 | 2 | XF |
| ch4 | VME02:MDIG1 | 3 | XF |
| ch3 | VME02:MDIG2 | 4 | XF |... (see idKindMap)
| ... | VME02:MDIG2 | ... | XN |

> Detailed per-channel kind from `idKindMap` (VME2-DIG1):
> ch0=XF, ch1=XF, ch2=E, ch3=E, ch4=E, ch5=E, ch6=E, ch7=E
> (VME2-DIG2): ch0=XN, ch1=XN, ch2=XN, ch3=XN, ch4=XF, ch5=XF, ch6=XF, ch7=XF

#### Bottom Side (Det 6–11)
| VME:MDIG | Channels | Det range |
|---|---|---|
| VME02:MDIG3 | ch0–ch7 | Det 4–11 (mixed E/XF/XN) |

> idKindMap (VME2-DIG3): ch0=E, ch1=E, ch2=E, ch3=E, ch4=E, ch5=E, ch6=XN, ch7=XN

#### Right Side (Det 12–17)
| VME:MDIG | Channels | Det range |
|---|---|---|
| VME03:MDIG1 | ch0–ch7 | Det 6–11 (mixed) |
| VME03:MDIG2 | ch0–ch7 | Det 8–15 (mixed) |
| VME03:MDIG3 | ch0–ch7 | Det 12–17 (mixed) |

#### Top Side (Det 18–23)
| VME:MDIG | Channels | Det range |
|---|---|---|
| VME04:MDIG1 | ch0–ch7 | Det 12–19 (mixed) |
| VME04:MDIG2 | ch0–ch7 | Det 18–23 (mixed) |
| VME04:MDIG3 | ch0–ch7 | Det 18–23 (mixed) |

---

## Full idDetMap / idKindMap (from GeneralSortMapping.h)

```
Board order: 10 channels per digitizer (ch0-ch7, ch8-ch9 unused)

VME01-MDIG1: DetMap= 101,100,103,102,105,104,107,106,-1,-1  (RDT)
VME01-MDIG2: DetMap= -1 x10  (unused)
VME01-MDIG3: DetMap= -1 x10  (unused)
VME01-MDIG4: DetMap= -1 x10  (unused)

VME02-MDIG1: DetMap=   1,  0,  5,  4,  3,  2,  1,  0,-1,-1  KindMap= 1,1,0,0,0,0,0,0
VME02-MDIG2: DetMap=   3,  2,  1,  0,  5,  4,  3,  2,-1,-1  KindMap= 2,2,2,2,1,1,1,1
VME02-MDIG3: DetMap=  11, 10,  9,  8,  7,  6,  5,  4,-1,-1  KindMap= 0,0,0,0,0,0,2,2
VME02-MDIG4: DetMap= -1 x10  (unused)

VME03-MDIG1: DetMap=   7,  6, 11, 10,  9,  8,  7,  6,-1,-1  KindMap= 2,2,1,1,1,1,1,1
VME03-MDIG2: DetMap=  15, 14, 13, 12, 11, 10,  9,  8,-1,-1  KindMap= 0,0,0,0,2,2,2,2
VME03-MDIG3: DetMap=  17, 16, 15, 14, 13, 12, 17, 16,-1,-1  KindMap= 1,1,1,1,1,1,0,0
VME03-MDIG4: DetMap= -1 x10  (unused)

VME04-MDIG1: DetMap=  19, 18, 17, 16, 15, 14, 13, 12,-1,-1  KindMap= 0,0,2,2,2,2,2,2
VME04-MDIG2: DetMap=  21, 20, 19, 18, 23, 22, 21, 20,-1,-1  KindMap= 1,1,1,1,0,0,0,0
VME04-MDIG3: DetMap=  23, 22, 21, 20, 19, 18, 23, 22,-1,-1  KindMap= 2,2,2,2,2,2,1,1
VME04-MDIG4: DetMap= -1 x10  (unused)
```

---

## Threshold PV Quick Reference

| Region | PVs | Channels |
|---|---|---|
| RDT energy | VME01:MDIG1:led_threshold0–7 | ch0–7 |
| Left energy | VME02:MDIG1:led_threshold2–7 | ch2–7 |
| Bottom energy | VME02:MDIG3:led_threshold0–7 | ch0–7 |
| Right energy | VME03:MDIG1–3:led_thresholdN | various |
| Top energy | VME04:MDIG1–3:led_thresholdN | various |

---

## Notes
- `NARRAY=24` — 24 PSD silicon detectors total
- ⚠️ **Det index 11 is always broken/dead — always disabled in analysis**
- `NRDT=8` — 8 RDT channels (4 E-dE pairs)
- `MWIN=100` — M-window value for energy filter (from digitizer setting)
- Each experiment: re-check `GeneralSortMapping.h` in `digios/analysis/working/`

## Experiment-Specific Known Issues

### h094 (¹⁹Ne(p,p))
- **Det 07** — Xn anomalous: `xnCorr ≈ 2.38` (typical ~0.92–1.11). Cause: cable or preamp issue. Still usable for energy; flag xn-based position.
- **Det 08, 09, 10** — Xn signal DEAD. Exclude from xnCorr fits and Xf+Xn sums. Xf-only position possible but degraded resolution.

### h095 (¹¹C(d,p))
- No known hardware dead channels beyond Det 11 (always dead).
- Det 20: requires band cut `1900 < Xf+Xn < 2500` for xnCorr fit (position cluster issue).

### h096 (³¹Si(d,p)³²Si)
- B = 2.85 T (rented power supply); magnet ramped 2026-04-08
- Experiment-specific detector issues TBD — update as calibration proceeds
- See `expMemory_h096.md` for current status

---

## See Also
- `HELIOS_PV_Reference.md` — EPICS PV names for thresholds, HV channels per detector
- `HELIOS_Calibration_Procedure.md` — calibration steps (energy, Xf/Xn, position)
- `calibration_notes.md` — xnCorr lessons, exShift iteration, dead detector handling
- `rdtCut_guideline.md` — RDT cut methods, FOM scoring, TObjArray format
- `expMemory_h094.md` / `expMemory_h095.md` — per-experiment detector status details
