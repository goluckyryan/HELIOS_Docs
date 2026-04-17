# HELIOS Knowledge Base

Documentation and reference files for the **HELIOS** (HELIcal Orbit Spectrometer) at Argonne National Laboratory.

## What is HELIOS?

HELIOS is a solenoidal spectrometer at the ATLAS facility (Argonne Tandem Linac Accelerator System). It uses a superconducting solenoid magnet to study nuclear reactions in inverse kinematics. Light recoil particles (protons, deuterons, tritons, etc.) spiral in the axial magnetic field back to an on-axis silicon detector array, providing excellent Q-value resolution (~100-200 keV FWHM) and wide center-of-mass angle coverage.

**Primary reactions:** (d,p), (d,3He), (d,alpha), (p,alpha), (t,p), and others with stable and radioactive beams.

## Documentation Index

### DAQ & Operations

| File | Description |
|------|-------------|
| [HELIOS_DAQ_Startup.md](HELIOS_DAQ_Startup.md) | DAQ startup sequence -- digitizer setup, trigger locking, healthy state values |
| [HELIOS_DAQ_Workflow.md](HELIOS_DAQ_Workflow.md) | DAQ run control, digios scripts, start/stop runs, data pipeline |
| [HELIOS_PV_Reference.md](HELIOS_PV_Reference.md) | EPICS PV names  --  digitizer thresholds, HV channels, timing |
| [HELIOS_Experiment_Flow.md](HELIOS_Experiment_Flow.md) | HELIOS experiment flow at ATLAS/ANL -- typical sequence |
| [HELIOS_Experiment_Switch.md](HELIOS_Experiment_Switch.md) | Procedure for switching experiment branches on DAQ + Mac2020 |
| [new_experiment_checklist.md](new_experiment_checklist.md) | Checklist for setting up a new experiment |

### Detectors & Calibration

| File | Description |
|------|-------------|
| [HELIOS_Detector_Geometry.md](HELIOS_Detector_Geometry.md) | Silicon array layout, channel mapping ([!!] experiment-dependent) |
| [HELIOS_Calibration.md](HELIOS_Calibration.md) | Complete calibration reference  --  physics, code, lessons per step |
| [rdtCut_guideline.md](rdtCut_guideline.md) | RDT (recoil detector telescope) cut methods  --  hand-drawn, SRIM, ML, FOM |

### Analysis & Simulation

| File | Description |
|------|-------------|
| [HELIOS_Analysis_Workflow.md](HELIOS_Analysis_Workflow.md) | ROOT analysis pipeline, Armory macros, TSelector framework |
| [HELIOS_Simulation_Cleopatra.md](HELIOS_Simulation_Cleopatra.md) | Cleopatra/Ptolemy DWBA simulation, kinematics tools |
| [HELIOS_Ptolemy_Build_Notes.md](HELIOS_Ptolemy_Build_Notes.md) | Ptolemy build notes -- Pi5 (ARM64) and Mac2020 (x86-64) ([OK] 2026-04-12) |

### Systems & Hardware

| File | Description |
|------|-------------|
| [HELIOS_TerminalServer.md](HELIOS_TerminalServer.md) | Terminal server (Digi PortServer TS 16 MEI)  --  verified port map, VME console access ([OK] 2026-04-05) |
| [HELIOS_Firmware_Inventory.md](HELIOS_Firmware_Inventory.md) | VME digitizer firmware versions ([OK] verified 2026-04-12) |
| [HELIOS_Trigger_MISC_STAT.md](HELIOS_Trigger_MISC_STAT.md) | reg_MISC_STAT_RBV bit map for trigger modules ([OK] verified 2026-04-12) |
| [HELIOS_Mac2017.md](HELIOS_Mac2017.md) | Mac2017 (.193)  --  role, digios state, disk usage, experiments |
| [HELIOS_Magnet_Pi.md](HELIOS_Magnet_Pi.md) | Magnet Pi (.208) -- magnet readout, liquid helium monitoring ([OK] 2026-04-16) |

### Infrastructure & Plans

| File | Description |
|------|-------------|
| [HELIOS_Migration_Mac2020.md](HELIOS_Migration_Mac2020.md) | Plan for migrating analysis to Mac2020 |
| [voice-bridge-plan.md](voice-bridge-plan.md) | Discord voice bridge architecture for HELIOS AI |
| [voice-terminal-plan.md](voice-terminal-plan.md) | Pi-based mic+speaker voice terminal for HELIOS AI |

## HELIOS Subnet

The spectrometer is controlled via a dedicated subnet (192.168.1.0/24):

| IP | Role |
|---|---|
| .1 | Cisco gateway/router |
| .2 | DAQ host (CentOS 6, EPICS soft IOC) |
| .3 | Terminal server (Digi PortServer TS 16 MEI)  --  2001=TrigCPU, 2002-2006=VME1-5, 2007=VME6(off) |
| .20-.24 | VME IOCs (VxWorks 5.5) |
| .100 | HELIOS AI (Raspberry Pi 5) |
| .155 | Iseg HV controller (SNMP) |
| .164 | Mac2020 (iMac, analysis workstation) |
| .193 | Mac2017 (iMac) |
| .208 | Raspberry Pi (magnet + LHe readout) |

## Software Stack

- **DAQ:** EPICS-based, digitizers via dgsIoc, run control via shell scripts
- **Analysis:** ROOT (TSelector), Armory utility macros, Cleopatra/Ptolemy for DWBA
- **Code repository:** [digios](https://github.com/calemhoffman/digios)  --  DAQ + analysis codebase
- **AI assistant:** OpenClaw on Raspberry Pi 5  --  monitors, assists with analysis, and operates HELIOS systems

## Related Resources

- [HELIOS Publications Summary](../publications/HELIOS_Publications_Summary.md)  --  36 publications with physics summaries
- [digios repository](https://github.com/calemhoffman/digios)  --  DAQ and analysis code
- [IsegSNMPGUI](https://github.com/goluckyryan/IsegSNMPGUI)  --  HV monitoring and control (branch: HELIOS)

## Contributing

These docs are maintained by the HELIOS team at ANL. Files are written in Markdown and intended to be both human-readable and machine-searchable by the HELIOS AI assistant.
