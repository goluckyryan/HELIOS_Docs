# HELIOS Terminal Server Reference

**Generated:** 2026-04-05  
[OK] **Verified 2026-04-05**  --  port map confirmed from `HELIOSterminals` script on DAQ + live port probing

---

## Device

- **Model:** Digi PortServer TS 16 MEI (16-port serial-to-network terminal server)
- **IP:** 192.168.1.3
- **Web UI:** http://192.168.1.3/ (requires login, Digi management interface)
- **Management telnet:** port 23 (`login:` prompt)

## Port Map (HELIOS Configuration)

Source: `/home/helios/digios/daq/edm/scripts/HELIOSterminals`

| TCP Port | Device | IP | Notes |
|----------|--------|----|-------|
| 2001 | TrigCPU |  --  | Trigger processor (NOT a VME IOC) |
| 2002 | VME1 | 192.168.1.20 | VxWorks 5.5, `->` prompt confirmed |
| 2003 | VME2 | 192.168.1.21 | VxWorks 5.5, `->` prompt confirmed |
| 2004 | VME3 | 192.168.1.22 | VxWorks 5.5, `->` prompt confirmed |
| 2005 | VME4 | 192.168.1.23 | VxWorks 5.5, `->` prompt confirmed |
| 2006 | VME5 | 192.168.1.24 | VxWorks 5.5, `->` prompt confirmed |
| 2007 | VME6 |  --  | Mapped but **powered off**  --  not in current HELIOS config |
| 2008-2015 |  --  |  --  | Closed / unused |
| 23 | Terminal Server mgmt |  --  | `login:` prompt (Terminal Server OS) |

## Usage

- Connect to a VME IOC console: `telnet 192.168.1.3 <port>` (e.g. port 2002 for VME1)
- The DAQ uses hostname alias `ts` for 192.168.1.3 in its scripts
- [!!] **Do not touch**  --  VxWorks consoles are live IOC shells. Read-only observation only.

## Scripts on DAQ

| Script | Path | Purpose |
|--------|------|---------|
| `HELIOSterminals` | `~/digios/daq/edm/scripts/HELIOSterminals` | HELIOS-specific terminal launcher (5 VMEs + TrigCPU) |
| `terminals` | `~/digios/daq/edm/scripts/terminals` | GRETINA-era generic script (up to 11 VMEs, TrigCPU on 2016) |

## Notes

- TS 16 MEI has 16 serial ports; HELIOS uses 7 (1 TrigCPU + 5 VME + 1 spare VME6 off)
- Port 2001 = TrigCPU  --  common mistake to assume it's VME1 (it's not)
- GRETINA-era `terminals` script exists on DAQ but maps ports differently  --  use `HELIOSterminals` for HELIOS

## See Also

- `HELIOS_DAQ_Workflow.md`  --  DAQ operations, run control, EPICS context
- `HELIOS_PV_Reference.md`  --  EPICS PV names for VME IOC channels
- `TOOLS.md` (workspace)  --  full subnet map, IP table, access methods
- `MEMORY.md` (workspace)  --  Terminal Server port map summary + [!!] do-not-touch rules
