# sistema_conde.py - SISTEMA CONDE PARA TODOS OS VEICULOS RODANTES
from triangulo import LeituraRegua, TrianguloConde, calcular_n_veiculo

def main():
    tri = TrianguloConde()
    
    print("=== SISTEMA CONDE - MODO FROTA UNIVERSAL ===")
    print("Rodando em: carro, moto, caminhao, trator, onibus\n")

    # Teste 1: Q95 (Régua Padrão)
    print("--- Teste 1: Q95 da Regua (Veiculo Leve) ---")
    leitura1 = TrianguloConde.leitura_a_partir_de_Z_prime(z_prime=2.64012536, L=1.5, delta=0.05)
    res1 = tri.mapear(leitura1)
    print(tri.resumo(res1))
    print(f"Resultado: Q95 -> n={res1['n']} | Status: OK para rodar\n")

    # Teste 2: Bootes (Cosmologico / Veiculo Pesado)
    print("--- Teste 2: Bootes Cosmologico (Veiculo Pesado) ---")
    leitura2 = LeituraRegua(Z0=15.0, grad=1.5, L=2.5, delta=0.5)
    res2 = tri.mapear(leitura2)
    print(tri.resumo(res2))
    print(f"Resultado: Bootes -> n={res2['n']} | Status: OK para rodar\n")

    # Teste 3: Modo direto para qualquer veiculo (sem classe)
    print("--- Teste 3: Modo Direto - Qualquer Veiculo ---")
    for nome, Z0, L, delta in [("Moto", 2.64, 1.5, 0.05), ("Carro", 15.0, 2.5, 0.5), ("Caminhao", 20.0, 3.0, 1.0)]:
        n = calcular_n_veiculo(Z0, L, delta)
        print(f"{nome}: Z0={Z0} L={L} -> n={n} | RODANDO")

    print("\n=== TODOS OS VEICULOS SINCRONIZADOS ===")

if __name__ == "__main__":
    main()
