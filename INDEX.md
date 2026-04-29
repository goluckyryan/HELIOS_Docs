# HELIOS_MD Index

Lightweight map of HELIOS system reference files.
All files located in `~/HELIOS_MD/`.

**Search:** `grep -ril "keyword" ~/HELIOS_MD/*.md` (no RAG needed  --  26 files, ~110KB)

## Files

| File | Contents |
|---|---|
| `README.md` | Entry point  --  overview of HELIOS, subnet, software stack |
| `HELIOS_DAQ_Startup.md` | DAQ startup sequence  --  digitizer setup, trigger locking, timestamp verification, healthy state values |
| `HELIOS_Trigger_MISC_STAT.md` | reg_MISC_STAT_RBV bit map for MTRG/RTR1/RTR2  --  lock bits, init state machine, healthy values ([OK] verified 2026-04-12) |
| `HELIOS_Firmware_Inventory.md` | Firmware versions for all boards (MTRG, RTR1, RTR2, DIGs)  --  revision encoding, dates, DGS comparison ([OK] verified 2026-04-12) |
| `HELIOS_DAQ_Workflow.md` | DAQ system overview, run control, EPICS PVs, data pipeline (skills are source of truth for start/stop) |
| `HELIOS_Analysis_Workflow.md` | ROOT analysis pipeline, Armory scripts, Mac2020 workflow |
| `HELIOS_Calibration.md` | Complete calibration reference  --  physics, code, lessons per step |
| `HELIOS_Detector_Geometry.md` | [!!] Experiment-dependent  --  array layout, channel mapping, GeneralSortMapping.h |
| `HELIOS_PV_Reference.md` | EPICS PV list  --  digitizer IOC PVs, thresholds, HV, timing |
| `HELIOS_Experiment_Flow.md` | HELIOS experiment flow at ATLAS/ANL -- pre-beam prep, beam tuning, RAISOR, checkout, physics running, teardown |
| `HELIOS_Experiment_Switch.md` | Non-interactive procedure for switching experiment branches on DAQ + Mac2020 |
| `HELIOS_Simulation_Cleopatra.md` | Cleopatra/Ptolemy + Transfer MC -- InFileCreator, DWInFileCreator, ExtractXSec, Check_Simulation, Simulation_Helper, alpha.C, transfer_test.C, PlotTGraphTObjArray, potentials.h (23 OM potentials, AK standard) |
| `HELIOS_Armory_Code.md` | Armory code reference  --  43/47 files documented: full calibration pipeline + analysis selectors + PACE4 + Penetrability + FitXsec (SF) + script_Ex + Monitors_Util (~30 fns) + testTraceFit (trapezoid filter) + more. 4 remaining are trivial .C wrappers for documented .h files. |
| `EventBuilder_Optimization.md` | EventBuilder benchmark + optimization notes  --  run011 performance (EventBuilder_S), data flow diagrams, mmap/LZ4/Reset improvements (EventBuilder_A, 2026-04-18) + GEBHeader/Event/Hit data structures (Hit.h, 2026-04-29) |
| `HELIOS_LIB_Reference.md` | HELIOS_LIB.h reference  --  TransferReaction, HELIOS trajectory, TargetScattering, Decay, Knockout, Isotope, constant.h, FindThetaCM |
| `HELIOS_Ptolemy_Build_Notes.md` | Ptolemy build notes  --  ARM64 (Spark/Jetson) and x86-64 (Mac2020) ([OK] verified 2026-04-12) |
| `HELIOS_Magnet_Pi.md` | Magnet Pi (.208)  --  Oxford 601-048T serial monitor, LHe level, shield temp, status flags ([OK] verified 2026-04-16) |
| `new_experiment_checklist.md` | Checklist for setting up a new experiment |
| `rdtCut_guideline.md` | RDT cut methods  --  hand-drawn, SRIM, ML, FOM comparison; h096 HDBSCAN summary + recoil species warning added 2026-04-23 |
| `voice-bridge-plan.md` | Discord voice bridge architecture for HELIOS AI |
| `voice-terminal-plan.md` | Mic+speaker voice terminal plan (targets Spark post-migration) |
| `HELIOS_TerminalServer.md` | Terminal server (Digi PortServer TS 16 MEI)  --  verified port map, VME console access reference |
| `HELIOS_Mac2017.md` | Mac2017 (.193) system reference  --  role, digios state, experiments, disk |
| `HELIOS_InfluxDB_Schema.md` | InfluxDB schema on Mac2017 -- measurements, tags, example queries (read-only from Spark) |
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
- Armory/working analysis code (calibration pipeline, fitting, analysis selectors) -> `HELIOS_Armory_Code.md`
- EventBuilder performance / version benchmarks -> `EventBuilder_Optimization.md`
- DWBA theory (ZR formulation, 9j/CG, radial integral, mass rescaling) -> `paper_notes/DWBA_ZR_Mathematics_Reference.md`
- Core kinematics engine (TransferReaction, HELIOS trajectory, TargetScattering) -> `HELIOS_LIB_Reference.md`
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

## Subdirectory: `proposals/`

Experiment proposals and notes. Not counted in the 26-file total above.

| File | Contents |
|---|---|
| `2214_Martin.pdf` | ATLAS Exp 2214 -- h096 proposal (31Si(d,p)32Si, config mixing in 32Si near N=20 island of inversion) |
| `h096_proposal_notes.md` | h096 proposal notes -- physics goal, setup, rate estimates, 32Si spectroscopy context |

## Subdirectory: `paper_notes/`

Detailed notes on individual HELIOS/ISS publications and theory references. 36 unique notes + 2 older duplicates = 38 files. **ALL 36/36 HELIOS pubs now have notes (100% COMPLETE as of 2026-04-26)!** Not counted in the 26-file total above.
Theory notes (Ryan's blog): ESPE_Theory.md, SF_Theory_SumRule.md, SF_Quenching_Review_2023.md (created 2026-04-24).
[Cleanup needed]: rm 2020_Tang_First_Exploration_Neutron_Shell.md + 2025_Watwood_32Si_proton_vacancy.md (superseded by newer versions)

| File | Paper |
|---|---|
| `2010_Lighthall_HELIOS_Commissioning.md` | Lighthall 2010 -- HELIOS commissioning (NIM A622) |
| `2012_Hoffman_19O_dp_20O.md` | Hoffman 2012 -- 19O(d,p)20O: prototype for h096; sd-shell (d5/2,s1/2,d3/2), 175 keV FWHM, 8 states, same team |
| `2012_Schiffer_SumRule_Ni_Isotopes.md` | Schiffer 2012 -- sum rule test on Ni isotopes; validates DWBA/transfer occupancy framework (Macfarlane-French sum rule satisfied) |
| `2013_Kay_Quenching_Cross_Sections.md` | Kay 2013 -- quenching of transfer cross sections |
| `2016_Szwec_Valence_Neutrons_136Xe_0vbb.md` | Szwec 2016 -- valence neutron occupancies in 136Xe->136Ba (0vββ decay NME constraint via (d,p)+(p,d)+(a,3He)+(3He,a)) |
| `2017_Almaraz_26Al_Astrophysics.md` | Almaraz-Calderon 2017 -- first 26Alm(d,p)27Al with isomeric beam; constrains galactic 26Al destruction; mirror symmetry |
| `2017_Freeman_100Mo_0vbb_Occupancies.md` | Freeman 2017 -- valence nucleon occupancies in 100Mo->100Ru 0vbb system via (d,p)+(p,d)+(3He,a)+(3He,d); theory discrepancies; Munich Q3D |
| `2017_Talwar_HighJ_Neutrons_137Xe.md` | Talwar 2017 -- high-j (h9/2, i13/2) neutron SFs in 137Xe via 136Xe(a,3He) at RCNP; isotonic chain N=83, 133Sn prediction |
| `2018_Santiago-Gonzalez_19F_Isomeric_Beam.md` | Santiago-Gonzalez 2018 -- single-particle character of 19F rotational band via isomeric 18mF beam at HELIOS (B=2.85 T) |
| `2020_Howard_NeutronHole_N81.md` | Howard 2020 -- neutron-hole strength in N=81 nuclei (p,d)+(3He,a) at Yale; monopole shifts, tensor force, g7/2 fragmentation |
| `2020_Tang_First_Exploration_207Hg.md` | Tang 2020 -- 206Hg(d,p)207Hg at ISS/ISOLDE; first N>126 shell structure below Pb; r-process N=126 bottleneck (Ryan's paper!) |
| `2021_Kay_Consistency_NucleonTransfer_SumRules.md` | Kay 2021 -- nucleon-transfer sum rules in deformed nuclei (Nj~1.18 vs ~0.6 for spherical; AK+KD potentials) |
| `2021_Szwec_SnIsotopes_Occupancies.md` | Szwec 2021 -- neutron occupancies + ESPEs across stable Sn chain (112-124Sn); g7/2/h11/2 systematics; Munich Q3D |
| `2022_Ayyad_NearThreshold_11B.md` | Ayyad 2022 -- near-threshold resonance in 11B (11Be beta-p) |
| `2022_Chen_15C_InelasticScattering.md` | Chen 2022 -- 15C(d,d') inelastic at HELIOS; Mn/Mp=3.6(4), moderate core decoupling; same 15C beam as Jiang 2025 |
| `2022_Hoffman_Inflight_Isomeric_16N.md` | Hoffman 2022 -- in-flight isomeric 16N beam via RAISOR at ATLAS (NIM A) |
| `2023_Bennett_Fission_Barrier_239U.md` | Bennett 2023 -- 238U(d,pf) at HELIOS; first direct fission-barrier via light-ion transfer in inverse kinematics; 239U result validates technique for exotic actinide beams |
| `2025_Jiang_Quenching_15C_Transfer.md` | Jiang 2025 -- quenching Rs~0.64 in 15C(p,d)+(d,t) at HELIOS; transfer contradicts HI-knockout Delta_S dependence |
| `2025_Watwood_32Si_Proton_Vacancy.md` | Watwood 2025 -- 32Si(3He,d)33P proton vacancy (inverse kin., 6.3 MeV/u); 1s1/2 empty in 32Si/34Si; direct h096 complement; same ANL team |
| `2026_Hoffman_32Si_5minus_isomer.md` | Hoffman 2026 (draft) -- 31Si(d,p)32Si at HELIOS 9.6 MeV/u; 5- isomer dominant 0f7/2 character (C2S=1.00), 3-1 C2S=0.44; hindered B(E2,5->3) from lack of proton participation; [!!] same reaction as h096 -- key reference for kinematics, DWBA, beam contamination |

| `DWBA_ZR_Mathematics_Reference.md` | ZR-DWBA math reference (PtolemyGUI/Raphael) -- radial integral, mass rescaling, 9j/CG, selection rules, ZR vs FR |
| `SF_Theory_SumRule.md` | SF theory: sum rule derivation (Glendenning Ch.7), simple picture, occupation number, quenching context |
| `SF_Quenching_Review_2023.md` | SF quenching review: full timeline 1993→2024, Gade plot, Kay 2022, Pohl 2023, observability debate (Ryan's blog) |
| `ESPE_Theory.md` | Effective Single Particle Energy: definition, ESPE formula, ¹²C worked example, connection to sum rule and WS mean field |

Full publication list: `~/publications/HELIOS_Publications_Summary.md` (36 papers)
