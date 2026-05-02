# Ptolemy Build Notes

[OK] Verified 2026-04-12 -- build tests on Pi5/ARM64 (now Spark/Jetson, same arch) and Mac2020 (x86-64)

## Source Repository

`~/Ptolemy_AI/` -- cloned from `https://github.com/goluckyryan/Ptolemy_AI`

Contains:
- `fortran/` -- original Fortran source (April 2007, Macfarlane & Pieper, ANL)
- `src/`, `include/`, `main.cpp` -- C++ translation (in progress)
- `docs/` -- manual, code map, theory docs
- `data/` -- AV18 potential, mass tables

## Pre-Built Binaries

### Ptolemy++ (C++, **PREFERRED on Spark**)
`~/Ptolemy_AI/ptolemy++` -- native ARM64 C++ binary, <0.01% error vs Fortran Ptolemy
- Runs natively on Spark (ARM64), no QEMU needed
- Same input format as Fortran Ptolemy
- **See `HELIOS_PtolemyPlusPlus.md` for full documentation**
- Build: `cd ~/Ptolemy_AI && make`

### Fortran Ptolemy (x86 32-bit, legacy)
`~/digios/analysis/Cleopatra/ptolemy` -- x86 32-bit static binary (original Fortran)
- Runs on all Linux platforms via QEMU user-mode emulation (`binfmt_misc` + `qemu-i386`)
- On Pi5: ~8x slower than native (QEMU overhead) but produces correct results

**[!!] Spark status (verified 2026-04-20):** `qemu-i386` NOT installed on Spark.
`ptolemy` (Fortran) gives "Exec format error" -- cannot run directly.
**Resolution: Use `ptolemy++` instead** (same input, native ARM64, <0.01% error).
Alternative: `sudo apt install qemu-user` or run on Mac2020 (x86-64) via SSH.

## Build Test Results (2026-04-12)

### x86 32-bit (`-m32`) -- the correct build

- **Pi5 (ARM64):** Cannot build -- `-m32` is x86-only, not supported on ARM
- **Mac2020 (x86-64 macOS):** Cannot build -- Apple dropped 32-bit support since Catalina
- **DAQ (CentOS 6 x86-64):** Should work (has `gcc-multilib`) but not tested (read-only policy)
- **Any Linux x86-64 with `gcc-multilib`:** Works (verified on Ubuntu 24.04 per README)

### ARM 32-bit (armhf cross-compile on Pi5)

- **Compiles:** Yes, using `arm-linux-gnueabihf-gfortran` (installed via apt)
- **Runs:** Yes, but **produces incorrect results**
- **Error:** `L, SP AND JP DO NOT FORM A TRIANGLE` -- spin quantum number parsing fails
- **Cause:** ARM vs x86 differences in integer rounding or EQUIVALENCE/COMMON block alignment
- Binary at `~/Ptolemy_AI/fortran/ptolemy_arm32`

### x86-64 / ARM-64 (`-O0`, no `-m32`)

- **Mac2020 (x86-64):** Compiles and runs with `gfortran-15 -O0`
- **Pi5 (ARM-64):** Compiles and runs with `gfortran -O0`
- **Results vs x86-32 reference (16O(d,p)17O at 20 MeV):**
  - Total cross section: **identical** (35.050 mb)
  - DCS values: **identical** (1 value differs by 0.002% at 130 deg -- last-digit rounding)
  - S-matrix phases: **differ by exactly pi** -- sign convention, not physics error
  - `LOC`/`BIASES` addresses: overflow 32-bit range but allocator still works
  - One `IEEE_INVALID_FLAG` warning on 64-bit (signaling NaN, did not affect results)
- **[!!] WARNING:** README states 64-bit can produce incorrect results for some reactions, even at `-O0`. This single test case passed, but other reactions may not.
- **[!!] `-O1` and higher are known to break** the 64-bit build

### Why 64-bit is risky

The Fortran code relies on:
1. **INTEGER for pointer arithmetic** -- `numbered_store.f`, `keep.f` use INTEGER*4 to store memory addresses (overflow on 64-bit)
2. **EQUIVALENCE mixing INTEGER and REAL** -- same size (4 bytes) on 32-bit, but 64-bit default INTEGER may differ
3. **Implicit SAVE behavior** -- uninitialized variable persistence between subroutine calls
4. **Optimization-sensitive rounding** -- `-O1+` changes floating-point evaluation order

### Debug prints in source

`source.f` contains unconditional `WRITE(0,...)` debug statements (`FTN_SM`, `FTN_BETA_LX4`) that go to stderr (unit 0). Separate stderr when running:
```bash
./ptolemy < input.in > output.out 2>/dev/null
```

## macOS Notes

- `brew install gcc` on Mac2020 installed `gfortran-15` (GCC 15.2.0)
- macOS uses `gcc-15`/`gfortran-15` (not `gcc`/`gfortran` which are Apple Clang wrappers)
- Apple Clang assembler does not support `-m32` (i386 instructions rejected)

## See Also

- `~/Ptolemy_AI/fortran/README.md` -- build instructions and warnings
- `~/Ptolemy_AI/docs/PTOLEMY_MANUAL.md` -- input format and examples
- `~/digios/analysis/Cleopatra/` -- Transfer binary (generates Ptolemy inputs from reaction parameters)
- `HELIOS_Simulation_Cleopatra.md` -- Cleopatra/Ptolemy workflow, kinematics, DWBA overview
