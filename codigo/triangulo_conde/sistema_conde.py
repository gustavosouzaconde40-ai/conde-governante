from triangulo import TrianguloConde

def main():
    sistema = TrianguloConde()
    testes = ["Q95", "Bootes"]
    for nome in testes:
        n = sistema.calcular(nome)
        print(f"{nome} -> n={n}")

if __name__ == "__main__":
    main()
