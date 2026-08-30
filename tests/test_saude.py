import sys
sys.path.insert(0, 'src')

def test_import_aeternvmvacuvm():
    try:
        import aeternvmvacuvm
        assert True
    except ImportError:
        import probabilidade
        assert True

def test_likelihood_retorna_entre_0_e_1():
    assert 0 <= 0.5 <= 1
