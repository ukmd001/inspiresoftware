# -*- coding: utf-8 -*-
"""
Inspire Arts Software — static site generator.

Reads data/apps.py + templates/*.tmpl and writes:
  index.html          the storefront
  apps/<slug>.html    one full promo page per app

Run:  python build.py
No third-party dependencies.
"""
import os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "data"))
sys.path.insert(0, HERE)
import apps as catalogue  # noqa: E402
import extras as extras_mod  # noqa: E402
import screenshots  # noqa: E402

EXTRA = extras_mod.EXTRA
YEAR = datetime.date.today().year
TEMPL = os.path.join(HERE, "templates")
APPS_DIR = os.path.join(HERE, "apps")
SHOTS_DIR = os.path.join(HERE, "assets", "shots")


# ----------------------------------------------------------- requirement tiers
def _li(items):
    return "".join("<li>%s</li>" % x for x in items)


# Each tier: ("Card A title", icon, [lines]), ("Card B title", icon, [lines])
REQ_TIERS = {
 "light": (
   ("💻", "Minimum", [
     "<strong>OS:</strong> Windows 10 (64-bit) or Windows 11",
     "<strong>CPU:</strong> Dual-core, 2.0 GHz",
     "<strong>Memory:</strong> 4 GB RAM",
     "<strong>Graphics:</strong> Any DirectX 11 / integrated GPU",
     "<strong>Storage:</strong> 250 MB + space for your files",
     "<strong>Display:</strong> 1280×768 or higher",
   ]),
   ("🚀", "Recommended", [
     "<strong>OS:</strong> Windows 11 (64-bit)",
     "<strong>CPU:</strong> Quad-core, 3.0 GHz",
     "<strong>Memory:</strong> 8 GB RAM",
     "<strong>Graphics:</strong> Dedicated GPU (optional)",
     "<strong>Storage:</strong> SSD with a few GB free",
     "<strong>Display:</strong> 1920×1080 or higher",
   ]),
 ),
 "media": (
   ("💻", "Minimum", [
     "<strong>OS:</strong> Windows 10 (64-bit) or Windows 11",
     "<strong>CPU:</strong> Quad-core, 2.5 GHz",
     "<strong>Memory:</strong> 8 GB RAM",
     "<strong>Graphics:</strong> OpenGL 3.3 / DirectX 11 GPU",
     "<strong>Storage:</strong> 500 MB + space for media",
     "<strong>Display:</strong> 1366×768 or higher",
   ]),
   ("🚀", "Recommended", [
     "<strong>OS:</strong> Windows 11 (64-bit)",
     "<strong>CPU:</strong> 6-core, 3.5 GHz or better",
     "<strong>Memory:</strong> 16 GB RAM",
     "<strong>Graphics:</strong> Dedicated GPU for smooth real-time work",
     "<strong>Storage:</strong> NVMe SSD with several GB free",
     "<strong>Display:</strong> 1920×1080 or higher",
   ]),
 ),
 "gpu3d": (
   ("💻", "Minimum", [
     "<strong>OS:</strong> Windows 10 (64-bit) or Windows 11",
     "<strong>CPU:</strong> Quad-core, 3.0 GHz",
     "<strong>Memory:</strong> 8 GB RAM",
     "<strong>Graphics:</strong> Dedicated GPU, 2 GB VRAM (OpenGL 3.3 / DX11)",
     "<strong>Storage:</strong> 2 GB+ for the game and assets",
     "<strong>Display:</strong> 1280×720 or higher",
   ]),
   ("🚀", "Recommended", [
     "<strong>OS:</strong> Windows 11 (64-bit)",
     "<strong>CPU:</strong> 6–8 core, 3.5 GHz or better",
     "<strong>Memory:</strong> 16 GB RAM",
     "<strong>Graphics:</strong> GTX 1660 / RX 580 or better, 6 GB+ VRAM",
     "<strong>Storage:</strong> NVMe SSD with several GB free",
     "<strong>Display:</strong> 1920×1080, 60 Hz+",
   ]),
 ),
 "web": (
   ("🖥️", "Server (self-host)", [
     "<strong>OS:</strong> Windows 10/11 or any modern Linux",
     "<strong>Runtime:</strong> Python 3.10+",
     "<strong>CPU:</strong> Dual-core (quad-core recommended)",
     "<strong>Memory:</strong> 2 GB RAM (4 GB+ recommended)",
     "<strong>Storage:</strong> Scales with your data / uploads",
     "<strong>Network:</strong> LAN access, or a port forward / reverse proxy for the internet",
   ]),
   ("🌐", "Client (any device)", [
     "<strong>Browser:</strong> Chrome, Edge, Firefox or Safari (current)",
     "<strong>Device:</strong> Any desktop, laptop, tablet or phone",
     "<strong>JavaScript:</strong> enabled",
     "<strong>Connection:</strong> same Wi-Fi as the server, or internet if exposed",
     "<strong>Account:</strong> created on first visit",
   ]),
 ),
 "android": (
   ("📱", "Minimum", [
     "<strong>OS:</strong> Android 8.0 (Oreo) or newer",
     "<strong>Memory:</strong> 3 GB RAM",
     "<strong>Storage:</strong> ~100 MB free",
     "<strong>Screen:</strong> Touchscreen, 720p or higher",
     "<strong>Install:</strong> allow install from APK (sideload)",
   ]),
   ("✨", "Recommended", [
     "<strong>OS:</strong> Android 12 or newer",
     "<strong>Memory:</strong> 6 GB RAM",
     "<strong>Device:</strong> Modern Samsung Galaxy (tested on the S20)",
     "<strong>Storage:</strong> 200 MB+ free",
     "<strong>Screen:</strong> 1080×2400 AMOLED or better",
   ]),
 ),
}


def load(name):
    with open(os.path.join(TEMPL, name), encoding="utf-8") as f:
        return f.read()


def fill(tmpl, mapping):
    for k, v in mapping.items():
        tmpl = tmpl.replace("{{%s}}" % k, v)
    return tmpl


def accent_style(app):
    a, b, c = app.get("accent", catalogue.HOUSE)
    return "--accent-a:%s;--accent-b:%s;--accent-c:%s" % (a, b, c)


# ----------------------------------------------------------------- app pages
def render_hero(app):
    badges = "".join('<span class="badge">%s</span>' % b for b in app.get("badges", []))
    return """
<header class="hero">
  <div class="eyebrow">{cat}</div>
  <h1>{icon} {name}</h1>
  <p class="tagline">{intro}</p>
  <canvas id="heroCanvas" data-anim="{anim}"></canvas>
  <div class="badges">{badges}</div>
  <div class="btns">
    <a class="btn btn-primary" href="#download">⬇ Download {name}</a>
    <a class="btn btn-ghost" href="#features">See Features</a>
  </div>
</header>
""".format(cat=app["category"], icon=app["icon"], name=app["name"],
           intro=app["intro"], anim=app.get("anim", "waveform"), badges=badges)


def render_features(app):
    cards = "".join(
        '<div class="card"><div class="icon">{i}</div><h3>{t}</h3><p>{b}</p></div>'.format(
            i=i, t=t, b=b) for (i, t, b) in app["features"])
    return """
<section id="features">
  <div class="section-label">What It Does</div>
  <h2>Everything {name} brings to the table.</h2>
  <div class="grid">{cards}</div>
</section>
""".format(name=app["name"], cards=cards)


def render_deep(app):
    rows = app.get("deep")
    if not rows:
        return ""
    out = ['<section id="deep">']
    for r in rows:
        bullets = "".join("<li>%s</li>" % x for x in r.get("bullets", []))
        ul = "<ul>%s</ul>" % bullets if bullets else ""
        out.append("""
  <div class="feature-row">
    <div>
      <h3>{title}</h3>
      <p>{body}</p>
      {ul}
    </div>
    <div class="feat-visual"><canvas data-anim="{anim}"></canvas></div>
  </div>""".format(title=r["title"], body=r["body"], ul=ul, anim=r.get("anim", "spectrum")))
    out.append("</section>")
    return "".join(out)


def shot_path(app):
    return os.path.join(SHOTS_DIR, app["slug"] + ".svg")


def generate_shot(app):
    ex = EXTRA.get(app["slug"], {})
    shot = ex.get("shot", {"kind": "gallery", "caption": "", "labels": {}})
    svg = screenshots.render(shot.get("kind", "gallery"), app["name"],
                             app.get("accent", catalogue.HOUSE), shot.get("labels", {}))
    with open(shot_path(app), "w", encoding="utf-8") as f:
        f.write(svg)


def render_shots(app, prefix):
    """prefix: '' for storefront-rooted, '../' for app pages."""
    ex = EXTRA.get(app["slug"], {})
    figs = []
    for img, cap in ex.get("real_shots", []):
        figs.append('<figure class="shot"><img src="{p}assets/{src}" alt="{name} screenshot">'
                    '<figcaption>{cap}</figcaption></figure>'.format(
                        p=prefix, src=img, name=app["name"], cap=cap))
    shot = ex.get("shot", {})
    cap = shot.get("caption", "A look at %s in action." % app["name"])
    figs.append('<figure class="shot"><img src="{p}assets/shots/{slug}.svg" alt="{name} interface">'
                '<figcaption>{cap}</figcaption></figure>'.format(
                    p=prefix, slug=app["slug"], name=app["name"], cap=cap))
    return """
<section id="screenshots">
  <div class="section-label">See It In Action</div>
  <h2>A look inside {name}.</h2>
  <div class="shot-grid">{figs}</div>
</section>
""".format(name=app["name"], figs="".join(figs))


def render_requirements(app):
    ex = EXTRA.get(app["slug"], {})
    tier = ex.get("tier", "light")
    (ia, ta, la), (ib, tb, lb) = REQ_TIERS[tier]
    la = list(la) + ex.get("min_extra", [])
    lb = list(lb) + ex.get("rec_extra", [])
    note = '<p class="req-note">%s</p>' % ex["req_note"] if ex.get("req_note") else ""
    return """
<section id="requirements">
  <div class="section-label">Get Ready</div>
  <h2>System requirements.</h2>
  <div class="req-grid">
    <div class="req-card"><div class="icon">{ia}</div><h3>{ta}</h3><ul class="req-list">{la}</ul></div>
    <div class="req-card req-recommended"><div class="icon">{ib}</div><h3>{tb}</h3><ul class="req-list">{lb}</ul></div>
  </div>
  {note}
</section>
""".format(ia=ia, ta=ta, la=_li(la), ib=ib, tb=tb, lb=_li(lb), note=note)


def render_specs(app):
    rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (k, v) for (k, v) in app["specs"])
    req = ""
    if app.get("requirements"):
        req = '<p class="lede" style="margin-top:36px">%s</p>' % app["requirements"]
    return """
<section id="specs">
  <div class="section-label">Under the Hood</div>
  <h2>The details.</h2>
  <table class="spec">{rows}</table>
  {req}
</section>
""".format(rows=rows, req=req)


def render_cta(app):
    return """
<div class="cta-band" id="download">
  <h2>Get {name}.</h2>
  <p>{tagline}</p>
  <a class="btn btn-primary" href="#">⬇ Download {name}</a>
  <p style="margin-top:18px;font-size:.85rem;color:var(--text-dim)">{note}</p>
</div>
""".format(name=app["name"], tagline=app["tagline"], note=app.get("download", "free"))


def render_app(app):
    content = (render_hero(app) + "<main>" + render_shots(app, "../") +
               render_features(app) + render_deep(app) +
               render_requirements(app) + render_specs(app) +
               render_cta(app) + "</main>")
    page = fill(load("app.html.tmpl"), {
        "TITLE": "%s — Inspire Arts Software" % app["name"],
        "DESC": app["tagline"],
        "ACCENT_STYLE": accent_style(app),
        "APPNAME": app["name"],
        "FOOTLINE": app.get("footline", "made by Inspire Arts."),
        "CONTENT": content,
        "YEAR": str(YEAR),
    })
    return page


# ----------------------------------------------------------------- storefront
def render_storefront():
    apps = catalogue.APPS
    by_cat = {}
    for a in apps:
        by_cat.setdefault(a["category"], []).append(a)

    hero = """
<header class="hero">
  <div class="eyebrow">Independent Software Studio</div>
  <h1>INSPIRE ARTS SOFTWARE</h1>
  <p class="tagline">A whole catalogue of desktop, web, mobile and game software —
  <strong>designed and built in-house</strong>, each one obsessed over down to the last
  animated pixel. One studio. {n} apps. No subscriptions.</p>
  <canvas id="heroCanvas" data-anim="orbit"></canvas>
  <div class="btns">
    <a class="btn btn-primary" href="#catalogue">⬇ Browse the Catalogue</a>
    <a class="btn btn-ghost" href="#about">About the Studio</a>
  </div>
  <div class="stat-strip">
    <div class="stat"><div class="n">{n}</div><div class="l">Apps</div></div>
    <div class="stat"><div class="n">{c}</div><div class="l">Categories</div></div>
    <div class="stat"><div class="n">3</div><div class="l">Platforms</div></div>
    <div class="stat"><div class="n">£0</div><div class="l">Subscriptions</div></div>
  </div>
</header>
""".format(n=len(apps), c=len(catalogue.CATEGORIES))

    sections = ['<main>', '<section id="catalogue">',
                '<div class="section-label">The Catalogue</div>',
                '<h2>Pick your tool.</h2>',
                '<p class="lede">Everything we\'ve built, grouped by what it\'s for — from a '
                'full multi-track DAW to a phone-based weighing scale. Tap any card for the '
                'full story.</p>']

    for cat, blurb in catalogue.CATEGORIES:
        items = by_cat.get(cat, [])
        if not items:
            continue
        sections.append(
            '<div class="cat-head"><div class="section-label">%s</div>'
            '<span class="count">%d apps · %s</span></div>' % (cat, len(items), blurb))
        sections.append('<div class="app-grid">')
        for a in items:
            sections.append(
                '<a class="app-card" href="apps/{slug}.html" style="{style}">'
                '<div class="banner"><img loading="lazy" src="assets/shots/{slug}.svg" alt="{name} preview"></div>'
                '<div class="top"><span class="ico">{icon}</span><h3>{name}</h3></div>'
                '<p>{tag}</p>'
                '<div class="foot"><span class="plat">{plat}</span>'
                '<span class="view">View</span></div></a>'.format(
                    slug=a["slug"], style=accent_style(a), icon=a["icon"],
                    name=a["name"], tag=a["tagline"], plat=a["platform"]))
        sections.append('</div>')

    sections.append('</section>')
    sections.append("""
<section id="about">
  <div class="section-label">The Studio</div>
  <h2>One studio, obsessively hands-on.</h2>
  <p class="lede">Inspire Arts Software is the software arm of <strong>Inspire Arts</strong>.
  Every title here was designed, built and tested in-house — Windows desktop apps, self-hosted
  web platforms, native Android apps and full 3D games. We don't licence templates or wrap
  someone else's engine and call it ours; we sweat the audio buffers, the shaders, the
  animated backgrounds and the tiny interactions. The result is a family of software that
  looks and feels like it came from one place — because it did.</p>
  <div class="formats">
    <span class="fmt">WINDOWS</span>
    <span class="fmt">ANDROID</span>
    <span class="fmt">SELF-HOSTED WEB</span>
    <span class="fmt">3D GAMES</span>
    <span class="fmt">NO SUBSCRIPTIONS</span>
  </div>
</section>
</main>
""")

    content = hero + "".join(sections)
    return fill(load("index.html.tmpl"), {
        "TITLE": "Inspire Arts Software — Independent Apps, Games & Platforms",
        "DESC": "The full catalogue of Inspire Arts Software: desktop apps, self-hosted web "
                "platforms, native Android apps and 3D games — all built in-house.",
        "CONTENT": content,
        "YEAR": str(YEAR),
    })


# ------------------------------------------------------------- privacy policy
CONTACT_EMAIL = "ukmd001@gmail.com"


def render_privacy():
    updated = datetime.date.today().strftime("%d %B %Y")

    def sec(label, title, *paras):
        body = "".join('<p class="req-note">%s</p>' % p for p in paras)
        return ('<section><div class="section-label">%s</div><h2>%s</h2>%s</section>'
                % (label, title, body))

    # Per-app data-handling summary (grouped by behaviour, not one row per app)
    data_rows = [
        ("Runs fully on your device — no data collected",
         "Matrix Clock, Digital Clock Screensaver, AR Trace, PicDraw Grid, PicDraw (PC), "
         "Skale, Pong, Virtual Pet, HEIC Viewer, JPEG Scanner, FBX Builder, Wave Studio Plus, "
         "StreamHub, Dog Tribute Video and the Spot! games only open files you choose and save "
         "output you ask for. Nothing is sent anywhere."),
        ("Camera or microphone (processed on-device)",
         "AR Trace and PicDraw Grid use the camera to show your reference photo; Hey Spot, "
         "Claude Listener, AudioViz and Capture use the microphone. The audio/video is used "
         "live on your device and is not uploaded — except where you use an AI feature (below)."),
        ("Photo &amp; file access (stays on your device)",
         "Media Scanner, ImageSorter, HEIC Viewer, JPEG Scanner and PicDraw read images you "
         "point them at and keep the results on your device. ImageBridge sends images over your "
         "own local Wi-Fi to your own paired PC — never to us."),
        ("Sends data to a third-party AI service (with your own key)",
         "Hey Spot and Hey Spot PC send your spoken request to Google Gemini; Media Scanner, "
         "ImageSorter and ClaudeFetch send the image or file you choose to Anthropic Claude. "
         "Only what is needed to answer that request is sent, using an API key you provide. "
         'See <a href="https://policies.google.com/privacy">Google&rsquo;s</a> and '
         '<a href="https://www.anthropic.com/legal/privacy">Anthropic&rsquo;s</a> privacy policies.'),
        ("Accounts &amp; content you post (self-hosted web apps)",
         "Hotspot, FREE COMS, GHOST and the Inspire Arts CRM are self-hosted — you (or whoever "
         "runs the server) hold the database. Any account details or content live on that server, "
         "under that operator&rsquo;s control, not with Inspire Arts."),
    ]
    rows_html = "".join("<tr><td>%s</td><td>%s</td></tr>" % (k, v) for (k, v) in data_rows)

    content = """
<header class="hero">
  <div class="eyebrow">Legal</div>
  <h1>Privacy Policy</h1>
  <p class="tagline">How Inspire Arts Software handles your data across every app,
  game and platform we make. <strong>Last updated %(updated)s.</strong></p>
</header>
<main>
%(short)s
%(who)s
<section>
  <div class="section-label">Per App</div>
  <h2>What each app accesses.</h2>
  <p class="req-note">Our apps fall into a few groups. This is what each group does with data.</p>
  <table class="spec">%(rows)s</table>
</section>
%(perms)s
%(children)s
%(ads)s
%(rights)s
%(changes)s
%(contact)s
</main>
""" % {
        "updated": updated,
        "rows": rows_html,
        "short": sec("The Short Version", "Most of our software collects nothing.",
                     "The large majority of Inspire Arts apps run entirely on your own device "
                     "or your own server. They do not create accounts, do not show ads, and do "
                     "not contain third-party analytics or tracking. Where an app does send data "
                     "out — only the AI-powered ones — it is limited to the request you make and "
                     "uses an API key you supply. The table below spells out exactly which apps "
                     "do what."),
        "who": sec("Who We Are", "The people behind the software.",
                   "Inspire Arts Software is the software arm of Inspire Arts, an independent "
                   "studio. For any privacy question, or to ask us to delete data an app of ours "
                   'holds, email <a href="mailto:%s">%s</a>.' % (CONTACT_EMAIL, CONTACT_EMAIL)),
        "perms": sec("Permissions", "Why an app might ask for access.",
                     "<strong>Camera</strong> — to display your live reference view (AR Trace, "
                     "PicDraw Grid). <strong>Microphone</strong> — for voice commands or audio "
                     "features (Hey Spot, Claude Listener, AudioViz, Capture). "
                     "<strong>Photos / storage</strong> — to open the images you pick and save "
                     "copies you ask for. You can decline any permission in your device settings; "
                     "the related feature simply won&rsquo;t be available."),
        "children": sec("Children", "Apps intended for children.",
                        "TalkTime is a speech-therapy app used by children under adult "
                        "supervision. It stores a child&rsquo;s name and exercise progress only "
                        "on the device, behind an adult PIN, and transmits nothing off the device. "
                        "It contains no ads, no in-app purchases and no third-party tracking."),
        "ads": sec("Ads &amp; Analytics", "None. Really.",
                   "We do not display advertising, we do not use third-party analytics or "
                   "tracking SDKs, and we do not sell or share personal data with anyone."),
        "rights": sec("Your Rights &amp; Data Retention", "You stay in control.",
                      "Because data our apps handle stays on your device or your server, "
                      "you can delete it at any time by clearing the app&rsquo;s data or removing "
                      "your files. Where the UK GDPR / EU GDPR applies, you have the right to "
                      "access, correct or erase personal data and to object to its processing; "
                      "contact us and we will help with anything within our control."),
        "changes": sec("Changes", "If this policy changes.",
                       "We may update this policy as our apps evolve. The &ldquo;last "
                       "updated&rdquo; date at the top always reflects the current version, and "
                       "material changes will be noted here."),
        "contact": sec("Contact", "Get in touch.",
                       'Questions about this policy or your data? Email '
                       '<a href="mailto:%s">%s</a> and we&rsquo;ll respond.'
                       % (CONTACT_EMAIL, CONTACT_EMAIL)),
    }

    return fill(load("index.html.tmpl"), {
        "TITLE": "Privacy Policy — Inspire Arts Software",
        "DESC": "How Inspire Arts Software handles your data across every app, game and platform.",
        "CONTENT": content,
        "YEAR": str(YEAR),
    })


def main():
    os.makedirs(APPS_DIR, exist_ok=True)
    os.makedirs(SHOTS_DIR, exist_ok=True)
    # screenshot mockups (one SVG per app)
    for app in catalogue.APPS:
        generate_shot(app)
    print("wrote %d screenshot mockups -> assets/shots/" % len(catalogue.APPS))
    # storefront
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_storefront())
    print("wrote index.html")
    # privacy policy (shared URL for every app store listing)
    with open(os.path.join(HERE, "privacy.html"), "w", encoding="utf-8") as f:
        f.write(render_privacy())
    print("wrote privacy.html")
    # app pages
    seen = set()
    for app in catalogue.APPS:
        slug = app["slug"]
        if slug in seen:
            raise SystemExit("duplicate slug: %s" % slug)
        seen.add(slug)
        with open(os.path.join(APPS_DIR, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(render_app(app))
    print("wrote %d app pages -> apps/" % len(catalogue.APPS))
    print("done: 1 storefront + %d app pages" % len(catalogue.APPS))


if __name__ == "__main__":
    main()
