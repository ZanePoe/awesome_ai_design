# Guide de contribution

Les contributions d'agents de design, de Skills pour agents, d'éditeurs de design ou de benchmarks de recherche sont bienvenues. Merci de fournir le dépôt GitHub canonique, l'usage principal, le périmètre d'application, ainsi que des liens vers les preuves fonctionnelles et les textes de licence. Un projet réduit à un service hébergé n'entre pas dans le noyau ; la documentation, les formats et les index de référence doivent indiquer clairement leur nature.

Modifiez `data/projects.json`, en conservant les liens vers des commits figés du README ou de la documentation officielle ; vérifiez LICENSE, NOTICE et les conditions distinctes des données, polices et ressources. N'éditez pas directement les README ou classements générés. Pour un nouvel élément, laissez `baseline` à `false` ; les quatre éléments initiaux de la première version restent inchangés.

En local, Python 3.12+ et un GitHub CLI authentifié (ou `GH_TOKEN` configuré) sont nécessaires.

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

## Fichiers multilingues

- `data/projects.json` porte les données d'audit canoniques en chinois : les faits ne se corrigent qu'au seul endroit ici.
- Dans les autres langues, les textes proviennent de `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`) et de `locales/<lang>/ui.json` ; `zh` retombe directement sur `data/projects.json`, donc il n'existe pas de `locales/zh/entries.json`.
- Quand vous ajoutez un projet ou réécrivez un positionnement, une limite ou une conclusion de licence, complétez les quatre locales en/es/hi/fr dans la même PR, sinon `python scripts/build.py --check` et `python -m unittest discover -s tests -v` échoueront.
- Documents statiques : l'anglais est à la racine (`docs/` et `CONTRIBUTING.md`), les autres langues sous `locales/<lang>/` aux mêmes chemins relatifs. Dans une copie miroir, les liens relatifs se résolvent depuis le répertoire du fichier ; ceux pointant vers la racine du dépôt (`data/`, `scripts/`, `research/`, `LICENSE`, `record/`) s'écrivent avec `../../`. Exception : `docs/readme-intro.md`, intégré au README et résolu depuis la racine de la langue.
- `record/` et `research/` conservent le texte d'origine tel qu'il a été rédigé, comme piste d'audit ; pas de traduction automatique.
- Les artefacts générés (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` et leurs homologues dans les copies miroirs par langue) ne doivent jamais être modifiés à la main ; ils sont produits par `python scripts/build.py`.
