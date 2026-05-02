# HELIOS MCP Server Design

**Project:** `helios-mcp` -- a Model Context Protocol server running on Spark, exposing HELIOS knowledge and control capabilities to any MCP-compatible AI tool.

**Created:** 2026-04-30 | **Status:** Design phase

---

## Motivation

Any AI tool (Claude Desktop, Codex, custom agents) that connects to this server gets:
- Direct access to the HELIOS knowledge base (HELIOS_MD, paper notes, synthesis)
- My synthesized opinions on physics problems and paper relationships
- (With appropriate access) live inference from me
- (With appropriate access) control over HELIOS hardware

This turns HELIOS AI knowledge into a **reusable service**, not just a context-injected session.

---

## Access Control: Three Tiers

API key → level mapping stored in `~/helios-mcp/config.yaml` (not hardcoded).
All Level 2+ calls logged to `~/HELIOS_MD/mcp_access.log`.

### Level 1 — Knowledge (shared key, low sensitivity)
Read-only access to the knowledge base.

**Who:** Collaborators, students, General HELIOS bot, external tools, visitors.

**Tools:**
| Tool | Description |
|------|-------------|
| `search_helios_md(query)` | Semantic/grep search across HELIOS_MD |
| `get_document(filename)` | Return full content of a HELIOS_MD file |
| `list_docs()` | List all HELIOS_MD files with descriptions (from INDEX.md) |
| `list_publications()` | List all PDFs in ~/publications/ with metadata |
| `get_paper_notes(identifier)` | Return paper notes by author/year/DOI |
| `search_papers(query)` | Search across all paper notes |
| `find_connections(paper_a, paper_b)` | Return relationship analysis between two papers |
| `get_study_notes(topic)` | Return synthesis notes on a physics topic |

**Resources:** `helios_md://{filename}`, `publications://{year_author}`

---

### Level 2 — Intelligence (personal key, higher sensitivity)
Level 1 + live inference from Master HELIOS.

**Who:** Ryan, Ben Kay (explicitly granted).

**Additional tools:**
| Tool | Description |
|------|-------------|
| `ask_helios(question)` | Send a physics question to me (Master HELIOS) via OpenClaw API; return response. All calls logged with timestamp and caller key ID. |
| `get_helios_opinion(topic)` | Return my synthesized take on a topic, cross-referencing relevant papers and notes. |

**Note:** `ask_helios` invokes me in real-time. I respond in my normal voice. The caller gets me as a physics oracle, but I remain bound by my normal safety rules and access policies.

---

### Level 3 — Control (restricted key, highest sensitivity)
Level 2 + HELIOS hardware control.

**Who:** Ryan only (or explicitly approved operators on shift).

**Additional tools:**
| Tool | Description |
|------|-------------|
| `get_channel(det, side, signal)` | Read EPICS PV values (threshold, rate, window) |
| `set_channel(det, side, signal, value)` | Set EPICS PV value |
| `hv_status()` | Read HV voltage + leakage current (all channels) |
| `hv_set(channel, voltage)` | Ramp HV to target voltage |
| `hv_on(channel)` / `hv_off(channel)` | Enable/disable HV channel |
| `run_status()` | Current run state, trigger rates, vacuum |
| `he_level()` | Read LHe level + shield temp + magnet status |
| `autotune(det_list)` | Run LED threshold auto-tune |
| `run_start(shift_info)` | Start a physics run (requires shift context) |
| `run_stop()` | Stop the current run |

**Safety:** All Level 3 tools route through existing SKILL.md logic. No bypass of safety checks. Destructive actions (HV ramp, run start/stop) require a confirmation token in the request.

**Confirmation token flow:**
```
Client: run_start(shift_info) 
Server: returns {status: "pending", token: "abc123", summary: "..."} 
Client: run_start_confirm(token="abc123")
Server: executes
```

---

## Architecture

```
helios-mcp/
├── server.py          -- main MCP server (stdio transport)
├── config.yaml        -- API keys → levels mapping
├── providers/
│   ├── knowledge.py   -- Level 1: HELIOS_MD + publications search
│   ├── inference.py   -- Level 2: OpenClaw API bridge
│   └── control.py     -- Level 3: EPICS/SNMP/skill bridge
├── auth.py            -- key validation + level enforcement
├── logger.py          -- access log for Level 2+
└── README.md
```

**Transport:** stdio (for local tools like Claude Desktop) + optional TCP socket with TLS for remote access via SSH tunnel.

**MCP SDK:** Python `mcp[cli]` package.

**Knowledge search:** Start with grep/INDEX.md lookup (fast, no dependencies). Upgrade to vector RAG later using existing `~/rag_digios/` infrastructure adapted for HELIOS_MD.

---

## Implementation Phases

### Phase 1 — Knowledge server (build now)
- Implement Level 1 tools only
- stdio transport, Spark-local
- grep-based search on HELIOS_MD
- No auth needed initially (local-only access)
- ~200 lines Python

### Phase 2 — Synthesis notes

> **Status (2026-05-02):** Several synthesis-quality notes already exist in `paper_notes/` and `HELIOS_MD/`:
> - `ESPE_Theory.md` ✓, `SF_Theory_SumRule.md` ✓, `SF_Quenching_Review_2023.md` ✓
> - `Coulomb_Displacement_Energy.md` ✓ (full CDE theory + isospin decomposition)
> - `paper_notes/1976_Schiffer_True_RMP.md` ✓, `paper_notes/2022_Schiffer_SPE_NucleonNumber.md` ✓
> - `HELIOS_PtolemyPlusPlus.md` ✓ (bound-state SF systematic, ZR vs FR)
> Phase 2 can be completed by creating the `synthesis/` dir and linking/copying the relevant sections.

- Write `~/HELIOS_MD/synthesis/` directory:
  - `SF_quenching.md` — quenching debate: data, models, my take
  - `ESPE_evolution.md` — shell evolution, tensor force, Schiffer arc 1976→2022
  - `Coulomb_corrections.md` — oscillator vs WS, isospin decomposition
  - `TBME_extraction.md` — Schiffer-True method, caveats, worked example
  - `32Si_structure.md` — h096/h097 context: what we know
  - `transfer_reactions.md` — DWBA validity, SF sum rules, HELIOS advantages
- Expose via `get_study_notes` and `find_connections` tools

### Phase 3 — Intelligence layer
- Add API key auth
- Wire `ask_helios` to OpenClaw API
- Add access logging
- Grant keys to Ryan + Ben

### Phase 4 — Control layer
- Add Level 3 tools
- Route through existing skill code
- Add confirmation token flow
- Restrict to Ryan key only

---

## Security Notes

- Level 1 key can be shared freely — it's just read access to public knowledge
- Level 2 key is personal — don't share; logs who asked what
- Level 3 key never leaves Spark — only used in local sessions or explicit Ryan approval
- MCP server listens on localhost only by default; remote access requires SSH tunnel (not open port)
- `ask_helios` responses are bounded by my normal safety rules — I won't do anything via MCP I wouldn't do in chat
- Hardware actions go through SKILL.md logic which has its own safety checks (HV ramp limits, run start pre-conditions, etc.)

---

## References
- MCP spec: https://modelcontextprotocol.io
- OpenClaw MCP plugin: `~/.npm-global/lib/node_modules/openclaw/docs/`
- Existing HELIOS skills: `~/.openclaw/workspace/skills/`
- Knowledge base: `~/HELIOS_MD/`

---

_Created: 2026-04-30 | Proposed by Ryan Tang | Designed by Master HELIOS_
