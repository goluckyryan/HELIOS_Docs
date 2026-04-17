# HELIOS DAQ Startup

Three steps, in order. Use the `helios-prep-daq` skill for full commands and verification.

---

## Step 1 -- Start SoftIOC

The EPICS soft IOC on DAQ (.2) must be running. It provides all PV access for digitizers and triggers.

If IOC is down: restart via the DAQ console (SSH to .2, run the IOC startup script).

## Step 2 -- Setup Trigger

[!!] **Must run BEFORE digitizer setup** -- digitizers lock to the trigger routers.

Runs `helios_setup_trigger` on DAQ. Sets Master/Router clocks, locks digitizers to routers.

**Verify:** `MTRG=17664`, `RTR1/RTR2=17668`, `LOST_LOCK=Off`

## Step 3 -- Setup Digitizer

Runs `helios_setup_digitizer_4sidesArray` on DAQ. Sets all digitizer defaults (thresholds, windows, polarity).

**Verify:** Script prints `Finished - helios_setup_digitizer` with no fatal errors.

**Known harmless error:** `VME01:MDIG2:triiger_polarity0` -- typo in script (double 'i'), non-critical.

---

## See Also

- `helios-prep-daq` skill -- full automated procedure with SSH commands and verification
- `HELIOS_PV_Reference.md` -- EPICS PV names and expected values
- `expMemory_<exp>.md` -- experiment-specific digitizer settings

_Simplified 2026-04-11. Full detail in helios-prep-daq skill._
