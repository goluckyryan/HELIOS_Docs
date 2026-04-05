# HELIOS Experiment Switch Procedure

**For HELIOS AI use** — replicates what `SetUpNewExp` does, non-interactively.
Run these steps whenever asked to switch experiment branches on DAQ and/or Mac2020.

---

## Pre-flight Checks (always do first)

1. **Verify both machines are clean:**
   ```bash
   # DAQ
   ssh digios1: cd ~/digios && git status --porcelain --untracked-files=no
   # Mac2020
   ssh mac2020: cd ~/digios && git status --porcelain --untracked-files=no
   ```
   If not clean → commit or stash before proceeding.

2. **Verify DAQ and Mac2020 are on same branch.**

---

## Switch to NEW experiment (e.g. h095_11C_dp_2)

### On Mac2020 (Darwin, phywl094)

```bash
cd ~/digios
git fetch pi
git checkout <expName>        # or git checkout -b <expName> if new branch
```

**If NEW branch:**
- Edit `expName.sh`:
  ```bash
  expName=<expName>
  daqDataPath=~/experiments     # Mac2020 data root
  LastRunNum=0
  ```
- Create data directories (Mac2020 only — no merged_data):
  ```bash
  mkdir -p ~/experiments/<expName>/data
  mkdir -p ~/experiments/<expName>/root_data
  ```
- Update symlinks:
  ```bash
  ln -sfv ~/experiments/<expName>/data      ~/digios/analysis/data
  ln -sfv ~/experiments/<expName>/root_data ~/digios/analysis/root_data
  ```
- Tell InfluxDB:
  ```bash
  curl -s -XPOST "http://192.168.1.193:8086/write?db=testing" \
    --data-binary "SavingData,expName=<expName> value=0" \
    --max-time 1 --connect-timeout 1
  ```
- Clean working directory:
  ```bash
  rm -fv ~/digios/analysis/working/reaction.dat
  rm -fv ~/digios/analysis/working/run_Summary.dat
  rm -fv ~/digios/analysis/working/RunTimeStamp.dat
  rm -fv ~/digios/analysis/working/*.root
  rm -fv ~/digios/analysis/working/*.d
  rm -fv ~/digios/analysis/working/*.so
  rm -fv ~/digios/analysis/working/*.pcm
  ```
- Commit and push:
  ```bash
  git add -A
  git commit -m "new experiment <expName>"
  git push pi <expName>
  ```

**If EXISTING branch:**
- Just update symlinks (data dirs already exist):
  ```bash
  ln -sfv ~/experiments/<expName>/data      ~/digios/analysis/data
  ln -sfv ~/experiments/<expName>/root_data ~/digios/analysis/root_data
  ```
- Tell InfluxDB (same curl as above)

---

### On DAQ (digios1, Linux)

⚠️ DAQ data layout is different — raw data goes directly under `<daqDataPath>/<expName>/`, NO `data/` subdir.

```bash
cd ~/digios
git fetch origin    # origin = Pi relay
git checkout <expName>    # or git checkout -b <expName> if new
```

**If NEW branch:**
- Edit `expName.sh`:
  ```bash
  expName=<expName>
  daqDataPath=<chosen disk, e.g. /media/DIGIOSDATA6>
  LastRunNum=0
  ```
- Create data directory (DAQ only — no subdirs):
  ```bash
  mkdir -p <daqDataPath>/<expName>
  ```
- ⚠️ **NO symlink needed on DAQ.** `start_run.sh` saves data directly to `${daqDataPath}/${expName}/` — the `analysis/data` symlink is not used by any DAQ scripts and is not required.
- Tell InfluxDB:
  ```bash
  curl -s -XPOST "http://192.168.1.193:8086/write?db=testing" \
    --data-binary "SavingData,expName=<expName> value=0" \
    --max-time 1 --connect-timeout 1
  ```
- Commit and push to Pi:
  ```bash
  git add expName.sh
  git commit -m "new experiment <expName>"
  git push origin <expName>
  ```

**If EXISTING branch:**
- Update `expName.sh` (LastRunNum etc.) only
- No mkdir or symlink needed

---

## Switch to MASTER (ARR01 = between experiments)

### On Mac2020
```bash
cd ~/digios && git fetch pi && git checkout master
# Update symlinks to ARR01
ln -sfv ~/experiments/ARR01/data      ~/digios/analysis/data
ln -sfv ~/experiments/ARR01/root_data ~/digios/analysis/root_data
curl -s -XPOST "http://192.168.1.193:8086/write?db=testing" \
  --data-binary "SavingData,expName=ARR01 value=0" --max-time 1 --connect-timeout 1
```

### On DAQ
```bash
cd ~/digios && git fetch origin && git checkout master
# No disk, mkdir, or symlink change needed — data saves directly via expName.sh
```

---

## After switching — always sync Pi → GitHub
```bash
~/digios_sync_github.sh
```

---

## Key Facts
- **DAQ data path**: `/media/DIGIOSDATA6/<expName>/` (no subdirs — raw data only, no data/ or root_data/ on DAQ)
- **DAQ symlink**: `analysis/data` symlink is NOT needed on DAQ — `start_run.sh` writes directly to `${daqDataPath}/${expName}/`; do not create it during SetUpNewExp
- **Mac2020 data path**: `~/experiments/<expName>/data` and `~/experiments/<expName>/root_data` (no merged_data — GEBSort removed)
- **InfluxDB**: `192.168.1.193:8086`, db=`testing`
- **DAQ origin**: Pi relay (`ryan@192.168.1.100:~/digios.git`)
- **Mac2020 pi remote**: `ryan@192.168.1.100:~/digios.git`
- **DAQ and Mac2020 must always be on the same branch**
- **master = ARR01** (between experiments)
- **`expName.sh`** is the source of truth for current experiment name and last run number
