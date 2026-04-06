# HELIOS Analysis Workflow Reference

**Source:** Mac2020 (192.168.1.164) `~/digios/analysis/`
**Generated:** 2026-03-12

---

## System Overview

| Host | Role |
|---|---|
| digios1 (192.168.1.2) | Raw data acquisition → `.gtd` files |
| Mac2020 (192.168.1.164) `phywl094` | Primary analysis machine — EventBuilder, ROOT, Monitors |
| Mac2017 (192.168.1.193) | Grafana/InfluxDB slow-control only |
| LCRC (Argonne HPC) | Archival + parallel/batch analysis via Globus |
| Pi (192.168.1.100) | HELIOS AI ☀️ |

---

## Directory Structure (Mac2020 `~/digios/`)

```
digios/
├── heliosrc.sh              ← source this first to set env
├── expName.sh               ← experiment name, data path, last run number
├── analysis/
│   ├── working/             ← HELIOSSYS/analysis/working = HELIOSANA
│   │   ├── GeneralSortMapping.h   ← ⭐ TRUE channel mapping (source of truth)
│   │   ├── Analyzer.C/.h          ← ROOT TSelector event-by-event analysis
│   │   ├── Monitors.C/.h          ← online/offline histogram monitoring
│   │   ├── ChainMonitors.C        ← chain multiple runs for Monitors
│   │   ├── reactionConfig.txt     ← reaction kinematics config
│   │   ├── detectorGeo.txt        ← physical array geometry
│   │   ├── Simulation_Helper.C    ← GUI for kinematics/DWBA simulation
│   │   ├── rootlogon.C            ← ROOT startup
│   │   └── correction_*.dat       ← calibration correction files
│   ├── Armory/              ← shared utility scripts and macros (on PATH)
│   │   ├── Process_RUN      ← ⭐ main entry point for analysis
│   │   ├── process_Sort     ← EventBuilder step
│   │   ├── process_Download ← rsync raw data from DAQ
│   │   ├── process_PathSetting ← sets all path variables
│   │   ├── Apollo.C/.h      ← core analysis library
│   │   ├── Cali_*.C         ← calibration routines
│   │   ├── Check_*.C        ← diagnostic checks
│   │   └── GetDataFromInfluxDB.py ← pull slow-control data
│   ├── EventBuilder/        ← C++ event builder binary
│   │   ├── EventBuilder_S   ← ⭐ standard event builder binary
│   │   ├── EventBuilder_S.cpp
│   │   └── makefile
│   ├── data/                ← raw .gtd files (synced from DAQ)
│   ├── root_data/           ← sorted ROOT files output
│   ├── Cleopatra/           ← kinematics & DWBA interface
│   │   ├── Cleopatra.C/.sh  ← wrapper for Ptolemy
│   │   └── DWInFileCreator.C
│   └── Woods-Saxon/         ← Woods-Saxon potential tools
└── daq/                     ← DAQ scripts (see HELIOS_DAQ_Workflow.md)
```

---

## Environment Setup

Always source `heliosrc.sh` before any analysis work:

```bash
cd ~/digios
source heliosrc.sh
```

This sets:

| Variable | Value | Description |
|---|---|---|
| `HELIOSSYS` | `~/digios` | Root of digios repo |
| `HELIOSDAQ` | `$HELIOSSYS/daq` | DAQ scripts |
| `HELIOSANA` | `$HELIOSSYS/analysis/working` | Analysis working dir |
| `PATH` | + `Armory/`, `Cleopatra/`, `daq/edm/scripts/` | Tool paths |
| `expName` | e.g. `h094_19Ne_pp` | Current experiment |
| `daqDataPath` | e.g. `/media/DIGIOSDATA6` | Data disk on DAQ |
| `LastRunNum` | e.g. `60` | Last completed run number |

---

## Main Entry Point: `Process_RUN`

Located in `Armory/`, available on PATH after sourcing `heliosrc.sh`.

```bash
cd $HELIOSANA
Process_RUN [RunNum] [EventBuild] [Monitor] [SaveTrace]
```

### Arguments

| Argument | Values | Description |
|---|---|---|
| `RunNum` | integer or `lastRun` | Run number to process |
| `EventBuild` | `0` = skip, `1` = build, `n>1` = build+trace, `-1` = force build, `-n` = force+trace | Event building mode |
| `Monitor` | `0` = none, `1` = single run, `2` = chain list, `10` = single+post web, `20` = chain+post web | Monitoring mode |
| `SaveTrace` | `0` / `1` | Save trace data (overridden when trace analysis enabled) |

### Typical Usage

```bash
# Process run 61, full pipeline (default: build + monitor)
Process_RUN 61

# Process last run
Process_RUN lastRun

# Process run 61, force rebuild, with monitoring
Process_RUN 61 -1 1

# Process run 61 with trace analysis
Process_RUN 61 2 1
```

---

## Practical Calibration + Analysis Workflow

### Phase 1 — Alpha Source Calibration

```bash
cd $HELIOSANA

# Step 1: Sort the alpha run (no monitor needed)
Process_RUN [alphaRun] 1 0

# Step 2: Run calibration macro interactively
root -l "AutoCalibrationTrace.C"
#   → option 0 : energy + XF/XN calibration (saves correction_e_alpha.dat, correction_xf_xn.dat)
#   → option 5 : x-scale normalization      (saves correction_scaleX.dat)
#   → option 1 : XF+XN → E calibration      (saves correction_xfxn_e.dat)

# Step 3: Activate alpha energy calibration via symlink
ln -sf correction_e_alpha.dat correction_e.dat

# Step 4: Generate calibrated ROOT file
root -l "AutoCalibrationTrace.C"
#   → option 3 : generates h094_19Ne_pp_gen_run[alphaRun].root
```

### Phase 2 — Beam Run + Monitor Check

```bash
# Step 5: Sort beam run and run Monitors.C
Process_RUN [beamRun] 1 1

# Step 6: Check Monitors.C histograms — verify calibration quality
# Look for: clean alpha peaks, x uniform distribution, z positions correct
```

### Phase 3 — Kinematic Refinement (if states visible)

```bash
root -l "AutoCalibrationTrace.C"
#   → option 2 : kinematic auto-calibration
#                Sub-step 1: generate temp.root
#                Sub-step 2: run Cleopatra/Transfer → transfer.root
#                Sub-step 3: Monte Carlo minimization (saves correction_e_KE.dat)

# Activate kinematically refined calibration
ln -sf correction_e_KE.dat correction_e.dat

# Regenerate calibrated ROOT file with refined calibration
root -l "AutoCalibrationTrace.C"
#   → option 3

# Re-run monitors to verify improvement
Process_RUN [beamRun] 0 1   # 0 = skip EventBuild, just re-run monitors
```

### Check which calibration is active at any time:
```bash
ls -la correction_e.dat
# e.g.: correction_e.dat -> correction_e_KE.dat  (kinematic)
#   or: correction_e.dat -> correction_e_alpha.dat (alpha only)
```

---

## Pipeline: Step by Step

### Step 1 — `process_Download` (rsync raw data)

- **Only runs on Mac2020 or heliosdb** (hostname check)
- `rsync`s from digios1 (192.168.1.2):
  - `{daqDataPath}/{expName}/data/{expName}_run_{RUN}.gtd01–04` → `analysis/data/`
  - `RunTimeStamp.dat` → `analysis/data/`
  - `expName.sh` → `$HELIOSSYS/`
- Smart: skips files already up to date

### Step 2 — `process_Sort` (EventBuilder)

- Compiles `EventBuilder_S` from `analysis/EventBuilder/`
- Event window: **1000 ticks = 10 µs** (coincidence window)
- Checks timestamps: skips if ROOT file newer than raw data
- Force rebuild with negative `isBuild` flag

**Input:** `analysis/data/{expName}_run_{RUN}.gtd01–04`

**Output:**
- Normal: `analysis/root_data/gen_run{RUN}.root`
- With trace: `analysis/root_data/trace_run{RUN}.root`

### Step 3 — `ChainMonitors.C` (ROOT monitoring)

- Runs `Monitors.C` histograms over sorted ROOT file
- Single run or chain from `runsList.txt`
- Optional: posts results to web server

---

## Key Config Files (per experiment — update each run)

### `expName.sh`
```bash
expName=h094_19Ne_pp       # experiment label
daqDataPath=/media/DIGIOSDATA6  # raw data disk on DAQ
LastRunNum=60              # last completed run
```

### `reactionConfig.txt` (current: h094_19Ne_pp)
```
beam:    19Ne  (A=19, Z=10), 9.0 MeV/u
target:  p     (A=1,  Z=1)  — actually CD₂ target
recoil:  p     (A=1,  Z=1)
decay:   to 15O (A=15, Z=8)
target density: 0.913 g/cm³, thickness: 2.2×10⁻⁴ cm
SRIM files: 20F_in_CD2.txt, 3H_in_CD2.txt
```

### `detectorGeo.txt` (current geometry)
```
B-field:          -2.85 T
Bore:             462.5 mm diameter
Detector radius:  11.5 mm from beam axis
Detector width:   10.0 mm
Detector length:  50.0 mm
First det pos:    +520 mm (upstream, - = upstream convention)
Det per side:     4
Det positions:    520.0, 461.4, 402.1, 343.2 mm (approx, from file)
Recoil position:  350 mm downstream
Recoil inner r:   10.0 mm
Recoil outer r:   40.2 mm
```

---

## Channel Mapping — `GeneralSortMapping.h`

⭐ **This is the authoritative source for channel-to-detector mapping.**
Updated each experiment when cables are changed.

Key arrays:
- `idDetMap[160]` — maps digitizer channel index → detector ID
- `idKindMap[160]` — maps digitizer channel index → signal type (0=E, 1=XF, 2=XN)
- Channel index = (board_number × 10) + channel, board order follows VME01–04 MDIG1–4

See `~/HELIOS_Detector_Geometry.md` for full parsed tables.

---

## Calibration Files (in `working/`)

| File | Purpose |
|---|---|
| `correction_e.dat` | Energy calibration coefficients |
| `correction_e_KE.dat` | Energy calibration (kinematic correction) |
| `correction_xf_xn.dat` | XF/XN position calibration |
| `correction_xfxn_e.dat` | Position-energy cross correction |
| `correction_scaleX.dat` | X position scale correction |

Calibration routines: `Armory/Cali_*.C`

---

## DWBA / Kinematics

```bash
cd $HELIOSANA
root -l Simulation_Helper.C   # GUI launcher for kinematics + DWBA
```

Or directly:
```bash
Cleopatra.sh    # runs Ptolemy DWBA code
```

Input files: `DWBA.in`, `DWBA.Ex.txt`, `DWBA.Xsec.txt`
Output: `DWBA.out`, `Ex.txt`

---

## Data Flow Summary

```
digios1 (DAQ)
  └── raw .gtd01–04 files
        ↓ rsync (process_Download)
Mac2020 analysis/data/
        ↓ EventBuilder_S (process_Sort, 10µs window)
analysis/root_data/gen_run{RUN}.root
        ↓ ChainMonitors.C / Analyzer.C (ROOT TSelector)
Histograms, calibrated spectra, excitation energy spectra
        ↓ Globus (when enabled)
LCRC /lcrc/project/HELIOS/experimentsData/{expName}/
```

---

## Useful Aliases (from heliosrc.sh)

| Alias | Action |
|---|---|
| `gotoAna` | `cd $HELIOSANA` |
| `gotoDaq` | `cd $HELIOSDAQ` |
| `gotoExp` | `cd $HELIOSSYS` |
| `gotoRawData` | `cd {daqDataPath}/{expName}` |
| `LastRunNum` | Print current experiment + last run number |
| `ShowRunSize [N]` | Show file size of run N |
| `ShowRunTimeStamp` | Print run timestamp log |
| `AutoStartStop` | Automated run start/stop |
| `SetThreshold` | `SetVMEThreshold` script |
| `SetTrigger` | `SetVMETrigger` script |

---

## Monitors.C — Key User Settings (top of file)

Edit these before running to match the experiment:

| Parameter | Default | Description |
|---|---|---|
| `rawEnergyRange` | 1000–3000 | Raw ADC energy range |
| `energyRange` | 1–20 MeV | Calibrated E-Z plot range |
| `exRange` | −2 to +10 MeV (30 keV bins) | Excitation energy range |
| `timeGate` | −30 to +20 ch | Coincidence time gate (1 ch = 10 ns) |
| `eCalCut` | 0.5–50 MeV | Valid calibrated energy range |
| `xGate` | 0.8 | Cut out edges of detector (|x| < xGate) |
| `skipDetID` | {2, 11, 20, 21} | ⚠️ Detectors to skip — det 11 always here |
| `rdtCutFile1/2` | `rdtCuts_Ne.root`, `rdtCuts_O.root` | RDT particle ID cuts |
| `thetaCMGate` | 10 deg | Minimum CM angle cut |
| `isUseRDTTrace` | true | Use RDT trace timing |

---

## Notes

- ⚠️ **Pi working directory (MANDATORY):** All analysis work on Pi lives in `~/digios_11C_2/analysis/working_Helios/`
  - h095 files: root of that dir
  - h094 files: `~/digios_11C_2/analysis/working_Helios/h094_cuts/`
  - Future experiments: create `~/digios_11C_2/analysis/working_Helios/<expName>/` subdirs
  - Generated PNGs → `~/screenshots/` only; never scatter to home dir or workspace
- ⚠️ **`analysis/working/` is experiment-specific** — all files here (Monitors.C, GeneralSortMapping.h, reactionConfig.txt, detectorGeo.txt, correction_*.dat, rdtCut*.root, etc.) change per experiment
- ⚠️ **`analysis/Armory/`, `Cleopatra/`, `EventBuilder/`, `Woods-Saxon/`** are general/shared — independent of experiment, do not edit casually
- ⚠️ `GeneralSortMapping.h` on Mac2020 is the **true correct map** — verify it matches DAQ's copy each experiment
- ⚠️ Do not use `GLBL:DIG:*` PVs — use individual `VMExx:MDIGn:*` PVs directly
- Globus transfer to LCRC is currently **disabled** in stop_run.sh
- AutoProcess on Mac2020 is triggered by DAQ's AutoStartStop for online monitoring during long runs
- Mac2020 hostname: `phywl094.phy.anl.gov`
