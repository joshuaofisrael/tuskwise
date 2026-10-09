#!/usr/bin/env python3
"""TuskWise static site builder. Renders _src/ fragments into static HTML at the repo root.

To move to the custom domain (planned: tuskwise.com): change SITE_URL below to "https://tuskwise.com/" (one line).
The build then writes the CNAME file itself (and deletes it while SITE_URL is a github.io URL).
Run `python3 _build.py`, commit, push, set the domain in Settings > Pages, then ping IndexNow (./indexnow.sh).
"""
import json, os, re, html, glob, datetime
from urllib.parse import urlparse

SITE_URL = "https://tuskwise.com/"   # <- the ONLY place the base URL lives
SITE_NAME = "TuskWise"
LEGAL = "Joshua Israel Ventures LLC"
GSC_TOKEN = ""          # Google Search Console verification token (meta tag); Joshua generates it in GSC
CF_BEACON_TOKEN = ""    # Cloudflare Web Analytics beacon token; empty = no beacon emitted
INDEXNOW_KEY = "e431c862123afb33b22681739bf0f4c8"
FORM_EMAIL = "joshuaofisrael@gmail.com"

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = urlparse(SITE_URL).path or "/"   # "/tuskwise/" now, "/" on a custom domain
OG_IMAGE = SITE_URL + "og-image.png"

NAV = [
    ("home", "Home", "index.html"),
    ("compare", "Species Compared", "african-vs-asian-elephant.html"),
    ("savanna", "Savanna Elephant", "african-savanna-elephant.html"),
    ("forest", "Forest Elephant", "african-forest-elephant.html"),
    ("asian", "Asian Elephant", "asian-elephant.html"),
    ("anatomy", "Anatomy", "anatomy.html"),
    ("behavior", "Behavior", "behavior.html"),
    ("intelligence", "Intelligence", "intelligence.html"),
    ("habitats", "Habitats & Diet", "habitats.html"),
    ("conservation", "Conservation", "conservation.html"),
    ("viewing", "Ethical Viewing", "ethical-viewing.html"),
    ("checklist", "Sanctuary Checklist", "elephant-sanctuary-checklist.html"),
    ("faq", "FAQ", "faq.html"),
    ("glossary", "Glossary", "glossary.html"),
    ("teachers", "For Teachers", "teachers/index.html"),
    ("games", "Games", "games/index.html"),
    ("blog", "Blog", "blog/index.html"),
]

LOGO = ('<svg role="img" width="36" height="36" viewBox="0 0 64 64" aria-hidden="true"><title>TuskWise logo</title>'
        '<rect width="64" height="64" rx="16" fill="#ffe566"/>'
        '<ellipse cx="17" cy="28" rx="12" ry="15" fill="#1f4bff"/><ellipse cx="47" cy="28" rx="12" ry="15" fill="#ff3b7a"/>'
        '<circle cx="32" cy="26" r="14" fill="#4d74ff"/>'
        '<path d="M26 34C25 40 22 44 18 43" fill="none" stroke="#ffe566" stroke-width="3.4" stroke-linecap="round"/><path d="M38 34C39 40 42 44 46 43" fill="none" stroke="#ffe566" stroke-width="3.4" stroke-linecap="round"/>'
        '<path d="M32 33c0 9-1 15 4 19 3 2 7 0 7-3" fill="none" stroke="#1a1464" stroke-width="6" stroke-linecap="round"/>'
        '<circle cx="26" cy="24" r="2" fill="#16182a"/><circle cx="38" cy="24" r="2" fill="#16182a"/>'
        '<circle cx="31" cy="32" r="2.2" fill="#ff3b7a"/>'
        '</svg>')

def esc(s):
    return html.escape(s, quote=True)

def load(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"<!--meta\s*(\{.*?\})\s*-->\s*", raw, re.S)
    if not m:
        raise SystemExit("missing meta: " + path)
    meta = json.loads(m.group(1))
    meta["body"] = raw[m.end():]
    return meta

def collect():
    pages = []
    for f in sorted(glob.glob(os.path.join(ROOT, "_src/pages/*.html"))):
        p = load(f); slug = os.path.basename(f)
        p["out"] = slug
        pages.append(p)
    for f in sorted(glob.glob(os.path.join(ROOT, "_src/blog/*.html"))):
        p = load(f); slug = os.path.basename(f)
        p["out"] = "blog/" + slug
        p.setdefault("nav", "blog")
        if slug != "index.html":
            p.setdefault("kind", "post")
        pages.append(p)
    for sub in ("teachers", "research", "credits"):
        for f in sorted(glob.glob(os.path.join(ROOT, "_src", sub, "*.html"))):
            p = load(f); slug = os.path.basename(f)
            p["out"] = sub + "/" + slug
            p.setdefault("nav", "teachers")
            pages.append(p)
    # Games hub + per-game folders (games/index.html and games/<slug>/index.html)
    games_src = os.path.join(ROOT, "_src", "games")
    for f in sorted(glob.glob(os.path.join(games_src, "*.html"))):
        p = load(f); slug = os.path.basename(f)
        p["out"] = "games/" + slug
        p.setdefault("nav", "games")
        p.setdefault("noads", True)
        pages.append(p)
    for f in sorted(glob.glob(os.path.join(games_src, "*", "index.html"))):
        p = load(f)
        rel = os.path.relpath(f, os.path.join(ROOT, "_src"))
        p["out"] = rel.replace("\\", "/")
        p.setdefault("nav", "games")
        p.setdefault("noads", True)
        pages.append(p)
    return pages

def url_for(out):
    if out == "index.html":
        return SITE_URL
    if out.endswith("/index.html"):
        return SITE_URL + out[:-len("index.html")]
    return SITE_URL + out

def org(include_logo=True):
    o = {"@type": "Organization", "@id": SITE_URL + "#organization", "name": LEGAL, "legalName": LEGAL, "url": SITE_URL,
         "email": FORM_EMAIL, "brand": {"@type": "Brand", "name": SITE_NAME}}
    if include_logo:
        o["logo"] = SITE_URL + "logo.png"
    return o

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"

def nice_date(d):
    dt = datetime.date.fromisoformat(d)
    return f"{dt.day} {dt.strftime('%B %Y')}"

# Small decorative doodle (original): elephant footprints and a leaf, hidden from assistive tech.
PRINTS = ('<svg class="prints" viewBox="0 0 132 24" aria-hidden="true" focusable="false">'
          '<defs><g id="fp"><ellipse cx="0" cy="2" rx="7" ry="6.5" fill="#1f4bff"/>'
          '<circle cx="-4.5" cy="-5.5" r="1.8" fill="#ff3b7a"/><circle cx="0" cy="-7" r="1.8" fill="#ffe566"/>'
          '<circle cx="4.5" cy="-5.5" r="1.8" fill="#1f4bff"/></g></defs>'
          '<use href="#fp" x="12" y="13"/><use href="#fp" x="38" y="11"/>'
          '<path d="M56 18c0-8 6-13 14-13 0 8-6 13-14 13z" fill="#ff3b7a"/><path d="M58 16l9-8" stroke="#1a1464" stroke-width="1.5" stroke-linecap="round"/>'
          '<path d="M76 18c0-8 6-13 14-13 0 8-6 13-14 13z" fill="#ffe566"/>'
          '<use href="#fp" x="104" y="11"/><use href="#fp" x="122" y="13"/></svg>')

def head(p, canonical, prefix, noindex=False, absolute=False):
    title = p["title"]; desc = p["description"]
    css = (BASE_PATH + "style.css") if absolute else (prefix + "style.css")
    fav = (BASE_PATH + "favicon.svg") if absolute else (prefix + "favicon.svg")
    h = ['<!doctype html><html lang="en"><head><meta charset="utf-8">']
    if p["out"] == "index.html" and GSC_TOKEN:
        h.append(f'<meta name="google-site-verification" content="{esc(GSC_TOKEN)}">')
    h.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    h.append(f"<title>{esc(title)}</title><meta name=\"description\" content=\"{esc(desc)}\">")
    if noindex:
        h.append('<meta name="robots" content="noindex">')
    else:
        h.append(f'<link rel="canonical" href="{canonical}">')
    font = (BASE_PATH if absolute else prefix) + "fonts/fredoka-600-latin.woff2"
    h.append(f'<link rel="preload" href="{font}" as="font" type="font/woff2" crossorigin>'
             f'<link rel="stylesheet" href="{css}"><link rel="icon" href="{fav}" type="image/svg+xml">')
    ogt = "article" if p.get("kind") in ("post", "article") else "website"
    h.append(f'<meta property="og:type" content="{ogt}"><meta property="og:site_name" content="{SITE_NAME}">'
             f'<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">'
             + (f'<meta property="og:url" content="{canonical}">' if not noindex else "") +
             f'<meta property="og:image" content="{OG_IMAGE}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
             f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}">'
             f'<meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{OG_IMAGE}">')
    return "".join(h)

def header(active, prefix, absolute=False):
    base = BASE_PATH if absolute else prefix
    links = []
    for key, label, href in NAV:
        cur = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{base}{href}"{cur}>{esc(label)}</a>')
    return (f'<header><a class="brand" href="{base}index.html">{LOGO}<span>{SITE_NAME}</span></a>'
            '<button class="menu" aria-label="Menu" onclick="document.body.classList.toggle(\'open\')">&#9776;</button>'
            f'<nav aria-label="Main">{"".join(links)}</nav></header>')

def footer(prefix, absolute=False):
    base = BASE_PATH if absolute else prefix
    beacon = ""
    if CF_BEACON_TOKEN:
        beacon = ("<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
                  "data-cf-beacon='{\"token\": \"" + CF_BEACON_TOKEN + "\"}'></script><!-- End Cloudflare Web Analytics -->")
    return (f'<footer>{PRINTS}<section class="contact-us" id="contact-us"><h2>Contact us</h2><p>Questions, corrections or ideas? Email '
            f'<a href="mailto:{FORM_EMAIL}">{FORM_EMAIL}</a> or use our <a href="{base}contact.html">contact form</a>.</p></section>'
            f'<p class="flinks"><a href="{base}terms.html">Terms</a> &middot; <a href="{base}privacy.html">Privacy</a> &middot; '
            f'<a href="{base}disclaimer.html">Disclaimer</a> &middot; <a href="{base}contact.html">Contact</a> &middot; '
            f'<a href="{base}about.html">About</a> &middot; <a href="{base}teachers/index.html">For Teachers</a> &middot; <a href="{base}games/index.html">Games</a> &middot; <a href="{base}credits/index.html">Photo credits</a> &middot; <a href="{base}blog/index.html">Blog</a></p>'
            f'<p class="legal">&copy; 2026 {LEGAL}. All rights reserved. {SITE_NAME} is owned and operated by {LEGAL}.</p>'
            f'<p>Original educational content about elephants. All text and illustrations are original.</p></footer>{beacon}</body></html>')

MLA_MON = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]

def cite_box(p, canonical, prefix):
    title = esc(p["h1"]); reviewed = p.get("modified", p["published"])
    dt = datetime.date.fromisoformat(reviewed)
    mon = dt.strftime("%B")
    end = "" if title[-1:] in "?!" else "."
    bare = canonical.replace("https://", "")
    apa = f"{SITE_NAME}. ({dt.year}, {mon} {dt.day}). <i>{title}</i>{end} {canonical}"
    mla = f"&ldquo;{title}{end}&rdquo; <i>{SITE_NAME}</i>, {LEGAL}, {dt.day} {MLA_MON[dt.month - 1]} {dt.year}, {bare}."
    chi = f"{SITE_NAME}. &ldquo;{title}{end}&rdquo; {LEGAL}. Last modified {mon} {dt.day}, {dt.year}. {canonical}."
    return (f'<section class="card cite" id="cite"><h2>Cite this page</h2>'
            f'<p class="meta">Last reviewed {nice_date(reviewed)}. Suggested citations for students and teachers:</p>'
            f'<p><b>APA</b><br>{apa}</p><p><b>MLA</b><br>{mla}</p><p><b>Chicago</b><br>{chi}</p>'
            f'<p class="meta">Using a fact from a study? Cite the original paper too. The <a href="{prefix}research/index.html">research page</a> lists the peer reviewed papers behind TuskWise with DOIs.</p></section>')

def render(p, by_out):
    out = p["out"]; depth = out.count("/"); prefix = "../" * depth
    canonical = url_for(out)
    noindex = p.get("noindex", False)
    body = p["body"].replace("@/", prefix).replace("{{SITE_URL}}", SITE_URL)
    kind = p.get("kind", "article")
    parts = [head(p, canonical, prefix, noindex=noindex)]
    # JSON-LD
    if out == "index.html":
        parts.append(ld({"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": SITE_URL,
                         "@id": SITE_URL + "#website",
                         "description": p["description"], "publisher": {"@id": SITE_URL + "#organization"}}))
        parts.append(ld({"@context": "https://schema.org", **org()}))
    elif not noindex:
        if kind in ("article", "post"):
            parts.append(ld({"@context": "https://schema.org", "@type": "Article" if kind == "article" else "BlogPosting",
                             "headline": p["h1"], "description": p["description"], "image": OG_IMAGE,
                             "datePublished": p["published"], "dateModified": p.get("modified", p["published"]),
                             "author": org(False), "publisher": org(),
                             "mainEntityOfPage": {"@type": "WebPage", "@id": canonical}, "inLanguage": "en"}))
        elif kind == "learning":
            lr = {"@context": "https://schema.org", "@type": "LearningResource", "name": p["h1"],
                  "description": p["description"], "url": canonical, "inLanguage": "en", "isAccessibleForFree": True,
                  "learningResourceType": p.get("lr_type", "lesson plan"),
                  "educationalLevel": p.get("edu_level", "K-12"),
                  "audience": {"@type": "EducationalAudience", "educationalRole": "teacher"},
                  "publisher": org(), "dateModified": p.get("modified", p["published"])}
            if p.get("lr_align"):
                lr["educationalAlignment"] = [{"@type": "AlignmentObject", "alignmentType": "teaches",
                    "educationalFramework": "NGSS", "targetName": c} for c in p["lr_align"]]
            parts.append(ld(lr))
        elif kind == "game":
            pub = org()
            parts.append(ld({"@context": "https://schema.org", "@graph": [
                {"@type": "WebPage", "@id": canonical + "#page", "url": canonical, "name": p["h1"] + " | " + SITE_NAME,
                 "description": p["description"], "inLanguage": "en",
                 "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": SITE_URL},
                 "publisher": pub, "mainEntity": {"@id": canonical + "#game"}},
                {"@type": "VideoGame", "@id": canonical + "#game", "name": p.get("game_name", p["h1"]),
                 "url": canonical, "description": p["description"],
                 "genre": p.get("game_genre", "Educational game"), "gamePlatform": "Web browser",
                 "applicationCategory": "Game", "operatingSystem": "Any", "playMode": "SinglePlayer",
                 "isAccessibleForFree": True, "inLanguage": "en",
                 "teaches": p.get("teaches", p["description"]),
                 "author": org(False), "publisher": pub, "copyrightHolder": org(False), "copyrightYear": 2026}]}))
        elif kind == "games-hub":
            items = [{"@type": "ListItem", "position": i + 1, "url": it["url"], "name": it["name"]}
                     for i, it in enumerate(p.get("game_list", []))]
            parts.append(ld({"@context": "https://schema.org", "@type": "CollectionPage",
                             "@id": canonical + "#page", "url": canonical, "name": p["h1"],
                             "description": p["description"], "inLanguage": "en",
                             "publisher": org(),
                             "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": SITE_URL},
                             "mainEntity": {"@type": "ItemList", "itemListElement": items}}))
        else:
            parts.append(ld({"@context": "https://schema.org", "@type": p.get("schema", "WebPage"), "name": p["h1"],
                             "description": p["description"], "url": canonical, "isPartOf": {"@type": "WebSite", "@id": SITE_URL + "#website", "name": SITE_NAME, "url": SITE_URL},
                             "publisher": org()}))
        crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL}]
        par = out.split("/")[0] + "/index.html"
        if "/" in out and out != par and par in by_out:
            crumbs.append({"@type": "ListItem", "position": 2, "name": by_out[par].get("crumb", by_out[par]["h1"]), "item": url_for(par)})
        crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1, "name": p.get("crumb", p["h1"]), "item": canonical})
        parts.append(ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": crumbs}))
    if p.get("ld_items"):
        parts.append(ld({"@context": "https://schema.org", "@type": "ItemList", "name": p["h1"], "numberOfItems": len(p["ld_items"]),
                         "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": it} for i, it in enumerate(p["ld_items"])]}))
    if p.get("faq"):
        parts.append(ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in p["faq"]]}))
    parts.append("</head><body>")
    parts.append(header(p.get("nav", ""), prefix))
    noads = kind == "learning" or p.get("noads")
    parts.append('<main>' if noads else '<!-- AD SLOT: top banner (reserved, no ad code) --><div class="ad-slot" data-slot="top" hidden></div><main>')
    # breadcrumb trail (visible)
    if out != "index.html" and not noindex:
        trail = f'<a href="{prefix}index.html">Home</a>'
        par = out.split("/")[0] + "/index.html"
        if "/" in out and out != par and par in by_out:
            trail += f' &rsaquo; <a href="{prefix}{par}">{esc(by_out[par].get("crumb", by_out[par]["h1"]))}</a>'
        trail += f' &rsaquo; <span>{esc(p.get("crumb", p["h1"]))}</span>'
        parts.append(f'<nav class="crumbs" aria-label="Breadcrumb">{trail}</nav>')
    if out != "index.html":
        parts.append(f'<h1>{esc(p["h1"])}</h1>')
        if kind in ("article", "post") and not noindex:
            reviewed = p.get("modified", p["published"])
            if kind == "post":
                parts.append(f'<p class="meta">Published {nice_date(p["published"])}'
                             + (f' &middot; Updated {nice_date(p["modified"])}' if p.get("modified") and p["modified"] != p["published"] else "")
                             + f' &middot; Last reviewed {nice_date(reviewed)} &middot; By the {SITE_NAME} team</p>')
            else:
                parts.append(f'<p class="meta">Last reviewed {nice_date(reviewed)}</p>')
        if kind == "learning" and not noindex:
            parts.append(f'<p class="meta">Last reviewed {nice_date(p.get("modified", p["published"]))} &middot; Free, no sign up, no ads</p>')
        if p.get("lead"):
            parts.append(f'<p class="lead">{p["lead"]}</p>')
    if "{{POSTS}}" in body:
        posts = sorted([q for q in by_out.values() if q.get("kind") == "post"], key=lambda q: q["published"], reverse=True)
        li = "".join(f'<li class="card"><h2><a href="{q["out"][5:]}">{esc(q["h1"])}</a></h2><p class="meta">{nice_date(q["published"])}</p><p>{esc(q["description"])}</p></li>' for q in posts)
        body = body.replace("{{POSTS}}", f'<ul class="postlist">{li}</ul>')
    parts.append(body)
    if p.get("faq"):
        qa = "".join(f'<details class="qa"><summary>{esc(q)}</summary><p>{a.replace("@/", prefix)}</p></details>' for q, a in p["faq"])
        parts.append(f'<section class="card" id="faq"><h2>{esc(p.get("faq_title", "Frequently asked questions"))}</h2>{qa}</section>')
    if p.get("related"):
        items = []
        for r in p["related"]:
            t = by_out[r]
            href = prefix + r
            items.append(f'<li><a href="{href}">{esc(t.get("short", t["h1"]))}</a></li>')
        parts.append(f'<aside class="card related"><h2>Keep exploring</h2><ul>{"".join(items)}</ul></aside>')
    if p.get("sources"):
        src = "".join(f'<li><a href="{esc(u)}" rel="noopener">{esc(t)}</a></li>' for t, u in p["sources"])
        parts.append(f'<section class="sources"><h2>Sources</h2><ol>{src}</ol></section>')
    if kind in ("article", "post") and not noindex:
        parts.append(cite_box(p, canonical, prefix))
    if kind == "learning":
        parts.append(f'<p class="meta">Free for classroom use. Printed from {SITE_URL}{"" if out == "index.html" else out.replace("index.html", "")} &middot; &copy; 2026 {LEGAL}.</p>')
    parts.append('</main>' if noads else '<!-- AD SLOT: in-content (reserved, no ad code) --><div class="ad-slot" data-slot="content-bottom" hidden></div></main>')
    parts.append(footer(prefix))
    return "".join(parts)

def notfound():
    p = {"out": "404.html", "title": "Page Not Found | TuskWise", "description": "This page wandered off with the herd."}
    b = BASE_PATH
    return (head(p, "", "", noindex=True, absolute=True) + "</head><body>" + header("", "", absolute=True) +
            '<main><h1>This page wandered off with the herd</h1><p>We could not find that page. Try the '
            f'<a href="{b}">home page</a>, the <a href="{b}african-vs-asian-elephant.html">African vs Asian elephant comparison</a>, '
            f'the <a href="{b}faq.html">elephant FAQ</a> or the <a href="{b}blog/index.html">blog</a>.</p></main>' + footer("", absolute=True))

def main():
    pages = collect()
    by_out = {p["out"]: p for p in pages}
    os.makedirs(os.path.join(ROOT, "blog"), exist_ok=True)
    for sub in ("teachers", "research", "credits", "games"):
        os.makedirs(os.path.join(ROOT, sub), exist_ok=True)
    for p in pages:
        d = os.path.dirname(os.path.join(ROOT, p["out"]))
        if d:
            os.makedirs(d, exist_ok=True)
    for p in pages:
        htmltext = render(p, by_out)
        open(os.path.join(ROOT, p["out"]), "w", encoding="utf-8").write(htmltext)
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(notfound())
    # sitemap
    urls = []
    for p in pages:
        if p.get("noindex") or p.get("sitemap") is False:
            continue
        urls.append((url_for(p["out"]), p.get("modified", p.get("published", "2026-10-08"))))
    urls.append((SITE_URL + "llms.txt", max(u[1] for u in urls)))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"<url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in urls) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
    # robots
    bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "Perplexity-User", "ClaudeBot",
            "Claude-SearchBot", "Claude-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckAssistBot", "Amazonbot"]
    rb = "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {SITE_URL}sitemap.xml\n"
    open(os.path.join(ROOT, "robots.txt"), "w").write(rb)
    # llms.txt
    groups = {"guides": [], "tools": [], "classroom": [], "blog": [], "optional": []}
    for p in pages:
        g = p.get("llms")
        if g:
            groups[g].append(p)
    def line(p):
        s = f"- [{p.get('short', p['h1'])}]({url_for(p['out'])}): {p.get('llms_desc', p['description'])}"
        if p.get("anchors"):
            s += "\n  - Sections: " + ", ".join(f"[{t}]({url_for(p['out'])}#{a})" for t, a in p["anchors"])
        return s
    lt = [f"# {SITE_NAME}", "",
          f"> {SITE_NAME} is a free, original educational website about elephants: the African savanna elephant, the African forest elephant and the Asian elephant. It covers how to tell the species apart, anatomy, family life and behavior, intelligence and memory research, habitats and diet, conservation status and population estimates, and how to see elephants ethically in the wild. Every page cites reputable sources such as the IUCN, WWF, accredited zoos and peer reviewed studies. Operated by {LEGAL}.",
          "", "The content is general education. Population figures are the latest published estimates and are dated on each page.", ""]
    for g, title in (("tools", "Tools"), ("guides", "Guides"), ("classroom", "Classroom"), ("blog", "Blog"), ("optional", "Optional")):
        if groups[g]:
            lt.append(f"## {title}")
            lt += [line(p) for p in groups[g]]
            lt.append("")
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(lt))
    open(os.path.join(ROOT, INDEXNOW_KEY + ".txt"), "w").write(INDEXNOW_KEY)
    host = urlparse(SITE_URL).hostname or ""
    cname = os.path.join(ROOT, "CNAME")
    if host.endswith("github.io"):
        if os.path.exists(cname): os.remove(cname)
    else:
        open(cname, "w").write(host + "\n")
    # dash check on generated user facing text
    bad = []
    for f in [p["out"] for p in pages] + ["404.html", "llms.txt"]:
        t = open(os.path.join(ROOT, f), encoding="utf-8").read()
        if "\u2014" in t or "\u2013" in t:
            bad.append(f)
    css_path = os.path.join(ROOT, "style.css")
    css = open(css_path, encoding="utf-8").read()
    marker = "/* PRINT */"
    # .onlyprint hidden on screen via the print block below
    base = css.split(marker)[0].rstrip() + "\n"
    printcss = """/* PRINT */
@media print{
body{background:#fff;color:#000}
header,.menu,nav,.crumbs,.jump,.ad-slot,.related,.prints,footer .contact-us,.flinks,form.contact,.noprint{display:none!important}
main{max-width:none;padding:0}
h1,h2,h3{color:#000}
a{color:#000;text-decoration:none}
.card,.tile,.postlist li,.tablewrap,.callout{background:#fff;box-shadow:none;border:1px solid #000;border-radius:0}
.hero{background:#fff;box-shadow:none}
figure.photo img,.hero-photo{box-shadow:none;border-radius:0}
.answer-key{display:block!important;break-before:page}
.onlyprint{display:inline}
table,th,td{border:1px solid #000}
footer{background:#fff;color:#000;border-radius:0}
.answer-key{border:2px solid #000}
.sheet h2::before{display:none}
}
"""
    open(css_path, "w", encoding="utf-8").write(base + printcss)
    if bad:
        raise SystemExit("em/en dash found in: " + ", ".join(bad))
    # JSON-LD parse check
    for f in [p["out"] for p in pages]:
        t = open(os.path.join(ROOT, f), encoding="utf-8").read()
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(m.group(1))
    print(f"built {len(pages)} pages + 404, sitemap {len(urls)} urls, base {SITE_URL}")

if __name__ == "__main__":
    main()
