# HELIOS Firmware Inventory

[OK] Verified 2026-04-13 -- read live from EPICS PVs via caget (all 16 DIGs + 3 trigger modules)

## How to Read

PVs: `VME$(CRATE):$(BOARD):reg_CODE_REVISION_RBV` and `reg_CODE_DATE_RBV` (trigger modules) or `reg_code_revision_RBV` and `code_date_RBV` (digitizers, lowercase).

### Revision Encoding (16-bit)

| Bits | Field | Meaning |
|------|-------|---------|
| 15:12 | PCB revision | 1=A, 2=B, 3=C, 4=D, ... |
| 11:8 | Board type | 4=MTRG(?), 6=RTRG, 0xC=DIG |
| 7:4 | Firmware major | |
| 3:0 | Firmware minor | |

### Date Encoding

- **Trigger modules**: 16-bit, `0xMMDD` (month/day, no year)
- **Digitizers**: 32-bit, `0xYYYYMMDD` (full date)

## Current Inventory

| Board | Role | Crate | Rev (hex) | PCB | FW | Date | Notes |
|-------|------|-------|-----------|-----|----|------|-------|
| MTRG | Master Trigger | VME32 | 0x2454 | B | 5.4 | 02/19 | Board type 4 |
| RTR1 | Router 1 | VME32 | 0x2609 | B | 0.9 | 02/23 | **Older firmware** |
| RTR2 | Router 2 | VME32 | 0x260C | B | 0.C | 05/24 | **Newer than RTR1** |
| MDIG1-4 | Digitizer (×4) | VME01 | 0x4CC0 | D | C.0 | 2016-07-17 | |
| MDIG1-4 | Digitizer (×4) | VME02 | 0x4CC0 | D | C.0 | 2016-07-17 | |
| MDIG1-4 | Digitizer (×4) | VME03 | 0x4CC0 | D | C.0 | 2016-07-17 | |
| MDIG1-4 | Digitizer (×4) | VME04 | 0x4CC0 | D | C.0 | 2016-07-17 | |

## Key Observations

### [!!] RTR1 and RTR2 have different firmware versions

- **RTR1: 0x2609 (fw 0.9)** -- older
- **RTR2: 0x260C (fw 0.C)** -- newer
- **DGS production: 0x260E (fw 0.E)** -- newest

This was discovered 2026-04-12 and was previously unknown. The firmware difference could mean:
- Different MISC_STAT bit assignments between routers
- Different bug fixes or features
- Potential subtle behavioral differences during edge cases (lock recovery, throttle, etc.)

It is unclear whether this is intentional or accidental. Worth investigating whether both should be updated to match.

### Digitizers are uniform

All 16 digitizers (4 per crate, 4 crates = VME01-04) are identical: firmware C.0, built 2016-07-17.

### Trigger module dates have no year

The MTRG and RTRG date registers only store month/day (16-bit). The year of the firmware build is unknown from the register alone. Based on firmware versions and DGS history, these are likely pre-2020 builds.

## DGS Comparison

| Module | HELIOS | DGS Production | Gap |
|--------|--------|----------------|-----|
| RTRG | 0.9 / 0.C | 0.E | 2-5 minor versions behind |
| MTRG | 5.4 (type 4) | ? (type 5?) | Different board type encoding |
| DIG | C.0 | ? | Unknown |

Source: `~/dgs-doc/deep_fpga_RTRG.md` reports DGS RTRG revision 0x260E.

## How to Check

```bash
# Trigger modules
CAGET=~/epics-base/bin/linux-aarch64/caget
$CAGET VME32:MTRG:reg_CODE_REVISION_RBV VME32:MTRG:reg_CODE_DATE_RBV
$CAGET VME32:RTR1:reg_CODE_REVISION_RBV VME32:RTR1:reg_CODE_DATE_RBV
$CAGET VME32:RTR2:reg_CODE_REVISION_RBV VME32:RTR2:reg_CODE_DATE_RBV

# All 16 digitizers (note: lowercase PV names)
for vme in VME01 VME02 VME03 VME04; do
  for dig in MDIG1 MDIG2 MDIG3 MDIG4; do
    $CAGET ${vme}:${dig}:reg_code_revision_RBV ${vme}:${dig}:code_date_RBV
  done
done
```

## See Also

- `HELIOS_Trigger_MISC_STAT.md` -- bit-level register decode (differs between firmware versions)
- `~/dgs-doc/deep_fpga_RTRG.md` -- DGS RTRG firmware documentation
- `~/dgs-doc/deep_fpga_MTRG_MAIN.md` -- DGS MTRG firmware documentation
