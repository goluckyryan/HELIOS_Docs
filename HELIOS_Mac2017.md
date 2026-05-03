# Mac2017 (192.168.1.193)  --  System Reference

**Generated:** 2026-04-05  
**Host:** iMac 2017 (macOS)  
**User:** heliosdigios  
**SSH:** `ssh -i ~/.ssh/id_rsa_mac2020 -o BatchMode=yes heliosdigios@192.168.1.193`

---

## Hardware / OS

- macOS 13.0 (Ventura), 1.9 TB internal disk
- `/` (Macintosh HD): 8.2 GB used / 1.9 TB  --  **3% full**
- `/System/Volumes/Data`: 1.6 TB used / 1.9 TB  --  **83% full** [!!]
- Time Machine snapshots active
- Uptime: 51 days (as of 2026-04-08)
- [OK] Verified 2026-05-02  --  direct SSH; up 75d 1h53m, load 3.34 (normal), disk 2% used (693Gi free); InfluxDB+Grafana running

## Role

Mac2017 is the **secondary analysis Mac**  --  older hardware, likely used for:
- Archived experiment analysis (h084, older runs)
- Grafana screenshot relay (`GrafanaWeb.sh`)
- InfluxDB slow-control data extraction (`GetInfluxData.py`)

**Mac2020 is the primary analysis workstation.**

## digios Repository

- Path: `~/digios`  --  on GitHub `master` branch (up to date with GitHub)
- HEAD: `87b8817`  --  "bug fix for decoding trace, should be 0x3FFF, not 0xFFFF"
- Remote: `git@github.com:calemhoffman/digios.git` (GitHub directly)
- **Behind Mac2020** (`ff05fc0`)  --  GitHub master IS at `ff05fc0`; Mac2017 just hasn't pulled recently. Not a sync issue  --  Mac2017 is stale.
- `~/digios_master`: separate clone, HEAD `7cad141`  --  older, purpose unclear

### Branches present locally:
`4SideArray`, `ebss`, `h068_29Al`, `h072_16N`, `h073_82Kr`, `h074_238U`, `h075_20Ne`, `h076_136Xe`, `h077_29Al`, `h084_48Ca_aj`, `h084_48Ca_aj_dt`, `h092_48Ca2_aj_dp`, `master`, `s004_32Si`

## Experiments Directory (`~/experiments/`)

| Dir | Size | Notes |
|-----|------|-------|
| `h084_48Ca_aj` | 96 GB | Large  --  active or archived data |
| `h092_48Ca2_aj_dp` | 0 B | Empty |
| `ARR01` | 8 KB | Tiny  --  likely config only, has data/root_data subdirs |
| `h073_82Kr`, `h083_85Kr`, others | (not measured) | Older experiments |

Also: Screenshots from Dec 2024 (`Screenshot 2024-12-*.png`), `Screenshots of s003_10Be/`

## Running Processes of Note

- No ROOT/analysis processes running (idle)
- XProtect (Apple security), backupd (Time Machine), Microsoft AutoUpdate
- No EPICS or DAQ processes

## Special Scripts in Home Dir

| Script | Purpose |
|--------|---------|
| `GrafanaWeb.sh` | Takes screenshot of Grafana display on monitor 2, pushes to ANL web (currently disabled  --  push commented out) |
| `GetInfluxData.py` | Pulls slow-control data from InfluxDB to CSV |
| `GrafanaWeb.sh` note | Says "Push to websrv1 is disabled. Please edit mac2017:~/digios/daq/GrafanaWeb.sh" |

## Notes / Observations

- **Disk space concern:** `/System/Volumes/Data` at 82% (1.6 TB / 1.9 TB). Primary cause likely h084 experiment data (96 GB) + OS/apps.
- Mac2017 appears to be a **secondary/archival machine**  --  not actively used for current experiments
- digios is on GitHub master (not the Pi relay)  --  means DAQ pulls and Mac2020 pushes don't automatically sync here
- `digios_master` clone purpose unknown  --  may be a stale second clone

## See Also

- ~~`HELIOS_Migration_Mac2020.md`~~  --  superseded 2026-04-17 (migrated to Spark instead, not Mac2020)
- `HELIOS_Experiment_Switch.md`  --  experiment branch management (Mac2020/DAQ primary; Mac2017 manual)
- `TOOLS.md` (workspace)  --  subnet map, SSH access details
- `MEMORY.md` (workspace)  --  Mac2017 system summary + disk warning

