# Contributing

- Runtime code uses the standard library only.
- Every bug fix adds a regression test to `tests/test_<module>.py`.
- Keep fixes minimal: no refactors, renames or formatting changes in the same PR.
- Do not change `.github/`, `pyproject.toml` or `requirements-dev.txt` in a fix PR.
