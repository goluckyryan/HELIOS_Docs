# HELIOS Magnet Pi (192.168.1.208)

[OK] Verified 2026-04-16 -- SSH read-only exploration

## Overview

Raspberry Pi 5 (aarch64) at 192.168.1.208, hostname `heliosPi`.
Monitors the Oxford 601-048T magnet supervisory controller and posts LHe/shield status.

## Access

```bash
sshpass -p '<password>' ssh -o StrictHostKeyChecking=no helios@192.168.1.208
```
User: `helios` -- see `security/credentials.md` for password

## What It Does

1. Reads **Oxford MPS 601-048T** via serial (`/dev/ttyUSB1`, 4800 baud)
2. Parses: LHe level (%), shield temperature (K), shim PSU status
3. Posts rendered PNG to **Discord** via webhook
4. Posts HeLevel and HeTemp to **InfluxDB** on Mac2017 (192.168.1.193, db=testing)
5. Saves `magnet_out.txt` and `magnet_out.png`

## Cron

```
0 7 * * *  /home/helios/HELIOSMagControl/monitor.py >> monitor_cron.log
```
Runs once daily at 7:00 AM. Single snapshot, not continuous.

## Key Files (`~/HELIOSMagControl/`)

| File | Purpose |
|------|---------|
| `monitor.py` | Main script: read serial, parse, post to Discord + InfluxDB |
| `MonitorTerminal.py` | Interactive terminal for the Oxford controller |
| `MPSControl.py` | Interactive console for the Siemens Magnet Power Supply -- **NEVER TESTED** |
| `MPSControl_2.py` | Variant of MPS control -- **NEVER TESTED** |
| `render_raw.py` | Parse ANSI escape sequences from serial output |
| `txt_to_png.py` | Render parsed text to PNG (Pillow) |
| `discord.WebHook` | Discord webhook URL for posting |
| `magnet_out.txt` | Latest status text |
| `magnet_out.png` | Latest status PNG |
| `monitor_cron.log` | Cron output log |
| `README.md` | Full documentation including Oxford command reference |

## Oxford 601-048T Serial Protocol

- Port: `/dev/ttyUSB1`, 4800 baud
- Sequence: ESC → wait 2s → CR → wait 6s → flush → `R\r`
- Response: full status screen with ANSI escape codes

### Key Commands

| Cmd | Function |
|-----|----------|
| `R` | Full status display |
| `DEM` | Set shim demand (channel, polarity, mA) |
| `ON/OFF` | Shim amplifiers on/off |
| `Z/H nnn` | Set 0%/100% He level ADC calibration |

## Status Display Fields

| Field | Location | Current Value (Apr 15) |
|-------|----------|----------------------|
| LHe Level | He Parameters → LEVEL | 62.1% |
| Shield Temp | Shield → Temp | 65 K |
| Shim PSUs (5) | Right panel | All 4.68A, 22.4V, 105W, OK |
| CCA Cabinet Temp | Bottom left | 23.4°C |

## Status Flags

### NIN_ (Inputs to supervisory)

| Flag | Meaning | Normal |
|------|---------|--------|
| NIN_MSG_SYSON | Main PSU system on | Active |
| NIN_MSG_EISOK | Emergency interlock OK | Active |
| NIN_MSG_HTROK | Heater OK | Active |
| NIN_MSG_SWITOK | Quench protection OK | Active |
| NIN_MSG_FRIG_NORM | Cryocooler normal | Active |
| NIN_MSG_ALARMOK | No alarms | Active |
| NIN_PROBE_OC | He probe open circuit | Inactive (good) |

### NOUT_ (Outputs from supervisory)

| Flag | Meaning | Normal |
|------|---------|--------|
| NOUT_MEASURE_ON | Enable signal to main PSU | Active |
| NOUT_HE_WARN | He level warning | Inactive (good) |
| NOUT_HE_ALARM | He level alarm | Inactive (good) |
| NOUT_FRIDGE_ON | Cryocooler on | Active |

## LHe Consumption Rate

From cron log (Apr 6-15):
- 71.9% → 62.1% in 9 days = **~1.1%/day** (standby, no beam)
- With beam, consumption increases (vibration + heat load)

**Updated 2026-04-20:** He level = **92.3%** (read from InfluxDB via Mac2017, 2026-04-19 12:00 UTC)
- Level much higher than Apr 15 reading (62.1%) -- LHe fill occurred during experiment
- At 1.1%/day standby: 50% warning ~May 11, 30% alarm ~May 29

## InfluxDB Measurements

| Measurement | Tag | Posted from |
|-------------|-----|-------------|
| HeLevel | (none) | magnet Pi |
| HeTemp | (none) | magnet Pi |

## Known Issue (2026-03-31)

NIN_MSG_SYSON was inactive → NOUT_MEASURE_ON inactive → main PSU inhibited.
Root cause: CAN bus communication issue between main PSU and supervisory.
Resolution: not documented (presumably fixed since magnet is currently at 2.85T).

## [!!] Rules

- **READ ONLY** -- do not write, modify, or execute anything on this Pi
- This Pi controls the magnet and cryogenics -- hands off
- Only Ryan may authorize changes

## Oxford IPS120-10 Power Supply Hardware Interface

**Source:** `~/Magnet/README.md` + Oxford IPS120-10 Operator's Handbook Rev 13 (86pp)

The HELIOS magnet uses an **Oxford IPS120-10** superconducting magnet power supply (120 A, 10 V).

### Parallel I/O Interface (rear panel, 15-way D-type, "PARALLEL I/O" / SK2)

Two key hardware interlocks:

| Pin | Signal | Direction | Function |
|---|---|---|---|
| **12** | Safe Current Interlock | Output | Active-low (sinks ~10mA) when current within safe limits; high-Z when unsafe |
| **14** | Auto-Run-Down | Input | Logic 1 (+5V ref pin 8) triggers emergency de-energise |
| 7 | +5V | Power | Reference for interlock circuits |
| 8 | 0V | Ground | |

### Auto-Run-Down Sequence (§9)
Triggered by Pin 14 high, or LHe level meter:
1. Unclamp if clamped
2. Sweep leads to last persistent current (if switch heater was off)
3. Wait 20s → turn switch heater on
4. De-energise in low-voltage mode (±1V)
5. Wait 20s → clamp output + turn off switch heater
6. **Operator locked out until external signal cleared**

⚠️ Only works if PSU is left powered on. Designed to protect magnet if LHe level drops critically low.

### Safe Current Interlock (§5.16.1)
- Output transistor sinks current (open-collector) when safe
- Current limits set via Test Mode §11.10 or read via serial `X` command
- NOT shown on front panel display

### Related docs in `~/Magnet/`
- `Oxford_IPS120-10_Manual.pdf` -- full operator handbook (JLab copy)
- `Oxford_IPS120-10_Datasheet.pdf` -- IPS120-10 / IPS125-9 datasheet
- `Oxford_Mercury_iPS_Manual.pdf` -- Mercury iPS manual (169pp)
- `page16_parallel_interface.png` through `page47_fault_conditions.png` -- extracted key pages

## See Also

- `~/HELIOSMagControl/README.md` -- full command reference and flag documentation
- `HELIOS_Firmware_Inventory.md` -- other system hardware
