import importlib.util
import inspect
from pathlib import Path
import pytest


def _find_emulator_module_paths():
    repo_root = Path(__file__).parent.parent
    candidates = [
        repo_root / "codigo" / "likelihood_emulator.py",
        repo_root / "codigo" / "triangulo_conde" / "likelihood_emulator.py",
        repo_root / "likelihood_emulator.py",
    ]
    return [p for p in candidates if p.exists()]


def _load_function_from_path(path):
    spec = importlib.util.spec_from_file_location("likelihood_emulator", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # try common function names
    for name in ("compute_likelihood", "computeLikelihood", "likelihood", "compute_likelihood_score"):
        if hasattr(mod, name):
            return getattr(mod, name)
    # fallback: if module exposes a single callable at top-level, use it
    callables = [getattr(mod, a) for a in dir(mod) if callable(getattr(mod, a))]
    # exclude common imports
    callables = [c for c in callables if getattr(c, "__module__", "").startswith("likelihood_emulator")]
    if len(callables) == 1:
        return callables[0]
    pytest.skip("No suitable compute_likelihood function found in module: %s" % path)


def _is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _check_result_in_unit_interval(res):
    # scalar
    if _is_number(res):
        return 0.0 <= float(res) <= 1.0
    # numpy array or similar
    if hasattr(res, "tolist"):
        try:
            vals = res.tolist()
        except Exception:
            return False
        return all(_is_number(v) and 0.0 <= float(v) <= 1.0 for v in (vals if isinstance(vals, (list, tuple)) else [vals]))
    # list/tuple
    if isinstance(res, (list, tuple)):
        return all(_is_number(v) and 0.0 <= float(v) <= 1.0 for v in res)
    return False


def test_compute_likelihood_returns_between_0_and_1_and_handles_empty_input():
    """Verifica que compute_likelihood (ou similar) retorna valor entre 0 e 1 e não quebra com entrada vazia."""
    paths = _find_emulator_module_paths()
    if not paths:
        pytest.skip("Nenhum módulo likelihood_emulator encontrado em paths esperados")

    func = None
    for p in paths:
        try:
            func = _load_function_from_path(p)
            break
        except pytest.skip.Exception:
            raise
        except Exception:
            # try next path
            func = None
    if func is None:
        pytest.skip("Não foi possível carregar uma função de likelihood de nenhum dos módulos candidatos")

    # Try several "empty" invocation patterns and ensure at least one works and returns value in [0,1]
    tried = []
    successes = []

    candidates = [(), ([],), ({},), (None,)]

    for args in candidates:
        try:
            if args == ():
                res = func()
            else:
                # single-argument call
                res = func(args[0])
            tried.append((args, res))
            if _check_result_in_unit_interval(res):
                successes.append((args, res))
        except TypeError:
            # signature mismatch, try next
            continue
        except Exception as e:
            # function raised for this input - record and continue
            tried.append((args, e))
            continue

    assert successes, (
        "compute_likelihood did not return a numeric value in [0,1] for any of the empty inputs tried. "
        f"Tried: {[(a, type(r)) for a, r in tried]}"
    )
