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

GitHub Pages deployment is handled by `.github/workflows/deploy.yml`.
