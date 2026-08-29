import numpy as np

SAMPLE_RATE_B210 = 61.44e6
SAMPLE_RATE_RFSOC = 1e9

def gaussian_pulse(fs, w=1.0):
    ws = w * 1e-9
    t = np.arange(-3*ws, 3*ws, 1/fs)
    sigma = ws / 2.355
    return (np.exp(-0.5*(t/sigma)**2) * np.blackman(len(t))).astype(np.complex64)

def raised_cosine(fs, w=16):
    ws = w * 1e-9
    t = np.arange(-2*ws, 2*ws, 1/fs)
    return (np.sinc(t/ws) * np.cos(np.pi*0.5*t/ws) / (1-(t/ws)**2+1e-12)).astype(np.complex64)

def numerical_range_bound(A):
    vals = []
    for _ in range(2000):
        x = np.random.randn(A.shape[0]) + 1j*np.random.randn(A.shape[0])
        x = x/np.linalg.norm(x)
        vals.append(np.vdot(x, A @ x))
    vals = np.array(vals)
    maxW = np.max(np.abs(vals))
    norm2 = np.linalg.norm(A, 2)
    ok = norm2 <= 2*maxW*1.1
    return maxW, norm2, ok

def crouzeix_check(A, Vin=1.0, Vth_high=1.8):
    maxW, norm2, ok = numerical_range_bound(A)
    criterion = 2 * maxW * Vin
    passed = criterion < Vth_high
    return {'maxW': float(maxW), 'norm2': float(norm2), 'bound_ok': bool(ok), 'criterion': float(criterion), 'passed': bool(passed)}

def positive_real_completion(S11, S21, Z0=50.0, Zvac=376.73, f=1e9):
    Zmeas = Z0 * (1 + S11) / (1 - S11 + 1e-12)
    ratio = Zvac / Zmeas
    L_match = (Zvac - Z0) / (2 * np.pi * f)
    C_match = 1.0 / (2 * np.pi * f * Zvac)
    return {'L_match': float(L_match), 'C_match': float(C_match), 'ratio': complex(ratio), 'Zmeas': complex(Zmeas)}

if __name__ == "__main__":
    A = np.array([[0,0.1,0],[0.1,0,0.1],[0,0.1,0]], dtype=complex)
    print(crouzeix_check(A))
