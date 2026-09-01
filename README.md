[![CI](https://github.com/gustavosouzaconde40-ai/conde-ruler/actions/workflows/python-package.yml/badge.svg)](https://github.com/gustavosouzaconde40-ai/conde-ruler/actions/workflows/python-package.yml) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# Conde-Ruler

Conde-Ruler is a lightweight Python package that provides a reproducible, programmatic "ruler" for measuring and characterizing the Conde current from observational time series.

## Installation

Install from source (recommended for development):

pip install .

For development and running the test-suite (requires the `test` extra declared in pyproject.toml):

pip install -e ".[test]"

## Quickstart

The example below shows a minimal usage pattern. Replace `CondeRuler` and method names with the actual API if different.

```python
from conde_ruler import CondeRuler

# create an instance (or call the top-level API)
cr = CondeRuler()

# load or prepare your time series (pandas Series or numpy array)
# time_series = ...

# measure the Conde current
result = cr.measure(time_series)

# result is a dictionary or object containing amplitude, phase and diagnostics
print(result)
```

Include a short, runnable example in `examples/` or `notebooks/` for users to reproduce results quickly.

## Large datasets

Large datasets (for example, `prime_gaps_1M.csv.gz`) have been moved to Zenodo to keep the repository lightweight. Please download them from the project's Zenodo archive (DOI to be added) or contact the maintainer. Small example datasets required for tests and tutorials are included in the repository.

## Running tests

Run the test-suite with pytest after installing the test extras:

pip install -e ".[test]"
pytest -q

To run a specific test file:

pytest tests/test_likelihood_emulator.py -q

Note: Tests should import the installed package (avoid manipulating sys.path in tests). Ensure `pyproject.toml` is configured to install the package correctly (use `packages` or `project` name and `src/` layout if needed).

## How to cite

Please cite the software using the JOSS paper and the repository:

Gustavo Alves Conde (2026). Conde‑Ruler: a Python ruler for measuring the Conde current. https://github.com/gustavosouzaconde40-ai/conde-ruler

A machine-readable citation is provided in `CITATION.cff`.

## License

This project is licensed under the terms in the `LICENSE` file.
v1.0.3 - 01/09/2026
