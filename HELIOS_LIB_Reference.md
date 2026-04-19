# HELIOS_LIB.h Reference

Core kinematics library for HELIOS simulations.
Location: `~/digios/analysis/Cleopatra/HELIOS_LIB.h`

Four classes + one struct:

---

## 1. `TransferReaction` -- Transfer Reaction Kinematics

Models A(a,b)B in inverse kinematics (heavy beam A on light target a).

### Setup
```cpp
TransferReaction react;
react.SetA(beamA, beamZ, ExA);    // beam nucleus + excitation
react.Seta(targetA, targetZ);      // target
react.Setb(lightA, lightZ);        // light recoil
react.SetB(heavyA, heavyZ);        // heavy recoil (or auto from conservation)
react.SetIncidentEnergyAngle(KEA_per_u, theta, phi);
react.CalReactionConstant();        // compute CM boost, p, Etot
// OR load from file:
react.SetReactionFromFile("reactionConfig.txt");
```

### Key quantities (after CalReactionConstant)
| Method | Returns |
|---|---|
| `GetQValue()` | Q = mA + ExA + ma - mb - mB - ExB [MeV] |
| `GetCMTotalEnergy()` | Etot (CM invariant mass) [MeV] |
| `GetReactionBeta/Gamma()` | CM boost β, γ |
| `GetMomentumbCM()` | p -- CM momentum of b (and B) [MeV/c] |
| `GetMaxExB()` | Maximum accessible Ex_B [MeV] |

### Monte Carlo event
```cpp
TLorentzVector * out = react.Event(thetaCM, phiCM);
// out[0]=PA, out[1]=Pa, out[2]=Pb (lab), out[3]=PB (lab)
```

### Inverse reconstruction (e, z -> Ex, thetaCM)
```cpp
int ok = react.CalExThetaCM(e_MeV, z_mm, Bfield_T, perpDist_mm);
// ok=1: success; ok=0: no solution (|Z|>=H or Newton diverged)
double Ex      = react.GetEx();
double thetaCM = react.GetThetaCM(); // degrees
```

**Algorithm:** Newton's method on the transcendental equation `H*sin(phi) - G*tan(phi) - Z = 0`
where:
- `alpha = 299.792458 * Zb * |B| / (2π) [MeV/mm]` -- cyclotron momentum scale
- `slope = alpha * beta / 1000` [MeV/mm]
- `G = alpha * γβ * perpDist` [MeV]
- `Z = alpha * γβ * z` [MeV]
- `H = γβ * sqrt(y²-m²)` [MeV], y = e + m

Tolerance: 0.001 rad; max 10 iterations; fails if |phi| > π/2 or f'(phi) <= 0.

---

## 2. `HELIOS` -- Detector Geometry + Trajectory Simulation

Simulates particle trajectories in the solenoidal B-field and checks detector acceptance.

### Setup
```cpp
HELIOS det;
det.SetDetectorGeometry("detectorGeo.txt"); // loads DetGeo via LoadDetectorGeo()
det.SetBeamPosition(xOff_mm, yOff_mm);      // beam offset
```

### Trajectory calculation
```cpp
det.CalArrayHit(Pb_4vec, Zb);    // light recoil -> silicon array
det.CalRecoilHit(PB_4vec, ZB);   // heavy recoil -> annular recoil detector
int status = det.DetAcceptance(); // check acceptance (see return codes)
```

### Orbit formulas (helical in B-field)
```
rho [mm] = Pt / (|B| * Z * c) * 1000      c = 299.792458 mm/ns
x(z) = rho * (sin(z*tan(theta)/rho - sign*phi) + sign*sin(phi)) + xOff
y(z) = rho * sign * (cos(z*tan(theta)/rho - sign*phi) - cos(phi)) + yOff
sign = +1 for B along +z; sign = -1 for B along -z (HELIOS physical case)
```

### DetAcceptance() return codes
| Code | Meaning |
|---|---|
| 1 | Hit -- good event |
| 2 | Loop incremented -- retry |
| -2 | y-distance too large (missed detector width) |
| -3 | z beyond full array range |
| -4 | Hit blocker |
| -5 | Hit inter-detector gap |
| -10 | rho too large (hits bore) |
| -11 | rho too small (<= perpDist) |
| -12 | Blocked by recoil detector |
| -13 | More than 3 loops |
| -14 | Heavy recoil misses annular detector |
| -15 | detRowID == -1 |
| -20 | Unknown (should not occur) |

### trajectory struct fields
| Field | Units | Meaning |
|---|---|---|
| `theta`, `phi` | rad | Lab emission angles |
| `vt`, `vp` | mm/ns | Transverse/parallel velocity |
| `rho` | mm | Cyclotron orbit radius |
| `z0`, `t0` | mm, ns | z-advance and period per cyclotron loop |
| `x`, `y`, `z` | mm | Hit position |
| `t` | ns | Time of flight |
| `loop` | int | Number of complete loops |
| `effLoop` | double | Fractional loop count = z/z0 |
| `detID` | int | Which z-position detector (0-indexed) |
| `detRowID` | int | Which azimuthal row (0 to mDet-1) |

---

## 3. `TargetScattering` -- Energy Loss + Angular Straggling

Simulates beam/recoil energy loss and angular straggling through the target using SRIM tables.

### Setup
```cpp
TargetScattering ts;
ts.LoadStoppingPower("beam_stopping.txt");  // SRIM output file
ts.SetTarget(density_g_cm3, thickness_cm);
TLorentzVector Pout = ts.Scattering(Pin);
```

### SRIM file format
Reads SRIM output text: energy (keV/MeV/GeV column), electronic+nuclear stopping [MeV/mm or MeV/(mg/cm²)], projected range [nm or um or mm], parallel straggling, perpendicular straggling.
Auto-detects units from "Stopping Units =" line.

### Energy loss integration
- 100 steps over path length `depth/cos(theta)`
- At each step: `KE -= density * S(KE) * 10 * dx` (factor 10: MeV/mm units)
- Stops if KE < 0 (particle stopped)

### Angular straggling model
At each step: Gaussian kick with sigma = `(perpStraggling/projRange) * sqrt(dx/length)`
Total deflection = sqrt(dThetaX² + dThetaY²), applied in a random azimuthal direction.

### Supported stopping unit modes
- `MeV/mm` or `keV/micron` → unitID=0 (density factor=1)
- `MeV/(mg/cm²)` → unitID=1 (multiply by density)

---

## 4. `Decay` -- Two-Body Decay (B -> d + D)

Models isotropic (or anisotropic) two-body decay of heavy recoil.

```cpp
Decay dec;
dec.SetMotherDaugther(AB, zB, AD, zD);
int ok = dec.CalDecay(P_mother, ExB, ExD, normOfReactionPlane);
// ok=1: success; ok=-1: mother not set; ok=-2: Q<0 (kinematically forbidden)
TLorentzVector Pd = dec.GetDaugther_d();
TLorentzVector PD = dec.GetDaugther_D();
```

Default: isotropic (uniform cos(theta) in mother frame).
Anisotropic: uncomment `f1 = new TF1(...)` and use `theta = ACos(f1->GetRandom())`.

---

## 5. `Knockout` -- Knockout Reaction A(a,12)B

Models quasi-free knockout where bound nucleon b is struck, leaving residual B.
Supports both normal and inverse kinematics.

Typical use: `(p,2p)`, `(p,pn)` reactions. Less commonly used than `TransferReaction` for HELIOS.

---

## Key Physical Constants

```cpp
const double c = 299.792458; // mm/ns (speed of light)
```

All masses via `Isotope` class (atomic masses, includes electron masses).

---

## Notes / Gotchas

- **sign convention**: HELIOS runs with B anti-parallel to beam → `sign = -1`. The archived `CalHit()` method (commented out) had a hardcoded sign=-1 workaround for this.
- **Loop limit**: max 3 loops in `DetAcceptance()` -- events requiring >3 loops are rejected.
- **`CalReactionConstant()` auto-derives B**: if `isBSet=false`, computes `AB = AA+Aa-Ab`, `zB = zA+za-zb` from conservation.
- **Newton's method in CalExThetaCM**: initial phi=0 ensures starting near the physical branch (f'(phi)>0). If |nPhi|>pi/2 or >10 iterations, returns NaN.
- **TargetScattering**: particle stops (KE->0) sets deltaTheta=0 to avoid NaN rotation.

---

---

## `Isotope` class (`Isotope.h` / `Isotope.C`)

Atomic mass lookup from AME2020 table. Used by all kinematics classes to get particle masses.

### Data source
- File: `$HELIOSSYS/analysis/Cleopatra/mass20.txt` (AME2020)
- Fallback: `../Cleopatra/mass20.txt` (relative path)
- Env variable `HELIOSSYS` sets the root path; must be set for production use
- File lines 37-3594 (3557 isotopes); jump table speeds lookup by A range:
  - A < 50: start line 37 | A 50-99: line 466 | A 100-149: line 1160 | A 150-199: line 1994 | A >= 200: line 2774

### Mass formula
```
Mass = Z*mp + (A-Z)*mn - BEA/1000 * A   [MeV/c²]
```
where BEA = binding energy per nucleon [keV/A] from AME2020 table.
**These are atomic masses** (include electron masses) — consistent with AME convention.

### Usage
```cpp
Isotope iso(A, Z);          // by A, Z
Isotope iso("31Si");         // by name
iso.Mass     // MeV/c²
iso.BEA      // keV/A
iso.Name     // e.g. "31Si" (special: 1H->"p", 2H->"d", 3H->"t", 4He->"a")
iso.Symbol   // e.g. "Si"
```

### Separation energy methods
```cpp
iso.CalSp(Np, Nn)    // S(Np protons, Nn neutrons) -- Q for (A,Z)->(A-Np-Nn, Z-Np) + Np*p + Nn*n
iso.CalSp2(a, z)     // S for removing nucleus (a,z) from (A,Z)
iso.Print()          // print mass + common separation energies (S1p, S1n, S2p, S2n, Sd, S3He, Sa...)
iso.ListShell()      // print shell model filling diagram for Z and N
```

### Shell model bookkeeping
- `magic[]` = {2, 8, 20, 28, 40, 50, 82, 128} -- magic numbers
- `TwoJ(nShell)` -- returns 2j for shell index (s1/2=0, p3/2=1, p1/2=2, d5/2=3, ...)
- `Orbital(nShell)` -- returns label string ("s1/2", "p3/2", etc.) up to nShell=28
- `ListShell()` -- prints proton and neutron shell filling: which orbitals are full, partially filled, or empty; marks magic numbers

---

## `constant.h` -- Physical Constants

| Constant | Value | Units |
|---|---|---|
| `amu` | 931.49432 | MeV/c² |
| `c` | 299.792458 | mm/ns |
| `hbarc` | 197.326979 | MeV·fm |
| `ee` | 1.439964454 | MeV·fm (e²) |
| `mp` | kg2MeV(mp_SI) ≈ 938.272 | MeV/c² |
| `mn` | kg2MeV(mn_SI) ≈ 939.565 | MeV/c² |

### Utility functions
- `T2Brho(mass, Z, A, T)` -- kinetic energy [MeV/A] → Bρ [T·m]
- `Brho2T(mass, Z, A, Brho)` -- Bρ → kinetic energy [MeV/A]
- `T2beta(mass, A, T)` -- kinetic energy → β
- `ev2nm(eV)` -- photon energy [eV] → wavelength [nm]

_Isotope + constant.h documented: 2026-04-18._

---

## `FindThetaCM` utility (`FindThetaCM.h`)

Standalone function: calculates θ_CM coverage for each detector position at a given Ex.
Useful for planning angular distribution measurements and normalizing yields.

### Call signature
```cpp
FindThetaCM(double Ex, int nDivision=1, double XRATION=0.95,
            string basicConfig="reactionConfig.txt",
            string detGeoFileName="detectorGeo.txt");
```
- `Ex`: excitation energy of state of interest [MeV]
- `nDivision`: subdivide each detector into N sections (1 = whole detector)
- `XRATION`: fraction of detector active length to use (0.95 = 95% = 5% dead edge on each side)

### Algorithm
1. Load `reactionConfig.txt` and `detectorGeo.txt`
2. Set up `TransferReaction` with beam at mean energy, Ex_B = Ex
3. Build a TGraph of z_hit vs θ_CM using the analytic orbit formula:
   ```
   slope = 299.8 * Zb * |B| / (2π) * β / 1000   [MeV/mm]
   z(θ_CM) = β/slope * (γβ*q - γ*p*cos(θ_CM)) * (1 - arcsin(2π*slope*a / (β*p*sin(θ_CM))) / (2π))
   ```
4. Find z_min (minimum reachable z = kinematic limit at small θ_CM)
5. For each detector strip (sub-divided by nDivision), evaluate:
   - θ_CM_min, θ_CM_max from z range via TGraph interpolation
   - θ_CM_mean = (min+max)/2
   - Δθ_CM = max-min
   - Solid-angle weight = sin(θ_CM_mean) * Δθ_CM (unnormalized)

### Output (stdout)
```
det-0[0]:  min_θ - max_θ |  mean_θ, Δθ, sin(θ)*Δθ
```
Use `sin(θ)*Δθ` column for normalizing angular distributions:
`dσ/dΩ ∝ counts / (sin(θ_mean) * Δθ * N_active_rows * efficiency)`

### Notes
- Runs from `working/` directory (relative paths for config files)
- Requires ROOT (TGraph interpolation)
- θ_CM grid sampled from 5° to ~100° in 1° steps; points below z_min removed
- `XRATION=0.95` is the standard -- matches the 5% dead-zone at strip edges
- For h096 (31Si(d,p)): used with B=2.85 T, 6-det × 4-row array, ELAB=23 MeV

_FindThetaCM documented: 2026-04-18._

_Documented: 2026-04-18 (Spark). Source: ~/digios/analysis/Cleopatra/HELIOS_LIB.h_
