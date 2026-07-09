# -*- coding: utf-8 -*-
"""
Inspire Arts Software — screenshot mockup generator.

Produces a themed SVG "screenshot" per app (window chrome + a representative
UI laid out in the app's accent colours). These are stylised representations —
drop real PNG captures into assets/img/ and reference them from data/extras.py
(real_shots) to override.

Each archetype function takes (a, b, c) accent hex strings and returns the inner
SVG body; frame() wraps it in a window. Public entry: render(kind, title, accent).
"""
import math

W, H = 760, 428


def frame(title, body, a, b, c):
    return (
f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
f'aria-label="{title} interface mockup" preserveAspectRatio="xMidYMid meet">'
'<defs>'
'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
'<stop offset="0" stop-color="#0b0b20"/><stop offset="1" stop-color="#130a2a"/></linearGradient>'
f'<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0">'
f'<stop offset="0" stop-color="{a}"/><stop offset="0.5" stop-color="{b}"/><stop offset="1" stop-color="{c}"/></linearGradient>'
f'<linearGradient id="accv" x1="0" y1="1" x2="0" y2="0">'
f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
'</defs>'
f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#bg)" stroke="{a}" stroke-opacity="0.35"/>'
'<rect x="1" y="1" width="758" height="34" rx="14" fill="#08081a"/>'
'<rect x="1" y="20" width="758" height="15" fill="#08081a"/>'
'<circle cx="24" cy="18" r="5" fill="#ff5f57"/><circle cx="42" cy="18" r="5" fill="#febc2e"/><circle cx="60" cy="18" r="5" fill="#28c840"/>'
f'<text x="380" y="23" text-anchor="middle" fill="#9AA3C7" font-family="Segoe UI, sans-serif" font-size="12">{title}</text>'
f'{body}</svg>')


def _wave(x0, x1, yc, amp, seed, n=64):
    pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        y = yc + amp * math.sin(i * 0.5 + seed) + amp * 0.4 * math.sin(i * 0.17 + seed * 1.3)
        pts.append(f"{x:.0f},{y:.0f}")
    return " ".join(pts)


def _panel(x, y, w, h, fill="#11112a", stroke=None, r=8):
    s = f' stroke="{stroke}" stroke-opacity="0.4"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{s}/>'


def _esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _txt(x, y, t, fill="#cdd4f5", size=11, anchor="start", weight="400"):
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-family="Segoe UI, sans-serif" '
            f'font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{_esc(t)}</text>')


# ---------------------------------------------------------------- archetypes
def daw(a, b, c, labels):
    out = [_panel(16, 46, 150, 366, "#0d0d24", a)]  # left header column
    rows = ["VOX", "GTR", "KEYS", "DRUM"]
    for i, name in enumerate(rows):
        y = 56 + i * 60
        out.append(_panel(24, y, 134, 48, "#141432", b))
        out.append(_txt(34, y + 20, name, "#fff", 11, weight="700"))
        out.append(f'<rect x="34" y="{y+28}" width="100" height="6" rx="3" fill="url(#acc)" opacity="0.5"/>')
        # clip with waveform
        cx = 178 + (i % 2) * 40
        out.append(_panel(cx, y, 540 - (i % 2) * 40, 48, "#0c0c22", c))
        out.append(f'<polyline points="{_wave(cx+8, cx+520-(i%2)*40, y+24, 14, i*1.7)}" '
                   f'fill="none" stroke="url(#acc)" stroke-width="2" opacity="0.9"/>')
    # ruler + playhead
    out.append(_panel(170, 46, 574, 14, "#0a0a1e"))
    for k in range(12):
        out.append(f'<line x1="{186+k*46}" y1="46" x2="{186+k*46}" y2="60" stroke="{b}" stroke-opacity="0.3"/>')
    out.append('<line x1="430" y1="46" x2="430" y2="392" stroke="#FF5555" stroke-width="2"/>')
    out.append('<polygon points="424,46 436,46 430,56" fill="#FF5555"/>')
    # transport
    for k, gl in enumerate(["#9AA3C7", "#39FF6E", "#9AA3C7", "#9AA3C7", "#FF5555"]):
        out.append(f'<circle cx="{210+k*30}" cy="402" r="11" fill="#15153a" stroke="{gl}" stroke-opacity="0.6"/>')
        out.append(f'<circle cx="{210+k*30}" cy="402" r="4" fill="{gl}"/>')
    out.append(f'<rect x="540" y="392" width="120" height="22" rx="6" fill="#0a0a1e"/>')
    out.append(_txt(600, 407, labels.get("timer", "00:42.318"), "#39FF6E", 14, "middle", "700"))
    return "".join(out)


def visualizer(a, b, c, labels):
    out = []
    cx, cy = 380, 230
    # radial bars
    for i in range(48):
        ang = i / 48 * math.tau
        amp = 40 + 55 * abs(math.sin(i * 0.6)) * (0.6 + 0.4 * abs(math.sin(i * 0.27)))
        x1 = cx + math.cos(ang) * 60; y1 = cy + math.sin(ang) * 60
        x2 = cx + math.cos(ang) * (60 + amp); y2 = cy + math.sin(ang) * (60 + amp)
        out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
                   f'stroke="url(#accv)" stroke-width="4" stroke-linecap="round" opacity="0.9"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="54" fill="none" stroke="{b}" stroke-opacity="0.5" stroke-width="2"/>')
    out.append(_txt(cx, cy + 5, labels.get("mode", "RADIAL"), b, 13, "middle", "700"))
    # bottom hud
    out.append(_panel(16, 388, 728, 26, "#0a0a1e"))
    for k in range(10):
        on = k in (0, 2, 5)
        col = b if on else "#2a2a4e"
        out.append(f'<rect x="{30+k*30}" y="396" width="20" height="10" rx="3" fill="{col}"/>')
    return "".join(out)


def gallery(a, b, c, labels):
    out = [_panel(16, 46, 120, 366, "#0d0d24", a)]
    for i, t in enumerate(labels.get("nav", ["All", "Dupes", "Unique", "Drives"])):
        on = i == 0
        out.append(_panel(24, 56 + i * 34, 104, 26, ("url(#acc)" if on else "#15153a")))
        out.append(_txt(34, 73 + i * 34, t, "#fff" if on else "#9AA3C7", 11, weight="700" if on else "400"))
    # thumbnail grid
    cols, rows = 5, 3
    gw, gh = 108, 100
    for r in range(rows):
        for col in range(cols):
            x = 150 + col * (gw + 8); y = 52 + r * (gh + 12)
            sel = (r == 0 and col == 1)
            grad = "url(#acc)" if (r + col) % 3 == 0 else ("url(#accv)" if (r + col) % 3 == 1 else "#1b1b3e")
            out.append(f'<rect x="{x}" y="{y}" width="{gw}" height="{gh-22}" rx="6" fill="{grad}" opacity="0.85"/>')
            if sel:
                out.append(f'<rect x="{x-2}" y="{y-2}" width="{gw+4}" height="{gh-18}" rx="7" fill="none" stroke="{b}" stroke-width="3"/>')
            out.append(_panel(x, y + gh - 18, gw, 14, "#11112a"))
            out.append(_txt(x + 6, y + gh - 8, f"IMG_{r}{col}.jpg", "#8a93bd", 8))
    return "".join(out)


def video(a, b, c, labels):
    out = [_panel(580, 46, 164, 366, "#0d0d24", a)]  # right rail
    out.append(_panel(16, 46, 552, 250, "#08081c", c))  # player
    out.append(f'<polygon points="270,150 270,208 320,179" fill="{b}" opacity="0.95"/>')
    out.append(f'<circle cx="292" cy="179" r="44" fill="none" stroke="{b}" stroke-opacity="0.6" stroke-width="3"/>')
    out.append(_panel(28, 276, 528, 8, "#15153a"))
    out.append(f'<rect x="28" y="276" width="300" height="8" rx="4" fill="url(#acc)"/>')
    out.append(_txt(34, 70, labels.get("title", "Now Playing"), "#fff", 12, weight="700"))
    # related thumbs
    for i in range(3):
        y = 300 + i * 0  # row of 4 below
    for i in range(4):
        x = 16 + i * 140
        out.append(_panel(x, 300, 128, 100, "#15153a"))
        out.append(f'<rect x="{x+8}" y="308" width="112" height="58" rx="4" fill="{"url(#acc)" if i%2 else "url(#accv)"}" opacity="0.8"/>')
        out.append(_txt(x + 8, 384, "Channel " + str(i + 1), "#9AA3C7", 9))
    for i in range(5):
        out.append(_panel(592, 56 + i * 70, 140, 60, "#15153a"))
        out.append(f'<rect x="600" y="{62+i*70}" width="48" height="40" rx="4" fill="{"url(#accv)" if i%2 else "url(#acc)"}" opacity="0.8"/>')
        out.append(_txt(656, 80 + i * 70, "Up next", "#9AA3C7", 9))
    return "".join(out)


def chat(a, b, c, labels):
    out = [_panel(16, 46, 180, 366, "#0d0d24", a)]
    for i in range(5):
        y = 56 + i * 64
        out.append(f'<circle cx="40" cy="{y+18}" r="14" fill="{"url(#acc)" if i%2 else "url(#accv)"}"/>')
        out.append(_txt(62, y + 14, "Contact " + str(i + 1), "#fff", 11, weight="700"))
        out.append(_txt(62, y + 30, "encrypted message…", "#8a93bd", 9))
    # bubbles
    bubbles = [(0, 220, 240), (1, 360, 300), (0, 220, 200), (1, 330, 260)]
    for i, (side, x, w) in enumerate(bubbles):
        y = 60 + i * 80
        fill = "#1b1b40" if side == 0 else "url(#acc)"
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="56" rx="14" fill="{fill}" opacity="0.92"/>')
        out.append(_txt(x + 16, y + 24, "Lorem ipsum dolor sit", "#e8ecff", 10))
        out.append(_txt(x + 16, y + 42, "amet consectetur.", "#cdd4f5", 10))
    out.append(_panel(216, 380, 520, 30, "#15153a", b))
    out.append(_txt(232, 399, "Type a message…", "#8a93bd", 11))
    return "".join(out)


def feed(a, b, c, labels):
    out = [_panel(16, 46, 150, 366, "#0d0d24", a), _panel(596, 46, 148, 366, "#0d0d24", c)]
    for i in range(2):
        y = 54 + i * 178
        out.append(_panel(186, y, 392, 168, "#11112a", b))
        out.append(f'<circle cx="212" cy="{y+28}" r="14" fill="{"url(#acc)" if i else "url(#accv)"}"/>')
        out.append(_txt(236, y + 24, "User Name", "#fff", 11, weight="700"))
        out.append(_txt(236, y + 40, "shared a post", "#8a93bd", 9))
        out.append(f'<rect x="200" y="{y+52}" width="364" height="70" rx="6" fill="{"url(#accv)" if i else "url(#acc)"}" opacity="0.6"/>')
        for k, e in enumerate(["👍", "👎", "😱"]):
            out.append(_txt(212 + k * 44, y + 150, e, "#cdd4f5", 14))
    return "".join(out)


def dashboard(a, b, c, labels):
    out = [_panel(16, 46, 140, 366, "#0d0d24", a)]
    for i, t in enumerate(labels.get("nav", ["Overview", "Customers", "Sales", "Finance", "Reports"])):
        on = i == 0
        out.append(_panel(24, 58 + i * 36, 124, 28, ("url(#acc)" if on else "#15153a")))
        out.append(_txt(34, 76 + i * 36, t, "#fff" if on else "#9AA3C7", 10, weight="700" if on else "400"))
    # stat cards
    stats = labels.get("stats", [("Revenue", "£12.4k"), ("Open", "18"), ("Due", "5"), ("Paid", "92%")])
    for i, (k, vv) in enumerate(stats):
        x = 170 + i * 145
        out.append(_panel(x, 52, 132, 70, "#13132f", b))
        out.append(_txt(x + 14, 84, vv, "#fff", 20, weight="800"))
        out.append(_txt(x + 14, 104, k, "#8a93bd", 10))
    # bar chart
    out.append(_panel(170, 134, 400, 270, "#11112a", c))
    for i in range(8):
        bh = 30 + 150 * abs(math.sin(i * 0.7))
        out.append(f'<rect x="{192+i*46}" y="{384-bh:.0f}" width="28" height="{bh:.0f}" rx="4" fill="url(#accv)" opacity="0.9"/>')
    # doughnut
    out.append(f'<circle cx="660" cy="270" r="64" fill="none" stroke="#15153a" stroke-width="22"/>')
    out.append(f'<circle cx="660" cy="270" r="64" fill="none" stroke="url(#acc)" stroke-width="22" '
               f'stroke-dasharray="240 402" transform="rotate(-90 660 270)"/>')
    return "".join(out)


def network(a, b, c, labels):
    out = []
    cx, cy = 360, 230
    nodes = [(cx, cy, "ROUTER")]
    for i in range(7):
        ang = i / 7 * math.tau
        nodes.append((cx + math.cos(ang) * 150, cy + math.sin(ang) * 120, ["PC", "PHONE", "TV", "PI", "LAPTOP", "IOT", "NAS"][i]))
    for nx, ny, _ in nodes[1:]:
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="{b}" stroke-opacity="0.25"/>')
    for i, (nx, ny, nm) in enumerate(nodes):
        col = "url(#acc)" if i == 0 else "url(#accv)"
        r = 24 if i == 0 else 16
        out.append(f'<circle cx="{nx:.0f}" cy="{ny:.0f}" r="{r}" fill="{col}" opacity="0.9"/>')
        out.append(_txt(nx, ny + r + 12, nm, "#9AA3C7", 9, "middle"))
    out.append(_panel(580, 56, 164, 120, "#11112a", a))
    out.append(_txt(596, 78, "192.168.0.4", "#fff", 11, weight="700"))
    out.append(_txt(596, 98, "DNS · 1.2 GB", "#8a93bd", 10))
    return "".join(out)


def viewport3d(a, b, c, labels):
    out = [_panel(596, 46, 148, 366, "#0d0d24", a)]
    # grid floor
    for i in range(8):
        out.append(f'<line x1="40" y1="{120+i*36}" x2="560" y2="{120+i*36}" stroke="{b}" stroke-opacity="0.12"/>')
        out.append(f'<line x1="{40+i*74}" y1="120" x2="{40+i*74}" y2="372" stroke="{b}" stroke-opacity="0.12"/>')
    # iso cube (a building)
    out.append(f'<polygon points="300,150 380,190 380,300 300,260" fill="url(#accv)" opacity="0.85"/>')
    out.append(f'<polygon points="300,150 220,190 220,300 300,260" fill="url(#acc)" opacity="0.6"/>')
    out.append(f'<polygon points="300,150 380,190 300,230 220,190" fill="{b}" opacity="0.9"/>')
    # param sliders
    for i in range(5):
        y = 60 + i * 60
        out.append(_txt(610, y, ["Width", "Height", "Depth", "Roof", "Scale"][i], "#9AA3C7", 9))
        out.append(_panel(610, y + 8, 118, 6, "#15153a"))
        out.append(f'<circle cx="{640+i*12}" cy="{y+11}" r="7" fill="url(#acc)"/>')
    return "".join(out)


def matrix(a, b, c, labels):
    out = [f'<rect x="2" y="35" width="756" height="391" fill="#000308"/>']
    import random
    rnd = random.Random(7)
    for col in range(30):
        x = 18 + col * 25
        head = rnd.randint(40, 360)
        for k in range(10):
            y = head - k * 24
            if 40 < y < 412:
                op = max(0.08, 1 - k * 0.12)
                ch = chr(0x30A0 + rnd.randint(0, 60))
                fill = "#eafff0" if k == 0 else b
                out.append(f'<text x="{x}" y="{y}" fill="{fill}" opacity="{op:.2f}" '
                           f'font-family="Consolas, monospace" font-size="16">{ch}</text>')
    out.append(_txt(380, 220, labels.get("clock", "21:48"), "#eafff0", 64, "middle", "800"))
    out.append(_txt(380, 252, labels.get("date", "Friday · 19 June"), b, 16, "middle", "600"))
    return "".join(out)


def game(a, b, c, labels):
    out = []
    # sky
    out.append('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
               f'<stop offset="0" stop-color="{a}" stop-opacity="0.5"/><stop offset="1" stop-color="{b}" stop-opacity="0.15"/>'
               '</linearGradient></defs>')
    out.append('<rect x="2" y="35" width="756" height="250" fill="url(#sky)"/>')
    out.append(f'<circle cx="640" cy="100" r="34" fill="{b}" opacity="0.8"/>')
    out.append(f'<rect x="2" y="270" width="756" height="156" fill="{c}" opacity="0.18"/>')
    out.append(f'<path d="M2 285 Q200 250 400 285 T758 280 L758 426 L2 426 Z" fill="{a}" opacity="0.22"/>')
    # trees
    for x in (120, 250, 560, 680):
        out.append(f'<rect x="{x}" y="225" width="10" height="40" fill="#3a2a1a"/>')
        out.append(f'<circle cx="{x+5}" cy="215" r="26" fill="{b}" opacity="0.55"/>')
    # character + dog
    out.append(f'<circle cx="350" cy="300" r="14" fill="#f3c79a"/><rect x="340" y="312" width="20" height="34" rx="6" fill="url(#acc)"/>')
    out.append(f'<ellipse cx="410" cy="345" rx="26" ry="13" fill="#2a2a2a"/><circle cx="432" cy="338" r="9" fill="#2a2a2a"/>')
    # HUD
    out.append(_panel(16, 384, 728, 28, "#0a0a1eaa".replace("aa", "")))
    for i, (nm, pct) in enumerate(labels.get("stats", [("Food", .7), ("Water", .5), ("Energy", .8), ("Happy", .9)])):
        x = 28 + i * 175
        out.append(_txt(x, 402, nm, "#9AA3C7", 9))
        out.append(_panel(x + 44, 394, 100, 8, "#15153a"))
        out.append(f'<rect x="{x+44}" y="394" width="{int(100*pct)}" height="8" rx="4" fill="url(#acc)"/>')
    return "".join(out)


def pong(a, b, c, labels):
    out = ['<rect x="2" y="35" width="756" height="391" fill="#020208"/>']
    for k in range(14):
        out.append(f'<rect x="378" y="{46+k*28}" width="4" height="16" fill="{b}" opacity="0.5"/>')
    out.append(f'<rect x="40" y="160" width="12" height="90" rx="3" fill="url(#accv)"/>')
    out.append(f'<rect x="708" y="220" width="12" height="90" rx="3" fill="url(#accv)"/>')
    out.append(f'<rect x="430" y="210" width="16" height="16" rx="3" fill="#fff"/>')
    out.append(_txt(300, 90, "3", "#fff", 40, "middle", "800"))
    out.append(_txt(460, 90, "2", "#fff", 40, "middle", "800"))
    return "".join(out)


def gridphoto(a, b, c, labels):
    out = [_panel(16, 46, 580, 366, "#08081c", c)]
    out.append(f'<rect x="40" y="66" width="532" height="326" rx="6" fill="url(#accv)" opacity="0.30"/>')
    # rule of thirds
    for i in (1, 2):
        out.append(f'<line x1="{40+i*177}" y1="66" x2="{40+i*177}" y2="392" stroke="#fff" stroke-opacity="0.6"/>')
        out.append(f'<line x1="40" y1="{66+i*109}" x2="572" y2="{66+i*109}" stroke="#fff" stroke-opacity="0.6"/>')
    # golden spiral hint
    out.append(f'<path d="M572 66 A266 326 0 0 1 306 392" fill="none" stroke="{b}" stroke-opacity="0.7"/>')
    out.append(_panel(610, 46, 134, 366, "#0d0d24", a))
    for i in range(6):
        y = 60 + i * 58
        out.append(_txt(624, y, ["Thirds", "Custom", "Pixel", "Golden", "B&W", "Grain"][i], "#9AA3C7", 9))
        out.append(_panel(624, y + 8, 104, 6, "#15153a"))
        out.append(f'<circle cx="{650+i*9}" cy="{y+11}" r="7" fill="url(#acc)"/>')
    return "".join(out)


# -------- phone-framed (Android) --------
def _phone(inner, a, b, c, title="App"):
    px, py, pw, ph = 300, 50, 160, 330
    out = [f'<rect x="2" y="35" width="756" height="391" fill="#070716"/>']
    out.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="26" fill="#05050f" stroke="{a}" stroke-opacity="0.5" stroke-width="2"/>')
    out.append(f'<rect x="{px+8}" y="{py+18}" width="{pw-16}" height="{ph-36}" rx="10" fill="#0b0b20"/>')
    out.append(f'<circle cx="{px+pw/2}" cy="{py+11}" r="3" fill="#222"/>')
    out.append(inner(px + 8, py + 18, pw - 16, ph - 36, a, b, c))
    # side phones (faded) for variety
    return "".join(out)


def _ph_grid(x, y, w, h, a, b, c):
    out = [f'<rect x="{x+6}" y="{y+8}" width="{w-12}" height="{h-70}" rx="4" fill="url(#accv)" opacity="0.3"/>']
    for i in (1, 2):
        out.append(f'<line x1="{x+6+(w-12)*i/3:.0f}" y1="{y+8}" x2="{x+6+(w-12)*i/3:.0f}" y2="{y+h-62}" stroke="#fff" stroke-opacity="0.6"/>')
        out.append(f'<line x1="{x+6}" y1="{y+8+(h-70)*i/3:.0f}" x2="{x+w-6}" y2="{y+8+(h-70)*i/3:.0f}" stroke="#fff" stroke-opacity="0.6"/>')
    out.append(f'<rect x="{x+6}" y="{y+h-50}" width="{w-12}" height="40" rx="6" fill="#11112a"/>')
    return "".join(out)


def _ph_scale(x, y, w, h, a, b, c):
    cx = x + w / 2
    out = [f'<circle cx="{cx}" cy="{y+90}" r="46" fill="url(#acc)" opacity="0.25" stroke="{b}" stroke-opacity="0.6"/>']
    out.append(_txt(cx, y + 170, "7.94", "#39FF6E", 34, "middle", "800"))
    out.append(_txt(cx, y + 192, "grams", "#9AA3C7", 11, "middle"))
    out.append(_txt(cx, y + 230, "STABLE", b, 11, "middle", "700"))
    out.append(f'<rect x="{x+14}" y="{y+250}" width="{(w-36)/2}" height="26" rx="6" fill="#15153a"/>')
    out.append(f'<rect x="{x+w/2+4}" y="{y+250}" width="{(w-36)/2}" height="26" rx="6" fill="#15153a"/>')
    out.append(_txt(x + 14 + (w - 36) / 4, y + 267, "TARE", "#cdd4f5", 9, "middle"))
    out.append(_txt(x + w / 2 + 4 + (w - 36) / 4, y + 267, "ZERO", "#cdd4f5", 9, "middle"))
    return "".join(out)


def _ph_kids(x, y, w, h, a, b, c):
    out = []
    emojis = ["🐶", "🍎", "⭐", "🚗", "🌈", "🐱"]
    for i, e in enumerate(emojis):
        cx = x + 18 + (i % 2) * 62
        cy = y + 24 + (i // 2) * 74
        out.append(f'<rect x="{cx}" y="{cy}" width="52" height="60" rx="10" fill="{"url(#acc)" if i%2 else "url(#accv)"}" opacity="0.85"/>')
        out.append(_txt(cx + 26, cy + 40, e, "#fff", 22, "middle"))
    return "".join(out)


def phone_grid(a, b, c, labels):  return _phone(_ph_grid, a, b, c)
def phone_scale(a, b, c, labels): return _phone(_ph_scale, a, b, c)
def phone_kids(a, b, c, labels):  return _phone(_ph_kids, a, b, c)


KINDS = {
    "daw": daw, "visualizer": visualizer, "gallery": gallery, "video": video,
    "chat": chat, "feed": feed, "dashboard": dashboard, "network": network,
    "viewport3d": viewport3d, "matrix": matrix, "game": game, "pong": pong,
    "gridphoto": gridphoto, "phone_grid": phone_grid, "phone_scale": phone_scale,
    "phone_kids": phone_kids,
}


def render(kind, title, accent, labels=None):
    a, b, c = accent
    body = KINDS.get(kind, gallery)(a, b, c, labels or {})
    return frame(title, body, a, b, c)
