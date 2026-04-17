# HELIOS_MD Index

Lightweight map of HELIOS system reference files.
All files located in `~/HELIOS_MD/`.

**Search:** `grep -ril "keyword" ~/HELIOS_MD/*.md` (no RAG needed  --  23 files, ~90KB)

## Files

| File | Contents |
|---|---|
| `README.md` | Entry point  --  overview of HELIOS, subnet, software stack |
| `HELIOS_DAQ_Startup.md` | DAQ startup sequence  --  digitizer setup, trigger locking, timestamp verification, healthy state values |
| `HELIOS_Trigger_MISC_STAT.md` | reg_MISC_STAT_RBV bit map for MTRG/RTR1/RTR2  --  lock bits, init state machine, healthy values, related PVs |
| `HELIOS_Firmware_Inventory.md` | Firmware versions for all boards (MTRG, RTR1, RTR2, DIGs)  --  revision encoding, dates, DGS comparison |
| `HELIOS_DAQ_Workflow.md` | DAQ system overview, run control, EPICS PVs, data pipeline (skills are source of truth for start/stop) |
| `HELIOS_Analysis_Workflow.md` | ROOT analysis pipeline, Armory scripts, Mac2020 workflow |
| `HELIOS_Calibration.md` | Complete calibration reference  --  physics, code, lessons per step |
| `HELIOS_Detector_Geometry.md` | [!!] Experiment-dependent  --  array layout, channel mapping, GeneralSortMapping.h |
| `HELIOS_PV_Reference.md` | EPICS PV list  --  digitizer IOC PVs, thresholds, HV, timing |
| `HELIOS_Experiment_Flow.md` | General experiment flow  --  pre-beam prep, beam tuning, RAISOR, checkout, physics running, teardown |
| `HELIOS_Experiment_Flow.md` | HELIOS experiment flow at ATLAS/ANL -- typical sequence from setup to data |
| `HELIOS_Experiment_Switch.md` | Non-interactive procedure for switching experiment branches on DAQ + Mac2020 |
| `HELIOS_Firmware_Inventory.md` | VME digitizer firmware versions -- verified live from EPICS PVs 2026-04-12 |
| `HELIOS_Trigger_MISC_STAT.md` | reg_MISC_STAT_RBV bit map for trigger modules -- verified from EDM + VHDL source 2026-04-12 |
| `HELIOS_Simulation_Cleopatra.md` | Cleopatra/Ptolemy DWBA simulation workflow, kinematics tools |
| `HELIOS_Ptolemy_Build_Notes.md` | Ptolemy build notes -- ARM64 (Pi5) and x86-64 (Mac2020) ([OK] verified 2026-04-12) |
| `HELIOS_Magnet_Pi.md` | Magnet Pi (192.168.1.208) -- Oxford 601-048T serial monitor, LHe level, shield temp, status flags |
| `new_experiment_checklist.md` | Checklist for setting up a new experiment |
| `rdtCut_guideline.md` | RDT cut methods  --  hand-drawn, SRIM, ML, FOM comparison |
| `HELIOS_Migration_Mac2020.md` | Mac2020 migration plan |
| `voice-bridge-plan.md` | Discord voice bridge architecture for HELIOS AI |
| `voice-terminal-plan.md` | Pi mic+speaker voice terminal plan |
| `HELIOS_TerminalServer.md` | Terminal server (Digi PortServer TS 16 MEI)  --  verified port map, VME console access reference |
| `HELIOS_Mac2017.md` | Mac2017 (.193) system reference  --  role, digios state, experiments, disk |
| `HELIOS_Magnet_Pi.md` | Magnet Pi (.208) -- magnet readout, liquid helium monitoring, SSH read-only ([OK] verified 2026-04-16) |
| `heartbeat-log.md` | Heartbeat task log (compact; full archive pre-2026-04-05 in heartbeat-log-archive-20260405.md) |
| `heartbeat-log-archive-20260405.md` | Archived verbose heartbeat entries prior to 2026-04-05 |

## When to load each

- DAQ, run control, EPICS, start/stop runs -> `HELIOS_DAQ_Workflow.md`
- Analysis, ROOT, sorting, processing -> `HELIOS_Analysis_Workflow.md`
- Calibration (all steps, physics + code + lessons) -> `HELIOS_Calibration.md`
- Detector layout, channel mapping -> `HELIOS_Detector_Geometry.md` [!!] verify per experiment
- EPICS PV names, thresholds, HV channels -> `HELIOS_PV_Reference.md`
- Experiment lifecycle overview -> `HELIOS_Experiment_Flow.md`
- Switching experiments (branches, DAQ, Mac2020) -> `HELIOS_Experiment_Switch.md`
- Firmware versions (digitizer) -> `HELIOS_Firmware_Inventory.md`
- Trigger MISC_STAT bit map -> `HELIOS_Trigger_MISC_STAT.md`
- DWBA, Ptolemy, kinematics simulation -> `HELIOS_Simulation_Cleopatra.md`
- Ptolemy build/compile notes -> `HELIOS_Ptolemy_Build_Notes.md`
- New experiment setup -> `new_experiment_checklist.md`
- RDT cuts, FOM, ML vs hand-drawn -> `rdtCut_guideline.md`
- Terminal server port map, VME consoles -> `HELIOS_TerminalServer.md`
- Mac2017 system state -> `HELIOS_Mac2017.md`
- Magnet Pi (.208) readout, liquid helium -> `HELIOS_Magnet_Pi.md`

## Related Files (not in HELIOS_MD  --  in workspace)

These live in `~/.openclaw/workspace/` and are loaded separately:

| File | Contents |
|---|---|
| `MEMORY.md` | Long-term memory  --  SSH keys, PV rules, host map, active TODO list |
| `expMemory_h094.md` | h094 1?Ne(p,p) experiment  --  runs, calibration state, analysis notes |
| `expMemory_h095.md` | h095 11C(d,p) experiment  --  runs, calibration state, exShift iterations |
| `expMemory_h096.md` | h096 31Si(d,p)32Si experiment  --  B=2.85 T, field ramped 2026-04-08, active |

> These are auto-loaded per channel (USER.md). Do not duplicate their content in HELIOS_MD.
