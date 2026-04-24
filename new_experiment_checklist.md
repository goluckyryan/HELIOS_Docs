# new_experiment_checklist.md  --  New Experiment Setup (MANDATORY)

Full checklist for setting up a new HELIOS experiment from scratch  --  covers DAQ, Mac2020, Spark repo, and analysis working directory.

---

## Part 1  --  DAQ/Mac2020/Spark Infrastructure

Follow `HELIOS_Experiment_Switch.md` for the detailed procedure. Summary:

### Step 1  --  DAQ (digios1, 192.168.1.2)
- [ ] **Check disk space** on `/media/DIGIOSDATA6`: `df -h /media/DIGIOSDATA6`  --  must have sufficient free space for the experiment (3-day run ~ few hundred GB typical). Flag if <500 GB free. **Record the result (size/used/free/date) in `expMemory_<expName>.md` under a "Storage" section.**
- [ ] `git fetch origin && git checkout -b <expName>` (branch from master)
- [ ] **Edit** `expName.sh`: set `expName=<expName>`, `daqDataPath=/media/DIGIOSDATA6`, `LastRunNum=0`
- [ ] `mkdir -p /media/DIGIOSDATA6/<expName>`  --  create raw data directory
- [ ] Notify InfluxDB: `curl -XPOST "http://192.168.1.193:8086/write?db=testing" --data-binary "SavingData,expName=<expName> value=0"`
- [ ] `git add expName.sh && git commit -m "new experiment <expName>" && git push origin <expName>`

### Step 2  --  Mac2020 (192.168.1.164)
- [ ] `git fetch spark && git checkout <expName>` (gets `expName.sh` automatically from DAQ commit; spark = Spark relay)
- [ ] `mkdir -p ~/experiments/<expName>/data ~/experiments/<expName>/root_data`
- [ ] Update symlinks:
  ```bash
  rm ~/digios/analysis/data ~/digios/analysis/root_data
  ln -s ~/experiments/<expName>/data ~/digios/analysis/data
  ln -s ~/experiments/<expName>/root_data ~/digios/analysis/root_data
  ```
- [ ] No InfluxDB call, no commit needed

### Step 3  --  Spark working repo (`~/digios`)
- [ ] `git fetch /home/heliosspark/digios.git <expName>:<expName> && git checkout <expName>`
- [ ] Verify `expName.sh` is correct

### Step 4  --  Spark -> GitHub sync
- [ ] `~/digios_sync_github.sh`  --  pushes all branches to GitHub

---

## Part 2  --  Analysis Working Directory

Working dir lives inside the experiment's digios repo on Spark:
**`<digios_repo>/analysis/working_Helios/<expName>/`**

- **Standard repo (h096+):** `~/digios/analysis/working_Helios/<expName>/`
- [!!] `~/digios_11C_2/` is a **special one-off** for h095 (11C analysis)  --  not a template, do not replicate
- The entire `analysis/working_Helios/` folder is git-ignored  --  local to Spark only

### Step 5  --  Create working dir skeleton

**Structure (mandatory for all experiments):**
```
analysis/working_Helios/
??? GeneralSortMapping.h   -> <expName>/GeneralSortMapping.h
??? correction_e.dat       -> <expName>/correction_e_alpha.dat
??? correction_e_alpha.dat -> <expName>/correction_e_alpha.dat
??? correction_xf_xn.dat   -> <expName>/correction_xf_xn.dat
??? correction_xfxn_e.dat  -> <expName>/correction_xfxn_e.dat
??? correction_scaleX.dat  -> <expName>/correction_scaleX.dat
??? exp.md                 -> <expName>/exp.md
??? plot_index.md          -> <expName>/plot_index.md
??? <expName>/             (real files live here)
```

Steps:
- [ ] `mkdir -p <digios_repo>/analysis/working_Helios/<expName>/`
- [ ] Copy `GeneralSortMapping.h` from `analysis/working/` into `<expName>/`
- [ ] Create empty placeholder correction files in `<expName>/`: `correction_e_alpha.dat`, `correction_xf_xn.dat`, `correction_xfxn_e.dat`, `correction_scaleX.dat`
- [ ] Create `<expName>/exp.md` and `<expName>/plot_index.md`
- [ ] Create symlinks in `working_Helios/` root pointing into `<expName>/`:
  ```bash
  cd analysis/working_Helios
  ln -sfv <expName>/GeneralSortMapping.h GeneralSortMapping.h
  ln -sfv <expName>/correction_e_alpha.dat correction_e_alpha.dat
  ln -sfv <expName>/correction_e_alpha.dat correction_e.dat
  ln -sfv <expName>/correction_xf_xn.dat correction_xf_xn.dat
  ln -sfv <expName>/correction_xfxn_e.dat correction_xfxn_e.dat
  ln -sfv <expName>/correction_scaleX.dat correction_scaleX.dat
  ln -sfv <expName>/exp.md exp.md
  ln -sfv <expName>/plot_index.md plot_index.md
  ```
- [ ] Add more symlinks as files are generated (reactionConfig.txt, detectorGeo.txt, transfer.root, etc.)
- [ ] Work in `working_Helios/` root  --  all paths resolve transparently via symlinks
- [ ] To switch experiments: update symlinks to point at new `<expName>/` subdir
- [ ] Verify `analysis/working_Helios/` is in `.gitignore` of that repo

### Step 6  --  Create expMemory file
- [ ] Create `~/.openclaw/workspace/expMemory_<expName>.md` with:
  - Reaction, B-field, beam energy, target
  - Data locations (DAQ raw, Mac2020 root_data, Spark working dir)
  - digios branch name
- [ ] Register in `USER.md`: add channel ID -> expMemory file mapping
- [ ] Add brief entry to `MEMORY.md`
- [ ] Commit and push workspace to Mac2020

---

## Part 2.5  --  Kinematics Setup (once proposal/beam energy is known)

**Workspace split:**
- **Mac2020 `analysis/working/`** -- user workspace, in git, tracked. reactionConfig.txt, detectorGeo.txt, Ex.txt, transfer.root all live HERE on Mac2020.
- **Spark `analysis/working_Helios/`** -- AI workspace, gitignored. transfer.root generated HERE on Spark. Symlinks to `../working/` config files.
- **Spark `analysis/working/`** -- stays in sync with Mac2020 via git (same branch). AI reads configs here, does not generate files here.

### Step 1 -- Edit config files (on both Mac2020 and Spark via SCP/git)

- [ ] Edit `analysis/working/reactionConfig.txt`:
  - beam_A, beam_Z, beam energy (MeV/u), target_A/Z, light recoil A/Z
  - Set `isTargetScattering=false` (skip SRIM -- target thickness unknown, effect tiny)
  - SRIM filenames don't matter when isTargetScattering=false, but update them anyway
- [ ] Edit `analysis/working/detectorGeo.txt`:
  - Bfield (negative = into page), first_position (negative = upstream), recoil_position
  - [!!] Proposal may say "800 cm" for RDT -- almost certainly a typo, should be "800 mm"
- [ ] Edit `analysis/working/Ex.txt` -- list excitation energies of interest:
  ```
  //Ex   relative_xsec   SF   sigma_in_MeV
  0.000    1.0     1.0     0.0100
  1.9417   1.0     1.0     0.0100
  ...
  #============_End_of_file
  ```
- [ ] SCP updated files to Mac2020: `scp -i ~/.ssh/id_rsa_mac2020 ... heliosdigios@192.168.1.164:~/digios/analysis/working/`
- [ ] Then `git pull` on Spark to get updated working/ files

### Step 2 -- Set up symlinks in working_Helios/ on Spark

```bash
cd ~/digios/analysis/working_Helios
ln -sfv ../working/reactionConfig.txt reactionConfig.txt
ln -sfv ../working/detectorGeo.txt detectorGeo.txt
ln -sfv ../working/Ex.txt Ex.txt
```

### Step 3 -- Compile and run Transfer binary

**On Mac2020** (has ROOT + can write to working/):
```bash
cd ~/digios/analysis/Cleopatra && make Transfer
cd ~/digios/analysis/working   # MUST run from working/ -- reads reactionConfig.txt and detectorGeo.txt relative to CWD
../Cleopatra/Transfer
# output: transfer.root and reaction.dat in working/
```

**On Spark** (ROOT in PATH via ~/.bashrc):
```bash
cd ~/digios/analysis/Cleopatra && make Transfer
cd ~/digios/analysis/working_Helios  # run from working_Helios/ -- uses symlinked configs
../Cleopatra/Transfer
# output: transfer.root and reaction.dat directly in working_Helios/ (NOT symlinks)
```

- [!!] transfer.root and reaction.dat are **real files** in working_Helios/ -- NOT symlinked
- [!!] transfer.root is gitignored -- local only on each machine
- [!!] Ex.txt must be present (as symlink or file) in the CWD when Transfer runs, or it defaults to ground state only

### Step 4 -- Verify and plot

- [ ] Check Transfer output: reaction name, B-field, array positions, number of states loaded
- [ ] Plot E-Z: gate on `hit==1 && loop==1`, draw `fxList` (kinematic lines) and `gList->At(0)` (thetaCM=0) from transfer.root
- [ ] Commit `reactionConfig.txt`, `detectorGeo.txt`, `Ex.txt` to git (tracked in working/)
  - `transfer.root` and `reaction.dat` are gitignored -- never commit
- [ ] Push to Spark bare repo -> Mac2020 pulls

---

## Part 3  --  Required Analysis Files

Populate the working dir as data becomes available:

| File | Content | When |
|------|---------|------|
| `exp.md` | Run log, array configs, Ex ranges, good runs, RDT cut files, beam notes | Before first run |
| `plot_index.md` | Sequential plot index (Plot-NNN) | Before first plot |
| `reactionConfig.txt` | Beam/target/recoil definition | Before sorting |
| `Ex.txt` | Excitation energies to simulate | Before Cleopatra |
| `detectorGeo_<config>.txt` | One per array position | Before sorting |
| `detectorGeo.txt` | Symlink -> active config | Before sorting |
| `reaction_<config>.dat` | Generated by Transfer binary | Before sorting |
| `reaction.dat` | Symlink -> active config | Before sorting |
| `transfer_<config>.root` | Generated by Transfer binary | Before sorting |
| `transfer.root` | Symlink -> active config | Before sorting |
| `GeneralSortMapping.h` | Channel mapping (copy  --  not symlink) | Before sorting |
| `correction_e_alpha.dat` | Energy cal (generate fresh  --  NOT copied from Ryan) | After alpha source run |
| `correction_e.dat` | Symlink -> correction_e_alpha.dat | After energy cal |
| `correction_xf_xn.dat` | Xf/Xn gain match | After energy cal |
| `correction_xfxn_e.dat` | Xs->E linearity | After xf/xn cal |
| `correction_scaleX.dat` | X position scale | After Xs->E cal |
| `alpha_calib_228Th_v5.C` | Calibration macro | Before energy cal |
| `xfxn_calib.C` | xnCorr macro | Before xf/xn cal |
| `xfxne_calib.C` | xfxne macro | Before Xs->E cal |
| `xscale_calib.C` | xScale macro | Before X scale cal |
| `rdtCuts_<name>.root` | RDT cut file (copy  --  not symlink) | Before physics analysis |
| `<exp>_analysis_procedure.md` | Full calibration pipeline with lessons learned | During analysis |

---

## Part 4  --  Calibration Order (non-negotiable)

1. Energy -> `correction_e_alpha.dat`
2. Xf/Xn gain -> `correction_xf_xn.dat`
3. Xs->E linearity -> `correction_xfxn_e.dat`
4. X scale -> `correction_scaleX.dat`

Config files are **real copies** (not symlinks to `working/`). Code files (Monitors.C, Armory/) and data (root_data/) may be symlinks.

---

## Part 5  --  Hardware Setup (before first run)

- [ ] **HV**  --  ramp silicon array HV to operating voltage (see HV ramp rules in `MEMORY.md`)
- [ ] **Thresholds**  --  set `led_threshold` per channel via `caput VME0X:MDIGn:led_threshold<CH> <value>`
  - [!!] `SetVMEThreshold` script uses **old 6-side array labels** (TT/TL/TR/BR/BB/BL)  --  **do not use until updated for 4-side array**
  - Set thresholds directly via `caput` or via `HELIOSArraySettings_4sidesArray.edl` EDM screen
  - [OK] **`HELIOSArraySettings_4sidesArray.edl`**  --  the real, active threshold screen
  - [X] **`HELIOSThresholds.edl`**  --  STALE, wrong PVs, do not use
- [ ] **Trigger**  --  configure with `SetVMETrigger` and `helios_setup_trigger`
- [ ] **Alpha source run**  --  required before physics; used for energy calibration

---

## Plot Index Convention

Create `plot_index.md` in the working dir before any plots:

```markdown
# Plot Index  --  <expName>

| Plot | File | Description |
|------|------|-------------|
| Plot-001 | ... | ... |
```

- Format: `Plot-NNN` (zero-padded to 3 digits, sequential, never reused)
- Every plot filename and title must include the index number

---

_Updated: 2026-04-08  --  restructured as full setup checklist; fixed working dir path; added SetVMEThreshold 6-side array warning; added Part 1 infrastructure steps_

---

## See Also
- `HELIOS_Experiment_Switch.md`  --  detailed DAQ/Mac2020 branch switching procedure
- `HELIOS_Calibration.md`  --  complete calibration reference (physics, code, lessons per step)
- `HELIOS_Detector_Geometry.md`  --  channel mapping, experiment-specific hardware issues
- `HELIOS_Simulation_Cleopatra.md`  --  kinematics / DWBA setup for new reaction
- `rdtCut_guideline.md`  --  RDT cut methods (hand-drawn, SRIM, ML, FOM)
