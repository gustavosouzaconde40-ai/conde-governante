import math
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict
import numpy as np

@dataclass
class LeituraRegua:
    """Representa uma leitura feita pela Regua de Conde."""
    Z0: float  # Impedancia de fundo
    grad: float  # Gradiente de impedancia (nabla Z)
    L: float  # Escala caracteristica do vortice
    delta: float  # Grau de deplecao

class TrianguloConde:
    """
    Triangulo de Conde: ferramenta combinatorio-estatistica acoplada a Regua de Conde.
    Mapeia leituras de campo em distribuicoes de estados e aproximacoes gaussianas.
    Teoria Aeternvm Vacvvm - Gustavo Souza Conde - 28/08/2026
    """
    # Constantes oficiais da Regua de Conde (valores imutaveis)
    MEDIA_REGUA = 1.00041294
    Q95_REGUA = 2.64012536
    Q99_REGUA = 3.90317770

    def __init__(self, alpha: float = 1.0, beta: float = 1.0):
        self.alpha = alpha
        self.beta = beta

    @classmethod
    def leitura_a_partir_de_Z_prime(cls, z_prime: float, L: float, delta: float) -> LeituraRegua:
        """
        Constroi uma LeituraRegua a partir de um valor Z' (gap / ln(p)).
        util para integrar com as saidas da Regua de Conde.
        """
        Z0 = z_prime
        grad = 0.1 * z_prime  # placeholder - substituir por medicao direta do gradiente
        return LeituraRegua(Z0=Z0, grad=grad, L=L, delta=delta)

    def calcular_n(self, leitura: LeituraRegua) -> float:
        """Calcula o indice de complexidade n a partir da leitura da Regua. Eq (3)"""
        return self.alpha * leitura.Z0 * leitura.L + self.beta * leitura.delta

    def linha_triangulo(self, n: int) -> List[int]:
        """Retorna a linha n do Triangulo de Pascal (coeficientes binomiais). Eq (1)"""
        if n < 0:
            return []
        return [math.comb(n, k) for k in range(n + 1)]

    def distribuicao_discreta(self, n: int) -> List[float]:
        """Retorna P(k|n) = C(n,k)/2^n. Eq (5)"""
        if n >= 64:  # evita overflow de 2^n
            # retorna aproximacao gaussiana discretizada
            mu = n/2; sigma = math.sqrt(n)/2
            xs = np.arange(0, n+1)
            gauss = (1.0/(sigma*math.sqrt(2*math.pi))) * np.exp(-((xs-mu)**2)/(2*sigma*sigma))
            return (gauss/gauss.sum()).tolist()
        linha = self.linha_triangulo(n)
        total = 1 << n  # 2^n
        return [c / total for c in linha]

    def mapear(self, leitura: LeituraRegua) -> dict:
        """
        Funcao principal de mapeamento.
        Entrada: leitura da Regua.
        Saida: dicionario com n, distribuicao discreta, mu, sigma, densidade de estados.
        Eqs (4), (5), (6)
        """
        n_float = self.calcular_n(leitura)
        n_int = int(round(n_float))
        if n_int < 0:
            n_int = 0

        dist_discreta = self.distribuicao_discreta(n_int)
        mu = n_int / 2.0
        sigma = math.sqrt(n_int) / 2.0 if n_int>0 else 0.0

        def gaussiana(x: float) -> float:
            if sigma == 0:
                return 0.0
            return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma * sigma))

        return {
            'n': n_int,
            'n_float': n_float,
            'distribuicao_discreta': dist_discreta,
            'coeficientes': self.linha_triangulo(n_int) if n_int < 50 else f"n grande ({n_int}), {n_int+1} coeficientes - use distribuicao_discreta",
            'mu': mu,
            'sigma': sigma,
            'densidade_estados': (1 << n_int) if n_int < 63 else float('inf'),
            'gaussiana': gaussiana,
            'leitura_original': leitura,
            'intervalo_95': (mu - 1.96*sigma, mu + 1.96*sigma),
            'intervalo_99': (mu - 2.576*sigma, mu + 2.576*sigma)
        }

    def resumo(self, resultado: dict) -> str:
        n = resultado['n']
        mu = resultado['mu']
        sigma = resultado['sigma']
        dist = resultado['distribuicao_discreta']
        dens = resultado['densidade_estados']
        i95 = resultado['intervalo_95']
        i99 = resultado['intervalo_99']
        linhas = [
            f"=== Triangulo de Conde - Resumo ===",
            f"n = {n} (float={resultado['n_float']:.4f})",
            f"mu = {mu:.4f}, sigma = {sigma:.4f}",
            f"Densidade de estados = {dens}",
            f"95% em k ∈ [{i95[0]:.2f}, {i95[1]:.2f}]",
            f"99% em k ∈ [{i99[0]:.2f}, {i99[1]:.2f}]",
            f"Coeficientes (primeiros 10): {resultado['coeficientes'][:10] if isinstance(resultado['coeficientes'], list) else resultado['coeficientes']}",
            f"P(k|n) max = {max(dist):.4f} em k={dist.index(max(dist))}",
        ]
        return "\n".join(linhas)

    def calibrar(self, dados: List[Tuple[LeituraRegua, Tuple[float, float]]]) -> None:
        """
        Calibra alpha e beta por ajuste de momentos.
        dados: lista de (leitura, (mu_obs, sigma_obs))
        """
        if not dados:
            return
        try:
            from scipy.optimize import minimize
        except ImportError:
            print("scipy nao encontrado - calibracao requer scipy")
            return

        def erro(params):
            alpha, beta = params
            erro_total = 0.0
            for leitura, (mu_obs, sigma_obs) in dados:
                n = alpha * leitura.Z0 * leitura.L + beta * leitura.delta
                if n < 0: n = 0
                mu_pred = n / 2.0
                sigma_pred = math.sqrt(max(0, n)) / 2.0
                erro_total += (mu_pred - mu_obs)**2 + (sigma_pred - sigma_obs)**2
            return erro_total

        inicial = [self.alpha, self.beta]
        resultado = minimize(erro, inicial, method='Nelder-Mead')
        if resultado.success:
            self.alpha, self.beta = resultado.x
            print(f"Calibracao OK: alpha={self.alpha:.6f}, beta={self.beta:.6f}")
        else:
            print("Falha na calibracao. Mantendo valores anteriores.")

    def gerar_histograma(self, n: int, ax=None, salvar_em=None):
        import matplotlib.pyplot as plt
        import numpy as np
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 5))
        dist = self.distribuicao_discreta(n)
        k = list(range(n + 1))
        ax.bar(k, dist, alpha=0.7, label=f'Binomial n={n}')
        mu = n / 2.0
        sigma = math.sqrt(n) / 2.0
        x = np.linspace(0, n, 300)
        gauss = (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma * sigma))
        ax.plot(x, gauss, 'r-', label='Gaussiana limite')
        ax.set_xlabel('k (estado)')
        ax.set_ylabel('P(k|n)')
        ax.set_title(f'Convergencia Binomial -> Gaussiana n={n} | mu={mu}, sigma={sigma:.2f}')
        ax.legend()
        ax.grid(True, alpha=0.3)
        if salvar_em:
            plt.savefig(salvar_em, dpi=150)
        if ax is None:
            plt.show()
        return ax

# --- Calibracao pre-definida para os 4 regimes do artigo ---
CALIBRACAO_4_REGIMES = [
    (LeituraRegua(1.0, 0.2, 1.0, 0.01), (3.0, 1.2)),
    (LeituraRegua(2.0, 0.5, 1.5, 0.03), (6.5, 1.8)),
    (LeituraRegua(3.0, 0.8, 2.0, 0.05), (10.0, 2.5)),
    (LeituraRegua(15.0, 1.5, 2.5, 0.5), (19.0, 3.08)),  # Bootes
]

if __name__ == "__main__":
    tri = TrianguloConde(alpha=1.0, beta=1.0)
    
    print("=== Teste 1: Q95 da Regua ===")
    leitura1 = TrianguloConde.leitura_a_partir_de_Z_prime(z_prime=TrianguloConde.Q95_REGUA, L=1.5, delta=0.05)
    resultado1 = tri.mapear(leitura1)
    print(tri.resumo(resultado1))
    print()
    
    print("=== Teste 2: Cosmologico Bootes ===")
    leitura2 = LeituraRegua(Z0=15.0, grad=1.5, L=2.5, delta=0.5)
    resultado2 = tri.mapear(leitura2)
    print(tri.resumo(resultado2))
    print()
    
    print("=== Teste 3: Q99 com L grande ===")
    leitura3 = TrianguloConde.leitura_a_partir_de_Z_prime(z_prime=TrianguloConde.Q99_REGUA, L=10.0, delta=1.0)
    resultado3 = tri.mapear(leitura3)
    print(tri.resumo(resultado3))

