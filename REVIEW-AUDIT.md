# Three-pass quality audit before deployment

Date: 7 October 2026 (Asia/Shanghai)

This log records the required review passes. The final push is made only after all three passes have passed locally and the deployment smoke checks are green.

## Pass 1 — navigation, routes, and player UX

Findings:

- Legal and guide pages had no obvious route back to Home.
- `/guides/` was missing even though the site needed a guide-library destination.
- The homepage Play action sent users to a separate page and the inline player was too far down the page.
- Guide cards accidentally pointed “Getting started” to the library route.
- Mobile sticky navigation needed a larger anchor offset.

Fixes:

- Added a shared sticky navigation with Home, Guides, Planner, Play, Updates, and language links.
- Made every brand pill link to `/`.
- Added `/guides` and corrected all related-guide links.
- Moved the game iframe directly after the homepage hero and source notice.
- Added a responsive player section and full-screen fallback.
- Added mobile scroll-margin for sticky navigation anchors and styled secondary source links.

Evidence:

- Local clean-route crawler: `/`, `/guides`, all guide pages, `/about`, `/contact`, `/privacy`, `/tools/merge-planner`, `/play`, `/updates` returned 200; random paths returned 404.
- Browser test: clicking Home from `/about` returned `/`; the homepage contained one playable game iframe.
- Mobile browser screenshot showed the shared navigation wrapping without overflow.

## Pass 2 — content quality, search intent, and trust

Findings:

- The root title was generic for a page that now supports direct play.
- Repeated guide boilerplate and vague hypothetical wording weakened the source-backed value.
- The homepage video notice still described the page as if it did not contain a player.
- Guide pages needed distinct, user-facing verification prompts.

Fixes:

- Updated the homepage title and description around “Play + Guide” intent while keeping the exact game name.
- Added a real `/guides` collection page and kept each guide mapped to a distinct question.
- Added page-specific Player checklist prompts instead of one identical maintenance sentence.
- Replaced the beginner hypothetical chain with the currently published CrazyGames sequence: toast pan → toast pair → toast with sunny-side-up egg, followed by named later food items.
- Kept unsupported costs, timers, offline progress, and hidden recipe trees explicitly unclaimed.
- Preserved the source capture, source links, maintainer email, disclaimer, and updates log.

Evidence:

- All 20 HTML pages parsed successfully with title, canonical, one H1, and valid JSON-LD where present.
- All guide pages regenerated deterministically from `src/content/guides.json`.
- Sitemap XML parsed successfully and contains only intended indexable routes.

## Pass 3 — privacy, consent, mobile, and deployment readiness

Findings:

- GA4 loaded before a privacy choice on pages that use analytics.
- A consent banner could appear on pages that do not load analytics.
- The privacy page described a future CMP but did not describe the current site-level analytics choice.
- The third-party frame needed a visible fallback and a clear source boundary.

Fixes:

- Added default-denied Google Consent Mode values before GA4 configuration.
- Added `site-consent.js` with Allow Analytics / Use Necessary Only choices stored locally.
- Gated the banner so pages without GA4 do not show an irrelevant prompt.
- Updated the privacy page to distinguish the current analytics preference from the future Google-certified CMP required before serving ads.
- Kept `ads.txt` comment-only and did not add a guessed publisher ID.
- Kept the third-party iframe lazy-loaded, attributed, and paired with a full-screen fallback.

Evidence:

- `node --check site-consent.js` passed.
- Browser test showed the consent banner, stored `denied`, removed the banner, and showed no banner on `/about`.
- Local route, HTML, JSON-LD, sitemap, canonical, and 404 checks passed.
- External smoke checks confirmed the live site returns 200 for indexable routes and 404 for an unknown route.

## Approval boundary

These passes improve readiness but cannot guarantee AdSense approval. Before adding ad code, replace the site-level preference with a Google-certified CMP where required, add the exact authorized seller line supplied by AdSense, and add additional dated first-hand gameplay observations and screenshots when available. The current site does not claim that those user-specific observations exist.
