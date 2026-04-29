# Paper Notes: Schiffer, Kay, Chen 2022 -- Single-Nucleon Energies Changing with Nucleon Number

**Citation:** J.P. Schiffer, B.P. Kay, J. Chen, Phys.Rev.C 105, L041302 (2022) [Letter]
**DOI:** 10.1103/PhysRevC.105.L041302
**PDF:** `~/publications/2022_Schiffer_SPE_NucleonNumber.pdf`
**Read:** 2026-04-28 (full PDF)
**Note:** Schiffer's last paper — a career-spanning synthesis.

---

## Core Observation

Effective single-particle energies (ESPEs) across the nuclear chart, when plotted on a **logarithmic scale** in nucleon number, show a remarkably simple and consistent pattern:

1. **np interaction (panel a):** Neutron states become more bound as proton number increases (and vice versa). Slopes are steep and **negative** (~-21 MeV per unit log N). Strong attraction. Consistent with pion-exchange dominance of np force.

2. **T=1 interaction, same orbit filling (panel b, green):** Same-species nucleon states change slowly and are **slightly repulsive** (~-4 MeV per unit log N) when only the orbit in question is filling.

3. **T=1 interaction, multiple orbits filling (panel b, red):** When multiple orbitals fill simultaneously (e.g., Ni, Sn isotopes), the slope **reverses sign** to slightly repulsive/positive (+4.6 MeV per unit log N).

**The factor-of-four ratio** between np slopes and T=1 slopes is consistent with the well-known asymmetry term in the semi-empirical mass formula and the symmetry term in the Woods-Saxon optical potential.

---

## Data Scope

- 33 different orbitals, A = 16–208
- ~200 data points total
- Mostly spherical nuclei; one deformed case (ν[521] rare-earth chain)
- Both particle and hole states treated equivalently
- Fragmented strength: spectroscopic-factor-weighted centroid used (Baranger definition)

---

## Key Equations

**Baranger centroid (for T=1 segments):**
```
E^{π,ν}_j = (E+_j G+_j + E-_j G-_j) / (G+_j + G-_j)
where G+_j + G-_j = 1.0
```

**Logarithmic slopes (Table I):**
| Category | dE/d(ln N) (MeV) |
|----------|-----------------|
| np (panel a) | -21.3 ± 3.7 |
| T=1, one orbit | -4.1 ± 1.3 |
| T=1, several orbits | +4.6 ± 1.5 |

---

## Physical Interpretation

### Why logarithmic scale?
Each added nucleon contributes equally to the overall binding field → slope per *fractional* change in nucleon number is approximately constant → logarithmic dependence is natural.

### Woods-Saxon explanation
Two competing effects when neutrons are added to Sn isotopes (proton state):
- **Symmetry term** (N-Z)/A → weakens proton binding (repulsive)
- **Growing radius** A^{1/3} → dilutes potential → also weakens binding

For **neutron states**: these two effects nearly cancel → very small slope (factor 4 weaker)
For **proton states**: both effects reinforce each other → steeper slope

But Schiffer notes: *"One should not regard this as an 'explanation,' rather that the empirical parametrization does describe the data, reasonably well."* — deliberately cautious about claiming the WS potential as a physical explanation.

### Connection to two-body matrix elements
The inset in Fig. 2 shows the monopole M₀ of empirical 2BME multiplets (from a previous Schiffer survey of two-nucleon spectra outside closed shells). The M₀ values confirm the same pattern:
- Identical-orbit multiplets (j₁=j₂): M₀ mostly < 0 (slightly repulsive)
- Non-identical multiplets (j₁≠j₂, np): M₀ > 0 (attractive)
This validates that the pattern seen in Fig. 1 is not an artifact of the Baranger interpolation.

---

## What's Genuinely New

The **logarithmic scale** is the key insight — this representation reveals that the slopes are approximately constant across an order of magnitude in nucleon number. This consistency "has not been explicitly noted before, though it may have been implicitly assumed." It's elegant and data-driven.

This is not a new model — it's a **new way of seeing** existing data that reveals underlying universality in the nuclear force.

---

## Connections to HELIOS Program

- **Kay and Chen are co-authors** — direct link to the HELIOS experimental team
- The ESPE framework is used in h096 (³¹Si(d,p)³²Si) analysis to interpret where the 0d3/2 orbital sits
- The Sn isotope data (Kay et al., Szwec et al.) contributed to the database in Fig. 1
- The 136Xe(d,p) data (Kay 2011) contributed via the νh9/2 and νi13/2 centroids
- The pattern shown here is why tracking ESPE evolution is a primary HELIOS science goal

---

## Critical Reading Notes

**Strong points:**
- Purely data-driven; minimal model assumptions
- Breadth: 33 orbitals, A=16-208, consistent treatment
- The logarithmic representation is a genuine insight
- Confirming that monopole 2BME data gives the same pattern

**Points worth probing:**
- The paper explicitly acknowledges that when strength is fragmented, the centroids may not be "true observables" (citing the SF debate). They note past works show the uncertainty is mostly smaller than the point-to-point variations — but this is not demonstrated here, just asserted.
- The deformed case (ν[521]) is included but treated the same as spherical cases — deformation mixes single-particle states differently and the centroid meaning is less clean.
- The Woods-Saxon "explanation" is presented cautiously and correctly — it's a parametrization, not a first-principles derivation. The authors are clear about this, which is good.
- Only even-even nuclei used as targets — odd-A neighbors may behave differently due to pairing.

---

## Legacy

This paper synthesizes ~70 years of nuclear structure data into a single coherent picture. The simplicity of the result — a universal logarithmic dependence of ESPE on nucleon number — is striking. It provides the empirical foundation for understanding shell evolution without requiring specific models.

As Schiffer's last paper, it reflects his career philosophy: let the data speak, be suspicious of over-interpretation, and look for simple patterns in large datasets.

---

_Created: 2026-04-28_
