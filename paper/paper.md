---
title: "Conde-Ruler: a Python ruler for measuring the Conde current"
tags: [Conde_current, geophysical_measurement, time_series, Python]
authors:
    - name: Gustavo Alves Conde
    affiliation: Independent Researcher, Baixo Guandu, ES, Brazil
date: 2026-08-31
bibliography: paper.bib
---

Summary

Conde-Ruler is a lightweight Python package that provides a reproducible, programmatic "ruler" for measuring and characterizing the Conde current from observational time series. The package implements a set of algorithms to (1) extract the local amplitude and phase of the Conde current, (2) compute standard summary statistics and derived metrics, and (3) produce publication-quality numeric and graphical outputs. Conde-Ruler is intended to make routine processing of Conde current observations fast, auditable, and repeatable for researchers and engineers working with coastal and oceanographic current measurements.

Statement of need

Accurate, reproducible measurement of oceanic and coastal currents is central to many scientific and engineering applications (e.g., transport estimation, coastal hazards, and ecosystem studies). The Conde current – a domain-specific flow pattern encountered in [insert regional/contextual description in documentation] – is commonly reported by different observational platforms and processed with ad hoc scripts that are rarely packaged, tested, or documented for reuse.

Conde-Ruler addresses this gap by providing:
- A small, opinionated library of measurement routines that codify best practices for Conde current extraction and summarization.
- A single, documented API suitable for batch processing of time series and interactive exploratory analysis.
- Outputs designed to be easily integrated into reproducible pipelines (machine-readable summaries, figures, and checks that can be run in continuous integration).

By packaging these routines, Conde-Ruler reduces duplication of effort, lowers the barrier to reproducible Conde current analysis, and helps researchers compare results across datasets and methods.

Features

Conde-Ruler implements the following core capabilities:

- Time series preprocessing
    - Uniform resampling, gap handling, detrending, and optional smoothing tailored for Conde current signals.

- Conde current extraction
    - Algorithms to estimate local amplitude and phase of the Conde current from one-dimensional or multichannel observations.
    - Multiple estimator options (deterministic filtering and a likelihood-based emulator) to support sensitivity analysis.

- Summary statistics and diagnostics
    - Computation of mean, variance, spectral estimates, and event detection tied to Conde current behavior.
    - Diagnostic tests and goodness-of-fit metrics to assess extraction robustness on observed data.

- Reproducible outputs
    - Machine-readable summary tables (CSV/JSON), standardized plots (PNG/SVG), and example notebooks demonstrating end-to-end workflows.
    - Small curated example datasets bundled for tests and tutorials; large datasets may be referenced externally with provenance metadata.

- Quality control and testing
    - A test suite (pytest) exercising importability, numerical consistency on synthetic cases, and key edge cases to guard against regressions.
    - Continuous integration examples provided in the repository to run tests automatically on supported Python versions.

- Extensibility
    - Modular API design to allow users to add new estimators, diagnostic measures, or output formats without modifying core functions.

Quality control

Conde-Ruler includes a unit and integration test-suite (pytest) that exercises importability, numerical consistency on synthetic data, and core edge cases. The repository provides a small curated example dataset for tests and tutorials; larger datasets are stored externally. Continuous integration (GitHub Actions) is configured to run the test-suite across supported Python versions (3.9, 3.10, 3.11) on each push and pull request.

Availability

Source code: GitHub — https://github.com/gustavosouzaconde40-ai/conde-ruler
License: MIT (see LICENSE file)
Installation: pip install. or pip install -e ".[test]" for development and tests.
Supported Python versions: officially tested on 3.9, 3.10 and 3.11.
Large datasets: archived on Zenodo (DOI to be added when available).

References

1. Conde, G. A. (2026). Conde-Ruler: a Python ruler for measuring the Conde current (version 0.1). GitHub repository. https://github.com/gustavosouzaconde40-ai/conde-ruler
