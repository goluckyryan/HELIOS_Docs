# HELIOS DAQ Workflow

DAQ system overview, run control, and data pipeline.
Run start/stop details: use `helios-start-run` and `helios-stop-run` skills (source of truth).

---

## System Overview

| Component | Host | Role |
|---|---|---|
| digios1 (192.168.1.2) | DAQ PC (CentOS 6, 32-bit) | softIOC, data receiver, run control |
| Mac2020 (192.168.1.164) | iMac 2020 | Elog posting, Discord push, AutoProcess |
| Mac2017 (192.168.1.193) | iMac 2017 | Grafana/InfluxDB |
| VME01-04 (VxWorks) | VME crates | Hardware IOCs -- digitizers |
| VME32 (VxWorks) | VME crate | Trigger master + routers |
| Spark (192.168.1.101) | NVIDIA Jetson | HELIOS AI [sun] -- migrated from Pi5-2 (.100) 2026-04-17 |

### DAQ Disk Layout (digios1)

| Partition | Size | Used | Mount | Contents |
|---|---|---|---|---|
| /dev/sda2 | 96G | 22G | /home | User homes |
| /dev/sda6 | 256G | 64G | /global | EPICS environment, digios, data archives |

`/global/devel7_newbsp/` (5.5G) = active EPICS/digios env. `devel5/`, `devel6/` = older.

---

## Experiment Configuration

### `expName.sh` -- [!!] Always read live, never hardcode

Location: `/global/devel7_newbsp/gretTop/9-22/dgsIoc/scripts/expName.sh`

```bash
source /global/devel7_newbsp/gretTop/9-22/dgsIoc/scripts/expName.sh
echo "$expName | LastRunNum=$LastRunNum | dataPath=$daqDataPath"
```

Variables: `expName`, `daqDataPath`, `LastRunNum`

### `DataBaseAddress.sh`

```bash
dataBaseAddress=192.168.1.193   # Mac2017 (Grafana/InfluxDB)
mac2020IP=192.168.1.164         # Mac2020 (Elog/Discord)
```

---

## Key EPICS PVs

### Run Control (softIOC on digios1)

| PV | Values | Description |
|---|---|---|
| `Online_CS_StartStop` | `Start` / `Stop` | Start or stop acquisition |
| `Online_CS_SaveData` | `Save` / `No Save` | Enable/disable data saving |
| `DAQG_CS_BuildEnable` | `Copy` / ... | DAQ builder enable |
| `DigFIFOSpeed` | `Fast` / `Slow` | FIFO speed |

### Trigger Logic (Ryan, 2026-04-23)

**Simple two-mode trigger -- no complex coincidence logic ever used:**

| Mode | PV | Physics | When used |
|---|---|---|---|
| **X (SUM_X)** | `VME32:MTRG:SUM_X` | Any Si array detector above threshold → readout. Light reaction products (p,d,t) orbit upstream in B-field and hit array. Heavy elastic recoil goes forward → NOT captured. | Normal physics runs (99% of time) |
| **Y (SUM_Y)** | `VME32:MTRG:SUM_Y` | Any RDT fires → readout. Captures elastic scattered beam + reaction recoils + contaminants. No upstream particle required. | Beam characterization, rate estimation |
| **XY** | `VME32:MTRG:SUM_XY` | Coincidence -- **NEVER used** | N/A |

**Key physics of X vs Y:**
- In X: elastic beam (heavy recoil) is suppressed -- goes straight forward, no array hit. Reaction products dominate.
- In Y: elastic beam dominates (Rutherford XS >> transfer XS). RDT PID plot shows beam spot (¹⁶O etc.) + reaction recoils (¹⁷O etc.) + contaminants -- all separable by dE-E.
- Y generates far more data (elastic XS huge) -- used only in short dedicated runs.
- **[!!] Y trigger buffer risk:** Elastic XS >> transfer XS. At normal beam rates, Y trigger can fill the VME buffer in <1s -- the unprotectable fast-fill case. Always run Y trigger carefully: low beam rate, short duration, actively watch buffer. If buffer fills fast → VME crate reboot required.
- Even in X: residual beam-like events appear from C+beam reactions on CD₂ target (carbon background) -- gated out in analysis via RDT PID cuts.
- Y trigger used to: (1) check beam composition/contamination, (2) estimate absolute beam rate from elastic spot intensity.
- **TrigCPU/TrigIOC**: used only for firmware updates (never updated in practice) -- treat as inert.
- **PileUp**: likely always enabled (verify in IOC settings).

### Trigger PVs (VME32)

| PV | Description |
|---|---|
| `VME32:MTRG:SUM_X` | X-plane trigger sum on/off |
| `VME32:MTRG:SUM_Y` | Y-plane trigger sum on/off |
| `VME32:MTRG:SUM_XY` | XY coincidence trigger |
| `VME32:MTRG:XTHRESH` / `YTHRESH` | Trigger thresholds |

[!!] **DO NOT use `GLBL:DIG:*` PVs** -- not confirmed reliable. Use individual `VMExx:MDIGn:*` PVs.

### Router Map

| VME | DIG | Router | Symbol |
|---|---|---|---|
| VME01 | MDIG1-4 | RTR1 | A-D |
| VME02 | MDIG1-4 | RTR1 | E-H |
| VME03 | MDIG1-4 | RTR2 | A-D |
| VME04 | MDIG1-4 | RTR2 | E-H |

### Digitizer Defaults (`helios_setup_digitizer_4sidesArray`)

| Parameter | Default | Notes |
|---|---|---|
| `led_threshold` | 400 | Per-channel |
| `m_window` | 1.0 | |
| `disc_width` | 15 | |
| `raw_data_length` | 1.0 | Trace length |
| `raw_data_window` | 3.32 | Pre-trigger |
| `trigger_polarity` | Both | |
| `trigger_mux_select` | ExtTTCL | External trigger |
| `pileup_mode` | Accept | |
| `CFD_fraction` | 30 | |
| `peak_sensitivity` | 3 | |
| `cfd_mode` | LED_Mode | |
| `holdoff_time` | 140 | |

Per-experiment overrides: see `expMemory_<exp>.md`

---

## EDM Screens

Entry point: `~/digios/daq/heliosCommander` -> launches `HELIOSMain_4sidesArray.edl`

- [OK] **`HELIOSArraySettings_4sidesArray.edl`** -- REAL threshold screen, actively in use
- [X] **`HELIOSThresholds.edl`** -- STALE, wrong PVs, NOT used
- [!!] Many EDM screens are outdated -- do not treat as authoritative

---

## Run Control

### Starting a Run

Use the `helios-start-run` skill (source of truth). Key steps:
1. Collect shift info (target, beam, purpose, who's on shift)
2. Read live system state (`expName.sh`, trigger PVs)
3. Build elog entry, SCP to DAQ
4. Call `start_run.sh --ai` (handles: expName increment, caput Start, elog/Discord push, xterms)
   - [!!] `start_run.sh` includes **HV check** (snmpget outputSwitch) -- aborts if HV not on
   - [!!] **Stale Pi SSH in start_run.sh (line 105) AND stop_run.sh (line 75):** both call `ssh ryan@192.168.1.100 ...` -- non-fatal (background) but fails silently since Pi retired 2026-04-17. Both need update to `ssh heliosspark@192.168.1.101`. (DAQ read-only -- admin change required)

### Stopping a Run

Use the `helios-stop-run` skill (source of truth). Key steps:
1. Collect stop reason
2. Build stop elog comment, SCP to DAQ
3. Call `stop_run.sh --ai` (handles: caput Stop, Grafana screenshot, elog/Discord push, kill xterms)

### Quick Status Check

```bash
caget Online_CS_StartStop Online_CS_SaveData
# Running: Start / Save
# Idle: Stop / No Save
```

### Auto Run Control -- `AutoStartStop`

Two modes:
- `AutoStartStop time <minutes> [repeats]` -- stop after N minutes
- `AutoStartStop size <kB> [repeats]` -- stop after file size
- Repeat = -1 -> infinite. Sends AutoProcess trigger to Mac2020.

### Elog CLI (standalone notes)

```bash
~/bin/elog -s -p 443 -h elog.phy.anl.gov -l H096_31Si_dp \
  -u MasterHelios helios \
  -a Category=Other -a Subject="<subject>" \
  -n 2 -m /tmp/elog_note.txt
```

- `-n 2` = HTML, `-n 1` = plain
- Attach file: `-f <filepath>`
- Edit existing: `-e <id>` | Reply: `-r <id>`
- No delete via CLI -- use web UI
- Binary: `~/bin/elog` (v3.1.6, ANL CloudFlare-patched)

---

## Run Control from Spark

### Method A: X11 Forwarding (current method)

`start_run.sh --ai` launches `gtReceiver4` xterms with `DISPLAY=192.168.1.164:0`.

**Pre-req:** `xhost +192.168.1.2` on Mac2020 (once per XQuartz session).

`gtReceiver4` binary: `/home/helios/gtReceiver_digios/gtReceiver4` (NOT in PATH).

### Method B: tcpReceiver on Mac2020 (DROPPED 2026-04-24)

Dropped -- would require rewriting gtReceiver logic, too messy. Not used.

---

## Data Flow

**Confirmed architecture (2026-04-24):**
```
Detector
     |
Digitizers (VME)
     |
VME IOCs (VxWorks)
     |
DAQ/digios1 softIOC + gtReceiver4
     | .gtd01-.gtd04 -> {daqDataPath}/{expName}/
     |
Mac2020 downloads raw data from DAQ for online analysis
     | (AutoProcess on Mac2020)
ROOT files
     | (Globus, when enabled)
LCRC archival

Spark (.101) also downloads raw data from DAQ for AI-driven analysis
     | (ROOT, Python, Cleopatra, PtolmeyCpp)
```

**Note:** Mac2020 = elog/Discord/online display. Spark = AI analysis, simulation, DWBA. Both pull from DAQ independently.
```

Data files: `{daqDataPath}/{expName}/{expName}_run_{RUN}.gtd01-04`
DAQ data layout: flat `{daqDataPath}/{expName}/` only.
Mac2020: `~/experiments/{expName}/data` + `root_data`

---

## Slow Control / Monitoring

| System | Host | Protocol |
|---|---|---|
| InfluxDB | Mac2017 (.193) | :8086 HTTP |
| Grafana | Mac2017 | Web |
| Elog | elog.phy.anl.gov | HTTPS (port 443) |
| Discord | Mac2020 (.164) | push2Discord.sh |
| HV (Iseg) | .155 | SNMP |
| Vacuum | Edwards D379 | Serial via DAQ |

---

## Key Scripts (`~/digios/daq/edm/scripts/`)

| Script | Purpose |
|---|---|
| `start_run.sh` / `stop_run.sh` | Run control (use `--ai` flag from Spark) |
| `helios_setup_trigger` | Trigger router setup |
| `helios_setup_digitizer_4sidesArray` | Digitizer defaults |
| `start_run_Mac.sh` / `stop_run_Mac.sh` | Mac2020-side run control: SCP expName.sh from DAQ, GenElog+GenElogExtra -> elogFull.txt -> post to ANL elog -> Discord. stop saves elog ID for reply attachment. Run via SSH from DAQ. |
| `GenElog.py` | Main elog HTML body: run number, timestamp, comment, B-field, array/RDT positions, trigger settings. Usage: `GenElog.py start` -> ~/elog.txt |
| `GrafanaWeb.sh` | Grafana screenshot (macOS): `screencapture -D2 ~/grafanaElog.jpg` (monitor 2). Called by stop_run_Mac.sh on Mac2017. Web push disabled. |
| `GrafanaElog.sh` | Legacy Linux Grafana screenshot (gnome-screenshot). Mostly commented out -- superseded by GrafanaWeb.sh |
| `push2Discord.sh` | Post run start/stop to Discord webhook (converts HTML->markdown). Uses WEBHOOK_DAQ_URL from ~/Discord_webhooks.sh. Called by start/stop_run_Mac.sh |
| `push2Elog.sh` | **Legacy** elog posting script (hardcoded paths). Superseded by start_run_Mac.sh/stop_run_Mac.sh pipeline. |
| `GenElogExtra.py` | Generates HTML table of detector thresholds (EPICS) + HV status (SNMP) for elog entries; can run on Spark (has EPICS CA + SNMP access) |
| `common.py` | Core Python utility: GeneralSortMapping.h parser (regex), side groupings (Left/Bottom/Right/Top), signal aliases (e/xf/xn/de), PV aliases (threshold/rate/M/D/K/etc), PV name builders (make_set/get_pv_name) |
| `DataBase.py` / `helios_database` | Slow-control monitoring loop (30s): run number, file size, VME buffers, disc_count rates, thresholds, trigger rate -> InfluxDB. Buffer protection: stops DAQ if buffer < 300, resumes after 30s. Logs to /home/helios/helioBuffer.log |

**[!!] VME Buffer Protection -- Known Limitation:**
- DataBase.py polls buffer every ~3s; EPICS PVs update at most every 1s.
- Protection only works if buffer fills **slower than ~1s**.
- If rate spikes and buffer fills in <1s (e.g. sudden high beam rate), DataBase.py cannot react in time.
- **Fast-fill result:** digitizer deadlocks, buffer full, ACQ cannot stop gracefully.
- **Recovery:** reboot the VME crate. This is the known and accepted recovery procedure.
- **Prevention:** keep beam rate sane during operations. Rate-based pre-emption is not reliable due to EPICS floor + trace-length dependence.
- Hitrate-based pre-emption would need: fill_rate = hitRate × bytes_per_event(trace_length), compared to buffer size -- doable but trace_length varies per experiment.
| `AutoTuneThreshold.py` | Automated threshold tuning |
| `Edwards_D379_read.py` | Vacuum gauge readout (Python 2.7): reads Edwards D379 via serial RS232, posts VacuumGauge to InfluxDB every 3s. Runs on DAQ where serial port is connected. |
| `HVMonitor.py` | Iseg HV readout -> InfluxDB |
| `GetPVLIstFromDB.py` | Dev utility (Python 2.7): parses EPICS .db/.template files to extract PV names. Not a service -- used for diagnostic enumeration of available PVs |

---

## See Also

- `HELIOS_DAQ_Startup.md` -- startup sequence (SoftIOC, trigger, digitizer)
- `HELIOS_PV_Reference.md` -- full PV name list
- `HELIOS_Detector_Geometry.md` -- channel/detector mapping
- `HELIOS_Analysis_Workflow.md` -- sorting, ROOT, processing
- `HELIOS_Calibration.md` -- calibration after data acquisition
- `expMemory_<exp>.md` -- experiment-specific settings

_Consolidated from HELIOS_DAQ_Workflow.md + start_stop_sequence.md (2026-04-11)_
