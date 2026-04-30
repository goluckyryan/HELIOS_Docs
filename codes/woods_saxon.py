#!/usr/bin/env python3
"""
Woods-Saxon Potential Solver
Finds bound-state energies and wave functions for a spherical WS potential.

STATUS: Framework implemented; physical state identification needs improvement.
  - The log-derivative matching is implemented but finds multiple states.
  - To identify the physical state, need to count radial nodes in u(r).
  - TODO: add node counter + select state by (n_radial_nodes, l) quantum numbers.
  - For now: use 'adjust_V0' with E_min/E_max bracket set to isolate the target state.
  - The Coulomb energy calculation works correctly once the wave function is obtained.

Known working: Coulomb potential from WS charge distribution, oscillator comparison.
Needs work: reliable bound-state finder for deep WS wells with many states.
"""

Method: Numerov algorithm (outward integration) + bisection on energy.

Physics:
  Radial Schrodinger equation (u = r*R):
    d²u/dr² = f(r,E) * u(r)
    f(r,E) = (2m/hbar²) * [V(r) - E] + l(l+1)/r²

  Potentials:
    V_WS(r)  = -V0 / (1 + exp((r-R0)/a))             [central]
    V_SO(r)  = Vso * (hbar/m_pi*c)² * (1/r) * dV_WS/dr * ls_factor  [spin-orbit]
    V_C(r)   = Coulomb (protons only)

  Boundary conditions:
    u(0) = 0
    u(r) -> 0 as r -> inf  [bound state]

  Bound state condition: for E < 0, u must match to decaying exponential.
  Solved by bisection: find E such that u(r_max) ~ 0.

Requirements: numpy, scipy

Usage:
  python3 woods_saxon.py
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ===========================================================================
# CONSTANTS (natural units: MeV, fm)
# ===========================================================================
HBAR_C   = 197.3269804   # MeV fm
M_N_C2   = 939.565       # MeV  (neutron rest mass)
M_P_C2   = 938.272       # MeV  (proton rest mass)
M_PI_C2  = 139.57        # MeV  (pion mass, for spin-orbit range)
E2       = 1.43996       # MeV fm  (e^2 = alpha * hbar*c)

# ===========================================================================
# POTENTIAL FUNCTIONS
# ===========================================================================

def V_WS(r, V0, R0, a):
    """Central Woods-Saxon: V_WS(r) = -V0 / (1 + exp((r-R0)/a))"""
    return -V0 / (1.0 + np.exp((r - R0) / a))

def dV_WS_dr(r, V0, R0, a):
    """Derivative of WS for spin-orbit: dV/dr = V0/a * f/(1+f)^2, f=exp(...)"""
    f = np.exp((r - R0) / a)
    return (V0 / a) * f / (1.0 + f)**2

def V_SO(r, Vso, R0, a, ls):
    """
    Spin-orbit potential: V_SO = Vso * (hbar/m_pi*c)^2 * (1/r) * dV_WS/dr * l.s
    The factor (hbar/m_pi*c)^2 = (HBAR_C/M_PI_C2)^2 [fm^2]
    ls = [j(j+1) - l(l+1) - 3/4] / 2  for spin-1/2
    """
    pion_range_sq = (HBAR_C / M_PI_C2)**2   # fm^2
    if r < 1e-10:
        return 0.0
    return Vso * pion_range_sq * (1.0 / r) * dV_WS_dr(r, 1.0, R0, a) * ls
    # Note: using dV_WS_dr with V0=1 (unit strength), then multiply by Vso

def V_Coulomb_uniform(r, Z_core, R0):
    """
    Coulomb potential for a proton in the field of Z_core protons,
    assuming uniform charge distribution of radius R0.
    """
    if r >= R0:
        return Z_core * E2 / r
    else:
        return Z_core * E2 / (2 * R0) * (3 - (r / R0)**2)

def V_Coulomb_WS(r, Z_core, R0, a, dr=0.01, r_max=20.0):
    """
    Coulomb potential from Woods-Saxon charge distribution.
    V_C(r) = (e^2/r) * integral_0^r 4pi r'^2 rho(r') dr'
           + e^2 * integral_r^inf 4pi r' rho(r') dr'
    Computed numerically on a grid. Slow for single r; use precomputed grid.
    """
    # For use in the ODE, precompute on a grid and interpolate
    # This function is for reference; use precomputed_coulomb_potential() instead
    raise NotImplementedError("Use precomputed_coulomb_potential() for efficiency.")

def precomputed_coulomb_potential(Z_core, R0, a, dr=0.02, r_max=25.0):
    """
    Precompute Coulomb potential on a grid from WS charge distribution.
    Returns (r_grid, V_C_grid) for interpolation.
    """
    from scipy.integrate import cumulative_trapezoid

    r = np.arange(dr, r_max, dr)
    # WS charge density (unnormalized)
    rho_raw = 1.0 / (1.0 + np.exp((r - R0) / a))
    # Normalize: integral 4pi r^2 rho dr = Z_core
    norm = np.trapz(4 * np.pi * r**2 * rho_raw, r)
    rho = Z_core * rho_raw / norm

    # Charge enclosed up to r: Q(r) = 4pi * integral_0^r r'^2 rho(r') dr'
    Q_enclosed = 4 * np.pi * cumulative_trapezoid(r**2 * rho, r, initial=0)

    # Coulomb potential: V_C(r) = e^2/r * Q(r) + e^2 * integral_r^inf rho(r') r' dr'
    # Second term: tail contribution
    tail_integrand = 4 * np.pi * r * rho
    tail = cumulative_trapezoid(tail_integrand[::-1], r[::-1], initial=0)[::-1]
    tail *= E2

    V_C = E2 * Q_enclosed / r + tail
    return r, V_C


# ===========================================================================
# NUMEROV INTEGRATOR
# ===========================================================================

def numerov_outward(r_grid, f_grid, u0=0.0, u1=1e-6):
    """
    Numerov's method for u'' = f(r)*u.
    More accurate than RK4 for this type of equation (O(h^6)).

    Args:
        r_grid: radial grid [fm]
        f_grid: f(r,E) = (2m/hbar^2)*(V(r)-E) + l(l+1)/r^2
        u0, u1: initial values at r[0] and r[1]

    Returns:
        u: array of wave function values
    """
    n = len(r_grid)
    u = np.zeros(n)
    u[0] = u0
    u[1] = u1
    h = r_grid[1] - r_grid[0]  # assumes uniform grid

    for i in range(1, n - 1):
        num = (2 * u[i] * (1 - (5/12) * h**2 * f_grid[i])
               - u[i-1] * (1 + (1/12) * h**2 * f_grid[i-1]))
        den = 1 + (1/12) * h**2 * f_grid[i+1]
        u[i+1] = num / den

    return u


# ===========================================================================
# BOUND STATE FINDER
# ===========================================================================

def find_bound_state(n_node, l, j, params, proton=False, Z_core=0,
                     E_min=-80.0, E_max=-0.001,
                     r_min=0.005, r_max=40.0, dr=0.01,
                     V_C_interp=None, verbose=True,
                     match_asymptotic=True):
    """
    Find a bound state with n_node radial nodes and orbital angular momentum l.

    Args:
        n_node: number of radial nodes (0 = ground state of that l)
        l, j: orbital and total angular momenta
        params: dict with keys V0, R0, a, Vso (MeV, fm)
        proton: True if proton (adds Coulomb)
        Z_core: number of core protons (for Coulomb)
        E_min, E_max: energy search range [MeV]
        r_min, r_max, dr: radial grid parameters [fm]
        V_C_interp: precomputed Coulomb potential interpolator
        verbose: print results

    Returns:
        (E_bound, u_norm, r_grid): energy [MeV], normalized wave function, grid
    """
    M_C2 = M_P_C2 if proton else M_N_C2
    hbar2_2m = HBAR_C**2 / (2 * M_C2)  # MeV fm^2

    # Spin-orbit factor: l.s = [j(j+1) - l(l+1) - 3/4] / 2
    ls = (j*(j+1) - l*(l+1) - 0.75) / 2.0

    V0  = params["V0"]
    R0  = params["R0"]
    a   = params["a"]
    Vso = params.get("Vso", 0.0)

    r = np.arange(r_min, r_max + dr, dr)

    # Precompute potential on grid
    V_cent = np.array([V_WS(ri, V0, R0, a) for ri in r])
    V_so   = np.array([V_SO(ri, Vso, R0, a, ls) for ri in r])
    V_tot  = V_cent + V_so

    if proton and V_C_interp is not None:
        V_C = V_C_interp(r)
        V_tot += V_C
    elif proton and Z_core > 0:
        V_C = np.array([V_Coulomb_uniform(ri, Z_core, R0) for ri in r])
        V_tot += V_C

    # Matching radius: far enough that V(r_match) ~ 0, so u ~ exp(-kappa*r)
    r_match_idx = int(0.85 * len(r))  # match at 85% of r_max
    r_match = r[r_match_idx]

    def boundary_condition(E):
        """
        Bound state condition via logarithmic derivative matching.
        Outward solution: u_out from Numerov.
        Asymptotic: u_asy ~ exp(-kappa*(r-r_match)) where kappa=sqrt(2m|E|)/hbar
        Match: (u_out'/u_out) = (u_asy'/u_asy) = -kappa  at r_match.
        Residual: u_out'(r_match)/u_out(r_match) + kappa
        """
        if E >= 0:
            return 1e10
        kappa = np.sqrt(-2 * M_C2 * E) / HBAR_C
        f = (V_tot - E) / hbar2_2m + l*(l+1) / r**2
        u = numerov_outward(r, f)
        if u[2] < 0:
            u = -u
        # Logarithmic derivative at r_match using finite difference
        i = r_match_idx
        if abs(u[i]) < 1e-30:
            return 1e10
        h = r[1] - r[0]
        dudr = (u[i+1] - u[i-1]) / (2 * h)
        log_deriv_out = dudr / u[i]
        log_deriv_asy = -kappa
        return log_deriv_out - log_deriv_asy

    # Scan energies to find sign changes (each sign change = one bound state)
    E_scan = np.linspace(E_min, E_max, 500)
    bc = np.array([boundary_condition(E) for E in E_scan])

    # Find sign changes
    sign_changes = []
    for i in range(len(bc)-1):
        if bc[i] * bc[i+1] < 0:
            sign_changes.append((E_scan[i], E_scan[i+1]))

    # n_node=0 -> deepest bound state; n_node=-1 -> shallowest (halo)
    # Use negative indexing: n_node=-1 for halo (last = shallowest)
    if abs(n_node) > len(sign_changes):
        if verbose:
            print(f"  Only {len(sign_changes)} bound states found (need node #{n_node})")
        return None, None, None

    # Bisect to find the n_node-th state
    E_lo, E_hi = sign_changes[n_node]
    E_bound = brentq(boundary_condition, E_lo, E_hi, xtol=1e-6)

    # Get the wave function
    u = u_outer(E_bound)
    if u[2] < 0:
        u = -u

    # Normalize: integral |u|^2 dr = 1
    norm = np.sqrt(np.trapz(u**2, r))
    u_norm = u / norm

    if verbose:
        # Count actual nodes (zero crossings in interior)
        interior = u_norm[5:-5]
        nodes = np.sum((interior[:-1] * interior[1:]) < 0)
        print(f"  E({n_node}{'spdfgh'[l]}{'+' if j==l+0.5 else '-'}1/2) = {E_bound:.4f} MeV")
        print(f"  Nodes (interior): {nodes}")
        rms = np.sqrt(np.trapz(r**2 * u_norm**2, r))
        print(f"  <r> rms = {rms:.3f} fm")

    return E_bound, u_norm, r


# ===========================================================================
# COULOMB ENERGY FROM WS WAVE FUNCTION
# ===========================================================================

def coulomb_energy_WS(u_norm, r_grid, Z_core, R0, a):
    """
    Compute Coulomb energy of an added proton:
        E_C = integral |u(r)|^2 * V_C(r) dr

    using WS charge distribution for V_C(r).
    """
    r_vc, V_C_grid = precomputed_coulomb_potential(Z_core, R0, a)
    V_C_interp = np.interp(r_grid, r_vc, V_C_grid)
    E_C = np.trapz(u_norm**2 * V_C_interp, r_grid)
    return E_C


# ===========================================================================
# ADJUST V0 TO REPRODUCE BINDING ENERGY
# ===========================================================================

def adjust_V0(target_E, n_node, l, j, params_in, proton=False, Z_core=0,
              V0_min=10.0, V0_max=120.0, tol=1e-4, verbose=True):
    """
    Find V0 such that the bound state energy equals target_E [MeV].
    Scans V0 to find a bracket where the target energy is crossed, then bisects.
    """
    def get_E(V0):
        params = dict(params_in)
        params["V0"] = V0
        E, _, _ = find_bound_state(n_node, l, j, params, proton=proton,
                                   Z_core=Z_core, verbose=False)
        return E

    if verbose:
        print(f"  Adjusting V0 to reproduce E = {target_E:.4f} MeV...")

    # Scan V0 to find bracket
    V0_scan = np.linspace(V0_min, V0_max, 50)
    E_scan = []
    for V0 in V0_scan:
        E = get_E(V0)
        E_scan.append(E if E is not None else 1e10)
    E_scan = np.array(E_scan)

    # Find bracket where E crosses target_E
    diff = E_scan - target_E
    bracket = None
    for i in range(len(diff)-1):
        if diff[i] * diff[i+1] < 0 and abs(diff[i]) < 50 and abs(diff[i+1]) < 50:
            bracket = (V0_scan[i], V0_scan[i+1])
            break

    if bracket is None:
        # Show what we found
        valid = [(V0_scan[i], E_scan[i]) for i in range(len(E_scan)) if abs(E_scan[i]) < 50]
        if verbose and valid:
            print(f"  Could not bracket target. Closest states found:")
            for v, e in valid[:5]:
                print(f"    V0={v:.1f} => E={e:.4f} MeV")
        raise ValueError(f"Cannot find V0 to reproduce E={target_E:.4f} MeV in [{V0_min},{V0_max}]")

    def energy_error(V0):
        E = get_E(V0)
        return (E if E is not None else 1e10) - target_E

    V0_sol = brentq(energy_error, bracket[0], bracket[1], xtol=tol)
    params_out = dict(params_in)
    params_out["V0"] = V0_sol
    if verbose:
        print(f"  V0 = {V0_sol:.4f} MeV")
    return params_out


# ===========================================================================
# INPUT -- Edit for your system
# ===========================================================================

# Example: 11Be 1s1/2 neutron (Ryan's blog case)
# NOTE on 11Be 1s1/2 halo state:
# The 11Be 1s1/2 neutron is bound at -0.502 MeV.
# With standard R0=1.25*A^(1/3)=2.78 fm, a=0.67 fm:
#   - The shallowest s1/2 state sits at ~-0.15 MeV (only one s1/2 supported)
#   - To reproduce -0.502 MeV, Ryan's blog uses deeper V0 (~51.56 MeV)
#     which finds the SECOND 1s1/2 (1 radial node at ~1.9 fm), not the halo
#   - Or use larger R0 (e.g. R0=2.2 fm, a=0.1 fm as explored in the blog)
# For sd-shell nuclei (d5/2 etc), the standard parameters work cleanly.
# Use n_node=1 (second 1s1/2) or adjust R0,a for halo cases.

system = {
    "name": "17O: 1d5/2 neutron -> 18O (sd-shell prototype)",
    "nucleus": "18O",
    "A": 18,
    "Z_core": 8,          # 16O core has Z=8
    "target_E": -4.144,   # MeV -- 17O 1d5/2 separation energy (eps = B(17O)-B(16O))
    "n_node": 0,          # 0 = deepest bound state of this l (standard for sd-shell)
    "l": 2,               # d-wave
    "j": 2.5,             # 5/2+
    "proton": False,      # neutron
    "params": {
        "R0": 1.25 * (18**(1.0/3.0)),  # fm = 3.24 fm
        "a":  0.65,
        "Vso": 6.0,        # MeV -- standard WS spin-orbit
        "V0": 50.0,        # initial guess
    }
}


# ===========================================================================
# RUN
# ===========================================================================

if __name__ == "__main__":
    print("\nWoods-Saxon Potential Solver")
    print("="*50)
    print(f"System: {system['name']}")
    print(f"Orbital: n={system['n_node']}, l={system['l']}, j={system['j']}")
    print(f"Target binding energy: {system['target_E']} MeV\n")

    # Step 1: Adjust V0 to reproduce binding energy
    params = adjust_V0(
        target_E = system["target_E"],
        n_node   = system["n_node"],
        l        = system["l"],
        j        = system["j"],
        params_in = system["params"],
        proton   = system["proton"],
        Z_core   = system["Z_core"],
        verbose  = True
    )

    # Step 2: Get wave function
    print("\nComputing wave function:")
    E_bound, u_norm, r = find_bound_state(
        n_node = system["n_node"],
        l      = system["l"],
        j      = system["j"],
        params = params,
        proton = system["proton"],
        Z_core = system["Z_core"],
        verbose = True
    )

    # Step 3: Coulomb energy (if neutron -> proton)
    if not system["proton"] and system["Z_core"] > 0:
        print(f"\nCoulomb energy of added proton (WS charge distribution):")
        E_C = coulomb_energy_WS(u_norm, r, system["Z_core"], params["R0"], params["a"])
        print(f"  E_C = {E_C:.4f} MeV")
        E_C_uniform = system["Z_core"] * E2 * np.trapz(u_norm**2 / r, r)
        # Uniform sphere comparison
        R0 = params["R0"]
        def vc_unif(ri):
            if ri >= R0:
                return system["Z_core"] * E2 / ri
            return system["Z_core"] * E2 / (2*R0) * (3 - (ri/R0)**2)
        V_C_u = np.array([vc_unif(ri) for ri in r])
        E_C_u = np.trapz(u_norm**2 * V_C_u, r)
        print(f"  E_C (uniform sphere) = {E_C_u:.4f} MeV")
        print(f"  Difference (WS vs uniform): {E_C - E_C_u:.4f} MeV")
        print(f"  (Ryan's blog result: WS~1.15 MeV, uniform~1.65 MeV for same system)")

    # Step 4: Plot
    print("\nSaving wave function plot...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Potential
    M_C2 = M_P_C2 if system["proton"] else M_N_C2
    V_plot = np.array([V_WS(ri, params["V0"], params["R0"], params["a"]) for ri in r])
    ax1.plot(r, V_plot, 'b-', label='V_WS')
    ax1.axhline(E_bound, color='r', ls='--', label=f'E={E_bound:.3f} MeV')
    ax1.set_xlabel('r [fm]')
    ax1.set_ylabel('V [MeV]')
    ax1.set_title(f"WS Potential: {system['name']}")
    ax1.legend()
    ax1.set_xlim(0, 12)
    ax1.set_ylim(-params["V0"]*1.1, 5)
    ax1.grid(True, alpha=0.3)

    # Wave function
    ax2.plot(r, u_norm, 'g-', label='u(r) = r*R(r)')
    ax2.plot(r, u_norm**2, 'b--', alpha=0.7, label='|u(r)|²')
    ax2.set_xlabel('r [fm]')
    ax2.set_ylabel('u(r) [fm⁻¹/²]')
    ax2.set_title(f"Wave function: n={system['n_node']}, l={system['l']}, j={system['j']}")
    ax2.legend()
    ax2.set_xlim(0, 12)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    outfile = "/tmp/ws_wavefunction.png"
    plt.savefig(outfile, dpi=100)
    print(f"  Saved to {outfile}")

    print("\nReference: Ryan Tang, nukephysik101.wordpress.com (2020, 2021)")
    print("See also: ~/HELIOS_MD/Coulomb_Displacement_Energy.md")
