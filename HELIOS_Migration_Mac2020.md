# HELIOS AI Migration Plan: Pi → Mac2020

**Goal:** Move HELIOS AI (OpenClaw) from Pi (192.168.1.100) to Mac2020 (192.168.1.164),
then decommission the Pi entirely from the HELIOS subnet.

**Status (2026-04-06):** ⏸ Not started — Node.js and OpenClaw not yet installed on Mac2020.
Mac2020 is reachable and healthy. Migration is planned but not scheduled.

---

## Phase 1 — Prepare Mac2020

### 1.1 Install Node.js
```bash
# Check if already installed
node --version   # need v18+
# If not: install via homebrew
brew install node
```

### 1.2 Install OpenClaw
```bash
npm install -g openclaw
openclaw --version
```

### 1.3 Verify network access
```bash
# Mac2020 must reach Discord (internet via eduroam) and DAQ subnet
ping 192.168.1.2    # DAQ
ping 192.168.1.20   # VME IOC
curl -s https://discord.com | head -1
```

### 1.4 Prevent sleep
```bash
# Mac2020 must not sleep if running as a server
# System Preferences → Energy Saver → "Prevent computer from sleeping"
# Or via CLI:
sudo pmset -a sleep 0 disksleep 0
```

---

## Phase 2 — Transfer Workspace

### 2.1 Copy workspace from Pi to Mac2020
```bash
# Run from Mac2020:
scp -r ryan@192.168.1.100:~/.openclaw/ ~/.openclaw/
```

### 2.2 Adapt config paths
- Edit `~/.openclaw/config.json` (or equivalent) on Mac2020
- Update `workdir` from `/home/ryan/.openclaw/workspace` → `/Users/heliosdigios/.openclaw/workspace`
- Keep same Discord bot token, API keys — no change needed

### 2.3 Update TOOLS.md
- Change host machine entry: `pi5-2 (192.168.1.100)` → `Mac2020 (192.168.1.164)`
- Update SSH notes: Mac2020 is now local, Pi no longer needed
- DAQ SSH: Mac2020 already has `~/.ssh/id_rsa_daq` — no change needed

### 2.4 Update MEMORY.md
- Change `Host: pi5-2 (Raspberry Pi 5)` → `Host: Mac2020 (192.168.1.164)`
- Remove Pi-specific notes (eth0/wlan0 network config, etc.)

---

## Phase 3 — EPICS / CA on Mac2020

### 3.1 Set environment variables
Add to `~/.zshrc` (Mac uses zsh by default):
```bash
export EPICS_CA_SERVER_PORT=5064
export EPICS_CA_REPEATER_PORT=5065
export EPICS_CA_AUTO_ADDR_LIST=YES
```

### 3.2 Verify caget works
```bash
source ~/.zshrc
# caget should already be on PATH via heliosrc.sh / digios env
source ~/digios/heliosrc.sh
caget VME01:MDIG1:led_threshold0
```

### 3.3 pyepics (optional — if Python CA access needed)
- Need EPICS base built or installed on Mac2020 for `libca.dylib`
- Or symlink from digios EPICS installation if available
- Set: `export PYEPICS_LIBCA=<path to libca.dylib>`

---

## Phase 4 — Git Relay: Remove Pi as Relay

Currently: `DAQ → Pi bare repo (~/digios.git) → GitHub`

After migration, Mac2020 has internet — it can push directly to GitHub.

### 4.1 Add GitHub remote to Mac2020
```bash
cd ~/digios
git remote add github git@github.com:calemhoffman/digios.git
# Verify SSH key for GitHub is set up on Mac2020
ssh -T git@github.com
```

### 4.2 Update DAQ origin
DAQ currently pulls from Pi (`ryan@192.168.1.100:~/digios.git`).
Options:
- **Option A:** Keep Pi bare repo running (simplest — DAQ doesn't change)
- **Option B:** Set up bare repo on Mac2020 and update DAQ origin:
  ```bash
  # On Mac2020: create bare repo
  git clone --bare ~/digios ~/digios.git

  # On DAQ: update origin
  git remote set-url origin heliosdigios@192.168.1.164:~/digios.git
  ```
- **Recommendation:** Option A is safer during transition. Option B removes Pi dependency fully.

### 4.3 Update daily sync cron
- Cancel Pi cron job (`~/digios_sync_github.sh` at 4AM on Pi)
- Set up equivalent cron on Mac2020 to push to GitHub directly

---

## Phase 5 — Start OpenClaw on Mac2020

```bash
# On Mac2020:
openclaw gateway start

# Verify it connects to Discord
openclaw gateway status
```

---

## Phase 6 — Stop OpenClaw on Pi

```bash
# SSH into Pi first, confirm Mac2020 is live
ssh ryan@192.168.1.100
openclaw gateway stop
# Or: systemctl stop openclaw (if running as service)
```

---

## Phase 7 — Decommission Pi

### 7.1 Final data/config backup
```bash
# From Mac2020 — grab anything remaining
scp -r ryan@192.168.1.100:~/IsegSNMPGUI/ ~/IsegSNMPGUI/
scp ryan@192.168.1.100:~/HELIOS_*.md ~/
scp ryan@192.168.1.100:~/*.sh ~/
```

### 7.2 Migrate IsegMonitor.py
- `IsegMonitor.py` currently runs on Pi, polling HV and pushing to InfluxDB at 192.168.1.193
- Move to Mac2020: `cd ~/IsegSNMPGUI && nohup python3 -u IsegMonitor.py >> /tmp/iseg_monitor.log 2>&1 &`
- Or set up as a launchd service on Mac2020 for auto-restart

### 7.3 Remove Pi from subnet table (TOOLS.md)
- Delete `192.168.1.100 | pi5-2 | Raspberry Pi 5 | HELIOS AI` row
- Update any SSH configs that reference 192.168.1.100

### 7.4 Physical decommission
- Power down Pi: `sudo poweroff`
- Disconnect from switch
- Update subnet documentation

---

## Phase 8 — Post-Migration Verification

- [ ] Discord bot responding from Mac2020
- [ ] `caget` working (EPICS CA to VME IOCs)
- [ ] HV monitor (`IsegMonitor.py`) pushing to InfluxDB / Grafana showing data
- [ ] Git relay working (DAQ can push, Mac2020 can push to GitHub)
- [ ] `Process_RUN` and ROOT analysis working natively
- [ ] Heartbeat/cron jobs running on Mac2020

---

## Key Advantages After Migration

- **ROOT native** — no SSH batch workaround, persistent interactive sessions
- **Direct data access** — `~/experiments/` is local, no rsync hop
- **Faster analysis** — Mac2020 has more CPU/RAM than Pi 5
- **Simpler topology** — one fewer machine in the chain

## Risks / Watchouts

- Mac2020 must **not sleep** — configure Energy Saver permanently
- Mac2020 IP (192.168.1.164) assumed static — verify it doesn't change
- `heliosdigios` user must have all required permissions
- launchd (not systemd) for Mac services — syntax is different


---

## See Also

- `HELIOS_DAQ_Workflow.md` — current DAQ workflow (Pi-based)
- `HELIOS_Analysis_Workflow.md` — analysis pipeline that will move to Mac2020
- `HELIOS_Mac2017.md` — Mac2017 role (archival, InfluxDB/Grafana host)
- `HELIOS_Experiment_Switch.md` — experiment switching procedure
- `MEMORY.md` — SSH key, Mac2020 access details
