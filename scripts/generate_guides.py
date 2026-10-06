#!/usr/bin/env python3
"""Generate static guide pages from src/content/guides.json."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'src/content/guides.json').read_text(encoding='utf-8'))
by_slug = {item['slug']: item for item in DATA}
SEO_TITLES = {
    'getting-started': 'Getting Started: Piece of Cake Guide',
    'merge-basics': 'Merge Basics: Piece of Cake Guide',
    'customer-orders': 'Customer Orders: Piece of Cake Guide',
    'cafe-restoration': 'Cafe Restoration: Piece of Cake Guide',
    'boosters-and-missions': 'Boosters: Piece of Cake Guide',
    'board-space': 'Board Space Tips: Piece of Cake Guide',
    'browser-controls': 'Browser Controls: Piece of Cake Guide',
}

def related_links(slugs):
    return '\n'.join(
        f'<li><a href="/guides/{html.escape(slug)}">{html.escape(by_slug[slug]["title"])}</a></li>'
        for slug in slugs if slug in by_slug
    )

for item in DATA:
    title = html.escape(item['title'])
    seo_title = html.escape(SEO_TITLES.get(item['slug'], item['title']))
    description = html.escape(item['description'])
    slug = html.escape(item['slug'])
    body = item['body']
    intro = item['intro']
    figure = ''
    if item.get('image'):
        figure = f'''<figure class="source-figure"><img src="{html.escape(item['image'])}" alt="{html.escape(item['image_alt'])}" loading="lazy" width="1280" height="675"><figcaption>Reference capture made during the 6 October 2026 review of the CrazyGames-hosted build. The game artwork belongs to its respective rights holders; this site uses the image to explain the public opening scene.</figcaption></figure>'''
    page = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-GRDHEDT25W"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-GRDHEDT25W');</script>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{seo_title} | piece-of-cake.online</title>
    <meta name="description" content="{description}" />
    <meta name="robots" content="index, follow" />
    <link rel="canonical" href="https://piece-of-cake.online/guides/{slug}" />
    <link rel="icon" href="/favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" href="/styles.css" />
    <script type="application/ld+json">{{
      "@context":"https://schema.org",
      "@type":"Article",
      "headline":{json.dumps(item['title'])},
      "description":{json.dumps(item['description'])},
      "url":"https://piece-of-cake.online/guides/{slug}",
      "dateModified":"2026-10-06",
      "author":{{"@type":"Organization","name":"Piece Of Cake Online Fan Guide","email":"bigdata20182023@gmail.com"}},
      "inLanguage":"en",
      "isPartOf":{{"@type":"WebSite","name":"Piece Of Cake Online Fan Guide","url":"https://piece-of-cake.online/"}},
      "about":{{"@type":"VideoGame","name":"Piece of Cake: Merge and Bake"}}
    }}</script>
  </head>
  <body>
    <header class="site-header">
      <div class="branding"><a class="brand-pill" href="/">🍰 Piece Of Cake Fan Guide</a><p class="tagline">Independent, source-backed game notes.</p></div>
      <nav class="language-toggle" aria-label="Language selector"><a class="lang-link is-active" href="/">English</a><a class="lang-link" href="/zh/">中文</a><a class="lang-link" href="/es/">Español</a></nav>
    </header>
    <main>
      <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><span aria-current="page">{title}</span></li></ol></nav>
      <article class="guide" aria-label="{title}">
        <p class="eyebrow">Independent guide</p>
        <h1>{title}</h1>
        <p class="guide-meta">Reviewed 6 October 2026 · Maintained by Piece Of Cake Online Fan Guide · <a href="mailto:bigdata20182023@gmail.com">Contact the maintainer</a></p>
        <p class="lead">{html.escape(intro)}</p>
        <div class="source-note"><strong>Source boundary:</strong> This guide uses the public <a href="https://www.crazygames.com/game/piece-of-cake-merge-and-bake" rel="noopener noreferrer nofollow">CrazyGames listing</a> for published facts. It does not claim hidden levels, fixed recipe values, offline progress, or features that the source does not confirm.</div>
{figure}
        {body}
        <section aria-labelledby="related-title">
          <h2 id="related-title">Continue with a related guide</h2>
          <ul class="related-links">{related_links(item['related'])}</ul>
        </section>
        <p class="source-note">Found an inaccurate statement? <a href="/contact">Contact the site owner</a> with the page URL and the correction.</p>
      </article>
    </main>
    <footer class="site-footer"><p>© <span id="year"></span> Piece Of Cake Online Fan Guide.</p><nav class="footer-links" aria-label="Footer links"><a href="/about">About</a><a href="/contact">Contact</a><a href="/privacy">Privacy</a><a href="/terms">Terms</a><a href="/disclaimer">Disclaimer</a></nav></footer>
    <script>document.getElementById('year').textContent = new Date().getFullYear();</script>
  </body>
</html>
'''
    out = ROOT / 'guides' / f'{item["slug"]}.html'
    out.write_text(page, encoding='utf-8')
    print(out.relative_to(ROOT))
