# Guía de contribución

Se aceptan de buen grado agentes de diseño, Agent Skills, editores de diseño o benchmarks de investigación. Aporta el repositorio canonical de GitHub, el uso principal, la frontera de aplicación y los enlaces de evidencia del README y de la licencia en un commit fijo. Los proyectos con solo un servicio gestionado no entran en el núcleo; la documentación, los formatos y los índices de referencia deben etiquetarse claramente según su forma.

Edita `data/projects.json` y conserva los enlaces a commits fijos del README o de la documentación oficial; revisa LICENSE, NOTICE y las condiciones independientes de datos, fuentes y materiales. No edites a mano el README ni las tablas generadas. En las entradas nuevas `baseline` debe seguir siendo `false`; los cuatro proyectos semilla de la primera versión permanecen sin cambios.

En local se necesitan Python 3.12+ y la GitHub CLI autenticada (o `GH_TOKEN` configurado).

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

## Archivos multilingües

- `data/projects.json` guarda los datos revisados canónicos en chino: un hecho se corrige una sola vez ahí.
- Los textos de los demás idiomas proceden de `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`) y de `locales/<lang>/ui.json`; `zh` recurre directamente a `data/projects.json`, así que no existe `locales/zh/entries.json`.
- Al añadir un proyecto o reformular su propósito, su frontera o su veredicto de licencia, completa en la misma pull request los cuatro idiomas en, es, hi y fr; si no, fallarán `python scripts/build.py --check` y `python -m unittest discover -s tests -v`.
- La prosa estática: el inglés vive en `docs/` y `CONTRIBUTING.md` de la raíz; los demás idiomas usan las mismas rutas relativas bajo `locales/<lang>/`. Los enlaces relativos de un espejo se resuelven desde el directorio del propio archivo; los que apuntan a la raíz del repositorio —`data/`, `scripts/`, `research/`, `LICENSE`, `record/`— deben escribirse como `../../` desde `locales/<lang>/CONTRIBUTING.md` y como `../../../` desde `locales/<lang>/docs/`; `docs/readme-intro.md` es la excepción porque se inserta en el README y se resuelve desde la raíz del idioma.
- `record/` y `research/` conservan el texto original con el que fueron escritos, como rastro de auditoría; no se traducen automáticamente.
- Los archivos generados (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` y sus espejos en cada idioma) no se editan a mano: los produce `python scripts/build.py`.
