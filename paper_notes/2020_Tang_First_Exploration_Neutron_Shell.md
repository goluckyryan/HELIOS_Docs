# First Exploration of Neutron Shell Structure Below Lead and Beyond N=126

**Authors:** T.L. Tang, B.P. Kay, C.R. Hoffman, J.P. Schiffer, D.K. Sharp, L.P. Gaffney, S.J. Freeman, M.R. Mumpower, et al.
**Journal:** Phys. Rev. Lett. 124, 062502 (2020)
**arXiv:** 2001.00976
**PDF:** `~/publications/2020_Tang_First_Exploration_of_Neutron.pdf`
**Instrument:** ISS — ISOLDE Solenoidal Spectrometer (CERN, sister instrument to HELIOS)
**Reaction:** 206Hg(d,p)207Hg in inverse kinematics
**Facility:** ISOLDE Solenoidal Spectrometer (ISS) at CERN

---

## Why This Paper Matters

This is the **first-ever measurement of single-neutron structure** in the Z<82, N>126 region of the nuclear chart. This region is:

1. **Crucial for r-process nucleosynthesis** -- the N=126 shell closure creates the bottleneck responsible for the A~195 peak in solar system elemental abundances
2. **Almost completely unexplored** -- prior to this work, nothing was known about single-neutron excitations in any nucleus with Z<82 and N>126
3. **Experimentally very difficult** -- fragmentation and ISOL methods produce only low-intensity beams of these neutron-rich nuclei below 208Pb

## The Experiment

- **Beam:** Radioactive 206Hg (46+), produced at ISOLDE/CERN
  - Rate: 3-8 x 10^5 pps
  - Energy: 7.38 MeV/u (1.52 GeV total)
  - Contamination: <2% 130Xe
- **Target:** Deuterated polyethylene (CD2), 165 ug/cm2
  - Replaced every ~4 hours due to beam damage (20 targets used in 82 hours)
- **Spectrometer:** ISS at 2.5 T magnetic field
  - Based on the **HELIOS technique** pioneered at ANL (Ref [37])
  - Used the HELIOS detector system (Si array)
  - Q-value resolution: ~140 keV FWHM
- **Statistics:** ~6000 protons identified from the (d,p) reaction
- **Angular coverage:** theta_cm < ~40 degrees

### Key Technical Points

- ISS is explicitly described as "based on a technique pioneered at Argonne National Laboratory" -- i.e., **us** (HELIOS)
- Factors of 2-3 improvement in Q-value resolution vs. conventional methods
- Data acquisition gated on REXEBIS timing to suppress background from fusion-evaporation alpha decays
- Background: predominantly prompt protons from beam + 12C fusion-evaporation

## Results

### States Observed in 207Hg

Seven states below 3 MeV, populating neutron orbitals beyond N=126:

| E (keV) | l | J^pi    | Orbital | S (normalized) |
|---------|---|---------|---------|----------------|
| 0 (g.s.)| 4 | 9/2+    | 1g9/2   | 0.82(13)       |
| 1195(20)| 2 | (5/2+)  | 2d5/2   | 0.47(9)        |
| 1600(45)| 2 | (5/2+)  | 2d5/2   | 0.13(2)        |
| 1810(20)| 2 | (5/2+)  | 2d5/2   | 0.42(7)        |
| 1960(30)| 0 | (1/2+)  | 3s1/2   | =1.00 (norm)   |
| 2335(20)| 2 | (3/2+)  | 2d3/2   | 1.00(17)       |
| 2530(20)| 4 | (7/2+)  | 1g7/2   | 0.62(12)       |

- **Not observed:** 0i11/2 (l=6, ~0.8 MeV expected) -- cross section too small at 7.38 MeV/u
- **Not observed:** 0j15/2 (negative parity) -- yields even smaller
- **2d5/2 fragmented** into 3 states -- attributed to coupling with 2+ core excitation in 206Hg (~1.1 MeV)
- 2d5/2 centroid: 1500(50) keV, summed C2S = 1.02(17)

### Sum-Rule Analysis

Spectroscopic factors normalized so S(3s1/2) = 1.00. Summed strengths:
- 1g9/2: 0.82(13) -- bulk of strength in g.s.
- 2d5/2: 1.02(14) -- distributed across 3 fragments
- 3s1/2: 1.00 (normalization)
- 2d3/2: 1.00(17) -- single state
- 1g7/2: 0.62(12) -- notably low, suggesting fragments at higher E

### DWBA Analysis

- Code: **Ptolemy** [45] (our old friend!)
- Bound-state form factors: Kay, Schiffer, Freeman prescription [46]
- Optical potentials: Koning-Delaroche [47] and An-Cai [48]
- Angular distributions relatively indistinct at 7.38 MeV/u
- l-assignments tentative, based on chi2 minimization
- Cross section uncertainties: ~30% absolute, <5% relative

## Physics Implications

### Shell Structure Extrapolation

- Woods-Saxon potential fitted to 207Hg + 209Pb data
- Extrapolated binding energies along N=127 isotonic chain toward r-process path
- **Key prediction:** Below Z~64 (Gd), N=127 nuclei become unbound
- Between Z=64-68 (Gd-Er): no bound excited states expected
- If only a bound 9/2+ g.s. exists, neutron capture is very difficult -- the N=126 bottleneck is MORE severe than N=82

### Comparison with Models

- 21 r-process models compared (grey band in Fig. 4)
- FRDM2012 agrees well with Woods-Saxon extrapolation
- UNEDF0 represents the other extreme
- New data at Z=80 provides a crucial anchor point between Z=82 (Pb) and the r-process path

### The N=126 Bottleneck

- R-process path crosses N=126 around Z~54
- Capture beyond N=126 starts at Z~64 +/- 2
- Without bound excited states, statistical capture assumptions fail
- Direct capture requires odd-parity phase shifts (l=3 or 5) -- but these orbitals are far from threshold
- **Conclusion:** N=126 bottleneck is more significant than N=82

## HELIOS Connection

This paper explicitly validates the solenoidal spectrometer technique:
- ISS at CERN is a **direct descendant of HELIOS** at ANL
- Uses the same silicon detector array concept
- Demonstrates the technique works with very exotic beams (206Hg at 3-8 x 10^5 pps)
- The Q-value resolution (~140 keV) is comparable to what HELIOS achieves

## Key References for Follow-Up

- [37] Lighthall et al., NIM A 622, 97 (2010) -- HELIOS instrument paper
- [46] Kay, Schiffer, Freeman, PRL 111, 042502 (2013) -- bound-state prescription
- [47] Koning & Delaroche, NPA 713, 231 (2003) -- global OMP (we use this in Ptolemy)
- [18] Manning et al., PRC 99, 041302(R) (2019) -- N=82 comparison

---

## Physics Understanding

### Why the N=126 bottleneck is worse than N=82
At N=82, the first orbitals beyond the shell closure include odd-parity p orbitals (2p1/2, 2p3/2) which can facilitate neutron capture via direct s-wave or p-wave processes with E1 transitions. At N=126, the first available orbitals are 1g9/2 (l=4) and 2d5/2 (l=2) -- high angular momentum. Direct neutron capture requires E1 multipoles (odd parity, l change of 1), but the nearest odd-parity single-neutron excitations (0i11/2 at ~0.8 MeV, 0j15/2 at ~1.2 MeV) are energetically far from the neutron threshold in neutron-poor N=127 nuclei. Higher multipoles are strongly suppressed. As Z decreases below ~64 (Gd), the Woods-Saxon extrapolation predicts no bound excited states at all -- just a 9/2+ ground state. Without bound excited states and with very low continuum level density, both statistical and direct capture mechanisms are severely hindered. The r-process essentially stalls at N=126.

### 2d5/2 fragmentation from core coupling
The 2d5/2 single-particle strength fragments into 3 states (1195, 1600, 1810 keV) rather than sitting in a single level. This arises from coupling between the valence neutron and the 2+ core excitation of 206Hg (~1.1 MeV). When the single-particle energy is close to the core excitation energy, the particle-core coupling mixes the configurations, splitting the strength. The same pattern appears in 211Po (Z=84, N=127) where the 210Po core 2+ is also ~1.1 MeV. The centroid at 1500 keV and summed C2S = 1.02 confirm the full single-particle strength is accounted for.

### s-orbital behavior near zero binding
As nuclei approach the drip line (decreasing Z along N=127), binding energies decrease. The 3s1/2 orbital (l=0) rises in energy less rapidly than higher-l states because its wavefunction has no centrifugal barrier and extends further spatially -- it "feels" the potential edge less. This is analogous to the Thomas-Ehrman shift in mirror nuclei. The consequence: 3s1/2 will be the last orbital to become unbound as Z decreases. However, being l=0, it can only participate in capture via higher multipoles (not E1 from s-wave), limiting its astrophysical impact.

### Robustness of N=126 closure
The normalized spectroscopic factors sum to ~1.0 for each orbital (1g9/2: 0.82, 2d5/2: 1.02, 3s1/2: 1.00, 2d3/2: 1.00), except 1g7/2 (0.62 -- missing strength at higher Ex). Near-unity sum rules indicate these are clean single-particle excitations with minimal configuration mixing. The N=126 shell closure remains robust at Z=80 (Hg), two protons below the doubly-magic 208Pb. The 2+ energies in even-even N=126 isotones remain essentially constant from Pb through Th (Z=90), further supporting shell robustness.

---

*Notes by Master HELIOS, 2026-04-16*
*This is Ryan's paper. First author. PRL. Incredible work.*
