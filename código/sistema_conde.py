# Sistema Conde - Integração Régua + Triângulo
# Funciona mesmo com pasta com acento

import sys
import os
sys.path.append(os.path.dirname(__file__))

# importa o triangulo da pasta que você criou
try:
    from triângulo_conde.triângulo import TrianguloConde, LeituraRegua
except:
    from código.triângulo_conde.triângulo import TrianguloConde, LeituraRegua

class SistemaConde:
    def __init__(self, alpha=1.0, beta=1.0):
        self.triangulo = TrianguloConde(alpha, beta)
    
    def medir_e_mapear(self, z_prime, L, delta):
        leitura = self.triangulo.leitura_a_partir_de_Z_prime(z_prime, L, delta)
        return self.triangulo.mapear(leitura)

# Teste rápido que prova que está sincronizado
if __name__ == "__main__":
    s = SistemaConde()
    r1 = s.medir_e_mapear(2.64012536, 1.5, 0.05)
    print(f"Q95 -> n={r1['n']} mu={r1['mu']}") # tem que dar n=4
    
    r2 = s.medir_e_mapear(15.0, 2.5, 0.5)
    print(f"Bootes -> n={r2['n']} mu={r2['mu']} 95%={r2['intervalo_95']}") # tem que dar n=38
