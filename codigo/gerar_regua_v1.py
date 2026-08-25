#!/usr/bin/env python3
# gerar_regua_v1.py - A MÁQUINA da Régua Condé v1
# Gera 1.000.000 primos até 15.485.863 e calcula Z' = gap / ln(p)
import math

def gerar_primos(n_primos=1_000_000):
    limite_estimado = 16_000_000
    sieve = bytearray(b'\x01') * (limite_estimado+1)
    sieve[0:2] = b'\x00\x00'
    primos = []
    for i in range(2, limite_estimado+1):
        if sieve[i]:
            primos.append(i)
            if len(primos) >= n_primos:
                break
            step = i
            start = i*i
            if start <= limite_estimado:
                sieve[start:limite_estimado+1:step] = b'\x00' * ((limite_estimado - start)//step +1)
    return primos[:n_primos]

primos = gerar_primos()
print(f"Gerados {len(primos)} primos, ultimo = {primos[-1]}")

with open('regua_conde_v1.csv','w') as f:
    f.write('n,p_n,gap,Z_prime\n')
    for i in range(len(primos)-1):
        p = primos[i]
        gap = primos[i+1]-p
        z = gap / math.log(p)
        f.write(f"{i+1},{p},{gap},{z:.8f}\n")
print("Arquivo regua_conde_v1.csv gerado com sucesso!")
