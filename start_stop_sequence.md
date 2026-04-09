# start_stop_sequence.md — HELIOS Run Start/Stop Procedure (AI-driven)

This documents what HELIOS AI must do when starting and stopping a run.
Applies to all experiments. Replaces manual EDM-driven workflow when AI is in control.

---

## START RUN

### Step 1 — Ask user (if not already provided)

Before starting, collect the following. If any are missing, **ask explicitly**:

| Info | Example |
|------|---------|
| Target | CD₂ 200 µg/cm², empty frame, ²²⁸Th α source |
| Beam intensity / rate | 5×10⁵ pps, ~10 nA |
| Purpose / objective | Physics run, calibration, beam tuning, background |
| Attenuation / slit settings | 0 dB, slit ±3 mm |
| Who's on shift | Ryan, Ben, etc. |

### Step 2 — Collect from live system

Read these PVs and note any **non-default** values:

| Parameter | PV / Source | Default |
|-----------|------------|---------|
| All E-channel thresholds | `caget VME0x:MDIGn:led_thresholdN` | 400 |
| Trace length | `raw_data_length` per board | 1.0 µs |
| Pre-trigger | `raw_data_window` per board | 3.32 µs |
| Trigger method | `VME32:MTRG:SUM_X/Y`, `trigger_mux_select` | Both, ExtTTCL |
| M-window | `m_window` | 1.0 |
| Disc width | `disc_width` | 15 |
| Array position | `detectorGeo.txt` or ask | — |
| B-field | Known from expMemory or EPICS | 2.85 T for h096 |

Only log values that differ from defaults — keep elog concise.

### Step 3 — Actions

- [ ] Increment `LastRunNum`, rewrite `expName.sh`
- [ ] Start data receiver (tcpReceiver on Mac2020, or gtReceiver via X11 on DAQ)
- [ ] `caput Online_CS_SaveData Save`
- [ ] `caput Online_CS_StartStop Start`
- [ ] Record start time
- [ ] Append to `RunTimeStamp.dat`: `RUN-NNN start at <datetime> | <comment>`
- [ ] Post to InfluxDB: `SavingData,expName=<exp>,comment=Start_RUN-<comment> value=1`
- [ ] Post **rich elog entry** (see format below)
- [ ] Post summary to Discord `#h096_31si_dp`

### Elog Entry Format — Start

```
RUN-NNN started at <datetime>
Target: <target>
Beam: <intensity> | Attenuation: <atten> | Slits: <slits>
Purpose: <purpose>
On shift: <names>

Detector settings (non-default only):
  Threshold: <value if ≠400, or "default 400">
  Trace length: <value if changed>
  Trigger: <method>
  Array position: <position mm>
  B-field: <T>

<any other notes>
```

---

## DURING RUN

Any changes made during the run must be **appended to the active elog entry**:

- PV changes via `SetChannel` → log: `[HH:MM] SetChannel Left E threshold 500`
- Any other caput → log with timestamp and reason
- User comments → append verbatim

---

## STOP RUN

### Step 1 — Ask user (if not provided)

- Stop reason / comment
- Any notable events during the run (beam loss, target change, etc.)

### Step 2 — Actions

- [ ] `caput Online_CS_StartStop Stop`
- [ ] `caput Online_CS_SaveData "No Save"`
- [ ] Kill data receiver processes (tcpReceiver or gtReceiver xterms)
- [ ] Record stop time, compute run duration
- [ ] Collect data file sizes (`.gtd01`–`.gtd04` + total)
- [ ] Collect event count (EPICS counter PV if available)
- [ ] Take Grafana screenshot from Mac2017 (via `GrafanaWeb.sh`)
- [ ] Append to `RunTimeStamp.dat`: `RUN-NNN stop at <datetime> | <comment>`
- [ ] Post to InfluxDB: `SavingData,...,comment=Stop_RUN-<comment> value=0`
- [ ] Post **rich elog stop entry** (see format below)
- [ ] Post summary to Discord
- [ ] (Optional) rsync data from Mac2020 → DAQ archive

### Elog Entry Format — Stop

```
RUN-NNN stopped at <datetime>
Duration: <HH:MM:SS>
Data size: <gtd01> + <gtd02> + <gtd03> + <gtd04> = <total>
Events: <count if available>

Changes during run:
  [HH:MM] <any PV changes or comments>

Stop reason: <comment>
[Grafana screenshot attached]
```

---

## Notes

- If the user says "start a run" without providing target/purpose → ask before proceeding
- Never start a run without at minimum: target and purpose confirmed
- elog is the permanent record — be thorough
- `RunTimeStamp.dat` is the local machine log — always update it
- Discord post is a brief summary — not the full elog

---

## See Also

- `HELIOS_DAQ_Workflow.md` — EPICS PVs, run control scripts, start/stop scripts
- `HELIOS_PV_Reference.md` — full PV list
- `expMemory_h096.md` — current experiment defaults and settings
- `new_experiment_checklist.md` — Part 5 hardware setup before first run

_Created: 2026-04-08_
