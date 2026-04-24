# HELIOS InfluxDB Schema

**Host:** Mac2017 (192.168.1.193), port 8086, InfluxDB 1.x  
**Database:** `testing`  
**Access:** Read-only HTTP API from Spark. No writes, no deletes.

```bash
# Example query
curl -s "http://192.168.1.193:8086/query?db=testing&q=SELECT+last(value)+FROM+\"VacuumGauge\""
```

**[!!] READ-ONLY. Never write or delete.**

---

## Measurements

| Measurement | Tags | Description |
|---|---|---|
| `RunNum` | — | Current run number |
| `SavingData` | `expName`, `comment` | 1=saving, 0=stopped |
| `fileSize` | — | Current raw data file size (bytes) |
| `buffer` | `VME` | VME buffer occupancy |
| `hitRate` | `CH`, `DIG`, `VME` | Per-channel hit rate (Hz) |
| `sumHitX` | `VME` | Sum X trigger rate |
| `sumHitY` | `VME` | Sum Y trigger rate |
| `threshold` | `CH`, `DIG`, `VME` | Per-channel LED threshold |
| `reshold` | `CH`, `DIG`, `VME` | (alias/duplicate of threshold -- legacy) |
| `VacuumGauge` | `Det`, `G` | Vacuum pressure (mbar) |
| `HeLevel` | — | Liquid helium level (%) |
| `HeTemp` | — | Helium shield temperature |
| `HPGeTemp` | — | HPGe detector temperature |
| `HV` | `Det`, `Module` | High voltage readback (V) |
| `Gauge` | `Det`, `G` | Gauge readback |
| `Isotope` | `iso` | Beam isotope ID |
| `LC`, `LC00`, `LC03`, `LC12` | `Det`/`ch` | Leakage current |
| `LockCount` | `DIG`, `router` | Lock count (sync status) |
| `router1`, `router2` | — | Router sync status |

## Example Queries

```bash
# Latest vacuum
curl -s "http://192.168.1.193:8086/query?db=testing&q=SELECT+last(value)+FROM+\"VacuumGauge\""

# Latest He level
curl -s "http://192.168.1.193:8086/query?db=testing&q=SELECT+last(value)+FROM+\"HeLevel\""

# Current run number
curl -s "http://192.168.1.193:8086/query?db=testing&q=SELECT+last(value)+FROM+\"RunNum\""

# Hit rates for all channels (last value)
curl -s "http://192.168.1.193:8086/query?db=testing&q=SELECT+last(value)+FROM+\"hitRate\"+GROUP+BY+*"

# Vacuum history last 1 hour
curl -s "http://192.168.1.193:8086/query?db=testing&q=SELECT+mean(value)+FROM+\"VacuumGauge\"+WHERE+time+>+now()-1h+GROUP+BY+time(1m)"
```

## Notes

- DataBase.py (runs on DAQ) writes to this database every 30s during active runs
- Grafana on Mac2017 reads from here for dashboards
- He level / vacuum are written by Pi .208 scripts (independent of run state)
- Last data: 2026-04-22 (h096 end), vacuum still updating as of 2026-04-24

_Created: 2026-04-24 by HELIOS (schema explored via HTTP API from Spark)_
