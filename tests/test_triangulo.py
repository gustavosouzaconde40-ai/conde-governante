import importlib.util
from pathlib import Path


def _load_triangulo():
    repo_root = Path(__file__).parent.parent
    module_path = repo_root / "codigo" / "triangulo_conde" / "triangulo.py"
    spec = importlib.util.spec_from_file_location("triangulo", str(module_path))
    triangulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(triangulo)
    return triangulo


def test_q95_returns_4():
    """Q95 deve mapear para n = 4 usando calcular_n_veiculo"""
    triangulo = _load_triangulo()
    n = triangulo.calcular_n_veiculo(triangulo.Q95_REGUA, 1.6, 0)
    assert n == 4


def test_bootes_returns_38():
    """Bootes deve mapear para n = 38 usando TrianguloConde.mapear"""
    triangulo = _load_triangulo()
    leitura = triangulo.TrianguloConde.leitura_a_partir_de_Z_prime(triangulo.MEDIA_REGUA, 38, 0)
    res = triangulo.TrianguloConde().mapear(leitura)
    assert res["n"] == 38
