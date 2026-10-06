#!/usr/bin/env python3
"""Serve this static site locally with the same clean URL aliases as Vercel."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {
    "/about": "/about.html",
    "/contact": "/contact.html",
    "/privacy": "/privacy.html",
    "/terms": "/terms.html",
    "/disclaimer": "/disclaimer.html",
    "/play": "/play.html",
    "/updates": "/updates.html",
    "/guides": "/guides/index.html",
    "/tools/merge-planner": "/tools/merge-planner.html",
}
for path in (ROOT / "guides").glob("*.html"):
    ALIASES[f"/guides/{path.stem}"] = f"/guides/{path.name}"

class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        parsed = urlsplit(path)
        clean = unquote(parsed.path)
        if clean == "/zh": clean = "/zh/"
        if clean == "/es": clean = "/es/"
        if clean in ALIASES:
            clean = ALIASES[clean]
        return super().translate_path(clean)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), PreviewHandler)
    print(f"Serving {ROOT} at http://127.0.0.1:{args.port}")
    server.serve_forever()
