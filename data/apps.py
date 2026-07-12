# -*- coding: utf-8 -*-
"""
Inspire Arts Software — app catalogue.
One dict per app. build.py turns each into a full promo page and a
storefront card. Copy is drawn from the real feature set of each app.

Field reference
---------------
slug         file name (apps/<slug>.html)
name         display name
icon         emoji used in hero / card
category     one of CATEGORIES (controls grouping + order on the storefront)
tagline      one line, used on the card and under the hero title
platform     short badge shown on the storefront card
badges       hero badge chips (list)
anim         hero canvas animation: waveform | spectrum | orbit | matrix | particles
accent       (a,b,c) hex accent colours; omit for the house blue/cyan/purple
footline     short phrase for the page footer
intro        hero/section lede (HTML <strong> allowed)
features     list of (icon, title, body)
specs        list of (label, value)
requirements optional HTML block (how to run / requirements)
download     text under the download button
deep         optional list of dicts: {title, body, bullets[], anim} feature rows
"""

CATEGORIES = [
    ("Audio & Video",                "Record it, mix it, capture it, ship it."),
    ("Creative & Imaging",           "Tools for pictures, references and 3D assets."),
    ("System & Network",             "See your machine and your network clearly."),
    ("Web Platforms",                "Self-hosted platforms you actually own."),
    ("Games & Screensavers",         "Play, idle and decorate your desktop."),
    ("Mobile",                       "Native Android, built for the Galaxy."),
]

HOUSE = ("#3A86FF", "#33E0FF", "#C77DFF")

APPS = [
# ============================================================ AUDIO & VIDEO
{
 "slug":"wave-studio-plus", "name":"Wave Studio Plus", "icon":"🌊",
 "category":"Audio & Video",
 "tagline":"A full multi-track DAW that looks as alive as it sounds.",
 "platform":"Windows", "anim":"waveform", "accent":HOUSE,
 "badges":["Windows 10 / 11","Unlimited tracks","One-click installer"],
 "footline":"record the wave, ride the light.",
 "intro":"The multi-track digital audio workstation that <strong>looks as alive as it "
         "sounds</strong>. Record, edit, mix and master on a stage of stars — with an "
         "interface that breathes, pulses and shifts colour to your music.",
 "features":[
   ("🎙️","Unlimited Multi-Track Recording","A low-latency duplex engine with <strong>ASIO support</strong> lets you monitor live input while the rest of the mix plays back, with per-track I/O level meters."),
   ("🌊","Gradient Waveforms","Every clip renders with a rich <strong>seven-stop vertical gradient</strong>, glowing edges and bold labels — read your arrangement across the room."),
   ("✂️","Non-Destructive Editing","Trim from clip edges without touching the source. <strong>Ctrl-drag to time-stretch</strong> with librosa, plus pitch-shift, fades and zero-crossing snap."),
   ("🎚️","Full Mixing Console","Vertical faders, pan dials, per-track FX, a master bus strip and an adaptive stereo master meter — all in sync with the track headers."),
   ("🌈","14-Mode 3D Visualiser","Press Ctrl+Alt+V for an OpenGL visualiser with <strong>fourteen hand-built 3D scenes</strong>, fed by a lock-free buffer so visuals never touch your latency."),
   ("📚","Built-In Media Library","Catalogues the audio on every drive, hover any file for a 6-second preview, then drag it straight into your project."),
 ],
 "specs":[
   ("Audio engine","Low-latency duplex streaming with ASIO, real-time monitoring, lock-free visualisation buffer"),
   ("Effects per track","Noise Gate → 3-Band EQ → Compressor → Reverb, plus per-clip noise reduction, filters and echo"),
   ("Editing","Non-destructive trim, time-stretch, pitch-shift, zero-crossing snap, fades, copy/paste"),
   ("Export","WAV 16/24/32-bit, MP3, FLAC, OGG, AAC/M4A — projects save as open .wspproj"),
   ("Visualiser","OpenGL hardware-accelerated, 14 modes, fullscreen capable"),
   ("Platform","Windows 10 / 11 · one-click installer · no account, no subscription"),
 ],
 "price":"£5 · one-time",
 "download":"Wave_Studio_Plus_Setup.exe · £5 one-time · no subscription · Windows 10/11",
},
{
 "slug":"streamhub", "name":"StreamHub", "icon":"📡",
 "category":"Audio & Video",
 "tagline":"Scenes, sources and one-click Go-Live RTMP streaming.",
 "platform":"Windows", "anim":"spectrum", "accent":("#FF3B6B","#FFB13B","#C77DFF"),
 "badges":["Windows 10 / 11","RTMP streaming","FFmpeg included"],
 "footline":"your studio, on air.",
 "intro":"A live-streaming and broadcast studio. Build scenes from <strong>screen, webcam, "
         "image and video</strong> sources, arrange them on a live preview, mix your audio, "
         "and hit Go Live to stream over RTMP to any platform.",
 "features":[
   ("🎬","Scenes & Sources","Compose screen captures, webcams, images and video clips. Drag, resize and select right on the preview with per-source and window opacity."),
   ("🔀","Pro Transitions","Switch scenes with Fade, Slide, Wipe, Zoom or Stinger transitions for a broadcast-grade look."),
   ("🎚️","Audio Mixer","Mix microphone and desktop loopback audio together before it ever leaves your machine."),
   ("🔴","Go Live over RTMP","Stream to any platform — set the RTMP URL, key, resolution and FPS, and FFmpeg pushes the broadcast."),
   ("🧩","Clean Engine Core","The scene, compositor and streaming core is decoupled from the interface — fast, stable and easy to extend."),
   ("📦","FFmpeg Included","FFmpeg ships inside the app, so streaming works the moment you install — nothing else to download or set up."),
 ],
 "specs":[
   ("Sources","Screen, webcam, image, video — drag/resize/select on a live preview"),
   ("Transitions","Fade · Slide · Wipe · Zoom · Stinger"),
   ("Audio","Microphone + desktop loopback, mixed pre-broadcast"),
   ("Streaming","RTMP via bundled FFmpeg; platform/URL/key/resolution/fps in Settings"),
   ("Distribution","Portable GUI build with FFmpeg bundled — no separate downloads"),
   ("Platform","Windows 10 / 11"),
 ],
 "price":"£5 · one-time",
 "download":"StreamHub · £5 one-time · FFmpeg included · Windows 10/11",
},
{
 "slug":"audioviz", "name":"AudioViz", "icon":"🎆",
 "category":"Audio & Video",
 "tagline":"20 real-time visualisations of whatever your PC is playing.",
 "platform":"Windows", "anim":"spectrum", "accent":("#FF5DA2","#33E0FF","#9D5BFF"),
 "badges":["Windows 10 / 11","20 modes","WASAPI loopback"],
 "footline":"see the sound.",
 "intro":"A real-time audio visualiser that turns your speakers or mic into light. "
         "<strong>Twenty visualisation modes</strong>, floating draggable meter panels, "
         "and a full-screen canvas that reacts to every beat.",
 "features":[
   ("🌈","20 Visualisation Modes","Glow, Spectrum, Wave, Particles, DNA, Tunnel, Plasma, Aurora, Matrix, Flames and more — toggle any of them with a single key."),
   ("🎛️","Floating Meter Panels","Separate draggable, resizable, collapsible panels for mic and output — horizontal spectrum bars plus a VU meter on each."),
   ("🔊","WASAPI Loopback","Visualises system audio via pyaudiowpatch loopback, or your microphone via sounddevice — no virtual cables needed."),
   ("⚙️","Deep Options Panel","Sensitivity sliders, colour schemes (rainbow/fire/ice/neon/mono), bar styles and background effects like fade trails and scanlines."),
   ("🖥️","Full-Screen Canvas","The visualiser fills the screen with a compact HUD of toggles — built to run as a living wallpaper."),
   ("📦","One-Click Installer","Ships as a PyInstaller + Inno Setup build, ready to drop on any Windows machine."),
 ],
 "specs":[
   ("Modes","20 — Glow, Spectrum, Wave, Mic Ring, Particles, Circular, Mirror, Starfield, Spectro, Lissajous, DNA, Tunnel, Plasma, CRT Scope, Kaleid, Aurora, Bounce, Ripple, Matrix, Flames"),
   ("Audio in","Microphone (sounddevice) + system output (pyaudiowpatch WASAPI loopback)"),
   ("Customisation","Sensitivity, colour schemes, bar styles, background effects"),
   ("Platform","Windows 10 / 11 · single portable .exe"),
 ],
 "price":"£4 · one-time",
 "download":"AudioViz.exe · £4 one-time · no install needed · Windows 10/11",
},
{
 "slug":"capture", "name":"Capture", "icon":"⏺️",
 "category":"Audio & Video",
 "tagline":"A clean H.264 screen recorder, Vegas-ready out of the box.",
 "platform":"Windows", "anim":"particles", "accent":("#FF5555","#FFB13B","#3A86FF"),
 "badges":["Windows 10 / 11","MP4 H.264","Global hotkeys"],
 "footline":"hit F9 and go.",
 "intro":"A no-nonsense screen recorder that outputs clean, editable <strong>MP4 H.264 + "
         "AAC</strong> — fully compatible with Vegas Movie Studio. Full screen, a single "
         "window, or a region you drag yourself.",
 "features":[
   ("🖥️","Three Capture Modes","Record a full monitor, a single window that follows if it moves, or a region you drag-select with an overlay."),
   ("🎧","Flexible Audio","None, microphone, system audio via WASAPI loopback, or both mixed together — your choice per recording."),
   ("⌨️","Global Hotkeys","F9 starts, F10 stops — thread-safe and working even when the app isn't focused."),
   ("🎬","Editor-Friendly Output","CRF 18, ultrafast preset, muxed to a final MP4 that drops straight into Vegas Movie Studio."),
   ("⏱️","Selectable Frame Rate","Record at 24, 30 or 60 FPS depending on whether you want size or smoothness."),
   ("⚡","Lean Pipeline","mss frame grab → FFmpeg stdin → temp files muxed on stop, so recording stays light."),
 ],
 "specs":[
   ("Capture modes","Full screen (monitor select) · Window (follows movement) · Region (drag-select)"),
   ("Output","MP4 H.264 + AAC, -crf 18 -preset ultrafast, Vegas-compatible"),
   ("Audio","None / Mic / System (WASAPI loopback) / Both (mixed)"),
   ("Hotkeys","F9 start · F10 stop"),
   ("Frame rate","24 / 30 / 60 FPS"),
   ("Platform","Windows 10 / 11 · FFmpeg bundled"),
 ],
 "price":"£4 · one-time",
 "download":"Capture · £4 one-time · FFmpeg included · Windows 10/11",
},
{
 "slug":"tribute-video-maker", "name":"Tribute Video Maker", "icon":"🕊️",
 "category":"Audio & Video",
 "tagline":"Turn a lifetime of photos into a gentle memorial film.",
 "platform":"Windows", "anim":"particles", "accent":("#C77DFF","#7FB2FF","#E8ECFF"),
 "badges":["Windows 10 / 11","Ken Burns","1080p MP4"],
 "footline":"forever in our hearts.",
 "intro":"A quiet, careful tool for making a memorial film from the photos and clips you "
         "already have. It gathers your media, gives every still a slow <strong>Ken Burns "
         "pan and zoom</strong>, and wraps it in title cards — so the memories can simply play.",
 "features":[
   ("🔎","Finds Your Media","Scans the whole device for images and video, so you don't have to hunt through folders for the right moments."),
   ("🎞️","Ken Burns Motion","Every still gets a slow, gentle pan and zoom; video clips are centre-cropped to a clean 1080p frame."),
   ("📝","Title & Closing Cards","An opening card sets the dates and a closing card carries your words — written with care and kept tender."),
   ("🎵","Your Music","Add an MP3 and the film carries the song that means the most."),
   ("📺","Clean 1080p Export","Renders to a single shareable MP4, saved straight to your Desktop."),
   ("💜","Made With Respect","Built originally as a memorial for a much-loved dog — the tone stays gentle throughout."),
 ],
 "specs":[
   ("Input","Images + video clips scanned from the whole device"),
   ("Stills","Ken Burns pan/zoom"),
   ("Video","Centre-cropped to 1080p"),
   ("Music","Optional MP3 soundtrack"),
   ("Output","1080p MP4 saved to Desktop"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"TributeVideoMaker_Setup.exe · free · Windows 10/11",
},

# ============================================================ CREATIVE & IMAGING
{
 "slug":"pc-picdraw", "name":"PC PicDraw", "icon":"📐",
 "category":"Creative & Imaging",
 "tagline":"Grid overlays and B&W references for drawing from photos.",
 "platform":"Windows", "anim":"orbit", "accent":("#3A86FF","#33E0FF","#7FFFD4"),
 "badges":["Windows 10 / 11","Always-on-top","Golden ratio grids"],
 "footline":"draw what you see.",
 "intro":"A drawing-reference viewer that lays accurate grids and black-and-white passes over "
         "any photo. Built for artists working from reference — with <strong>recursive zoom "
         "grids</strong>, custom rotation, and an always-on-top window you can draw beside.",
 "features":[
   ("🔲","Four Grid Types","Rule of Thirds, Custom, Pixel and Golden-Ratio Fibonacci grids — with colour, opacity, thickness and a closed border rect."),
   ("🔍","Recursive Zoom Grids","Zoom in and nested sub-grid levels appear automatically, each hue-shifted so you always know which level you're on."),
   ("🎚️","B&W Reference Passes","Convert to greyscale with presets plus brightness, contrast, R/G/B mix and grain sliders to read values clearly."),
   ("🔄","Custom Rotation & Area Lock","Free-angle rotation, drag-select an area to zoom into, align the image under a fixed grid, then lock the view."),
   ("📌","Always-On-Top + Opacity","Pin the reference over your canvas and dial in window opacity — perfect for tracing-by-eye beside any drawing app."),
   ("💾","Save a Gridded Copy","Bake the grid and effects into a saved copy in a PicDrawGrid subfolder."),
 ],
 "specs":[
   ("Grids","Rule of Thirds · Custom · Pixel · Golden Ratio (Fibonacci spiral) + closed border"),
   ("B&W","Presets + brightness/contrast/RGB mix/grain"),
   ("Transform","Free-angle rotation, area selection, align-to-grid, position lock"),
   ("Window","Always-on-top, adjustable opacity, keyboard shortcuts"),
   ("Platform","Windows 10 / 11"),
 ],
 "price":"£3 · one-time",
 "download":"PC_PicDraw.exe · £3 one-time · no subscription · Windows 10/11",
},
{
 "slug":"jpeg-scanner", "name":"JPEG Scanner", "icon":"🔍",
 "category":"Creative & Imaging",
 "tagline":"Find and clear duplicate JPEGs across every drive.",
 "platform":"Windows", "anim":"particles", "accent":("#33E0FF","#3A86FF","#C77DFF"),
 "badges":["Windows 10 / 11","SHA-256 + perceptual","Recycle-bin safe"],
 "footline":"one of each, please.",
 "intro":"A duplicate-photo manager for large JPEG collections spread across multiple drives. "
         "It finds <strong>exact and look-alike duplicates</strong>, shows them side by side, "
         "and only ever soft-deletes to the Recycle Bin.",
 "features":[
   ("🧬","Exact + Perceptual Matching","SHA-256 catches byte-identical copies; optional perceptual hashing catches resized and re-saved look-alikes."),
   ("🖼️","Lazy-Loading Grid","Browse thousands of thumbnails in a smooth, lazy-loading grid that doesn't choke on big libraries."),
   ("🆚","Side-by-Side Compare","Open a compare dialog to judge two images before you decide which copy to keep."),
   ("♻️","Recycle-Bin Safe","Deletes go to the Recycle Bin via send2trash — nothing is ever permanently destroyed."),
   ("⚡","Incremental Scans","A SQLite cache skips files whose path, size and mtime are unchanged, so re-scans fly."),
   ("🗂️","Smart Filters","All / Duplicates / Unique / Similar Groups, with drive selection before each scan."),
 ],
 "specs":[
   ("Detection","SHA-256 exact + imagehash perceptual"),
   ("Extensions",".jpg .jpeg .jfif .jpe"),
   ("Deletes","Recycle Bin via send2trash (no permanent delete)"),
   ("Cache","SQLite at ~/.jpegscanner, incremental re-scans"),
   ("Filters","All · Duplicates · Unique · Similar Groups"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"JPEG_Scanner_Setup.exe · free · Windows 10/11",
},
{
 "slug":"heic-viewer", "name":"HEIC Viewer", "icon":"📷",
 "category":"Creative & Imaging",
 "tagline":"Open iPhone HEIC photos and batch-convert them to JPEG.",
 "platform":"Windows", "anim":"particles", "accent":("#33E0FF","#39FF6E","#3A86FF"),
 "badges":["Windows 10 / 11","Batch convert","Drive scan"],
 "footline":"HEIC in, JPEG out.",
 "intro":"A simple tool to deal with iPhone photos on Windows. Point it at a drive, it "
         "<strong>finds every .heic file</strong>, previews them, and converts the ones you "
         "tick to ordinary JPEGs in a folder of your choosing.",
 "features":[
   ("🔎","Whole-Drive Scan","Pick a drive and HEIC Viewer finds every .heic on it, skipping system folders to avoid permission errors."),
   ("👁️","Background Preview","Selected files preview in a non-blocking background thread, so the list never freezes."),
   ("☑️","Tick & Convert","A checkbox column drives the conversion batch; row selection drives the preview — independent and clear."),
   ("📁","Choose Your Output","Converted JPEGs land in a folder you pick, auto-renaming on collision (stem_1.jpg, stem_2.jpg…)."),
   ("🌑","Dark, Familiar UI","The same dark Fusion palette as the rest of the suite, so it feels at home."),
 ],
 "specs":[
   ("Input",".heic files found by drive scan"),
   ("Conversion","Pillow + pillow-heif → JPEG, auto-rename on collision"),
   ("Preview","Background ThumbLoader thread"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"HEIC_Viewer_Setup.exe · free · Windows 10/11",
},
{
 "slug":"imagesorter", "name":"ImageSorter", "icon":"🗃️",
 "category":"Creative & Imaging",
 "tagline":"Claude vision sorts your images into tidy category folders.",
 "platform":"Windows", "anim":"orbit", "accent":("#9D5BFF","#33E0FF","#FF5DA2"),
 "badges":["Windows 10 / 11","AI vision","Bulk sort"],
 "footline":"let the AI file it.",
 "intro":"An AI image sorter that looks at each picture with <strong>Claude vision</strong> and "
         "copies it into the right category folder for you — People, Landscape, Food, Animals, "
         "Documents, Screenshots and any categories you add.",
 "features":[
   ("🤖","Claude Vision Sorting","Each image is analysed by Claude and assigned a category automatically — resized to 1024px first to keep it fast and cheap."),
   ("🌳","Browser + Queue","A folder tree on the left and an image queue with thumbnails on the right; recursive scanning and multi-select."),
   ("🏷️","Custom Categories","Manage your own category list, with presets — and a manual review dialog whenever Claude returns “Other”."),
   ("📂","Copies, Never Moves","Sorted images are copied into <strong>Library B/&lt;Category&gt;</strong> (configurable), leaving your originals untouched."),
   ("🚀","Quick Navigation","One-tap jumps to Desktop, Pictures and Downloads to get sorting fast."),
   ("⚙️","Settings","Masked API-key field, destination folder and which file extensions to include."),
 ],
 "specs":[
   ("Model","Claude (claude-sonnet-4-6) vision"),
   ("Default categories","People, Landscape, Food, Animals, Documents, Screenshots, Other"),
   ("Output","Copies into C:/Library B/<Category>/ (configurable)"),
   ("Requires","Anthropic API key (entered in Settings)"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"ImageSorter_Setup.exe · free · Windows 10/11 · API key required",
},
{
 "slug":"imagebridge", "name":"ImageBridge", "icon":"🌉",
 "category":"Creative & Imaging",
 "tagline":"Beam phone photos to your PC and convert them to JPEG.",
 "platform":"Windows + Android", "anim":"particles", "accent":("#7C3AED","#33E0FF","#C77DFF"),
 "badges":["Windows + Android","Wi-Fi or USB","HEIC/RAW → JPEG"],
 "footline":"phone to PC, in one tap.",
 "intro":"A two-app bridge for getting every photo off your phone and onto your PC in a uniform "
         "format. The Android app sends over Wi-Fi or USB; the PC app receives, organises and "
         "<strong>converts HEIC, PNG, WebP, BMP, TIFF and RAW to JPEG</strong>.",
 "features":[
   ("📲","Android Sender","A full native gallery with date headers, multi-select, sort and view modes — Copy, Convert on-phone, or both, sent over Wi-Fi."),
   ("📥","Wi-Fi Receiver","The PC app runs a Flask receiver; incoming photos land in a date-grouped thumbnail panel with a zoom lightbox."),
   ("🔁","Universal Conversion","Pillow + pillow-heif + rawpy convert HEIC/PNG/WebP/BMP/TIFF/RAW into clean JPEGs on arrival."),
   ("🗂️","Built-In File Manager","A full browser tab — folder tree, thumbnail/list/detail views, search, and right-click copy/cut/paste/rename/convert."),
   ("🔌","USB / ADB Mode","Prefer a cable? Scan the device over ADB and pull all images with a progress bar."),
   ("🗑️","Recycle Bin","The Android side keeps a soft-delete recycle bin with restore and permanent-delete."),
 ],
 "specs":[
   ("PC app","PyQt6 + Flask receiver on port 8765"),
   ("Android app","Native Kotlin, minSdk 26, Room recycle bin"),
   ("Transfer","Wi-Fi (HTTP multipart) or USB/ADB"),
   ("Conversion","HEIC, PNG, WebP, BMP, TIFF, RAW → JPEG"),
   ("Platform","Windows 10 / 11 + Android 8+"),
 ],
 "download":"ImageBridge_Setup.exe (PC) + app-debug.apk (Android) · free",
},
{
 "slug":"fbx-builder", "name":"FBX Builder", "icon":"🧱",
 "category":"Creative & Imaging",
 "tagline":"Generate parametric FBX assets for Unreal Engine 5.",
 "platform":"Windows", "anim":"orbit", "accent":("#39FF6E","#33E0FF","#3A86FF"),
 "badges":["Windows 10 / 11","OpenGL viewport","UE5-ready FBX"],
 "footline":"build it, export it, drop it in UE5.",
 "intro":"A parametric asset builder that writes <strong>UE5-compatible FBX</strong> directly — "
         "no FBX SDK required. Generate buildings, vehicles and props, preview them in a live "
         "3D viewport, and export Z-up, centimetre-scale meshes Unreal imports cleanly.",
 "features":[
   ("🏢","Parametric Generators","Buildings, vehicles (sedan/SUV/truck/van) and eight prop types — bench, lamppost, fence, sign, barrier, hydrant, mailbox, trashcan."),
   ("🖥️","Live OpenGL Viewport","Orbit, pan and zoom a real-time 3D preview; toggle wireframe and grid as you tweak parameters."),
   ("📥","FBX Import","Reads both ASCII and binary FBX 7.x — drag files from the navigator or the desktop into the viewport."),
   ("📤","UE5-Correct Export","Writes FBX ASCII 7.4, Z-up, Y-forward, 1 unit = 1 cm — matching Unreal's import defaults exactly."),
   ("🗂️","Three-Panel Workflow","File navigator, viewport and parameter panel side by side — adjust and re-export in seconds."),
   ("🧮","No External SDK","Geometry math in numpy, FBX written directly — nothing to install beyond Python packages."),
 ],
 "specs":[
   ("Generators","Building · Vehicle · Prop (8 types)"),
   ("Import","FBX ASCII + binary 7.x"),
   ("Export","FBX ASCII 7.4, Z-up, cm units (UE5-ready)"),
   ("Viewport","PyOpenGL core, orbit camera, wireframe/grid toggles"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"FBX_Builder_Setup.exe · free · Windows 10/11",
},

# ============================================================ SYSTEM & NETWORK
{
 "slug":"pcpro", "name":"PCpro Professional Suite", "icon":"🖥️",
 "category":"System & Network",
 "tagline":"Live system monitoring, optimisation and maintenance — buy once, no subscription.",
 "platform":"Windows", "anim":"spectrum", "accent":("#33E0FF","#39FF6E","#3A86FF"),
 "badges":["One-time purchase · no subscription","Live monitoring","No bloat, no telemetry"],
 "footline":"know your machine.",
 "intro":"A complete PC suite: <strong>live CPU, RAM, disk, network, GPU, audio and display "
         "monitoring</strong>, a process manager, BIOS and boot tools, and ten optimisation "
         "toolkits — all in one tabbed dashboard.",
 "features":[
   ("📊","Live Hardware Monitoring","Real-time CPU, memory, disk, network and GPU readouts with detail cards, sampled continuously."),
   ("🔊","Audio Tab","Per-channel input/output level meters, volume and mute for default devices, plus a full device list."),
   ("🖥️","Display Tab","Per-monitor resolution, refresh, depth, DPI, orientation, adapter and EDID, with an Identify-displays button."),
   ("🧰","Ten Optimise Toolkits","A suite of maintenance and optimisation tools for cleaning up and tuning Windows."),
   ("📋","Process Manager","See and manage running processes, with BIOS and boot utilities alongside."),
   ("🔇","Crash-Safe Audio","Hard-won COM handling keeps the audio enumeration in a throwaway subprocess so the app never crashes on device queries."),
 ],
 "specs":[
   ("Monitoring","CPU · RAM · Disk · Network · GPU · Audio · Display"),
   ("Audio","pycaw level meters, volume/mute, device list"),
   ("Display","ctypes user32/shcore + WMI per-monitor details"),
   ("Tools","Process manager, BIOS/boot tools, 10 optimise toolkits"),
   ("Platform","Windows 10 / 11 (silent pythonw launcher)"),
 ],
 "price":"£12 · one-time",
 "download":"PCpro_Setup.exe · £12 one-time · no subscription · no bloat · Windows 10/11",
},
{
 "slug":"netwatch", "name":"NetWatch", "icon":"🛰️",
 "category":"System & Network",
 "tagline":"Map your LAN, watch DNS and bandwidth, scan ports.",
 "platform":"Windows", "anim":"orbit", "accent":("#FFB13B","#3A86FF","#33E0FF"),
 "badges":["Windows 10 / 11","ARP + DNS sniff","Admin + Npcap"],
 "footline":"see who's on your network.",
 "intro":"A home-network monitor that <strong>discovers every device on your LAN</strong>, draws "
         "them on a draggable map, and shows per-device DNS history, bandwidth and an on-demand "
         "port scan.",
 "features":[
   ("📡","ARP Discovery","Sweeps the LAN every 30 seconds to find all devices, colour-coded by type — router, Apple, Android, PC, Pi or unknown."),
   ("🗺️","Draggable Device Map","A dark, dot-grid canvas where every device is a node you can drag into the layout that makes sense to you."),
   ("🔎","Passive DNS Sniffing","Watches UDP port 53 to log which domains each device is querying — see what's really talking to the internet."),
   ("📈","Bandwidth Tracking","Bytes sent and received per device since launch, so heavy talkers stand out."),
   ("🔐","On-Demand Port Scan","Scan 18 common ports on any device in a background thread, without stalling the UI."),
   ("ℹ️","Device Detail Panel","Click a node for IP, MAC, hostname, manufacturer, DNS log and bandwidth totals."),
 ],
 "specs":[
   ("Discovery","ARP sweep every 30s, manufacturer via OUI"),
   ("Sniffing","DNS (UDP 53) + bandwidth via Scapy"),
   ("Port scan","18 common ports, background thread"),
   ("Requires","Npcap + run as Administrator"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"NetWatch_Setup.exe · free · Windows 10/11 · Npcap + admin",
},
{
 "slug":"claudefetch", "name":"ClaudeFetch", "icon":"🪝",
 "category":"System & Network",
 "tagline":"AI-guided file finder and bulk downloader.",
 "platform":"Windows", "anim":"particles", "accent":("#D97757","#33E0FF","#C77DFF"),
 "badges":["Windows 10 / 11","DuckDuckGo search","AI filtering"],
 "footline":"find it, rank it, fetch it.",
 "intro":"A downloader that finds the files you actually want. Paste a URL or search the web, and "
         "<strong>Claude AI filters and ranks</strong> the results before pulling everything down "
         "with progress bars — handy for bulk asset grabs like UE5 packs.",
 "features":[
   ("🔗","URL Scan","Paste any page, set a crawl depth (0–5), and ClaudeFetch finds every downloadable file on it."),
   ("🔎","Web Search","Search via DuckDuckGo (free, no key), then let Claude pick the most promising URLs to scan."),
   ("🤖","Smart AI Filtering","Claude (haiku, kept cheap) ranks links and filters noise so you download what matters."),
   ("🗂️","Type Filters","Documents, Archives, Media, Images, UE5 Assets and Code — tick what you want, skip the rest."),
   ("⬇️","Multi-File Downloads","Threaded downloads with per-file progress bars; save directory remembered between runs."),
   ("🔑","Optional Key","Works without an API key using extension-based detection; add a key to unlock AI ranking."),
 ],
 "specs":[
   ("Scan","requests + BeautifulSoup, crawl depth 0–5"),
   ("Search","DuckDuckGo (no key required)"),
   ("AI","Claude haiku for filtering + URL ranking (optional)"),
   ("Types","Documents · Archives · Media · Images · UE5 Assets · Code"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"ClaudeFetch_Setup.exe · free · Windows 10/11 · API key optional",
},
{
 "slug":"claude-listener", "name":"Claude Listener", "icon":"🎙️",
 "category":"System & Network",
 "tagline":'Say "Hey Claude" and dictate straight into the chat box.',
 "platform":"Windows", "anim":"spectrum", "accent":("#D97757","#39FF6E","#33E0FF"),
 "badges":["Windows 10 / 11","Wake word","Tray app"],
 "footline":"just say the word.",
 "intro":"A wake-word voice-to-text tray app. Say <strong>“Hey Claude”</strong>, speak your "
         "message, and it transcribes your speech, pastes it into the focused window, and presses "
         "Enter for you — hands-free prompting for Claude.",
 "features":[
   ("👂","Wake-Word Listening","Listens continuously for “Hey Claude” (and common mishears), beeps, then records your command."),
   ("⌨️","Auto-Paste + Enter","Transcribes via Google Speech Recognition, pastes into the focused window and auto-sends after a short, cancellable countdown."),
   ("📊","Live Overlay","A floating overlay shows a 12-band spectrum analyser, a mute button and a sensitivity slider while you talk."),
   ("🤫","Smart Silence Detection","Stops recording after 5 seconds of silence, with a 60-second ceiling for longer thoughts."),
   ("🔇","Mute & Pause","A separate muted state pauses wake-word detection from the tray or overlay whenever you need quiet."),
   ("🪟","Lives in the Tray","Runs quietly in the system tray with a full right-click menu."),
 ],
 "specs":[
   ("Wake phrases","“Hey Claude” / “Hi Claude” + common mishears"),
   ("Transcription","Google Speech Recognition"),
   ("Overlay","12-band FFT spectrum, mute, sensitivity slider"),
   ("Silence","5s stop threshold, 60s max command"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"ClaudeListener_Setup.exe · free · Windows 10/11",
},

# ============================================================ WEB PLATFORMS
{
 "slug":"ghost", "name":"GHOST", "icon":"👻",
 "category":"Web Platforms",
 "tagline":"Your own YouTube — HLS streaming, channels, the lot.",
 "platform":"Web · Self-host", "anim":"particles", "accent":("#C77DFF","#FF5555","#33E0FF"),
 "badges":["Self-hosted","HLS transcoding","Windows + Linux installers"],
 "footline":"host your own tube.",
 "intro":"A complete self-hosted video platform — a YouTube alternative you fully own. Upload a "
         "video and GHOST <strong>transcodes it to adaptive HLS</strong> (360p/720p/1080p), "
         "serves it in a Video.js player, and gives you channels, subscriptions, comments and a "
         "full admin panel.",
 "features":[
   ("🎥","Upload → HLS","Uploads transcode in the background via FFmpeg to 360p/720p/1080p HLS, with an auto-thumbnail grabbed at 3 seconds."),
   ("📺","Channels & Subscriptions","Every account is a channel — subscribe, get bell notifications on new uploads, and browse a subscription feed."),
   ("💬","Reactions & Comments","Like, Dislike, a WTF reaction and 1–5 star ratings, plus threaded comments with replies."),
   ("👥","Groups & Sharing","Public and private groups with roles, group feeds, and a share button that posts a video straight into a group."),
   ("🌐","External Embeds","Drop in YouTube, Vimeo, Dailymotion or direct MP4 URLs — auto-detected, no transcoding needed."),
   ("🛠️","Admin & Auto-Install","Full admin dashboard plus one-shot installers for Windows (NSSM service) and Linux (systemd + nginx)."),
 ],
 "specs":[
   ("Stack","Flask + SQLAlchemy/SQLite, FFmpeg HLS, Video.js"),
   ("Qualities","360p / 720p / 1080p adaptive HLS"),
   ("Social","Subscriptions, reactions, star ratings, threaded comments, groups"),
   ("Admin","Dashboard, user + video management, visibility public/unlisted/private"),
   ("Install","install_windows.ps1 (service) · install_linux.sh (systemd + nginx)"),
   ("Run","python run.py → http://localhost:5000"),
 ],
 "requirements":"Requires Python 3 and FFmpeg. After first run, register an account then "
                "promote it with <code>python make_admin.py &lt;username&gt;</code>.",
 "download":"GHOST source + auto-installers · free · self-hosted",
 "deep":[
   {"title":"🎞️ Upload once, stream everywhere","anim":"spectrum",
    "body":"Drop in a file and GHOST takes over — FFmpeg transcodes it to <strong>adaptive HLS</strong> "
           "in the background while you keep working, and Video.js serves the right quality for every "
           "viewer's connection.",
    "bullets":["<strong>360p / 720p / 1080p</strong> rendered automatically",
               "<strong>Auto-thumbnails</strong> grabbed at the 3-second mark",
               "<strong>External videos</strong> — YouTube, Vimeo, Dailymotion, direct MP4, auto-embedded",
               "<strong>Player zoom</strong> — Shift+Scroll to 1×–5×, drag to pan"]},
 ],
},
{
 "slug":"free-coms", "name":"FREE COMS", "icon":"🔐",
 "category":"Web Platforms",
 "tagline":"End-to-end encrypted messaging with calls and stories.",
 "platform":"Web · Self-host", "anim":"orbit", "accent":("#39FF6E","#33E0FF","#3A86FF"),
 "badges":["Self-hosted","E2E encrypted","Voice + video calls"],
 "footline":"your messages, your server.",
 "intro":"A private, self-hosted messenger in the WhatsApp mould — with real "
         "<strong>end-to-end encryption</strong> (RSA-OAEP + AES-GCM via Web Crypto), WebRTC "
         "voice and video calls, groups, 24-hour stories and a full admin panel.",
 "features":[
   ("🔒","True E2E Encryption","One-to-one DMs are encrypted in the browser with a hybrid RSA-OAEP + AES-GCM scheme; keys never leave the client."),
   ("👥","Encrypted Groups","Group chats use an encrypted AES key per member, so the server only ever sees ciphertext."),
   ("📞","Voice & Video Calls","Peer-to-peer WebRTC calls with the server acting only as a STUN signalling relay."),
   ("📸","24-Hour Stories","Post status updates that expire after a day, with view tracking and a carousel viewer."),
   ("🎨","Deep Personalisation","Six colour themes, font sizes, bubble styles and custom chat backgrounds — saved server-side per user."),
   ("🛡️","Admin Control","Ban, unban, flag, warn, review reports and remove messages from a full admin panel with animated styling."),
 ],
 "specs":[
   ("Stack","Flask + Flask-SocketIO + SQLAlchemy/SQLite, PyQt6 desktop wrapper"),
   ("Encryption","RSA-OAEP + AES-GCM hybrid (Web Crypto API)"),
   ("Calls","WebRTC P2P, server as STUN signalling"),
   ("Extras","Stories, read receipts, typing indicators, presence, block/report"),
   ("Run","python run.py (startup password gate) → port 5050"),
 ],
 "requirements":"Default admin <code>admin / admin123</code>. Desktop wrapper launches the "
                "server and shows a splash; or run headless with <code>python run.py</code>.",
 "download":"FREE COMS source + desktop wrapper · free · self-hosted",
},
{
 "slug":"hotspot", "name":"Hotspot", "icon":"🔥",
 "category":"Web Platforms",
 "tagline":"A social network with public feeds and private groups.",
 "platform":"Web · Self-host", "anim":"particles", "accent":("#FF5DA2","#FFB13B","#9D5BFF"),
 "badges":["Self-hosted","Real-time DMs","Public + private groups"],
 "footline":"your community, your rules.",
 "intro":"A full social platform you can stand up on your own server — public feeds, "
         "<strong>invite-only private groups</strong>, reactions, threaded comments, follows, "
         "real-time DMs and an admin panel, all on a Bootstrap dark theme.",
 "features":[
   ("📝","Rich Posts","Text, image and video posts with visibility control — public, friends-only or group-only."),
   ("😱","Three Reactions","Like, Dislike and a WTF reaction on every post, plus threaded comments with replies."),
   ("🔒","Public & Private Groups","Spin up invite-only groups (token links) or open public ones for your community."),
   ("💬","Real-Time DMs","Direct messages delivered live over SocketIO, with notifications for reactions, comments, follows and DMs."),
   ("🔎","Explore & Search","An explore page and search across both users and posts to find people and topics."),
   ("🛠️","Admin Panel","User management, post moderation, open/invite-only registration toggle and invite-token generation."),
 ],
 "specs":[
   ("Stack","Flask + SQLAlchemy/SQLite + Flask-SocketIO (eventlet), Bootstrap 5"),
   ("Posts","Text/image/video, visibility public/friends/group"),
   ("Social","Reactions, threaded comments, follow/unfollow, real-time DMs"),
   ("Admin","Ban/unban/delete/make-admin, moderation, invite tokens"),
   ("Run","python run.py → http://127.0.0.1:5000"),
 ],
 "requirements":"Default admin <code>admin / admin123</code>.",
 "download":"Hotspot source · free · self-hosted",
},
{
 "slug":"inspire-arts-crm", "name":"Inspire Arts CRM", "icon":"💼",
 "category":"Web Platforms",
 "tagline":"Customers, commissions, invoicing and finance in one CRM.",
 "platform":"Web · Self-host", "anim":"orbit", "accent":("#6E48B0","#C9A840","#9D5BFF"),
 "badges":["Self-hosted","Multi-account","PDF invoices"],
 "footline":"run the whole business.",
 "intro":"A complete CRM and finance system built for a real arts business — "
         "<strong>customers, commissions, invoicing, payment schedules and full finance "
         "reporting</strong>, with a multi-account architecture that keeps each business or "
         "household in its own database.",
 "features":[
   ("👤","Customers & Commissions","Full customer records and contacts, plus a commission pipeline with a kanban board, PDF quotes and file attachments."),
   ("🧾","Sales & Invoices","Generate PDF invoices with VAT, discount and shipping; track Pending/Paid/Overdue/Refunded across eleven sales channels."),
   ("🔁","Payment Schedules","Recurring plans (weekly to annual) with one-click “Log Payment” that creates the invoice and advances the next date."),
   ("💷","Business & Home Finance","Non-customer finance entries (grants, loans, transfers) and a complete home-finance module with budgets and custom fields."),
   ("📊","Charts Everywhere","Revenue by month, commission status, top customers, payment totals and sales-channel breakdowns — all on Chart.js."),
   ("🔐","Multi-Account & Roles","A master auth DB plus per-account databases, account switching, and role decorators for business vs home views."),
 ],
 "specs":[
   ("Stack","Flask + SQLite (per-account DBs) + Waitress, Bootstrap 5, Chart.js"),
   ("CRM","Customers, contacts, commissions (kanban), PDF quotes/invoices, attachments"),
   ("Finance","Sales channels, payment schedules, business + home finance, budgets"),
   ("Branding","Purple #4A2C6E / gold #C9A840"),
   ("Run","Desktop launcher → http://localhost:5000 (LAN-accessible)"),
 ],
 "requirements":"Runs on 0.0.0.0:5000 — reachable from any device on the same Wi-Fi. "
                "cloudflared is bundled for later internet exposure.",
 "download":"Inspire Arts CRM source · self-hosted",
},

# ============================================================ GAMES & SCREENSAVERS
{
 "slug":"spot", "name":"Spot!", "icon":"🐕",
 "category":"Games & Screensavers",
 "tagline":"A 2D dog-walking game — keep Spot happy and out of trouble.",
 "platform":"Windows Game", "anim":"particles", "accent":("#39FF6E","#7FB2FF","#FFB13B"),
 "badges":["Windows 10 / 11","Open world","Pure Pygame"],
 "footline":"good boy.",
 "intro":"A hand-drawn dog-walking game built in pure Pygame. Walk Spot through home, park and "
         "neighbourhood, <strong>manage five needs</strong>, teach twelve commands, and clean up "
         "after him before the bin — all rendered with anti-aliased vector art.",
 "features":[
   ("🌳","Scrolling Open World","Roam a 3072×1590 world across three connected scenes — Home & Backyard, Park and Neighbourhood — with a camera that tracks you."),
   ("📊","Five Needs to Balance","Food, water, energy, happiness and bladder all tick down — let two bottom out and it's game over."),
   ("🎯","Twelve Commands","Fetch, Sit, Stay, Lay, Stand, Run, Here, Pet, Good Boy, Wee, and step left/right — Spot has a full state machine."),
   ("💩","Wee, Waste & Bin","Bladder fills over time; send Spot to a tree, pick up the waste, and bin it for points."),
   ("🐩","A World of Characters","Ten dog breeds, joggers, children, the elderly, cyclists, squirrels and cars all share the streets."),
   ("🖼️","Vector Art","Everything is drawn with pygame.gfxdraw anti-aliased vectors — no external assets, crisp at any size."),
 ],
 "specs":[
   ("Engine","Python 3.12 + Pygame 2.6.1 (single file, no assets)"),
   ("World","3072×1590, three scenes, camera tracking"),
   ("Stats","Food, water, energy, happiness, bladder"),
   ("Commands","12 — Fetch/Sit/Stay/Lay/Stand/Run/Here/Pet/GoodBoy/Wee/Left/Right"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"Spot_Setup.exe · free · Windows 10/11",
},
{
 "slug":"spot-3d", "name":"Spot! 3D", "icon":"🎮",
 "category":"Games & Screensavers",
 "tagline":"The dog-walk reborn in Godot 4 — day/night, water, real models.",
 "platform":"Windows Game", "anim":"orbit", "accent":("#39FF6E","#33E0FF","#3A86FF"),
 "badges":["Windows 10 / 11","Godot 4","Day/night cycle"],
 "footline":"walk the dog in 3D.",
 "intro":"Spot reborn as a full 3D game in Godot 4. A seamless open world with a "
         "<strong>live day/night cycle</strong>, animated water, swaying grass, real Kenney and "
         "Quaternius models, and an in-game character creator — third-person, with the same "
         "twelve commands.",
 "features":[
   ("🌍","Seamless Open World","One continuous 300-unit world — Home, Park and Neighbourhood — no loading screens, with a third-person orbit camera."),
   ("🌅","Live Day/Night Cycle","A moving sun, atmospheric sky and volumetric fog shift in real time, with a live clock in the HUD."),
   ("💧","Shaders & Effects","Animated water with fresnel and foam, PBR ground and road, 3,000 wind-swayed grass blades, SSAO/SSIL/SSR and colour grading."),
   ("🧍","Character Creator","Customise skin, hair, jacket, trousers and shoes — or play as the skinned Mixamo “James” model."),
   ("🐾","Detailed Spot","A fully procedural, animated Rough Collie — tricolour coat, semi-erect ears, wagging tail — with all twelve commands."),
   ("🚦","A Living Town","Nineteen NPCs with real animal models, twelve vehicles on lane-following traffic, and three-phase animated traffic lights."),
 ],
 "specs":[
   ("Engine","Godot 4.6.3 Forward+ (non-Mono)"),
   ("Graphics","SSAO/SSIL/SSR, PhysicalSky, volumetric fog, 16k shadow atlas, custom shaders"),
   ("Assets","Kenney environment + Quaternius characters/animals, PolyHaven PBR textures"),
   ("World","300×300 units, Home/Park/Neighbourhood zones, day/night"),
   ("Platform","Windows 10 / 11 (open in Godot or run the build)"),
 ],
 "download":"Spot_3D (Godot project + build) · free · Windows 10/11",
},
{
 "slug":"spot-vue", "name":"Spot vUE", "icon":"🏙️",
 "category":"Games & Screensavers",
 "tagline":"A GTA-style open city dog-walk in Unreal Engine 5.",
 "platform":"Windows Game", "anim":"orbit", "accent":("#FFB13B","#FF5555","#3A86FF"),
 "badges":["Windows 10 / 11","Unreal Engine 5.7","C++ gameplay"],
 "footline":"big city, good dog.",
 "intro":"The most ambitious Spot yet — a <strong>GTA-style open city</strong> built in Unreal "
         "Engine 5.7 with C++ gameplay. Thousands of imported assets, skeletal-mesh dogs and "
         "pedestrians, traffic, a day/night city and a runtime world builder.",
 "features":[
   ("🌆","Runtime City World","A C++ world builder assembles the entire city at runtime — house and garden, main road, pavements, lamp posts, a park and a pond."),
   ("🐕","Skeletal-Mesh Spot","Spot is a real skeletal mesh (ShibaInu/Husky/Wolf/Fox by breed) driven by an anim instance for idle, walk, run and jump."),
   ("🚗","Traffic & Pedestrians","Kenney vehicles drive the lanes while Quaternius skeletal NPCs walk the pavements."),
   ("🎾","Ball, Frisbee & Fetch","Throw a physics ball or a ballistic frisbee and Spot fetches; pet him, praise him, bin his waste."),
   ("🌃","Day/Night City","Lamp posts light up on a day/night cycle across a city of modular buildings and skyscrapers."),
   ("🧩","3,000+ Assets","Animals, NPCs, trees, modular buildings, a roads kit and mini-characters — all imported and wired to C++."),
 ],
 "specs":[
   ("Engine","Unreal Engine 5.7.4, C++ gameplay"),
   ("World","Runtime-built city — house, roads, park, traffic, pedestrians"),
   ("Spot","Skeletal mesh per breed + anim instance"),
   ("Controls","WASD + mouse, run/jump, fetch (ball/frisbee), Spot commands"),
   ("Platform","Windows 10 / 11 (packaged build)"),
 ],
 "download":"SpotVUE packaged game · free · Windows 10/11",
},
{
 "slug":"pong", "name":"Pong", "icon":"🏓",
 "category":"Games & Screensavers",
 "tagline":"1972-style Pong that doubles as a Windows screensaver.",
 "platform":"Windows Game", "anim":"waveform", "accent":("#39FF6E","#33E0FF","#39FF6E"),
 "badges":["Windows 10 / 11","1P / 2P / Demo","Installs as .scr"],
 "footline":"the original, reborn.",
 "intro":"A faithful, 1972-style Pong — and a working Windows screensaver. Play one-player "
         "versus AI, two-player local, or let the <strong>AI-vs-AI demo</strong> run as your "
         "idle screen.",
 "features":[
   ("🤖","Three Modes","Demo (AI vs AI), 1 Player vs AI with W/S, and 2 Players local with W/S and the arrow keys."),
   ("🖥️","Real Screensaver","Installs as a .scr and honours the Windows /s, /c and /p screensaver arguments."),
   ("🔲","Fullscreen by Default","Launches fullscreen, with F11 to toggle a window at any time."),
   ("🔊","Synthesised Sound","Classic blips generated from raw buffers — no sound files needed."),
   ("🪟","Menu From Demo","Press any key in the demo to open the mode-select menu; Esc drops back to the screensaver."),
 ],
 "specs":[
   ("Engine","Python 3.12 + Pygame 2.6.1 (single file)"),
   ("Modes","Demo · 1 Player · 2 Players"),
   ("Screensaver","Installs to System32 as .scr, supports /s /c /p"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"Pong_Setup.exe / pong.scr · free · Windows 10/11",
},
{
 "slug":"virtual-pet", "name":"Virtual Pet", "icon":"🐉",
 "category":"Games & Screensavers",
 "tagline":"A 3D desktop pet and screensaver — fish, dog, cat or dragon.",
 "platform":"Windows", "anim":"particles", "accent":("#33E0FF","#C77DFF","#39FF6E"),
 "badges":["Windows 10 / 11","3D screensaver","Transparent desktop pet"],
 "footline":"a little life on your desktop.",
 "intro":"A virtual pet that lives as a <strong>3D screensaver</strong> or a transparent "
         "creature on your desktop. Choose a fish, dog, cat or dragon — each with its own scene, "
         "stats, day/night cycle and ways to play.",
 "features":[
   ("🐟","Four Pets, Four Worlds","A fish in an aquarium, a dog in a yard, a cat in a living room, a dragon in a cave — each its own 3D environment."),
   ("🖱️","Real Interactions","Feed the fish, throw a ball for the dog, tease the cat with a laser dot, make the dragon breathe fire."),
   ("🌗","Stats & Day/Night","Each pet has decaying stats and lives under a day/night cycle with per-scene fog and lighting."),
   ("🖼️","Transparent Desktop Mode","A 2D mode renders the pet directly on your desktop with click-through, so it wanders over your work."),
   ("🎬","Cinematic Screensaver","In screensaver mode a slow camera pans the 3D scene; install it as a .scr to use system-wide."),
   ("🔊","Procedural Sound","Sounds are generated in numpy — no audio assets to ship."),
 ],
 "specs":[
   ("3D mode","Ursina (Panda3D) — lighting, shadows, fog"),
   ("2D desktop pet","Pygame + transparent layered window (click-through)"),
   ("Pets","Fish · Dog · Cat · Dragon"),
   ("Install","python main.py /s, or install.bat for a .scr"),
   ("Platform","Windows 10 / 11"),
 ],
 "download":"VirtualPet_Setup.exe · free · Windows 10/11",
},
{
 "slug":"digital-clock-screensaver", "name":"Digital Clock Screensaver", "icon":"🕒",
 "category":"Games & Screensavers",
 "tagline":"Matrix rain behind a big, configurable clock.",
 "platform":"Windows", "anim":"matrix", "accent":("#39FF6E","#33E0FF","#39FF6E"),
 "badges":["Windows 10 / 11","3D Matrix rain","Store-ready"],
 "footline":"time, falling like code.",
 "intro":"A screensaver that drops <strong>3D perspective Matrix rain</strong> behind a clean, "
         "full-screen clock. Katakana, Latin and digits stream past the time, day and date — "
         "fully configurable, and packaged ready for the Microsoft Store.",
 "features":[
   ("🌧️","3D Matrix Rain","Perspective katakana, Latin and digit rain streams toward you behind the clock overlay."),
   ("🕰️","Full-Screen Clock","Time, day and date front and centre, in 24-hour or 12-hour format with optional seconds."),
   ("🎨","Eight Colour Modes","Cycle through hues or fix one of eight presets, with adjustable rain speed, density and panel opacity."),
   ("🔑","Password Protection","Optionally require a password to dismiss the screensaver."),
   ("⚙️","Live Settings","Press S while running to open settings without leaving the screensaver."),
   ("🪟","Proper Screensaver","Supports the Windows /s, /c and /p arguments and ships with an Inno Setup installer."),
 ],
 "specs":[
   ("Engine","Python 3.12 + Pygame + tkinter settings"),
   ("Rain","3D perspective katakana + Latin + digits"),
   ("Clock","12/24h, seconds, day, date"),
   ("Options","8 colour presets, speed/density, opacity, password"),
   ("Platform","Windows 10 / 11 (.scr + installer + Store assets)"),
 ],
 "price":"£3 · one-time",
 "download":"DigitalClock_Setup.exe / DigitalClock.scr · £3 one-time · Windows 10/11",
},

# ============================================================ MOBILE
{
 "slug":"picdraw-grid", "name":"PicDraw Grid", "icon":"🖼️",
 "category":"Mobile",
 "tagline":"Drawing-reference grids and B&W passes, on your phone — pay once, no subscription.",
 "platform":"Android", "anim":"orbit", "accent":("#FF5555","#FFB13B","#C77DFF"),
 "badges":["Pay once — no subscription","Native · offline","Android 10+"],
 "footline":"reference in your pocket.",
 "intro":"The pocket edition of the PicDraw idea — a native Android viewer that overlays accurate "
         "<strong>drawing grids and black-and-white passes</strong> on any photo, with immersive "
         "full-screen viewing tuned for high-res Galaxy images.",
 "features":[
   ("📁","Albums → Gallery → Viewer","Browse albums, then a gallery grid, then a swipeable full-screen viewer powered by SubsamplingScaleImageView for huge images."),
   ("🔲","Four Grid Types","Rule of Thirds, Custom, Pixel Grid and Golden Ratio — with colour, opacity, thickness and a closed border."),
   ("🎚️","B&W Effects","Hardware-accelerated ColorMatrix B&W with five presets plus brightness, contrast, R/G/B mix and grain."),
   ("⛶","Immersive Full Screen","A full-screen button hides all chrome, keeps the screen awake, and auto-hides controls after four seconds."),
   ("🔍","Pinch to Zoom","Native pinch-zoom on high-resolution images without running out of memory."),
   ("💾","Save a Copy","Export a gridded copy straight to Pictures/PicDrawGrid via MediaStore."),
 ],
 "specs":[
   ("Platform","Native Android (Kotlin), minSdk 29 (Android 10)"),
   ("Grids","Thirds · Custom · Pixel · Golden Ratio + closed border (3px default)"),
   ("B&W","ColorMatrix, 5 presets + sliders, hardware layer"),
   ("Viewer","SubsamplingScaleImageView, immersive full screen, auto-hide"),
   ("Tested on","Samsung Galaxy S20"),
 ],
 "price":"£3 · one-time",
 "download":"PicDrawGrid.apk · £3 one-time · no subscription · Android 10+",
},
{
 "slug":"skale", "name":"Skale", "icon":"⚖️",
 "category":"Mobile",
 "tagline":"Weigh small objects using your phone's touchscreen.",
 "platform":"Android", "anim":"spectrum", "accent":("#33E0FF","#39FF6E","#3A86FF"),
 "badges":["Android 8+","Touchscreen sensing","Coin auto-calibration"],
 "footline":"the scale in your pocket.",
 "intro":"A genuinely clever experiment: a scale that weighs objects by reading the "
         "<strong>capacitive contact area</strong> of the touchscreen. Place a coin or a key on "
         "the glass and Skale maps the contact ellipse to grams in real time.",
 "features":[
   ("📐","Contact-Area Sensing","Maps each touch point's major/minor axes to an ellipse area, summing all simultaneous contacts into a live weight."),
   ("🪙","18-Coin Auto-Calibration","Calibrate instantly by placing a known coin from a picker of 18 common UK, US, EU and AU coins — or type an exact gram value."),
   ("🟢","Live Readout","A monospace green display shows grams immediately, with STABLE/MEASURING status and visible contact ellipses."),
   ("⚖️","Tare & Zero","Tare and zero buttons let you weigh on top of a container, just like a real scale."),
   ("🔧","Auto or Precise","A DPI-based default means numbers show on first run; calibrate for precision and the label switches AUTO → CALIBRATED."),
 ],
 "specs":[
   ("Platform","Native Android (Kotlin), minSdk 26"),
   ("Method","Touch contact ellipse area (π·major·minor/4) → grams"),
   ("Calibration","18-coin picker or manual grams, RESET TO AUTO"),
   ("Note","Capacitive screens only sense conductive objects (coins, cutlery, water)"),
   ("Tested on","Samsung Galaxy S20"),
 ],
 "download":"Skale.apk · free · Android 8+",
},
{
 "slug":"talktime", "name":"TalkTime", "icon":"🗣️",
 "category":"Mobile",
 "tagline":"A gentle speech-therapy companion for children.",
 "platform":"Android", "anim":"particles", "accent":("#FF5DA2","#FFB13B","#33E0FF"),
 "badges":["Android 8+","4 exercises","Progress charts"],
 "footline":"every word counts.",
 "intro":"A speech-therapy aid for children, built around <strong>four playful exercises</strong> "
         "that adapt to each child's age. Text-to-speech models the words, the child records and "
         "plays back, and a PIN-locked admin panel tracks progress over time.",
 "features":[
   ("🖼️","Picture Words","Ten questions per round — tap the correct word for an emoji while TTS reads it aloud."),
   ("🎤","Repeat After Me","TTS plays a phrase, the child records themselves and plays it back to compare."),
   ("🔤","Letter Sounds","Random letters with a phonetic tip, a mouth cue and an example word, voiced by TTS."),
   ("📖","Story Time","Three emoji story scenes per session; TTS reads the prompt and the child records an answer."),
   ("⭐","Encouraging Results","Each session ends with a score, a percentage, a 1–3 star rating and a kind message."),
   ("🔐","Admin & Progress","A PIN-locked panel manages child profiles and charts progress per exercise with MPAndroidChart."),
 ],
 "specs":[
   ("Platform","Native Android (Kotlin), Room/SQLite, minSdk 26"),
   ("Exercises","Picture Words · Repeat After Me · Letter Sounds · Story Time"),
   ("Age groups","Toddler · Early · Primary (vocabulary scales by age)"),
   ("Admin","PIN-locked (default 1234), progress LineCharts"),
   ("Tested on","Samsung Galaxy S20"),
 ],
 "download":"TalkTime.apk · free · Android 8+",
},
]
