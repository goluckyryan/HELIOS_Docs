# AutoFit.C — Code Notes

Source: `~/digios/analysis/Armory/AutoFit.C` (3114 lines, by Ryan Tang ~2019, updated 2022)

## Purpose

ROOT macro library for automated peak fitting in excitation energy spectra. Provides multiple fitting strategies from fully automatic to interactive mouse-click fitting.

## Architecture

### Global State
- `BestFitMean`, `BestFitCount`, `BestFitSigma` — vectors storing last fit results
- `nPeaks`, `nPols` — global counters for current fit
- `recentFitMethod` — tracks which fit was last used

### Fit Functions (TF1-compatible)
- `nGauss(x, par)` — sum of N normalized Gaussians (3 params each: norm, mean, sigma)
- `nPolFunc(x, par)` — polynomial of degree nPols
- `nGaussPol(x, par)` — N Gaussians + polynomial background
- `nGF3(x, par)` — GF3-style peak shape (Gaussian + exponential tails, from RadWare)
- `nGF3Pol(x, par)` — GF3 + polynomial

### Fitting Methods

| Function | Strategy | Use Case |
|----------|----------|----------|
| `fitAuto()` | TSpectrum peak search → estimate BG → fit N-Gauss | Quick automatic fit |
| `fitGaussPol()` | 1 Gaussian + pol-n BG | Single isolated peak |
| `fit2GaussP1()` | 2 Gaussians + pol-1 | Doublet |
| `fitGF3Pol()` | GF3 shape + pol-n | Gamma-ray peaks (asymmetric) |
| `fitNGauss()` | N-Gauss with estimated BG, reads input file | Manual peak list |
| `fitNGaussSub()` | Fit BG with pol, subtract, then fit N-Gauss | Clean BG subtraction |
| `fitNGaussPol()` | N-Gauss + pol-n simultaneous | Standard multi-peak + BG |
| `fitNGaussPolSub()` | Subtract pol-n BG, then fit N-Gauss | Two-step approach |
| `fitSpecial()` | Hardcoded for h074_82Kr experiment | Legacy/special case |

### Interactive (Mouse-Click) Methods
- `clickFitNGaussPol()` — click peaks + BG points, then fit N-Gauss + pol
- `clickFitNGaussPolSub()` — click peaks + BG, subtract BG, fit N-Gauss
- `clickFitPol()` — click points on 2D histogram, fit polynomial
- `clickFitCut()` — click points on 2D histogram to create TCutG

Uses `Clicked()` and `Clicked2D()` signal handlers connected to canvas mouse events.

### Utilities
- `PrintPar()` — print fit parameters
- `GoodnessofFit()` — chi-square, reduced chi-square, residuals
- `SaveFitPara()` — save parameters to `AutoFit_para.txt`
- `loadFitParameters()` — read peak list from file
- `PlotResidual()` — draw residual panel
- `ScaleAndDrawHist()` — zoom and draw
- `NewCanvas()` — create canvas with custom divisions
- `RGBWheel()` — color generation for multi-peak display

## Input File Format (`AutoFit_para.txt`)

```
// comment lines start with //
energy  sigma  [energy_flag  sigma_flag]
// flags: 0=free, 1=fixed
1.234   0.050   0   0
2.567   0.060   1   0
```

## Key Design Patterns

1. **TSpectrum for peak finding** — `fitAuto()` uses ROOT's TSpectrum to automatically locate peaks, then constrains each peak to lie between midpoints of neighbors
2. **Background estimation** — uses TSpectrum::Background() with configurable smoothing parameter
3. **Two-step fitting** — several methods fit BG first, subtract, then fit peaks (avoids BG-peak correlation)
4. **Canvas layout** — typically 4 panels: original histogram, fitted spectrum, background, residuals
5. **Parameter bounds** — peak means constrained to ±range around initial guess, sigmas bounded by sigmaMax

## Observations

- `fitSpecial()` is hardcoded for h074_82Kr — dead code for other experiments
- GF3 fitting (`nGF3`, `fitGF3Pol`) implements the RadWare gamma-ray peak shape — useful for gamma spectroscopy but not typically used for charged-particle spectra
- The interactive click methods are powerful but complex (~300 lines each)
- No unit tests — validation is visual (plot inspection)
- 11 other files reference AutoFit.C — it's the most-used Armory file
