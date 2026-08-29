import numpy as np
from viec_mkIII_control_crouzeix import crouzeix_check, positive_real_completion

def run_production():
    f = 1e9
    Z0 = 50.0
    Zvac = 376.73
    S11 = 0.05 + 0.02j
    S21 = 0.95 - 0.01j
    A = np.array([[S11, S21],[S21, S11]], dtype=complex)
    chk = crouzeix_check(A, Vin=1.0)
    comp = positive_real_completion(S11, S21, Z0, Zvac, f)
    print(f"Crouzeix passed: {chk['passed']} - bound {chk['criterion']:.3f} < 1.8V")
    print(f"Comp L={comp['L_match']*1e9:.2f}nH C={comp['C_match']*1e12:.2f}pF")
    if chk['passed']:
        print("VIEC-01 Mk.IV-C PRONTO PARA MEDICAO")
    return chk['passed']

if __name__ == "__main__":
    run_production()
