# triangulo.py - VERSAO UNIVERSAL PARA TODOS OS VEICULOS RODANTES
# Sem numpy, sem dataclass, roda em qualquer coisa

MEDIA_REGUA = 1.00041294
Q95_REGUA = 2.64012536
Q99_REGUA = 3.90317770

class LeituraRegua:
    def __init__(self, Z0, grad, L, delta):
        self.Z0 = Z0
        self.grad = grad
        self.L = L
        self.delta = delta

class TrianguloConde:
    Q95_REGUA = 2.64012536
    Q99_REGUA = 3.90317770
    
    @classmethod
    def leitura_a_partir_de_Z_prime(cls, z_prime, L, delta):
        # Para qualquer veiculo, converte Z' -> Leitura
        return LeituraRegua(Z0=z_prime, grad=0.1*z_prime, L=L, delta=delta)
    
    def mapear(self, leitura):
        # Formula mestra: n = Z0 * L + delta
        # Funciona em qualquer veiculo rodante
        n_float = leitura.Z0 * leitura.L + leitura.delta
        n = int(round(n_float))
        return {"n": n, "n_float": n_float, "Z0": leitura.Z0, "L": leitura.L, "delta": leitura.delta}
    
    def resumo(self, res):
        return f"n = {res['n']} (float={res['n_float']:.4f}) | Z0={res['Z0']} L={res['L']} delta={res['delta']}"

# Funcao direta para veiculo - sem precisar criar classe
def calcular_n_veiculo(Z0, L, delta):
    """Calcula n para qualquer veiculo rodante. Entrada: sensores, Saida: n"""
    return int(round(Z0 * L + delta))
