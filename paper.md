---
title: 'Conde-Ruler: A Python Ruler for Measuring the Conde Current from Prime Gaps'
tags: [Python, prime gaps, anomaly detection, statistics, time series]
authors:
- name: Gustavo Alves Condé
  orcid: 0009-0003-8264-7907
  affiliation: 1
affiliations:
- name: Independent Researcher, Baixo Guandu, ES, Brazil
  index: 1
date: 02 September 2026
bibliography: paper.bib
---

# Summary

Conde-Ruler is a lightweight, pure-Python package that provides a reproducible and immutable statistical ruler derived from one million prime gaps. The ruler is characterized by mean 1.00041294, q95=2.64 and q99=3.90, calculated from the file prime_gaps_1M.csv.gz archived on Zenodo. The package allows any observational time series to be measured against this ruler to extract the Conde current and to flag anomalous intervals in a comparable way across domains [@caldwell1998][@oliveira2014].

The core API is `from conde_governante import CondeRuler`, installable via `pip install .` from the repository. All versions are archived with a Concept DOI 10.5281/zenodo.22095020 and version DOIs (e.g., v1.0.6: 10.5281/zenodo.22237483).

# Statement of need

Anomaly detection in observational time series often relies on data-dependent thresholds that change between datasets, hindering reproducibility. Researchers in geophysics, hydrology and space physics need a stable, domain-agnostic reference to quantify deviations.

Conde-Ruler addresses this need by using the empirical distribution of prime gaps as a universal ruler. Prime gaps are well-studied, stationary and independent of the observed system, providing an external reference. The package was created to support the Conde current studies developed by the author, where the current is defined as the deviation of local gap statistics from the global prime-gap ruler.

# State of the field

Existing Python ecosystems for time series analysis include scipy [@virtanen2020], scikit-learn for outlier detection [@pedregosa2011], and stumpy for matrix profiles. For prime numbers, libraries focus on primality testing and generation, not on using gap statistics as a measurement tool.

The distribution of prime gaps has been studied theoretically [@goldston2007] and empirically [@caldwell1998]. However, no package provides a versioned, citable ruler with q95/q99 thresholds ready for direct application to arbitrary time series. Conde-Ruler fills this gap by packaging the 1M-gap dataset, the ruler calibration, and the measurement functions in a tested, MIT-licensed library with GitHub Actions CI.

# Software design

The package is organized in `src/conde_governante/` and `conde_governante/` shim for backward compatibility. Main modules are `ruler.py` that loads the 1M-gap statistics and exposes RULER_MEAN, RULER_Q95 and RULER_Q99, `current.py` with CondeRuler class that computes rolling gap metrics and Conde current, `anomaly.py` for thresholding against q95/q99, and `testes/` with pytest suite. Auxiliary web demo is provided via `index.html` + `app.js`. Installation is via `pyproject.toml`.

# Research impact statement

By providing an immutable external ruler, Conde-Ruler enables cross-study comparison of anomalies without retraining. Applications include detection of geomagnetic disturbances, hydrological extremes and laboratory plasma currents where the author has applied the Conde current concept. The Zenodo archiving ensures long-term reproducibility.

# AI usage disclosure

No generative AI was used to write the scientific code, the ruler calibration, or the scientific claims. Generative AI was used only for English grammar correction and for formatting the JOSS paper to comply with the required sections.

# Acknowledgements

The author thanks the open prime gap datasets community and Zenodo for archiving.

# References
