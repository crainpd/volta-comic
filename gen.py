import urllib.request, urllib.parse, time, os
os.chdir(os.path.expanduser('~/volta-comic'))
STYLE = " Bold clean comic-book ink linework, flat vibrant cel-shaded colors, all-ages kids comic style, no text, no watermark."
imgs = {
 "01_volta_character_sheet": ("Superhero character design sheet, full body front view. VOLTA: young woman mid-20s, brown skin, dark curly hair with one glowing white streak. Deep navy fitted suit with thin glowing cyan circuit-board trace lines on arms, chest and legs, short cape, fingerless gloves with glowing fingertips. No mask, confident friendly smile. Open hands with soft cyan electric arcs. Plain light grey background." + STYLE, 1024, 1280, 11),
 "02_volta_and_echo_twin": ("Superhero VOLTA (young woman, brown skin, dark curly hair with white streak, navy suit with glowing cyan circuit lines) stands facing viewer. Beside her floats ECHO, her translucent digital twin: an identical figure made entirely of glowing cyan light and circuit traces, hologram-like. A thin thread of light connects their temples. Dark blue lab background, awe and wonder mood." + STYLE, 1280, 1024, 22),
 "03_origin_lab": ("Origin scene in a high-tech lab: a giant glowing brain-shaped machine made of crystal and circuitry lights up in the center. Three scientists in lab coats stare amazed. Foreground: a young woman with brown skin and curly dark hair touches her temple as every screen, light and monitor in the room blazes bright cyan at once, cables glowing. Dramatic wide shot." + STYLE, 1280, 768, 33),
 "04_blackout_action": ("Superhero VOLTA (young woman, navy suit with glowing cyan circuit lines, dark curly hair with white streak, short cape) hovers above a dark blacked-out city at night, arms raised wide. A wave of light spreads outward from her as streetlights, windows and neon signs turn back on block by block. Children cheer on a rooftop below. Dynamic low angle, epic wide shot." + STYLE, 1280, 768, 44),
 "05_villain_glitch": ("Cute mischievous cartoon villain GLITCH: a small round blob creature made of flickering TV static and broken pixel blocks, two big mischievous yellow eyes, wide grin, little arms. He sits on top of a flickering traffic light at night, zapping it with tiny sparks. Funny and playful, not scary, for young kids. Dark blue night background." + STYLE, 1024, 1024, 55),
 "06_cover_issue1": ("Comic book cover. Superhero VOLTA (young woman, brown skin, dark curly hair with white streak, navy suit with glowing cyan circuit lines, short cape) leaps toward the viewer, hands crackling with cyan lightning. Behind her a giant translucent glowing cyan twin figure made of circuit light looms over a city skyline at dusk. A small static-blob creature peeks in from the corner grinning. Big empty space at top for title. Dynamic, bold, kid-friendly." + STYLE, 1024, 1344, 66),
}
for name,(prompt,w,h,seed) in imgs.items():
    url = "https://image.pollinations.ai/prompt/" + urllib.parse.quote(prompt) + f"?width={w}&height={h}&seed={seed}&model=flux&nologo=true&enhance=false"
    ok=False
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
            data = urllib.request.urlopen(req, timeout=180).read()
            if len(data) > 20000:
                open(f"{name}.jpg","wb").write(data); print(name, len(data), flush=True); ok=True; break
            print(name, "small", len(data), flush=True)
        except Exception as e:
            print(name, "err", e, flush=True)
        time.sleep(8)
    if not ok: print(name, "FAILED", flush=True)
print("DONE", flush=True)
