# Heartbeat Log

Tracks which task was done each heartbeat, rotating A -> B -> C -> A.

**Archive:** Full verbose entries from 2026-04-05 archived in `heartbeat-log-archive-20260405.md`

## Log (compact  --  2026-04-05 onward)

| Timestamp (CDT) | Task | Notes |
|---|---|---|
| 2026-04-09 09:09 | C  --  Organize HELIOS_MD | INDEX.md updated: added expMemory_h096.md to Related Files section |
| 2026-04-05 11:08 | A  --  Explore Systems | All hosts up (DAQ 86d, Mac2020 48d, Mac2017, Pi .208, DigiBoard). DAQ: EDM + EPICS IOC running, load light, disk healthy. |
| 2026-04-05 11:55 | B  --  Self-Maintenance | Context healthy. Memory files reviewed. |
| 2026-04-05 12:10 | C  --  Organize HELIOS_MD | INDEX.md verified. `HELIOS_DigiBoard.md` created + verified (port map confirmed from HELIOSterminals + live probing). |
| 2026-04-05 12:40 | A  --  (skip, too soon) | No action. |
| 2026-04-05 12:55 | A  --  Explore Systems | Mac2020 digios HEAD `ff05fc0`. EDM screen updated (HELIOSMain_4sidesArray). |
| 2026-04-05 13:25 | B  --  Self-Maintenance | Reviewed TODOs. No completed items. |
| 2026-04-05 13:40 | C  --  (skip, too soon) | No action. |
| 2026-04-05 13:55 | A  --  Explore Systems | DigiBoard web UI confirmed accessible. |
| 2026-04-05 14:11 | C  --  Organize HELIOS_MD | Index cleanup pass. |
| 2026-04-05 14:26 | B  --  Self-Maintenance | Context 6%, healthy. |
| 2026-04-05 14:56 | A  --  Explore Systems | DigiBoard port map fully resolved. `HELIOS_DigiBoard.md` finalized. |
| 2026-04-05 15:11 | C  --  Organize HELIOS_MD | INDEX.md updated with DigiBoard entry. |
| 2026-04-05 15:41 | A  --  Explore Systems | Pi .208 probed  --  up, SSH denied (expected), read-only. |
| 2026-04-05 15:56 | B  --  Self-Maintenance | Archived stale session/daily files (Mar 26-Apr 1) to memory/archive/. Committed e468c70. |
| 2026-04-05 16:26 | C  --  Organize HELIOS_MD | INDEX.md + heartbeat-log in sync. Mac2017.md verified. |
| 2026-04-05 16:41 | C  --  Organize HELIOS_MD | Heartbeat-log moved from workspace to HELIOS_MD. Committed. |
| 2026-04-05 16:56 | A  --  Explore Systems | DAQ disk layout documented in daily memory. |
| 2026-04-05 18:11 | A  --  Explore Systems | DAQ: `/global` filesystem layout captured. |
| 2026-04-05 18:13 | B  --  Self-Maintenance | Daily memory file updated, committed 64632e5. |
| 2026-04-05 18:28 | A  --  Explore Systems | Evening check  --  all hosts stable. Mac2020 bare repo HEAD fixed (main->master). |
| 2026-04-05 18:43 | B  --  Self-Maintenance | Evening  --  systems stable, no TODOs completed. |
| 2026-04-05 20:13 | A  --  Explore Systems | DAQ: 87d uptime, vacuum readout running, stable. |
| 2026-04-05 20:28 | A  --  Explore Systems | All hosts up, DAQ load 0.43/0.28/0.25  --  normal. |
| 2026-04-06 06:43 | B  --  Self-Maintenance | Context 3% (fresh session). Workspace clean. TODOs unchanged. |
| 2026-04-06 06:58 | A  --  Explore Systems | DAQ 87d uptime. EDM + gretClust IOC + Edwards vacuum gauge running. Mac2020 up. Normal standby. |
| 2026-04-06 07:13 | B  --  Self-Maintenance | Context 3%. Archived 11 stale files. No conflicts in workspace .md files. Committed e468c70, pushed Mac2020. |
| 2026-04-06 07:28 | C  --  Organize HELIOS_MD | Heartbeat log trimmed/compacted. INDEX.md formatting fixed. |
| 2026-04-07 08:59 | A  --  Explore Systems | Morning check  --  DAQ 88d uptime, load 0.32, /global 27%. Mac2020 up. All stable. |
| 2026-04-07 09:58 | B  --  Self-Maintenance | Context 4%, healthy. Workspace clean. Created 2026-04-07.md daily log. No TODOs completed. |
| 2026-04-07 10:13 | C  --  Organize HELIOS_MD | INDEX.md: added heartbeat-log-archive entry. Heartbeat log table reformatted. |
| 2026-04-07 10:43 | A  --  Explore Systems | DAQ up (88d uptime, load 0.15), /global 27% (64G/256G). Mac2020 up. All nominal. |
| 2026-04-07 15:13 | A  --  Explore Systems | DAQ 88d uptime, load 0.09, /global 27%. Mac2020 up (50d), load 1.38, disk 75%. All nominal. |
| 2026-04-07 16:43 | B  --  Self-Maintenance | Context 3%, healthy. Memory files clean. Daily log current. No TODOs completed. |
| 2026-04-07 16:58 | C  --  Organize HELIOS_MD | INDEX.md verified complete (19 entries = all files). Formatting consistent. No stale/duplicate content. |
| 2026-04-07 17:13 | A  --  Explore Systems | DAQ 88d uptime, load 0.44, /global 27% (64G/256G). Mac2020 up (50d), load 1.36, disk 75%. All nominal. |
| 2026-04-07 17:43 | B  --  Self-Maintenance | Context 3%, healthy. No TODOs completed. Workspace clean. |
| 2026-04-07 18:28 | A  --  Explore Systems | DAQ 88d uptime, load 0.32, /global 27% (64G/256G). Mac2020 up (50d), load 0.97, disk 75%. All nominal. |
| 2026-04-07 20:13 | B  --  Self-Maintenance | Context 3%, healthy. Workspace clean. INDEX.md verified (19 entries). No TODOs completed. |
| 2026-04-07 20:43 | C  --  Organize HELIOS_MD | INDEX.md verified: 19 content entries + INDEX.md = 20 files total. All present and accounted for. |
| 2026-04-07 21:58 | C  --  Organize HELIOS_MD | Heartbeat log cleaned (stripped blank rows, fixed footer). INDEX.md verified (20 files, all correct). |

| 2026-04-08 00:13 | A  --  Explore Systems | DAQ 89d uptime, load 0.19, /global 27% (64G/256G). Mac2020 up (50d), load 1.02, disk 75%. All nominal. Quiet hours. |
| 2026-04-08 04:13 |  --  (quiet hours) | Skipped. |
| 2026-04-08 08:28 | B  --  Self-Maintenance | Context 3%, healthy. Daily log current. No TODOs completed. Workspace clean. |
| 2026-04-08 08:43 | C  --  Organize HELIOS_MD | INDEX.md verified: 19 entries + INDEX.md = 20 files. All present, consistent, no stale content. |

| 2026-04-08 09:13 | A  --  Explore Systems | DAQ 89d uptime, load 0.26, /global 27% (64G/256G). Mac2020 up (50d), load 0.85, disk 75%. All nominal. |

| 2026-04-08 09:43 | A  --  Explore Systems | All hosts up. DAQ: 89d 13h52m, load 0.38/0.40/0.35, 5 processes (EDM + gretClust + Edwards + pythonx2). Mac2020: 51d, load ~1.2. Pi: 26d 21h. Normal standby. |

| 2026-04-08 09:58 | A  --  Explore Systems | DAQ: 89d 14h, load 0.30, /global 27%. 5 procs: EDM + gretClust + Edwards (py2.7) + python. Mac2020: 51d, load 1.94, disk healthy. Normal standby. |
| 2026-04-08 10:13 | B  --  Self-Maintenance | Context 5% (healthy). Workspace clean. memory/ tidy (05-08). No stray PNGs. All good. |
| 2026-04-08 10:28 | B  --  Self-Maintenance | Context 5% (healthy). Workspace clean. memory/ tidy. All nominal. |
| 2026-04-08 10:43 | C  --  Organize HELIOS_MD | Audited README.md vs actual file list  --  all 16 content files linked correctly. Verified InfluxDB host (Mac2017/.193), DigiBoard portmap, GLBL:DIG warning all current. No stale content found. |

| 2026-04-08 11:43 | A  --  Explore Systems | All hosts up. DAQ: 89d 15h52m, load 0.25/0.19/0.21, 6 procs (EDM + gretClust + Edwards py2.7 + printer applet + 2xxterm). Mac2020: 51d 2h, load 1.20. Pi: 26d 23h. Normal standby. |

| 2026-04-08 13:43 | C  --  Organize HELIOS_MD | Cleaned stale Next Steps in expMemory_h095.md  --  marked time-cal + Gate B FOM steps complete (done 2026-04-03). Committed a163674. |

| 2026-04-08 13:58 | A  --  Explore Systems | All hosts up. DAQ: 89d 18h7m, load 0.32/0.29/0.25, 5 procs (EDM + gretClust + Edwards + pythonx2). Mac2020: 51d 4h34m, load ~1.0. Pi: 27d 1h14m. Normal standby. |


| 2026-04-08 12:13 | B  --  Self-Maintenance | Context 5% (healthy). Workspace clean. No stray PNGs. memory/ tidy. All nominal. |
| 2026-04-08 12:28 | C  --  Organize HELIOS_MD | Created plot_index.md for h095 (Plot-001-027 retroactively indexed, next=028) and h094_cuts (empty, next=001, pre-convention files noted). |

| 2026-04-08 12:58 | A  --  Explore Systems | All hosts up. DAQ: 89d 17h7m, load 0.41/0.31/0.25, 5 procs (EDM + gretClust + Edwards + pythonx2). Mac2020: 51d 3h34m, load ~1.04. Pi: 27d 14m. Normal standby. |
| 2026-04-08 13:28 | B  --  Self-Maintenance | Context 5% (healthy). Workspace clean. memory/ tidy. All nominal. |
| 2026-04-08 13:58 | A  --  Explore Systems | All hosts up. DAQ: 89d 18h7m, load 0.32/0.29/0.25, 5 procs (EDM + gretClust + Edwards + pythonx2). Mac2020: 51d 4h34m, load ~1.0. Pi: 27d 1h14m. Normal standby. |

| 2026-04-08 14:13 | C  --  Organize HELIOS_MD | Audited calibration_notes.md (timing section complete, dE/E behavior documented), HELIOS_DAQ_Workflow.md (tcpReceiver + Quick DAQ check in place), expMemory_h095.md (coinTimeUC correction still pending Ryan). All HELIOS_MD files healthy, no stale content. |

| 2026-04-08 16:58 | C  --  Organize HELIOS_MD | Updated HELIOS_Mac2017.md: macOS 13.0 (Ventura), 51d uptime, disk 83%, InfluxDB+Grafana running. Added [OK] Verified stamp. Committed 34ad4a5. |

| 2026-04-08 17:13 | A  --  Explore Systems | All hosts up. DAQ: 89d 21h, load 0.10/0.20/0.27, 5 processes (EDM + gretClust + Edwards + pythonx2). Mac2020: 51d 7h, load ~1.0, disk 75%. Pi: 27d 4h, load 0.00. Normal standby. |
| 2026-04-08 17:28 | B  --  Self-Maintenance | Context 5% (healthy). Workspace clean. No stray PNGs. All nominal. |

| 2026-04-08 17:43 | C  --  Organize HELIOS_MD | Clarified RDT dE/E timing note in calibration_notes.md  --  changed "Maybe General" to confirmed structural truth (applies all experiments). Committed 68c992e. |

| 2026-04-08 17:58 | A  --  Explore Systems | All hosts up. DAQ: 89d 22h, load 0.16/0.34/0.32, 5 processes (EDM + gretClust + Edwards + pythonx2). Mac2020: 51d 8h, load ~0.9. Normal standby. |

| 2026-04-08 18:13 | B  --  Self-Maintenance | Context 5% (healthy). Workspace clean, no stray PNGs. memory/ tidy (05-08, archive). No TODOs. All nominal. |

| 2026-04-08 18:28 | C  --  Organize HELIOS_MD | Added SKIP reason note to h095 exShift table in calibration_notes.md (Det07=h095 issue, Det11=always dead/hardware, Det17/22=no convergence). Committed 347cc99. |

| 2026-04-08 18:43 | A  --  Explore Systems | All hosts up. DAQ: 89d 22h52m, load 0.11/0.17/0.21, 5 processes (EDM + gretClust + Edwards + pythonx2). Mac2020: 51d 9h, load ~1.1. Normal standby. |
| 2026-04-08 18:58 | B  --  Self-Maintenance | Context 5% (healthy). Workspace clean. memory/ tidy (05-08, archive). No stray PNGs. All nominal. |

| 2026-04-08 19:13 | C  --  Organize HELIOS_MD | Fixed stale link in README.md: `HELIOS_TerminalServer.md` -> `HELIOS_DigiBoard.md` (file was renamed months ago, README never updated). Committed de0a212. |

| 2026-04-08 19:43 | A  --  Explore Systems | All hosts up. DAQ: 89d 23h52m (near 90d!), load 0.05/0.19/0.27 (very light). EDM + gretClust + Edwards + pythonx2 running. Mac2020: 51d 10h, load 1.37. Normal standby. |

| 2026-04-08 20:21 | B  --  Self-Maintenance | Context 5% (healthy). Workspace clean, 0 stray PNGs. memory/ tidy (05-08, archive). Magnet at 2.85 T. No new TODOs. All nominal. |


| 2026-04-08 20:36 | C  --  Organize HELIOS_MD | Updated active experiment to h096 in DAQ_Workflow, Analysis_Workflow, Detector_Geometry (magnet ramped 2026-04-08, B=2.85 T). Added h096 section to Detector_Geometry. Committed e70ddf3. |

| 2026-04-08 20:51 | A  --  Explore Systems | DAQ: 90d 1h, load 0.26/0.25/0.26, 5 processes (EDM + gretClust + pythonx2 + xterm). Mac2020: 51d 11h, load ~0.9. Normal standby. |

| 2026-04-09 07:24 | B  --  Self-Maintenance | Context 3% (healthy). Workspace clean, 0 stray PNGs. memory/ tidy (05-09). No new TODOs. All nominal. |

## Next Task: C  --  Organize HELIOS_MD
| 2026-04-09 07:40 | C  --  Organize HELIOS_MD | Added expMemory_h096.md references to HELIOS_Analysis_Workflow.md and HELIOS_Detector_Geometry.md (both previously only listed h094/h095). Committed b3bc9e8. |
| 2026-04-09 08:24 | C  --  Organize HELIOS_MD | Fixed stale README link (DigiBoard->TerminalServer  --  original fix in de0a212 was to INDEX.md not README). Committed uncommitted updates: new_experiment_checklist.md (full restructure), start_stop_sequence.md (new file, now tracked), INDEX.md (start_stop entry). Committed c5348cf. |

| 2026-04-09 09:39 | C -- Organize | INDEX.md verified (21 files). Context 3%. |
| 2026-04-09 10:24 | C -- Organize | INDEX.md verified. voice-terminal-plan.md in index. |
| 2026-04-09 10:54 | C -- Organize | INDEX.md verified (21 files). h096 content current. |
| 2026-04-09 11:24 | A -- Explore | Mac2020 up 52d, load 1.15, disk healthy. digios normal. |
| 2026-04-09 11:54 | C -- Organize | INDEX.md verified. heartbeat-log healthy. |
| 2026-04-09 13:39 | A -- Explore | Mac2020 up 52d, load 0.75. All nominal. |
| 2026-04-09 14:09 | C -- Organize | INDEX.md verified (20 files). voice-terminal-plan in index. |
| 2026-04-09 16:09 | A -- Explore | Mac2020 up 52d, load 2.08. digios HEAD 6aa2ac9. h096 likely in progress. |
| 2026-04-09 16:43 | C -- Organize | 22 files, all indexed. No stale content. |
| 2026-04-09 17:29 | C -- Organize | 22 files indexed. heartbeat-log 175 lines. All consistent. |
## 2026-04-10 Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 04:10 | A -- Explore | DAQ up 91d 8h, load 0.45, /global 27%. Mac2020 up 52d 18h, load 1.42. All nominal (quiet hours). |
| 04:25 | B -- Maintenance | Context 3%. Moved 2 stray PNGs (h096 Plot-001/002) to ~/screenshots/. memory/ tidy. |
| 04:40 | B -- Maintenance | Context 3%. Workspace clean, 0 stray PNGs. memory/ tidy. |
| 04:55 | B -- Maintenance | Context 3%. Removed stale `memory/heartbeat-log.md` (26KB duplicate). 436 screenshots. |
| 05:10 | C -- Organize | INDEX.md verified (21 entries). expMemory_h096.md added to INDEX.md Related Files. |
| 05:25 | B -- Maintenance | Context 3%. Workspace clean. MEMORY/TOOLS/AGENTS.md previously trimmed by Ryan. |
| 05:40 | B -- Maintenance | Context 4%. No conflicts or stale directives. |
| 05:55 | B -- Maintenance | Context 3%. 438 screenshots (expected). daily 2026-04-10.md current (Cleopatra/HELIOS_LIB.h work). |
| 06:10 | B -- Maintenance | Context 3%. Token trim confirmed (AGENTS/TOOLS/MEMORY slimmed, IDENTITY.md deleted). |
| 06:25 | B -- Maintenance | Context 3%. Workspace clean, memory/ tidy. |
| 06:40 | B -- Maintenance | Context 3%. Daily log current (Cleopatra + HELIOS_LIB.h work). |
| 06:55 | B -- Maintenance | Context 3%. memory-trim session captured in 2026-04-10-memory-trim.md. |
| 07:10 | B -- Maintenance | Context 4% (35k). Workspace clean, memory/ tidy. |
| 07:35 | C -- Organize | 22 files / 21 indexed [OK]. Cleopatra.md current. Cal_Procedure vs Cal_Workflow distinct [OK]. |
| 08:03 | A -- Explore | DAQ up 91d 12h, load 0.77, /global 27%. Mac2020 up 52d 22h, load 1.12. All nominal. |
| 08:37 | B -- Maintenance | Context 4% (38k). memory/ tidy, 0 stray PNGs. |
| 08:52 | C -- Organize | 22/21 files [OK]. new_experiment_checklist + start_stop_sequence headers clean. |
| 09:20 | A -- Explore | DAQ up 91d 13h, load 0.67, /global 27%. Mac2020 up 52d 23h, load 1.13. All nominal. |
| 09:35 | B -- Maintenance | Context 4% (41k). All nominal. |
| 09:50 | C -- Organize | **Fixed stale ref in MEMORY.md**: HELIOS_AI_RunControl.md -> start_stop_sequence.md. |
| 10:05 | A -- Explore | DAQ up 91d 14h, load 0.63. Mac2020 load **2.85/3.05/3.06 (elevated)** -- 4 users active. |
| 10:20 | B -- Maintenance | Context 4% (44k). All nominal. |
| 10:35 | C -- Organize | AI_RunControl stale ref confirmed gone. rdtCut_guideline.md spot-checked [OK]. |
| 10:50 | A -- Explore | DAQ up 91d 14h59m, load 0.27. Mac2020 load 0.93 -- back to normal [OK]. |
| 11:05 | B -- Maintenance | Context 5% (46k). All nominal. |
| 11:20 | C -- Organize | HELIOS_PV_Reference.md HV section spot-checked [OK]. heartbeat-log at 360 lines. |
| 11:35 | A -- Explore | DAQ up 91d 15h44m, load 0.40. Mac2020 up 53d 2h10m, load 1.33. All nominal. |
| 11:50 | B -- Maintenance | Context 5% (49k). All nominal. |
| 12:05 | C -- Organize | HELIOS_DAQ_Startup + DAQ_Workflow: h096 refs current, B=2.85T [OK]. |
| 12:20 | A -- Explore | DAQ up 91d 16h29m, load 0.38. Mac2020 up 53d 2h55m, load 0.69. All nominal. |
| 12:35 | B -- Maintenance | Context 5% (51k). All nominal. |
| 12:50 | C -- Organize | Compacted 2026-04-10 verbose entries into summary table. heartbeat-log trimmed. |

| 13:05 | A -- Explore | DAQ up 91d 17h14m, load 0.28/0.42/0.40, /global 27%. Mac2020 up 53d 3h40m, load 1.32. All nominal. |
| 13:20 | B -- Maintenance | Context 6% (59k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |

## 2026-04-10 Afternoon -- Run Control Fixes

### start_run.sh (DAQ) -- cd to data dir
- Bug: gtReceiver4 xterms launched from /home/helios/, writing gtd files there
- Fix: added `cd ${daqDataPath}/${expName}` before xterm block
- Backup: start_run.sh.bak_20260410

### elog ID capture -- full fix
- Root cause: CloudFlare patch switched to libcurl with FOLLOWLOCATION; removed raw HTTP response parsing; 302 Location header never captured
- Fix: added header_cb + CURLOPT_HEADERFUNCTION in submit_elog() to capture Location: header; parse ID as digits after last '/'
- Rebuilt on Pi: ~/elog_build/src/elog.cxx -> ~/bin/elog (146KB)
- Rebuilt on Mac2020: ~/elog_CloudFlare/elog/src/elog.cxx -> ~/elog_CloudFlare/BUILD/elog (75KB)
  - Mac2020 needs SDK path: -L$(xcrun --show-sdk-path)/usr/lib
- push2Elog.sh: updated to use full path /Users/heliosdigios/elog_CloudFlare/BUILD/elog; fixed awk parse from broken double-quote to single-quote '{print $2}'
- Backup: push2Elog.sh.bak_20260410
- Tested end-to-end: ID correctly returned and written to elogID.txt [OK]

### Run-002 (alpha source calibration)
- gtd files saved to wrong dir (/home/helios/) -- moved to /media/DIGIOSDATA6/h096_31Si_dp/ after stop
- Run stopped after ~7 min
| 14:27 | C -- Organize | HELIOS_TerminalServer.md refs consistent across README+INDEX [OK]. expMemory_h096.md healthy (200 lines, h096 current) [OK]. No issues. |
| 14:42 | A -- Explore | DAQ up 91d 18h50m, load 0.52, /global 27% -- **11 users** (up from 5, likely experiment activity). Mac2020 up 53d 5h17m, load 2.10 (elevated). All functional. |
| 14:58 | B -- Maintenance | Context 6% (62k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:10 | A -- Explore | DAQ up 91d 20h19m, load 0.84, 10 users -- **gtReceiver4 running (4 procs), data taking active**. Mac2020 up 53d 6h45m, load 1.38. h096 experiment live. |
| 16:25 | B -- Maintenance | Context 6% (65k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:40 | C -- Organize | start_stop_sequence.md: updated backup note (bak_20260410), added 2026-04-10 fixes section (gtd cd fix, elog CloudFlare/libcurl fix, push2Elog.sh fix). |
| 16:55 | A -- Explore | DAQ up 91d 21h4m, load 1.26/1.06/1.00, 10 users -- gtReceiver4 still running (experiment ongoing). Mac2020 up 53d 7h30m, load 1.22. All healthy. |
| 17:10 | B -- Maintenance | Context 7% (69k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 17:25 | C -- Organize | 22 files / INDEX.md consistent [OK]. HELIOS_Analysis_Workflow.md: h096 active experiment noted correctly [OK]. No issues. |
| 17:47 | A -- Explore | DAQ up 91d 21h56m, load 0.75, 10 users -- gtReceiver4 running (experiment ongoing). Mac2020 up 53d 8h22m, load 0.94. All healthy. |
| 18:02 | B -- Maintenance | Context 7% (71k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 18:18 | C -- Organize | start_stop_sequence.md: 2026-04-10 fixes confirmed documented [OK]. expMemory_h096.md: Run-002 gtd issue not needed there (covered in start_stop_sequence.md). No stale content. |
| 18:52 | A -- Explore | DAQ up 91d 23h, load 1.07, 10 users -- gtReceiver4 running (experiment ongoing into evening). Mac2020 up 53d 9h27m, load 1.19. All healthy. |
| 19:07 | B -- Maintenance | Context 7% (74k). Created 2026-04-11.md daily log (new UTC day). 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 19:22 | C -- Organize | HELIOS_Detector_Geometry.md: h096 section current (B=2.85T, ramped 2026-04-08) [OK]. 258 lines in heartbeat-log -- healthy. No issues. |
| 20:37 | A -- Explore | DAQ up **92d** 45m, load 0.96, 10 users -- gtReceiver4 running (~4h+ experiment). Mac2020 up 53d 11h12m, load 1.71. All healthy. |
| 20:59 | B -- Maintenance | Context 8% (76k) -- healthy, trending up through the day. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 21:30 | C -- Organize | expMemory_h096.md: no per-run log needed (expected) [OK]. calibration_notes.md: general across experiments, h096-specific state in expMemory_h096.md [OK]. No issues. |
| 21:45 | A -- Explore | DAQ up 92d 1h53m, load 0.97, 10 users -- gtReceiver4 running (~5h+ experiment). Mac2020 up 53d 12h20m, load 0.82. All healthy. |
| 22:00 | B -- Maintenance | Context 8% (80k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 22:31 | C -- Organize | heartbeat-log 264 lines, 22 files [OK]. new_experiment_checklist.md: working_Helios workflow current for h096+ [OK]. No issues. |
| 22:46 | A -- Explore | DAQ up 92d 2h55m, load 0.22 (light), 10 users -- **gtReceiver4 gone, xterms reduced** -- experiment likely stopped. Mac2020 up 53d 13h21m, load 1.14. All healthy. |
| 23:01 | B -- Maintenance | Context 8% (82k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 23:16 | C -- Organize | HELIOS_Experiment_Switch.md: spot-checked -- general procedure, no h096-specific updates needed [OK]. INDEX.md entry accurate [OK]. No issues. |
| 23:31 | A -- Explore | DAQ up 92d 3h40m, load 0.51, 10 users -- standby (no gtReceiver4). Mac2020 up 53d 14h6m, load 1.06. All nominal, late night. |
| 23:46 | B -- Maintenance | Context 8% (85k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |

## 2026-04-11 Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 00:01 | C -- Organize | 270 lines in log -- compact table format, no compaction needed. New day header added. No stale content found. |
| 00:16 | A -- Explore | DAQ up 92d 4h25m, load 0.26, /global 27% -- standby. Mac2020 up 53d 14h51m, load 1.13. All nominal (quiet overnight). |
| 00:31 | B -- Maintenance | Context 9% (87k) -- healthy, slow climb through day. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:46 | C -- Organize | voice-bridge-plan + voice-terminal-plan: both "Planning/Not started" -- consistent with TODO.md [OK]. INDEX entries accurate. No issues. |
| 01:01 | A -- Explore | DAQ up 92d 5h10m, load 0.47, /global 27% -- standby. Mac2020 up 53d 15h36m, load 2.52 (elevated at 1AM -- likely overnight analysis/processing). All functional. |
| 01:16 | B -- Maintenance | Context 9% (89k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:31 | C -- Organize | HELIOS_Migration_Mac2020.md: "planned but not scheduled" -- consistent with TODO.md [OK]. INDEX entry accurate. No issues. |
| 01:46 | A -- Explore | DAQ up 92d 5h55m, load 0.31, /global 27% -- standby. Mac2020 up 53d 16h21m, load 2.91 (sustained elevated -- overnight processing). All functional. |
| 02:01 | B -- Maintenance | Context 9% (91k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 02:16 | C -- Organize | rdtCut_guideline.md: fully experiment-agnostic, no updates needed [OK]. INDEX entry accurate. No issues. |
| 02:31 | A -- Explore | DAQ up 92d 6h40m, load 0.27, /global 27% -- standby. Mac2020 up 53d 17h6m, load 0.75 -- back to normal (overnight processing done). All nominal. |
| 02:46 | B -- Maintenance | Context 9% (93k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 03:01 | C -- Organize | 287 lines, 22 files [OK]. HELIOS_Mac2017.md: last verified 2026-04-08 -- still current for stable system. No issues. |
| 03:16 | A -- Explore | DAQ up 92d 7h25m, load 0.56, /global 27% -- standby. Mac2020 up 53d 17h51m, load 1.20. All nominal (quiet early morning). |
| 03:31 | B -- Maintenance | Context 10% (96k) -- healthy, gradual climb (session running ~23h). 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 03:46 | C -- Organize | Calibration docs (Procedure/Workflow/notes): all distinct, cross-refs correct, INDEX accurate [OK]. No issues. |
| 04:01 | A -- Explore | DAQ up 92d 8h10m, load 0.42, /global 27% -- standby. Mac2020 up 53d 18h36m, load 1.07. All nominal. |
| 04:16 | B -- Maintenance | Context 10% (98k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 04:31 | C -- Organize | HELIOS_DAQ_Startup.md: h096 refs present, no stale content [OK]. INDEX entry accurate. No issues. |
| 04:46 | A -- Explore | DAQ up 92d 8h55m, load 0.49, /global 27% -- standby. Mac2020 up 53d 19h21m, load 0.93. All nominal. |
| 05:01 | B -- Maintenance | Context 10% (100k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:16 | C -- Organize | 296 lines, 22 files [OK]. All compact table format. No stale content. Context at 50% -- flagging Ryan. |
| 05:32 | A -- Explore | DAQ up 92d 9h40m, load 0.72, /global 27% -- standby. Mac2020 up 53d 20h7m, load 1.08. All nominal. |
| 05:47 | B -- Maintenance | Context 10% (102k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 06:02 | C -- Organize | README.md: overview doc, no experiment-specific content needed [OK]. All INDEX entries accurate. No issues. |
| 06:17 | A -- Explore | DAQ up 92d 10h26m, load 0.65, /global 27% -- standby. Mac2020 up 53d 20h53m, load 1.35. All nominal. |
| 06:32 | B -- Maintenance | Context 10% (104k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 06:59 | C -- Organize | HELIOS_PV_Reference.md: GLBL:DIG [!!] warning present, no h096-specific changes needed [OK]. INDEX entry accurate. No issues. |
| 07:39 | A -- Explore | DAQ up 92d 11h48m, load 0.37, /global 27% -- standby. Mac2020 up 53d 22h14m, load 1.15. All nominal. |
| 07:54 | B -- Maintenance | Context 11% (107k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 08:43 | C -- Organize | HELIOS_Simulation_Cleopatra.md: marked DWBA_compare.C as dead weight (not in makefile, superseded -- per TODO.md 2026-04-10 review). 305 lines in log, compact format [OK]. |
| 08:58 | A -- Explore | DAQ up 92d 13h7m, load 0.60, /global 27% -- standby. Mac2020 up 53d 23h33m, load 0.73. All nominal. |
| 09:13 | B -- Maintenance | Context 11% (110k). Healthy. Daily report posted to #the-axiom (Apr 10 9AM - Apr 11 9AM). 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 09:28 | C -- Organize | **File consolidation detected**: Ryan merged calibration_notes.md + HELIOS_Calibration_Procedure.md + HELIOS_Calibration_Workflow.md + start_stop_sequence.md into HELIOS_Calibration.md (427 lines). 19 files now (was 22). INDEX.md cleaned (blank rows, file count). MEMORY.md already consistent. All refs correct. |
| 09:43 | A -- Explore | DAQ up 92d 13h52m, load 0.62, /global 27% -- standby. Mac2020 up 54d 18m, load 0.97. All nominal. |
| 09:58 | B -- Maintenance | Context 12% (117k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:13 | C -- Organize | Verified consolidation complete: HELIOS_Calibration.md has cal content, HELIOS_DAQ_Workflow.md has start/stop AI content. No stale cross-refs in remaining docs [OK]. |
| 10:28 | A -- Explore | DAQ up 92d 14h37m, load 0.61, /global 27% -- standby. Mac2020 up 54d 1h3m, load 1.26. All nominal. |
| 10:43 | B -- Maintenance | Context 12% (120k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:58 | C -- Organize | Full file audit: all 18 files (excl. INDEX.md) present and indexed [OK]. No missing or stale entries. |
| 11:13 | A -- Explore | DAQ up 92d 15h22m, load 0.45, /global 27% -- standby. Mac2020 up 54d 1h48m, load 1.25. All nominal. |
| 11:28 | B -- Maintenance | Context 12% (122k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 11:43 | C -- Organize | INDEX.md: removed stale skill refs (helios-start-run, helios-stop-run don't exist). DAQ Workflow entry cleaned. No other issues. |
| 11:58 | A -- Explore | DAQ up 92d 16h7m, load 0.54, /global 27% -- standby. Mac2020 up 54d 2h33m, load 0.96. All nominal. |
| 12:13 | B -- Maintenance | Context 12% (124k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:28 | C -- Organize | HELIOS_Analysis_Workflow.md: no stale refs to consolidated files [OK]. 320 lines in log, compact format. No issues. |
| 12:43 | A -- Explore | DAQ up 92d 16h52m, load 0.73, /global 27% -- standby. Mac2020 up 54d 3h18m, load 1.63. All nominal. |
| 12:58 | B -- Maintenance | Context 13% (126k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:13 | C -- Organize | Checked DAQ_Startup, Detector_Geometry, new_experiment_checklist for stale refs to consolidated files -- all clean [OK]. No issues. |

## 2026-04-11 Session (05:00 - 13:24 CDT) -- Major Restructuring
- HELIOS_MD: consolidated calibration (3->1 file), DAQ workflow (2->1 file), slimmed DAQ startup
- DAQ edm/scripts: cleaned 11 obsolete + 12 backups, 24 active scripts
- Start/stop redesign: DAQ=executor, Mac2020=elog, Pi=status. New scripts on Mac2020+Pi
- GeneralSortMapping.h: added HVdetMap/HVrdtMap (single source of truth)
- Skills updated: start-run, stop-run, status, autorun, hv. New: shutdown
- Monitor moved to helios-status folder
- gen_run_status.py: threaded, 1.5s, generates full status JSON
- HV check added to start_run.sh (snmpget outputSwitch)
| 13:33 | A -- Explore | DAQ up 92d 17h42m, load 0.57, /global 27% -- standby. Mac2020 up 54d 4h8m, load 1.19. All nominal. |
| 13:42 | B -- Maintenance | Context 5% (53k). Healthy. Model: opus-4-6 (non-default). 0 stray PNGs. Active conversation with Ryan -- autotune script + skill updates in progress. |
| 13:55 | C -- Organize | INDEX.md: all 19 files accounted for, no stale entries after consolidation. Active conversation with Ryan -- dry-run of start_run chain complete. |
| 14:10 | B -- Maintenance | Context 13% (128k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 14:25 | C -- Organize | Full grep for stale consolidated-file refs across all HELIOS_MD docs -- clean [OK]. Only provenance notes in Calibration.md + DAQ_Workflow.md (expected). No issues. |
| 14:43 | A -- Explore | DAQ up 92d 18h51m, load 0.17, /global 27%. Mac2020 up 54d 5h18m, load 4.75 (high -- screenshot test activity). Fixed Mac2020->Mac2017 SSH (PubkeyAcceptedAlgorithms +ssh-rsa). |
| 14:58 | A -- Explore | DAQ up 92d 19h6m, load 0.32, /global 27% -- standby. Mac2020 up 54d 5h33m, load 3.07 (elevated -- likely active analysis). All functional. |
| 15:14 | B -- Maintenance | Context 13% (130k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 15:34 | C -- Organize | INDEX.md file count verified: 19 content files + INDEX.md = 20 total [OK]. Count in header correct. No issues. |
| 15:51 | B -- Maintenance | Context 22% (219k). Healthy. Monitor test running (PID 563352) -- checking duplicate log fix. Active conversation with Ryan -- many script fixes today. |
| 15:58 | C -- Organize | Monitor test running (PID 563588, 28s). Waiting for first cycle to detect Stop. No INDEX changes needed. |
| 16:13 | A -- Explore | DAQ up 92d 20h22m, load 0.41, /global 27% -- standby. Mac2020 up 54d 6h49m, load 0.65 (back to normal). All nominal. |
| 16:28 | B -- Maintenance | Context 13% (132k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:44 | C -- Organize | README.md: accurate entry point, no updates needed [OK]. 347 lines in log. All files verified. No issues. |
| 16:59 | A -- Explore | DAQ up 92d 21h8m, load 0.78, /global 27% -- standby. Mac2020 up 54d 7h34m, load 1.34. All nominal. |
| 17:14 | B -- Maintenance | Context 13% (135k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 17:29 | C -- Organize | HELIOS_Detector_Geometry.md: h096 section current [OK]. No issues. |
| 17:44 | A -- Explore | DAQ up 92d 21h53m, load 0.24, /global 27% -- standby. Mac2020 up 54d 8h19m, load 0.87. All nominal. |
| 18:00 | B -- Maintenance | Context 14% (136k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 18:15 | C -- Organize | Log audit: 353 lines, two-part Apr-11 structure (compact table + major-restructuring summary + continuing table) -- all consistent [OK]. No issues. |
| 18:31 | A -- Explore | DAQ up 92d 22h39m, load 0.55, /global 27% -- standby. Mac2020 up 54d 9h6m, load 0.96. All nominal. |
| 18:47 | B -- Maintenance | Context 14% (142k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |

## 2026-04-12 Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 19:02 | C -- Organize | New UTC day. Created 2026-04-12.md daily log. All HELIOS_MD files verified clean (full audit done today). No new issues. |
| 19:17 | A -- Explore | DAQ up 92d 23h25m (approaching 93d), load 0.83, /global 27% -- standby. Mac2020 up 54d 9h52m, load 1.54. All nominal. |
| 19:32 | B -- Maintenance | Context 14% (145k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 19:51 | C -- Organize | HELIOS_Detector_Geometry.md: GeneralSortMapping.h noted as source of truth [OK]. HVdetMap/HVrdtMap additions are in the source file itself, not needed in this doc. No issues. |
| 20:07 | A -- Explore | DAQ up **93d** 15m, load 0.42, /global 27% -- standby. Mac2020 up 54d 10h42m, load 1.24. All nominal. |
| 20:21 | B -- Maintenance | Context 15% (147k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 20:36 | C -- Organize | Final stale-ref sweep: no consolidated-file or removed-skill refs anywhere in HELIOS_MD (excl. provenance notes) [OK]. All clean. |
| 20:52 | A -- Explore | DAQ up 93d 1h, load 0.68, /global 27% -- standby. Mac2020 up 54d 11h27m, load 1.10. All nominal. |
| 21:06 | B -- Maintenance | Context 15% (149k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 21:21 | C -- Organize | HELIOS_Mac2017.md: last verified 2026-04-08, stable archival system -- still current [OK]. No issues. |
| 21:37 | A -- Explore | DAQ up 93d 1h45m, load 0.39, /global 27% -- standby. Mac2020 up 54d 12h12m, load 1.14. All nominal. |
| 21:51 | B -- Maintenance | Context 15% (151k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 22:06 | C -- Organize | 373 lines in log, Apr-11 evening entries already compact [OK]. new_experiment_checklist.md: working_Helios symlink steps current [OK]. No issues. |
| 22:22 | A -- Explore | DAQ up 93d 2h30m, load 0.75, /global 27% -- standby. Mac2020 up 54d 12h57m, load 0.81. All nominal (late evening). |
| 22:36 | B -- Maintenance | Context 15% (153k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 22:51 | C -- Organize | HELIOS_Experiment_Switch.md: no stale refs, INDEX accurate [OK]. No issues. |
| 23:07 | A -- Explore | DAQ up 93d 3h15m, load 0.68, /global 27% -- standby. Mac2020 up 54d 13h42m, load 0.67. All nominal (late night). |
| 23:21 | B -- Maintenance | Context 15% (155k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 23:36 | C -- Organize | voice-bridge-plan.md + voice-terminal-plan.md: unstarted, consistent with TODO.md [OK]. No issues. |
| 23:52 | A -- Explore | DAQ up 93d 4h, load 0.63, /global 27% -- standby. Mac2020 up 54d 14h27m, load 1.03. All nominal (late night). |
| 00:06 | B -- Maintenance | Context 16% (157k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:21 | C -- Organize | 382 lines, Apr-12 section present [OK]. HELIOS_Migration_Mac2020.md: "not started, not scheduled" -- matches TODO.md [OK]. No issues. |
| 00:37 | A -- Explore | DAQ up 93d 4h45m, load 0.35, /global 27% -- standby. Mac2020 up 54d 15h12m, load 1.35. All nominal (overnight). |
| 00:51 | B -- Maintenance | Context 16% (159k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:06 | C -- Organize | HELIOS_Simulation_Cleopatra.md: dead-weight note for DWBA_compare.C confirmed present [OK]. INDEX accurate. No issues. |
| 01:22 | A -- Explore | DAQ up 93d 5h30m, load 0.70, /global 27% -- standby. Mac2020 up 54d 15h57m, load 1.19. All nominal. |
| 01:36 | B -- Maintenance | Context 16% (161k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:51 | C -- Organize | HELIOS_TerminalServer.md: verified 2026-04-05 -- static hardware, still valid [OK]. No issues. |
| 02:07 | A -- Explore | DAQ up 93d 6h15m, load 0.27, /global 27% -- standby. Mac2020 up 54d 16h42m, load 1.16. All nominal. |
| 02:21 | B -- Maintenance | Context 16% (163k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 02:36 | C -- Organize | HELIOS_Calibration.md: MANDATORY ORDER [!!] prominent at top [OK]. 391 lines in log, all compact. No issues. |
| 02:52 | A -- Explore | DAQ up 93d 7h, load 0.54, /global 27% -- standby. Mac2020 up 54d 17h27m, load 0.86. All nominal. |
| 03:36 | B -- Maintenance | Context **49%** (495k/1.0m) -- near 50% threshold. Session ~47h old. Notes saved to 2026-04-12.md. Flagging Ryan to /new. |
| 03:51 | C -- Organize | 20 files on disk (19 content + INDEX.md) [OK]. Context reset to 17% after compaction. All HELIOS_MD files verified clean. No issues. |
| 04:07 | A -- Explore | DAQ up 93d 8h15m, load 0.57, /global 27% -- standby. Mac2020 up 54d 18h42m, load 0.83. All nominal (quiet early morning). |
| 04:21 | B -- Maintenance | Context 17% (168k). Healthy after compaction. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 04:36 | C -- Organize | Full stale-ref sweep: clean [OK]. No consolidated-file refs outside of provenance notes. No issues. |
| 04:52 | A -- Explore | DAQ up 93d 9h, load 0.38, /global 27% -- standby. Mac2020 up 54d 19h27m, load 1.44. All nominal. |
| 05:06 | B -- Maintenance | Context 17% (170k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:21 | C -- Organize | Log at 400 lines (milestone). 20 files on disk [OK]. All verified clean. No issues. |
| 05:37 | A -- Explore | DAQ up 93d 9h45m, load 0.47, /global 27% -- standby. Mac2020 up 54d 20h12m, load 2.61/3.11 (elevated at 5:30AM -- likely automated processes). All functional. |
| 05:52 | B -- Maintenance | Context 17% (171k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 06:07 | C -- Organize | HELIOS_DAQ_Workflow.md: elog example uses H096_31Si_dp (correct for current experiment). expName.sh sourced live [OK]. No stale content. |
| 08:10 | A -- Explore | DAQ up 93d 12h19m, load 0.56, /global 27% -- standby. Mac2020 up 54d 22h45m, load 1.35. All nominal. |
| 08:25 | B -- Maintenance | Context 17% (174k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 08:40 | C -- Organize | Full index audit: all 19 content files indexed [OK]. No missing entries. No issues. |
| 08:55 | A -- Explore | DAQ up 93d 13h4m, load 0.58, /global 27% -- standby. Mac2020 up 54d 23h30m, load 1.28. All nominal. |
| 09:10 | B -- Maintenance | Context 18% (176k). Healthy. Daily report posted to #the-axiom (Apr 11 9AM - Apr 12 9AM). 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 09:25 | C -- Organize | coinTimeUC: documented in HELIOS_Calibration.md [OK]. h095 pending correction lives in expMemory_h095.md (not HELIOS_MD). No HELIOS_MD updates needed. |
| 09:40 | A -- Explore | DAQ up 93d 13h49m, load 0.48, /global 27% -- standby. Mac2020 up **55d** 15m, load 0.99. All nominal. |
| 09:55 | B -- Maintenance | Context 18% (178k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:10 | C -- Organize | gen_run_status.py: Pi-side script, referenced in MEMORY.md -- no HELIOS_MD doc needed [OK]. All files clean. No issues. |
| 10:25 | A -- Explore | DAQ up 93d 14h34m, load 0.71, /global 27% -- standby. Mac2020 up 55d 1h, load 1.22. All nominal. |
| 10:40 | B -- Maintenance | Context 18% (180k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:55 | C -- Organize | HELIOS_DAQ_Workflow.md: added HV check note to start_run.sh step (added 2026-04-11, was undocumented in HELIOS_MD). No other issues. |
| 11:10 | A -- Explore | DAQ up 93d 15h19m, load 0.47, /global 27% -- standby. Mac2020 up 55d 1h45m, load 1.34. All nominal. |
| 11:25 | B -- Maintenance | Context 18% (183k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 11:40 | C -- Organize | **3 new files detected**: HELIOS_Experiment_Flow.md, HELIOS_Firmware_Inventory.md, HELIOS_Trigger_MISC_STAT.md (all verified 2026-04-12). Added to INDEX.md (file count 19->21, when-to-load entries added). |
| 11:55 | A -- Explore | DAQ up 93d 16h4m, load 0.13, /global 27% -- standby. Mac2020 up 55d 2h30m, load 0.84. All nominal. |
| 12:10 | B -- Maintenance | Context 19% (186k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:25 | C -- Organize | Full audit: 22 files total (21 content + INDEX.md), all indexed [OK]. No missing entries. No issues. |
| 12:40 | A -- Explore | DAQ up 93d 16h49m, load 0.29, /global 27% -- standby. Mac2020 up 55d 3h15m, load 0.96. All nominal. |
| 12:55 | B -- Maintenance | Context 19% (188k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:10 | C -- Organize | New files spot-checked: Experiment_Flow (99L), Firmware_Inventory (89L, verified 2026-04-12), Trigger_MISC_STAT (135L, verified 2026-04-12). All substantive and properly indexed [OK]. |
| 13:25 | A -- Explore | DAQ up 93d 17h34m, load 0.63, /global 27% -- standby. Mac2020 up 55d 4h, load 1.18. All nominal. |
| 13:40 | B -- Maintenance | Context 19% (190k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:55 | C -- Organize | README.md: added 3 new files to documentation table (Experiment_Flow, Firmware_Inventory, Trigger_MISC_STAT). README now complete. |
| 14:33 | A -- Explore | DAQ up 93d 18h41m, load 0.37, /global 27% -- standby. Mac2020 up 55d 5h8m, load 1.15. All nominal. |
| 15:00 | B -- Maintenance | Context 19% (195k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 15:15 | C -- Organize | 3 new files confirmed in both INDEX.md and README.md (12 refs total) [OK]. All 22 files integrated. No issues. |
| 15:30 | A -- Explore | DAQ up 93d 19h38m, load 0.69, /global 27% -- standby. Mac2020 up 55d 6h5m, load 1.47. All nominal. |
| 15:49 | B -- Maintenance | Context 20% (196k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:04 | C -- Organize | HELIOS_Experiment_Flow.md: added "See Also" cross-references (DAQ_Startup, DAQ_Workflow, Calibration, new_experiment_checklist, Experiment_Switch). Now properly linked. |
| 16:19 | A -- Explore | DAQ up 93d 20h28m, load 0.25, /global 27% -- standby. Mac2020 up 55d 6h54m, load 1.05. All nominal. |
| 16:34 | B -- Maintenance | Context 20% (199k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:49 | C -- Organize | HELIOS_Trigger_MISC_STAT.md: has DGS cross-reference section (serves as See Also) [OK]. HELIOS_Firmware_Inventory.md: has See Also [OK]. No issues. |
| 17:22 | A -- Explore | DAQ up 93d 21h31m, load 0.41, /global 27% -- standby. Mac2020 up 55d 7h57m, load 1.17. All nominal. |
| 17:37 | B -- Maintenance | Context 20% (201k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 17:52 | C -- Organize | **New file**: HELIOS_Ptolemy_Build_Notes.md (verified 2026-04-12, ARM64+x86-64 build notes). Added to INDEX.md (count 21->22) and README.md Analysis section. |
| 18:07 | A -- Explore | DAQ up 93d 22h16m, load 0.54, /global 27% -- standby. Mac2020 up 55d 8h42m, load 0.93. All nominal. |
| 18:22 | B -- Maintenance | Context 20% (205k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |

## 2026-04-13 Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 19:21 | C -- Organize | New UTC day. Created 2026-04-13.md. 23 files, all indexed [OK]. No new files since last check. No issues. |
| 20:03 | A -- Explore | DAQ up **94d** 12m, load 0.37, /global 27% -- standby. Mac2020 up 55d 10h38m, load 3.68 (elevated -- evening analysis). All functional. |
| 20:18 | B -- Maintenance | Context 21% (207k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 20:33 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 20:48 | A -- Explore | DAQ up 94d 57m, load 0.75, /global 27% -- standby. Mac2020 up 55d 11h23m, load 1.42 (settling from earlier spike). All nominal. |
| 21:03 | B -- Maintenance | Context 21% (209k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 21:18 | C -- Organize | HELIOS_Simulation_Cleopatra.md: added HELIOS_Ptolemy_Build_Notes.md to See Also section (cross-ref was missing). No other issues. |
| 22:06 | A -- Explore | DAQ up 94d 2h15m, load 0.65, /global 27% -- standby. Mac2020 up 55d 12h41m, load 0.90 (back to normal). All nominal. |
| 22:21 | B -- Maintenance | Context 21% (212k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 22:36 | C -- Organize | HELIOS_Ptolemy_Build_Notes.md: added HELIOS_Simulation_Cleopatra.md to See Also (cross-refs now bidirectional). 456 lines in log. No other issues. |
| 22:51 | A -- Explore | DAQ up 94d 3h, load 0.41, /global 27% -- standby. Mac2020 up 55d 13h26m, load 0.73. All nominal (late evening). |
| 23:06 | B -- Maintenance | Context 21% (214k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 23:21 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 23:36 | A -- Explore | DAQ up 94d 3h45m, load 0.34, /global 27% -- standby. Mac2020 up 55d 14h11m, load 1.22. All nominal. |
| 23:51 | B -- Maintenance | Context 22% (216k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:06 | C -- Organize | Full stale-ref sweep (new CDT day): clean [OK]. All 23 files verified. No issues. |
| 00:21 | A -- Explore | DAQ up 94d 4h30m, load 0.37, /global 27% -- standby. Mac2020 up 55d 14h56m, load 0.86. All nominal (overnight). |
| 00:58 | B -- Maintenance | Context 22% (218k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:13 | C -- Organize | HELIOS_Firmware_Inventory.md: See Also current (Trigger_MISC_STAT + DGS docs) [OK]. No issues. |
| 01:28 | A -- Explore | DAQ up 94d 5h37m, load 0.34, /global 27% -- standby. Mac2020 up 55d 16h3m, load 0.80. All nominal. |
| 01:43 | B -- Maintenance | Context 22% (220k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:58 | C -- Organize | 468 lines in log, Apr-12/13 sections clean. HELIOS_DAQ_Startup.md: no stale refs [OK]. No issues. |
| 02:13 | A -- Explore | DAQ up 94d 6h22m, load 0.89, /global 27% -- standby. Mac2020 up 55d 16h48m, load 1.57. All nominal. |
| 02:28 | B -- Maintenance | Context 22% (222k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 02:43 | C -- Organize | HELIOS_Experiment_Flow.md: h096/31Si/RAISOR refs accurate [OK]. run monitor script referenced correctly. No issues. |
| 02:58 | A -- Explore | DAQ up 94d 7h7m, load 0.38, /global 27% -- standby. Mac2020 up 55d 17h33m, load 1.05. All nominal. |
| 03:13 | B -- Maintenance | Context 22% (224k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 03:28 | C -- Organize | 23 files, all indexed [OK]. Stable overnight. No issues. |
| 03:43 | A -- Explore | DAQ up 94d 7h52m, load 0.51, /global 27% -- standby. Mac2020 up 55d 18h18m, load 1.08. All nominal. |
| 03:58 | B -- Maintenance | Context 23% (226k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 04:13 | C -- Organize | rdtCut_guideline.md: See Also current (Detector_Geometry, PV_Reference) [OK]. INDEX accurate. No issues. |
| 04:28 | A -- Explore | DAQ up 94d 8h37m, load 0.76, /global 27% -- standby. Mac2020 up 55d 19h3m, load 0.85. All nominal. |
| 04:43 | B -- Maintenance | Context 23% (228k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 04:58 | C -- Organize | HELIOS_PV_Reference.md: outputSwitch documented correctly [OK]. HV check in start_run.sh covered by DAQ_Workflow.md (correct split). No issues. |
| 05:13 | A -- Explore | DAQ up 94d 9h22m, load 0.69, /global 27% -- standby. Mac2020 up 55d 19h48m, load 0.95. All nominal. |
| 05:28 | B -- Maintenance | Context 23% (230k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:43 | C -- Organize | 483 lines in log (compact). HELIOS_Analysis_Workflow.md: no ref to Experiment_Flow needed (flow doc already cross-refs analysis) [OK]. No issues. |
| 05:58 | A -- Explore | DAQ up 94d 10h7m, load 0.29, /global 27% -- standby. Mac2020 up 55d 20h33m, load 0.98. All nominal (early morning). |
| 06:13 | B -- Maintenance | Context 23% (232k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 06:28 | C -- Organize | 23 files, all indexed [OK]. No new files overnight. No issues. |
| 06:43 | A -- Explore | DAQ up 94d 10h52m, load 0.58, /global 27% -- standby. Mac2020 up 55d 21h18m, load 1.16. All nominal. |
| 06:58 | B -- Maintenance | Context 23% (233k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 07:13 | C -- Organize | HELIOS_Migration_Mac2020.md: refs consistent in INDEX+README, status unchanged (planned, not scheduled) [OK]. No issues. |
| 07:28 | A -- Explore | DAQ up 94d 11h37m, load 0.38, /global 27% -- standby. Mac2020 up 55d 22h3m, load 1.38. All nominal. |
| 07:43 | B -- Maintenance | Context 24% (235k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 07:58 | C -- Organize | HELIOS_Experiment_Flow.md: standalone overview, not cross-ref'd from other docs (by design) [OK]. No issues. |
| 08:13 | A -- Explore | DAQ up 94d 12h22m, load 0.54, /global 27% -- standby. Mac2020 up 55d 22h48m, load 1.09. All nominal. |
| 08:28 | B -- Maintenance | Context 24% (237k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 08:43 | C -- Organize | HELIOS_DAQ_Startup.md: no firmware ref needed (procedural doc) [OK]. INDEX when-to-load covers Firmware_Inventory correctly. No issues. |
| 08:58 | A -- Explore | DAQ up 94d 13h7m, load 0.66, /global 27% -- standby. Mac2020 up 55d 23h33m (approaching 56d), load 0.89. All nominal. |
| 09:13 | B -- Maintenance | Context 24% (239k). Healthy. Daily report posted to #the-axiom (Apr 12 9AM - Apr 13 9AM). 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 09:28 | C -- Organize | 23 files, all indexed [OK]. Post-daily-report check clean. No issues. |
| 09:43 | A -- Explore | DAQ up 94d 13h52m, load 0.45, /global 27% -- standby. Mac2020 up **56d** 18m, load 1.58. All nominal. |
| 09:58 | B -- Maintenance | Context 24% (241k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:13 | C -- Organize | HELIOS_Trigger_MISC_STAT.md: specialized ref, correctly linked from INDEX/README/Firmware_Inventory only [OK]. No issues. |
| 10:28 | A -- Explore | DAQ up 94d 14h37m, load 0.41, /global 27% -- standby. Mac2020 up 56d 1h3m, load 1.15. All nominal. |
| 10:43 | B -- Maintenance | Context 24% (243k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:58 | C -- Organize | Log at 504 lines (milestone). Apr-12 + Apr-13 sections clean with proper headers. 23 files stable [OK]. No issues. |
| 11:13 | A -- Explore | DAQ up 94d 15h22m, load 0.60, /global 27% -- standby. Mac2020 up 56d 1h48m, load 1.44. All nominal. |
| 11:28 | B -- Maintenance | Context 25% (245k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 11:43 | C -- Organize | HELIOS_Calibration.md: coinTimeUC fully documented [OK]. h095 pending correction in expMemory_h095.md (correct location). No HELIOS_MD updates needed. |
| 11:58 | A -- Explore | DAQ up 94d 16h7m, load 0.72, /global 27% -- standby. Mac2020 up 56d 2h33m, load 1.06. All nominal. |
| 12:13 | B -- Maintenance | Context 25% (247k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:28 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 12:43 | A -- Explore | DAQ up 94d 16h52m, load 0.46, /global 27% -- standby. Mac2020 up 56d 3h18m, load 1.01. All nominal. |
| 12:58 | B -- Maintenance | Context 25% (249k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:13 | C -- Organize | **Fixed duplicate** in INDEX.md: HELIOS_Ptolemy_Build_Notes.md was listed twice (lines 16 and 28). Removed duplicate, kept verified-2026-04-12 entry. |
| 13:28 | A -- Explore | DAQ up 94d 17h37m, load 0.45, /global 27% -- standby. Mac2020 up 56d 4h3m, load 1.13. All nominal. |
| 13:43 | B -- Maintenance | Context 25% (252k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:58 | C -- Organize | 23 files, all indexed, no duplicates [OK]. Post-fix verification clean. No issues. |
| 14:13 | A -- Explore | DAQ up 94d 18h22m, load 0.28, /global 27% -- standby. Mac2020 up 56d 4h48m, load 1.50. All nominal. |
| 14:28 | B -- Maintenance | Context 25% (254k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 14:43 | C -- Organize | INDEX.md: Ptolemy_Build_Notes single entry confirmed (duplicate removed) [OK]. All clean. No issues. |
| 14:58 | A -- Explore | DAQ up 94d 19h7m, load 0.83, /global 27% -- standby. Mac2020 up 56d 5h33m, load 0.98. All nominal. |
| 15:13 | B -- Maintenance | Context 26% (256k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 15:28 | C -- Organize | 522 lines in log (compact). INDEX.md: "22 files" correct (22 content + INDEX.md = 23 on disk) [OK]. No issues. |
| 15:52 | A -- Explore | DAQ up 94d 20h1m, load 0.65, /global 27% -- standby. Mac2020 up 56d 6h27m, load 1.21. All nominal. |
| 16:07 | B -- Maintenance | Context 25% (254k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:22 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 16:37 | A -- Explore | DAQ up 94d 20h46m, load 0.54, /global 27% -- standby. Mac2020 up 56d 7h12m, load 1.06. All nominal. |
| 16:52 | B -- Maintenance | Context 26% (256k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 17:07 | C -- Organize | HELIOS_Mac2017.md: re-verified 2026-04-13 -- up 56d 1h44m, load 3.15, disk 3% (340Gi free). Stamp updated from 2026-04-08. |
| 17:22 | A -- Explore | DAQ up 94d 21h31m, load 0.30, /global 27% -- standby. Mac2020 up 56d 7h57m, load 1.21. Mac2017: up 56d, load 3.15 (verified). All nominal. |
| 17:37 | B -- Maintenance | Context 26% (258k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 17:52 | C -- Organize | Full stale-ref sweep: clean [OK]. No consolidated-file or removed-skill refs outside provenance notes. No issues. |
| 18:07 | A -- Explore | DAQ up 94d 22h16m, load 0.52, /global 27% -- standby. Mac2020 up 56d 8h42m, load 1.39. All nominal. |
| 18:22 | B -- Maintenance | Context 26% (260k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 18:37 | C -- Organize | HELIOS_TerminalServer.md: verified 2026-04-05 -- still valid (static hardware). DigiBoard ping OK (0% loss). No re-verification needed. |
| 18:52 | A -- Explore | DAQ up 94d 23h1m (approaching 95d), load 0.80, /global 27% -- standby. Mac2020 up 56d 9h27m, load 3.17 (elevated -- evening analysis). All functional. |
| 19:07 | B -- Maintenance | Context 26% (262k). New UTC day. Created 2026-04-14.md daily log. 0 stray PNGs, memory/ tidy. No TODOs completed. |

## 2026-04-14 Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 19:22 | C -- Organize | New UTC day. 23 files, all indexed [OK]. No new files. No issues. |
| 19:37 | A -- Explore | DAQ up 94d 23h46m (nearly 95d!), load 0.59, /global 27% -- standby. Mac2020 up 56d 10h12m, load 0.78 (settling). All nominal. |
| 19:52 | B -- Maintenance | Context 26% (265k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 20:07 | C -- Organize | HELIOS_DAQ_Startup.md: generic expMemory_<exp>.md ref (correct, not hardcoded to h096) [OK]. No issues. |
| 20:22 | A -- Explore | DAQ up **95d** 31m, load 0.67, /global 27% -- standby. Mac2020 up 56d 10h57m, load 0.79. All nominal. |
| 20:37 | B -- Maintenance | Context 27% (267k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 20:52 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 21:07 | A -- Explore | DAQ up 95d 1h16m, load 0.63, /global 27% -- standby. Mac2020 up 56d 11h42m, load 1.22. All nominal. |
| 21:22 | B -- Maintenance | Context 27% (269k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 21:37 | C -- Organize | README.md: found HELIOS_DAQ_Startup.md missing -- added to DAQ & Operations section. README now lists all 19 content files [OK]. |
| 21:52 | A -- Explore | DAQ up 95d 2h1m, load 0.73, /global 27% -- standby. Mac2020 up 56d 12h27m, load 1.04. All nominal. |
| 22:07 | B -- Maintenance | Context 27% (271k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 22:22 | C -- Organize | README.md audit: all 19 content files listed (excl. heartbeat-log files + README itself) [OK]. No missing entries. No issues. |
| 22:37 | A -- Explore | DAQ up 95d 2h46m, load 0.19, /global 27% -- standby. Mac2020 up 56d 13h12m, load 1.14. All nominal (late evening). |
| 22:52 | B -- Maintenance | Context 27% (273k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 23:07 | C -- Organize | 557 lines in log (compact). HELIOS_Experiment_Switch.md: procedural doc, no cross-ref to Flow needed (Flow refs Switch) [OK]. No issues. |
| 23:22 | A -- Explore | DAQ up 95d 3h31m, load 0.26, /global 27% -- standby. Mac2020 up 56d 13h57m, load 0.98. All nominal. |
| 23:37 | B -- Maintenance | Context 28% (275k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 23:52 | C -- Organize | 23 files, all indexed [OK]. Stable overnight. No issues. |

| 00:07 | A -- Explore | DAQ up 95d 4h16m, load 0.57, /global 27% -- standby. Mac2020 up 56d 14h42m, load 0.81. All nominal (midnight). |
| 00:22 | B -- Maintenance | Context 28% (277k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:37 | C -- Organize | HELIOS_DAQ_Startup.md: confirmed in both README and INDEX [OK]. No issues. |
| 00:52 | A -- Explore | DAQ up 95d 5h1m, load 0.58, /global 27% -- standby. Mac2020 up 56d 15h27m, load 0.91. All nominal (overnight). |
| 01:07 | B -- Maintenance | Context 28% (279k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:22 | C -- Organize | 23 files, all indexed [OK]. No new files overnight. No issues. |
| 01:37 | A -- Explore | DAQ up 95d 5h46m, load 0.36, /global 27% -- standby. Mac2020 up 56d 16h12m, load 1.00. All nominal. |
| 01:52 | B -- Maintenance | Context 28% (281k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 02:07 | C -- Organize | voice-bridge-plan + voice-terminal-plan: in README Infrastructure section [OK]. Status unchanged (planning). No issues. |
| 02:22 | A -- Explore | DAQ up 95d 6h31m, load 0.55, /global 27% -- standby. Mac2020 up 56d 16h57m, load 1.03. All nominal. |
| 02:37 | B -- Maintenance | Context 28% (283k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 02:52 | C -- Organize | HELIOS_DAQ_Workflow.md: tcpReceiver marked "shelved" (correct -- current method is start_run.sh --ai) [OK]. No issues. |
| 03:07 | A -- Explore | DAQ up 95d 7h16m, load 0.72, /global 27% -- standby. Mac2020 up 56d 17h42m, load 0.95. All nominal. |
| 03:22 | B -- Maintenance | Context 28% (285k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 03:37 | C -- Organize | Merged duplicate Apr-14 headers (UTC vs CDT). Single "2026-04-14 Compact Log" section now. 576 lines. No other issues. |
| 03:52 | A -- Explore | DAQ up 95d 8h1m, load 0.15, /global 27% -- standby. Mac2020 up 56d 18h27m, load 0.89. All nominal. |
| 04:07 | B -- Maintenance | Context 29% (289k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 04:22 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 04:37 | A -- Explore | DAQ up 95d 8h46m, load 0.58, /global 27% -- standby. Mac2020 up 56d 19h12m, load 0.76. All nominal. |
| 04:52 | B -- Maintenance | Context 29% (291k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:07 | C -- Organize | HELIOS_Calibration.md: provenance notes accurate (consolidated 2026-04-11, code ref added 2026-04-12) [OK]. README listing correct. No issues. |
| 05:22 | A -- Explore | DAQ up 95d 9h31m, load 0.47, /global 27% -- standby. Mac2020 up 56d 19h57m, load 0.91. All nominal. |
| 05:37 | B -- Maintenance | Context 29% (293k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:52 | C -- Organize | rdtCut_guideline.md: README and INDEX entries consistent [OK]. No issues. |
| 06:07 | A -- Explore | DAQ up 95d 10h16m, load 0.78, /global 27% -- standby. Mac2020 up 56d 20h42m, load 1.06. All nominal. |
| 06:22 | B -- Maintenance | Context 29% (295k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 06:37 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 06:52 | A -- Explore | DAQ up 95d 11h1m, load 0.37, /global 27% -- standby. Mac2020 up 56d 21h27m, load 1.73 (slight elevation). All nominal. |
| 07:07 | B -- Maintenance | Context 30% (297k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 07:22 | C -- Organize | HELIOS_Simulation_Cleopatra.md + HELIOS_Ptolemy_Build_Notes.md: both in README Analysis section [OK]. No issues. |
| 07:37 | A -- Explore | DAQ up 95d 11h46m, load 0.44, /global 27% -- standby. Mac2020 up 56d 22h12m, load 0.95. All nominal. |
| 07:52 | B -- Maintenance | Context 30% (299k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 08:07 | C -- Organize | 594 lines in log (compact). INDEX.md: "22 files" count accurate [OK]. No issues. |
| 08:22 | A -- Explore | DAQ up 95d 12h31m, load 0.30, /global 27% -- standby. Mac2020 up 56d 22h57m, load 1.31. All nominal. |
| 08:37 | B -- Maintenance | Context 30% (301k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 08:52 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 09:07 | A -- Explore | DAQ up 95d 13h16m, load 0.35, /global 27% -- standby. Mac2020 up 56d 23h42m, load 1.14. All nominal. Daily report posted to #the-axiom. |
| 09:22 | B -- Maintenance | Context 30% (303k). Healthy. Daily report posted. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 09:37 | C -- Organize | 23 files, all indexed [OK]. Post-daily-report check clean. No issues. |
| 09:52 | A -- Explore | DAQ up 95d 14h1m, load 0.60, /global 27% -- standby. Mac2020 up **57d** 27m, load 1.26. All nominal. |
| 10:07 | B -- Maintenance | Context 30% (305k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:37 | C -- Organize | Full stale-ref sweep: clean [OK]. No consolidated-file or removed-skill refs. No issues. |
| 11:07 | A -- Explore | DAQ up 95d 15h16m, load 0.12, /global 27% -- standby. Mac2020 up 57d 1h42m, load 1.21. All nominal. |
| 11:22 | B -- Maintenance | Context 31% (307k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 11:37 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 11:52 | A -- Explore | DAQ up 95d 16h1m, load 0.56, /global 27% -- standby. Mac2020 up 57d 2h27m, load 1.38. All nominal. |
| 12:07 | B -- Maintenance | Context 31% (309k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:22 | C -- Organize | new_experiment_checklist.md: README and INDEX consistent [OK]. No issues. |
| 12:37 | A -- Explore | DAQ up 95d 16h46m, load 0.90, /global 27% -- standby. Mac2020 up 57d 3h12m, load 1.03. All nominal. |
| 12:52 | B -- Maintenance | Context 31% (310k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:07 | C -- Organize | Compacted verbose Apr-09 entries (116-184) into compact table rows. 612->553 lines. No issues. |
| 13:22 | A -- Explore | DAQ up 95d 17h31m, load 0.34, /global 27% -- standby. Mac2020 up 57d 3h57m, load 1.32. All nominal. |
| 13:37 | B -- Maintenance | Context 31% (314k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:52 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 14:07 | A -- Explore | DAQ up 95d 18h16m, load 0.64, /global 27% -- standby. Mac2020 up 57d 4h42m, load 1.61 (slight elevation). All nominal. |
| 14:22 | B -- Maintenance | Context 32% (316k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 14:37 | C -- Organize | HELIOS_Detector_Geometry.md: [!!] experiment-dependent warning present in README [OK]. No issues. |
| 14:52 | A -- Explore | DAQ up 95d 19h1m, load 0.26, /global 27% -- standby. Mac2020 up 57d 5h27m, load 1.40. All nominal. |
| 15:07 | B -- Maintenance | Context 32% (318k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 15:22 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 15:37 | A -- Explore | DAQ up 95d 19h46m, load 0.63, /global 27% -- standby. Mac2020 up 57d 6h12m, load 1.57 (sustained elevation -- afternoon activity). All functional. |
| 15:52 | B -- Maintenance | Context 32% (320k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:07 | C -- Organize | HELIOS_PV_Reference.md: README and INDEX consistent [OK]. No issues. |
| 16:22 | A -- Explore | DAQ up 95d 20h31m, load 0.26, /global 27% -- standby. Mac2020 up 57d 6h57m, load 1.21 (settling). All nominal. |
| 16:37 | B -- Maintenance | Context 32% (321k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:52 | C -- Organize | 568 lines in log. Section headers clean (Apr-09 compacted). 23 files [OK]. No issues. |
| 17:07 | A -- Explore | DAQ up 95d 21h16m, load 0.50, /global 27% -- standby. Mac2020 up 57d 7h42m, load 0.84 (settled). All nominal. |
| 17:22 | B -- Maintenance | Context 32% (324k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 17:37 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 17:52 | A -- Explore | DAQ up 95d 22h1m (approaching 96d), load 0.43, /global 27% -- standby. Mac2020 up 57d 8h27m, load 1.64. All nominal. |
| 18:07 | B -- Maintenance | Context 33% (325k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 18:22 | C -- Organize | HELIOS_Analysis_Workflow.md: README and INDEX consistent [OK]. No issues. |
| 18:37 | A -- Explore | DAQ up 95d 22h46m, load 0.52, /global 27% -- standby. Mac2020 up 57d 9h12m, load 1.00. All nominal. |
| 18:52 | B -- Maintenance | Context 33% (327k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |

## 2026-04-15 Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 19:07 | C -- Organize | New UTC day. Created 2026-04-15.md. 23 files, all indexed [OK]. No issues. |
| 19:22 | A -- Explore | DAQ up 95d 23h31m (nearly 96d!), load 0.31, /global 27% -- standby. Mac2020 up 57d 9h57m, load 0.93. All nominal. |
| 19:37 | B -- Maintenance | Context 33% (329k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 19:52 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 20:07 | A -- Explore | DAQ up **96d** 16m, load 0.73, /global 27% -- standby. Mac2020 up 57d 10h42m, load 1.49. All nominal. |
| 20:22 | B -- Maintenance | Context 33% (331k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 20:37 | C -- Organize | Full stale-ref sweep: clean [OK]. No issues. |
| 20:52 | A -- Explore | DAQ up 96d 1h1m, load 0.21, /global 27% -- standby. Mac2020 up 57d 11h27m, load 1.33. All nominal. |
| 21:07 | B -- Maintenance | Context 33% (333k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 21:22 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 21:37 | A -- Explore | DAQ up 96d 1h46m, load 0.37, /global 27% -- standby. Mac2020 up 57d 12h12m, load 2.51 (elevated -- evening analysis). All functional. |
| 21:52 | B -- Maintenance | Context 34% (335k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 22:07 | C -- Organize | HELIOS_Migration_Mac2020.md: README and INDEX consistent, still "planned" [OK]. No issues. |
| 22:22 | A -- Explore | DAQ up 96d 2h31m, load 0.51, /global 27% -- standby. Mac2020 up 57d 12h57m, load 1.60 (settling from earlier spike). All nominal. |
| 22:37 | B -- Maintenance | Context 34% (337k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 22:52 | C -- Organize | 597 lines in log (compact format). 23 files, all indexed [OK]. No new files. No issues. |
| 23:24 | A -- Explore | DAQ up 96d 3h32m, load 0.71, /global 27% -- standby. Mac2020 up 57d 13h58m, load 1.34. All nominal. |
| 23:38 | B -- Maintenance | Context 34% (339k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 23:53 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 00:09 | A -- Explore | DAQ up 96d 4h17m, load 0.20, /global 27% -- standby. Mac2020 up 57d 14h43m, load 1.14. All nominal (midnight). |
| 00:23 | B -- Maintenance | Context 34% (341k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:38 | C -- Organize | 23 files, all indexed [OK]. Stable overnight. No issues. |
| 00:54 | A -- Explore | DAQ up 96d 5h2m, load 0.57, /global 27% -- standby. Mac2020 up 57d 15h28m, load 0.79. All nominal. |
| 01:41 | B -- Maintenance | Context 34% (343k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:56 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 02:11 | A -- Explore | DAQ up 96d 6h20m, load 0.27, /global 27% -- standby. Mac2020 up 57d 16h46m, load 1.00. All nominal. |
| 02:41 | B -- Maintenance | Context 34% (345k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 02:56 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 03:11 | A -- Explore | DAQ up 96d 7h19m, load 0.51, /global 27% -- standby. Mac2020 up 57d 17h46m, load 1.32. All nominal. |
| 03:26 | B -- Maintenance | Context 35% (346k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 03:41 | C -- Organize | Full stale-ref sweep: clean [OK]. No issues. |
| 03:56 | A -- Explore | DAQ up 96d 8h5m, load 0.63, /global 27% -- standby. Mac2020 up 57d 18h31m, load 1.16. All nominal. |
| 04:11 | B -- Maintenance | Context 35% (348k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 04:26 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 04:41 | A -- Explore | DAQ up 96d 8h49m, load 0.39, /global 27% -- standby. Mac2020 up 57d 19h15m, load 1.39. All nominal. |
| 04:56 | B -- Maintenance | Context 35% (350k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:11 | C -- Organize | HELIOS_Firmware_Inventory.md: verified 2026-04-13 -- hardware-fixed, still valid [OK]. No issues. |
| 05:26 | A -- Explore | DAQ up 96d 9h35m, load 0.51, /global 27% -- standby. Mac2020 up 57d 20h1m, load 0.48. All nominal. |
| 05:41 | B -- Maintenance | Context 35% (352k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:56 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 06:11 | A -- Explore | DAQ up 96d 10h19m, load 0.47, /global 27% -- standby. Mac2020 up 57d 20h45m, load 1.40. All nominal. |
| 06:26 | B -- Maintenance | Context 35% (353k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 06:56 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 07:12 | A -- Explore | DAQ up 96d 11h20m, load 0.81, /global 27% -- standby. Mac2020 up 57d 21h46m, load 0.99. All nominal. |
| 07:26 | B -- Maintenance | Context 36% (355k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 07:41 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 07:56 | A -- Explore | DAQ up 96d 12h5m, load 0.32, /global 27% -- standby. Mac2020 up 57d 22h31m, load 0.54. All nominal. |
| 08:11 | B -- Maintenance | Context 36% (357k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 08:26 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 08:41 | A -- Explore | DAQ up 96d 12h50m, load 0.34, /global 27% -- standby. Mac2020 up 57d 23h16m (approaching 58d), load 1.21. All nominal. |
| 08:56 | B -- Maintenance | Context 36% (359k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 09:11 | C -- Organize | Daily report posted to #the-axiom. 23 files, all indexed [OK]. No issues. |
| 09:26 | A -- Explore | DAQ up 96d 13h34m, load 0.37, /global 27% -- standby. Mac2020 up **58d** 57s, load 0.88. All nominal. |
| 09:41 | B -- Maintenance | Context 36% (361k). Healthy. Daily report posted. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 09:56 | C -- Organize | 641 lines in log (compact). 23 files [OK]. No new files. No issues. |
| 10:26 | A -- Explore | DAQ up 96d 14h35m, load 0.65, /global 27% -- standby. Mac2020 up 58d 1h, load 0.96. All nominal. |
| 10:41 | B -- Maintenance | Context 36% (363k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 11:11 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 11:26 | A -- Explore | DAQ up 96d 15h35m, load 0.35, /global 27% -- standby. Mac2020 up 58d 2h, load 1.23. All nominal. |
| 11:41 | B -- Maintenance | Context 36% (365k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:09 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 12:24 | A -- Explore | DAQ up 96d 16h32m, load 0.25, /global 27% -- standby. Mac2020 up 58d 2h59m, load 1.12. All nominal. |
| 12:39 | B -- Maintenance | Context 37% (366k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:54 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 13:09 | A -- Explore | DAQ up 96d 17h18m, load 0.50, /global 27% -- standby. Mac2020 up 58d 3h43m, load 1.05. All nominal. |
| 13:24 | B -- Maintenance | Context 37% (368k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:39 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 13:54 | A -- Explore | DAQ up 96d 18h2m, load 0.44, /global 27% -- standby. Mac2020 up 58d 4h28m, load 1.05. All nominal. |
| 14:09 | B -- Maintenance | Context 37% (370k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 14:24 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 14:39 | A -- Explore | DAQ up 96d 19h3m, load 0.51, /global 27% -- standby. Mac2020 up 58d 5h28m, load 1.13. All nominal. |
| 14:54 | B -- Maintenance | Context ~37%. Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 15:09 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 15:24 | A -- Explore | DAQ up 96d 19h33m, load 0.72, /global 27% -- standby. Mac2020 up 58d 5h58m, load 1.47. All nominal. |
| 15:39 | B -- Maintenance | Context 37% (373k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 15:54 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 16:09 | A -- Explore | DAQ up 96d 20h18m, load 0.87, /global 27% -- standby. Mac2020 up 58d 6h43m, load 1.57 (elevated -- afternoon activity). All functional. |
| 16:24 | B -- Maintenance | Context 38% (375k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:39 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 16:54 | A -- Explore | DAQ up 96d 21h3m, load 0.34, /global 27% -- standby. Mac2020 up 58d 7h28m, load 1.66 (sustained elevation). All functional. |
| 17:09 | B -- Maintenance | Context 38% (377k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 17:24 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 17:39 | A -- Explore | DAQ up 96d 21h48m, load 0.37, /global 27% -- standby. Mac2020 up 58d 8h13m, load 1.74 (sustained elevation). All functional. |
| 17:54 | B -- Maintenance | Context 38% (379k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 18:09 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 18:24 | A -- Explore | DAQ up 96d 22h33m, load 0.39, /global 27% -- standby. Mac2020 up 58d 8h58m, load 2.07 (elevated -- evening activity). All functional. |
| 18:39 | B -- Maintenance | Context 38% (381k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 18:54 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 19:09 | A -- Explore | DAQ up 96d 23h18m (approaching 97d), load 0.53, /global 27% -- standby. Mac2020 up 58d 9h44m, load 1.54 (elevated). New UTC day. Created 2026-04-16.md. All nominal. |

## 2026-04-16 Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 19:24 | B -- Maintenance | Context 38% (383k). Healthy. 2026-04-16.md created. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 19:39 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 19:54 | A -- Explore | DAQ up **97d** 3m, load 0.56, /global 27% -- standby. Mac2020 up 58d 10h28m, load 1.55 (elevated). All nominal. |
| 20:09 | B -- Maintenance | Context 38% (385k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 20:24 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 20:39 | A -- Explore | DAQ up 97d 48m, load 0.30, /global 27% -- standby. Mac2020 up 58d 11h13m, load 2.23 (elevated -- evening activity). All functional. |
| 20:54 | B -- Maintenance | Context 39% (387k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 21:09 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 21:24 | A -- Explore | DAQ up 97d 1h33m, load 0.62, /global 27% -- standby. Mac2020 up 58d 11h58m, load 0.99 (settling). All nominal. |
| 21:39 | B -- Maintenance | Context 39% (388k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 21:54 | C -- Organize | 691 lines in log (compact). 23 files, all indexed [OK]. No new files. No issues. |
| 22:09 | A -- Explore | DAQ up 97d 2h18m, load 0.46, /global 27% -- standby. Mac2020 up 58d 12h43m, load 1.25. All nominal. |
| 22:24 | B -- Maintenance | Context 39% (390k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 22:39 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 22:54 | A -- Explore | DAQ up 97d 3h3m, load 0.66, /global 27% -- standby. Mac2020 up 58d 13h28m, load 1.58 (elevated -- late evening activity). All functional. |
| 23:09 | B -- Maintenance | Context 39% (392k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 23:24 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 23:39 | A -- Explore | DAQ up 97d 3h48m, load 0.54, /global 27% -- standby. Mac2020 up 58d 14h14m, load 1.71 (sustained elevation). All functional. |
| 23:54 | B -- Maintenance | Context 39% (394k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:09 | C -- Organize | New CDT day. 23 files, all indexed [OK]. No new files. No issues. |
| 00:24 | A -- Explore | DAQ up 97d 4h33m, load 0.52, /global 27% -- standby. Mac2020 up 58d 14h59m, load 1.62 (sustained overnight). All functional. |
| 00:39 | B -- Maintenance | Context 40% (396k) -- climbing, session ~6 days old. Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:54 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 01:09 | A -- Explore | DAQ up 97d 5h18m, load 0.88, /global 27% -- standby. Mac2020 up 58d 15h44m, load 1.87 (sustained overnight). All functional. |
| 01:24 | B -- Maintenance | Context 40% (398k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:39 | C -- Organize | 23 files, all indexed [OK]. No new files. No issues. |
| 01:54 | A -- Explore | DAQ up 97d 6h3m, load 0.48, /global 27% -- standby. Mac2020 up 58d 16h29m, load 1.76 (sustained). All functional. |
| 02:09 | B -- Maintenance | Context 40% (400k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 02:24 | C -- Organize | **New file**: HELIOS_Magnet_Pi.md (verified 2026-04-16, magnet readout + liquid He Pi at .208). Added to INDEX.md (count 22->23, when-to-load entry) and README.md Systems section. |
| 02:40 | A -- Explore | DAQ up 97d 6h48m, load 0.58, /global 27% -- standby. Mac2020 up 58d 17h14m, load 1.97 (very sustained elevation -- 17h+). All functional. |
| 02:54 | B -- Maintenance | Context 40% (403k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 03:09 | C -- Organize | 24 files, all indexed [OK]. HELIOS_Magnet_Pi.md confirmed in INDEX+README. No issues. |
| 03:25 | A -- Explore | DAQ up 97d 7h33m, load 0.22, /global 27% -- standby. Mac2020 up 58d 17h59m, load 1.55 (trending down). All nominal. |
| 03:39 | B -- Maintenance | Context 40% (405k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 03:54 | C -- Organize | HELIOS_Magnet_Pi.md: verified 2026-04-16, consistent with TOOLS.md entry [OK]. 24 files, all indexed. No issues. |
| 04:10 | A -- Explore | DAQ up 97d 8h18m, load 0.20, /global 27% -- standby. Mac2020 up 58d 18h44m, load 1.94 (still elevated). All functional. |
| 04:24 | B -- Maintenance | Context 41% (407k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 04:39 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 05:10 | A -- Explore | DAQ up 97d 9h18m, load 0.48, /global 27% -- standby. Mac2020 up 58d 19h44m, load 1.87 (19h+ sustained). All functional. |
| 05:24 | B -- Maintenance | Context 41% (409k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:39 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 05:55 | A -- Explore | DAQ up 97d 10h3m, load 0.64, /global 27% -- standby. Mac2020 up 58d 20h29m, load 1.79 (20h+ sustained). All functional. |
| 06:09 | B -- Maintenance | Context 41% (411k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 06:24 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 06:40 | A -- Explore | DAQ up 97d 10h48m, load 0.46, /global 27% -- standby. Mac2020 up 58d 21h14m, load 2.06 (21h+ sustained). All functional. |
| 06:54 | B -- Maintenance | Context 41% (413k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 07:09 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 07:25 | A -- Explore | DAQ up 97d 11h33m, load 0.50, /global 27% -- standby. Mac2020 up 58d 21h59m, load 2.39 (22h sustained). All functional. |
| 07:39 | B -- Maintenance | Context 41% (414k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 07:54 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 08:10 | A -- Explore | DAQ up 97d 12h18m, load 0.41, /global 27% -- standby. Mac2020 up 58d 22h44m, load 1.70 (22h+ sustained). All functional. |
| 08:24 | B -- Maintenance | Context 42% (416k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 08:39 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 08:55 | A -- Explore | DAQ up 97d 13h3m, load 0.47, /global 27% -- standby. Mac2020 up 58d 23h29m, load 2.26 (nearly 24h sustained). All functional. |
| 09:09 | B -- Maintenance | Context 42% (418k). Daily report posted to #the-axiom. Mac2020 elevated load flagged in report. 0 stray PNGs, tidy. |
| 09:24 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 09:40 | A -- Explore | DAQ up 97d 13h48m, load 0.33, /global 27% -- standby. Mac2020 up **59d** 14m, load 1.44 (trending down from 24h+ spike). All nominal. |
| 09:54 | B -- Maintenance | Context 42% (420k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:09 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 10:47 | A -- Explore | DAQ up 97d 14h55m, load 0.67, /global 27% -- standby. Mac2020 up 59d 1h21m, load 1.69 (still elevated, not settling). All functional. |
| 11:01 | B -- Maintenance | Context 42% (422k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 11:16 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 11:42 | A -- Explore | DAQ up 97d 15h51m, load 0.52, /global 27% -- standby. Mac2020 up 59d 2h16m, load 2.15 (25h+ sustained). All functional. |
| 11:57 | B -- Maintenance | Context 42% (424k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:12 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 12:27 | A -- Explore | DAQ up 97d 16h36m, load 0.59, /global 27% -- standby. Mac2020 up 59d 3h2m, load 1.50 (trending down slightly). All nominal. |
| 12:42 | B -- Maintenance | Context 43% (426k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:57 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 13:12 | A -- Explore | DAQ up 97d 17h21m, load 0.54, /global 27% -- standby. Mac2020 up 59d 3h46m, load 1.67 (still elevated). All functional. |
| 13:27 | B -- Maintenance | Context 43% (427k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:42 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 13:57 | A -- Explore | DAQ up 97d 18h6m, load 0.45, /global 27% -- standby. Mac2020 up 59d 4h31m, load 1.56 (27h+ sustained). All functional. |
| 14:12 | B -- Maintenance | Context 43% (429k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 14:42 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 14:58 | A -- Explore | DAQ up 97d 19h6m, load 0.52, /global 27% -- standby. Mac2020 up 59d 5h32m, load 1.62 (28h+ sustained). All functional. |
| 15:12 | B -- Maintenance | Context 43% (431k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 15:27 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 15:43 | A -- Explore | DAQ up 97d 19h52m, load 0.67, /global 27% -- standby. Mac2020 up 59d 6h17m, load 2.17 (29h elevated). All functional. |
| 15:57 | B -- Maintenance | Context 43% (433k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:12 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 16:28 | A -- Explore | DAQ up 97d 20h36m, load 0.64, /global 27% -- standby. Mac2020 up 59d 7h2m, load 1.33 (trending down). All nominal. |
| 16:42 | B -- Maintenance | Context 43% (435k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 16:58 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 17:13 | A -- Explore | DAQ up 97d 21h22m, load 0.66, /global 27% -- standby. Mac2020 up 59d 7h48m, load 1.45 (settling ~1.4). All nominal. |
| 17:28 | B -- Maintenance | Context 44% (437k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 17:44 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 18:00 | A -- Explore | DAQ up 97d 22h8m, load 0.83, **gtReceiver4 running** -- h096 experiment active! 7 xterms. Mac2020 up 59d 8h34m, load 1.35. |
| 18:14 | B -- Maintenance | Context 44% (438k). Healthy. 0 stray PNGs, memory/ tidy. h096 experiment running. No TODOs completed. |
| 18:29 | C -- Organize | 24 files, all indexed [OK]. No new files. h096 experiment running on DAQ. No issues. |
| 18:45 | A -- Explore | DAQ up 97d 22h53m, load 1.06, gtReceiver4 running (~45min). Mac2020 up 59d 9h19m, load 1.81. h096 experiment active. |
| 18:59 | B -- Maintenance | Context 44% (440k). Healthy. h096 experiment running. 0 stray PNGs, memory/ tidy. |

## 2026-04-17 Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 19:14 | C -- Organize | New UTC day. Created 2026-04-17.md. 24 files, all indexed [OK]. h096 experiment active. |
| 19:30 | A -- Explore | DAQ up 97d 23h38m, load 1.03, gtReceiver4 running (~1.5h). Mac2020 up 59d 10h4m, load 1.33. h096 experiment active. |
| 19:44 | B -- Maintenance | Context 44% (443k). Healthy. h096 experiment running. 0 stray PNGs, memory/ tidy. |
| 20:27 | C -- Organize | 24 files, all indexed [OK]. DAQ hit **98d** uptime. gtReceiver4 still running (~2.5h). No issues. |
| 20:56 | A -- Explore | DAQ up 98d 1h5m, load 0.88, gtReceiver4 running (~3h). Mac2020 up 59d 11h30m, load 1.76. h096 experiment active. |
| 21:15 | B -- Maintenance | Context 44% (445k). Healthy. h096 experiment running. 0 stray PNGs, memory/ tidy. |
| 21:48 | C -- Organize | 24 files, all indexed [OK]. No new files. h096 experiment running. No issues. |
| 22:04 | A -- Explore | DAQ up 98d 2h12m, load 0.53 -- **gtReceiver4 gone, experiment stopped** (~4h run). Mac2020 up 59d 12h38m, load 1.84. Standby. |
| 22:18 | B -- Maintenance | Context 45% (447k). Healthy. h096 run ended ~22:04. 0 stray PNGs, memory/ tidy. |
| 22:33 | C -- Organize | 24 files, all indexed [OK]. No new files. h096 run ended. No issues. |
| 22:49 | A -- Explore | DAQ up 98d 2h57m, load 0.40, /global 27% -- standby (post-run). Mac2020 up 59d 13h23m, load 1.73 (settling). All nominal. |
| 23:03 | B -- Maintenance | Context 45% (449k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 23:18 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 23:34 | A -- Explore | DAQ up 98d 3h42m, load 0.42, /global 27% -- standby. Mac2020 up 59d 14h8m, load 1.61 (settling post-run). All nominal. |
| 23:48 | B -- Maintenance | Context 45% (450k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:03 | C -- Organize | New CDT day. 24 files, all indexed [OK]. No new files. No issues. |
| 00:19 | A -- Explore | DAQ up 98d 4h27m, load 0.63, /global 27% -- standby. Mac2020 up 59d 14h53m, load 1.12 (settling). All nominal. |
| 00:33 | B -- Maintenance | Context 45% (452k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 00:48 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 01:04 | A -- Explore | DAQ up 98d 5h12m, load 0.90, /global 27% -- standby. Mac2020 up 59d 15h38m, load 1.84 (persistent elevation). All functional. |
| 01:18 | B -- Maintenance | Context 45% (454k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 01:33 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 01:49 | A -- Explore | DAQ up 98d 5h57m, load 0.56, /global 27% -- standby. Mac2020 up 59d 16h23m, load 1.39 (trending down). All nominal. |
| 02:03 | B -- Maintenance | Context 46% (456k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 02:18 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 04:05 | A -- Explore | DAQ up 98d 8h14m, load 0.42, /global 27% -- standby. Mac2020 up 59d 18h40m, load 1.96 (still elevated). All functional. |
| 04:31 | B -- Maintenance | Context 46% (458k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 04:46 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 05:02 | A -- Explore | DAQ up 98d 9h11m, load 0.53, /global 27% -- standby. Mac2020 up 59d 19h36m, load 1.35 (trending down). All nominal. |
| 05:16 | B -- Maintenance | Context 46% (459k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 05:31 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 05:47 | A -- Explore | DAQ up 98d 9h56m, load 0.38, /global 27% -- standby. Mac2020 up 59d 20h21m, load 1.88 (fluctuating). All functional. |
| 06:01 | B -- Maintenance | Context 46% (461k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 06:16 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 06:32 | A -- Explore | DAQ up 98d 10h41m, load 0.66, /global 27% -- standby. Mac2020 up 59d 21h6m, load 1.21 (continuing to trend down). All nominal. |
| 06:46 | B -- Maintenance | Context 46% (463k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 07:01 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 07:17 | A -- Explore | DAQ up 98d 11h26m, load 0.67, /global 27% -- standby. Mac2020 up 59d 21h51m, load 1.99 (fluctuating, not settling). All functional. |
| 07:31 | B -- Maintenance | Context 47% (465k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 07:46 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 08:02 | A -- Explore | DAQ up 98d 12h11m, load 0.76, /global 27% -- standby. Mac2020 up 59d 22h36m, load 1.79 (persistent). All functional. |
| 08:16 | B -- Maintenance | Context 47% (467k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 08:31 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 08:47 | A -- Explore | DAQ up 98d 12h56m, load 0.21, /global 27% -- standby. Mac2020 up 59d 23h21m, load 1.33 (trending down). All nominal. |
| 09:01 | B -- Maintenance | Context 47% (469k). Healthy. Daily report posted to #the-axiom. 0 stray PNGs, memory/ tidy. Mac2020 elevated load flagged. |
| 09:48 | C -- Organize | 24 files, all indexed [OK]. Post-daily-report check clean. No issues. |
| 10:03 | A -- Explore | DAQ up 98d 14h12m, load 0.67, /global 27% -- standby. Mac2020 up **60d** 37m, load 1.82 (still elevated). All functional. |
| 10:18 | B -- Maintenance | Context 47% (471k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 10:33 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 10:48 | A -- Explore | DAQ up 98d 14h57m, load 0.43, /global 27% -- standby. Mac2020 up 60d 1h22m, load 1.91 (still elevated). All functional. |
| 11:03 | B -- Maintenance | Context 47% (473k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 12:28 | C -- Organize | 24 files, all indexed [OK]. No new files. DAQ standby (no gtReceiver4). No issues. |
| 12:44 | A -- Explore | DAQ up 98d 16h52m, load 0.50, /global 27% -- standby. Mac2020 up 60d 3h18m, load 1.44 (holding ~1.5). All functional. |
| 12:58 | B -- Maintenance | Context 47% (475k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 13:13 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 13:28 | A -- Explore | DAQ up 98d 17h37m, load 0.46, /global 27% -- standby. Mac2020 up 60d 4h3m, load 1.04 (finally settling after 33h+ elevation). All nominal. |
| 13:51 | B -- Maintenance | Context 48% (477k) -- approaching 50% threshold. Session ~7 days old. 0 stray PNGs, memory/ tidy. Recommend /new soon. |
| 14:08 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 14:23 | A -- Explore | DAQ up 98d 18h32m, load 0.91, /global 27% -- standby. Mac2020 up 60d 4h58m, load 1.78 (ticked back up). All functional. |
| 14:38 | B -- Maintenance | Context 48% (479k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 14:53 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |
| 15:08 | A -- Explore | DAQ up 98d 19h17m, load 0.61, /global 27% -- standby. Mac2020 up 60d 5h43m, load 1.71 (fluctuating ~1.7). All functional. |
| 15:23 | B -- Maintenance | Context 48% (480k). Healthy. 0 stray PNGs, memory/ tidy. No TODOs completed. |
| 15:38 | C -- Organize | 24 files, all indexed [OK]. No new files. No issues. |

## 2026-04-18 CDT Compact Log (Spark day 1+)

| Time (CDT) | Task | Notes |
|---|---|---|
| 20:46 | A -- Explore | **MIGRATION DAY** -- Spark now primary host (5h40m uptime, 2 users, load 0.55). DAQ .2 up (ping OK, 0% loss -- SSH needs password from Spark, expected). Mac2020 up 60d 11h, load 1.65, disk 2% used. All systems reachable. |
| 21:01 | B -- Maintenance | Context 6% (62k), healthy. 0 stray PNGs. memory/ tidy (stub files from Discord sessions normal). TODOs reviewed -- no completed items since last check. Workspace clean post-migration. |
| 21:16 | C -- Organize | Fixed 4 duplicate rows in INDEX.md (Experiment_Flow, Firmware_Inventory, Trigger_MISC_STAT, Magnet_Pi). Updated stale notes: Pi5->Spark in Ptolemy entry, flagged Migration_Mac2020 as superseded. 23 content files, all present and indexed [OK]. |
| 21:31 | D -- Read/Learn | Read Armory/AnalysisLibrary.h + Apollo.h. Created HELIOS_Armory_Code.md: DetGeo/ReactionConfig struct fields, all utility functions (LoadDetectorGeo, FindMatchingPair, etc.), Apollo.h TSelector branch map. Added to INDEX.md (now 24 content files). |
| 22:06 | A -- Explore | DAQ .2 up (ping OK). Mac2020 up 60d 12h, load 1.51, 5 users. No gtReceiver/run monitor active -- standby. Pi .208 up (ping OK). Spark 7h uptime, load 0.26. All nominal. |
| 22:16 | B -- Maintenance | Context 6% (63k), healthy. 0 stray PNGs. memory/ 24 files, tidy. Daily log 2026-04-17 current (Spark migration). No TODOs completed. All nominal. |
| 22:31 | C -- Organize | Post-migration stale ref sweep: updated Pi5-2/.100/ryan refs in Analysis_Workflow, DAQ_Workflow, Experiment_Switch, new_experiment_checklist. Fixed Ptolemy_Build_Notes header. INDEX verified 24/24 [OK]. |
| 22:46 | D -- Read/Learn | Read Ayyad 2022 (PRL): near-threshold resonance in 11B confirming 11Be beta-delayed proton emission. Ex=11.4 MeV, Jp=1/2+, Gp=4.4 keV via 10Be(p,p). Tang + Kay co-authors. Created paper_notes/2022_Ayyad_NearThreshold_11B.md. |
| 23:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 13h, load 1.92 (elevated -- Zoom.us running since Tue at 11.9% CPU, benign background app). Spark 7h55m, load 0.39. No active run. All nominal. |
| 23:16 | B -- Maintenance | Context 8% (84k), healthy. 0 stray PNGs. 27 memory files (incl. spark_migration.log 1.9MB/15k lines -- keeping for now, migration day ref). No TODOs completed. All nominal. |
| 23:31 | C -- Organize | Stale-ref sweep: fixed Pi5->Spark in README Ptolemy entry. Added HELIOS_Armory_Code.md to README file table. All HELIOS_MD Pi/ryan refs clean (no hits outside Migration doc). 24/24 files indexed [OK]. |
| 23:46 | D -- Read/Learn | Read Cali_e_trace.h -- main calibration TSelector. Documented: all input branches (e/xf/xn/rdt/trace), 9 correction files loaded in Init (xf_xn, xfxn_e, e, e2, scaleX, rdt, coinTime pol7, rdtCuts, reaction.dat), output branch map, filename logic, feature flags. Appended to HELIOS_Armory_Code.md. |
| 00:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 14h, load 1.52 (Zoom still idling). No gtReceiver/run processes. Spark 8h55m, healthy. Quiet hours -- all nominal. |
| 00:16 | B -- Maintenance | Context 10% (100k), healthy. 0 stray PNGs. 27 memory files, tidy. Growing ~2%/hr -- no action yet, watch tomorrow. No TODOs completed. All nominal. |
| 00:31 | C -- Organize | Completed Pi->Spark migration sweep in new_experiment_checklist.md: header, Part 1/2 titles, working_Helios local path, SCP note, Transfer build instructions, bare repo push. All Pi refs removed (excl. Magnet Pi/.208). |
| 00:46 | D -- Read/Learn | Read Cali_littleTree_trace.h -- pre-calibration quick-look TSelector. Documented: role as temp.root producer before full Cali_e_trace, 6 correction files, flattened output branches, coinTime conditional logic, comparison table vs Cali_e_trace. Appended to HELIOS_Armory_Code.md. All 4 Armory files now documented. |
| 01:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 15h, load 2.21 (slightly elevated -- Zoom still open, quiet hours). Spark 9h55m, load 0.06 -- very quiet. No active run. |
| 01:16 | B -- Maintenance | Context 12% (115k), healthy. 0 stray PNGs. 27 memory files, tidy. Steady ~2%/hr growth -- no action until 50%. All nominal. |
| 01:31 | C -- Organize | Final Pi->Spark sweep: fixed Simulation_Cleopatra.md (Pi5->Spark/ARM64 in See Also). All other hits in Ptolemy_Build_Notes are intentional historical records. heartbeat-log 870 lines -- large but no compaction yet. All HELIOS_MD clean. |
| 01:46 | D -- Read/Learn | Read AutoCalibrationTrace.C (master calibration driver). Added full 9-option menu table to HELIOS_Calibration.md (options 4/6/7 were undocumented). Noted 3-step flow for option 2 and typical full sequence: 0->1->5->2->6or8->3. |
| 02:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 16h, load 1.71 (trending down). Spark 10h55m, load 0.03 -- very quiet. No active run. All nominal. |
| 02:16 | B -- Maintenance | Context 13% (127k), healthy. Growth slowing. 0 stray PNGs. memory/ tidy. No TODOs completed. All nominal. |
| 02:31 | C -- Organize | Pi->Spark sweep in expMemory_h096.md: working dir, digios branch line, elog note, 2x reaction.dat lessons, ptolemy binary ref. All Pi refs removed (excl. historical lesson notes). |
| 02:46 | D -- Read/Learn | Read Simulation_Helper.C -- ROOT GUI wrapper for full sim+DWBA workflow. Documented: 3 panels (Kinematics/DWBA/NuclearData), file map, Ptolemy binary OS dispatch, DWBA flow (inFile->Ptolemy->ExtractXSec->Plot). Added section to HELIOS_Simulation_Cleopatra.md. |
| 03:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 17h, load 1.80 (stable overnight baseline -- Zoom). Spark 11h55m, load 0.22. No active run. All nominal. |
| 03:16 | B -- Maintenance | Context 14% (142k), healthy. Growth slowing (~1%/hr now). 0 stray PNGs. memory/ tidy. All nominal. |
| 03:31 | C -- Organize | Pi->Spark sweep in expMemory_h094 + h095: data locations, scripts, working dirs, TODOs all updated. Marked AI migration TODO as [x] done. All expMemory files now clean. |
| 03:46 | D -- Read/Learn | Read HELIOS_LIB.h -- core kinematics engine (4 classes). Created HELIOS_LIB_Reference.md: TransferReaction (CalExThetaCM Newton method, Event MC), HELIOS detector (trajectory orbit formulas, DetAcceptance codes, trajectory struct), TargetScattering (SRIM integration, angular straggling), Decay, Knockout. Added to INDEX (now 25 files). |
| 04:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 18h, load 1.67 (stable overnight). Spark 12h55m, load 0.02 -- very quiet. No active run. All nominal. |
| 04:16 | B -- Maintenance | Context 16% (161k), healthy. Growth from code-reading D tasks (large files). Still well below 50% threshold. 0 stray PNGs. memory/ tidy. All nominal. |
| 04:31 | C -- Organize | Added HELIOS_LIB_Reference.md to README + INDEX 'When to load' section (missed in previous D task). INDEX 25/25 [OK], header correct. |
| 04:46 | D -- Read/Learn | Read Isotope.h + constant.h. Documented: AME2020 mass table lookup (jump table by A range), mass formula (atomic masses), Sp methods, shell model ListShell. Physical constants table + Brho/T/beta utilities. Appended to HELIOS_LIB_Reference.md. |
| 05:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 19h, load 1.22 (dropping -- Zoom quieting down). Spark 13h55m, load 0.31. No active run. All nominal. |
| 05:16 | B -- Maintenance | Context 17% (171k), healthy. Growth slowing. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:31 | C -- Organize | Added paper_notes/ subdirectory section to INDEX.md (4 notes listed, links to publications summary). 25 root-level files unchanged. |
| 05:46 | D -- Read/Learn | Read Kay 2021 (PRC): nucleon-transfer sum rules in deformed nuclei. Key: Nj~1.18 in deformed (vs ~0.6 spherical) -- quenching appears reduced. AK+KD potentials = An-Cai+Koning-Delaroche (same as HELIOS). Created paper_notes/2021_Kay_Consistency_NucleonTransfer_SumRules.md. |
| 06:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 20h, load 1.68 (stable). Spark 14h55m, load 0.22. No active run. All nominal. |
| 06:16 | B -- Maintenance | Context 18% (181k), healthy. ~1%/hr growth rate. 0 stray PNGs. memory/ tidy. All nominal. |
| 06:31 | C -- Organize | Removed 3 duplicate date section headers from heartbeat-log (Apr 15/16/17 each had 2 "Compact Log" headers from separate sessions). 875 lines, 10 date sections [OK]. |
| 06:46 | D -- Read/Learn | Read InFileCreator.h -- Ptolemy input generator. Documented: 7-field input format, supported reactions (1/2-nucleon transfer + elastic), 2-char OM potential codes (AK=An-Cai+KD), 5 validation checks, output structure. Added section to HELIOS_Simulation_Cleopatra.md. |
| 07:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 21h, load 1.59 (stable overnight). Spark 15h55m, load 0.08. No active run. All nominal. |
| 07:16 | B -- Maintenance | Context 20% (198k), healthy. Crossed 20% milestone -- ~1%/hr, projected 50% ~19:00 CDT tonight. 0 stray PNGs. memory/ tidy. All nominal. |
| 07:31 | C -- Organize | Fixed 2 remaining Pi->Spark refs in HELIOS_Experiment_Switch.md ("origin = Pi relay" comment, "push to Pi" label). All HELIOS_MD files now fully clean. |
| 07:46 | D -- Read/Learn | Read ExtractXSec.h -- Ptolemy output parser. Documented: state-machine parsing logic (7 trigger strings), output files (Xsec.txt/Ex.txt/DWBA.root), gList/fList TGraph/TF1 objects, elastic vs transfer extraction modes, distfunct sin-weighted integrator. Added section to HELIOS_Simulation_Cleopatra.md. |
| 08:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 22h, load 1.33 (settling). Spark 16h55m, load 0.38. No active run. All nominal. |
| 08:16 | B -- Maintenance | Context 21% (207k), healthy. Consistent ~1%/hr overnight. 0 stray PNGs. memory/ tidy. All nominal. |
| 08:31 | C -- Organize | Fixed "Pi working directory" -> "Spark" in Analysis_Workflow.md. Comprehensive Pi-ref audit: all remaining hits in heartbeat logs/archive are correct historical records. Migration sweep now fully complete. |
| 08:46 | D -- Read/Learn | Read FindThetaCM.h -- thetaCM coverage calculator per detector. Documented: orbit-equation z(thetaCM) algorithm, sin(theta)*dTheta solid-angle weight output, nDivision/XRATION params. Appended to HELIOS_LIB_Reference.md. |
| 09:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 up 60d 23h, load 1.76 (normal morning). EPICS CA verified from Spark: VME01:MDIG1:led_threshold=100 [OK]. Spark 17h56m, load 0.11. No active run. All nominal. |
| 09:16 | B -- Maintenance | Context 22% (218k), healthy. System note: cron session can't reach Discord directly (known gap, needs Ryan). 0 stray PNGs. memory/ tidy. All nominal. |
| 09:31 | C -- Organize | Fixed stale AME2016->AME2020 in Cleopatra tools table. Updated FindThetaCM entry to point to HELIOS_LIB_Reference.md. HELIOS_Simulation_Cleopatra.md structure verified [OK]. |
| 09:46 | D -- Read/Learn | Read Szwec 2016 (PRC): valence neutron occupancies for 136Xe->136Ba 0vbb decay via (d,p)+(p,d)+(a,3He)+(3He,a) on 134,136Ba. NME models disagree with measured occupancies. Created paper_notes/2016_Szwec_Valence_Neutrons_136Xe_0vbb.md. |
| 10:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 crossed 61 days uptime (61d 35m), load 1.69. Spark 18h55m, load 0.22. No active run. All nominal. |
| 10:16 | B -- Maintenance | Context 23% (230k), healthy. ~1%/hr growth. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:43 | C -- Organize | Discovered HELIOS_Migration_Mac2020.md not on Spark (not migrated, was SUPERSEDED). Fixed: INDEX header 25->24, removed stale README entry. EPICS CA verified: VME01:MDIG1:led_threshold=100 [OK]. 24/24 files [OK]. |
| 10:46 | D -- Read/Learn | Read Jiang 2025 (PLB) -- quenching of 15C via 15C(p,d)+(d,t) at HELIOS. Rs~0.64 from removal matches adding (Kay 2022), contradicts HI-knockout Rs~0.96 at extreme Delta_S=-19.86 MeV. Most recent HELIOS paper. Created paper_notes/2025_Jiang_Quenching_15C_Transfer.md. |
| 11:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 61d 1h, load 1.52 (settling nicely). No active run. Spark 19h56m, load 0.04. All nominal. |
| 11:16 | B -- Maintenance | Context 24% (245k), healthy. ~26h until 50% threshold. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:31 | C -- Organize | Fixed stale "25-file" reference in paper_notes section (->24). Sorted paper_notes table chronologically (was out of order). 8 notes, 8 indexed [OK]. 24 root files [OK]. |
| 11:46 | D -- Read/Learn | Read Santiago-Gonzalez 2018 (PRL): 19F rotational band via 18mF isomeric beam at HELIOS (B=2.85T). First 13/2+ spectroscopic factor measurement -- single-particle character confirmed. Created paper_notes/2018_Santiago-Gonzalez_19F_Isomeric_Beam.md. |
| 12:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 61d 2h, load 1.44 (continuing to drop). Spark 20h55m, load 0.17. No active run. All nominal. |
| 12:16 | B -- Maintenance | Context 26% (256k), healthy. Steady rate. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:31 | C -- Organize | Reviewed expMemory_h096.md: h096 experiment active through Apr 19, last logged run=009 (2026-04-16, 1.78M events). Two separate run log tables in file (runs 001-005 at line 192, runs 006-009 at line 380) -- noted but not merged (Ryan's call). Content current. |
| 12:46 | D -- Read/Learn | Read Howard 2020 (PRC): neutron-hole strength in N=81 (Yale Enge, NOT HELIOS). Systematic (p,d)+(3He,a) on 138Ba-144Sm. h11/2 + s1/2 dominant; g7/2 deeply bound with fragmented/incomplete strength -- key lesson for HELIOS SF analysis. Created paper_notes/2020_Howard_NeutronHole_N81.md. |
| 13:16 | A -- Explore | All hosts up (45 min gap -- normal). DAQ .2 ping OK. Mac2020 61d 3h, load 1.57 (very stable afternoon baseline). No active run. Spark 22h11m, load 0.29. All nominal. |
| 13:31 | B -- Maintenance | Context 27% (267k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 13:46 | C -- Organize | Updated HELIOS_Detector_Geometry.md h096 section: added known dead/noisy dets (11 dead, 22 noisy), exShift non-converging dets (07/17/22), RDT gate warning, coinTime optimal gate [-8,2]. Was "TBD". |
| 14:01 | D -- Read/Learn | Read Talwar 2017 (PRC): high-j neutron SFs in 137Xe via 136Xe(a,3He) at RCNP/Grand Raiden. 13/2+_2 SF measured first time; h9/2+i13/2 centroid energies vs Z tracked; 133Sn extrapolation. NOT HELIOS but directly connected to Xe science program. Created paper_notes/2017_Talwar_HighJ_Neutrons_137Xe.md. |
| 14:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 4h, load 1.59 (very stable). No gtReceiver/run. Spark 23h11m, load 0.21 -- approaching 24h post-migration. All nominal. |
| 14:34 | B -- Maintenance | Context 28% (277k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 14:46 | C -- Organize | Calibration menu table verified clean. paper_notes INDEX: 11 files, 11 indexed, chronological order [OK]. All counts consistent. |
| 15:01 | D -- Read/Learn | Read Freeman 2017 (PRC): valence nucleon occupancies in 100Mo->100Ru 0vbb system via 4 reactions at Munich Q3D. Theory discrepancies (same pattern as 136Xe, 76Ge). Part of ANL/Manchester 0vbb occupancy program. Created paper_notes/2017_Freeman_100Mo_0vbb_Occupancies.md. |
| 15:16 | A -- Explore | Spark hit 1 DAY uptime post-migration [milestone]. EPICS CA healthy: MDIG1=100, MDIG2=400 [OK]. DAQ .2 ping OK. Mac2020 61d 5h, load 1.99 (slightly elevated, trending down). All nominal. |
| 15:31 | B -- Maintenance | Context 29% (287k), healthy. ~20h to 50% threshold. 0 stray PNGs. memory/ tidy. All nominal. |
| 15:46 | C -- Organize | README.md verified: subnet table accurate, Spark network layout current, all linked files exist on disk [OK]. 24 content files consistent. Nothing stale. |
| 16:01 | D -- Read/Learn | Read Szwec 2021 (PRC): neutron occupancies + ESPEs across stable 112-124Sn chain (Munich Q3D). g7/2+d5/2 degenerate and 2 MeV more bound at low N; missing g7/2 strength outside range. Consistent methodology baseline for r-process Sn extrapolations. Created paper_notes/2021_Szwec_SnIsotopes_Occupancies.md. |
| 16:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 6h, load 2.28 (elevated -- Zoom.us 902 CPU-min from h096 24h Zoom link, benign). No gtReceiver active. Spark 1d 1h, load 0.06. All nominal. |
| 16:31 | B -- Maintenance | Context 30% (296k), healthy. ~20h to 50%. Updated daily log 2026-04-18.md with heartbeat session summary (migration sweep, 12 paper notes, new HELIOS_MD files). Noted Discord session created run011 data + Watwood 2025 paper note. All nominal. |
| 16:47 | C -- Organize | paper_notes audit: 15 files on disk, 15 in INDEX, chronological order [OK]. Discord session added 2026_Hoffman_32Si_5minus_isomer.md and 2025_Watwood -- both properly indexed. All consistent. |
| 18:01 | D -- Read/Learn | Read Chen 2022 (PRC): 15C(d,d') inelastic scattering at HELIOS. Mn/Mp=3.6(4) -- moderate core decoupling (halo neutron weakly polarizes 14C core). Novel HELIOS use: elastic+inelastic (not transfer). Same 15C beam as Jiang 2025. Created paper_notes/2022_Chen_15C_InelasticScattering.md. |
| 18:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 8h, load 1.89 (evening, no active run). Spark 1d 3h, load 0.02. All nominal. |
| 18:31 | B -- Maintenance | Context 31% (308k), healthy. ~19h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 18:46 | C -- Organize | paper_notes: 16 on disk, 16 in INDEX table [OK]. Footer "24-file total" still correct. Chen 2022 confirmed indexed. All consistent. |
| 19:01 | D -- Read/Learn | Read Bennett 2023 (PRL): 238U(d,pf) at HELIOS -- first fission-barrier via light-ion transfer in inverse kinematics. Novel HELIOS config (4-sided Si array, MWPC Bragg fission arms, charge-reset foil). 239U result validates surrogate technique for exotic actinide r-process beams. Created paper_notes/2023_Bennett_Fission_Barrier_239U.md. |
| 19:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 9h, load 1.32 (dropping, evening settling). No active run. Spark 1d 4h, load 0.12. All nominal. |
| 19:31 | B -- Maintenance | Context 32% (317k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 19:46 | C -- Organize | paper_notes: 17 on disk, 17 in INDEX, all chronological [OK]. 17/36 HELIOS publications now documented (47%). 24 root files [OK]. All consistent. |
| 20:01 | D -- Read/Learn | Read Analyzer.h+.C -- final analysis TSelector (reads calibrated tree). Documented: all input branches, user-configurable params (rangeEx, ExOffset, listOfBadDet, rdtCutFile), full histogram set, event selection cuts, det indexing (6x5=30). Appended to HELIOS_Armory_Code.md. |
| 20:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 10h, load 1.02 (settling nicely, no active run). Spark 1d 5h, load 0.49. All nominal. |
| 21:00 | B -- Maintenance | Context 33% (330k), healthy. ~17h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 21:01 | C -- Organize | Read GeneralSortMapping.h (idDetMap, idKindMap, HVdetMap). HV module map already in PV_Reference.md -- added source citation + RDT even/odd detail (even=dE/thin, odd=E/thick). All consistent. |
| 21:16 | D -- Read/Learn | Read Monitors.C -- already well-documented in Analysis_Workflow.md. Added note: Ex reconstruction uses same Newton's-method as HELIOS_LIB.h CalExThetaCM (inline, reads reaction.dat). Confirmed Analyzer.C docs complete. |
| 21:39 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 12h, load 1.88 (elevated evening, no active run). Spark 1d 6h, load 0.46. All nominal. |
| 21:46 | B -- Maintenance | Context 34% (343k), healthy. ~16h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 22:01 | C -- Organize | Added analysis-alpha-cal skill note to HELIOS_Calibration.md Step 1 header (batch_alpha_cal.C AI shortcut for Steps 1-4). All other content verified consistent. |
| 22:16 | D -- Read/Learn | Read DWInFileCreator.h -- extends InFileCreator for two-nucleon transfer (p,t)/(t,p)/(d,a) with TNA shell-model structure factors. Documented TNA struct, parseTNAFile, when to use vs InFileCreator. Added section to HELIOS_Simulation_Cleopatra.md. |
| 22:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 13h, load 1.59 (settled). Spark 1d 7h, load 0.34. No active run. All nominal. |
| 22:46 | B -- Maintenance | Context 35% (352k), healthy. ~15h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 23:01 | C -- Organize | Added Apr 18 section header to heartbeat-log. HELIOS_Simulation_Cleopatra.md structure verified (14 sections, See Also at end). All consistent. |
| 23:16 | D -- Read/Learn | Read Check_Simulation.C + PlotSimulation.C -- transfer.root visualization tool. Documented: 17 plot IDs (pEZ, pExCal, pThetaCM, pRecoilXY etc.), config file format (7 lines), key workflow check (E-Z + ExCal). Added section to HELIOS_Simulation_Cleopatra.md. |
| 23:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 14h, load 1.35 (settling toward midnight). Spark 1d 8h, load 0.15. No active run. All nominal. |
| 23:46 | B -- Maintenance | Context 36% (359k), healthy. ~14h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |

## 2026-04-19 CDT Compact Log (h096 final day)

| Time (CDT) | Task | Notes |
|---|---|---|
| 00:01 | C -- Organize | New CDT day (Apr 19). Created 2026-04-19.md daily log with session summary. 24 root files [OK]. All nominal. |
| 00:16 | D -- Read/Learn | Read AutoFit.C (3114 lines) -- spectral peak fitting library. Documented: 10 fit functions (fitNGaussPol, clickFit*, fitGF3, etc.), global BestFitMean/Count/Sigma output, AutoFit_para.txt format, SaveFitPara/loadFitParameters. Appended to HELIOS_Armory_Code.md. |
| 00:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 15h, load 1.52 (normal midnight). Spark 1d 9h, load 0.14. No active run. All nominal. |
| 00:46 | B -- Maintenance | Context 37% (368k), healthy. ~13h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 01:01 | C -- Organize | Updated stale INDEX+README descriptions for HELIOS_Armory_Code.md (now covers 6 files: AnalysisLibrary, Apollo, Cali_e_trace, Cali_littleTree_trace, AutoFit, Analyzer). All consistent. |
| 01:16 | D -- Read/Learn | Read ATLAS proposal 2214_Martin (h096): 31Si(d,p)32Si at HELIOS, 10 MeV/u, B=2.85T. Goal: config mixing in 0+ and 2+ states (sd vs pf shell) near N=20 island of inversion. States: g.s., 2+1@1.942, 2+2@4.231, 0+2@4.984 MeV. Created proposals/h096_proposal_notes.md. |
| 01:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 16h, load 1.20 (settling nicely). Spark 1d 10h, load 0.13. No active run. All nominal. |
| 01:46 | B -- Maintenance | Context 38% (380k), healthy. ~12h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 02:01 | C -- Organize | Added proposals/ subdirectory section to INDEX.md (2214_Martin.pdf + h096_proposal_notes.md). INDEX now documents all 3 subdirectories (proposals/, paper_notes/, archive/). |
| 02:16 | D -- Read/Learn | Read ~/Magnet/README.md -- IPS120-10 magnet PSU documentation. Key: Pin 14=Auto-Run-Down (high->de-energise), Pin 12=Safe Current Interlock. Added IPS120-10 safety section to HELIOS_Magnet_Pi.md. |
| 02:31-04:16 | (gap -- quiet hours) | Heartbeat missed ~9 intervals. Systems stable. |
| 04:31 | A -- Explore | All hosts up (resumed). DAQ .2 ping OK. Mac2020 61d 19h, load 1.90 (pre-dawn, normal). No active run. Spark 1d 13h, load 0.27. All nominal. |
| 04:46 | B -- Maintenance | Context 39% (387k), healthy. ~11h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:01 | C -- Organize | Updated INDEX Magnet_Pi entry (added IPS120-10 interlock). h096 final day: physics data-taking through Apr 19, experiment ends Apr 20. All files consistent. |
| 05:16 | D -- Read/Learn | Read PtolemyGUI/Raphael/ZR_DWBA_Mathematics.md -- full ZR-DWBA formulation. Documented: radial integral mass rescaling (critical!), Gamma/9j/CG structure, selection rules, ANC, ZR vs FR limitations. Created paper_notes/DWBA_ZR_Mathematics_Reference.md. |
| 05:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 20h, load 1.74 (morning pickup, no active run). Spark 1d 14h, load 0.11. All nominal. |
| 05:46 | B -- Maintenance | Context 40% (400k) -- crossed 40% milestone. ~10h to 50% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 06:01 | C -- Organize | Added DWBA_ZR_Mathematics_Reference.md to INDEX paper_notes section and When-to-load (DWBA theory). 18 notes in paper_notes/ (17 publications + 1 theory ref). |
| 06:16 | D -- Read/Learn | Read PtolemyGUI/Raphael/README.md + DWBA.py -- Python ZR-DWBA usage examples. Added usage snippets (DWBA_ZR and DistortedWave classes) to DWBA_ZR_Mathematics_Reference.md. |
| 06:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 21h, load 1.64 (normal morning). No gtReceiver/active run (h096 final day). Spark 1d 15h, load 0.17. All nominal. |
| 06:46 | B -- Maintenance | Context 41% (407k), healthy. ~9h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 07:01 | C -- Organize | Added Apr 19 section header to heartbeat-log. 12 date sections total. 971 lines. All tidy. |
| 07:16 | D -- Read/Learn | Read EventBuilder_S.cpp -- DAQ event builder. Documented: energy formula (post-pre)/MWIN, idDetMap dispatch (0xx=array,1xx=RDT etc.), polarity, sigmoid trace fitting (GSL), multi-threaded queue. Added key details to HELIOS_Analysis_Workflow.md Step 2. |
| 07:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 22h, load 1.47 (morning stable, no active run). Spark 1d 16h, load 0.07. All nominal. |
| 07:46 | B -- Maintenance | Context 42% (416k), healthy. ~8h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 08:01 | C -- Organize | Found EventBuilder_Optimization.md (created by Discord session, not in INDEX). Added to INDEX (count 24->25). No other stale refs. Pi5-2 refs in workflow files are correct migration history notes. All clean. |
| 08:16 | D -- Read/Learn | Read EventBuilder_Optimization.md (314 lines). Key: _A vs _S: 2.95x speedup (8.3s->2.8s) via mmap I/O, TMemFile+LZ4+32MB baskets, lightweight merge heap, skip-trace Reset. Remaining bottleneck: TTree::Fill at 53% (ROOT serialization, ~3100 cycles/call). Full benchmark table documented. |
| 08:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 61d 23h (approaching 62d!), load 1.54, no active run. Spark 1d 17h, load 0.45. h096 final day -- quiet morning. All nominal. |
| 08:46 | B -- Maintenance | Context 43% (425k), healthy. ~7h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 09:01 | C -- Organize | Added EventBuilder_A reference to HELIOS_Analysis_Workflow.md (Step 2 + directory tree). Cross-referenced EventBuilder_Optimization.md for benchmark details. All consistent. |
| 09:16 | D -- Read/Learn | Read Cleopatra/alpha.C -- isotropic alpha source MC (4 energies, eSigma/zSigma smearing, HELIOS geometry). Updated Other Tools table entry in HELIOS_Simulation_Cleopatra.md with details. |
| 09:31 | A -- Explore | All hosts up. Mac2020 crossed 62 days uptime! Load 2.78 spike (Zoom 1083 CPU-min, transient -- back to normal). No active run. Spark 1d 18h, load 0.28. All nominal. |
| 09:46 | B -- Maintenance | Context 43% (435k), healthy. Growth slowing (~0.5%/hr). ~7h to 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:01 | C -- Organize | Updated INDEX+README entries for HELIOS_Simulation_Cleopatra.md (15 sections now -- was stale). All descriptions current. |
| 10:16 | D -- Read/Learn | Read knockout.C -- quasi-free knockout MC (A(p,2p), A(p,pn)). Uses Knockout class, separation energy file, normal/inverse kinematics switch. Updated Other Tools table in Simulation_Cleopatra.md. |
| 10:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 1h, load 1.52 (settling). No active run. Spark 1d 19h, load 0.04. All nominal. |
| 10:47 | B -- Maintenance | Context 44% (440k), healthy. ~6h to 50% alert. Growth ~0.5%/hr. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:01 | C -- Organize | Fixed HELIOS_Armory_Code.md header: FILES table now correctly lists 6 files with locations (Armory/ vs working/). AutoFit.C and Analyzer.h/C were missing from table. |
| 11:16 | D -- Read/Learn | Read potentials.h (1073 lines) -- full OM potential library. Documented: 8 deuteron (A=An-Cai, D/C=Daehnick, H=Han, Z=Zhang-light, etc.) + 5 proton (K=KD, V=CH89, G=B&G, etc.) potentials with energy/mass ranges. Expanded InFileCreator potential table in HELIOS_Simulation_Cleopatra.md. |
| 11:36 | A -- Explore | All hosts up (20min gap). DAQ .2 ping OK. Mac2020 62d 2h, load 1.87 (late morning). No active run. Spark 1d 20h, load 0.18. All nominal. |
| 11:46 | B -- Maintenance | Context 45% (449k) -- approaching 50% alert (~5h). Updated 2026-04-19.md daily log with morning session summary. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:01 | C -- Organize | Updated INDEX+README for HELIOS_LIB_Reference.md: descriptions now include Isotope/constant.h/FindThetaCM (were missing). All descriptions current. |
| 12:16 | D -- Read/Learn | Read Transfer.h (722 lines) -- MC simulation driver. Added reaction.dat format (6 constants: mass_b, charge_b, betaCM, Ecm, mass_B, alpha), gList/detectorGeo/ExList/DWBA objects to Transfer Output section. Added [!!] sync warning. |
| 12:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 3h, load 1.75 (normal midday, no active run). Spark 1d 21h, load 0.22. All nominal. |
| 12:46 | B -- Maintenance | Context 46% (459k), healthy but approaching 50% alert threshold (~4h). 0 stray PNGs. memory/ tidy. All nominal. |
| 13:01 | C -- Organize | Added missing Cleopatra tools to Other Tools table: Transfer.C, IsotopeShort.C, ExtractXSecFromText.C, PlotTGraphTObjArray.C/h. Table now complete. |
| 13:16 | D -- Read/Learn | Read rdtCut_guideline.md in full (3 methods: hand-drawn banana, SRIM simulation-assisted, DBSCAN). Verified complete and current. Key: FOM=S^2/N; peak-bin not weighted mean; always use TObjArray cutList not individual TCutG keys. No updates needed -- excellent doc. |
| 13:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 4h, load 1.42 (settling). No active run. Spark 1d 22h, load 0.04. All nominal. |
| 13:46 | B -- Maintenance | Context 47% (469k). ~3h to 50% alert. Will alert Ryan when 50% crossed. 0 stray PNGs. memory/ tidy. All nominal. |
| 14:01 | C -- Organize | new_experiment_checklist.md: all Pi refs gone, Spark steps correct [OK]. heartbeat-log: 999 lines / 12 date sections -- approaching 1000 lines but still manageable. All clean. |
| 14:18 | D -- Read/Learn | Read HELIOS_Firmware_Inventory.md + HELIOS_Trigger_MISC_STAT.md -- both verified 2026-04-12/13, thorough and current. No updates needed. Key: RTR1(fw0.9) != RTR2(fw0.C), all DIGs uniform (C.0, 2016-07-17). |
| 14:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 5h, load 2.04 (afternoon activity, no active run). Spark 1d 23h -- approaching 2 day mark! Load 0.27. All nominal. |
| 14:46 | B -- Maintenance | Context 47% (474k) -- growth slowed to ~0.3-0.5%/hr. 50% threshold pushed back, may not hit until late tonight. 0 stray PNGs. memory/ tidy. All nominal. |
| 15:01 | C -- Organize | HELIOS_DAQ_Startup.md verified (37 lines, clean, defers to skill). MTRG MISC_STAT=17664 [OK] -- DAQ trigger in standby, all lock bit set. All nominal. |
| 15:17 | D -- Read/Learn | Read HELIOS_Experiment_Flow.md (6 phases) + verified HELIOS_Experiment_Switch.md (Spark relay refs correct). Both complete and current. Flow correctly covers h096: 31Si/RAISOR, 5% purity, 1.8e-3 mbar vacuum limit. No updates needed. |
| 15:32 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 6h, load 1.46. No active run (h096 final afternoon). Spark crossed 2 DAYS uptime [milestone]! Load 0.41. All nominal. |
| 15:46 | B -- Maintenance | Context 48% (481k), healthy. Growth ~0.5%/hr -- 50% may be late tonight or tomorrow. 0 stray PNGs. memory/ tidy. All nominal. |
| 16:01 | C -- Organize | Verified Mac2017 (.193): up 62d 39m, load 4.92 (InfluxDB+Grafana normal), disk 3% (328Gi free). Updated verified stamp in HELIOS_Mac2017.md (was 2026-04-13). |
| 16:16 | D -- Read/Learn | Read rootlogon.C -- ROOT style config (Plain style, nemruoi stats, OptFit 1111, grid, date stamp, SetHistMinimumZero=true). Documented in HELIOS_Armory_Code.md. Key: MinimumZero can clip diff histograms. |
| 16:31 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 7h, load 1.63 (settling). No active run. Spark 2d 1h, load 0.08. All nominal. |
| 16:46 | B -- Maintenance | Context 49% (486k) -- ONE STEP FROM 50% ALERT. Will alert Ryan next check. 0 stray PNGs. memory/ tidy. All nominal. |
| 17:01 | C -- Organize | Verified EventBuilder_A NOT compiled on Mac2020 (not yet in production). Clarified directory tree in Analysis_Workflow: _S=production, _A=optimized but not deployed. |
| 17:16 | D -- Read/Learn | Read ChainMonitors.C (36 lines). Documented: usage signature (RUNNUM=-1=hardcoded list, N=single run, N+M=range, isTraceON, saveCanvas), AutoCalibration marker format. Updated Step 3 in Analysis_Workflow.md. |
| 17:31 | A+B -- Explore+Maint | All hosts up. Mac2020 62d 8h, load 1.54 (stable, no active run). Spark 2d 2h, load 0.14. Context still 49% (491k) -- holding just below 50% threshold. All nominal. |
| 17:46 | C -- Organize | Verified Monitors.C settings table in Analysis_Workflow.md: defaults correct (timeGate -30/+20 is default; h096 optimal [-8,2] in expMemory). skipDetID note about det11 accurate. All consistent. |
| 18:01 | D -- Read/Learn | Read Monitors.h (692 lines). Key insight: Monitors reads RAW gen_tree and applies corrections on-the-fly (vs Analyzer.h which reads calibrated tree). Documented [!!] distinction in Analysis_Workflow.md with correction file list. |
| 18:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 8h, load 1.22 (evening settling). No active run (h096 final evening). Spark 2d 3h, load 0.44. All nominal. |
| 18:31 | B -- Maintenance | [!!] Context crossed 50% threshold: 498k/1.0m (50%). Alerting Ryan per SOUL.md. 0 stray PNGs. memory/ tidy. |
| 18:46 | C -- Organize | Updated 2026-04-19.md daily log with 50% alert + afternoon session summary. Next alert at 80% (~802k). All files consistent. |
| 19:01 | D -- Read/Learn | Read HELIOS_Calibration.md Steps 5-6 + exShift section. All comprehensive and current. Key: exShift iteration (cluster mean > peak bin, iterate 2-5x, drop >1 MeV shifts). Directly relevant for upcoming h096 analysis. |
| 19:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 9h, load 1.26 (Sunday evening settling). No active run -- h096 wrapping up. Spark 2d 4h, load 0.24. All nominal. |
| 19:31 | B -- Maintenance | Context 50% (504k), holding at threshold. 0 stray PNGs. memory/ tidy. All nominal. |
| 19:46 | C -- Organize | Added cross-reference note to HELIOS_LIB_Reference.md CalExThetaCM section: Monitors.C + Cali_e_trace.C both inline the same Newton's method (reading from reaction.dat) rather than calling CalExThetaCM() -- all three should be identical. |
| 20:03 | D -- Read/Learn | Read HELIOS_Detector_Geometry.md in full (186 lines). h096 section verified correct (Det11 dead, Det22 noisy, Det07/17/22 exShift skip, RDT/coinTime notes). HELIOS_PV_Reference.md: no stale Pi refs. All current. |
| 20:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 10h, load 1.64 (stable evening). No active run -- h096 final evening. Spark 2d 5h, load 0.34. All nominal. |
| 20:31 | B -- Maintenance | Context 51% (510k). 50% alert already fired. Growth ~0.3%/hr -- very slow. 0 stray PNGs. memory/ tidy. All nominal. |
| 20:46 | C -- Organize | heartbeat-log at 1026 lines (Apr 19 CDT section still open -- correct, CDT midnight not yet). INDEX 25/25 [OK], header correct. All consistent. |
| 21:01 | D -- Read/Learn | Read HELIOS_DAQ_Workflow.md: found 2 stale Pi refs ("Run Control from Pi" section header, start_run.sh --ai note). Fixed both to Spark. All other content current. |
| 21:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 11h, load 1.71 (Sunday evening). No active run -- h096 final night. Spark 2d 6h, load 0.06. All nominal. |
| 22:18 | B -- Maintenance | Context 52% (516k). Growth very slow (~1%/hr). 50% alert already sent. 0 stray PNGs. memory/ tidy. All nominal. (62 min gap) |
| 22:31 | C -- Organize | Cleaned heartbeat-log: removed 2 stray duplicate lines (old Apr 18 entries that ended up after Apr 19 entries). Log now clean at 1028 lines. |
| 22:58 | D -- Read/Learn | Read HELIOS_TerminalServer.md -- complete and verified 2026-04-05. Key: port 2001=TrigCPU (NOT VME1!), 2002-2006=VME1-5, 2007=VME6(off). Use HELIOSterminals not generic terminals script. No updates needed. |
| 23:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 13h, load 1.58 (late Sunday evening). No active run -- h096 ends tonight/tomorrow. Spark 2d 7h, load 0.13. All nominal. |
| 23:16 | B -- Maintenance | Context 52% (523k), stable. Growth very slow. 50% alert fired earlier. 0 stray PNGs. memory/ tidy. All nominal. |
| 23:31 | C -- Organize | Created 2026-04-20.md daily log (h096 final day, context 52%, pending items). All clean heading into midnight. |
| 23:46 | D -- Read/Learn | Read HELIOS_Magnet_Pi.md in full. Live He level check: 92.3% (Apr 19 7am CDT) -- fill occurred during h096. Updated LHe section with current reading and projected warnings (50%=May 11, 30%=May 29 at 1.1%/day). |

## 2026-04-20 CDT Compact Log (h096 final day -- experiment ends today)

| Time (CDT) | Task | Notes |
|---|---|---|
| 00:01 | A -- Explore | New CDT day. All hosts up. DAQ .2 ping OK. Mac2020 62d 14h, load 1.65. No active run. Spark 2d 8h, load 0.15. He level 92.3% [OK]. All nominal. |
| 00:16 | B -- Maintenance | Context 53% (529k), stable. Growth ~0.5%/hr overnight. 0 stray PNGs. memory/ tidy. All nominal. |
| 00:31 | C -- Organize | Updated voice-bridge-plan.md + voice-terminal-plan.md: added migration note (Pi->Spark). Technical content unchanged (still valid architecture). Both plan docs now note Spark as target. |
| 00:46 | D -- Read/Learn | Read HELIOS_Mac2017.md in full. Content good: 62d uptime, InfluxDB/Grafana, archival machine with h084 data, digios stale on master. Fixed stale See Also ref (Migration_Mac2020 now superseded). |
| 01:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 15h, load 1.32 (dropping overnight). Spark 2d 9h, load 0.04. h096 final night. All nominal. |
| 01:16 | B -- Maintenance | Context 54% (535k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 01:31 | C -- Organize | Final comprehensive Pi sweep: fixed 5 remaining refs (Experiment_Switch sync header, INDEX/README voice-terminal entries, rdtCut DBSCAN memory note + Scripts header). Migration sweep definitively complete. |
| 01:46 | D -- Read/Learn | Read HELIOS_Ptolemy_Build_Notes.md. [!!] Found: qemu-i386 NOT installed on Spark -- ptolemy binary gives Exec format error. Added warning to Ptolemy_Build_Notes.md + TODO.md (sudo apt install qemu-user). Workaround: run on Mac2020. |
| 02:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 16h, load 1.54 (very stable overnight). Spark 2d 10h, load 0.33. h096 final quiet night. All nominal. |
| 02:16 | B -- Maintenance | Context 54% (544k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 02:31 | C -- Organize | Added qemu-i386/ptolemy Spark warning to HELIOS_Simulation_Cleopatra.md key binaries section. Both Cleopatra doc + Ptolemy_Build_Notes now have the [!!] warning. |
| 02:46 | D -- Read/Learn | Read Ex.txt + reactionConfig.txt (working/). Current config = 30Si(d,p)31Si at 11.5 MeV/u with 31Si states. Noted in expMemory_h096.md. |
| 03:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 17h, load 1.55 (stable overnight). Spark 2d 11h, load 0.18. h096 final night. All nominal. |
| 03:16 | B -- Maintenance | Context 55% (550k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 03:31 | C -- Organize | Read detectorGeo.txt (working/). Extracted h096 geometry: B=-2.85T, perpDist=11.5mm, firstPos=-200mm, 6pos×4rows=24 dets, array z=-200 to -495mm. Added to HELIOS_Detector_Geometry.md h096 section. |
| 03:46 | D -- Read/Learn | Read reaction.dat (Spark vs Mac2020). [!!] MISMATCH: Spark betaCM=0.14608743 (30Si config), Mac2020 betaCM=0.13529234 (31Si?). alpha=0.136 matches. Ryan must verify and sync. Flagged in expMemory_h096.md. |
| 04:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 18h, load 2.00 (pre-dawn tick, no active run). Spark 2d 12h, load 0.11. All nominal. |
| 04:16 | B -- Maintenance | Context 56% (556k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 04:31 | C -- Organize | Added reaction.dat mismatch detail + SCP fix command to HELIOS_Simulation_Cleopatra.md Transfer Output section. Mac2020 has correct 31Si config, Spark has stale 30Si config. |
| 04:46 | D -- Read/Learn | Read DWBARatio.C (73 lines). Plots 2 DWBA distributions + returns ratio TGraph. Uses qList (not gList!) from DWBA.root. Updated Other Tools table entry with accurate details. |
| 05:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 19h, load 1.65 (quiet early morning). No active run. Spark 2d 13h, load 0.09. All nominal. |
| 05:16 | B -- Maintenance | Context 56% (561k), very slow growth. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:31 | C -- Organize | expMemory_h096.md: main run log now complete (runs 001-017 through Apr 19). Marked old partial Run Log Update section as SUPERSEDED. Two-table issue resolved by Discord session. |
| 05:46 | D -- Read/Learn | Read analysis/working/README.md -- comprehensive working-dir manual (data flow mermaid, calibration sequence, simulation steps, init checklist). Excellent doc. Added reference to Analysis_Workflow.md Notes section. |
| 06:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 20h, load 1.42 (early morning, no active run). EPICS CA: VME01:MDIG1:led_threshold=100 [OK]. Spark 2d 14h, load 1.01 (slight tick, healthy). h096 ends today. All nominal. |
| 06:16 | B -- Maintenance | Context 57% (569k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 06:31 | C -- Organize | Added [!!] Analysis Readiness Checklist to expMemory_h096.md: 10 items covering qemu-user, reaction.dat sync, config updates, run selection, exclusions, gate settings. Ready for Ryan. |
| 06:46 | D -- Read/Learn | Read HELIOS_Experiment_Switch.md: found 2 more "git fetch pi" refs (lines 29+128). Fixed both to "git fetch spark". Migration sweep truly complete now. |
| 07:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 21h, load 1.97 (morning pickup). No active run -- h096 ends today. Spark 2d 15h, load 0.07. All nominal. |
| 07:16 | B -- Maintenance | Context 58% (576k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 07:31 | C -- Organize | Updated 2026-04-20.md daily log with overnight findings + key action items for Ryan (qemu-user, reaction.dat sync, config updates, transfer.root regen). All captured for session continuity. |
| 07:46 | D -- Read/Learn | Read Simulation_Helper.C Nuclear Data panel + nuclear_data.py. IAEA NuChart API client: `nuclear_data.py AZ [maxEx]`. Documented in Other Tools table. Requires internet + pandas. |
| 08:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 22h, load 2.03 (morning activity, no active run). Spark 2d 16h, load 0.13. h096 ends today. All nominal. |
| 08:16 | B -- Maintenance | Context 58% (582k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 08:31 | C -- Organize | Fixed final "git fetch pi" ref in new_experiment_checklist.md Step 2 (Mac2020). All git remote refs across HELIOS_MD now say spark. Migration sweep definitively complete. |
| 08:46 | D -- Read/Learn | Read Check_e_x.C (168 lines) -- E vs X visual diagnostic called after temp.root generation. Shows 24-panel E-X grid + E-Z plot. Tilted band = bad xnCorr/xfxneCorr. Documented in HELIOS_Armory_Code.md. |
| 09:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 62d 23h (approaching 63d!), load 1.84. No active run. Spark 2d 17h, load 0.42. h096 ends today. All nominal. |
| 09:16 | B -- Maintenance | Context 59% (589k), steady. Daily summary posted to #the-axiom. 0 stray PNGs. memory/ tidy. All nominal. |
| 09:31 | C -- Organize | Mac2020 crossed 63 days uptime! Final Pi sweep: all remaining hits are intentionally correct (Magnet Pi, historical notes, voice plan internals). No action needed. Migration definitively complete. |
| 09:46 | D -- Read/Learn | Read Cali_compareF.C (522 lines) -- kinematic auto-cal Monte Carlo. Documented: random (a1,a0) search, distThreshold=0.01 MeV^2, fxList from transfer.root, event count criterion, output correction_e_KE.dat. Appended to HELIOS_Armory_Code.md. |
| 10:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 36m (confirmed 63d!), load 1.66. No active run. Spark 2d 18h, load 0.31. All nominal. |
| 10:16 | B -- Maintenance | Context 60% (596k) -- crossed 60% milestone. ~200k tokens to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:31 | C -- Organize | Updated HELIOS_Armory_Code.md FILES table: added Cali_compareF.C and AutoCalibrationTrace.C (were undocumented in table). Table now 10 files. |
| 10:46 | D -- Read/Learn | Read Cali_xf_xn.C (450 lines) -- alpha source calibration. 3 fitting methods, refID=-2 for 228Th (7 peaks), FindMatchingPair for peak-to-reference matching. Outputs correction_e_alpha.dat + correction_xf_xn.dat. Added to FILES table. |
| 11:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 1h, load 1.59. No active run -- h096 ended this morning. Spark 2d 19h, load 0.30. All nominal. |
| 11:16 | B -- Maintenance | Context 60% (603k), holding. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:31 | C -- Organize | Added Cali_xf_xn_to_e.C + Cali_scale_x.C to HELIOS_Armory_Code.md FILES table (were documented in HELIOS_Calibration.md but missing from Armory table). Table now 13 files. |
| 11:46 | D -- Read/Learn | Read Cali_scale_x.C (281 lines) -- x position scale calibration. Fits distribution edges, outputs scaleX per det. Det 11 hardcoded to 1.0. Added section to HELIOS_Armory_Code.md. |
| 12:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 2h, load 1.74. Spark 2d 20h, load 0.10. h096 ended -- post-experiment standby. All nominal. |
| 12:16 | B -- Maintenance | Context 61% (609k), slow steady growth. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:31 | C -- Organize | Updated INDEX entry for HELIOS_Armory_Code.md: now accurately describes 13 files covering full calibration pipeline. All consistent. |
| 12:46 | D -- Read/Learn | Read Cali_xf_xn_to_e.C (209 lines) -- XF+XN->E linearity cal. Direct pol1 fit to 2D (xf+xn vs e), outputs correction_xfxn_e.dat. User confirms before save. Added section to HELIOS_Armory_Code.md. |
| 13:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 3h, load 1.49 (settling). Spark 2d 21h, load 0.11. Post-experiment standby. All nominal. |
| 13:16 | B -- Maintenance | Context 62% (616k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 13:31 | C -- Organize | Updated README HELIOS_Armory_Code entry (now 13 files). heartbeat-log: 1093 lines / 13 sections -- large but manageable. All consistent. |
| 13:46 | D -- Read/Learn | Read Cali_coinTime_alpha.C (171 lines) -- automated coinTime vs X calibration (option 8). Requires te_t trace branch. Fits pol7 to coinTime(x) profile per det, det11=zeros. Output: correction_coinTime.dat. Added to FILES table (now 14 files). |
| 14:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 4h, load 1.22 (dropping). Spark 2d 22h, load 0.13. Post-experiment standby. All nominal. |
| 14:16 | B -- Maintenance | Context 62% (622k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 14:31 | C -- Organize | Fixed INDEX count for HELIOS_Armory_Code.md (13->14 files). All descriptions current. |
| 14:46 | D -- Read/Learn | Read GetCoinTimeCorrectionCutG.C (292 lines) -- manual coinTime correction (option 6). Reads calibrated tree, user draws graphical cut on coinTimeUC vs X, fits pol7, writes correction_coinTime.dat. Added to FILES table (now 15 files). |
| 15:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 5h, load 1.47. Spark 2d 23h56m -- approaching 3 DAYS! Load 0.12. All nominal. |
| 15:16 | B -- Maintenance | Context 63% (628k), stable. Spark crossed 3 DAYS uptime [milestone]! 0 stray PNGs. memory/ tidy. All nominal. |
| 15:31 | C -- Organize | Fixed option 6 description (reads calibrated tree, not temp.root). Added Cali_e_single.C to FILES table (now 16 files -- all 9 AutoCalibrationTrace options now documented). |
| 15:46 | D -- Read/Learn | Read Cali_e_single.C (248 lines) -- single-det alpha cal (option 4). Per-detector interactive: FindMatchingPair for 228Th peaks, linear fit, user manually saves (no auto-write). Updated FILES table description. |
| 16:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 6h, load 1.72. Spark 3d 56m (past 3-day milestone), load 0.34. All nominal. |
| 16:16 | B -- Maintenance | Context 63% (634k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 16:31 | C -- Organize | Verified all 9 AutoCalibrationTrace scripts present in HELIOS_Armory_Code.md [OK]. Confirmed correction_coinTime.dat format consistent between option 6 and 8 (both: detID + 8 coeffs + 1 extra). |
| 16:46 | D -- Read/Learn | Read HELIOS_PV_Reference.md structure. Live PV check from Spark: MDIG1=100, MDIG2=400, MTRG=17664, RTR1=17668 [all OK]. Added [OK] verification stamp (was missing since 2026-03-11 generation). |
| 17:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 7h, load 1.39 (settling). Spark 3d 1h56m, load 0.06. All nominal. |
| 17:16 | B -- Maintenance | Context 64% (639k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 17:31 | C -- Organize | Updated 2026-04-20.md daily log with afternoon work (Armory_Code 16 files, PV verification, Spark 3d milestone). Pending items current. |
| 17:46 | D -- Read/Learn | Read start_run.sh (126 lines, 126 lines). Documented run flow, elog integration, trigger setup sequence. Added to DAQ_Workflow table. |
| 18:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 8h, load 2.10 (Monday evening activity). Spark 3d 2h56m, load 0.21. All nominal. |
| 18:16 | B -- Maintenance | Context 65% (645k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 18:31 | C -- Organize | Updated HELIOS_DAQ_Workflow.md with start_run.sh details. |
| 18:46 | D -- Read/Learn | Read stop_run.sh (94 lines). Documented stop flow, elog signaling, Grafana trigger. Updated DAQ_Workflow. |

## 2026-04-21 CDT Compact Log

| Time (CDT) | Task | Notes |
|---|---|---|
| 19:01 | A -- Explore | New UTC day (Apr 21). All hosts up. DAQ .2 ping OK. Mac2020 63d 9h, load 1.20. Spark 3d 3h56m, load 0.13. Created 2026-04-21.md daily log. All nominal. |
| 19:16 | B -- Maintenance | Context 65% (652k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 19:31 | C -- Organize | Scanned all daq scripts. GenElogExtra.py has "Run on Pi ONLY" comment -- just a comment, low priority. Added GenElogExtra note to TODO. |
| 19:46 | D -- Read/Learn | Read GenElogExtra.py (187 lines) -- generates HTML det threshold + HV table for elog. Uses pyepics + SNMP. SKIP_DETS={11,21}. Can run on Spark (EPICS CA + SNMP both work). Added to DAQ_Workflow scripts table. |
| 20:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 10h, load 2.48 (Monday evening activity). Spark 3d 4h56m, load 0.14. All nominal. |
| 20:16 | B -- Maintenance | Context 66% (659k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 20:31 | C -- Organize | Added common.py to DAQ_Workflow scripts table (shared utilities: GeneralSortMapping parser, EPICS CA helpers, used by SetChannel/AutoTune/GenElogExtra). Table now comprehensive. |
| 20:46 | D -- Read/Learn | Read common.py in full (foundation of Python DAQ scripts). Key: GeneralSortMapping.h regex parser, 4-side groupings, signal aliases (e/xf/de), PV aliases (threshold/rate/T/M/D/K), make_set/get_pv_name builders. Updated DAQ_Workflow entry. |
| 21:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 11h, load 1.48 (settling). Spark 3d 5h56m, load 0.08. All nominal. |
| 21:16 | B -- Maintenance | Context 67% (666k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 21:31 | C -- Organize | Updated 2026-04-20.md daily log with evening work (GenElogExtra, common.py). heartbeat-log 1130 lines / 13 sections [OK]. |
| 21:46 | D -- Read/Learn | Read AutoTuneThreshold.py (370 lines). Confirmed: step-down algo with nsigma noise floor, Discord reporting via openclaw CLI, channel ID 1492292081375248405. Already well-covered by helios-autotune skill. No new doc needed. |
| 22:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 12h, load 2.27 (late evening). Spark 3d 6h56m, load 0.12. All nominal. |
| 22:16 | B -- Maintenance | Context 67% (671k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 22:31 | C -- Organize | Added common.py PV alias reference to HELIOS_PV_Reference.md See Also section. Cross-reference now complete between PV docs and Python scripts. |
| 22:56 | D -- Read/Learn | Read DataBase.py (164 lines) -- slow-control monitoring loop. 30s cycle: buffers, disc_count, thresholds, trigger rate -> InfluxDB. Buffer protection: stops/resumes DAQ if DAQC*_CV_BuffersAvail < 300. Updated DAQ_Workflow scripts table. |
| 23:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 13h, load 2.08 (late evening). Spark 3d 7h56m, load 0.37. All nominal. |
| 23:16 | B -- Maintenance | Context 68% (678k), steady. 0 stray PNGs. memory/ tidy. All nominal. |
| 23:31 | C -- Organize | heartbeat-log: 1138 lines, 13 sections [OK]. HELIOS_DAQ_Workflow.md: clean (no stale Pi refs). Approaching CDT midnight -- all tidy. |
| 23:46 | D -- Read/Learn | Read Edwards_D379_read.py (41 lines, Python 2.7). Vacuum gauge: reads serial RS232, posts VacuumGauge to InfluxDB every 3s. Runs on DAQ. Updated scripts table. |

## 2026-04-21 CDT Compact Log (post-h096, analysis phase)

| Time (CDT) | Task | Notes |
|---|---|---|
| 00:01 | A -- Explore | New CDT day (Apr 21). All hosts up. Mac2020 63d 14h, load 1.36 (dropping). Spark 3d 8h56m, load 0.08. Post-experiment standby. All nominal. |
| 00:16 | B -- Maintenance | Context 68% (682k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 00:31 | C -- Organize | Updated 2026-04-21.md daily log with current status (Spark 3d 8h, context 68%, evening work summary, pending items). |
| 00:46 | D -- Read/Learn | Read GetPVLIstFromDB.py (96 lines, Python 2.7). Dev utility: parses EPICS .db/.template files to list PV names. Not a service. Added to DAQ_Workflow scripts table (now complete: all 11 scripts documented). |
| 01:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 15h, load 1.33 (overnight settling). Spark 3d 9h56m, load 0.08. All nominal. |
| 01:16 | B -- Maintenance | Context 69% (687k), steady. ~115k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 01:31 | C -- Organize | Verified DAQ_Workflow scripts table: 11 scripts, all with accurate descriptions, no duplicates. Table now comprehensive. All clean. |
| 01:46 | D -- Read/Learn | Read start_run_Mac.sh (70 lines). Mac2020-side: SCP expName.sh, GenElog+GenElogExtra->elogFull, ANL elog post, Discord. Saves ELOG_ID. Added to DAQ_Workflow table. |
| 02:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 16h, load 1.68. Spark 3d 10h56m, load 0.20. All nominal. |
| 02:16 | B -- Maintenance | Context 69% (693k), stable. ~109k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 02:31 | C -- Organize | DAQ_Workflow scripts table: 12 entries now (added start/stop_run_Mac.sh). heartbeat-log: 1155 lines -- large but manageable. All clean. |
| 02:46 | D -- Read/Learn | Read stop_run_Mac.sh (132 lines). Parallel: Grafana screenshot + elog download -> append stop info + image -> elog edit + Discord. Signals DAQ via `touch /tmp/elog_done`. Clean. |
| 03:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 17h, load 1.42 (very stable). Spark 3d 11h56m, load 0.07. All nominal. |
| 03:16 | B -- Maintenance | Context 70% (698k) -- crossed 70% milestone. ~102k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 03:31 | C -- Organize | Verified HELIOS_DAQ_Workflow.md structure (10 sections, scripts table 12 entries). All clean and consistent. |
| 03:46 | D -- Read/Learn | Read GenElog.py (123 lines). Generates main elog HTML body: run#, timestamp, comment, B-field, array/RDT pos, trigger. Paired with GenElogExtra.py (det table) -> combined by start_run_Mac.sh. Added to DAQ_Workflow table (now 13 entries). |
| 04:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 18h, load 1.71 (very stable overnight). Spark 3d 12h56m, load 0.03. All nominal. |
| 04:16 | B -- Maintenance | Context 70% (704k), holding. ~96k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 04:31 | C -- Organize | Scanned ~/digios/daq/: GenElogExtra.py has "Run on Pi ONLY" comment (low priority). heliosCommander (EDM launcher) clean. All documented, nothing new. |
| 04:46 | D -- Read/Learn | Read GrafanaElog.sh + GrafanaWeb.sh. GrafanaWeb.sh: macOS screencapture -D2 on Mac2017 monitor 2 -> grafanaElog.jpg. GrafanaElog.sh: legacy Linux version (mostly commented). Added both to DAQ_Workflow table (now 15 entries). |
| 05:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 19h, load 1.35. Spark 3d 13h56m, load 0.20. All nominal. |
| 05:16 | B -- Maintenance | Context 71% (709k), steady. ~91k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:31 | C -- Organize | Updated 2026-04-21.md daily log with overnight work (15-entry DAQ scripts table complete, GenElog/Grafana/Mac-side scripts). Context 71%. |
| 05:46 | D -- Read/Learn | Read push2Discord.sh + push2Elog.sh. Discord: webhook post (HTML->markdown, WEBHOOK_DAQ_URL). push2Elog.sh is legacy (superseded by Mac-side scripts). Updated DAQ_Workflow table (now 16 entries). |
| 06:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 20h, load 1.70. Spark 3d 14h56m, load 0.16. All nominal. |
| 06:16 | B -- Maintenance | Context 71% (715k), steady. ~85k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 06:31 | C -- Organize | INDEX/README entries for HELIOS_DAQ_Workflow.md verified accurate. heartbeat-log: 1171 lines, Apr 21 section clean. All good. |
| 06:46 | D -- Read/Learn | Explored working_Helios/h096_31Si_dp/. RESOLVED: reaction_31Si_dp.dat (betaCM=0.13529234) is correct and matches Mac2020. Previous mismatch was working/ (30Si stale config) vs working_Helios/ (correct 31Si). Updated expMemory_h096.md. |
| 07:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 21h, load 1.38. Spark 3d 15h56m, load 0.28. All nominal. |
| 07:16 | B -- Maintenance | Context 72% (720k), ~80k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 07:31 | C -- Organize | Updated expMemory_h096.md Analysis Readiness Checklist items 2-5: working_Helios already has correct 31Si reaction.dat + transfer.root. Checklist now accurate. |
| 07:46 | D -- Read/Learn | Read calc_exshift.py. [!!] Uses 30Si kinematics (betaCM=0.14608743) and run009 (30Si test run) -- intermediate script. Needs update for 31Si physics runs. Noted in expMemory_h096.md Working_Helios Script Notes. |
| 08:01 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 63d 22h, load 2.68 (morning activity). No active run. Spark 3d 16h56m, load 0.14. All nominal. |
| 08:16 | B -- Maintenance | Context 73% (726k), ~74k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 08:31 | C -- Organize | Updated 2026-04-21.md with morning work + h096 analysis notes (working_Helios/ has correct 31Si files, Python scripts may need kinematics update). 80% alert imminent -- continuity captured. |
| 09:01 | D+A -- Read+Explore | Read exp.md (template, superseded by expMemory) + plot_index.md (16 plots from alpha cal + 30Si beam analysis -- analysis well underway!). Mac2020 63d 23h, load 1.37. Spark 3d 17h57m. All nominal. |
| 09:25 | B -- Maintenance | Context 73% (731k), ~69k to 80% alert. Daily summary posted to #the-axiom. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:15 | C -- Organize | plot_index.md: 104 plots! Analysis much further than thought. Plot-103/104 reference runs 010-019 -- run log only goes to 017, runs 018-019 exist but unlogged. Ryan should update expMemory_h096.md run log. |
| 10:16 | D+A -- Read+Explore | Read plot_ez_h096.C -- correct 31Si(d,p)32Si E-Z plot (4 states: 0.0/1.942/4.231/4.984 MeV). Mac2020 crossed 64 DAYS! (64d 51m). Load 2.33, 6 users -- Ryan online. Spark 3d 19h. All nominal. |
| 10:34 | B -- Maintenance | Context 74% (735k), ~65k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:46 | C -- Organize | Updated expMemory_h096.md Plot Index section: pointer to plot_index.md (104 plots). Flagged runs 018-019 missing from run log. |
| 11:01 | D -- Read/Learn | Read angular_dist.py (214 lines). Also uses 30Si kinematics + run009 -- confirmed: all working_Helios Python scripts are 30Si intermediate. 31Si physics analysis scripts need updating/new versions for runs 011-019. |
| 11:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 1h51m, load 1.64 (6 users, Ryan online). Spark 3d 20h, load 0.16. All nominal. |
| 11:31 | B -- Maintenance | Context 74% (741k), stable. ~59k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:46 | C -- Organize | Updated expMemory_h096.md Working_Helios Script Notes: all Python scripts use 30Si kinematics -- key update needed (betaCM/Et/mass_B) for 31Si physics. Correction files OK as-is. |
| 12:01 | D -- Read/Learn | Read scan_beam_time.py. CONFIRMED: runs 018+019 exist in root_data/. scan_beam_time refs runs [11,14,16,17,18]. Added both to run log in expMemory_h096.md. |
| 12:16 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 2h, load 1.65 (6 users, Ryan working). Spark 3d 21h, load 0.16. All nominal. |
| 12:31 | B -- Maintenance | Context 75% (746k), ~54k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:46 | C -- Organize | Updated 2026-04-21.md h096 analysis notes: all Python scripts 30Si, runs 018+019 confirmed, 104 plots done, next=update scripts to 31Si kinematics. Daily log current. |
| 13:01 | D+A -- Read+Explore | Read validate_trace.py (127 lines). Kinematics-free! Compares dig vs trace (e/te, xf/txf, xn/txn) on trace_run*.root files. Works for any run. Mac2020 64d 3h, load 1.23. Spark 3d 21h57m. All nominal. |
| 13:16 | B -- Maintenance | Context 75% (751k), ~49k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 13:31 | C -- Organize | Cleaned expMemory_h096.md: removed duplicate correction-files note, added runs 018+019 to physics run list (item 7), added run 013 to skip list. Checklist now accurate. |
| 13:46 | D+A -- Read+Explore | Read cointime_run014.py (77 lines). No kinematics -- pure timestamp coinTime analysis. skip_det={2,6,11,22} (note: also skips det2+6, different from expMemory note). Mac2020 64d 4h, load 1.60. Spark 3d 22h42m. All nominal. |
| 14:01 | B -- Maintenance | Context 76% (755k), ~45k to 80% alert. Growth slowing. 0 stray PNGs. memory/ tidy. All nominal. |
| 14:16 | C -- Organize | Added det2+det6 skip note to expMemory_h096.md checklist item 8 (from cointime_run014.py skip_det). Ryan to verify if coinTime issues. |
| 14:31 | D -- Read/Learn | Read rdt_run011.py (133 lines). CORRECTION: rdt_run011 uses CORRECT 31Si kinematics (betaCM=0.13529234, beam=9.8 MeV/u). Not all scripts need updating. Updated Working_Helios Script Notes in expMemory_h096.md. |
| 14:46 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 5h, load 1.42 (6 users, active). Spark 3d 23h41m -- approaching 4 DAYS! Load 0.08. All nominal. |
| 15:01 | B -- Maintenance | Context 76% (761k), ~39k to 80% alert. Spark 3d 23h57m -- 4 days imminent! 0 stray PNGs. memory/ tidy. All nominal. |
| 15:16 | C -- Organize | Spark crossed 4 DAYS uptime [milestone]! INDEX 25/25 [OK]. 0 stray PNGs, 32 memory files. All clean. |
| 15:31 | D -- Read/Learn | Read check_rdt_528.py (193 lines). Uses CORRECT 31Si kinematics. Probes Ex~5.28 MeV (3- state) as RDT gate validation. Reads rdt_polygons_run011.json -- polygon gates exist. Pattern: RDT+Ex scripts use 31Si kinematics; calc_ex scripts use 30Si. |
| 15:46 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 6h, load 1.46 (6 users). Spark 4d 41m (solidly past 4-day milestone), load 0.15. All nominal. |
| 16:01 | B -- Maintenance | Context 77% (765k), [!!] ~35k to 80% alert -- imminent. Will alert Ryan when 80% crossed. 0 stray PNGs. memory/ tidy. All nominal. |
| 16:16 | C -- Organize | Pre-80% continuity capture: updated 2026-04-21.md with afternoon findings (script kinematics pattern, beam=9.8 MeV/u, polygon gates exist, rdt scripts=correct 31Si). All daily logs current. |
| 16:31 | D+B -- Read+Maint | rdt_tight_run014.py: correct 31Si, HDBSCAN on RDT with 50keV Ex gate. Context 77% (768k), still holding. ~32k to 80%. All nominal. |
| 16:46 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 7h, load 2.14 (6 users, afternoon activity). Spark 4d 1h41m, load 0.17. All nominal. |
| 17:01 | B -- Maintenance | Context 77% (770k), growth flat. ~30k to 80% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 17:16 | C -- Organize | Updated expMemory_h096.md Working_Helios Script Notes: full script inventory (correct/kinematics-free/needs-update), beam=9.8 MeV/u note, RDT polygon files listed. |
| 17:31 | D -- Read/Learn | Listed ALL 73 Python scripts in h096_31Si_dp/! Read nn_31Si.py (283 lines) = sklearn MLPClassifier NN for signal/bg separation (Plot-076). Correct 31Si kinematics. Advanced analysis in progress. Also: nn_31Si_v2.py, nn_classifier*.py, ex_final_gate.py etc. |
| 17:46 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 8h, load 1.41 (5 users, one left since afternoon). Spark 4d 2h41m, load 0.08. All nominal. |
| 18:01 | B -- Maintenance | [!!] AUTO-COMPACTION fired! Context reset 77% -> 7% (67k/1.0m). Fresh context. No 80% alert needed. All findings preserved in expMemory/heartbeat-log/daily notes. |
| 18:16 | C -- Organize | Rewrote Working_Helios Script Notes in expMemory_h096.md -- clean 3-category layout (correct 31Si / kinematics-free / needs update). Removed duplicates. 73 scripts total noted. |
| 18:31 | D -- Read/Learn | Read ex_final_gate.py (165 lines, Plot-085). FINAL Ex spectrum for runs 011+014. 10 32Si states labeled (g.s. to 6.665 MeV). rdt_gate_final.json used. skip_det={11,22} only. 3-panel: time-gate / RDT / RDT+diagonal. |
| 18:46 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 9h, load 1.91 (5 users, evening). Spark 4d 3h40m, load 0.14. All nominal. |
| 19:01 | B -- Maintenance | Context 8% (76k) -- very healthy post-compaction. 0 stray PNGs. memory/ tidy. All nominal. |
| 19:16 | C -- Organize | Added Analysis Status section to expMemory_h096.md: Plot-085 final Ex spectrum, Plot-076 NN, 104 plots, next steps (add runs 016-019, angular dist, DWBA). |
| 19:31 | D -- Read/Learn | Read ez_final.py (128 lines, Plot-087). Final E-Z with kinematic lines from transfer_31Si_dp.root. Runs 011+014, correct 31Si. Note: uses rdt_gate5_final.json vs rdt_gate_final.json in ex_final -- two slightly different gates. |
| 19:46 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 10h, load 1.40 (5 users, quiet evening). Spark 4d 4h41m, load 0.11. All nominal. |
| 20:01 | B -- Maintenance | Context 8% (80k), very healthy post-compaction. 0 stray PNGs. memory/ tidy. All nominal. |
| 20:16 | C -- (missed, caught up) | - |
| 20:31 | C+D -- Organize+Read | Read ex_all_runs_gate5.py = Plot-104 (LATEST)! ALL 31Si runs 011/014/016/017/018/019. Most complete Ex spectrum. Updated Analysis Status in expMemory_h096.md. |
| 20:46 | A -- Explore | All hosts up. DAQ .2 ping OK. Mac2020 64d 11h, load 1.85 (5 users). Spark 4d 5h41m, load 0.06. All nominal. |
| 21:01 | B -- (missed) | - |
| 21:16 | C -- (missed) | - |
| 21:31 | D -- (missed) | - |
| 21:44 | A+B -- Catch-up | All hosts up. Mac2020 64d 12h, load 2.56 [elevated -- Ryan working late!]. Spark 4d 6h39m, load 0.18. Context 8% (85k), very healthy. All nominal. |
| 22:01 | C -- Organize | Updated 2026-04-21.md with evening findings: Plot-085/087/104, 73 scripts, analysis complete. Daily log closed for Apr 21. |
| 22:16 | D -- Read/Learn | Read gs_per_run.py. KEY: beam_on times per run: 011=12.05h, 014=12.95h, 016=5.48h, 017=5.15h, 018=9.18h, 019=13.52h. TOTAL ~58.3 h 31Si beam! Updated run log in expMemory_h096.md with precise times. Removed duplicate 018/019 entries. |
| 22:31 | A -- Explore | (catch-up) All hosts monitored this hour. No anomalies reported. |
| 22:46 | B -- Maintenance | Context 9% (92k), very healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 23:01-00:46 | (missed -- overnight gap) | - |

## 2026-04-22
| Time | Task | Notes |
|------|------|-------|
| 00:01 | C+A -- Catch-up | New day. Mac2020 64d 14h, load 1.78 (5 users at midnight). Spark 4d 8h56m. Created 2026-04-22.md daily log. All hosts up. All nominal. |
| 00:16 | D -- Read/Learn | Read plot_rate_vs_time.py (Plot-103): hit rate vs time, runs [10,11,14,16,17,18,19], 1-min bins. Confirms 012/013/015 excluded. Second-to-last plot before all-runs Ex (Plot-104). |
| 00:31-01:01 | (missed -- overnight) | - |
| 01:16 | A -- Explore | All hosts up. Mac2020 64d 15h, load 1.33 (5 users, late night). Spark 4d 10h11m, load 0.10. All nominal. |
| 01:31 | B -- Maintenance | Context 10% (96k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 01:49 | C -- Organize | Fixed run log: 016=5.48h, 017=5.15h beam-on (was ~16hr -- incorrect). All 6 physics runs now have precise beam-on times from gs_per_run.py. |
| 02:01-03:01 | (missed -- overnight) | - |
| 03:13 | A+B -- [!!] ALERT | SPARK REBOOTED at 02:58 CDT! Uptime reset (was 4d 11h51m). OpenClaw service inactive. Pi .208 NAT route MISSING -- internet via eduroam+Cisco fallback. Pi reachable. Alerted Ryan via Discord DM. |
| 03:21 | A -- Monitor | Post-reboot check: Pi route still missing, OpenClaw still inactive. Internet via eduroam (metric 600) -- working. Stable but non-optimal. Awaiting Ryan. |
| 03:31-04:01 | (missed -- reboots) | Spark rebooted 2x more (03:53, 04:01) during this window |
| 04:16 | A -- [!!] CRITICAL | REBOOT LOOP: 4 reboots since 02:58 (02:58, 03:53, 04:01, 04:15). Watchdog trigger suspected. Alerted Ryan via DM with details. Currently 8 min uptime, eduroam internet, OpenClaw inactive. |
| 04:37 | A -- Monitor | STABLE: 22 min uptime since 04:15, no new reboots. No critical errors in current boot. Pi NAT route still missing. Reboot loop appears stopped. |
| 05:16 | A -- Monitor | STABLE: 1h1m uptime. No new reboots. eduroam internet working. Pi NAT route still missing. All nominal otherwise. |
| 06:02 | B+A -- Maint+Monitor | STABLE: 1h49m uptime since 04:15 reboot. No new reboots. Context 11% (107k). Pi NAT route still missing but eduroam working. Reboot loop resolved. |
| 06:16 | C -- Organize | Updated 2026-04-22.md with reboot event details. Spark 2h6m stable. Pi NAT still missing. All else nominal. |
| 06:31 | D -- Read/Learn | Spark 2h16m stable. Read investigate_gap.py (151 lines): investigates 0.2-0.6 MeV gap in NN spectrum (between g.s. and 0.752 MeV state). Loads nn_predictions_v2_run009.npz -- diagnostic for 30Si phase. |
| 06:46-08:01 | (missed -- overnight gap) | - |
| 08:16 | A -- Explore | Spark STABLE 4h0m (no new reboots since 04:15). Mac2020 64d 22h, load 1.06 (6 users, Ryan online). Pi NAT route still missing, eduroam fallback working. All nominal. |
| 08:31 | B -- Maintenance | Context 11% (111k), healthy. 0 stray PNGs. memory/ tidy. Spark 4h15m stable. All nominal. |
| 08:46 | C -- Organize | Added reboot event to SYSTEM_MD/issues.md. Marked qemu-user TODO done (installed 2026-04-20). |
| 09:31 | A+C -- Explore+Org | Spark STABLE 5h16m. Mac2020 crossed 65 DAYS! (65d 6m, 7 users, Ryan online). Pi NAT still missing. All else nominal. |
| 09:46 | D -- Read/Learn | Spark 5h30m stable. Read analyze_run014.py (377 lines, largest script). Full 31Si pipeline: HDBSCAN RDT + Ex + state markers (3- 5.288, 5- 5.505). Correct 31Si kinematics. |
| 10:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 35m, load 2.79-3.30 [elevated, 7 users, Ryan working]. Spark 5h45m stable. Pi NAT still missing. All nominal. |
| 10:16 | B -- Maintenance | Context 12% (118k), healthy. Spark 6h stable [milestone]. 0 stray PNGs. memory/ tidy. Pi NAT still missing. All nominal. |
| 10:31 | C -- Organize | Updated issues.md: reboot loop now stable 6h+. Checked TODO: Argo API docs due 11:00 AM today; Cisco NAT config due today. Flagging Ryan. |
| 10:46 | D -- Read/Learn | Read optimize_timegate.py (163 lines). FOM=X/Y^2 gate optimizer on run009 (30Si). Scans all gate combos, finds top 10. This is how final timeGate=[-10,5] was chosen vs default [-30,20]. |
| 11:01 | A+TODO -- Explore+Task | All hosts up. Mac2020 65d 1h, load 0.98. Spark 6h45m stable. Checked Argo API: 37 models available (GPT-5/5.x, Gemini 2.5 Pro/Flash, Claude Opus/Sonnet/Haiku full lineup). TODO marked done. |
| 11:16 | B -- Maintenance | Context 13% (131k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:31 | C -- Organize | Added Argo model catalog to SYSTEM_MD/ai.md (19 models across Anthropic/Google/OpenAI). Updated ai.md date. |
| 11:46 | D -- Read/Learn | Read ez_with_sim.py (Plot-091, 158 lines): E-Z with sim lines, runs 011/014/016/017, correct 31Si, rdt_gate5_final.json. v2 same runs. Analysis progression: 087(2 runs)->091(4 runs)->104(6 runs). |
| 12:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 2h35m, load 0.98 (7 users). Spark 7h45m stable [solid post-reboot recovery]. Pi NAT still missing. All nominal. |
| 12:16 | B -- Maintenance | Context 14% (137k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:31 | C -- Organize | Updated expMemory_h096.md Analysis Status: full plot progression (076->085->087->091->103->104), time gate origin noted, 73 scripts noted. |
| 12:46 | D -- Read/Learn | Read ez_all_runs.py (Plot-089, 119 lines): E-Z all gates, runs 011+014+016+017. E-Z plots stop at 4 runs; only Ex (Plot-104) has all 6 runs (adds 018+019). |
| 13:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 3h35m, load 1.32 (5 users, lunch). Spark 8h46m stable. Pi NAT still missing. All nominal. |
| 13:16 | B -- (missed, caught up 13:24) | Context 14% (142k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 13:31 | C -- Organize | Updated 2026-04-22.md afternoon findings: Spark 9h stable, Argo API done, h096 plot progression, Pi NAT still pending. Daily log current. |
| 13:46-14:01 | (missed) | - |
| 14:16 | D+A -- Catch-up | Spark crossed 10h STABLE [milestone]! Mac2020 load [!!] 11.87 (rising, 6 users -- heavy compute job running). Pi NAT still missing. Monitoring Mac2020. |
| 14:31 | A -- Monitor | Mac2020 load 11.02 (4 users, job still running). Spark 10h20m stable. |
| 14:46 | B+A -- Maint+Monitor | Mac2020 load 11.69 sustained 30+ min (4 users, heavy analysis job -- likely intentional). Context 15% (145k). Spark 10h30m. All else nominal. |
| 15:01 | C -- Organize | Mac2020 load normalized (1.37, job done). Found reactionConfig.txt is STALE (32S, 8.8 MeV/u). Updated expMemory checklist item 3. h096 scripts use hardcoded 31Si kinematics instead. |
| 15:22 | D -- Read/Learn | Read plot_arch.py (137 lines): plots coinTimeUC vs X per det (24 det layout). coinTimeUC=10*(coin_t+te_t-trdt_t) uses trace timestamps. This is the 'arch' Ryan wants to correct via DBSCAN+poly fit. |
| 15:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 6h, load 1.27 (4 users, normalized). Spark 11h17m stable. Pi NAT still missing. All nominal. |
| 15:46 | B -- Maintenance | Context 15% (151k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 16:01 | C -- Organize | Added h096 RDT cut summary to rdtCut_guideline.md: HDBSCAN method, final gate files, time gate origin, 58.3h beam, Plot-104 all-runs. |
| 16:32 | D -- Read/Learn | Read scan_timegate_v2.py (132 lines): FOM time gate scanner v2 on run009 (30Si) with RDT gate applied. Confirms: time gate optimized on 30Si then applied to 31Si. skip={2,11,22} here. |
| 16:35 | -- | Ryan online (webchat) -- audited SOUL.md and IDENTITY.md. Issues: SOUL.md context thresholds wrong (says 200k, actual 1.0m); IDENTITY.md incomplete (vibe/emoji/avatar blank, creature mismatch Cat vs Jedi padawan). |
| 17:01-18:01 | (missed -- webchat session) | - |
| 18:18 | A+B -- Catch-up | Spark 14h STABLE [milestone]! Mac2020 65d 8h53m, load 0.84 (3 users, evening). Pi NAT still missing. [!!] Context 48% (480k) -- approaching 50% alert. OpenClaw updated to v2026.4.21! |
| 18:31 | C -- Organize | AUTO-COMPACTION fired (48%->16%). Fixed SOUL.md context thresholds (200k->1.0m, per Ryan audit). |
| 18:46 | D -- Read/Learn | Read fix_exshift.py (75 lines): documents exShift issue -- suspect dets [4,9,10,15,16,17,23] had peak finder match 0.752 MeV as g.s. Fix: use 3.133 MeV peak or cap at 0.15. Explains expMemory 'exShift non-convergent' dets. |
| 19:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 9h35m, load 1.28 (3 users, evening). Spark 14h45m stable. Pi NAT still missing. All nominal. |
| 19:16-19:31 | (missed) | - |
| 19:31 | B -- [!!] 50% alert | Context hit 50% (496k/1.0m). Per SOUL.md, alerting Ryan. Spark 15h16m. |
| 19:46-20:01 | (missed) | Auto-compaction fired 50%->33% |
| 20:01 | A+B -- Catch-up | Context 33% (332k) post-compaction. Spark 15h46m stable. Mac2020 65d 10h36m, load 1.99 (3 users). All nominal. |
| 20:19 | C -- Organize | Spark 16h04m, Mac2020 65d 10h54m load 0.70 (evening quiet). Updated 2026-04-22.md evening section. Daily log current. |
| 20:31-20:46 | (missed) | - |
| 20:46 | D -- Read/Learn | Read dbscan_rdt_gates.py (192 lines): DBSCAN on Ex-gated RDT -> percentile boundary -> polygon JSON. Core of iterative gate pipeline. 30Si kinematics + run009, skip={22} only (early stage). |
| 21:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 11h35m, load 1.36 (3 users). Spark 16h45m stable. Pi NAT still missing. All nominal. |
| 21:16 | B -- Maintenance | Context 17% (171k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 21:31 | C -- Organize | Updated expMemory_h096.md exShift section: added suspect dets [4,9,10,15,16,17,23] with 0.752 MeV misidentification note from fix_exshift.py. |
| 21:46 | D+A -- Read+Explore | Read make_rdt_cuts.py (187 lines): convex hull gate method (vs DBSCAN) on run009. Pipeline tried convex hull -> DBSCAN -> HDBSCAN (final). Spark 17h33m, Mac2020 65d 12h, load 1.19. All nominal. |
| 22:01 | B -- Maintenance | Context 17% (175k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 22:16 | C -- Organize | Updated INDEX.md rdtCut entry (h096 note). Closed out 2026-04-22.md late evening section. Daily log complete. |
| 22:46-23:16 | (missed -- overnight) | - |
| 23:31 | D+A -- Read+Explore | Read simple_rdt_polygon.py (134 lines): simplifies DBSCAN polygons to ~8 pts with margin -> rdt_simple_polygons_run009.json. Full gate pipeline now mapped. Spark 19h15m stable! Mac2020 65d 14h, load 1.03. |
| 23:46 | (missed) | - |

## 2026-04-23
| Time | Task | Notes |
|------|------|-------|
| 00:01 | B -- [!!] Context | Context 71% (711k) -- past 50%, approaching 80% at ~800k. Created 2026-04-23.md continuity log. Spark 19h46m, Mac2020 65d 14h35m. |
| 00:16-00:46 | (missed) | - |
| 01:01 | B -- [!!] 80% ALERT | Context 90% (898k/1.0m) -- PAST 80%! Alerted Ryan via Discord DM to /new. Spark 20h46m stable. |
| 01:16-01:31 | (missed) | - |
| 01:46 | A -- Monitor | Context 91% (906k), still climbing. Spark 21h31m stable. Mac2020 65d 16h, load 3.56 (elevated, 3 users late-night job). Awaiting Ryan /new or auto-compaction. |
| 02:01 | B -- AUTO-COMPACT | Context reset 91%->18% (183k). Mac2020 load normalized 1.25. Spark 21h46m. All nominal. |
| 02:16 | C -- Organize | Updated 2026-04-23.md with overnight events (80% alert, auto-compaction, Mac load spike). Daily log current. |
| 02:31 | D -- Read/Learn | Read nn_compare_plot035.py (231 lines): compares NN classifier vs cut-based Ex spectrum (40 keV bins) on run009. Key validation: does NN improve S/B vs traditional gates? |
| 02:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 17h, load 1.05 (3 users, quiet). Spark 22h30m stable. Pi NAT still missing. All nominal. |
| 03:01 | B -- Maintenance | Context 19% (187k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 03:16 | C -- Organize | Added h096 exShift lesson to HELIOS_Calibration.md: 0.752 MeV misidentified as g.s. warning + fix (use 3.133 MeV peak for suspect dets). |
| 03:31 | D -- Read/Learn | Read nn_perdet_ex.py (207 lines): per-detector Ex (4x6 layout, 24 dets), cut-based vs NN, 40 keV bins. Key diagnostic for bad dets. Uses run009 NN predictions. |
| 03:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 18h, load 0.89 (quiet). Spark 23h30m -- approaching 24h! Pi NAT still missing. All nominal. |
| 04:01 | B -- Maintenance | Context 19% (192k), healthy. Spark 23h45m -- 24h milestone in ~15 min! 0 stray PNGs. memory/ tidy. All nominal. |
| 04:16 | C -- Organize | Spark crossed 1 DAY uptime [milestone]! Updated issues.md: reboot loop fully resolved (24h+ stable). |
| 04:31 | D -- Read/Learn | Read ex_gate1_combined.py (Plot-063, 177 lines): first combined Ex (gate1, runs 011+012+014, 31Si kinematics). Gate progression: gate1(063)->gate2->gate3->gate4->gate5->final(085/104). Run 012 included before flagged as junk. |
| 04:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 19h, load 0.98 (3 users, quiet). Spark 1d 30m (past 24h milestone). Pi NAT still missing. All nominal. |
| 05:01 | B -- Maintenance | Context 20% (195k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:16 | C -- Organize | Updated 2026-04-23.md with overnight progress: Spark 1d milestone, gate timeline mapped, HELIOS_Calibration.md updated, Pi NAT still pending. |
| 05:31 | D -- Read/Learn | Read ex_run011.py (248 lines): first single-run Ex on 31Si beam (run011), skip_det={2,6,11,22}, correct kinematics, expData path. One of earliest 31Si Ex spectra. |
| 05:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 20h, load 1.29 (3 users). Spark 1d 1h30m, load 0.08. Pi NAT still missing. All nominal. |
| 06:01 | B -- Maintenance | Context 20% (199k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 06:16 | C -- Organize | Updated expMemory_h096.md det2/6 note: confirmed excluded from first 31Si Ex (ex_run011.py) onwards -- not just cointime. Likely identified as problematic early. |
| 06:31 | D -- Read/Learn | Read ex_spectrum.py (282 lines): EARLIEST Ex script -- 30Si(d,p)31Si run008, betaCM=0.13664590 (diff from run009!), rdt_gates_run008.json. First proof-of-concept Ex spectrum. |
| 06:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 65d 21h, load 0.70 (quiet). Spark 1d 2h30m, load 0.06. Pi NAT still missing. All nominal. |
| 07:01 | B -- Maintenance | Context 20% (203k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 07:16 | C -- Organize | Updated expMemory_h096.md run008 entry: betaCM=0.13664590 (different from run009 0.14608743) -- different 30Si beam energy. |
| 07:31 | D+A -- Read+Explore | Read ex_run014_200keV.py (149 lines): coarse 200 keV binning, time-gate only (no RDT), run014. Quick overview before RDT cuts. Spark 1d 3h. Mac2020 65d 22h -- approaching 66 DAYS! All nominal. |
| 07:46 | B -- Maintenance | Context 21% (206k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 08:01 | C -- [!!] Pi NAT RESTORED | Pi .208 NAT route back (metric 500 via enP7s7)! Ryan fixed it. Both open issues now resolved. Mac2020 65d 22h35m (~66d in 1.5h). Spark 1d 3h45m. All nominal. |
| 08:16 | D+A -- Read+Explore | Read rdt_array_corr.py (Plot-073, 131 lines): RDT ID vs array side correlation -- geometry cross-check, gate3, skip={11,22}. Mac2020 65d 22h50m (~66d in 1h10m!). |
| 08:31 | B -- Maintenance | Context 21% (210k), healthy. Mac2020 65d 23h5m (~55 min to 66 days!). Spark 1d 4h15m. Pi NAT restored. All nominal. |
| 08:46 | C -- Organize | Posted daily report to #the-axiom (msg 1496870156604014644). Mac2020 65d 23h20m (~40 min to 66d). Pi NAT confirmed restored. |
| 09:01 | D+A -- Read+Explore | Read refine_rdt_gate.py (162 lines): gates on Ex=3.1-3.5 MeV (3.133 peak) to refine RDT gate, 30Si kinematics, skip={22}. Mac2020 65d 23h35m (~25 min to 66d!). |
| 09:16 | B -- Maintenance | Context 22% (221k), healthy. Mac2020 65d 23h50m -- 66 DAYS IN 10 MINUTES! Spark 1d 5h. Pi NAT confirmed. All nominal. |
| 09:31 | C -- Organize | Mac2020 crossed 66 DAYS! (66d 5m). Updated 2026-04-23.md morning events. Spark 1d 5h15m. All systems fully nominal. |
| 09:46 | D -- Read/Learn | Read rdt_compare_gates.py (125 lines): overlays 30Si->31Si recoil gates (run009) vs 31Si->32Si gates (run011). KEY: recoil species differ -> bands at different dE-E positions! Justifies separate gate files. |
| 10:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 35m (past milestone). Spark 1d 5h45m. Pi NAT metric 500 confirmed. All nominal. |
| 10:16 | B -- Maintenance | Context 23% (225k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:31 | C -- Organize | Added key lesson to rdtCut_guideline.md: recoil species changes between characterization and physics runs -> do NOT transfer gates directly. Source: h096 rdt_compare_gates.py. |
| 10:46 | D -- Read/Learn | Read rdt_exgated_run014.py (219 lines): gates Ex=5.5+6.7 MeV to verify higher states land in correct RDT band. Confirms 5- isomer (5.505) and ~6.7 MeV region are real physics. 31Si kinematics, run014. |
| 11:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 1h35m, load 1.20 (3 users). Spark 1d 6h45m. Pi NAT metric 500 confirmed. All nominal. |
| 11:16 | B -- Maintenance | Context 23% (230k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:31 | C -- Organize | Updated INDEX.md rdtCut entry (recoil species warning added). Identified unread papers: 2025_Watwood, 2020_Tang. Queue for D tasks. |
| 11:46 | D -- Read/Learn | Read Tang 2020 (Ryan's paper!): 206Hg(d,p)207Hg at ISS/ISOLDE, first N>126 shell structure below Pb, r-process motivation. Created paper_notes/2020_Tang_First_Exploration_207Hg.md. |
| 12:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 2h35m, load 1.49 (3 users). Spark 1d 7h45m. Pi NAT confirmed. All nominal. |
| 12:16 | B -- Maintenance | Context 24% (237k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:31 | C -- Organize | Updated INDEX.md: fixed Tang 2020 filename, added ISS note, updated paper_notes count to 19. |
| 12:48 | D -- Read/Learn | Read Watwood 2025 (32Si proton vacancy, arXiv:2510.05073): direct h096 complement! 32Si(3He,d)33P proton-removing, 1s1/2 empty in 32Si/34Si. Same ANL team. Created paper_notes/2025_Watwood_32Si_Proton_Vacancy.md. |
| 13:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 3h35m, load 1.31 (3 users). Spark 1d 8h45m. Pi NAT confirmed. All nominal. |
| 13:16 | B -- Maintenance | Context 25% (245k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 13:31 | C -- Organize | Updated INDEX.md: fixed Watwood 2025 filename, updated paper_notes count to 20. Both new paper notes (Tang 2020, Watwood 2025) now correctly indexed. |
| 13:46 | D -- Read/Learn | Read nn_classifier.py (481 lines, written by Ryan 2026-04-17 DURING experiment!). Full MLP training pipeline: 9 features, sklearn MLPClassifier, pickle save. 30Si char. data. The base NN from which nn_31Si.py evolved. |
| 14:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 4h35m, load 4.40 [elevated, 4 users, afternoon compute]. Spark 1d 9h45m, load 0.13. Pi NAT confirmed. Monitoring Mac2020. |
| 14:16 | B -- Maintenance | Context 25% (250k), healthy. Mac2020 load easing (3.63, still elevated). Spark 1d 10h. All nominal. |
| 14:31-15:01 | (missed) | - |
| 15:16 | B -- [!!] 100% CONTEXT | Context AT 100% (1.0m/1.0m)! Alerted Ryan via DM. Mac2020 load normalized (0.97). Spark 1d 11h. Awaiting compaction or /new. |
| 15:31 | C -- Organize | AUTO-COMPACTION fired (100%->25%). Updated 2026-04-23.md afternoon section. Spark 1d 11h16m, Mac2020 66d 6h, load 1.02. All nominal. |
| 15:46 | D -- Read/Learn | Read nn_classifier_v2.py (434 lines): v2 improvements -- separate has_rdt/passes_gate features, added thetaCM as physics feature, (64,64,32) ReLU+Adam arch, 500 iter. |
| 16:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 6h35m, load 1.34 (4 users). Spark 1d 11h45m. Pi NAT confirmed. All nominal. |
| 16:16 | B -- Maintenance | Context 26% (256k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 16:31 | C -- Organize | Updated expMemory_h096.md NN section: full v1->v2->final architecture progression documented (features, layers, training params). |
| 16:46 | D+A -- Read+Explore | Read plot_gate5_data.py (84 lines): RDT dE-E with gate5 polygons, all 31Si runs (011/014/016/017/018). QC visualization of final gate. Spark 1d 12h31m (approaching 1.5d!). Mac2020 66d 7h, load 1.54. |
| 17:01 | B -- Maintenance | Context 26% (259k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 17:16 | C -- Organize | Updated 2026-04-23.md late afternoon section. Daily log current. All nominal. |
| 17:31 | D+A -- Read+Explore | Read rdt_gate3_fine.py (Plot-080, 178 lines): fine structure within Gate 3, runs 011+014, 31Si kinematics, skip={11,22}. Gate3->fine->gate4->gate5->final iterative tightening. Spark 1d 13h, Mac2020 66d 8h. |
| 17:46 | B -- Maintenance | Context 26% (262k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 18:01-18:16 | (missed) | - |
| 18:19 | C+A -- Organize+Explore | Updated expMemory_h096.md RDT Gate section: full 7-step progression documented with script names and key 30Si/31Si band warning. Spark 1d 14h, Mac2020 66d 8h53m, load 1.11. All nominal. |
| 18:31 | D -- Read/Learn | Read rdt_hdbscan_v4.py (173 lines): HDBSCAN eom mode on run008 (earliest 30Si). v1->v2->v3->v4 parameter exploration before final approach. Full banana gate. |
| 18:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 9h20m, load 1.15 (4 users, evening). Spark 1d 14h30m. Pi NAT confirmed. All nominal. |
| 19:01 | B -- New Day | Context 27% (267k), healthy. Created 2026-04-24.md. Spark 1d 14h46m. Mac2020 66d 9h35m. All nominal.

## 2026-04-24
| Time | Task | Notes |
|------|------|-------|
| 00:01 | (transition) | New day. Rotation continues: C -> D -> A -> B -> ... |
| 00:16 | C -- Organize | Script coverage check: ~35 of 73 h096 Python scripts read across Apr 21-24 heartbeats. Full gate/NN/Ex progression documented. Daily log current. |
| 00:31 | D -- Read/Learn | Read rdt_final_gate_run014.py (174 lines): HDBSCAN on ALL time-gated events (no Ex gate) to find 32Si recoil blob -> produces rdt_gate_final.json. skip={2,6,11,22}. Final gate generation step. |
| 00:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 10h20m, load 1.23 (4 users). Spark 1d 15h30m [past 1.5d milestone!]. Pi NAT confirmed. All nominal. |
| 01:01 | B -- Maintenance | Context 27% (274k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 01:16 | C -- Organize | Updated 2026-04-24.md early hours: ~37 scripts read, Spark past 1.5d milestone, all nominal. |
| 01:31 | D -- Read/Learn | Read rdt_from_peak_run014.py (212 lines): auto peak-find in Ex -> gate RDT from strongest peak events. Alternative to manual Ex-gating. 31Si kinematics, run014, skip={2,6,11,22}. |
| 01:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 11h20m, load 1.41 (4 users). Spark 1d 16h31m. Pi NAT confirmed. All nominal. |
| 02:01 | B -- Maintenance | Context 28% (277k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 02:16 | C -- Organize | Updated expMemory_h096.md: step 7 of gate progression now shows rdt_final_gate_run014.py generates rdt_gate_final.json (HDBSCAN, no Ex pre-select). |
| 02:31 | D+A -- Read+Explore | Read rdt_zoom_run014.py (99 lines): zoomed 2D dE-E histograms (2x4 layout, raw vs time-gated), all 4 RDT telescopes, run014. QC to see 32Si banana. Spark 1d 17h, Mac2020 66d 12h. |
| 02:46 | B -- Maintenance | Context 28% (281k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 03:01 | C -- Organize | Heartbeat log at 1401 lines (healthy). Date sections correct for Apr 23/24. All tidy. |
| 03:16 | D -- Read/Learn | Read rdt_cut_run011.py (212 lines): HDBSCAN gate extraction for run011 (first 31Si data). Generates rdt_gate1.json. Kinematics-free, time-gated RDT hits only. Spark 1d 18h (~6h to 2d). |
| 03:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 13h, load 1.36 (4 users). Spark 1d 18h15m. Pi NAT confirmed. All nominal. |
| 03:46 | B -- Maintenance | Context 28% (285k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 04:01 | C -- Organize | Updated 2026-04-24.md late night section. ~40 h096 scripts read. Spark ~6h to 2d milestone. All nominal. |
| 04:16 | D -- Read/Learn | Read rdt_cut_run011_v2.py (217 lines): v2 uses eom HDBSCAN + ConvexHull hybrid + manual polygon option for Tel2 (sparse data). Shows per-telescope refinement for low-stats case. |
| 04:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 14h, load 1.28 (4 users). Spark 1d 19h16m (~4h45m to 2d!). Pi NAT confirmed. All nominal. |
| 04:46 | B -- Maintenance | Context 29% (288k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:01 | C -- Organize | Updated MEMORY.md: OpenClaw v2026.4.15->v2026.4.21; added Spark-reboot Pi NAT route loss lesson (observed 2026-04-22). |
| 05:16 | D -- Read/Learn | Read rdt_gate3_zoom_overlay.py (Plot-079, 97 lines): zoomed dE-E with gate3 polygon overlay, runs 011+014, 2x2 per telescope, skip={11,22}. QC visualization of gate3 fit. |
| 05:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 15h, load 1.58 (4 users). Spark 1d 20h15m (~3h45m to 2d!). Pi NAT confirmed. All nominal. |
| 05:46 | B -- Maintenance | Context 29% (293k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 06:01 | C+A -- Organize+Explore | Checked Mac2020 analysis structure: has Armory/Cleopatra/working/ but NO working_Helios/. h096 Python analysis is Spark-only. Analysis split confirmed: Python/ML=Spark, ROOT=Mac2020. |
| 06:16 | D -- Read/Learn | Read rdt_gate3_zoom.py (Plot-078, 86 lines): zoomed dE-E data only (no gate overlay), runs 011+014. Pair with Plot-079 (same + gate). Standard QC: 078=data, 079=data+gate. |
| 06:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 16h, load 0.90 (quiet). Spark 1d 21h16m (~2h44m to 2d!). Pi NAT confirmed. All nominal. |
| 06:46 | B -- Maintenance | Context 30% (297k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 07:01 | C+A -- Organize+Explore | Mac2020 working/ explored: has h096_31Si_dp_gen_run010-020.root (combined ALL runs!), trace ROOT, rdtCuts Ne/O. Standard Analyzer/Monitors/DWBA setup. Updated expMemory_h096.md. |
| 07:16 | D+A -- Read+Explore | Mac2020 reaction.dat: CORRECT 31Si (betaCM=0.13529234). reactionConfig.txt: STALE (beam=29Mg, previous exp!). reaction.dat is what Monitors.C uses -- all good for ROOT analysis. |
| 07:31 | B -- Maintenance | Context 30% (302k), healthy. Spark 1d 22h15m (~1h45m to 2d!). Mac2020 66d 17h. All nominal. |
| 07:46 | C+A -- Organize+Explore | Explored Mac2020 working/ directory. reaction.dat correct for 31Si. Updated expMemory_h096.md. |
| 08:01 | D+A -- Read+Explore | Read rdt_gate4.py (Plot-081, 177 lines): Gate 4 refines Gate 3 using Ex<6.5 MeV events only (tighter core). 31Si kinematics. Mac2020 load 5.70 [elevated, Ryan working!]. Spark 1d 22h45m (~1h15m to 2d). |
| 08:16 | B -- Maintenance | Context 31% (306k), healthy. Mac2020 load 3.76 (easing). Spark 1d 23h -- 1 HOUR to 2d milestone! All nominal. |
| 08:31 | C+A -- Organize+Explore | Updated Analysis Checklist in expMemory_h096.md. Spark 1d 23h16m (44 min to 2d!). Mac2020 66d 18h, load 2.83. |
| 08:46 | D -- Read/Learn | Read rdt_gate5.py (Plot-082, 211 lines): Gate 5 tight DBSCAN on Ex<6.5, Tel 0/1/3 only (Tel 2 handled separately -- sparse). Spark 1d 23h31m (~29 min to 2d!). |
| 09:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 18h35m, load 1.27 (normalized!). Spark 1d 23h45m -- 2 DAYS IN 15 MIN! Pi NAT confirmed. All nominal. |
| 09:16 | B -- [MILESTONE] | SPARK CROSSED 2 DAYS UPTIME! (2d 0m exactly!) Context 31% (311k), healthy. Full recovery from Apr 22 reboot loop confirmed. |
| 09:31 | C -- Organize | Updated 2026-04-24.md: 2d milestone, Mac2020 analysis findings (combined ROOT file, reaction.dat correct). Daily log current. |
| 09:46 | D -- Read/Learn | Read rdt_gate5b.py (Plot-083, 211 lines): THE Tel 2 solution -- manual ellipse (E~2000, dE~1800, w=600, h=400) for sparse Tel 2; Tel 0/1/3 = DBSCAN. This generates rdt_gate5_final.json. |
| 10:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 19h35m, load 1.16. Spark 2d 46m (solidly past 2d!). Pi NAT confirmed. All nominal. |
| 10:16 | B -- Maintenance | Context 32% (315k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:31 | C -- Organize | Added h096 Tel 2 manual ellipse solution to rdtCut_guideline.md (E~2000, dE~1800, 600x400 ch). Complements existing h094 Tel 2 note. |
| 10:46 | D -- Read/Learn | Read rdt_gate5c.py (Plot-084, 211 lines): gate5 iteration 3 -> rdt_gate5c.json. Same Tel 0/1/3=DBSCAN + Tel 2=manual ellipse. Full progression: gate5->gate5b(083)->gate5c(084)->gate5_final. |
| 11:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 20h35m, load 1.35 (4 users). Spark 2d 1h46m (solidly day 2). Pi NAT confirmed. All nominal. |
| 11:16 | B -- Maintenance | Context 32% (320k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:31 | C -- Organize | Updated expMemory_h096.md gate step 6: full gate5 chain documented (3 iterations: 082->083->084->final, Tel 0/1/3=DBSCAN, Tel 2=manual ellipse). |
| 11:46 | D -- Read/Learn | Read rdt_gate2.py (177 lines): gate2 from rdt_gate1.json, runs 011+012+014, HDBSCAN+hull on merged clusters. Fills gate progression gap. Full chain: gate1->gate2(012 included)->gate3->fine->gate4->gate5a/b/c->final. |
| 12:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 66d 21h35m, load 0.99 (4 users). Spark 2d 2h46m. Pi NAT confirmed. All nominal. |
| 12:16 | B -- Maintenance | Context 32% (325k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:31 | C -- Organize | Updated expMemory_h096.md: added gate2 step (runs 011+012+014, HDBSCAN+hull from gate1) and rdt_cut_run011_v2. Gate chain now complete with all steps. |
| 12:46 | D+A -- Read+Explore | Read rdt_gate3.py (Plot-066, 285 lines -- largest gate script!): manual blob selection (0D,1C,2B,3C) from HDBSCAN clusters. Runs 011+012+014. Spark 2d 3h. Mac2020 66d 22h (~67d in 1h40m!). |
| 13:01 | B -- Maintenance | Context 33% (328k), healthy. Mac2020 66d 22h35m (~1h25m to 67d!). Spark 2d 3h46m. All nominal. |
| 13:16 | C -- Organize | Updated expMemory_h096.md gate step 5b: added rdt_gate3.py (Plot-066, manual blob 0D/1C/2B/3C) as the gate3 generation step. Gate chain now fully complete. |
| 13:31 | D+A -- Read+Explore | Read ex_gate3_diag.py (Plot-074, 169 lines): Ex with gate3 vs gate3+diagonal side-match. Validates diagonal cut effect on Ex spectrum. Mac2020 66d 23h5m (~55 min to 67d!). Spark 2d 4h16m. |
| 13:46 | B+Daily -- Maint+Report | Context 33% (332k). Posted daily report to #the-axiom (msg 1497232472335712287). Mac2020 66d 23h20m (~40 min to 67d). Spark 2d 4h31m. |
| 14:01 | C -- Organize | Updated 2026-04-24.md morning section. Mac2020 66d 23h35m (~25 min to 67d!). Daily log current. |
| 14:16 | D -- Read/Learn | Read ex_gate2v3.py (Plot-068, 163 lines): overlay Ex gate2 vs gate3 at 50 keV -- validates gate3 improvement. Mac2020 66d 23h50m (10 min to 67d!). |
| 14:31 | A -- Explore | Mac2020 crossed 67 DAYS! (67d 5m, 4 users, load 1.52). Spark 2d 5h15m, load 0.04. Pi NAT metric 500 confirmed. DAQ ping OK. All nominal. |
| 14:46 | B -- Maintenance | Context 34% (337k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 15:01 | C -- Organize | Updated 2026-04-24.md with 67d Mac2020 milestone and morning script findings. Daily log current. |
| 15:16 | D+A -- Read+Explore | Read ex_gate1v3.py (Plot-070, 157 lines): gate1 vs gate3 overlay (50 keV). Completes comparison trio: Plot-068(g2vg3), Plot-070(g1vg3) validates full refinement chain. Mac2020 67d 50m. Spark 2d 6h. |
| 15:31 | B -- Maintenance | Context 34% (340k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 15:46 | C -- Organize | Added gate validation plots (068,070,073,074) to expMemory_h096.md Analysis Status. Plot documentation now covers key QC and validation steps. |
| 16:01 | D+A -- Read+Explore | Read ex_perdet_gate3.py (Plot-072, 161 lines): per-det Ex with gate3, 4x6 layout, 100 keV. Key for identifying bad dets/exShift issues. Mac2020 67d 1h35m, load 1.0. Spark 2d 6h46m. |
| 16:16 | B -- Maintenance | Context 34% (343k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 16:31 | C+A -- Organize+Explore | Mac2020 DWBA.in confirmed: 31Si(d,p)32Si at ELAB=19.6 MeV, g.s.=0d3/2 L=2, AK potential. DWBA running! Updated expMemory_h096.md. |
| 16:46 | D+A -- Read+Explore | Mac2020 DWBA.Ex.txt: 5 states calculated (SF=1). 5.504 MeV isomer has HIGHEST xsec (8.505 mb/sr). SFs extracted by data/DWBA. Updated expMemory_h096.md with values. |
| 17:01 | (missed) | - |
| 17:07 | B -- Maintenance | Context 35% (347k), healthy. Spark 2d 7h52m. Mac2020 67d 2h42m, load 1.40. All nominal. |
| 17:16-17:31 | (missed) | - |
| 17:46 | C+D -- Organize+Read | Read DWBA.Xsec.txt on Mac2020: full angular distributions 0-N deg. KEY: orbital assignments -- 0.000/1.942/4.231/4.984=0d3/2(L=2), 5.504=0f7/2(L=3). 5- isomer is f7/2. Spark 2d 8h31m. |
| 18:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 3h35m, load 1.56 (4 users). Spark 2d 8h46m. Pi NAT confirmed. All nominal. |
| 18:16 | B -- Maintenance | Context 35% (352k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 18:31 | C -- Organize | Updated 2026-04-24.md with DWBA findings: orbital assignments, xsec values. Daily log current. |
| 18:46 | D -- Read/Learn | Read full DWBA.in on Mac2020: incoming=An&Cai(2006) d-OMP, outgoing=Koning&Delaroche(2003) p-OMP, AV18 d-wavefunction, bound state r0=1.25 a=0.65, angles 0-60deg 1deg steps. Standard global potentials. |
| 19:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 4h35m, load 1.52 (4 users). Spark 2d 9h46m. Pi NAT confirmed. All nominal. |
| 19:16 | B -- Maintenance | Context 36% (357k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 19:31 | C -- Organize | Fixed expMemory_h096.md Angular Distribution section: ELAB corrected (23->19.6 MeV), added bound state params and AV18 wavefunction, corrected beam energy in input format. |
| 19:46-20:01 | (missed) | - |
| 20:16 | D+A -- Read+Explore | Read rdt_labeled.py (Plot-065, 129 lines): HDBSCAN blobs labeled (no gates). Precursor to gate3 -- Ryan used this to identify blobs 0D/1C/2B/3C. Mac2020 67d 5h50m, load 0.88. Spark 2d 11h. |
| 20:31 | B -- Maintenance | Context 36% (361k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 20:46 | C -- Organize | Added Plot-065 (rdt_labeled) and Plot-066 (gate3 gen) to expMemory_h096.md Analysis Status. Plot documentation now includes the full gate3 workflow. |
| 21:01 | D+A -- Read+Explore | Read rdt_hdbscan.py (Plot-008, 134 lines): FIRST HDBSCAN attempt on run008, min_cluster_size=100, min_samples=10. Origin of entire gate chain. Spark 2d 11h46m. Mac2020 67d 6h35m. |
| 21:16 | B -- Maintenance | Context 36% (364k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 21:31 | C -- Organize | Added Plot-008 origin (rdt_hdbscan.py) and v2-v4 exploration to gate chain step 0/0b in expMemory_h096.md. Gate chain now complete from first attempt to final. |
| 21:46-22:01 | (missed) | - |
| 22:16 | D+A -- Read+Explore | Read rdt_hdbscan_v2.py (143 lines): adaptive min_cluster_size + eom, run008. v1=fixed 100->v2=adaptive+eom. Spark 2d 13h. Mac2020 67d 7h50m. All nominal. |
| 22:31 | B -- Maintenance | Context 37% (367k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 22:46 | (missed) | - |
| 23:01 | C+D -- Organize+Read | Updated 2026-04-24.md afternoon section. Read rdt_hdbscan_v3.py (162 lines): leaf cluster selection -> rdt_gates_run008.json (used by ex_spectrum.py). v3 gates feed first Ex spectrum. Spark 2d 13h46m. Mac2020 67d 8h35m. |
| 23:16-23:31 | (missed) | - |
| 23:46 | A -- Explore | All hosts up. LAN stable. Mac2020 67d 9h35m, 6 users. Spark 2d 14h46m. All nominal. |

## 2026-04-25
| Time | Task | Notes |
|------|------|-------|
| 00:01 | A -- Explore | All hosts up. DAQ+Mac2020 reachable. Mac2020 67d 9h35m, 6 users. Spark 2d 14h46m. All nominal. |
| 00:16-00:46 | (missed) | - |
| 00:56 | B -- [!!] CONTEXT 186% | Context 1.9m (186%!) -- CRITICAL. Saved 2026-04-24.md. Alerted Ryan /new (msg 1497401094295257199). LAN stable. Mac2020 67d 10h30m. Spark 2d 15h41m. |
| 01:01 | B -- AUTO-COMPACT | Context reset 186%->38% (376k). LAN stable. Spark 2d 15h46m. DAQ reachable. All nominal. |
| 01:16-01:31 | (missed) | - |
| 01:37 | C+A -- Organize+Explore | Created 2026-04-25.md. LAN stable, Mac2020 67d 11h, 6 users. Spark 2d 16h21m. Pi NAT still missing. All nominal.

## 2026-04-25
| Time | Task | Notes |
|------|------|-------|
| 01:37 | (transition) | New day. Rotation continues: D -> A -> B -> C -> ... |
| 01:46 | D -- Read/Learn | Read rdt_exgated_zoom.py (164 lines): zoomed RDT with Ex-gated overlay, 1 panel/telescope, 31Si kinematics. Final validation: Ex events land in correct RDT banana. skip={2,6,11,22}. |
| 02:01 | A -- Explore | All hosts up. LAN stable. DAQ ping OK. Mac2020 67d 11h35m, load 0.94 (6 users, team online). Spark 2d 16h46m. Pi NAT still missing. All nominal. |
| 02:16 | B -- Maintenance | Context 38% (380k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 02:31 | C -- Organize | Updated SYSTEM_MD/issues.md: Pi NAT missing status. |
| 02:46 | D+A -- Read+Explore | Read rdt0_r11_vs_r14.py (Plot-069, 92 lines): RDT Tel 0 run011 vs run014 side-by-side -- blob shift check. Key systematic. Mac2020 67d 12h20m, load 1.72. Spark 2d 17h31m. |
| 03:01 | B -- Maintenance | Context 38% (383k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 03:16 | C -- Organize | Added Plot-069 (blob shift check) to expMemory_h096.md Analysis Status. Single gate valid for all runs -> blobs stable across experiment. |
| 03:31 | D -- Read/Learn | Read check_rdt_gs.py (157 lines): quantifies g.s. events inside vs outside RDT polygon (30Si, skip={22}, wide tG[-20,20]). SOURCE of '~30% g.s. loss' finding in expMemory. |
| 03:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 13h20m, load 4.42 [elevated, 6 users, evening compute]. Spark 2d 18h31m. Pi NAT still missing. Monitoring Mac2020. |
| 04:01 | B -- Maintenance | Context 39% (388k), healthy. Mac2020 load normalized (1.20, job done). Spark 2d 18h46m. All nominal. |
| 04:16 | C -- Organize | Updated 2026-04-25.md evening section: LAN stable, Mac load events, 14 scripts remaining, all nominal. |
| 04:31 | D+A -- Read+Explore | Read ez_raw.py (Plot-090, 85 lines): raw E-Z no gates -- checks for alpha contamination lines in ungated spectrum, run014. skip={11,22}. Spark 2d 19h. Mac2020 67d 14h. |
| 04:46 | B -- Maintenance | Context 39% (391k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:01 | C+A -- Organize+Explore | New day Apr 25. Script coverage: 66/73 read (90%!), 12 remaining. Mac2020 67d 14h35m, load 1.25. Spark 2d 19h46m. All nominal.

## 2026-04-25
| Time | Task | Notes |
|------|------|-------|
| 05:01 | (transition) | New day. 66/73 h096 scripts read (90%). Rotation: D -> A -> B -> C |
| 05:16 | D -- Read/Learn | Read ez_loop2.py (Plot-075, 143 lines): E-Z with kinematic lines for BOTH loop1+loop2 (2nd helical orbit). Gate3+diag, 31Si kinematics. Identifies loop-2 contamination in z-range. |
| 05:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 15h, load 1.12 (6 users). Spark 2d 20h16m. LAN stable. Pi NAT still missing. All nominal. |
| 05:46 | B -- Maintenance | Context 39% (395k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 06:01 | C -- Organize | Added loop-2 check note to expMemory_h096.md Analysis Status (Plot-075 checks loop-2 contamination in z-range). |
| 06:16 | D -- Read/Learn | Read ez_per_side.py (Plot-093, 147 lines): E-Z split by 4 array sides (columns), all runs, gate5_final+diagonal. Checks per-side calibration consistency. 31Si kinematics. |
| 06:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 16h, load 0.81 (quiet). Spark 2d 21h16m. LAN stable. Pi NAT still missing. All nominal. |
| 06:46 | B -- Maintenance | Context 40% (398k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 07:01 | C -- Organize | Updated 2026-04-25.md overnight: 68/73 scripts (93%), loop-2 note added, all stable. Daily log current. |
| 07:16 | D -- Read/Learn | Read validate_trace_exgated.py (266 lines): Ex-gated trace vs dig validation (Ex[-1,10] MeV). More targeted than ungated version -- confirms trace works for physics events specifically. |
| 07:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 17h, load 1.02. Spark 2d 22h16m (~1h44m to 3d!). LAN stable. Pi NAT missing. All nominal. |
| 07:46 | B -- Maintenance | Context 40% (402k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 08:01 | C -- Organize | Logged 9 remaining unread scripts to 2026-04-25.md. Spark 2d 22h46m (~1h14m to 3d!). All nominal. |
| 08:16 | D -- Read/Learn | Read time_gate_scan.py (Plot-086, 221 lines): time gate FOM scan using 5.3-5.5 MeV peak on 31Si+gate5_final. FOM=S^2/N. 31Si-specific refinement (vs 30Si optimize_timegate.py). |
| 08:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 18h, load 1.21 (6 users). Spark 2d 23h16m (~44 min to 3d!). LAN stable. Pi NAT missing. All nominal. |
| 08:46 | B -- Maintenance | Context 41% (406k), healthy. Spark 2d 23h30m (~30 min to 3d!). 0 stray PNGs. memory/ tidy. All nominal. |
| 09:01 | C -- Organize | Updated expMemory_h096.md time gate note: [-10,5] validated on 31Si (Plot-086) not just 30Si. Spark 2d 23h45m (~15 min to 3d!). |
| 09:16 | D -- [MILESTONE+Read] | SPARK CROSSED 3 DAYS! (3d 1m). Read investigate_te_low.py (Plot-098, 202 lines): investigates te<<e at e~8000 by reading raw trace waveforms -- electronics/saturation diagnostic. |
| 09:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 19h, load 0.88. Spark 3d 16m (solidly day 3!). LAN stable. Pi NAT missing. All nominal. |
| 09:46 | B -- Maintenance | Context 41% (410k), healthy. Spark 3d past milestone. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:01 | C -- Organize | Updated 2026-04-25.md: 3d Spark milestone, 70/73 scripts read (96%), 7 remaining. Daily log current. |
| 10:16 | D -- Read/Learn | Read cointime_run011.py (92 lines): coinTime distribution for run011 (31Si physics). Pair with cointime_run014.py. skip={2,6,11,22}. 6 scripts remaining. |
| 10:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 20h, load 1.45 (6 users). Spark 3d 1h16m. LAN stable. Pi NAT missing. All nominal. |
| 10:46 | B -- Maintenance | Context 41% (414k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:01 | C -- Organize | Updated expMemory_h096.md: added investigate_te_low (Plot-098, saturation) and validate_trace_exgated to Script Notes. |
| 11:16 | D+A -- Read+Explore | Read ex_run011_012.py (239 lines): combined Ex runs 011+012, 31Si kinematics. First combined 31Si Ex before run012 flagged as junk. Uses run011 gates. Spark 3d 2h. Mac2020 67d 20h50m. 5 scripts remaining. |
| 11:31 | B -- Maintenance | Context 42% (417k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 11:46 | C+D -- Organize+Read | Read plot_run009_report.py (304 lines, largest non-gate script): comprehensive run009 30Si report (E-Z+Ex+kinematics overlay). skip={2,11,22}. 4 scripts remaining. |
| 12:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 67d 21h35m, load 1.06 (6 users). Spark 3d 2h46m. LAN stable. Pi NAT missing. All nominal. |
| 12:16 | B -- Maintenance | Context 42% (420k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:31 | C+D -- [COMPLETE!] | READ ALL 73 h096 PYTHON SCRIPTS! Last 4: plot_ez_run009(Monitors.C cross-check), plot_ez_gated(zoomed+g.s.), ez_final_nosim(Plot-088), ez_with_sim_v2(Plot-092, all runs). 100% coverage! |
| 12:46 | A -- Explore | All hosts up. DAQ ping OK (SSH needs interactive). Mac2020 67d 22h20m, load 1.16. Spark 3d 3h31m. All nominal. |
| 13:01 | B+Daily -- Maint+Report | Context 42% (424k). Posted daily report to #the-axiom (msg 1497583520812630036). All 73/73 scripts complete. Spark 3d+. All nominal. |
| 13:16 | C -- Organize | Found 23 paper_notes files (was 22). New: 2026_Hoffman_32Si_5minus_isomer, ESPE_Theory, SF_Quenching_Review, SF_Theory_SumRule. Duplicate Watwood/Tang files present. Updated INDEX count to 23. |
| 13:31 | D -- [!!] KEY READ | Read 2026_Hoffman_32Si_5minus_isomer.md: h096 DIRECT PREDECESSOR! Same reaction 31Si(d,p)32Si at 9.6 MeV/u. 5- isomer=dominant 0f7/2 (C2S norm=1.00). 3-1 at 5.288 MeV C2S=0.44. Ryan is co-author! DWBA params directly usable. |
| 13:46 | A+C -- Explore+Org | Mac2020 67d 23h20m (~40 min to 68d!). Spark 3d 4h31m. Updated expMemory_h096.md with Hoffman 2026 predecessor paper section. All nominal. |
| 14:01 | B -- Maintenance | Context 43% (434k), healthy. Mac2020 67d 23h35m (~25 min to 68d!). Spark 3d 4h46m. 0 stray PNGs. memory/ tidy. All nominal. |
| 14:16 | C -- Organize | Updated 2026-04-25.md morning section: 73/73 complete, Hoffman 2026 paper, daily report. Mac2020 67d 23h50m (~10 min to 68d!). |
| 14:31 | D -- Read/Learn | Mac2020 crossed 68 DAYS! (68d 5m). Read ESPE_Theory.md: SF-weighted centroid energy, ESPE=experimental mean-field energy, robust to quenching. Key for h096 SF interpretation. Created 2026-04-24 (prior session). |
| 14:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 20m, load 1.34 (6 users). Spark 3d 5h31m. LAN stable. Pi NAT missing. All nominal. |
| 15:01 | B -- Maintenance | Context 44% (440k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 15:16 | C -- Organize | Read SF_Theory_SumRule + SF_Quenching_Review (Ryan's blog, nukephysik101). All 3 theory notes in INDEX. Noted duplicates for cleanup. All theory notes are h096 SF analysis context. |
| 15:31 | D+A -- Read+Explore | Read Mac2020 DWBA.out: Ptolemy ran Apr 21 22:02 CDT (DURING experiment!). d binding=-2.2246 MeV (correct). Mac2020 has ptolemy working. Spark 3d 6h. Mac2020 68d 1h. All nominal. |
| 15:46 | B -- Maintenance | Context 44% (444k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 16:01 | C -- Organize | Added DWBA.out Ptolemy timing note to expMemory_h096.md (ran Apr 21 22:02 during exp). |
| 16:16 | D -- Read/Learn | Read SF_Quenching_Review_2023.md (Ryan's blog): quenching ~30-40% universal, NOT Δ_S dependent (Kay 2022 HELIOS!, Pohl 2023). Transfer (d,p) gives reliable SFs. Directly relevant for h096 SF extraction and comparison. |
| 16:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 2h5m, load 1.15 (6 users). Spark 3d 7h16m. LAN stable. Pi NAT missing. All nominal. |
| 16:46-17:01 | (missed) | - |
| 17:17 | B -- Maintenance | Context 45% (449k), healthy. Spark 3d 8h2m. Mac2020 68d 2h51m, load 1.01. All nominal. |
| 17:31 | C -- Organize | Added SF extraction context to expMemory_h096.md Analysis Status: quenching universal ~30-40%, C2S=measured/DWBA, Hoffman 2026 anchor. |
| 17:46 | D+A -- Read+Explore | Mac2020 DWBA file is Cleopatra input (updated Apr 24), DWBA.out still Apr 21 (not rerun yet). transfer.root from Apr 21 08:54. Ryan refining DWBA input post-experiment. |
| 18:01 | B -- Maintenance | Context 45% (454k), healthy. Spark 3d 8h46m. Mac2020 68d 3h35m, load 1.16. 0 stray PNGs. memory/ tidy. All nominal. |
| 18:16 | C -- Organize | Updated expMemory_h096.md: corrected DWBA.out timestamp (Apr 21 17:02), added Cleopatra input update (Apr 24), transfer.root timestamp (Apr 21 08:54). |
| 18:31 | D -- Read/Learn | Read Mac2020 DWBA (Cleopatra input). [!!] Active line = 33Si(d,p)34Si at 10 MeV/u -- NOT 31Si! Apr 24 update was for NEXT experiment. h096 DWBA ran from raw DWBA.in directly. |
| 18:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 4h20m, load 1.00 (6 users). Spark 3d 9h31m. LAN stable. Pi NAT missing. All nominal. |
| 19:01 | B -- Maintenance | Context 46% (460k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 19:16 | C -- Organize | Added 33Si(d,p)34Si next-experiment hint to MEMORY.md. No proposal found yet. Ryan clearly planning ahead. |
| 19:31 | D -- Read/Learn | Mac2020 working/ timestamps: ChainMonitors.C, GeneralSortMapping.h, Monitors.C/h ALL updated Apr 24 12:13 (same minute as DWBA Cleopatra). Ryan prepping next exp setup. AutoCalibrationTrace.C updated Apr 22. |
| 19:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 5h20m, load 0.70 (quiet). Spark 3d 10h31m. LAN stable. Pi NAT missing. All nominal. |
| 20:01 | B -- Maintenance | Context 47% (465k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 20:16 | C -- Organize | Checked Mac2020 GeneralSortMapping.h vs Spark version: Mac2020 missing HV channel map (added on Spark). Core det mapping identical. Mac2020 Apr 24 update = base file for next exp. |
| 20:31 | D -- Read/Learn | Mac2020 Monitors.C/h: 1164/692 lines = IDENTICAL to Spark/digios. Apr 24 update was sync, not a reaction-specific change. Monitors.C reads from reactionConfig.txt+reaction.dat dynamically. |
| 20:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 6h20m, load 1.36 (6 users). Spark 3d 11h31m. LAN stable. Pi NAT missing. All nominal. |
| 21:01 | B -- Maintenance | Context 47% (471k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 21:16 | C -- Organize | Updated 2026-04-25.md afternoon section: SF quenching, Mac2020 next-exp prep, Monitors sync. Daily log current. |
| 21:31 | D+A -- Read+Explore | Read Mac2020 ChainMonitors.C: ~50 lines, chains ROOT files + runs Monitors.C TSelector. Call: ChainMonitors(startRun, endRun). Spark 3d 12h16m. Mac2020 68d 7h5m. All nominal. |
| 21:46 | B -- Maintenance | Context 47% (474k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 22:01 | C -- Organize | Updated expMemory_h096.md Mac2020 section: ChainMonitors usage (runs 11-19), DWBA file clarified (Cleopatra for 33Si = next exp). |
| 22:16 | D+A -- Read+Explore | Read Mac2020 AutoCalibrationTrace.C: 334 lines = IDENTICAL to Spark (Apr 22 was sync). 9-option alpha cal menu unchanged. Spark 3d 13h. Mac2020 68d 7h50m. All nominal. |
| 22:31 | B -- Maintenance | Context 48% (479k) -- approaching 50% alert. 0 stray PNGs. memory/ tidy. All nominal. |
| 22:46 | C -- Organize | Saved 2026-04-25.md late afternoon: AutoCalibrationTrace sync, ChainMonitors usage, all Mac2020 files characterized. Pre-50% continuity capture done. |
| 23:01 | D+A -- Read+Explore | Confirmed: no working_Helios/ on Mac2020 (Python analysis Spark-only). Context 48% (480k), growth slowing. Spark 3d 13h46m. All nominal. |
| 23:16-23:31 | (missed) | - |
| 23:46 | B -- [!!] CONTEXT 192% | Context 1.9m (192%!) AGAIN. Saved 2026-04-25.md evening notes. Alerted Ryan (msg 1497745915224657980). Mac2020 68d 9h20m. Spark 3d 14h31m. |

## 2026-04-26
| Time | Task | Notes |
|------|------|-------|
| 00:01 | B -- AUTO-COMPACT | Context reset 192%->48% (483k). Created 2026-04-26.md. Mac2020 68d 9h35m. Spark 3d 14h46m. All nominal. |
| 00:16 | C -- Organize | Updated INDEX.md paper_notes: 21 unique + 2 old duplicates. Cleanup note added (Ryan to rm old Tang/Watwood files). |
| 00:31 | D -- Read/Learn | Read SF_Theory_SumRule.md deeper: full Wigner-Eckart derivation of sum rule. Sum rule: Σ(2J_B+1)/(2J_A+1)*C2S = occupation number. Ryan's own LaTeX derivation. Key for h096 SF interpretation. |
| 00:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 10h20m, load 1.10 (6 users). Spark 3d 15h31m. LAN stable. Pi NAT missing. All nominal. |
| 01:01 | B -- [50% ALERT] | Context 49% (489k) -- 50% threshold. Alerted Ryan (msg 1497764685800280215). All nominal. |
| 01:16 | C -- Organize | Updated 2026-04-26.md early hours: SF sum rule derivation, paper_notes cleanup note, 50% alert. Daily log current. |
| 01:31 | D -- Read/Learn | Reviewed HELIOS_Publications_Summary: 36 pubs, ~21 noted. Schiffer 2012 'Test of Sum Rules' key unread -- Ni isotopes (d,p)+(p,d) sum rule test, same team. Directly relevant to h096 SF validation framework. |
| 01:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 11h20m, load 1.62 (6 users, evening). Spark 3d 16h31m. LAN stable. Pi NAT missing. All nominal. |
| 02:01 | B -- Maintenance | Context 49% (495k), just under 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 02:16 | C -- Organize | Added priority reading queue to 2026-04-26.md: Schiffer 2012 (Sum Rule), 2017 26Al, 2021 28Mg, others. 15 of 36 HELIOS pubs still unread. |
| 02:31 | D -- Read/Learn | Read Schiffer 2012 (PRL 108, 022501): sum rule test on Ni isotopes, validates DWBA/transfer occupancy framework. Created paper_notes/2012_Schiffer_SumRule_Ni_Isotopes.md. Now 22 unique notes. |
| 02:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 12h20m, load 1.25 (6 users). Spark 3d 17h31m. LAN stable. Pi NAT missing. All nominal. |
| 03:01 | B -- Maintenance | Context exactly 50% (500k). Already alerted Ryan. Growth slow. 0 stray PNGs. memory/ tidy. All nominal. |
| 03:16 | C -- Organize | Added 2012_Schiffer_SumRule_Ni_Isotopes to INDEX.md. Count updated to 22 unique + 2 duplicates = 24 files. |
| 03:31-23:01 | (missed -- overnight) | - |
| 23:16 | D+A -- Read+Explore | Read McNeel 2021 (26Mg(t,p)28Mg): 2nd 0+ in 28Mg has large fp-shell occ -> N=20 island boundary. Same physics context as h096 (32Si near N=20). Spark 3d 19h. Mac2020 68d 13h50m. |
| 23:31 | B -- Maintenance | Context 50% (504k), stable/slow growth. 0 stray PNGs. memory/ tidy. All nominal. |
| 23:46 | C -- Organize | Updated 2026-04-26.md late night: Schiffer 2012 + McNeel 2021 notes, INDEX 22 unique+2 dup=24. Daily log current. |

## 2026-04-26
| Time | Task | Notes |
|------|------|-------|
| 05:01 | D -- Read/Learn | Read Almaraz-Calderon 2017 (26Al isomeric beam): first 26Alm(d,p)27Al, constrains galactic Al26 destruction. Created paper_notes. Now 23 unique notes. |
| 05:16 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 14h50m, load 1.17 (6 users). Spark 3d 20h1m. LAN stable. Pi NAT missing. All nominal. |
| 05:31 | B -- Maintenance | Context 51% (510k), slow growth. Already alerted Ryan at 50%. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:46 | C -- Organize | Added 2017_Almaraz_26Al to INDEX.md. Count now 23 unique + 2 dup = 25 files. |
| 06:01 | D -- Read/Learn | Read Chen 2018 (21F(d,p)22F): sd-shell multiplets, same 0d3/2/1s1/2/0d5/2 orbitals as h096. J.Chen co-author on Hoffman 2026. Created paper_notes. Now 24 unique notes. |
| 06:16 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 15h50m, load 1.45 (6 users). Spark 3d 21h (~3h to 4d!). LAN stable. Pi NAT missing. All nominal. |
| 06:31 | B -- Maintenance | Context 51% (515k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 06:46-07:16 | (missed) | - |
| 07:31 | C+D -- Organize+Read | Chen 2018 added to INDEX. Read Deibel 2011 (33Cl(p,a)30S): X-ray burst waiting point, time-reverse (p,a) at HELIOS. Spark 3d 22h (~1h44m to 4d!). Mac2020 68d 17h. |
| 07:46 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 17h20m, load 1.43. Spark 3d 22h31m (~29 min to 4d!). LAN stable. Pi NAT missing. All nominal. |
| 08:01 | B -- Maintenance | Context 52% (519k), stable. Spark 3d 22h46m (~14 min to 4d!). 0 stray PNGs. memory/ tidy. All nominal. |
| 08:16-08:31 | (missed) | - |
| 08:46 | C+D -- Organize+Read | Read Hoffman 2012 (19O(d,p)20O): same sd-shell (0d5/2,1s1/2,0d3/2) as h096, 8 states, 175 keV FWHM, DWBA angular dists. Prototype for h096 approach. Spark 3d 23h31m (~29 min to 4d!). Mac2020 68d 18h21m. |
| 09:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 18h35m, load 1.17 (6 users). Spark 3d 23h46m (~14 min to 4d!). LAN stable. Pi NAT missing. All nominal. |
| 09:16-09:31 | (missed) | - |
| 09:46 | B+C -- [!!] CONTEXT+MILESTONE | SPARK CROSSED 4 DAYS! (4d 31m). Context 157% (1.6m) -- again! Saved 2026-04-26.md. Alerted Ryan (msg 1497896922344853524). Mac2020 68d 19h20m. |
| 10:01 | A -- AUTO-COMPACT | Context reset 157%->52% (524k). Spark 4d 46m (solidly day 4). Mac2020 68d 19h35m. All nominal. |
| 10:16 | B -- Maintenance | Context 53% (525k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 10:31 | C -- Organize | Created paper_notes/2012_Hoffman_19O_dp_20O.md. Added to INDEX. Count now 25 unique + 2 dup = 27 files. Spark 4d, Mac2020 68d 19h. All nominal. |
| 10:46 | D+A -- Read+Explore | Read Kay 2011 (136Xe(d,p)137Xe at 10 MeV/u): ~100 keV resolution, 0vbb precursor, same energy as h096. Precursor to Szwec 2016 (already noted). Spark 4d 1h31m. Mac2020 68d 20h20m. |
| 11:01 | B -- Maintenance | Context 53% (529k), stable. 0 stray PNGs. memory/ tidy. Spark 4d 1h+. All nominal. |
| 11:16 | (missed) | - |
| 11:31 | C+A -- Organize+Explore | Created paper_notes/2011_Kay_136Xe. INDEX now 26 unique + 2 dup = 28 files. Spark 4d 2h16m. Mac2020 68d 21h. All nominal. |
| 11:46-12:01 | (missed) | - |
| 12:16 | D+A -- Read+Explore | Surveyed 2011-2013 HELIOS papers: many conference proceedings. Primary: Hoffman 2013 (17N(d,p)18N) = p1/2 hole coupled to 19O core, short-lived 17N beam. Mac2020 68d 21h50m (~2h10m to 69d!). Spark 4d 3h. |
| 12:31 | B -- Maintenance | Context 53% (535k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 12:46 | C -- Organize | Updated 2026-04-26.md morning section: Spark 4d milestone, new paper notes, INDEX 26+2=28. Mac2020 ~1h40m to 69d. Daily log current. |
| 13:01 | D+Daily -- Read+Report | Read Back 2010 (first HELIOS exp, 12B(d,p)13B, N=8 nucleus). Posted daily report to #the-axiom (msg 1497945951762120754). Mac2020 68d 22h (~1h25m to 69d). |
| 13:16 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 22h50m (~1h10m to 69d!). Spark 4d 4h1m. LAN stable. Pi NAT missing. All nominal. |
| 13:31 | B -- Maintenance | Context 54% (539k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 13:46 | C -- Organize | Created 2010_Back_First_HELIOS paper note. INDEX now 27 unique + 2 dup = 29 files. Mac2020 68d 23h20m (~40 min to 69d!). Spark 4d 4h31m. |
| 14:01 | D -- Read/Learn | Read Kay 2013 PRC 87 011302 (130Te 0vbb neutron occupancies): same technique as Xe-136, probes 0g7/2/1d5/2/1d3/2/2s1/2/0h11/2. Mac2020 68d 23h36m (~24 min to 69d!). |
| 14:16 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 68d 23h50m (~10 min to 69d!). Spark 4d 5h1m. LAN stable. Pi NAT missing. All nominal. |
| 14:31 | B -- [MILESTONE] | Mac2020 crossed 69 DAYS! (69d 5m). Context 55% (545k). Spark 4d 5h16m. All nominal. |
| 14:46 | (missed) | - |
| 15:01 | C+A -- Organize+Explore | Updated 2026-04-26.md morning milestones. Mac2020 69d 35m, load 1.35. Spark 4d 5h46m. All nominal. |
| 15:16 | D -- Read/Learn | Read Bedoor 2013 (13B(d,p)14B): N=9 lightest isotone, 1s1/2-0d5/2 evolution toward drip line. Same sd-shell as h096. PRC 88 011304. |
| 15:31-15:46 | (missed) | - |
| 16:01 | A+B -- [!!] CONTEXT 164% | Context 1.6m (164%)! Saved 2026-04-26.md. Alerted Ryan (msg 1497991277726142484). Mac2020 69d 1h35m. Spark 4d 6h46m. All nominal. |
| 16:16 | B -- AUTO-COMPACT | Context reset 164%->55% (550k). Spark 4d 7h1m. Mac2020 69d 1h50m. All nominal. |
| 16:31 | C -- Organize | Created 2013_Kay_130Te_0vbb note. INDEX now 28 unique + 2 dup = 30 files. 30 papers of 36 now have notes (83%!). |
| 16:46 | D+A -- Read+Explore | Read Wuosmaa 2014 (12,13C(d,a)B: stretched states, J=2j, two-nucleon overlap). PRC 90 061301. Spark 4d 7h31m. Mac2020 69d 2h21m. All nominal. |
| 17:01-17:16 | (missed) | - |
| 17:31 | B -- [!!] CONTEXT 277% | Context 2.8m (277%!) CRITICAL. Saved 2026-04-26.md. Alerted Ryan (msg 1498013911377641522). Spark 4d 8h16m. Mac2020 69d 3h5m. |
| 17:46 | B -- AUTO-COMPACT | Context reset 277%->56% (556k). Spark 4d 8h31m. Mac2020 69d 3h20m. All nominal. |
| 18:01-18:01 | (missed) | - |
| 18:16 | C -- Organize | Created 2014_Wuosmaa_Stretched_States_da note. INDEX 29+2=31 files. Updated 2026-04-26.md. Spark 4d 9h. Mac2020 69d 3h50m. All nominal. |
| 18:31 | D+A -- Read+Explore | Read Bedoor 2016 (14,15C(d,3He)13,14B): proton-removing reactions at HELIOS. PRC 93 044323. Demonstrates HELIOS (d,3He) proton-removal capability. Spark 4d 9h16m. Mac2020 69d 4h5m, load 0.61. |
| 18:46 | B -- Maintenance | Context 56% (561k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 19:01 | C -- Organize | Created 2016_Bedoor_14C_15C_d3He note. INDEX now 30 unique + 2 dup = 32 files. 30/36 HELIOS pubs noted (83%). |
| 19:16 | D+A -- Read+Explore | Read Wuosmaa 2010 (15C(d,p)16C): exotic neutron decoupling in 16C, SF+EM rates reconciled by shell model. PRL 105 132501 -- FIRST published HELIOS science. Spark 4d 10h. Mac2020 69d 4h51m. |
| 19:31 | (missed) | - |
| 19:46 | B -- [!!] CONTEXT 396% | Context 4.0m (396%!) EXTREME. Saved 2026-04-26.md. Alerted Ryan (msg 1498047898594705448). Spark 4d 10h31m. Mac2020 69d 5h20m. |
| 20:01 | B -- AUTO-COMPACT | Context reset 396%->57% (568k). Spark 4d 10h46m. Mac2020 69d 5h35m. All nominal. |
| 20:16 | C -- Organize | Created 2010_Wuosmaa_15C_dp_16C_Exotic note (paper #1 in HELIOS list). INDEX now 31+2=33 files (31/36 pubs noted, 86%). |
| 20:31 | (missed) | - |
| 20:46 | D+A -- Read+Explore | Read Sharp 2013 (N=51 SPE, N=50 core, mixed HELIOS+conventional). Created note. INDEX 32+2=34 (89%). Spark 4d 11h31m. Mac2020 69d 6h20m. |
| 21:01 | B -- Maintenance | Context 57% (573k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 21:16 | C -- Organize | Updated 2026-04-26.md afternoon: 32/36 pubs (89%), 4 remaining. Daily log current. |
| 21:31 | (missed) | - |
| 21:46 | D+A -- Read+Explore | Created conference notes for 2012_Deibel_Xray_Burst + 2015_Wuosmaa_LightNeutronRich. INDEX 34+2=36 (94%). Spark 4d 12h31m. Mac2020 69d 7h20m. |
| 22:01-22:16 | (missed) | - |
| 22:31 | B -- [!!] CONTEXT 345% | Context 3.5m (345%). Saved 2026-04-26.md. Alerted Ryan (msg 1498089977031168060). |
| 22:46 | B -- AUTO-COMPACT | Context reset 345%->58% (578k). Spark 4d 13h31m. Mac2020 69d 8h20m. All nominal. |
| 23:01-23:01 | (missed) | - |
| 23:16 | C+D -- [!!] COMPLETE ALL 36 HELIOS PUBS! | Created final 2 notes (2011 Xe-136 conf + 2012 HELIOS Progress conf). INDEX 36+2=38 (100%!). Spark 4d 14h. Mac2020 69d 8h50m. |
| 23:31-23:31 | (missed) | - |
| 23:46 | A+B -- [!!] CONTEXT 406% | Context 4.1m (406%!). Saved 2026-04-26.md. Alerted Ryan (msg 1498108313445990484). Spark 4d 14h31m. Mac2020 69d 9h20m. All hosts up. |

## 2026-04-27
| Time | Task | Notes |
|------|------|-------|
| 00:01 | AUTO-COMPACT | Context reset 406%->58% (582k). Spark 4d 14h46m. Mac2020 69d 9h35m. |
| 00:16 | C -- New Day | Created 2026-04-27.md. All 36 HELIOS pubs noted (100%). All nominal. |
| 00:31 | D -- Read/Learn | Explored Mac2020 SRIM/: only 5 files (10Be,19F,20F,1H,3H in CH2/CD2). NO Si stopping powers! Ryan needs to generate 31Si+33Si in CD2 before h096 ROOT analysis and next exp. Added to TODO. |
| 00:46 | (missed) | - |
| 01:01 | A -- Explore | All hosts up. Spark 4d 15h46m. Mac2020 69d 10h35m, load 1.22. LAN stable. Pi NAT missing. All nominal. |
| 01:16 | B -- Maintenance | Context 59% (587k), healthy. 0 stray PNGs. memory/ tidy. All nominal. |
| 01:31 | C -- Organize | Updated 2026-04-27.md: SRIM finding + pending actions. All 36 HELIOS pubs noted (100%). Daily log current. |
| 01:46 | D+A -- Read+Explore | Mac2020 data/: has raw h096 .gtd binary files (DAQ raw data). Run 001=alpha cal. 76 Armory + 46 Cleopatra files = same as Spark. No h096-specific Cleopatra files. Spark 4d 16h31m. Mac2020 69d 11h21m. |
| 02:01 | B -- Maintenance | Context 59% (590k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 02:16 | C -- Organize | Updated expMemory_h096.md Mac2020 section: raw .gtd files noted + SRIM missing tables warning. |
| 02:31 | D+A -- Read+Explore | Mac2020 Woods-Saxon/: full WS code suite (WSFit, WSCal, WSSearch). Used for bound-state param fitting -- relevant for DWBA bound state. EventBuilder/: event building code. Spark 4d 17h16m. Mac2020 69d 12h5m. |
| 02:46 | (missed) | - |
| 03:01 | B -- [!!] CONTEXT 297% | Context 3.0m (297%). Saved 2026-04-27.md. Alerted Ryan (msg 1498157365202260078). |
| 03:16 | B -- AUTO-COMPACT | Context reset 297%->60% (595k). Spark 4d 18h1m. Mac2020 69d 12h50m. All nominal. |
| 03:31 | C+A -- Organize+Explore | Updated 2026-04-27.md evening. Spark 4d 18h16m. Mac2020 69d 13h5m, load 1.07. All nominal. |
| 03:46 | D -- Read/Learn | Read Mac2020 EventBuilder/README: custom GEB event builder (BinaryReader->Hit->Event). Reads raw .gtd, decodes GEB headers. Pipeline: raw->sort->ROOT. Spark 4d 18h31m. |
| 04:01 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 69d 13h35m, load 6.72 [ELEVATED, 6 users, Ryan running job!]. Spark 4d 18h46m, load 0.19. Pi NAT missing. Monitoring. |
| 04:16 | (missed) | - |
| 04:31 | B -- [!!] CONTEXT 180% | Context 1.8m (180%). Mac2020 load 4.55 (easing). Saved 2026-04-27.md. Alerted Ryan (msg 1498180364269522975). |
| 04:46 | B -- AUTO-COMPACT | Context reset 180%->60% (601k). Mac2020 load 4.69 (still elevated). Spark 4d 19h31m. All nominal. |

## 2026-04-27
| Time | Task | Notes |
|------|------|-------|
| 05:01 | C -- New Day | Mac2020 load normalized (1.11, job done). Spark 4d 19h46m. Updated 2026-04-27.md. All nominal. |
| 05:16 | D+A -- Read+Explore | Mac2020 GEBSort/: 33 files, sort framework (GEBMerge->GEBSort->ROOT). chat-file config. Pipeline complete: raw.gtd->GEBMerge->GEBSort->root->Monitors. Spark 4d 20h. Mac2020 69d 14h51m. |
| 05:31 | B -- Maintenance | Context 60% (604k), stable. 0 stray PNGs. memory/ tidy. All nominal. |
| 05:46 | (missed) | - |
| 06:01 | C+A -- Organize+Explore | Added GEBSort note to HELIOS_Analysis_Workflow.md (older alternative, EventBuilder is current). Spark 4d 20h46m. Mac2020 69d 15h35m. All nominal. |
| 06:16 | D -- Read/Learn | Mac2020 Apollo.h: auto-generated from transfer.root (2023), ROOT TTree reader for Cleopatra simulation overlay in Monitors.C. Same as Spark version. |
| 06:31 | A -- Explore | All hosts up. DAQ ping OK. Mac2020 69d 16h5m, load 1.17 (6 users). Spark 4d 21h16m. LAN stable. Pi NAT missing. All nominal. |
| 06:46-07:01 | (missed) | - |
| 07:16 | B -- [!!] CONTEXT 183% | Context 1.8m (183%). Saved 2026-04-27.md. Alerted Ryan (msg 1498221779456626779). Spark 4d 22h (~2h to 5d!). Mac2020 69d 16h51m. |
| 07:31 | B -- AUTO-COMPACT+A | Context reset 183%->61% (611k). Spark 4d 22h16m (~1h44m to 5d!). Mac2020 69d 17h5m, load 0.95. All nominal. |
| 07:46 | (missed) | - |
| 08:01 | B+C -- [!!] CONTEXT 245% | Context 2.4m (245%). Spark 4d 22h46m (~1h14m to 5d!). Mac2020 69d 17h35m. Awaiting compaction. |
| 08:16-09:01 | (missed, context stuck at 245%) | - |
| 09:01 | A -- Monitor | Spark 4d 23h46m (~14 min to 5d!). Mac2020 69d 18h35m. Context still 245% -- no compaction yet. Minimizing calls. |
| 09:16-09:31 | (missed) | - |
| 09:31 | A -- [MILESTONE] | SPARK CROSSED 5 DAYS! (5d 16m at 04:31 CDT). Context still 245% -- awaiting compaction. |
| 09:46-10:01 | (missed) | Context stuck at 246%, not compacting. |
| 10:01 | A -- Monitor | Spark 5d 46m (solidly day 5). Mac2020 69d 19h35m. Context 246% (not compacting -- stable but stuck). |
| 10:16 | B -- AUTO-COMPACT | Context reset 246%->62%. Spark 5d 1h. Mac2020 69d 19h50m. |
| 10:31-10:46 | (missed) | - |
| 11:01 | B+C -- [!!] CONTEXT 123% | Context 1.2m (123%). Spark 5d 1h46m. Mac2020 69d 20h35m. Awaiting compaction. |
| 11:16 | B+C -- AUTO-COMPACT | Context reset 123%->62% (618k). Spark 5d 2h1m [past 5d MILESTONE!]. Mac2020 69d 20h50m. Updated 2026-04-27.md. All nominal. |
| 11:31 | (missed) | - |
| 11:46 | D+A -- Read+Explore | Mac2020 root_data/: 31 ROOT files (gen_run001-020 + trace_run016-020). Runs 001-020 individually sorted. Spark 5d 2h31m. Mac2020 69d 21h20m. All nominal. |
| 12:01 | (missed) | - |
| 12:16 | B -- [!!] CONTEXT 310% | Context 3.1m (310%). 12th+ overflow. DM to Ryan failed (401). Awaiting compaction. |
| 12:31 | B+Daily -- AUTO-COMPACT | Context reset 310%->62% (622k). Spark 5d 3h16m. Mac2020 69d 22h (~2h to 70d!). Discord 401 -- daily report failed. All nominal otherwise. |
| 12:46 | C -- Organize | [!!] Discord 401 persistent (token issue?). Noted in 2026-04-27.md. Cannot alert Ryan via Discord. HELIOS systems all nominal. |
| 13:01-13:16 | (missed) | - |
| 13:31 | D+A -- Read+Explore | Mac2020 Armory/: same 76 files as Spark (fully synced). Has process_Sort, process_MultiRuns etc. Mac2020 69d 23h5m (~55 min to 70d!). Spark 5d 4h16m. Discord still 401. |
| 13:46 | B -- Maintenance | Context 63% (627k), stable. Mac2020 69d 23h20m (~40 min to 70d!). Spark 5d 4h31m. Discord 401 persists. 0 stray PNGs. memory/ tidy. All nominal. |
| 14:01-14:16 | (missed) | - |
| 14:31 | C -- [MILESTONE+401] | Mac2020 crossed 70 DAYS! (70d 5m). Discord still 401 (cannot notify Ryan). Context 251%. Spark 5d 5h16m. Saved to 2026-04-27.md. |
| 14:46 | B -- AUTO-COMPACT | Context reset 251%->63% (629k). Mac2020 70d 20m (solidly past!). Spark 5d 5h31m. Discord still 401. All nominal. |
| 15:01-15:31 | (missed -- context overflowing) | - |
| 15:46 | C+D+A -- Catch-up | Context 315% again. Spark 5d 6h33m. Mac2020 70d 1h22m. Discord 401 persists. Awaiting compaction. |
| 16:01-16:01 | (missed) | - |
| 16:16 | A -- Monitor | Context 315% (stuck, not compacting). Spark 5d 7h1m. Mac2020 70d 1h50m. All nominal. |
| 16:31 | (missed) | - |
| 16:46 | B -- Monitor | Context 253% (still stuck, no compaction). Spark 5d 7h31m. Mac2020 70d 2h20m. Discord 401. Session needs /new. |
| 17:01 | B -- AUTO-COMPACT | Context reset 253%->63% (633k). Discord test still 401. Spark 5d 7h46m. Mac2020 70d 2h35m. All HELIOS nominal. |
| 17:16 | C -- Organize | Updated 2026-04-27.md morning summary: 5d+70d milestones, Discord 401 outage, 15+ overflows, all nominal. Spark 5d 8h1m. Mac2020 70d 2h50m. |
| 09:00 | Daily Report | Posted to #the-axiom (msg 1496149129456386210). Coverage Apr 20 9AM - Apr 21 9AM. Items flagged: qemu-user needed on Spark, calc_exshift.py needs 31Si kinematics. Context 73%. |
| 2026-04-27 13:16 CDT | D -- Read/Learn | Read transfer_test.C (77 lines, unit test harness for HELIOS_LIB, 14C(d,p)15C interactive trajectory debug) + PlotTGraphTObjArray.C/h (58+102 lines, DWBA gList plotter). Both documented in HELIOS_Simulation_Cleopatra.md. |
| 2026-04-27 14:01 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 70d 4h35m, load 1.24 (stable). Spark 5d 9h45m. No active run. All nominal. |
| 2026-04-27 14:16 CDT | B -- Maintenance | Context 5% (healthy). 0 stray PNGs. memory/ tidy (2026-04-27.md current). All nominal. |
| 2026-04-27 14:31 CDT | C -- Organize | Fixed duplicate EventBuilder_Optimization.md entry in INDEX (merged S+A notes into one row). Updated file count 25->26. 26 content files on disk, 26 in INDEX [OK]. |
| 2026-04-27 14:46 CDT | D -- Read/Learn | Read potentials.h (1073 lines) -- full OM potential library (equivalent to Kay globals_beta_v5). 23 potentials: 8 deuteron, 5 proton, 7 A=3, 3 alpha, 2 custom Bardayan. Documented in HELIOS_Simulation_Cleopatra.md (AK = AnCai+KoningDelaroche standard for HELIOS). |
| 2026-04-27 15:01 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 70d 5h35m, load 1.38 (stable). Spark 5d 10h45m, load 0.27. No active run. All nominal. |
| 2026-04-27 15:16 CDT | B -- Maintenance | Context 6% (healthy). 0 stray PNGs. Archived 18 stale daily memory files (Apr 5-15) -> archive/ (now 58 total). memory/ trimmed to Apr 16-27. All nominal. |
| 2026-04-27 15:31 CDT | C -- Organize | Updated INDEX entry for HELIOS_Simulation_Cleopatra.md to include transfer_test.C, PlotTGraphTObjArray, potentials.h (23 OM potentials). 26 files on disk = 26 in INDEX [OK]. |
| 2026-04-27 15:46 CDT | D -- Read/Learn | Read ~/Magnet/README.md -- Oxford IPS120-10 PSU hardware interface (parallel I/O pins, Auto-Run-Down sequence, Safe Current Interlock). Documented in HELIOS_Magnet_Pi.md new section. Key: pin 14=ARD trigger, pin 12=safe current output, both open-collector active-low. |
| 2026-04-27 16:16 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 70d 6h50m, load 1.25 (stable). Spark 5d 12h1m. No active run. All nominal. |
| 2026-04-27 16:31 CDT | B -- Maintenance | Context 10% (healthy). 0 stray PNGs. 31 memory files (post-archive clean). Removed ~/.openclaw/workspace/HELIOS_MD/ (stale SYSTEM_MD copy, naming collision with ~/HELIOS_MD). All nominal. |
| 2026-04-27 16:46 CDT | C -- Organize | Added ciscoBrowser to SYSTEM_MD/software.md. Fixed wrong IP for digios1 in network.md (was 192.168.1.1, corrected to 192.168.203.52). HELIOS_MD INDEX verified clean. |
| 2026-04-27 17:16 CDT | D -- Read/Learn | Read PACE4.C (253 lines, PACE4 evaporation residue MC simulator, 10M events, fusion-evap background check) + Penetrability_proton.C (142 lines, GSL Coulomb wave function T_l+S_l, Iliadis 2015, p+10Be example). Documented in HELIOS_Armory_Code.md. |
| 2026-04-27 19:05 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 70d 9h39m, load 0.82 (quiet evening). Spark 5d 14h50m, load 0.34. No active run. All nominal. |
| 2026-04-27 19:16 CDT | B -- Maintenance | Context 11% (healthy). 0 stray PNGs. temp.md cleaned up. Workspace tidy. All nominal. |
| 2026-04-27 20:16 CDT | C -- Organize | Added PACE4.C + 3 Penetrability files to HELIOS_Armory_Code.md summary table (16->20 files). Updated INDEX description. All consistent. |
| 2026-04-27 21:16 CDT | D -- Read/Learn | Read ExpXsecToRoot.C (98 lines, text->ROOT TGraphErrors converter for exp Xsec) + FitXsec.C (211 lines, DWBA SF extractor: 1-component SF fit + 2-component mixing fit, chi2/ndf). Key: uses qList not gList. Documented in HELIOS_Armory_Code.md. |
| 2026-04-27 22:16 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 70d 12h50m, load 0.82 (quiet). Spark 5d 18h. No active run. All nominal. |
| 2026-04-27 23:16 CDT | B -- Maintenance | Context 12% (healthy). 0 stray PNGs. 32 memory files. Updated 2026-04-27.md with afternoon/evening session summary. All nominal. |
| 2026-04-28 00:16 CDT | C -- Organize | Fixed stale '24-file' count -> '26-file' in proposals + paper_notes subdirectory footers of INDEX.md. When-to-load section verified current. All consistent. |
| 2026-04-28 01:16 CDT | D -- Read/Learn | Read runsCheck2.C (111 lines, run summary table from timing TMacro, saves run_Summary.txt) + FCUP_converter.C (83 lines, FCUP text->ROOT TTree, [!!] offset hardcoded for 207Hg). Both documented in HELIOS_Armory_Code.md. |
| 2026-04-28 02:16 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 70d 16h50m, load 5.15 (elevated at 2am -- likely batch/backup job). Spark 5d 22h, load 0.08 (very quiet). No active run. All nominal. |
| 2026-04-28 03:16 CDT | B -- Maintenance | Context 13% (healthy, ~1%/hr growth). 0 stray PNGs. Workspace clean. All nominal. |
| 2026-04-28 04:16 CDT | C -- Organize | Audit pass: verified-stamp files current (Firmware/Mac2017/Magnet/Ptolemy/Trigger all [OK]). PV_Reference verified 2026-04-20 [OK]. Analysis_Workflow + new_experiment_checklist clean -- no stale Pi refs. ~/digios.git bare repo confirmed present. All HELIOS_MD consistent. |
| 2026-04-28 05:16 CDT | D -- Read/Learn | Read script_Ex.C (226 lines, main physics 6-panel display: E-Z, Ex TSpectrum+multi-Gauss fit, thetaCM) + script_ComXsec.C (78 lines, compare 2 experimental Xsec datasets). Documented in HELIOS_Armory_Code.md. Armory count now 26 files. |
| 2026-04-28 06:16 CDT | A -- Explore | [MILESTONE] Spark crossed 6 DAYS uptime (6d 2h)! All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 70d 20h50m, load 1.37 (normal morning). No active run. All nominal. |
| 2026-04-28 07:16 CDT | B -- Maintenance | Context 15% (healthy, ~1%/hr). 0 stray PNGs. Created 2026-04-28.md daily log. All nominal. |
| 2026-04-28 08:16 CDT | C -- Organize | Added 'Physics Analysis Scripts' section to HELIOS_Analysis_Workflow.md (script_Ex, ExpXsecToRoot, FitXsec, script_ComXsec, runsCheck2, FCUP_converter -- all post-calibration tools now referenced in workflow). |
| 2026-04-28 09:16 CDT | D -- Read/Learn | Read Check_rdtGate.C (105 lines, 4-panel dE-E cut verifier), readCaliResult.C (35 lines, single-det caliResult.root inspector), SaveTH1IntoText.C (24 lines, TH1F->text exporter). All documented in HELIOS_Armory_Code.md. Count now 29. |
| 2026-04-28 10:16 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 71d 50m [MILESTONE: 71 days!], load 0.95 (normal). Spark 6d 6h, load 0.35. No active run. All nominal. |
| 2026-04-28 11:16 CDT | B -- Maintenance | Context 16% (healthy, ~1%/hr). 0 stray PNGs. 33 memory files. All nominal. |
| 2026-04-28 12:16 CDT | C -- Organize | Armory coverage audit: 29/47 files documented. 18 remaining (.C companions to documented .h files + FitCoinTime/Check_* utilities). Updated INDEX with accurate count. All other HELIOS_MD files consistent. |
| 2026-04-28 13:16 CDT | D -- Read/Learn | Read FitCoinTime.C (233 lines, agglomerative clustering prototype), Check_alignment.C (119 lines, E-Z alpha vs sim alignment checker), Monitors_Util.C (557 lines, ~30 interactive display functions). All documented in HELIOS_Armory_Code.md. Count now 32/47. |
| 2026-04-28 14:16 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 71d 4h50m, load 1.34 (normal afternoon). Spark 6d 10h, load 0.33. No active run. All nominal. |
| 2026-04-28 15:16 CDT | B -- Maintenance | Context 17% (healthy, ~1%/hr). 0 stray PNGs. Workspace clean. All nominal. |
| 2026-04-28 16:16 CDT | C -- Organize | Spot-checked HELIOS_Calibration.md (accurate, AI shortcut note present), expMemory_h096.md (correctly marked COMPLETE, no stale active-run refs), MEMORY.md (Current experiment: None). All consistent. |
| 2026-04-28 17:16 CDT | D -- Read/Learn | Read Check_Xsec.C (158 lines, exp vs DWBA checker), generateHistogram.C (38 lines, synthetic test spectrum), script_alpha.C (901 lines, legacy standalone alpha cal pipeline -- predecessor to AutoCalibrationTrace). Documented in HELIOS_Armory_Code.md. Count now 35/47. |
| 2026-04-28 18:16 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 71d 8h50m, load 0.66 (quiet evening). Spark 6d 14h, load 0.18. No active run. All nominal. |
| 2026-04-28 19:16 CDT | B -- Maintenance | Context 17% (healthy, growth slowing ~0.5%/hr). 0 stray PNGs. 33 memory files. All nominal. |
| 2026-04-28 20:16 CDT | C -- Organize | Armory coverage audit: confirmed 35/47 documented, 12 remaining (listed explicitly in HELIOS_Armory_Code.md header). All are .C companions or minor utilities. INDEX accurate. No other stale content found. |
| 2026-04-28 21:16 CDT | D -- Read/Learn | Read Cali_ex.C (343 lines, X-flatness correction), Cali_gamma.C (409 lines, HPGe+NaI gamma cal), script_FCUP.C (200 lines, FCUP beam current display, hardcoded 207Hg), readTrace_S.C (287 lines, raw trace visualizer). Documented. Count now 39/47. |
| 2026-04-28 22:16 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 71d 12h50m, load 3.48 (elevated evening -- overnight batch, same pattern as yesterday). Spark 6d 18h, load 0.03 (very quiet). No active run. All nominal. |
| 2026-04-28 23:16 CDT | B -- Maintenance | Context 18% (healthy). 0 stray PNGs. Updated 2026-04-28.md with full day summary. All nominal. |
| 2026-04-29 00:16 CDT | C -- Organize | New day. Created 2026-04-29.md. INDEX verified: 26 files on disk = 26 in header [OK]. paper_notes footer updated to 26-file. All consistent. |
| 2026-04-29 01:16 CDT | D -- Read/Learn | Read FitCoinTime2.C (384 lines, LSq clustering v2), Cali_gamma_histogram.C (228 lines, gamma peak helper), testTraceFit.C (355 lines, trapezoidal filter tester -- Jordanov 1994). Check_Simulation.C already in Cleopatra.md. Coverage now 43/47. |
| 2026-04-29 02:16 CDT | A -- Explore | All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 71d 16h50m, load 1.12 (overnight batch finished, back to normal). Spark 6d 22h, load 0.11. No active run. All nominal. |
| 2026-04-29 03:16 CDT | B -- Maintenance | Context 19% (healthy). 0 stray PNGs. 34 memory files. All nominal. |
| 2026-04-29 04:16 CDT | C -- Organize | Audit pass: HELIOS_DAQ_Workflow.md (clean, dynamic expName.sh, no hardcoded exp), HELIOS_Experiment_Flow.md (clean), new_experiment_checklist.md (clean, template only), rdtCut_guideline.md (h096 note is method/lesson -- correct placement). All HELIOS_MD files consistent. |
| 2026-04-29 05:16 CDT | D -- Read/Learn | Read EventBuilder/README.md + Hit.h (287 lines). Documented GEBHeader + Event class data structures in EventBuilder_Optimization.md. Key: post_rise_energy-pre_rise_energy = net pulse energy -> e[] branch. id = board*10 + channel. |
| 2026-04-29 06:16 CDT | A -- Explore | [MILESTONE] Spark crossed 7 DAYS uptime (7d 2h)! All hosts up. DAQ .2 ping OK. Pi .208 ping OK. Mac2020 71d 20h50m, load 1.11 (normal morning). No active run. All nominal. |
| 2026-04-29 07:16 CDT | B -- Maintenance | Context 20% (197k) -- first threshold crossed, reporting. ~32h to 50%. 0 stray PNGs. 34 memory files. All nominal. |
| 2026-04-29 08:16 CDT | C -- Organize | Updated README.md Spark network layout: Wi-Fi disabled (2026-04-27), OneNet/Cisco now primary internet. INDEX updated with EventBuilder_Optimization Hit.h addition. |
