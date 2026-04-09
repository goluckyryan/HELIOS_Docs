# HELIOS DAQ Workflow Reference

**Source:** digios1 (192.168.1.2) `~/digios/daq/`
**Generated:** 2026-03-12

---

## System Overview

| Component | Host | Role |
|---|---|---|
| digios1 (192.168.1.2) | DAQ PC (CentOS 6, 32-bit) | softIOC host, data receiver, run control |
| Mac2020 (192.168.1.164) | iMac 2020 | Elog posting, Discord push, AutoProcess |
| Mac2017 (192.168.1.193) | iMac 2017 | Grafana/InfluxDB (dataBaseAddress) |
| VME01–04 (VxWorks) | VME crates | Hardware IOCs — digitizers |
| VME32 (VxWorks) | VME crate | Trigger master + routers |
| Pi5-2 (192.168.1.100) | Raspberry Pi 5 | HELIOS AI (me ☀️) |

### DAQ Disk Layout (digios1) — verified 2026-04-05

| Partition | Size | Used | Mount | Contents |
|-----------|------|------|-------|---------|
| /dev/sda1 | 1.9G | 100M | /boot | Boot |
| /dev/sda2 | 96G | 22G | /home | User homes (helios, etc.) |
| /dev/sda3 | 82G | 13G | / | OS root |
| /dev/sda6 | 256G | 64G | /global | EPICS environment, digios, data archives |

`/global` layout: `devel7_newbsp/` (5.5G, active) contains current EPICS/digios env; `devel5/` (1.7G), `devel6/` (3.3G) are older environments; `devel3/4.tgz` are archives.

---

## Key EPICS PVs for Run Control (softIOC on digios1)

| PV | Values | Description |
|---|---|---|
| `Online_CS_StartStop` | `Start` / `Stop` | Start or stop data acquisition |
| `Online_CS_SaveData` | `Save` / `No Save` | Enable/disable data saving to disk |
| `DAQG_CS_BuildEnable` | `Copy` / ... | DAQ builder enable |
| `DigFIFOSpeed` | `Fast` / `Slow` | FIFO speed |

### Trigger PVs (VME32)
| PV | Description |
|---|---|
| `VME32:MTRG:SUM_X` | X-plane trigger sum on/off |
| `VME32:MTRG:SUM_Y` | Y-plane trigger sum on/off |
| `VME32:MTRG:SUM_XY` | XY coincidence trigger |
| `VME32:MTRG:XTHRESH` | X-plane threshold |
| `VME32:MTRG:YTHRESH` | Y-plane threshold |
| `VME32:RTR1:reg_X_PLANE_MAP_A–H` | X-plane trigger routing (RTR1) |
| `VME32:RTR1:reg_Y_PLANE_MAP_A–H` | Y-plane trigger routing (RTR1) |
| `VME32:RTR2:reg_X_PLANE_MAP_A–H` | X-plane trigger routing (RTR2) |
| `VME32:RTR2:reg_Y_PLANE_MAP_A–H` | Y-plane trigger routing (RTR2) |

### Router Map (VME → Router → Symbol)
| VME | DIG | Router | Symbol |
|---|---|---|---|
| VME01 | MDIG1 | RTR1 | A |
| VME01 | MDIG2 | RTR1 | B |
| VME01 | MDIG3 | RTR1 | C |
| VME01 | MDIG4 | RTR1 | D |
| VME02 | MDIG1 | RTR1 | E |
| VME02 | MDIG2 | RTR1 | F |
| VME02 | MDIG3 | RTR1 | G |
| VME02 | MDIG4 | RTR1 | H |
| VME03 | MDIG1 | RTR2 | A |
| VME03 | MDIG2 | RTR2 | B |
| VME03 | MDIG3 | RTR2 | C |
| VME03 | MDIG4 | RTR2 | D |
| VME04 | MDIG1 | RTR2 | E |
| VME04 | MDIG2 | RTR2 | F |
| VME04 | MDIG3 | RTR2 | G |
| VME04 | MDIG4 | RTR2 | H |

---

## Entry Point: heliosCommander

`~/digios/daq/heliosCommander` — main launcher script.

- Sets EDM environment variables (EDMOBJECTS, EDMBASE, EDMFILES, EDMDATAFILES, EDMSCRIPTS)
- Launches `HELIOSMain_4sidesArray.edl` — the top-level EDM control panel
- All operator interaction starts from this GUI

---

## Experiment Configuration

### `expName.sh` (current)
```bash
expName=h094_19Ne_pp       # experiment name
daqDataPath=/media/DIGIOSDATA6   # data disk
LastRunNum=60              # last completed run number
```

### `DataBaseAddress.sh`
```bash
dataBaseAddress=192.168.1.193   # Mac2017 (Grafana/InfluxDB)
mac2020IP=192.168.1.164         # Mac2020 (Elog/Discord)
```

---

## DAQ Startup Workflow

### Step 1: Setup digitizers — `helios_setup_digitizer`

Sets all global digitizer parameters via `GLBL:DIG:*` PVs:

| Parameter | Value | Notes |
|---|---|---|
| `Online_CS_StartStop` | Stop | Ensure stopped first |
| `Online_CS_SaveData` | No Save | Ensure not saving |
| `baseline_start` | 8192 | 0 volts |
| `d_window` | 0.2 | |
| `k_window` | 0.8 | |
| `m_window` | 1.0 | |
| `k0_window` | 0.0 | |
| `d3_window` | 0.2 | |
| `d2_window` | 0.2 | |
| `led_threshold` | 400 | Default threshold |
| `CFD_fraction` | 30 | |
| `raw_data_length` | 1.0 | |
| `raw_data_window` | 3.32 | traceLength + data |
| `trigger_polarity` | Both | |
| `pileup_mode` | Accept | |
| `trigger_mux_select` | ExtTTCL | External trigger |
| `channel_enable` | Run | Enable all |
| `peak_sensitivity` | 3 | |
| `cfd_mode` | LED_Mode | |
| `delay` | 26 | |
| `tracking_speed` | 3 | |
| `holdoff_time` | 140 | |
| `disc_width` | 15 | |
| `veto_enable` | Disabled | |

Then sets **individual channel overrides:**
- VME01:MDIG1 ch1–8 → Reset (disable) — RDT board, special handling
- VME01:MDIG1 ch9 → Run (TAC channel)
- VME01:MDIG1:trigger_mux_select → IntAcptAll (internal for TAC)
- VME01:MDIG2/3 raw_data_window ch2–7 → 8.32 (trace for recoil)
- VME01:MDIG1 raw_data_window ch0–1 → 0.32 (ion chamber)

Then sets **trigger routing** (X/Y plane maps) and final master logic:
- `GLBL:DIG:master_fifo_reset` 1→0
- `GLBL:DAQ:DAQTimeDelayA` = 0.001
- `GLBL:DAQ:DAQTimeDelayB` = 0.01
- `GLBL:DAQ:BuildSendDelay` = 0.0
- `VME32:MTRG:XTHRESH/YTHRESH` = 0
- `VME32:MTRG:SUM_X/SUM_Y` = on, `SUM_XY` = off

---

## Quick DAQ Status Check

To check if a run is currently active (read-only, safe to run anytime):

```bash
# Check acquisition state
EPICS_CA_ADDR_LIST=192.168.1.2 caget Online_CS_StartStop Online_CS_SaveData

# Expected when running:
#   Online_CS_StartStop   Start
#   Online_CS_SaveData    Save

# Expected when idle:
#   Online_CS_StartStop   Stop
#   Online_CS_SaveData    No Save
```

> ⚠️ `EPICS_CA_ADDR_LIST` must point to digios1 (192.168.1.2) since CA broadcast on wlan0 won't reach the HELIOS subnet automatically. Alternatively, ensure `eth0` (192.168.1.100) is active and `AUTO_ADDR_LIST=YES`.

Check current run number:
```bash
# On DAQ (digios1) — read expName.sh
cat /global/devel7_newbsp/gretTop/9-22/dgsIoc/scripts/expName.sh | grep LastRunNum
```

---

## Starting a Run — `start_run.sh`

1. Reads `expName.sh` → increments `LastRunNum`
2. Prompts for a single-line run comment
3. Posts **start marker** to InfluxDB (Mac2017:8086)
4. Writes updated `LastRunNum` back to `expName.sh`
5. Logs run start + comment to `RunTimeStamp.dat`
6. Reads trigger PVs (`GLBL:DIG:trigger_mux_select`, `VME32:MTRG:SUM_X/Y`) for elog
7. **`caput Online_CS_SaveData Save`** — start saving data
8. **`caput Online_CS_StartStop Start`** — start acquisition
9. Sends start message to Mac2020 → posts to **Elog** and **Discord**
10. Spawns 4 `gtReceiver4` xterms (ioc1–ioc4) — data receivers writing `.gtd01–.gtd04` files
11. Starts `helios_database` — slow-control database logging
12. Window closes after 30 sec

**Data files:** `{daqDataPath}/{expName}/data/{expName}_run_{RUN}.gtd01–04`

---

## Stopping a Run — `stop_run.sh`

1. **`caput Online_CS_StartStop Stop`** — stop acquisition
2. **`caput Online_CS_SaveData "No Save"`** — stop saving
3. Posts **stop marker** to InfluxDB
4. Logs stop time + comment to `RunTimeStamp.dat`
5. Takes Grafana screenshot (from Mac2017) → attaches to Elog
6. Posts stop message to Mac2020 → **Elog** and **Discord**
7. Reports total file size (`du`)
8. Kills all `gtReceiver4` xterms (ioc1–4)
9. *(Globus transfer to LCRC currently disabled)*

---

## Auto Run Control — `AutoStartStop`

Two modes:
- **`AutoStartStop time <minutes> [repeats]`** — stop after N minutes, optionally repeat
- **`AutoStartStop size <kB> [repeats]`** — stop after file reaches N kB, optionally repeat

Repeat = -1 → infinite runs. Sends AutoProcess trigger to Mac2020 for online analysis.

---

## Other Key Scripts

| Script | Purpose |
|---|---|
| `SetVMETrigger <VME> <DIG> <PLANE>` | Set trigger bitmap for one digitizer on X or Y plane |
| `helios_save_array` | Save current array configuration |
| `helios_setup_other` | Additional setup (non-digitizer) |
| `SetVMEThreshold` | Set VME thresholds |
| `HVMonitor.py` | Iseg HV readout → InfluxDB |
| `DataBase.py` / `helios_database` | Slow-control DB acquisition |
| `globus_out.py` / `globus_in.py` | Data transfer to/from LCRC (currently disabled) |
| `Edwards_D379_read.py` | Vacuum gauge readout |
| `AutoTuneThreshold.py` | Automated threshold tuning |
| `push2Discord.sh` | Post run status to Discord |
| `push2Elog.sh` | Post to electronic logbook |
| `WriteComment` | Write comment to elog |
| `tcpReceiver` | **Experimental** multi-threaded TCP receiver (HELIOS AI, 2026-03-12) — see below |

---

## tcpReceiver (Experimental)

- **Location:** `~/digios/daq/Receiver/tcpReceiver.cpp` (pre-built binary: `tcpReceiver`)
- **Purpose:** Multi-threaded drop-in replacement for `gtReceiver4` — one thread per IOC, no shared mutable state
- **Build:** `cd ~/digios/daq/Receiver && g++ -O2 -pthread -o tcpReceiver tcpReceiver.cpp`
- **Usage:** `tcpReceiver <filename_base> <maxfilesize> <GEBID> <server1> [server2] ...`
- **Example:** `tcpReceiver ARR01_run_001.gtd 2000000000 14 ioc1 ioc2 ioc3 ioc4`
- **Status:** ⚠️ Not yet tested on live DAQ — TODO: test with Ryan present
- **Author:** General HELIOS AI, based on `gtReceiver4.c` (LBL/ANL DGS group)

---

## Data Flow

```
VME IOCs (VxWorks)
     ↓ (CA / fiber)
digios1 softIOC
     ↓ (gtReceiver4 × 4)
.gtd01–.gtd04 files → /media/DIGIOSDATA6/{expName}/data/
     ↓ (AutoProcess on Mac2020)
ROOT files
     ↓ (Globus, when enabled)
LCRC archival + parallel analysis
```

---

## Slow Control / Monitoring

| System | Host | Port/Protocol |
|---|---|---|
| InfluxDB | Mac2017 (192.168.1.193) | :8086 HTTP |
| Grafana | Mac2017 | Web |
| Elog | Mac2020 (192.168.1.164) | SSH + push2Elog.sh |
| Discord | Mac2020 | push2Discord.sh |
| HV (Iseg) | 192.168.1.155 | SNMP |
| Vacuum | Edwards D379 | Serial via DAQ |

---

## Notes

- Current experiment: **h096_31Si_dp** (³¹Si(d,p)³²Si, B=2.85 T) — magnet ramped 2026-04-08; see `expMemory_h096.md`
- Previous: h095 (¹¹C(d,p)), h094 (¹⁹Ne(p,p))
- ⚠️ **DO NOT use `GLBL:DIG:*` PVs** — not confirmed reliable. Always use individual `VMExx:MDIGn:*` PVs directly
- `VMExx:MDIGn:*` PVs target individual boards — use for per-channel overrides
- The softIOC on digios1 hosts the `Online_CS_*`, `DAQG_*`, `GLBL:DAQ:*`, `DigFIFOSpeed` PVs
- Hardware PVs (`VMExx:MDIGn:*`, `VME32:*`) live on VxWorks IOCs, reachable via CA broadcast
- ⚠️ Many EDM screens are outdated or never used — do not treat them as authoritative. Ryan will confirm which screens are actively used.
- ✅ **`HELIOSArraySettings_4sidesArray.edl`** — REAL threshold screen, actively in use
- ❌ **`HELIOSThresholds.edl`** — STALE, wrong PVs, NOT used — do not reference


---

## See Also

- `HELIOS_PV_Reference.md` — full PV name list for CA queries
- `HELIOS_Detector_Geometry.md` — channel/detector mapping
- `HELIOS_Experiment_Switch.md` — switching experiment branches on DAQ + Mac2020
- `HELIOS_Analysis_Workflow.md` — sorting, ROOT analysis, processing pipeline
- `HELIOS_Calibration_Procedure.md` — calibration steps after data acquisition
- `HELIOS_Simulation_Cleopatra.md` — kinematics / DWBA simulation
- `HELIOS_TerminalServer.md` — terminal server port mapping
