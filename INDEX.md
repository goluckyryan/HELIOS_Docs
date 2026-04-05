# HELIOS_MD Index

Lightweight map of HELIOS system reference files.
**Load this every session. Load individual files only when needed.**
All files located in `~/HELIOS_MD/`.

## Files

| File | Contents |
|---|---|
| `HELIOS_DAQ_Workflow.md` | DAQ run control, digios repo, start/stop runs, data pipeline |
| `HELIOS_Analysis_Workflow.md` | ROOT analysis pipeline, Armory scripts, Mac2020 workflow |
| `HELIOS_Calibration_Procedure.md` | Manual silicon detector calibration — energy, Xf/Xn, position |
| `HELIOS_Calibration_Workflow.md` | AutoCalibrationTrace, AutoFit, calibration scripts in Armory |
| `HELIOS_Detector_Geometry.md` | ⚠️ Experiment-dependent — array layout, channel mapping, GeneralSortMapping.h |
| `HELIOS_PV_Reference.md` | EPICS PV list — digitizer IOC PVs, thresholds, HV, timing |
| `HELIOS_Experiment_Switch.md` | Non-interactive procedure for switching experiment branches on DAQ + Mac2020 |
| `HELIOS_Simulation_Cleopatra.md` | Cleopatra/Ptolemy DWBA simulation workflow, kinematics tools |

## When to load each

- DAQ, run control, EPICS, start/stop runs → `HELIOS_DAQ_Workflow.md`
- Analysis, ROOT, sorting, processing → `HELIOS_Analysis_Workflow.md`
- Energy/position calibration procedure → `HELIOS_Calibration_Procedure.md`
- AutoFit, AutoCalibrationTrace scripts → `HELIOS_Calibration_Workflow.md`
- Detector layout, channel mapping → `HELIOS_Detector_Geometry.md` ⚠️ verify per experiment
- EPICS PV names, thresholds, HV channels → `HELIOS_PV_Reference.md`
- Switching experiments (branches, DAQ, Mac2020) → `HELIOS_Experiment_Switch.md`
- DWBA, Ptolemy, kinematics simulation → `HELIOS_Simulation_Cleopatra.md`
