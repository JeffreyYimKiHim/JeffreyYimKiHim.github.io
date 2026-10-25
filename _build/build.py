#!/usr/bin/env python3
"""
Jeffrey Yim — site builder.
Scans content/<section>/*.md, renders each to essays/<section>/<slug>.html,
and regenerates index.html. Run by GitHub Actions on every commit; you can
also run it locally with:  python _build/build.py   (needs: pip install markdown)

A post file looks like:

    ---
    title: My Essay Title
    date: 2026-10-25
    tag: Optional Tag
    summary: One-line teaser shown on the homepage.
    status: published        <- or "draft" to hide it from the site
    ---

    Markdown body here...
"""
import re
from pathlib import Path
from datetime import date

import markdown

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
ESSAYS = ROOT / "essays"
HOME_HTML = ROOT / "_build" / "home.html"

SECTIONS = [
    ("aftermath",    "Ideas",  "Post-mortems of non-mainstream trade ideas — thesis, expression, outcome, lesson. The P&amp;L is the least interesting number."),
    ("ai-investing", "AI-Investing",     "Where AI actually helps an investor implements."),
    ("journal",      "Review",   "If I can't write down what would prove me wrong, I don't have a thesis."),
    ("apps",         "Beyond Investing",  "Shark Tank Ideas!"),
    ("thoughts",     "Personal Thoughts", ""),
]

MONTHS = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

CSS = """
:root {
    --serif-font: 'Spectral', Georgia, serif;
    --sans-font: 'Jost', 'Helvetica Neue', Helvetica, sans-serif;
    --dark-text-color: rgb(148, 148, 148);
    --bullet-color: rgb(184, 184, 184);
    --link-color: #52525b;
    --link-background-color: #9191a07f;
    --background-color: white;
    --subtle-background-darker: rgb(252, 248, 243);
    --border-background-color: #e0e0e0;
    --code-background-color: rgb(245, 245, 245);
    --color: black;
    --nav-bg: rgba(255, 255, 255, 0.55);
    --particle-color: rgba(120, 120, 135, 0.35);
}
@media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
        --dark-text-color: #949494;
        --bullet-color: rgb(90, 90, 90);
        --background-color: #121212;
        --subtle-background-darker: rgb(23, 23, 23);
        --border-background-color: #3b3d3e;
        --code-background-color: #242424;
        --link-background-color: #6b6b6b;
        --link-color: rgb(161, 161, 161);
        --color: rgb(200, 200, 200);
        --nav-bg: rgba(18, 18, 18, 0.55);
        --particle-color: rgba(140, 140, 150, 0.28);
    }
}
html[data-theme="dark"] {
    --dark-text-color: #949494;
    --bullet-color: rgb(90, 90, 90);
    --background-color: #121212;
    --subtle-background-darker: rgb(23, 23, 23);
    --border-background-color: #3b3d3e;
    --code-background-color: #242424;
    --link-background-color: #6b6b6b;
    --link-color: rgb(161, 161, 161);
    --color: rgb(200, 200, 200);
    --nav-bg: rgba(18, 18, 18, 0.55);
    --particle-color: rgba(140, 140, 150, 0.28);
}
* { box-sizing: border-box; }
body {
    background-color: var(--background-color);
    color: var(--color);
    font-family: var(--serif-font);
    font-size: 17.5px;
    line-height: 1.6;
    margin: 0; padding: 0;
    text-align: left;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    transition: background-color 0.35s ease, color 0.35s ease;
}
#field { position: fixed; inset: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; }
.container { max-width: 650px; margin: 0 auto; padding: 20px 20px 40px 20px; position: relative; z-index: 1; }
.site-nav-wrapper {
    position: sticky; top: 0; z-index: 1000;
    -webkit-backdrop-filter: saturate(180%) blur(8px);
    backdrop-filter: saturate(180%) blur(8px);
    background-color: var(--nav-bg);
    transition: background-color 0.35s ease;
}
.site-nav-inner { max-width: 650px; margin: 0 auto; padding: 18px 20px; display: flex; align-items: baseline; justify-content: space-between; gap: 1em; }
.site-name { font-family: var(--sans-font); font-weight: 500; font-size: 15px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--color); text-decoration: none; border-bottom: none; }
.site-nav { display: flex; align-items: baseline; gap: 1.15em; flex-wrap: wrap; justify-content: flex-end; }
.site-nav a { font-family: var(--sans-font); font-size: 13.5px; color: var(--link-color); text-decoration: none; border-bottom: none; position: relative; }
.site-nav a::after { content: ""; position: absolute; left: 0; bottom: -2px; width: 100%; height: 1px; background: var(--color); transform: scaleX(0); transform-origin: left; transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1); }
.site-nav a:hover::after { transform: scaleX(1); }
#theme-toggle { background: none; border: none; cursor: pointer; font-family: var(--sans-font); font-size: 14px; color: var(--link-color); padding: 0 0 0 0.4em; line-height: 1; transition: transform 0.4s ease, color 0.3s ease; }
#theme-toggle:hover { transform: rotate(30deg); color: var(--color); }
h1, h2, h3 { font-family: var(--sans-font); font-weight: 500; }
h1 { font-size: 1.9em; font-weight: 400; letter-spacing: -0.01em; margin: 0.2em 0 0.6em 0; }
h2 { font-size: 13px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; color: var(--dark-text-color); margin: 3.2em 0 1.1em 0; display: flex; align-items: center; gap: 0.9em; }
h2::after { content: ""; flex: 1; height: 1px; background: var(--border-background-color); }
h3 { font-size: 1.05em; margin: 0 0 0.15em 0; font-weight: 500; }
p { margin: 0.6em 0; }
.lede { font-size: 1.06em; }
.dim { color: var(--dark-text-color); }
.small { font-size: 0.86em; }
a { font-weight: 400; text-decoration: none; color: var(--link-color); border-bottom: 0.1em solid var(--link-background-color); transition: all 0.3s; }
a:hover { border-bottom: 0.1em solid var(--color); }
blockquote { font-style: italic; background-color: var(--code-background-color); padding: 6px 20px; margin: 1.4em 0; border-left: 2px solid var(--border-background-color); border-radius: 8px; }
ul { list-style-type: none; padding-left: 0; }
ul > li { position: relative; padding-left: 1.2em; margin-bottom: 0.55em; }
ul > li::before { content: "\\2022"; color: var(--bullet-color); position: absolute; left: 0; top: 0.1em; font-size: 30px; line-height: 1; }
ol { padding-left: 1.4em; }
ol > li { margin-bottom: 0.7em; }
ol > li::marker { color: var(--bullet-color); }
.beliefs-list { column-count: 2; column-gap: 2rem; }
.beliefs-list li { break-inside: avoid; }
@media (max-width: 640px) { .beliefs-list { column-count: 1; } }
.entry { margin-bottom: 1.6em; }
.entry .meta { font-family: var(--sans-font); font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--dark-text-color); margin-bottom: 0.25em; }
.entry .tag { display: inline-block; font-family: var(--sans-font); font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--dark-text-color); border: 1px solid var(--border-background-color); border-radius: 3px; padding: 1px 7px; margin-left: 0.6em; vertical-align: 1px; }
.entry p { margin: 0.35em 0 0 0; }
article .meta { font-family: var(--sans-font); font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--dark-text-color); margin: 0.4em 0 1.6em 0; }
article h2 { font-size: 1.25em; letter-spacing: 0; text-transform: none; color: var(--color); margin: 1.8em 0 0.5em 0; display: block; }
article h2::after { content: none; }
article h3 { font-size: 1.05em; margin: 1.4em 0 0.3em 0; }
article p { margin: 0.8em 0; }
article code { font-family: 'SFMono-Regular', Consolas, monospace; font-size: 0.88em; background: var(--code-background-color); padding: 2px 6px; border-radius: 4px; }
article img { max-width: 100%; border-radius: 6px; }
article hr { border: none; height: 1px; background: var(--border-background-color); margin: 2.2em 0; }
.back-link { font-family: var(--sans-font); font-size: 13px; letter-spacing: 0.06em; border-bottom: none; color: var(--dark-text-color); }
.back-link:hover { color: var(--color); border-bottom: none; }
footer { margin-top: 5em; padding-top: 1.4em; border-top: 1px solid var(--border-background-color); font-family: var(--sans-font); font-size: 13px; color: var(--dark-text-color); display: flex; justify-content: space-between; flex-wrap: wrap; gap: 1em; }
footer a { font-size: 13px; }
.fade-up { opacity: 0; transform: translateY(1rem); transition: opacity 1.1s cubic-bezier(.22, 1, .36, 1), transform 1.1s cubic-bezier(.22, 1, .36, 1); }
.fade-up.seen { opacity: 1; transform: translateY(0); }
@media (prefers-reduced-motion: reduce) { .fade-up { opacity: 1; transform: none; transition: none; } }
@media (max-width: 768px) { body { font-size: 16.5px; } .site-nav-inner { padding: 14px 20px; } .site-nav { gap: 0.85em; } }
"""

THEME_JS = """(function(){var b=document.getElementById('theme-toggle');
function d(){var h=document.documentElement;var m=window.matchMedia('(prefers-color-scheme: dark)').matches;
var dk=h.getAttribute('data-theme')==='dark'||(!h.hasAttribute('data-theme')&&m&&localStorage.getItem('theme')!=='light');
b.textContent=dk?'\\u25d1':'\\u25d0';}
b.addEventListener('click',function(){var h=document.documentElement;
var m=window.matchMedia('(prefers-color-scheme: dark)').matches;
var cur=h.hasAttribute('data-theme')?(h.getAttribute('data-theme')==='dark'):m;
if(cur){h.setAttribute('data-theme','light');localStorage.setItem('theme','light');}
else{h.setAttribute('data-theme','dark');localStorage.setItem('theme','dark');}d();});
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change',d);d();})();"""

FADE_JS = """(function(){var els=document.querySelectorAll('.fade-up');
if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('seen');});return;}
var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('seen');io.unobserve(x.target);}});},{threshold:0.08});
els.forEach(function(e){io.observe(e);});})();"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='0.9em' font-size='90'>&#9670;</text></svg>">
<script>(function(){{try{{var t=localStorage.getItem('theme');if(t==='dark'){{document.documentElement.setAttribute('data-theme','dark');}}else if(t==='light'){{document.documentElement.removeAttribute('data-theme');}}}}catch(e){{}}}})();</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,100..900;1,100..900&family=Spectral:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>"""

NAV = """
<div class="site-nav-wrapper">
    <div class="site-nav-inner">
        <a class="site-name" href="/">Jeffrey Yim</a>
        <nav class="site-nav">
            <a href="/#aftermath">Ideas</a>
            <a href="/#ai-investing">AI-Investing</a>
            <a href="/#journal">Review</a>
            <a href="/#apps">Beyond Investing</a>
            <a href="/#thoughts">Thoughts</a>
            <button id="theme-toggle" aria-label="Toggle dark mode">&#9680;</button>
        </nav>
    </div>
</div>
"""

FOOTER = """
    <footer>
        <span>&copy; 2026 Jeffrey Yim</span>
        <span>
            <a href="mailto:yimkihimjeffrey@gmail.com">Email</a> &middot;
            <a href="https://www.linkedin.com/in/yimkihimjeffrey" target="_blank" rel="noopener">LinkedIn</a> &middot;
            <a href="/Jeffrey_Yim_CV.pdf" target="_blank" rel="noopener">CV</a>
        </span>
    </footer>
"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def parse_post(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.lstrip().startswith("---"):
        parts = text.lstrip().split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip().lower()] = v.strip()
            body = parts[2]
    return meta, body


def fmt_date(iso, style="short"):
    try:
        y, m, d = (int(x) for x in iso.split("-"))
        if style == "short":
            return f"{MONTHS[m]} {y}"
        return f"{d} {MONTHS[m]} {y}"
    except Exception:
        return iso


def load_posts():
    """Returns {section_key: [post, ...]} sorted newest first."""
    posts = {}
    for key, _, _ in SECTIONS:
        folder = CONTENT / key
        entries = []
        if folder.is_dir():
            for md_file in sorted(folder.glob("*.md")):
                meta, body = parse_post(md_file)
                if meta.get("status", "published").lower() != "published":
                    continue
                entries.append({
                    "slug": md_file.stem,
                    "section": key,
                    "title": meta.get("title", md_file.stem.replace("-", " ").title()),
                    "date": meta.get("date", ""),
                    "tag": meta.get("tag", ""),
                    "summary": meta.get("summary", ""),
                    "body": body,
                })
        entries.sort(key=lambda p: p["date"], reverse=True)
        posts[key] = entries
    return posts


def render_essay(post, section_name):
    body_html = markdown.markdown(post["body"], extensions=["extra", "sane_lists"])
    meta_bits = []
    if post["date"]:
        meta_bits.append(fmt_date(post["date"], "long"))
    meta_bits.append(section_name)
    if post["tag"]:
        meta_bits.append(post["tag"])
    html_doc = HEAD.format(title=esc(post["title"]) + " — Jeffrey Yim",
                           desc=esc(post["summary"] or post["title"]), css=CSS)
    html_doc += NAV
    html_doc += '<div class="container">\n    <article class="fade-up seen">\n'
    html_doc += f'        <p><a class="back-link" href="/#{post["section"]}">&larr; {esc(section_name)}</a></p>\n'
    html_doc += f"        <h1>{esc(post['title'])}</h1>\n"
    html_doc += f'        <div class="meta">{" &middot; ".join(meta_bits)}</div>\n'
    html_doc += "        " + body_html.replace("\n", "\n        ") + "\n"
    html_doc += "    </article>\n"
    html_doc += FOOTER + "</div>\n"
    html_doc += f"<script>{THEME_JS}</script>\n</body>\n</html>\n"
    return html_doc


def entry_html(post):
    tag = f'<span class="tag">{esc(post["tag"])}</span>' if post["tag"] else ""
    date = fmt_date(post["date"]) if post["date"] else ""
    url = f'/essays/{post["section"]}/{post["slug"]}.html'
    return f'''        <div class="entry">
            <div class="meta">{esc(date)}</div>
            <h3><a href="{url}">{esc(post["title"])}</a>{tag}</h3>
            <p class="dim">{esc(post["summary"])}</p>
        </div>'''


def render_home(posts, home_html):
    doc = HEAD.format(title="Jeffrey Yim", desc="Jeffrey Yim — multi-asset execution trader. AI-augmented investing, market microstructure, app blueprints, and trade aftermaths.", css=CSS)
    doc += '<canvas id="field"></canvas>\n'
    doc += NAV
    doc += '<div class="container" id="top">\n\n'
    doc += home_html.strip() + "\n\n"

    section_names = {k: n for k, n, _ in SECTIONS}
    for key, name, blurb in SECTIONS:
        doc += f'    <!-- ============ {name.upper()} ============ -->\n'
        doc += f'    <section class="fade-up" id="{key}">\n'
        doc += f"        <h2>{esc(name)}</h2>\n"
        if blurb:
            doc += f'        <p class="dim small">{blurb}</p>\n\n'
        entries = posts.get(key, [])
        if entries:
            doc += "\n\n".join(entry_html(p) for p in entries) + "\n"
        else:
            doc += '        <div class="entry">\n            <div class="meta">&nbsp;</div>\n'
            doc += '            <h3>Nothing here yet</h3>\n'
            doc += f'            <p class="dim">First entry coming soon.</p>\n        </div>\n'
        doc += "    </section>\n\n"

    doc += FOOTER + "</div>\n"
    doc += f"<script>{THEME_JS}</script>\n<script>{FADE_JS}</script>\n"

    # Particle field (homepage only)
    doc += """<script>
(function(){var c=document.getElementById('field');if(!c)return;var x=c.getContext('2d');
var dpr=Math.min(window.devicePixelRatio||1,2),W,H,dots=[],px=-9999,py=-9999,N=42;
function rs(){W=c.width=innerWidth*dpr;H=c.height=innerHeight*dpr;c.style.width=innerWidth+'px';c.style.height=innerHeight+'px';}
function sd(){dots=[];for(var i=0;i<N;i++){dots.push({x:Math.random()*W,y:Math.random()*H,r:(Math.random()*1.6+0.8)*dpr,vx:(Math.random()-0.5)*0.12*dpr,vy:(Math.random()-0.5)*0.12*dpr,ph:Math.random()*Math.PI*2});}}
function col(){return getComputedStyle(document.documentElement).getPropertyValue('--particle-color').trim()||'rgba(120,120,135,0.3)';}
addEventListener('pointermove',function(e){px=e.clientX*dpr;py=e.clientY*dpr;});
addEventListener('pointerleave',function(){px=py=-9999;});
var t=0;function fr(){t+=0.004;x.clearRect(0,0,W,H);var cc=col();
for(var i=0;i<dots.length;i++){var d=dots[i];
d.x+=d.vx+Math.sin(t+d.ph)*0.06*dpr;d.y+=d.vy+Math.cos(t*0.8+d.ph)*0.05*dpr;
var dx=d.x-px,dy=d.y-py,q=dx*dx+dy*dy,R=120*dpr;
if(q<R*R&&q>0.01){var s=Math.sqrt(q),f=(1-s/R)*0.6*dpr;d.x+=(dx/s)*f;d.y+=(dy/s)*f;}
if(d.x<-10)d.x=W+10;if(d.x>W+10)d.x=-10;if(d.y<-10)d.y=H+10;if(d.y>H+10)d.y=-10;
x.globalAlpha=0.55+0.45*Math.sin(t*2+d.ph*3);x.fillStyle=cc;x.beginPath();x.arc(d.x,d.y,d.r,0,Math.PI*2);x.fill();}
x.globalAlpha=1;requestAnimationFrame(fr);}
if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){rs();sd();addEventListener('resize',function(){rs();sd();});requestAnimationFrame(fr);}})();
</script>
</body>
</html>
"""
    return doc


def main():
    posts = load_posts()
    total = 0
    section_names = {k: n for k, n, _ in SECTIONS}
    for key, entries in posts.items():
        out_dir = ESSAYS / key
        # wipe stale pages so deletions propagate
        if out_dir.is_dir():
            for old in out_dir.glob("*.html"):
                old.unlink()
        if entries:
            out_dir.mkdir(parents=True, exist_ok=True)
        for p in entries:
            (out_dir / f"{p['slug']}.html").write_text(
                render_essay(p, section_names[key]), encoding="utf-8")
            total += 1

    home_html = HOME_HTML.read_text(encoding="utf-8") if HOME_HTML.is_file() else ""
    (ROOT / "index.html").write_text(render_home(posts, home_html), encoding="utf-8")
    (ROOT / ".nojekyll").touch()
    print(f"Built {total} essay(s) + index.html")


if __name__ == "__main__":
    main()
