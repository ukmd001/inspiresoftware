# -*- coding: utf-8 -*-
"""
Per-app extras: screenshot archetype + caption, system-requirements tier and
any per-app requirement overrides. Keyed by the app slug used in data/apps.py.

tier        -> base requirements template (see REQ_TIERS in build.py):
               light | media | gpu3d | web | android
shot        -> {kind, caption, labels} ; kind is an archetype in screenshots.py
real_shots  -> optional [(img_path_relative_to_assets, caption)] to use real
               captures instead of the generated mockup on the app page
min_extra / rec_extra -> extra <li> lines appended to the requirement cards
req_note    -> paragraph shown under the requirement cards
"""

EXTRA = {
 # ---------------- Audio & Video ----------------
 "wave-studio-plus": {
   "tier": "media",
   "shot": {"kind": "daw", "caption": "The full studio — gradient-waveform timeline, per-track headers, transport and a running phosphor timer.",
            "labels": {"timer": "00:42.318"}},
   "real_shots": [
     ("img/wave_main_window.png", "The real Wave Studio Plus main window — timeline, mixer, media library and I/O panel under the animated logo banner."),
     ("img/wave_timeline_zoom.png", "Zoomed into a selected clip — the seven-stop gradient waveform and bold timeline ruler."),
   ],
   "min_extra": ["<strong>Audio:</strong> any Windows-compatible input/output device"],
   "rec_extra": ["<strong>Audio:</strong> ASIO-compatible interface for low-latency recording"],
   "req_note": "Requires FFmpeg on PATH for MP3 / FLAC / OGG / AAC export. The OpenGL 3.3 GPU requirement is for the 14-mode 3D visualiser.",
 },
 "streamhub": {
   "tier": "media",
   "shot": {"kind": "video", "caption": "A live preview with your scene sources and Up-Next list, ready to Go Live over RTMP.",
            "labels": {"title": "Scene: Main"}},
   "req_note": "Requires FFmpeg on PATH for RTMP streaming. A webcam and capture-capable GPU help for multi-source scenes.",
 },
 "audioviz": {
   "tier": "media",
   "shot": {"kind": "visualizer", "caption": "Radial mode reacting to system audio, with the mode HUD along the bottom.",
            "labels": {"mode": "RADIAL"}},
   "req_note": "An OpenGL-capable GPU keeps all 20 modes smooth at full screen.",
 },
 "capture": {
   "tier": "media",
   "shot": {"kind": "video", "caption": "Live capture preview with the recording controls — full screen, window or drag-selected region.",
            "labels": {"title": "● REC  Region"}},
   "req_note": "Requires FFmpeg on PATH. H.264 encoding is CPU-bound — more cores mean higher frame rates at higher resolutions.",
 },
 "tribute-video-maker": {
   "tier": "media",
   "shot": {"kind": "video", "caption": "A Ken Burns frame with the film strip below — stills pan and zoom, clips crop to 1080p.",
            "labels": {"title": "Building tribute…"}},
   "req_note": "Rendering is CPU-bound (moviepy + FFmpeg). Longer films and more clips benefit from more cores and RAM.",
 },

 # ---------------- Creative & Imaging ----------------
 "pc-picdraw": {
   "tier": "light",
   "shot": {"kind": "gridphoto", "caption": "A reference photo under a rule-of-thirds grid with the golden-ratio guide and the effects panel."},
 },
 "jpeg-scanner": {
   "tier": "light",
   "shot": {"kind": "gallery", "caption": "The lazy-loading thumbnail grid with a selected duplicate and the filter rail.",
            "labels": {"nav": ["All", "Dupes", "Unique", "Similar"]}},
   "req_note": "Scanning very large libraries across many drives benefits from more RAM and an SSD for the thumbnail cache.",
 },
 "heic-viewer": {
   "tier": "light",
   "shot": {"kind": "gallery", "caption": "HEIC files found on a drive, ticked for conversion, with a live preview.",
            "labels": {"nav": ["Scan", "Selected", "Convert"]}},
 },
 "imagesorter": {
   "tier": "light",
   "shot": {"kind": "gallery", "caption": "The image queue with Claude's category assignments and the category rail.",
            "labels": {"nav": ["Queue", "People", "Food", "Animals"]}},
   "req_note": "Requires an Anthropic API key (entered in Settings). A steady internet connection is needed for vision analysis.",
 },
 "imagebridge": {
   "tier": "light",
   "shot": {"kind": "gallery", "caption": "The date-grouped received panel; incoming phone photos convert to JPEG on arrival.",
            "labels": {"nav": ["Received", "Browser", "USB"]}},
   "req_note": "PC and phone must be on the same Wi-Fi for wireless transfer; USB mode needs ADB drivers for your phone.",
 },
 "fbx-builder": {
   "tier": "light",
   "shot": {"kind": "viewport3d", "caption": "A parametric building in the OpenGL viewport with the live parameter panel.",
            "labels": {}},
   "min_extra": ["<strong>Graphics:</strong> OpenGL 3.3-capable GPU (for the 3D viewport)"],
 },

 # ---------------- System & Network ----------------
 "pcpro": {
   "tier": "light",
   "shot": {"kind": "dashboard", "caption": "The live monitoring dashboard — hardware stat cards, a usage chart and the tab rail.",
            "labels": {"nav": ["CPU", "Memory", "Disk", "Audio", "Display"],
                       "stats": [("CPU", "32%"), ("RAM", "58%"), ("GPU", "41%"), ("Disk", "77%")]}},
 },
 "netwatch": {
   "tier": "light",
   "shot": {"kind": "network", "caption": "The draggable device map after an ARP sweep, with a device's DNS and bandwidth detail."},
   "min_extra": ["<strong>Drivers:</strong> Npcap (free) installed", "<strong>Privileges:</strong> must run as Administrator"],
   "req_note": "NetWatch needs Npcap for DNS sniffing and bandwidth capture, and must run as Administrator for raw sockets.",
 },
 "claudefetch": {
   "tier": "light",
   "shot": {"kind": "gallery", "caption": "Discovered files from a scan, filtered by type and queued for download.",
            "labels": {"nav": ["URL Scan", "Search", "Files"]}},
   "req_note": "Works without a key using extension detection; add an Anthropic API key to enable AI ranking and filtering.",
 },
 "claude-listener": {
   "tier": "light",
   "shot": {"kind": "visualizer", "caption": "The floating overlay with its 12-band spectrum analyser while listening.",
            "labels": {"mode": "LISTENING"}},
   "min_extra": ["<strong>Audio:</strong> a working microphone", "<strong>Network:</strong> internet (Google Speech Recognition)"],
 },

 # ---------------- Web Platforms ----------------
 "ghost": {
   "tier": "web",
   "shot": {"kind": "video", "caption": "The watch page — Video.js player, channel rail and up-next, on the dark GHOST theme.",
            "labels": {"title": "Watch"}},
   "req_note": "The server needs FFmpeg for HLS transcoding. Transcoding is CPU-heavy — more cores mean faster processing; storage scales with your video library.",
 },
 "free-coms": {
   "tier": "web",
   "shot": {"kind": "chat", "caption": "An end-to-end encrypted conversation with the contact list and message composer."},
   "req_note": "Encryption happens in the browser — any modern browser with Web Crypto works. The desktop wrapper bundles a Chromium view.",
 },
 "hotspot": {
   "tier": "web",
   "shot": {"kind": "feed", "caption": "The public feed — posts with Like / Dislike / WTF reactions, between the nav rails."},
 },
 "inspire-arts-crm": {
   "tier": "web",
   "shot": {"kind": "dashboard", "caption": "The business dashboard — revenue and status cards, a 12-month chart and a breakdown doughnut.",
            "labels": {"nav": ["Overview", "Customers", "Commissions", "Finance", "Reports"],
                       "stats": [("Revenue", "£12.4k"), ("Open", "18"), ("Due", "5"), ("Paid", "92%")]}},
   "req_note": "Runs on a Waitress server reachable from any device on the same Wi-Fi; cloudflared is bundled for later internet exposure.",
 },

 # ---------------- Games & Screensavers ----------------
 "spot": {
   "tier": "light",
   "shot": {"kind": "game", "caption": "Walking Spot through the park, with the five-stat HUD along the bottom.",
            "labels": {"stats": [("Food", .7), ("Water", .5), ("Energy", .8), ("Happy", .9)]}},
 },
 "spot-3d": {
   "tier": "gpu3d",
   "shot": {"kind": "game", "caption": "The Godot 3D world at golden hour — animated water, swaying grass and the stat HUD.",
            "labels": {"stats": [("Food", .6), ("Water", .7), ("Energy", .9), ("Happy", .8)]}},
 },
 "spot-vue": {
   "tier": "gpu3d",
   "shot": {"kind": "game", "caption": "The Unreal Engine 5 city — modular buildings, traffic and Spot on the pavement.",
            "labels": {"stats": [("Food", .8), ("Water", .6), ("Energy", .7), ("Happy", .9)]}},
   "min_extra": ["<strong>Graphics:</strong> DirectX 12 GPU, 4 GB VRAM"],
   "rec_extra": ["<strong>Graphics:</strong> RTX 2060 / RX 5700 or better, 8 GB VRAM"],
   "req_note": "Spot vUE is a packaged Unreal Engine 5 game — it's the heaviest title in the catalogue and wants a dedicated GPU.",
 },
 "pong": {
   "tier": "light",
   "shot": {"kind": "pong", "caption": "Classic Pong — two paddles, a centre net and the score, also installable as a screensaver."},
 },
 "virtual-pet": {
   "tier": "gpu3d",
   "shot": {"kind": "game", "caption": "A 3D pet in its scene under a day/night cycle — also runs as a transparent desktop pet.",
            "labels": {"stats": [("Food", .5), ("Fun", .8), ("Rest", .7), ("Love", .9)]}},
   "req_note": "The 3D screensaver uses the Ursina/Panda3D engine and likes a GPU; the 2D transparent desktop pet is far lighter.",
 },
 "digital-clock-screensaver": {
   "tier": "light",
   "shot": {"kind": "matrix", "caption": "Matrix rain falling behind the full-screen clock, day and date.",
            "labels": {"clock": "21:48", "date": "Friday · 19 June"}},
 },

 # ---------------- Mobile ----------------
 "picdraw-grid": {
   "tier": "android",
   "shot": {"kind": "phone_grid", "caption": "The full-screen viewer on a Galaxy S20 with a rule-of-thirds grid overlay."},
   "min_extra": ["<strong>OS:</strong> Android 10 (minSdk 29) or newer"],
 },
 "skale": {
   "tier": "android",
   "shot": {"kind": "phone_scale", "caption": "The live gram readout with a coin on the touchscreen and the Tare / Zero controls."},
   "min_extra": ["<strong>Hardware:</strong> capacitive touchscreen (senses conductive objects only)"],
   "req_note": "Skale reads the capacitive touchscreen, so it only senses conductive objects — coins, cutlery, a glass of water.",
 },
 "talktime": {
   "tier": "android",
   "shot": {"kind": "phone_kids", "caption": "A child's exercise home screen of emoji word cards, on a Galaxy S20."},
   "min_extra": ["<strong>Hardware:</strong> microphone + a text-to-speech engine"],
 },
}
