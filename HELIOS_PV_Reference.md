# HELIOS EPICS PV Reference

**Source:** `digios1` (192.168.1.2) — `/global/devel7_newbsp/gretTop/9-22/dgsIoc/db/`
**Generated:** 2026-03-11
**IOC:** dgsIoc (DGS/HELIOS digitizer IOC, VxWorks 5.5)
**EPICS CA Port:** 5064 (TCP+UDP)

---

## Architecture Overview

| Component | Description |
|---|---|
| VME01–VME04 | Digitizer crates (active HELIOS config, 4 crates) |
| VME32 | Trigger crate (1 master MTRG + 2 routers RTR1, RTR2) |
| GLBL | System-wide broadcast (dfanout to all crates/FPGAs) |
| VMExx:GLBL | Per-crate broadcast (dfanout to all MDIGs in that crate) |
| VMExx:MDIGn | Individual digitizer module (4 per crate) |
| VMExx:MDIGn_F2 | Second FPGA on dual-FPGA digitizer boards |

### Digitizer Board ID Map (user_package_data)
| PV Prefix | Board ID |
|---|---|
| VME01:MDIG1 | 101 |
| VME01:MDIG2 | 102 |
| VME01:MDIG3 | 103 |
| VME01:MDIG4 | 104 |
| VME02:MDIG1 | 105 |
| VME02:MDIG2 | 106 |
| VME02:MDIG3 | 107 |
| VME02:MDIG4 | 108 |
| VME03:MDIG1 | 109 |
| VME03:MDIG2 | 110 |
| VME03:MDIG3 | 111 |
| VME03:MDIG4 | 112 |
| VME04:MDIG1 | 113 |
| VME04:MDIG2 | 114 |
| VME04:MDIG3 | 115 |
| VME04:MDIG4 | 116 |

---

## Global DAQ PVs (GLBL:DAQ:)

| PV Name | Type | Description |
|---|---|---|
| GLBL:DAQ:BuildSendDelay | ao | Build/send delay |
| GLBL:DAQ:BuildSendEna | bo | Build/send enable |
| GLBL:DAQ:DAQTimeDelayA | ao | DAQ time delay A |
| GLBL:DAQ:DAQTimeDelayB | ao | DAQ time delay B |

---

## Global Digitizer PVs (GLBL:DIG:)

> ⚠️ **DO NOT use GLBL:DIG:\* PVs to set individual channel parameters** — these broadcast to ALL digitizers and will overwrite specific settings. Always use `VMExx:MDIGn:*` individual module PVs directly.

These broadcast to all digitizers system-wide via dfanout chains (F01–F05 per parameter).

| PV Name | Type | Description |
|---|---|---|
| GLBL:DIG:ahit_count_mode | bo | A-hit count mode |
| GLBL:DIG:auto_mode | bo | Auto mode |
| GLBL:DIG:baseline_delay | ao | Baseline delay |
| GLBL:DIG:baseline_start | longout | Baseline start |
| GLBL:DIG:BGO_discbit_select | bo | BGO discriminator bit select |
| GLBL:DIG:CFD_fraction | ao | CFD fraction |
| GLBL:DIG:cfd_mode | bo | CFD mode |
| GLBL:DIG:channel_enable | bo | Channel enable |
| GLBL:DIG:clk_select | bo | Clock select |
| GLBL:DIG:config_diag_fpga | bo | Configure diagnostic FPGA |
| GLBL:DIG:config_main_fpga | bo | Configure main FPGA |
| GLBL:DIG:config_override | bo | Configuration override |
| GLBL:DIG:counter_mode | bo | Counter mode |
| GLBL:DIG:counter_reset | bo | Counter reset |
| GLBL:DIG:d2_window | ao | D2 window |
| GLBL:DIG:d3_window | ao | D3 window |
| GLBL:DIG:dac_attenuation | longout | DAC attenuation |
| GLBL:DIG:dac_channel_select | longout | DAC channel select |
| GLBL:DIG:dc_balance_enable | bo | DC balance enable |
| GLBL:DIG:decimation_factor | mbbo | Decimation factor |
| GLBL:DIG:delay | ao | Delay |
| GLBL:DIG:DIAG_DISC_SEL | bo | Diagnostic discriminator select |
| GLBL:DIG:diag_input | longout | Diagnostic input |
| GLBL:DIG:diag_input_en | longout | Diagnostic input enable |
| GLBL:DIG:diag_isync | bo | Diagnostic isync |
| GLBL:DIG:diag_mux_control | mbbo | Diagnostic mux control |
| GLBL:DIG:DIAG_WAVE_SEL | bo | Diagnostic waveform select |
| GLBL:DIG:disc_count_mode | bo | Discriminator count mode |
| GLBL:DIG:disc_width | longout | Discriminator width |
| GLBL:DIG:dropped_event_count_mode | bo | Dropped event count mode |
| GLBL:DIG:d_window | ao | D window |
| GLBL:DIG:enable_dec_pause | bo | Enable decimation pause |
| GLBL:DIG:event_count_mode | bo | Event count mode |
| GLBL:DIG:event_extention_mode | mbbo | Event extension mode |
| GLBL:DIG:ext_disc_sel | mbbo | External discriminator select |
| GLBL:DIG:ext_disc_src | mbbo | External discriminator source |
| GLBL:DIG:ext_disc_ts_sel | mbbo | External discriminator timestamp select |
| GLBL:DIG:flash_mode | bo | Flash mode |
| GLBL:DIG:holdoff_time | longout | Holdoff time |
| GLBL:DIG:k0_window | ao | K0 window |
| GLBL:DIG:k_window | ao | K window |
| GLBL:DIG:led_threshold | longout | LED threshold |
| GLBL:DIG:load_baseline | bo | Load baseline |
| GLBL:DIG:load_delays | bo | Load delays |
| GLBL:DIG:manual_data | ao | Manual data |
| GLBL:DIG:master_counter_reset | bo | Master counter reset |
| GLBL:DIG:master_fifo_reset | bo | Master FIFO reset |
| GLBL:DIG:master_logic_enable | bo | Master logic enable |
| GLBL:DIG:m_window | ao | M window |
| GLBL:DIG:output_mode | mbbo | Output mode |
| GLBL:DIG:p1_window | ao | P1 window |
| GLBL:DIG:p2_window | ao | P2 window |
| GLBL:DIG:peak_sensitivity | longout | Peak sensitivity |
| GLBL:DIG:phase_hunt | bo | Phase hunt |
| GLBL:DIG:pileup_extention_mode | bo | Pileup extension mode |
| GLBL:DIG:pileup_mode | bo | Pileup mode |
| GLBL:DIG:pileup_waveform_only_mode | bo | Pileup waveform-only mode |
| GLBL:DIG:preamp_reset_delay | longout | Preamp reset delay |
| GLBL:DIG:preamp_reset_delay_en | bo | Preamp reset delay enable |
| GLBL:DIG:raw_data_length | ao | Raw data length |
| GLBL:DIG:raw_data_window | ao | Raw data window |
| GLBL:DIG:rj45_discbit_mode | mbbo | RJ45 discriminator bit mode |
| GLBL:DIG:rj45_spare_io_dir | mbbo | RJ45 spare IO direction |
| GLBL:DIG:rj45_spare_io_mux_sel | mbbo | RJ45 spare IO mux select |
| GLBL:DIG:rj45_throttle_mode | mbbo | RJ45 throttle mode |
| GLBL:DIG:rst_flash | bo | Reset flash |
| GLBL:DIG:rst_main_fpga | bo | Reset main FPGA |
| GLBL:DIG:sd_line_loopback_en | bo | SD line loopback enable |
| GLBL:DIG:sd_local_loopback_en | bo | SD local loopback enable |
| GLBL:DIG:sd_pem | mbbo | SD PEM |
| GLBL:DIG:sd_rx_pwr | bo | SD RX power |
| GLBL:DIG:sd_sm_lost_lock_flag | bo | SD SM lost lock flag |
| GLBL:DIG:sd_sm_stringent_lock | bo | SD SM stringent lock |
| GLBL:DIG:sd_sync | bo | SD sync |
| GLBL:DIG:sd_tx_pwr | bo | SD TX power |
| GLBL:DIG:tracking_speed | ao | Tracking speed |
| GLBL:DIG:trigger_mux_select | mbbo | Trigger mux select |
| GLBL:DIG:trigger_polarity | mbbo | Trigger polarity |
| GLBL:DIG:ts_err_count_ctrl | bo | Timestamp error count control |
| GLBL:DIG:user_package_data | longout | User package data (board ID) |
| GLBL:DIG:veto_enable | bo | Veto enable |
| GLBL:DIG:veto_gate_width | longout | Veto gate width |
| GLBL:DIG:vme_sandboxA | longout | VME sandbox A |
| GLBL:DIG:vme_sandboxB | longout | VME sandbox B |
| GLBL:DIG:vme_sandboxC | longout | VME sandbox C |
| GLBL:DIG:vme_sandboxD | longout | VME sandbox D |
| GLBL:DIG:win_comp_max | ao | Window comparator max |
| GLBL:DIG:win_comp_min | ao | Window comparator min |
| GLBL:DIG:write_flags | bo | Write flags |

> **Note:** Each GLBL:DIG parameter fans out via dfanout records GLBL:DIG:F01 through GLBL:DIG:F05.

---

## Per-Crate Global PVs (VMExx:GLBL:)

Pattern: `VMExx:GLBL:<parameter>` — same parameter set as GLBL:DIG above,
fans out to all MDIG modules within that crate.

Crates: **VME01, VME02, VME03, VME04, VME05, VME06**

---

## Per-Module PVs (VMExx:MDIGn: and VMExx:MDIGn_F2:)

Pattern: `VMExx:MDIGn:<parameter>` and `VMExx:MDIGn_F2:<parameter>`

Modules per crate: **MDIG1, MDIG2, MDIG3, MDIG4** (+ _F2 variants for dual-FPGA boards)

### Parameters available per module (dfanout type):

| Parameter | Description |
|---|---|
| ahit_count_mode | A-hit count mode |
| baseline_start | Baseline start |
| CFD_fraction | CFD fraction |
| channel_enable | Channel enable |
| clk_select | Clock select |
| counter_reset | Counter reset |
| d2_window | D2 window |
| d3_window | D3 window |
| decimation_factor | Decimation factor |
| disc_count_mode | Discriminator count mode |
| disc_width | Discriminator width |
| dropped_event_count_mode | Dropped event count mode |
| d_window | D window |
| enable_dec_pause | Enable decimation pause |
| event_count_mode | Event count mode |
| event_extention_mode | Event extension mode |
| ext_disc_sel | External discriminator select |
| ext_disc_src | External discriminator source |
| k0_window | K0 window |
| k_window | K window |
| led_threshold | LED threshold |
| m_window | M window |
| p1_window | P1 window |
| pileup_extention_mode | Pileup extension mode |
| pileup_mode | Pileup mode |
| pileup_waveform_only_mode | Pileup waveform-only mode |
| preamp_reset_delay | Preamp reset delay |
| preamp_reset_delay_en | Preamp reset delay enable |
| raw_data_length | Raw data length |
| raw_data_window | Raw data window |
| trigger_polarity | Trigger polarity |
| write_flags | Write flags |

---

## IOC Boot Files

| File | VME Crate | Description |
|---|---|---|
| `vme01.HELIOS.cmd` | VME01 | Digitizer crate 1 (boards 101–104) |
| `vme02.HELIOS.cmd` | VME02 | Digitizer crate 2 (boards 105–108) |
| `vme03.HELIOS.cmd` | VME03 | Digitizer crate 3 (boards 109–112) |
| `vme04.HELIOS.cmd` | VME04 | Digitizer crate 4 (boards 113–116) |
| `vme32.HELIOS.cmd` | VME32 | Trigger crate (MTRG + RTR1 + RTR2) |

**Location:** `/global/devel7_newbsp/gretTop/9-22/dgsIoc/iocBoot/iocArray/`

---

## Trigger Crate PVs (VME32:)

| PV Prefix | Module | Description |
|---|---|---|
| VME32:MTRG: | Master trigger | Master trigger module (slot 3) |
| VME32:RTR1: | Router 1 | Trigger router 1 (slot 4) |
| VME32:RTR2: | Router 2 | Trigger router 2 (slot 5) |

AutoSave file: `dgs_vme32_HELIOS.sav` → `/global/devel7_newbsp/boot/autosave/vme32/`

---

## DB File Locations

| File | Contents |
|---|---|
| `dgsGlobals_HELIOS_GLBL.db` | GLBL:DAQ and GLBL:DIG PVs |
| `dgsGlobals_HELIOS_VME01.db` | VME01 crate + MDIG PVs |
| `dgsGlobals_HELIOS_VME02.db` | VME02 crate + MDIG PVs |
| `dgsGlobals_HELIOS_VME03.db` | VME03 crate + MDIG PVs |
| `dgsGlobals_HELIOS_VME04.db` | VME04 crate + MDIG PVs |
| `dgsGlobals_HELIOS_VME05.db` | VME05 crate + MDIG PVs |
| `dgsGlobals_HELIOS_VME06.db` | VME06 crate + MDIG PVs |

**DB Path:** `/global/devel7_newbsp/gretTop/9-22/dgsIoc/db/`

---

## See Also

- `HELIOS_DAQ_Workflow.md` — using PVs in DAQ control (caget/caput, run control PVs)
- `HELIOS_Detector_Geometry.md` — detector layout (channel → PV mapping context)
- `rdtCut_guideline.md` — RDT detector PVs and HV channels for recoils
- `HELIOS_Experiment_Switch.md` — PVs that change between experiments (thresholds, HV)
- `expMemory_h095.md` / `expMemory_h094.md` — experiment-specific threshold and HV settings
