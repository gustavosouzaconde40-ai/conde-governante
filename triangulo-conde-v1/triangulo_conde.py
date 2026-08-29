"""
Triângulo de Condé - Código de Referência v1.0.0
Teoria Aeternvm Vacuvm
"""
import math
from math import comb

MEDIA = 1.00041294
Q95 = 2.64012536
Q99 = 3.90317770

def Z_prime(gap, p):
    return gap / math.log(p)

def calcula_n(L, lambda0=1.0, gradZ=0.1, Z0=15.0, delta=0.5, alpha=1.0, beta=1.0):
    return alpha * (L/lambda0) * (1 + beta * abs(gradZ)/Z0) * (1/(1-delta))

def P_k_n(k, n):
    return comb(n, k) / (2**n)

def distribuicao(n):
    mu = n/2
    sigma = math.sqrt(n)/2
    return mu, sigma

if __name__ == "__main__":
    n_bootes = 38
    mu, sigma = distribuicao(n_bootes)
    print(f"Bootes n={n_bootes} mu={mu} sigma={sigma:.2f} IC95=[{mu-1.96*sigma:.2f}, {mu+1.96*sigma:.2f}]")
