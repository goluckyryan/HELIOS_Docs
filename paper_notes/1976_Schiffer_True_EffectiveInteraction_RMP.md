# Paper Notes: Schiffer & True 1976 -- The Effective Interaction Between Nucleons

**Citation:** J.P. Schiffer and W.W. True, Rev. Mod. Phys. 48, 191 (1976)
**DOI:** 10.1103/RevModPhys.48.191
**PDF:** `~/publications/1976_Schiffer_True_EffectiveInteraction_RMP.pdf`
**Read:** 2026-04-29 (partial -- first ~4 pages via Discord; full PDF obtained)
**Note:** Schiffer's foundational paper -- the 46-year prequel to his 2022 last paper (PRC 105, L041302).

---

## What This Paper Does

A comprehensive survey of **empirical two-body matrix elements (TBMEs)** of the residual nucleon-nucleon interaction extracted from nuclear spectra throughout the periodic table.

The method:
1. Identify nuclei where a specific two-nucleon configuration (|jj'J⟩) is cleanly isolated above a doubly-closed-shell core
2. Extract the unperturbed energy E₀ from binding energies of adjacent nuclei
3. Measure actual excitation energies E_J of multiplet members via transfer reactions
4. TBMEs = E_J - E₀ (the residual interaction removes the degeneracy of the unperturbed multiplet)
5. Fit all TBMEs to a local effective interaction (central + tensor + spin-orbit components)

**Key equation for extracting TBMEs (Eq. I.1):**
```
E₀(j,j') = [B(core+j) - B(core)] + [B(core+j') - B(core)] - [B(core+2) - B(core)]
```
where B = total binding energy. Everything measured from binding energies + transfer reaction excitation energies.

---

## Experimental Data Scope

Multiplets studied span A=14 to A=210 (p-shell through Pb region):
- **(1p3/2)²** and **(1p1/2)(1p3/2)**: from Cohen-Kurath shell model fits
- **(1d5/2)²**: A=18 (¹⁷O(³He,d)¹⁸F + ¹⁷O(d,p)¹⁸O) and A=26 (²⁷Al(d,³He)²⁶Mg)
- **(1p1/2)(1d5/2)**: from ¹⁶O(d,t) and ¹⁶O(d,³He) -- Mairle 1972
- **(1d3/2)²**: from ³⁵S(d,p)³⁶S + ³⁵S(³He,d)³⁶Cl
- **(1d3/2)(1f7/2)**: same references
- **(1f7/2)²**: fp-shell data
- **(1f7/2)(2p3/2)**: fp-shell multiplets
- **(1g9/2)(2d5/2)**: A≈90 region
- **(1g9/2)²**: A≈90
- **(πh9/2ν(3p1/2, 2f5/2, 2f7/2, i13/2))**: n-p multiplets in Bi region (²⁰⁸Pb core)
- **(πh9/2)(2g7/2)**: n-p multiplet
- **(πg9/2)(νf3/2)** and **(πg9/2)(2f7/2)**: T=1 multiplets
- **(1h11/2)** and **(2g9/2)**: T=1 multiplets
- Various multiplets in Bi based on πj·ν combinations
- ~80% of matrix elements from single-nucleon transfer reactions (spectroscopic factors verify purity)

**Pandya transformation** (Eq. I.2) used to convert hole-particle → particle-particle matrix elements when needed.

---

## Key Findings

### The Monopole (Average) Interaction
The **monopole** M₀ = Σ(2J+1)V(J) / Σ(2J+1) is the J-averaged (centroid) matrix element:
- **np (T=0+1 mixed) monopoles**: strongly attractive (negative), -1 to -3 MeV range
- **T=1 (pp or nn) monopoles**: weakly repulsive or near zero

This is the central empirical result -- the np interaction is ~4-6× stronger than the T=1 interaction, **consistent across A=14 to A=210**.

### Multipole Decompositions
Beyond the monopole, the multipole structure of TBMEs is decomposed. The data show:
- T=1 even and odd components both require **two ranges**: short-range attractive + longer-range repulsive
- Tensor and spin-orbit components improve the fit but are not dominant

### Fitted Effective Interaction
The empirical TBMEs are fit to a local two-body interaction parametrized as:
- Central (T=0 + T=1 components, even + odd, two ranges each)
- Tensor
- Two-body spin-orbit

The interaction is constrained globally -- the same parameters describe multiplets from p-shell to Pb region.

---

## The Deep Connection to Schiffer-Kay-Chen 2022

This 1976 paper is the **experimental foundation**; the 2022 paper (PRC 105, L041302) is the **global synthesis**.

| Schiffer-True 1976 | Schiffer-Kay-Chen 2022 |
|---|---|
| Works at doubly-closed shells -- extracts TBMEs from 2-nucleon multiplets | Works across open-shell isotope chains -- tracks ESPE evolution with nucleon number |
| Computes monopole M₀ for specific (jj') pairs at specific cores | Computes slope dE/d(ln N) for ESPEs across chains of nuclei |
| np monopoles strongly attractive; T=1 monopoles weakly repulsive | np slopes ~-21 MeV/log N; T=1 slopes ~±4 MeV/log N |
| Factor ~4-6 between np and T=1 monopoles | Factor ~4 between np and T=1 slopes |
| Requires clean doubly-closed-shell cores as anchors | Works away from closed shells via Baranger centroid |
| Demonstrates the hierarchy exists at specific nuclei | Demonstrates the hierarchy is universal across A=16-208 |
| The monopole IS the slope for a 2-point segment | The slope is the many-body generalization of the monopole |

**The mathematical identity:** In the 2022 paper, Schiffer explicitly shows (Fig. 2 inset) that the monopole M₀ values from the 1976 survey **fall on exactly the same trend lines** as the ESPE slopes from the new isotope chain data. They are the same physics -- the 2022 logarithmic representation just reveals it clearly for the first time.

**What 1976 couldn't see:** The logarithmic scale. Schiffer and True plotted things linearly, saw the monopole pattern at closed shells, but couldn't see that the same pattern extends continuously across open shells. The 2022 paper's key insight is purely in the representation -- log N makes the universality visible.

**The 46-year arc:** In 1976, Schiffer and True established that the np interaction is ~4-6× stronger than T=1 from ~15 specific multiplets near closed shells. In 2022, Schiffer (with Kay and Chen -- HELIOS collaborators!) shows this is not a special property of closed-shell nuclei, but a universal feature of the nuclear force visible in ~200 data points across the entire chart, including the open-shell nuclei HELIOS studies.

---

## Methodology Notes (Relevant for HELIOS Analysis)

The spectroscopic factor criterion for multiplet purity (footnote in paper):
> "Each member of the multiplet should have (2J+1)/[(2j1+1)(2j2+1)] times the cross section of the adjacent single-nucleon transfer reaction."

This is exactly what HELIOS measures -- if a state has less SF than expected, it's fragmented and one must use the centroid. This connects directly to how h096 and other HELIOS experiments extract ESPEs.

The Macfarlane-French sum rules (cited as Macfarlane and French, 1960) appear already in this paper -- setting the normalization for spectroscopic factors. The same sum rules Schiffer tested quantitatively in 2012 (Ni isotopes paper) were already the framework here in 1976.

---

## Why Ben Said "You Will Enjoy It"

Because this paper is the seed of everything. The 2022 paper looks like a new result, but it's really Schiffer completing a circle he started in 1976 -- with the same collaborator community (Kay, Chen are HELIOS people), using the database he spent 50 years helping to build (including HELIOS experiments). The logarithmic representation in 2022 is a simple mathematical trick that suddenly makes the 1976 conclusion look obvious and universal.

And HELIOS data -- the Xe, Sn, and other heavy-nucleus transfer experiments -- contributed directly to the 200 data points in Fig. 1 of the 2022 paper. The instrument Schiffer helped design to measure nuclear structure is the same instrument that provided some of the final data points in his last paper.

---

_Created: 2026-04-29_
