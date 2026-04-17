# HELIOS Experiment Flow

General flow for a HELIOS experiment at ATLAS/ANL. Not every experiment is identical, but this is the typical sequence.

---

## Phase 1 — Pre-Beam Preparation (days/weeks before)

- Proposal approved, beam time scheduled
- Shift schedule created (Google Sheets), collaborators assigned
- Detector array installed, cabled, and tested
- HV channels mapped and verified
- DAQ configured: IOCs running, digitizer + trigger setup
- Alpha source calibration runs — verify all channels, establish energy calibration
- Threshold tuning (AutoTune with source)
- Kinematics simulation: generate `transfer.root`, verify E-Z acceptance (Check_Simulation)
- `reactionConfig.txt` + `detectorGeo.txt` configured for the experiment
- Analysis framework ready: `GeneralSortMapping.h`, correction files, working_Helios directory

## Phase 2 — Beam Day (e.g. Monday morning)

These happen **in parallel**, not sequentially:

### Upstream: Beam Tuning (~24 hrs)
- Stable beam tuning starts at ATLAS ion source
- Beam is tuned stage by stage downstream through the accelerator
- Takes ~24 hours to reach the experimental area

### At HELIOS: Target Installation
- Open HELIOS bore
- Remove alpha source
- Install CD2 (or other) target fans
- Close bore, pump down to vacuum (< 1.8e-3 mbar)
- Ramp HV back up on detectors (if powered down for opening)
- Verify DAQ still running, all channels responding

## Phase 3 — RAISOR Tuning (radioactive beam experiments)

- Only applies when using in-flight production (e.g. 31Si from RAISOR)
- RAISOR separator tuned for beam purity (~0.5-1 day)
- During RAISOR tuning: DAQ can be running (not recording data) to monitor recoil rates in RDT
- This gives real-time feedback on beam optimization

For stable beam experiments, skip this phase.

## Phase 4 — Beam on Target + Checkout

- Beam delivered to HELIOS target position
- Start with attenuators in (reduced rate)
- Verify:
  - Recoils visible in RDT
  - Proton/light-ion signals in PSD array
  - E-Z kinematics lines match simulation
  - Trigger rates reasonable
- Threshold re-tuning with beam (rates differ from alpha source)
- Short checkout run — verify data quality, energy calibration

## Phase 5 — Physics Running

- Remove attenuators, ramp to full beam intensity
- Production data taking (continuous, shift-based)
- Monitor: trigger rates, vacuum, beam current, detector health
- Run monitor script active (`helios_run_monitor.py`): alerts on beam loss, vacuum issues
- Elog entries for every run (start/stop, conditions, notes)
- Periodic checks: leakage current, threshold stability, data file sizes
- Shift handoffs: outgoing shift records conditions, incoming shift verifies

### During Physics Running
- Runs typically 1-4 hours each (depends on experiment)
- Between runs: quick online analysis, adjust if needed
- Target changes possible (e.g. CD2 -> empty frame for background)
- Beam may drop — monitor alerts, wait for recovery or escalate to control room

## Phase 6 — End of Experiment

- Final run stopped
- HV ramped down
- DAQ stopped
- Final elog entries
- Data copied to LCRC via Globus for offline analysis
- HELIOS opened, target removed
- Post-experiment: analysis, calibration refinement, publications

---

## Key Contacts During Experiment

- **Control room:** +1 (630) 252-4115
- **Data room:** +1 (630) 252-5002
- **PI and shift leader** per shift schedule

---

## Notes

- Beam tuning time varies: stable beams ~12-24 hrs, radioactive beams may take longer
- RAISOR purity is typically ~5% for in-flight beams — contaminant rejection relies on E-dE in RDT
- Vacuum limit for detector safety: 1.8e-3 mbar (nighttime auto-HV-off in monitor)
- Always have 24h Zoom link active for remote collaborators

---

## See Also

- `HELIOS_DAQ_Startup.md` -- digitizer setup, trigger locking, healthy state values
- `HELIOS_DAQ_Workflow.md` -- run control, start/stop procedure, data pipeline
- `HELIOS_Calibration.md` -- full calibration pipeline (energy, position, exShift)
- `new_experiment_checklist.md` -- checklist for setting up a new experiment branch
- `HELIOS_Experiment_Switch.md` -- procedure for switching experiment branches
