# HaSuNo0620.github.io

Personal digital garden built with Astro.

## Local development

```bash
npm install
npm run dev
```

Production build:

```bash
npm run build
```

## Study app

`/study/` contains a static, case-based qualification study application. The first content pack covers 危険物取扱者 乙4「性質・火災予防・消火」. Story content and the curriculum graph live under `src/study-content/`; the reusable engines and React UI live under `src/study/`.

Useful commands:

```bash
npm run dev
npm test
npm run validate:study
npm run check:study
npm run build
```

`npm run validate:study` checks story graph integrity, knowledge references, provenance, and curriculum coverage before deployment. `npm run check:study` combines content validation, Vitest, and `astro check`.

Normal learning history is stored only in the current browser's IndexedDB. There is no account or cross-device sync in the initial version, and clearing site data resets normal progress. If a future/incompatible local database schema is detected, the app leaves that database untouched and offers an emergency JSON export of the recognized data.

## Content

Notes live in `src/data/notes/` and are loaded through Astro Content Collections.

Each note has a status:

- `seed`: fragment / memo
- `growing`: still developing
- `evergreen`: reasonably stable

## Writing and figure style

Figures follow the site-wide **Figure Style v1.3** in [`docs/figure-style.md`](docs/figure-style.md).
Matplotlib helpers and semantic defaults live in [`scripts/figure_style.py`](scripts/figure_style.py).

Inline/display math usage follows **Math Style v1.1** in [`docs/math-style.md`](docs/math-style.md). Markdown math is parsed with `remark-math` before being handed to MathJax so multiline TeX environments such as matrices are preserved.

GitHub Pages deployment is handled by `.github/workflows/deploy.yml`.
