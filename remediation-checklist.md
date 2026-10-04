# Remediation and deployment checklist

This branch rewrites the site for accuracy and trust. Complete these manual items before publishing:

1. Configure `hello@piece-of-cake.online` as a monitored mailbox, or replace it in `contact.html` with the real address.
2. Confirm the deployment host serves `404.html` with HTTP 404 for unknown paths. A static `404.html` file alone cannot override a host-wide homepage fallback.
3. Keep `ads.txt` comment-only until AdSense approves the site. Then replace the comments with the exact authorized-seller line from the AdSense account; never guess a publisher ID.
4. Submit `sitemap.xml` in Search Console after deployment and inspect `/`, `/privacy.html`, `/contact.html`, and `/404.html`.
5. Recheck GA4 and Search Console for at least 28 days. Treat third-party traffic estimates as directional.
6. Reapply to AdSense only after the pages are live, the contact address works, and the public game facts and source links have been reviewed.
7. Before adding any ad code, update `privacy.html` with the selected ad provider and the required consent behavior for the visitors you serve.
