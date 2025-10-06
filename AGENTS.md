# Repository Guidelines

## Project Structure & Module Organization
The repository targets a single-page marketing site that embeds the CrazyGames "Piece Of Cake" iframe and ships SEO content in English and Chinese. Keep `instruction.md` as the canonical product brief; sync with stakeholders before editing it. Place runtime assets in `src/`, keeping `src/index.html` as the entry point, `src/styles/` for modular CSS, `src/scripts/` for UI logic, and `src/content/` for localized article segments (Markdown or YAML). Generate crawl-facing files (`robots.txt`, `sitemap.xml`) into `public/`, and emit production bundles into `dist/`. Do not commit local preview caches or editor artefacts.

## Build, Test, and Development Commands
Install dependencies once a `package.json` is present with `npm install`. Use a Vite workflow: `npm run dev` starts the hot-reload dev server, `npm run build` packs the static site into `dist/`, and `npm run preview` validates the production build locally. For a lightweight static check, `npx serve dist` will host the compiled assets. Always verify the iframe, language toggles, and SEO meta tags before pushing.

## Coding Style & Naming Conventions
Write semantic HTML5 with 2-space indentation. Follow BEM-style CSS class names (`.section__title`) and keep filenames lowercase-kebab-case (`game-intro.en.md`, `game-intro.zh.md`). Use ES module syntax for JavaScript; prefer one feature per file to keep modules focused. Run `npm run lint` and `npm run format` before committing—configure Prettier and Stylelint accordingly if missing—so markup, CSS, and scripts stay consistent.

## Testing Guidelines
Add automated smoke tests with Playwright under `tests/e2e/` to confirm the iframe loads, the bilingual article renders, and SEO elements exist. Place any reusable helpers under `tests/unit/` and cover them with Vitest. Execute `npm run test` locally, and include `npm run test:e2e` in release checks. If a test is flaky, skip it temporarily with `test.skip` and open a tracking issue.

## Commit & Pull Request Guidelines
Adopt Conventional Commits (`feat: add zh SEO outline`) and reference issues in the footer (`Refs #12`). Pull requests must outline scope, list tests performed, and attach desktop + mobile screenshots of the hero section. Include Lighthouse scores when performance shifts. Keep PRs under roughly 400 changed lines; split larger efforts.

## SEO & Content Workflow
Maintain keyword density (≥3%) by editing the structured article outlines in `src/content/`. Update English and Chinese variants together and include publication dates in front matter so the sitemap stays current. When embedding new media, confirm it is lazy-loaded and captioned for both locales.
