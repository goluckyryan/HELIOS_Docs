# RDT DeltaE-E Cut Guideline

A comprehensive guide for drawing Recoil Detector Telescope (RDT) particle identification (PID) cuts on the DeltaE-E plot in HELIOS. Covers three methods: hand-drawn banana, SRIM simulation-assisted, and DBSCAN refinement. Developed from h095 11C(d,p)12C and h094 1?Ne(p,p) analysis.

---

## 1. Physics Background

### What the DeltaE-E Plot Shows
- **x-axis**: E_res  --  residual energy after passing through the thin DeltaE detector (channel units)
- **y-axis**: DeltaE  --  energy lost in the thin silicon detector (channel units)
- Each recoil species (different Z) traces a **banana-shaped locus** following Bethe-Bloch energy loss
- Higher Z -> higher DeltaE at the same E_res -> bands are ordered vertically by Z

### Band Shape
- Bands run **top-left to bottom-right** (high DeltaE at low E_res, low DeltaE at high E_res)
- Shape follows non-relativistic Bethe-Bloch: `dE/dx ? Z2/v2` where `v2` scales with kinetic energy
- Bananas have curvature  --  **NOT straight lines, NOT rectangles**
- The curvature (and relative spacing between bands) changes with Z because effective charge corrections matter at 4-10 MeV/u

### Why Cuts Are Needed
- Without cuts, the Ex spectrum contains events from all recoil species (physics signal + beam contaminants)
- A good cut selects only the desired recoil species (e.g. 1?Ne or 12C) while rejecting others (e.g. 1?F, 1?O)
- The cut defines a region in 2D DeltaE-E space -> only events inside the polygon contribute to the gated Ex spectrum

---

## 2. General Principles (All Methods)

### Banana, NOT Rectangle
- The Bethe-Bloch curve is NOT a straight line
- A rectangular gate ALWAYS cuts real events at the curve's corners and includes contamination at the straight edges
- Every cut must follow the banana curvature

### Figure of Merit (FOM)
**FOM = S2/N** where:
- **S** = signal counts (events in known physics peaks, e.g. g.s. + 4.4 MeV for 12C)
- **N** = all counts in the relevant Ex range (signal + background + contamination)
- Equivalently: `(S/N) x S`  --  combines purity (signal/total) x yield (signal count)
- Equivalently: square of Poisson statistical significance `(S/?N)2`
- **Maximizing FOM** finds the optimal balance between tight (clean but low yield) and wide (high yield but contaminated)
- Forbidden gap: a known Ex region where NO physics states exist (e.g. 0.5-3.5 MeV for 12C). Any events here = contamination leakage. Use this to monitor cut purity.

### Save Format
- ROOT file containing a `TObjArray` named `cutList`
- Each entry is a `TCutG` named `cut0`, `cut1`, `cut2`, `cut3` (one per telescope)
- Monitors.C expects two separate files: `rdtCutFile1` (primary species) and `rdtCutFile2` (secondary species)
- `cutList->At(i)->IsInside(rdt[2*i], rdt[2*i+1])` for telescope `i`
- **Individual top-level TCutG keys crash Monitors.C**  --  always use TObjArray `cutList`!
- Inactive telescopes: use a 4-point dummy TCutG at (0,0)

### Iterative Process
- Never trust a first-pass cut. Always iterate:
  1. Draw initial cut
  2. Apply in Monitors.C, check Ex spectrum
  3. Check forbidden gap contamination
  4. Adjust cut, reapply, repeat
- 3-5 iterations is normal

---

## 3. Method 1: Hand-Drawn Banana Cut

**Best when:** The species of interest has a clearly visible, well-separated banana in the DeltaE-E plot (e.g. 12C in h095 where contaminant blob is well below the 12C locus).

### Procedure

#### Step 1: Run Without Cuts
- Set `rdtCutFile1 = ""` in Monitors.C (no RDT gate)
- Run ChainMonitors on all physics runs -> get ungated Ex spectrum
- This computes Ex for ALL events regardless of recoil species

#### Step 2: Ex-Gate to Identify Physics Events
- Gate on known physics peaks in Ex (e.g. g.s. ? 0.5 MeV, 4.4 MeV ? 0.3 MeV for 12C)
- Plot these Ex-gated events in DeltaE-E space -> see where the desired recoil species sits
- This tells you **where the physics IS** in 2D DeltaE-E space

#### Step 3: Overlay All Events
- On the same DeltaE-E plot, overlay ALL events (ungated) using thick black markers (`MarkerStyle(20), Size(0.4)`)
- The physics events (colored from Ex-gate) sit on the desired banana
- Contaminant blobs (other species) become visible as separate clusters
- The **gap** between the physics banana and contaminant cluster is where your cut goes

#### Step 4: Trace the Cut
- Follow the banana shape through the gap between physics and contaminant
- **~100-150 channel breathing room**  --  don't bloat, don't clip
- Close the polygon (first point = last point)
- For the open ends of the banana (high-E and low-E), extend generously  --  you can always tighten later

#### Step 5: Apply and Evaluate
- Save as TCutG -> ROOT file (see Save Format above)
- Run ChainMonitors with the cut enabled
- Check:
  - g.s. and 4.4 MeV peak yields
  - Forbidden gap contamination (should be minimal)
  - FOM = S2/N
- Iterate: adjust cut boundaries, rerun, compare FOM

### Key Rules
- The 2D scatter plot is the **final judge**  --  do NOT trust 1D projections (Ex vs E or Ex vs DeltaE)
- Always Ex-gate first to know where physics events sit
- Band shapes are different for each telescope  --  draw each telescope independently

---

## 4. Method 2: SRIM Simulation-Assisted Cut

**Best when:** DeltaE-E bands overlap and can't be cleanly separated by eye, but one strong isotope (e.g. 1?F beam contaminant) provides a clear, bright band to anchor the calibration. Developed for h094 1?Ne(p,p).

### Procedure

#### Step 1: Obtain SRIM Stopping Power Tables
- **Best source**: InChaP (`physicscalculation/ionInteraction` on GitHub)
  - Ships full SRIM tables for common ions in Si
  - Tables at `InChaP/data/{ion}-data/Si.csv`
  - Format: Energy (MeV), MSP (MeV/(mg/cm2)), ProjRange, ...
- **Alternative**: IAEA stopping power API (`https://www-nds.iaea.org/stopping/api/data/ion:{ion}/target:{target}`)
  - Has measured data for Ne, O; F only to 0.5 MeV/u (must extrapolate)

#### Step 2: Choose DeltaE Detector Thickness
- Scan candidate thicknesses (e.g. 50, 80, 120 um)
- Convert to mg/cm2: `SI_THICK = thickness_um x 1e-4 x 2.336 x 1000`
- Compute SRIM DeltaE for the anchor species at known data E values
- Pick the thickness where computed curves best match data shape
- h094 result: **50 um** (80 um and 120 um gave worse Ne/F calibration tension)

#### Step 3: Calibrate sE and sdE from the Anchor Species
- The anchor species (e.g. 1?F) must be the **brightest, cleanest** band in the data
- Extract its peak positions: slice data at fixed E_res values, find the **peak bin** in DeltaE projection
  - [!!] Use **peak bin**, NOT weighted mean  --  multiple overlapping bands corrupt the weighted mean
  - Only use E_res slices where the anchor is clearly the dominant (brightest) peak
- Grid search (sE, sdE) to minimize RMS of `SRIM_predicted_dE - measured_dE_peaks`
  - Coarse 200x200 grid, then fine-tune ?2 around best -> target RMS < 15 ch
- [!!] Do NOT fit sE and sdE simultaneously from scratch  --  anchor sE independently from a known data point first (e.g. find where Ne sits at ~6050 ch -> sE = 6050 / E_res_MeV)

#### Step 4: Set Energy Windows from Kinematics
- Use `transfer.root` with `hit==1` gate for physics species (Ne, O)
- For beam contaminants (F, N): estimate from beam energy and known reactions
- [!!] **Data position may not match expected energy**  --  empirically adjust. h094: Ne beam at 9.0 MeV/u but data matched 10-12 MeV/u (unexplained charge state / effective energy issue)

#### Step 5: Build the Physics Species Cut from SRIM Curve
- Compute the SRIM DeltaE(E_res) curve for the target species in the energy window
- Scale to channel units using calibrated sE, sdE
- Build polygon: upper edge = center + half-width, lower edge = center - half-width, closed
- h094: Ne ?120 ch, O ?140 ch

#### Step 6: Data-Driven Shift for Secondary Species (if needed)
- The SRIM curve has correct shape but may need a uniform DeltaE offset
  - Cause: pulse height defect, ADC non-linearity differ between species
- Slice data inside the initial (unshifted) gate in E sectors
- At each slice: find DeltaE peak bin, compute `shift = data_peak - SRIM_center`
- Take **median** shift across all slices (robust to outliers from band contamination)
- Apply uniform DeltaE offset to the entire SRIM curve, preserving shape
- h094 O shifts: Tel 0 = +49 ch, Tel 1 = +69 ch, Tel 2 = +63 ch

#### Step 7: Save as TCutG
- Convert polygon CSVs to ROOT TCutG objects in the standard format

### Key Lessons
- **F band (brightest) is the anchor**  --  calibrate everything relative to it
- **Peak bin, NOT weighted mean**  --  critical when bands overlap
- **SRIM shape is trustworthy, absolute position may need shifting**  --  species-dependent offsets are real
- **sE and sdE are NOT the same for all species**  --  15-25% discrepancy between Ne and F; calibrate from F, accept that Ne needs empirical position adjustment
- **Median > mean for shift calculation**  --  outlier slices don't corrupt the result
- **Scan DeltaE thickness**  --  affects both curve shape and Ne/F calibration tension

---

## 5. Method 3: DBSCAN Refinement

**Best when:** You have an initial cut (from Method 1 or 2) and want to data-tighten the boundary using clustering. Works well for Ne-like bands where the core is dense and contamination is at the edges.

### Procedure

#### Step 1: Pre-gate with Initial Cut
- Use the SRIM or hand-drawn cut as a pre-filter
- Optionally widen the lower edge by ~100 ch to let DBSCAN see the species boundary and make its own decision
- Dump (E_res, DeltaE) for all surviving events to CSV

#### Step 2: Run DBSCAN on Dumped Events
- Normalize features (StandardScaler)
- Key parameters:
  - `eps`  --  neighborhood radius (controls tightness). Smaller = tighter boundary, more noise
  - `min_samples`  --  minimum cluster size. 50 works well for ~400K events
- Typical settings for HELIOS RDT data:
  - **Loose**: eps=0.05, min_samples=50 -> mean boundary width ~94 ch
  - **Tight**: eps=0.03, min_samples=50 -> mean boundary width ~66 ch

#### Step 3: Extract Boundary from Dominant Cluster
- DBSCAN labels: main cluster (label 0, typically 85-95% of events), noise (label -1), small clusters
- Bin events in E_res slices
- At each bin: find 97.5th and 2.5th percentile of DeltaE in the dominant cluster
- These form the upper and lower boundary of the banana polygon

#### Step 4: Convert to TCutG and Apply
- Polygon: upper boundary points (left to right) + lower boundary points (right to left), closed
- Save as TCutG in standard format
- Run Monitors.C and evaluate FOM

### Parameter Selection
- Run a parameter scan (e.g. 6 combinations of eps x min_samples) on one telescope
- Plot all resulting boundaries overlaid on the data
- Choose the combination that best balances yield (signal) and purity (forbidden gap)
- Apply that choice to all telescopes

### [!!] Practical Limits
- **Memory**: DBSCAN on >400K events requires >4 GB RAM. Spark has 122 GB -- no downsample needed. (If running on Pi/Mac with <8 GB, downsample to 400K max)
- **Tel-by-tel**: Parameters that work for Tel 0 may not work for Tel 2 (different band structure, overlaps)
- **Multi-band telescopes**: Tel 2 in h094 has 6 visible bands (Mg > Na > Ne > F > O > N at low E). DBSCAN fragments heavily here (64 clusters, 42% noise). Consider hand-tuning Tel 2 separately.

### Cut Comparison and Ring Analysis (Advanced)
After generating cuts at multiple tightness levels (e.g. cut1 = loose, cut2 = tight):

1. **Ring = cut1 - cut2**: Events passing the loose cut but NOT the tight cut
   - These are the marginal events: some real physics tail, some contamination
2. **Quantify the ring**: Plot DeltaE-E heatmap (logZ!) and count events by Ex region:

| Ex Region | cut1 (all) | cut2 (tight) | Ring (c1-c2) | Ring % |
|-----------|-----------|-------------|-------------|--------|
| g.s.      | count     | count       | count       | %      |
| 6 MeV     | count     | count       | count       | %      |
| Forbidden gap | count | count       | count       | %      |

3. If ring adds signal and contamination proportionally -> tighter cut doesn't help purity, only loses statistics
4. If ring is mostly contamination -> tight cut is justified

---

## 6. Monitors.C Integration

### Cut File Configuration
```cpp
TString rdtCutFile1 = "rdtCuts_Ne_srim.root";    // Primary species (Ne)
TString rdtCutFile2 = "rdtCuts_O_srim.root";      // Secondary species (O)
```

### How Gating Works
- `rdtgate1 = true` if event passes any cut in `rdtCutFile1` for the matching telescope
- `rdtgate2 = true` if event passes any cut in `rdtCutFile2`
- `hExCut1` = Ne-gated Ex spectrum (blue, drawn by `rdtgate1`)
- `hExCut2` = O-gated Ex spectrum (green, drawn by `rdtgate2`)
- `hEx` = ungated (all events with valid Ex)
- `heCalVzGC` (gated E vs Z) uses `rdtgate1 || rdtgate2` (union)

### Running ChainMonitors
- Enable desired runs in `ChainMonitors.C`
- Execute via ROOT batch: `root -l -b -q ChainMonitors.C` (or use the `run_chain_srim.sh` wrapper)
- Output canvas auto-saved to `Canvas/Canvas_YYYYMMDD_HHMMSS.png`
- Typical runtime: ~2-3 min for 43M events on Mac2020

### DeltaE-E Plot Convention
- hrdt2D: x = E_res (residual energy), y = DeltaE (energy loss)
- [!!] Future: use logz for RDT 2D histograms (Ryan's standing request)

---

## 7. Common Pitfalls

| Pitfall | Why It's Wrong | What to Do Instead |
|---------|---------------|-------------------|
| Rectangular gate | Cuts physics at banana corners, includes contamination at straight edges | Follow Bethe-Bloch curvature |
| Weighted mean for peak finding | Multiple overlapping bands corrupt the mean | Use peak bin (highest count) |
| Total event count as FOM | Includes all species equally | Use S2/N (signal2/total) |
| Z2A scaling for band positions | Effective charge corrections at 4-10 MeV/u make this 7-9% off | Use empirical peak positions or SRIM tables directly |
| Same cut parameters for all telescopes | Each telescope has different gain, resolution, band structure | Treat each telescope independently |
| Trusting 1D projections | Overlapping bands create misleading peaks in 1D | Always check the 2D scatter |
| Convex hull for banana cuts | Bethe-Bloch is concave -> hull includes contamination | Use percentile boundary or hand-traced polygon |
| Fitting both sE and sdE simultaneously | Can converge to wrong minimum | Anchor sE from a known data point first |
| Adding ADC channels from different detectors | Different gains make sum physically meaningless | Use E_res only (not E_res + DeltaE) |

---

## 8. File Locations

### h094 1?Ne(p,p) Cut Files (Mac2020)
- `~/digios_h094/analysis/working/rdtCuts_Ne_srim.root`  --  SRIM Ne cuts
- `~/digios_h094/analysis/working/rdtCuts_O_srim.root`  --  SRIM O cuts
- `~/digios_h094/analysis/working/rdtCuts_Ne_dbscan.root`  --  DBSCAN loose (eps=0.05)
- `~/digios_h094/analysis/working/rdtCuts_Ne_dbscan_tight.root`  --  DBSCAN tight (eps=0.03)

### h095 11C(d,p)12C Cut Files (Mac2020)
- `~/digios_11C_2/analysis/working/rdtCuts_12C_6.root`  --  HELIOS v12 cut
- `~/digios_11C_2/analysis/working/ryan_para/rdtCuts_12C_3.root`  --  Ryan's hand-drawn _3 cut

### Scripts (were on Pi ~/workspace/ -- Pi retired 2026-04-17; check Spark ~/workspace/)
- `~/digios_11C_2/analysis/working_Helios/h094/rdt_banana_all_tels.py`  --  empirical peak tracing + polynomial cut generator (h094)
- [!!] DBSCAN and SRIM cut-generation scripts were session-temporary (`/tmp/`)  --  recreate from scratch for new experiments using procedure in sections 4 and 5

---

## 9. Quick Decision Tree

```
Is the target species band well-separated from other bands?
??? YES -> Method 1 (Hand-Drawn Banana)
?         ??? Ex-gate -> identify physics in DeltaE-E
?         ??? Overlay all events -> find the gap
?         ??? Trace banana through the gap
?
??? NO (bands overlap heavily)
    ??? Is there a strong anchor band (brightest species)?
    ?   ??? YES -> Method 2 (SRIM Simulation-Assisted)
    ?   ?         ??? Get SRIM tables (InChaP/IAEA)
    ?   ?         ??? Calibrate sE/sdE from anchor
    ?   ?         ??? Build cut from SRIM curve ? half-width
    ?   ?
    ?   ??? NO -> Hand-draw best guess, then refine with Method 3
    ?
    ??? Want to tighten an existing cut data-adaptively?
        ??? Method 3 (DBSCAN Refinement)
                ??? Pre-gate -> dump events -> DBSCAN
                ??? Extract percentile boundary from main cluster
```

---

## [!!] Key Lesson: Recoil Species Change Between Characterization and Physics Runs

For experiments using radioactive beams with a stable-beam characterization run:
- **Characterization run** (e.g. 30Si beam): recoil = 31Si → specific dE-E band position
- **Physics run** (e.g. 31Si beam): recoil = 32Si → DIFFERENT dE-E band position

The recoil mass/Z changes between runs, shifting the Bethe-Bloch band in dE-E space.
**Do NOT transfer characterization gates directly to physics runs** — they will be offset.
Always generate new gates from the physics run data (use Ex-gated events from known states).

_Source: h096 rdt_compare_gates.py — confirmed 30Si→31Si and 31Si→32Si bands differ in dE-E._

## See Also

- `HELIOS_Analysis_Workflow.md`  --  RDT cut usage in Monitors.C, plot indexing convention
- `HELIOS_Detector_Geometry.md`  --  RDT channel mapping (IDs 100-107, Module 3 HV)
- `HELIOS_PV_Reference.md`  --  HV PV names for RDT channels (u300-u315)
- `expMemory_h094.md` / `expMemory_h095.md` / `expMemory_h096.md`  --  experiment-specific cut files and FOM results
- `MEMORY.md` -> "RDT Cut Reference"  --  summary of hand-drawn vs ML FOM results

---

_Created: 2026-03-27 by HELIOS_  
_Updated: 2026-04-23 (h096-specific values moved to expMemory_h096.md)_  
_Sources: h094 analysis (2026-03-26/27), h095 analysis (2026-03-13/14), MEMORY.md_
