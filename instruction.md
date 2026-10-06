# Piece Of Cake Online Fan Guide Brief

## Purpose

Build an independent, source-backed fan guide for *Piece of Cake: Merge and Bake* at `https://piece-of-cake.online/`. The site must clearly state that it is not affiliated with HG POINT LTD or CrazyGames.

## Game embed and source

- Embed the CrazyGames-hosted game: `https://games.crazygames.com/en_US/piece-of-cake-merge-and-bake/index.html?isNewUser=false`
- Credit the referenced YouTube walkthrough and link to its original page.
- Use the public CrazyGames listing as the source for developer, platform, controls, and published gameplay facts.
- Separate verified facts from independent strategy observations. Never invent mechanics, events, currencies, or account features.

## Languages

Publish English, Simplified Chinese, and Spanish pages only when each translation has useful, readable content. Each page needs its own canonical URL, language metadata, and reciprocal hreflang links.

## Editorial and trust requirements

- Write for players first; do not target a fixed keyword density or word count.
- Use original explanations, practical tables/checklists, source links, clear dates, and correction contact information.
- Add visible About, Contact, Privacy, Terms, and Disclaimer pages.
- Do not imply that the site, game embed, or video is official.
- Use descriptive image alt text and only publish assets that exist at the referenced URL.

## Technical requirements

- Serve valid `robots.txt`, `sitemap.xml`, `ads.txt`, and `404.html` files.
- Unknown paths and missing assets must return a real 404 response at the deployment host; they must not silently return the homepage.
- Keep GA4 tracking limited to the configured property and document the analytics/privacy behavior.
- Test mobile layout, iframe loading, internal links, canonical URLs, structured data, and Search Console URL inspection before deployment.

## 扩展内容与工具

- English guide pages live under `guides/` and are generated from `src/content/guides.json` with `python3 scripts/generate_guides.py`.
- The homepage links to source-backed guides for getting started, merge basics, customer orders, cafe restoration, boosters and missions, board space, and browser controls.
- `tools/merge-planner.html` is a browser-only checklist. It stores the user's notes in local storage and does not send them to a server.
- `/play` is a noindex page for the third-party game and walkthrough embeds; the homepage prioritizes independent editorial content.
- Chinese and Spanish landing pages remain available but are `noindex` until they receive a full human-reviewed expansion.
