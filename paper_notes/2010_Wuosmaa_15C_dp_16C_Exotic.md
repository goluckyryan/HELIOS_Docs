# Paper Notes: Wuosmaa et al. 2010 -- 15C(d,p)16C Exotic Behavior

**Citation:** A.H. Wuosmaa, B.B. Back, S. Baker, B.A. Brown, C.M. Deibel, P. Fallon et al., PRL 105, 132501 (2010)
**DOI:** 10.1103/PhysRevLett.105.132501
**PDF:** `~/publications/2010_Wuosmaa_15Cdp16C.pdf`
**Read:** 2026-04-26 (notes); PDF obtained 2026-04-28

## Context & Motivation

- Prior EM measurements (Imai 2004, Elekes 2004) found anomalously small B(E2) for 2+1→0+1 in ¹⁶C
- Interpreted as exotic decoupling of sd-shell valence neutrons from ¹⁴C core
- Many theory papers followed (shell model, three-body, cluster) -- most reproduced small B(E2)
- A later lifetime measurement (Wiedeking 2008) gave a much LARGER B(E2), consistent with systematics
- This paper uses (d,p) transfer to get an independent, complementary probe of the wave functions

## Experiment

- **Beam:** ¹⁵C (T½ = 2.45 s), 123 MeV (16.4 MeV/u), 1-2×10⁶/s from In-Flight at ATLAS
- **Production:** ¹⁴C + cryogenic D₂ gas cell → ¹⁴C(d,p)¹⁵C
- **Target:** 110 μg/cm² CD₂
- **B-field:** 2.85 T
- **Resolution:** ~140 keV FWHM (detector + beam energy spread + kinematics)
- **Recoil detection:** ΔE-E Si telescopes, 0.5°–2.8° lab
- **Efficiency:** ~80% coincidence efficiency (Monte Carlo corrected)

## Results -- States in ¹⁶C

| State | Ex (MeV) | ℓ | S_exp | S_WBP |
|-------|----------|---|-------|-------|
| 0+1 | 0.000 | 0 | 0.60(13) | 0.60 |
| 2+1 | 1.766 | 2 | 0.52(12) | 0.58 |
| 0+2 | 3.027 | 0 | 1.40(31) | 1.34 |
| 2+2/3+1 | ~4.08 | 2 | unresolved | — |

- Normalization: sum of 0+ SFs = 2.0 (relative normalization due to 30% systematic on absolute flux)
- DWBA with 4 OM parameter sets (Fortune, Perey, Schiffer, Corrigan); WBP interaction used
- Strong mixing between (1s1/2)² and (0d5/2)² in both 0+ states -- (1s1/2)² dominant in 0+2, not 0+1
- Conflicts with Elekes 2004 conclusion that g.s. is dominantly (1s1/2)²

## Residual Interaction Matrix Elements (sd)² → 0+

| Element | Exp (MeV) | LSF | WBP |
|---------|-----------|-----|-----|
| ⟨s1/2 s1/2 \| v \| s1/2 s1/2⟩ | -0.92(28) | -1.54 | -2.12 |
| ⟨d5/2 d5/2 \| v \| d5/2 d5/2⟩ | -3.60(28) | -2.78 | -2.82 |
| ⟨s1/2 s1/2 \| v \| d5/2 d5/2⟩ | -1.39(12) | -1.72 | -1.32 |

## Conclusion

- Same WBP shell-model calculations reproduce BOTH transfer SFs (this work) AND Wiedeking 2008 EM rates
- **¹⁶C is NOT anomalous** -- no exotic phenomena needed
- The earlier B(E2) measurements were likely systematically low
- HELIOS provides a clean, qualitatively different probe that resolves the controversy

## Significance

- **Paper #1 in the HELIOS publication list** -- first published HELIOS science result (PRL 2010)
- Demonstrates HELIOS capability for short-lived exotic beams (T½ = 2.45 s)
- Wuosmaa is HELIOS co-developer (also Lighthall 2010 commissioning paper)
- Physics lesson: EM transitions alone can be misleading; transfer reactions give independent wavefunction info

_Created: 2026-04-26 | Updated with full details: 2026-04-28_
