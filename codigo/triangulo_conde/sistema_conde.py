from triangulo import LeituraRegua, TrianguloConde

def main():
    tri = TrianguloConde(alpha=1.0, beta=1.0)

    print("=== Teste 1: Q95 da Regua ===")
    leitura1 = TrianguloConde.leitura_a_partir_de_Z_prime(z_prime=TrianguloConde.Q95_REGUA, L=1.5, delta=0.05)
    resultado1 = tri.mapear(leitura1)
    print(tri.resumo(resultado1))
    
    print("\n=== Teste 2: Cosmologico Bootes ===")
    leitura2 = LeituraRegua(Z0=15.0, grad=1.5, L=2.5, delta=0.5)
    resultado2 = tri.mapear(leitura2)
    print(tri.resumo(resultado2))

if __name__ == "__main__":
    main()
