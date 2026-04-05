# HELIOS_MD Index

Lightweight map of HELIOS system reference files.
All files located in `~/HELIOS_MD/`.

**Search:** `grep -ril "keyword" ~/HELIOS_MD/*.md` (no RAG needed — 16 files, ~90KB)

## Files

| File | Contents |
|---|---|
| `README.md` | Entry point — overview of HELIOS, subnet, software stack |
| `HELIOS_DAQ_Workflow.md` | DAQ run control, digios repo, start/stop runs, data pipeline |
| `HELIOS_Analysis_Workflow.md` | ROOT analysis pipeline, Armory scripts, Mac2020 workflow |
| `HELIOS_Calibration_Procedure.md` | Manual silicon detector calibration — energy, Xf/Xn, position |
| `HELIOS_Calibration_Workflow.md` | AutoCalibrationTrace, AutoFit, calibration scripts in Armory |
| `HELIOS_Detector_Geometry.md` | ⚠️ Experiment-dependent — array layout, channel mapping, GeneralSortMapping.h |
| `HELIOS_PV_Reference.md` | EPICS PV list — digitizer IOC PVs, thresholds, HV, timing |
| `HELIOS_Experiment_Switch.md` | Non-interactive procedure for switching experiment branches on DAQ + Mac2020 |
| `HELIOS_Simulation_Cleopatra.md` | Cleopatra/Ptolemy DWBA simulation workflow, kinematics tools |
| `calibration_notes.md` | Lessons learned — energy cal pipeline, xnCorr, X scale, exShift |
| `new_experiment_checklist.md` | Checklist for setting up a new experiment |
| `rdtCut_guideline.md` | RDT cut methods — hand-drawn, SRIM, ML, FOM comparison |
| `HELIOS_Migration_Mac2020.md` | Mac2020 migration plan |
| `voice-bridge-plan.md` | Discord voice bridge architecture for HELIOS AI |
| `voice-terminal-plan.md` | Pi mic+speaker voice terminal plan |
| `heartbeat-log.md` | Heartbeat task log |

## When to load each

- DAQ, run control, EPICS, start/stop runs → `HELIOS_DAQ_Workflow.md`
- Analysis, ROOT, sorting, processing → `HELIOS_Analysis_Workflow.md`
- Energy/position calibration procedure → `HELIOS_Calibration_Procedure.md`
- AutoFit, AutoCalibrationTrace scripts → `HELIOS_Calibration_Workflow.md`
- Detector layout, channel mapping → `HELIOS_Detector_Geometry.md` ⚠️ verify per experiment
- EPICS PV names, thresholds, HV channels → `HELIOS_PV_Reference.md`
- Switching experiments (branches, DAQ, Mac2020) → `HELIOS_Experiment_Switch.md`
- DWBA, Ptolemy, kinematics simulation → `HELIOS_Simulation_Cleopatra.md`
- Calibration lessons / exShift / xnCorr → `calibration_notes.md`
- New experiment setup → `new_experiment_checklist.md`
- RDT cuts, FOM, ML vs hand-drawn → `rdtCut_guideline.md`
