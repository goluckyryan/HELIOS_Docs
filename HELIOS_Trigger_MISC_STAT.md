# reg_MISC_STAT_RBV Bit Map -- Trigger Modules

[OK] Verified 2026-04-12 -- extracted from EDM screens + cross-referenced with DGS VHDL source

## Overview

`reg_MISC_STAT_RBV` is a 16-bit read-only status register on the master trigger (MTRG) and router trigger (RTR1, RTR2) modules. It encodes NIM input states, link lock status, initialization state, and error flags.

**Key operational bits (same across all firmware versions):**
- **Bit 14 (All Lock)** -- all links locked and synchronized. Must be 1 for valid data.
- **Bit 15 (Lock Error)** -- a lock error has occurred (latched/sticky). If set, trigger setup must be re-run.
- **Bit 2 (Router: R Lock)** -- receive link from Master is locked.
- **Bit 2 (Master: TS roll)** -- timestamp rollover (normally 0).

## HELIOS Firmware Versions

| Module | Revision | Board Type | Firmware | Date |
|--------|----------|------------|----------|------|
| MTRG | 0x2454 | 4 | 5.4 | 0x0219 |
| RTR1 | 0x2609 | 6 (Router) | 0.9 | 0x0223 |
| RTR2 | 0x260C | 6 (Router) | 0.C | 0x0524 |

DGS production RTRG is 0x260E (fw 0.E) -- newer than HELIOS routers.
**HELIOS uses older firmware; some mid-range bits differ from DGS.**

## MTRG Bit Map (Master Trigger)

| Bit | Mask | HELIOS EDM Label | DGS VHDL (fw 0.E) | Notes |
|-----|------|------------------|---------------------|-------|
| 0 | 0x0001 | NIM In B | NIM_IN1 | NIM input 1 state |
| 1 | 0x0002 | NIM In A | NIM_IN2/TDC | NIM input 2 state |
| 2 | 0x0004 | TS roll | TS_ROLLOVER | Timestamp rollover (normally 0) |
| 3 | 0x0008 | Fast Str | FRAME_12_PENDING | **DIFF**: HELIOS=CPLD fast strobe; DGS=frame pending |
| 4 | 0x0010 | rsvd | FRAME_14_PENDING | **DIFF** |
| 5 | 0x0020 | rsvd | FRAME_16_PENDING | **DIFF** |
| 6 | 0x0040 | rsvd | FRAME_17_PENDING | **DIFF** |
| 7 | 0x0080 | rsvd | rsvd | Reserved |
| 8 | 0x0100 | L Init State 1 | LINK_INIT_STATE[0] | Same -- init state machine bit 0 |
| 9 | 0x0200 | L Init State 2 | LINK_INIT_STATE[1] | Same -- init state machine bit 1 |
| 10 | 0x0400 | L Init State 4 | LINK_INIT_STATE[2] | Same -- init state machine bit 2 |
| 11 | 0x0800 | L Init State 8 | LINK_INIT_STATE[3] | Same -- init state machine bit 3 |
| 12 | 0x1000 | Trig Veto | ANY_TRIGGER_VETO | Same -- trigger veto active |
| 13 | 0x2000 | 0 | rsvd | Reserved |
| 14 | 0x4000 | All Lock | ALL_LOCKED | **CRITICAL** -- all links locked |
| 15 | 0x8000 | Lock Error | LOCK_ERROR | **CRITICAL** -- latched lock error |

### MTRG Link Init State (bits 11:8) -- from DGS VHDL

| Value | State | Meaning |
|-------|-------|---------|
| 0 | INIT | Reset state |
| 1 | EN_SERDES | Enabling transceivers |
| 2 | SYNC | Synchronizing |
| 3 | WAIT_LOCK | Waiting for all links to lock |
| 4 | ALL_LOCK | All links locked (normal running) |
| 5 | ACKED | Lock acknowledged |
| 6 | ERROR | Lock failed |

**Expected healthy value: 5 (ACKED) = bits 8+10 set = 0x0500**

## RTRG Bit Map (Router Trigger -- RTR1, RTR2)

| Bit | Mask | HELIOS EDM Label | DGS VHDL (fw 0.E) | Notes |
|-----|------|------------------|---------------------|-------|
| 0 | 0x0001 | NIM In B | NIM_IN1 | NIM input 1 state |
| 1 | 0x0002 | NIM In A | NIM_IN2 | NIM input 2 state |
| 2 | 0x0004 | R Lock | ROUTER_LOCKED | **KEY** -- upstream link to MTRG locked |
| 3 | 0x0008 | Fast Str | rsvd | **DIFF**: HELIOS=CPLD fast strobe; DGS=reserved |
| 4 | 0x0010 | CPLD 1 | rsvd | **DIFF**: HELIOS=CPLD status; DGS=reserved |
| 5 | 0x0020 | CPLD 2 | rsvd | **DIFF** |
| 6 | 0x0040 | CPLD 4 | rsvd | **DIFF** |
| 7 | 0x0080 | CPLD 8 | rsvd | **DIFF** |
| 8 | 0x0100 | L Init State 1 | rsvd (STATE_MON) | **DIFF**: HELIOS uses these; DGS doesn't |
| 9 | 0x0200 | L Init State 2 | rsvd (STATE_MON) | **DIFF** |
| 10 | 0x0400 | L Init State 4 | rsvd (STATE_MON) | **DIFF** |
| 11 | 0x0800 | L Init State 8 | rsvd (STATE_MON) | **DIFF** |
| 12 | 0x1000 | 0 | LOST_LOCK (latched) | **DIFF**: DGS has latched lost-lock here |
| 13 | 0x2000 | 0 | rsvd | Reserved |
| 14 | 0x4000 | All Lock | ALL_LOCKED | **CRITICAL** -- all downstream DIG links locked |
| 15 | 0x8000 | Lock Error | LOCK_ERROR | **CRITICAL** -- latched lock error |

**Note on bit 12:** DGS firmware (0.E) puts `LOST_LOCK` (latched/sticky) at bit 12. HELIOS firmware (0.9/0.C) may or may not have this -- the EDM screen labels it as "0". HELIOS uses the separate `LOST_LOCK_RBV` PV instead (which reads from a different source in older firmware).

## Expected Healthy Values

| Module | Value | Hex | Active Bits |
|--------|-------|-----|-------------|
| MTRG | 17664 | 0x4500 | L Init State 1+4 (=ACKED), All Lock |
| RTR1 | 17668 | 0x4504 | R Lock, L Init State 1+4, All Lock |
| RTR2 | 17668 | 0x4504 | R Lock, L Init State 1+4, All Lock |

**Unhealthy indicators:**
- Bit 14 = 0 (All Lock off) -- link(s) not synchronized
- Bit 15 = 1 (Lock Error) -- lock was lost at some point
- RTR bit 2 = 0 (R Lock off) -- router not receiving from master

## Related PVs

| PV | Type | Description |
|----|------|-------------|
| `VME32:RTR1:LOST_LOCK_RBV` | Read | Off=OK, On=lost lock (Router 1) |
| `VME32:RTR2:LOST_LOCK_RBV` | Read | Off=OK, On=lost lock (Router 2) |
| `VME32:RTR1:SM_LOST_LOCK_RESET` | Write | Toggle On then Off to clear lost-lock flag |
| `VME32:RTR2:SM_LOST_LOCK_RESET` | Write | Toggle On then Off to clear lost-lock flag |
| `VME32:MTRG:LOCK_ACK` | Write | Acknowledge lock init (toggle 1 then 0) |
| `VME32:MTRG:LOCK_RETRY` | Write | Retry lock init (toggle 1 then 0) |
| `VME32:MTRG:IMP_SYNC` | Write | Imperative sync (1=on, 0=off) |
| `VME32:RTR1:STRINGENT_LOCK` | Write | Enable stringent lock mode |
| `VME32:RTR1:STRINGENT_LOCK_RBV` | Read | Stringent lock readback |
| `VME32:MTRG:reg_MISC_STAT2_RBV` | Read | MTRG only: SPARE_LVDS + throttle request |
| `VME32:RTR1:LOCK_COUNT_A_RBV` ... `H_RBV` | Read | Per-link lock event counters |

## What Happens on Lock Loss

When a router loses lock (`LOST_LOCK_RBV = On` or bit 15 = Lock Error):
1. System loses timestamp synchronization
2. Data from different digitizers cannot be correlated
3. **All data taken after lock loss is suspect**

Recovery: re-run `helios_setup_trigger` (see helios-prep-daq skill).

## DGS Cross-Reference

DGS documentation repo: `~/dgs-doc/` (from `gitlab.phy.anl.gov/dgs-tools-pack/doc`).

Relevant files:
- `deep_fpga_RTRG.md` -- RTRG MISC_STAT bit map (VHDL-verified 2026-04-12)
- `deep_fpga_MTRG_MAIN.md` -- MTRG MISC_STAT + MISC_STAT2 bit maps (VHDL-verified 2026-04-12)
- `deep_fpga_MTRG_VME.md` -- VME FPGA: `register_block.vhd` has register definitions
- `VME_registers.md` -- Full register map for both MTRG and RTRG
- `connectors.md` -- References "Master Trigger Registers Master Document.pdf"

EDM screen sources (HELIOS-specific labels):
- `~/digios/daq/edm/screens/gen_Master.edl` -- MTRG ByteClass widget
- `~/digios/daq/edm/screens/genRouter.edl` -- RTRG ByteClass widget
