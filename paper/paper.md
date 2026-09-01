

## Quality control

Conde‑Ruler includes a unit and integration test-suite (pytest) that exercises importability, numerical consistency on synthetic data, and core edge cases. The repository provides a small curated example dataset for tests and tutorials; larger datasets are stored externally. Continuous integration (GitHub Actions) is configured to run the test-suite across supported Python versions on each push and pull request.

## Availability

Source code: GitHub — https://github.com/gustavosouzaconde40-ai/conde-ruler  
License: MIT (see LICENSE file)  
Installation: pip install . or pip install -e ".[test]" for development and tests.  
Supported Python versions: officially tested on 3.9, 3.10 and 3.11.  
Large datasets: archived on Zenodo (DOI to be added when available).
