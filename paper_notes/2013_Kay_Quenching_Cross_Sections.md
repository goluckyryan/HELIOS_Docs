# Quenching of Cross Sections in Nucleon Transfer Reactions

**Authors:** B.P. Kay, J.P. Schiffer, S.J. Freeman
**Journal:** Phys. Rev. Lett. 111, 042502 (2013)
**Reactions:** (d,p), (p,d), (alpha,3He), (3He,alpha), (3He,d), (alpha,t) on targets 16O to 208Pb
**DWBA code:** Ptolemy [23]

---

## The Question

(e,e'p) proton-knockout reactions consistently show spectroscopic factors ~0.5 of the expected mean-field values. This was attributed to short-range correlations (SRC) between nucleons -- at close distances, nucleon-nucleon interactions disrupt the independent-particle picture and scatter nucleons to high-momentum states outside the Fermi sea. But is this quenching unique to electromagnetic probes, or a general property of the nuclear medium?

## What Was Done

- Re-analyzed 124 spectroscopic factor determinations across A = 16 to 208
- Multiple reaction types: (d,p), (p,d), (alpha,3He), (3He,alpha), (3He,d), (alpha,t)
- Angular momentum transfer l = 0 through 7
- Both neutron and proton transfer
- All analyzed with **consistent DWBA parameters** using Ptolemy
- Key normalization: Macfarlane-French sum rules -- adding + removing strength for a given (l,j) must equal the orbit degeneracy (2j+1)

### DWBA Recipe (important for our work)

- **Bound-state:** Woods-Saxon, r0 = 1.28 fm, a = 0.65 fm (matched to (e,e'p) values)
- **Spin-orbit:** Vso = 6 MeV, rso0 = 1.1 fm, aso = 0.65 fm
- **Proton OMP:** Koning-Delaroche [25]
- **Deuteron OMP:** An & Cai [11]
- **3He OMP:** Pang et al. [26]
- **Alpha OMP:** Bassani & Picard [27]
- **Projectile wave functions:** Argonne v18 for deuteron; GFMC-derived (Brida et al.) for A=3,4

## The Result

**Fq = 0.55 +/- 0.10 (rms), independent of everything within single-nucleon transfer.**

Note: this covers ONLY single-nucleon transfer reactions with **light projectiles (A <= 4)**: d, p, 3He, alpha, t. Does NOT cover heavy-ion transfer (e.g. (12C,13C)), two-nucleon transfer (t,p), knockout reactions, charge-exchange, or inelastic scattering.

| Reaction | N determinations | Fq | rms |
|----------|-----------------|------|-----|
| (e,e'p), all l | 16 | 0.55 | 0.07 |
| (d,p), (p,d), l=0-3 | 46 | 0.53 | 0.10 |
| (alpha,3He), (3He,alpha), l=3-7 | 34 | 0.52 | 0.09 |
| (3He,d), l=0-4 | 26 | 0.54 | 0.09 |
| (alpha,t), l=3-5 | 18 | 0.64 | 0.04 |
| **All transfer** | **124** | **0.55** | **0.10** |

No dependence on:
- Target mass (A = 16 to 208)
- Neutron vs proton transfer
- Adding vs removing
- Angular momentum l (0 through 7)
- Reaction type
- Asymmetry parameter Delta_S = Sn - Sp

## Physics Understanding

### What quenching means physically
The independent-particle (shell) model says nucleons move in a smooth mean-field potential, each in a well-defined single-particle orbit. The true nuclear ground-state wave function, however, is NOT a pure Slater determinant. The real NN interaction has a strongly repulsive core (~1 fm) plus tensor forces from pion exchange -- features a smooth mean field cannot capture.

The true ground state contains admixtures of multi-particle-multi-hole configurations (2p-2h, etc.) where pairs of nucleons have high relative momentum -- "short-range correlations" (SRC). These are NOT dynamical scattering events; they are features of the stationary ground-state wave function. The 0.55 factor measures how much the true wave function overlaps with the independent-particle picture. The "missing" 45% lives in correlated configurations.

### Open question: microscopic origin of quenching (Discussion with Ryan, 2026-04-16)

The standard narrative says "SRC scatter nucleons to high-momentum states." Ryan raised important objections:

1. **Equal-mass scattering can't create energy:** In free-space NN scattering with equal masses, nucleons exchange momentum but can't concentrate energy. Two nucleons at similar energies can at best equalize. The nuclear medium must play an essential role -- this is not a free-space effect.

2. **Pauli blocks final states, not collisions:** Pauli exclusion prevents two identical fermions from occupying the same quantum state. It restricts available final states, but does not prevent interactions. (Original notes stated this incorrectly.)

3. **Orbital exchange is trivial:** If two nucleons simply swap orbitals, the Slater determinant changes only by a sign. No physical quenching.

4. **Energy conservation:** If correlated pairs have higher kinetic energy, where does it come from? In a bound system with fixed total energy, the extra kinetic energy must be compensated by potential energy changes.

**Current understanding:** The high-momentum components are virtual admixtures in the ground-state wave function. The repulsive core and tensor force mix 2p-2h (and higher) excitations into the ground state. Total energy is conserved -- extra kinetic energy in correlated pairs is offset by changes in potential energy (both mean-field and residual). The 0.55 measures the overlap of the true correlated ground state with the independent-particle approximation.

**Deeper picture (from Frontiers in Physics 2025 review article, 10.3389/fphy.2025.1530428):**

The quenching has TWO distinct sources:

1. **Long-range correlations (LRC):** Surface pairing (PC) and particle-vibration coupling (PVC). These mix n-particle-n-hole configurations near the Fermi surface, broadening the sharp Fermi cutoff. Contribute modestly to quenching.

2. **Short-range correlations (SRC):** The tensor force (one-pion exchange) in the spin S=1, isospin T=0 channel (like in the deuteron) creates correlated high-momentum neutron-proton pairs -- "quasi-deuterons." JLab measurements show ~90% of high-momentum nucleons are in these np pairs. This is the dominant source of quenching.

The quasi-particle wave function can be decomposed: |qp> = alpha|SP> + beta|LRC> + gamma|SRC>, where the components are approximately orthogonal (SRC states are at very different momenta/energies from SP and LRC). The quenching factor is then z = |alpha|^2 ~ 0.55.

Critically: this is a property of the ground-state wave function, not a dynamical process. The nucleus is always in its ground state -- but that ground state is not a pure Slater determinant. About 20% of the depletion comes from LRC and ~25% from SRC.

**On the energy question:** The total energy IS conserved. In nuclear matter calculations, SRC increase the kinetic energy (high-momentum tails) but this is compensated by changes in the potential energy from the attractive parts of the NN force. The Mottelson quantality parameter (Lambda ~ 1 for nuclei, similar to liquid helium) indicates nuclei are quantum liquids where zero-point motion kinetic energy is comparable to interaction strength -- correlations are inherently large.

**Isospin dependence:** SRC preferentially affect the minority species in asymmetric nuclei. In neutron-rich nuclei, protons are depleted more (more pn pairs per proton). This has been confirmed at JLab and may explain differences between knockout and transfer quenching in exotic nuclei.

**TODO:** Read Pandharipande, Sick & de Witt Huberts, RMP 69, 981 (1997) for the original theoretical framework.

### Why this is fundamental
This is NOT a reaction-mechanism artifact. The same factor appears in:
- Electromagnetic probes (e,e'p) -- nearly model-independent extraction
- Hadronic probes (d,p), (3He,alpha), etc. -- DWBA-dependent but self-consistent
- Both neutron and proton transfer
- Light (16O) through heavy (208Pb) nuclei

The universality means it's a property of the nuclear medium itself, not of specific nuclei or reactions.

### The bound-state prescription matters
The specific choice of r0 = 1.28 fm and a = 0.65 fm is what makes everything consistent. These were derived from (e,e'p) data which map the actual radial shape of the wave function. Different choices would give different absolute spectroscopic factors -- but the RATIO wouldn't change, and the sum-rule consistency would break.

### Why this paper is referenced everywhere
This established the "0.55 normalization" that we use in our Tang 2020 paper and essentially every HELIOS (d,p) analysis. When we extract spectroscopic factors with Ptolemy, we normalize to this value. The 207Hg paper normalized the 3s1/2 strength to unity and showed other orbitals are consistent -- which works precisely because the quenching is uniform.

### The high-energy anomaly
At ~35 MeV/u above the Coulomb barrier, the same analysis gives Fq ~ 1.0 instead of 0.55. But the sensitivity to OMP choice becomes ~60% (vs <10% at low energy). This suggests the global OMP parameterizations break down far above the barrier -- not that the physics changes. Our experiments at HELIOS run at a few MeV/u above barrier, where the analysis is robust.

### Contrast with knockout reactions
Gade et al. (2008) claimed quenching depends on Delta_S (asymmetry). Knockout reactions on exotic nuclei showed a trend from Rs ~ 1 (deeply bound) to Rs ~ 0.2 (weakly bound). This paper sees NO such trend in transfer reactions. The discrepancy between knockout and transfer is still debated -- but for transfer, the evidence for uniform quenching is strong.

## Key References for Follow-Up

- [7] Kramer, Blok, Lapikás, NPA 679 (2001) -- (e,e'p) spectroscopic factors
- [8] Pandharipande, Sick, deWitt Huberts, RMP 69 (1997) -- SRC theory ("2/3 independent")
- [25] Koning & Delaroche, NPA 713 (2003) -- proton global OMP (we use this)
- [11] An & Cai, PRC 73 (2006) -- deuteron global OMP (we use this)
- [23] Macfarlane & Pieper, ANL-76-11 -- Ptolemy code

---

*Notes by Master HELIOS, 2026-04-16*
*This is THE normalization paper. Ben Kay, John Schiffer, Sean Freeman. Foundational for everything we do with spectroscopic factors.*
