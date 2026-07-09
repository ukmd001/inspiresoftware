# Inspire Arts Software — storefront website

A self-contained marketing website that advertises **Inspire Arts Software** and gives every
app its own promo page, all styled to match the Wave Studio Plus ("Audio editor") look:
space-navy background, blue→purple→cyan gradient headings, star-field canvas and animated
hero graphics.

Everything needed to view or host the site is in this one folder.

## View it

- **Quick look:** double-click `index.html` (works straight from `file://`).
- **Proper local server** (recommended — relative links behave exactly as when hosted):
  double-click `serve.bat`, then open http://localhost:8750

## How it's built

The site is generated from data + templates so all 29 pages stay pixel-identical in style:

```
data/apps.py        ← the catalogue (one dict per app: name, tagline, features, specs, …)
data/extras.py      ← per-app screenshot archetype + caption, requirements tier, overrides
templates/          ← index.html.tmpl + app.html.tmpl (HTML shells with {{tokens}})
screenshots.py      ← generates a themed SVG "screenshot" mockup per app
assets/css/site.css ← shared style; each app sets its own accent via CSS variables
assets/js/site.js   ← shared canvas animations (starfield + 5 reusable hero animations)
assets/shots/       ← generated SVG mockups (one per app) — used on cards + app pages
assets/img/         ← real screenshots (e.g. the two genuine Wave Studio Plus captures)
build.py            ← reads the above and writes index.html + apps/<slug>.html
```

## Screenshots

Every app shows screenshots — on its page (a gallery) and as a banner on its storefront card.
By default these are **generated, on-brand SVG mockups** (`assets/shots/<slug>.svg`), drawn in
each app's accent colours by `screenshots.py` — they are *representations*, not live captures.

To use a **real screenshot** instead, drop the image into `assets/img/` and add a `real_shots`
entry for that app in `data/extras.py`:

```python
"my-app": { ..., "real_shots": [("img/my-app-1.png", "Caption for the shot.")] },
```

Real shots appear first on the app page; the generated mockup follows. (Wave Studio Plus already
uses its two genuine captures this way.)

## System requirements

Each app page has a detailed **Minimum / Recommended** requirements block (or **Server / Client**
for the self-hosted web platforms). These come from a *tier* per app set in `data/extras.py`
(`light` / `media` / `gpu3d` / `web` / `android`), with the base lists defined in `REQ_TIERS` in
`build.py`. Per-app tweaks use `min_extra`, `rec_extra` and `req_note` in `data/extras.py`
(e.g. "requires FFmpeg", "run as Administrator", "needs an API key").

### Regenerate after editing content

Edit `data/apps.py` (or the templates/CSS/JS), then:

```
python build.py
```

This rewrites `index.html` and every `apps/*.html`. No third-party packages required.

### Add a new app

Append a new dict to `APPS` in `data/apps.py` (copy an existing one as a template), set its
`category` to one of the entries in `CATEGORIES`, then run `python build.py`.

## Distribute / host it

The whole folder is static HTML/CSS/JS — drop it on any static host:

- **GitHub Pages / Netlify / Cloudflare Pages:** push the folder; serve `index.html` as root.
- **Your own server (nginx/Apache):** point the web root at this folder.
- **Inspire Arts home server:** copy into the Nginx static root.

You do **not** need Python on the server — `build.py` only runs locally when you change content.

### Wiring up real downloads

Every "Download" button currently points to a `#` placeholder (same as the live Wave site).
To make them real, edit the `"download"` link target in two places per app:

1. In `build.py`, `render_cta()` — the `href="#"` on the primary download button.
2. (Optional) add a `"download_url"` field per app in `data/apps.py` and use it in
   `render_cta()` instead of the hard-coded `#`.

Your packaged installers already live in `C:\Users\Inspi\OneDrive\Desktop\RELEASE\` — either
upload those to a host and point the links at the URLs, or copy the relevant `*_Setup.exe` /
`*.apk` files into an `assets/downloads/` folder here and link to them relatively.

### Optional screenshots

Drop images into `assets/img/` and reference them from `data/apps.py` (you can extend the app
template with an image section the same way the features grid is built).

## Notes

- The Wave Studio Plus page in this catalogue is a fresh, on-brand summary. The original,
  fuller Wave promo site remains at `C:\Users\Inspi\wavestudioplus\website\index.html`.
- Excluded from the catalogue: Home Cloud Server (still in planning) and the abandoned SpotUE5
  prototype (superseded by Spot vUE).

© 2026 Inspire Arts. All rights reserved.
