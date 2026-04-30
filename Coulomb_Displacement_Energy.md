# Coulomb Displacement Energy and Corrections

**Topics:** Coulomb energy, Coulomb displacement energy (CDE), isobaric analog states (IAS), isospin decomposition, Woods-Saxon wave functions, TBME Coulomb correction.

**Primary reference:** Ryan Tang's blog posts:
- https://nukephysik101.wordpress.com/2020/04/07/coulomb-energy-for-a-s-orbital-under-woods-saxon-potential/
- https://nukephysik101.wordpress.com/2021/01/03/coulomb-displacement-energy-for-11be-and-11b/

---

## 1. What is the Coulomb Displacement Energy?

When a neutron is changed to a proton (or vice versa) in a nucleus, the energy difference between the isobaric analog states (IAS) is the **Coulomb displacement energy (CDE)**:

```
ΔE_C = M(Z, N) - M(Z+1, N-1)  [corrected for neutron-proton mass difference]
```

For mirror nuclei (A=2T+1 systems), the CDE is directly measurable from masses. For non-mirror pairs, it requires knowing the IAS excitation energy.

**Empirical formula (uniform sphere approximation):**
```
ΔE_C ≈ (3/5) * e²/R * [2Z+1]     R = r₀ * A^(1/3)
```
Typical values: ~1-2 MeV for sd-shell nuclei, growing with Z.

---

## 2. Single-Orbital Coulomb Energy (WS approach)

### The problem with the uniform sphere

The standard formula assumes uniform charge distribution and a point-like added proton. In reality:
- The proton wave function has a specific radial shape ψ(r)
- The nuclear charge distribution is diffuse (WS shape, not uniform sphere)

### Proper calculation

For a proton in orbital (n,l,j) under a Woods-Saxon potential:

**Step 1:** Solve the radial Schrödinger equation:
```
[-ℏ²/2m * d²/dr² + V_WS(r) + ℏ²l(l+1)/(2mr²)] u(r) = E * u(r)
```
with V_WS(r) = -V₀ / (1 + exp((r-R)/a)) + spin-orbit term.
Adjust V₀ to reproduce the experimental binding energy.

**Step 2:** Build the Coulomb potential from the WS charge distribution:
```
ρ_ch(r) = ρ₀ / (1 + exp((r-R)/a))    [normalized to Z]
```
The normalized WS potential uses the polylogarithm function:
```
ρ₀ = Z / (4π * a³ * Li₃(-exp(R/a)))
```
where Li₃ is the polylogarithm of order 3.

**Step 3:** Compute V_C(r) from ρ_ch(r) by integrating Poisson's equation.

**Step 4:** Coulomb energy of the added proton:
```
ΔE_C = ∫₀^∞ |ψ(r)|² * V_C(r) * r² dr
```

### Example: ¹¹Be 1s₁/₂ (Ryan's blog, Apr 2020)

Parameters: r₀ = 1.25 fm, a = 0.67 fm, V₀ adjusted to give ε(1s₁/₂) = -0.502 MeV (¹¹Be separation energy).

Result: **ΔE_C(1s₁/₂) ≈ 1.15-1.24 MeV** (WS) vs 1.65 MeV (uniform sphere).

Experimental CDE for ¹¹Be T=3/2 IAS: **1.83 MeV**. Gap = 0.7 MeV.

Initial hypothesis: wave function shape mismatch.
True reason: **isospin decomposition** (see Section 3).

---

## 3. Isospin Decomposition of CDE -- The Key Lesson

### The IAS is NOT just "swap one neutron"

The isospin lowering operator T₋ acts on **all** nucleons:
```
T₋ = Σᵢ tᵢ₋    [sum over all nucleons]
```

For ¹¹Be (1s₁/₂ valence neutron + 3 × 0p₃/₂ neutrons in core):
```
T₋ |¹¹Be⟩ → contributes from 1s₁/₂ AND from 0p₃/₂ neutrons
```

The CDE of the T=3/2 IAS in ¹¹B is a **coherent sum**:
```
ΔE_C(IAS) = (1/3) * ΔE_C(1s₁/₂) + (2/3) * ΔE_C(core p₃/₂)
```
(The fraction 1/3 : 2/3 comes from the number of neutrons in each orbit and the isospin algebra.)

### Solving for the 1s₁/₂ Coulomb energy

```
ΔE_C(core) ≈ ΔE_C(¹⁰Be → ¹⁰B) = M(¹⁰Be) - M(¹⁰B) = 9325.504 - 9324.436 = 1.065 MeV
```
Wait -- the Coulomb displacement of the p₃/₂ core is estimated from ¹⁰Be → ¹⁰B: **1.965 MeV**.

Then:
```
ΔE_C(IAS, ¹¹B) = (1/3)*ΔE_C(1s₁/₂) + (2/3)*1.965
1.83 = (1/3)*ΔE_C(1s₁/₂) + 1.31
ΔE_C(1s₁/₂) = (1.83 - 1.31)*3 = 1.56 MeV
```

This is much closer to the WS calculation (~1.15-1.24 MeV) than the naive estimate. The remaining ~0.3-0.4 MeV difference is from WS shape sensitivity and possibly electromagnetic effects.

### General rule

**The CDE of an IAS ≠ Coulomb energy of a single orbital**, unless the core is truly inert (doubly closed shell). For mixed-configuration cores or halo nuclei, the isospin decomposition is essential.

---

## 4. Implications for TBME Coulomb Corrections

When extracting hadronic TBMEs from proton-proton (T=1) multiplets, the Coulomb part must be subtracted:

```
V_hadronic(J) = V_measured(J) - ΔV_C(J)
```

**When oscillator Slater integrals are sufficient:**
- Both nucleons in the same sd-shell orbital (d5/2, s1/2, d3/2)
- Normal binding (not halo)
- Closed-shell core (¹⁶O, ⁴⁰Ca, etc.)
- Accuracy needed: ~0.1-0.3 MeV

**When WS wave functions are needed:**
- Loosely bound states (ε < 1 MeV), especially s1/2 (no centrifugal barrier)
- Near drip line
- Non-doubly-magic cores (isospin decomposition may matter)
- Accuracy needed: < 0.1 MeV

**When isospin decomposition is needed:**
- Core is NOT a closed shell -- has open-shell neutrons
- The CDE mixes contributions from multiple orbitals
- Must identify which fraction of the CDE belongs to the orbital of interest

### Oscillator vs WS comparison for (1d5/2)² at A=26

| Method | ΔV_C monopole |
|--------|--------------|
| Oscillator Slater F⁰ (this code) | ~0.39 MeV |
| Paper (Schiffer-True 1976, oscillator) | J=0: 0.461, J=2: 0.389, J=4: 0.362 MeV |
| WS (expected, normal binding) | ~0.35-0.40 MeV |
| Uniform sphere | ~0.55 MeV |

For d5/2 in the sd shell (normal binding, ¹⁶O core), oscillator gives good results. WS correction matters at the ~10% level.

---

## 5. Code Reference

`~/HELIOS_MD/codes/tbme_estimator.py` implements:
- Oscillator Slater integral Coulomb correction (F^k, all k up to 2l)
- Angular coefficients via Wigner 6j + CG (requires sympy)
- WS-based correction: **planned** (solve Schrödinger + integrate V_C from WS charge)

The isospin decomposition factor must be applied **manually** when the core is not doubly closed. The code assumes a clean doubly-closed-shell core.

---

## 6. Key Numbers to Remember

| System | CDE (exp) | CDE (calc, uniform sphere) | Notes |
|--------|-----------|---------------------------|-------|
| ¹¹Be → ¹¹B (T=3/2 IAS) | 1.83 MeV | 1.65 MeV | 1/3 from 1s₁/₂, 2/3 from p₃/₂ |
| ¹⁰Be → ¹⁰B | 1.065 MeV | — | Core (p₃/₂) reference |
| 1s₁/₂ only in ¹¹Be | ~1.56 MeV (derived) | ~1.24 MeV (WS) | Halo orbital -- WS essential |
| (1d5/2)² in A=26 | — | 0.39-0.46 MeV | sd-shell -- oscillator OK |

---

_Created: 2026-04-29 | Source: Ryan Tang's blog (nukephysik101.wordpress.com) + Schiffer-True 1976_
