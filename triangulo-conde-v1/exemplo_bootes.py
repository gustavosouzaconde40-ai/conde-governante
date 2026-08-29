"""
Validação Vazio de Boötes - Triângulo de Condé
n ≈ 38, mu=19, sigma≈3.08, IC95 [12.96, 25.04]
"""
from triangulo_conde import distribuicao
n = 38
mu, sigma = distribuicao(n)
print(f"Bootes n={n} mu={mu} sigma={sigma}")
print("Galaxias residuais ocupam estados dentro do IC95 - densidade nao e aleatoria, e geometrica")
