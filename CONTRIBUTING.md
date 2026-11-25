# Contributing guide

Submissions of design agents, agent Skills, design editors or research benchmarks are welcome. Please provide the canonical GitHub repository, the primary purpose, the applicable boundary, features, and original links for the license. Projects that only exist as a hosted service are not listed in the core; documentation, formats and reference indexes must state their nature clearly.

Edit `data/projects.json`, keep pinned-commit links to the README or official docs; check LICENSE, NOTICE and the separate terms of data, fonts and assets. Do not edit the generated README or rankings directly. New entries keep `baseline` as `false`; the four seed entries of the first release do not change.

Locally you need Python 3.12+ and an authenticated GitHub CLI (or `GH_TOKEN` configured).

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

## Multilingual files

- `data/projects.json` is the canonical reviewed data in Chinese: facts are changed only here, once.
- Wording in other languages comes from `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`) and `locales/<lang>/ui.json`; `zh` falls back to `data/projects.json`, so there is no `locales/zh/entries.json`.
- When adding a project or rewording its purpose, boundary or license verdict, complete the en/es/hi/fr locales in the same pull request, otherwise `python scripts/build.py --check` and `python -m unittest discover -s tests -v` fail.
- Static documents: English lives at the repository root `docs/` and `CONTRIBUTING.md`; other languages use the same relative paths under `locales/<lang>/`. Relative links inside a mirror resolve from the directory of that file, so links from `locales/<lang>/docs/` to the repository root (`data/`, `scripts/`, `research/`, `LICENSE`, `record/`) are written as `../../../`, and from `locales/<lang>/CONTRIBUTING.md` as `../../`; `docs/readme-intro.md` is an exception — it is embedded into the README and resolves from the locale root.
- `record/` and `research/` keep their original wording as an audit trail and are not machine-translated.
- Generated files (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` and the same-named files in each language mirror) are never edited by hand; they come from `python scripts/build.py`.
