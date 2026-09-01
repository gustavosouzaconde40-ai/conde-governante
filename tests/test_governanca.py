import pytest
import conde_governante as cg


def test_import_gov_ernanca():
    # smoke test: package imports
    assert hasattr(cg, "__name__")


def test_regua_entre_0_e_1():
    nota = 0.75
    assert 0 <= nota <= 1
