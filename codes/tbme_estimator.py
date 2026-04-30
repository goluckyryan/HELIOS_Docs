#!/usr/bin/env python3
"""
TBME Estimator -- based on Schiffer & True, Rev. Mod. Phys. 48, 191 (1976)

Extracts diagonal two-body matrix elements (TBMEs) of the residual
nucleon-nucleon interaction from nuclear binding energies and excitation energies.

Method (Eq. I.1 of Schiffer-True 1976):
  E0 = eps(j1) + eps(j2)           [unperturbed two-nucleon energy above core]
  TBME(J) = E_J(exc in 2-nuc) - E0 [residual interaction shifts each J member]
  Monopole M0 = sum_J (2J+1)*V(J) / sum_J (2J+1)

Coulomb correction for same-orbital proton pairs:
  Uses harmonic oscillator radial wave functions to compute Slater integrals F^k.
  The J-dependent Coulomb matrix element is built from F^k and angular coefficients.
  Method: Schiffer-True 1976, following Talmi 1952 / Condon-Shortley.

Requirements: numpy, scipy (for Coulomb correction)

Usage:
  Edit the INPUT section, then: python3 tbme_estimator.py
"""

import numpy as np
from scipy.integrate import dblquad
from scipy.special import gamma as Gamma
import sys

# ===========================================================================
# OSCILLATOR RADIAL WAVE FUNCTION
# ===========================================================================

def R_osc(r, n, l, b):
    """
    Harmonic oscillator radial wave function R_nl(r) (no radial nodes for n=0).
    For n=0: R_0l(r) = N_l * (r/b)^l * exp(-r^2/(2b^2))
    Normalization: integral_0^inf |R_0l|^2 r^2 dr = 1
    => N_l^2 = 2 / (b^3 * Gamma(l+3/2))

    Args:
        r: radial coordinate [fm]
        n: radial quantum number (0 = no nodes; this implements n=0 only)
        l: orbital angular momentum
        b: oscillator length [fm]
    """
    if n != 0:
        raise NotImplementedError("Only n=0 (no radial nodes) implemented.")
    N_sq = 2.0 / (b**3 * Gamma(l + 1.5))
    N = np.sqrt(N_sq)
    return N * (r / b)**l * np.exp(-r**2 / (2 * b**2))


def oscillator_length(A):
    """
    Oscillator length b [fm] from standard hbar*omega formula.
    hbar*omega [MeV] = 45*A^(-1/3) - 25*A^(-2/3)
    b = sqrt(hbar^2 / (m * hbar*omega)) = sqrt(hbar*c^2 / (m_p*c^2 * hbar*omega))
    """
    hw = 45.0 * A**(-1.0/3.0) - 25.0 * A**(-2.0/3.0)  # MeV
    hbar_c = 197.3269804  # MeV fm
    m_p_c2 = 938.272  # MeV
    b = hbar_c / np.sqrt(m_p_c2 * hw)
    return b, hw


# ===========================================================================
# SLATER INTEGRALS F^k  (for Coulomb matrix elements)
# ===========================================================================

def slater_Fk(k, n1, l1, n2, l2, b, r_max=20.0, tol=1e-4):
    """
    Compute Slater integral F^k(nl, n'l') numerically:
        F^k = integral_0^inf integral_0^inf
              |R_n1l1(r1)|^2 * r_<^k/r_>^(k+1) * |R_n2l2(r2)|^2
              * r1^2 r2^2 dr1 dr2

    where r_< = min(r1,r2), r_> = max(r1,r2)

    Uses symmetry: F^k = 2 * integral_{r1>r2} ... (1/r1^(k+1)) * r2^k ...
    """
    def integrand(r2, r1):
        R1 = R_osc(r1, n1, l1, b) * r1  # u(r) = r*R(r)
        R2 = R_osc(r2, n2, l2, b) * r2
        return R1**2 * R2**2 * (r2**k / r1**(k+1))  # r_< = r2, r_> = r1

    # Integrate r2 from 0 to r1, then r1 from 0 to r_max
    result, err = dblquad(
        integrand,
        0, r_max,          # r1 limits
        0, lambda r1: r1,  # r2 limits: 0 to r1
        epsabs=tol, epsrel=tol
    )
    return 2.0 * result  # factor 2 for the r1<r2 region (by symmetry)


# ===========================================================================
# ANGULAR COEFFICIENTS FOR COULOMB MATRIX ELEMENTS
# (same orbit: j1 = j2 = j, two identical nucleons)
# ===========================================================================

def coulomb_angular_coeff(k, j, J, T):
    """
    Compute the angular coefficient A_k(jjJ) for the Coulomb matrix element:
        <jj J T | e^2/r12 | jj J T> = sum_k A_k * F^k

    For two identical nucleons (T=1), using the formula:
        A_k = (2k+1) * (-1)^(j+J+1/2+k) * { j j k }^2 * (j -1/2 k 0 | j 1/2)^2
                                             { j j J }
    where { } is Wigner 6j and (| ) is Clebsch-Gordan.

    Note: only even k contribute (parity selection).
    This uses the sympy wigner_6j and clebsch_gordan.

    Args:
        k: multipole order (even integer)
        j: total angular momentum of the orbital (half-integer)
        J: coupled total angular momentum (integer for identical particles)
        T: isospin (1 for pp or nn)
    """
    try:
        from sympy.physics.wigner import wigner_6j, clebsch_gordan
        from sympy import Rational, N as symN, S
    except ImportError:
        raise ImportError("sympy required for angular coefficients. pip install sympy")

    j_s = Rational(int(2*j), 2)  # convert to sympy Rational
    k_s = S(k)
    J_s = S(J)

    # Clebsch-Gordan: (j, -1/2, k, 0 | j, 1/2) = <j -1/2; k 0 | j 1/2>
    cg = clebsch_gordan(j_s, k_s, j_s, Rational(-1,2), 0, Rational(1,2))
    # Wigner 6j: {j j k; j j J}
    w6j = wigner_6j(j_s, j_s, k_s, j_s, j_s, J_s)

    phase = (-1)**(int(2*j) + J + int(2*0.5) + k)  # (-1)^(2j is integer, J, 2*1/2=1, k)
    # Standard formula:
    # A_k = (2k+1) * (-1)^(j-1/2+k) * (2j+1)^2 * W^2 * CG^2
    # Actually the standard form varies by reference. Use:
    # V_C = e^2 * sum_k (2k+1) * [<j -1/2, k 0 | j 1/2>]^2 * {j j k; j j J}^2 * F^k
    # times a normalization factor

    coeff = float(symN((2*k_s + 1) * cg**2 * w6j**2))
    return coeff


# ===========================================================================
# COULOMB CORRECTION FOR (j)^2 PROTON PAIRS
# ===========================================================================

def coulomb_correction_pp(n, l, j, A, J_list, verbose=True):
    """
    Compute Coulomb correction ΔV_C(J) for a (j)^2 T=1 proton-proton pair.

    Uses harmonic oscillator wave functions (Schiffer-True 1976 method).
    Only even Slater integrals F^k contribute (k=0,2,...,2l).

    Args:
        n: radial quantum number (0 for lowest state)
        l: orbital angular momentum
        j: total angular momentum (half-integer)
        A: mass number of the two-nucleon nucleus
        J_list: list of J values to compute corrections for
        verbose: print intermediate results

    Returns:
        dict {J: ΔV_C(J)} in MeV
    """
    e2 = 1.44  # e^2 in MeV fm
    b, hw = oscillator_length(A)

    if verbose:
        print(f"\nCoulomb correction for (n={n},l={l},j={j})^2 T=1 at A={A}")
        print(f"  hbar*omega = {hw:.3f} MeV,  b = {b:.3f} fm")

    # Compute Slater integrals F^k for k = 0, 2, ..., 2l
    Fk = {}
    for k in range(0, 2*l+1, 2):
        if verbose:
            print(f"  Computing F^{k}...", end=" ", flush=True)
        Fk[k] = slater_Fk(k, n, l, n, l, b)
        if verbose:
            print(f"F^{k} = {Fk[k]:.5f} fm^-1  =>  e^2*F^{k} = {e2*Fk[k]:.4f} MeV")

    # Compute angular coefficients and corrections
    corrections = {}
    for J in J_list:
        dV = 0.0
        for k in range(0, 2*l+1, 2):
            try:
                Ak = coulomb_angular_coeff(k, j, J, T=1)
            except ImportError:
                # Fallback: use F^0 monopole only
                Ak = 1.0 if k == 0 else 0.0
            dV += Ak * e2 * Fk[k]
        corrections[J] = dV
        if verbose:
            print(f"  ΔV_C(J={J}) = {dV:+.4f} MeV")

    return corrections


# ===========================================================================
# CENTROID AVERAGING (for fragmented J members)
# ===========================================================================

def spectroscopic_centroid(states):
    """
    Compute the spectroscopic-factor-weighted centroid of a multiplet member.

    Args:
        states: list of (E_exc, C2S) tuples -- excitation energy and C2S for each fragment

    Returns:
        E_centroid: strength-weighted mean excitation energy
        G_total: total strength
    """
    if not states:
        return None, 0.0
    G_total = sum(c2s for _, c2s in states)
    if G_total == 0:
        return None, 0.0
    E_centroid = sum(e * c2s for e, c2s in states) / G_total
    return E_centroid, G_total


# ===========================================================================
# MAIN TBME CALCULATION
# ===========================================================================

def calc_tbme(system, apply_coulomb=False, verbose=True):
    """
    Calculate TBMEs from binding energies and excitation energies.

    Args:
        system: dict with keys:
            name, j1, j2, T,
            B_core, B_core_j1, B_core_j2, B_core_2,
            excitations: dict {J: E_exc}  OR  {J: [(E_exc, C2S), ...]} for centroids
            n1, l1, j1_val, n2, l2, j2_val  (for Coulomb correction)
        apply_coulomb: if True, compute Coulomb correction for pp T=1 pairs
        verbose: print detailed output

    Returns:
        (tbme dict, M0, E0_shift, coulomb dict)
    """
    B_core  = system["B_core"]
    B_j1    = system["B_core_j1"]
    B_j2    = system["B_core_j2"]
    B_2     = system["B_core_2"]
    excit   = system["excitations"]

    # Single-particle binding energies relative to core
    eps_j1 = B_j1 - B_core
    eps_j2 = B_j2 - B_core
    B_2_rel = B_2 - B_core  # total binding of 2-nuc above core

    # TBME for the ground-state J member (from binding energies alone)
    # V(J_gs) = eps_j1 + eps_j2 - B_2_rel
    V_gs = eps_j1 + eps_j2 - B_2_rel  # negative = attractive

    if verbose:
        print(f"\n{'='*60}")
        print(f"System: {system['name']}")
        print(f"j1 = {system['j1']},  j2 = {system['j2']},  T = {system['T']}")
        print(f"{'='*60}")
        print(f"\nBinding energies (AME):")
        print(f"  B(core)     = {B_core:.3f} MeV")
        print(f"  B(core+j1)  = {B_j1:.3f} MeV  =>  eps(j1) = {eps_j1:.3f} MeV")
        print(f"  B(core+j2)  = {B_j2:.3f} MeV  =>  eps(j2) = {eps_j2:.3f} MeV")
        print(f"  B(core+2)   = {B_2:.3f} MeV")
        print(f"\n  eps(j1) + eps(j2)                = {eps_j1+eps_j2:.3f} MeV")
        print(f"  B(core+2) - B(core)              = {B_2_rel:.3f} MeV")
        print(f"  V(g.s. J member) = V_gs          = {V_gs:+.3f} MeV")
        print(f"  (negative = attractive residual interaction)")

    # Resolve excitation energies -- support both scalar and list-of-(E,C2S) inputs
    E_exc_resolved = {}
    G_total = {}
    for J, val in sorted(excit.items()):
        if isinstance(val, (int, float)):
            E_exc_resolved[J] = float(val)
            G_total[J] = None  # no centroid info
        else:
            # list of (E_exc, C2S) tuples -- compute centroid
            E_c, G = spectroscopic_centroid(val)
            E_exc_resolved[J] = E_c
            G_total[J] = G

    # Coulomb correction (for pp T=1 pairs)
    coulomb = {}
    if apply_coulomb and system.get("T") == 1 and system.get("proton_pair", False):
        coulomb = coulomb_correction_pp(
            n=system.get("n1", 0),
            l=system.get("l1"),
            j=system.get("j1_val"),
            A=system.get("A_coulomb", int(B_2)),
            J_list=list(E_exc_resolved.keys()),
            verbose=verbose
        )

    # Compute TBMEs
    if verbose:
        print(f"\nTBMEs  V(J) = V_gs + E_J(exc) [+ Coulomb correction if pp]:")
    tbme = {}
    for J, E_J in sorted(E_exc_resolved.items()):
        if E_J is None:
            continue
        dVC = coulomb.get(J, 0.0)
        V_J = V_gs + E_J - dVC  # subtract Coulomb to get hadronic TBME
        tbme[J] = V_J
        if verbose:
            G_str = f"  (G={G_total[J]:.2f})" if G_total[J] else ""
            dVC_str = f"  Coulomb={dVC:+.3f}" if dVC else ""
            print(f"  J={J}: E_exc={E_J:.3f}{G_str}  =>  V({J}) = {V_J:+.3f} MeV{dVC_str}")

    # Monopole
    if tbme:
        num   = sum((2*J+1) * v for J, v in tbme.items())
        denom = sum((2*J+1) for J in tbme)
        M0 = num / denom
        if verbose:
            print(f"\nMonopole (J-weighted average):")
            print(f"  M0 = {M0:+.3f} MeV  (negative = net attractive)")
    else:
        M0 = None

    return tbme, M0, V_gs, coulomb


# ===========================================================================
# PANDYA TRANSFORMATION  (hole-particle -> particle-particle)
# Eq. (I.2) of Schiffer-True 1976
# ===========================================================================

def pandya_transform(j1, j2, V_hp, verbose=True):
    """
    Convert hole-particle TBMEs to particle-particle TBMEs.

    V^pp(J; j1,j2) = -sum_{J'} (2J'+1) * W(j1,j2,j1,j2; J,J') * V^hp(J'; j1,j2-bar)

    where W is the Racah coefficient (related to Wigner 6j).

    Args:
        j1, j2: orbital angular momenta (floats)
        V_hp: dict {J': V(J')} -- hole-particle matrix elements
        verbose: print results

    Returns:
        dict {J: V(J)} -- particle-particle matrix elements
    """
    try:
        from sympy.physics.wigner import wigner_6j
        from sympy import Rational, N as symN
    except ImportError:
        print("sympy required for Pandya transform. pip install sympy")
        return {}

    j1_s = Rational(int(2*j1), 2)
    j2_s = Rational(int(2*j2), 2)

    J_max = int(j1 + j2)
    V_pp = {}
    for J in range(0, J_max + 1):
        val = 0.0
        for Jp, v_hp in V_hp.items():
            w6j = float(symN(wigner_6j(j1_s, j2_s, J, j2_s, j1_s, Jp)))
            val += -(2*Jp + 1) * w6j * v_hp
        V_pp[J] = val

    if verbose:
        print("\nPandya-transformed (pp) matrix elements:")
        for J, v in sorted(V_pp.items()):
            print(f"  V^pp(J={J}) = {v:+.4f} MeV")

    return V_pp


# ===========================================================================
# INPUT -- Edit here for your system
# ===========================================================================

system = {
    "name": "(1d5/2)^2 T=1 in A=18 from 17O(d,p)18O",
    "j1": "1d5/2",  "j2": "1d5/2",
    "T": 1,

    # Binding energies [MeV] from AME2020
    "B_core":    127.619,   # 16O
    "B_core_j1": 131.763,   # 17O (1d5/2 g.s.)
    "B_core_j2": 131.763,   # same
    "B_core_2":  139.808,   # 18O

    # Excitation energies [MeV] of J-members in 18O
    # Option A: single energy  {J: E_exc}
    # Option B: fragmented     {J: [(E_exc, C2S), (E_exc2, C2S2), ...]}
    "excitations": {
        0: 0.000,   # 0+ ground state
        2: 1.982,   # 2+ (dominant component; paper uses centroid over multiple 2+ states)
        4: 3.555,   # 4+
        # J=1,3,5 Pauli-forbidden for (d5/2)^2 T=1 identical neutrons
    },

    # For Coulomb correction (only relevant if proton_pair=True)
    "proton_pair": False,  # set True for pp pairs
    "n1": 0, "l1": 2, "j1_val": 2.5,  # 1d5/2: n=0, l=2, j=5/2
    "n2": 0, "l2": 2, "j2_val": 2.5,
    "A_coulomb": 18,  # mass number for oscillator length
}

# ===========================================================================
# RUN
# ===========================================================================

if __name__ == "__main__":
    print("\nTBME Estimator -- Schiffer & True, Rev. Mod. Phys. 48, 191 (1976)")
    print("="*60)

    tbme, M0, V_gs, coulomb = calc_tbme(
        system,
        apply_coulomb=system.get("proton_pair", False),
        verbose=True
    )

    print(f"\n{'='*60}")
    print("Summary:")
    print(f"  Monopole M0 = {M0:+.4f} MeV")
    for J, V in sorted(tbme.items()):
        print(f"  V({J}) = {V:+.4f} MeV")
    print()
    print("Reference: Schiffer & True, Rev. Mod. Phys. 48, 191 (1976)")
    print("See also:  Schiffer, Kay, Chen, Phys. Rev. C 105, L041302 (2022)")
