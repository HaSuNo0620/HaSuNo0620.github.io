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

## Content

Notes live in `src/data/notes/` and are loaded through Astro Content Collections.

Each note has a status:

- `seed`: fragment / memo
- `growing`: still developing
- `evergreen`: reasonably stable

## Figure style

Figures follow the site-wide **Figure Style v1.1** in [`docs/figure-style.md`](docs/figure-style.md).
Matplotlib helpers and semantic defaults live in [`scripts/figure_style.py`](scripts/figure_style.py).

GitHub Pages deployment is handled by `.github/workflows/deploy.yml`.
