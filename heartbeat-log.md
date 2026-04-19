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
| 23:31 | C -- Organize | Stale-ref sweep: fixed Pi5->Spark in README Ptolemy entry. Added HELIOS_Armory_Code.md to README file table. All HELIOS_MD Pi/ryan refs clean (no hits outside Migration doc). 24/24 files indexed [OK]. |
| 10:29 | D -- Read/Learn | Read Hoffman 2022 (NIM A): in-flight 16N isomeric beam via 15N(d,p) at ATLAS. 40% isomer at 7.9 MeV/u, 24% at 13.2 MeV/u. Angular acceptance controls isomer fraction. Created paper_notes/2022_Hoffman_Inflight_Isomeric_16N.md. |
