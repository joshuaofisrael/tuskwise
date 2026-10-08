# TuskWise SEO log

## 2026-10-08: v1 launch (no Search Console data yet)
Built from scratch following /workspace/animal-sites/BRIEF.md and SNAKE-BOT-PLAYBOOK.md (mirrors snakewise:
plain static HTML, one CSS file, GitHub Pages deploy from branch, relative links, AI crawler robots, llms.txt,
IndexNow), plus the playbook's "do better" items: sources and last updated dates on every page, Article/BlogPosting
schema with datePublished, dateModified and image, BreadcrumbList, og:image, sitemap lastmod, About/Contact/Privacy,
a blog, no placeholder shop.

Pages: home; unique asset african-vs-asian-elephant.html (3 species comparison table, deep link anchors, FAQ);
species pillars (savanna, forest, Asian); anatomy; behavior; intelligence; habitats and diet; conservation;
ethical viewing; FAQ (myths, FAQPage); glossary; about; contact (FormSubmit + mailto); privacy; blog index + 5 posts:
how many elephants are left, do elephants never forget, is it ethical to ride elephants, why big ears,
how long are elephants pregnant. thanks.html and 404.html are noindex and not in the sitemap.

Owner update 8 Oct 11:00: every page has a visible "Contact us" block in the footer with a mailto link to
joshuaofisrael@gmail.com and a link to the contact form.

Unique angle vs current results: dated, sourced population numbers including the IUCN 2024 forest elephant
report (released Nov 2025) and India's 2025 DNA based estimate, which many popular pages have not caught up with.

Not yet possible: Cloudflare beacon (box API tokens get "Authentication error" on rum/site_info), GSC verification
(token must come from Joshua; GSC_TOKEN placeholder in _build.py).

Next ideas: add an original SVG trunk tip diagram; once GSC data exists, see which comparison anchors earn
impressions; update the population post when the IUCN savanna elephant status report is published.

## 2026-10-08 ~11:55 London: signature resource + verification
- New unique asset: /elephant-sanctuary-checklist.html ("Is this elephant sanctuary ethical?"): 9 anchored sections
  (riding, bathing, performing, bullhooks, chaining, breeding, trade, contact/photos, transparency), vetting steps,
  printable list, 5 question FAQ with FAQPage schema. Practices only; no venue named or rated. Sources: World Animal
  Protection, ABTA 2019 guidelines, GFAS standards and position statements, IFAW. Linked from home hero, home callout,
  home tile grid, nav, ethical viewing (callout, jump row, sanctuaries section, related), riding post and conservation.
- Species pages now each carry a compact savanna vs forest vs Asian table (ears, tusks, back, trunk tip, range,
  status) linking to the full comparison.
- Live check: 24 sitemap URLs + robots, sitemap, llms.txt, key file all HTTP 200; 404 page works; footer Contact us
  (mailto) + LLC line on 25/25 live pages; 30/30 crawler UA checks 200.
- IndexNow (all 24 sitemap URLs): api.indexnow.org HTTP 202, bing.com/indexnow HTTP 200.
- Note: on github.io the host root robots.txt (joshuaofisrael.github.io/robots.txt) is 404, which crawlers treat as
  allow all; our /tuskwise/robots.txt becomes authoritative only once a custom domain is live.

## 2026-10-08 ~12:00 London: rebrand to TuskWise (approved via Personal assistant)
- Site renamed (formerly the first name, see git history); repo renamed to joshuaofisrael/tuskwise; SITE_URL now
  https://joshuaofisrael.github.io/tuskwise/. Planned domain tuskwise.com (no CNAME yet; build writes CNAME
  automatically once SITE_URL is a non github.io host). OG image and logo regenerated (_og.py).
- Old github.io path no longer serves (GitHub does not redirect Pages paths after a repo rename); the old URLs were
  only hours old. IndexNow re-pinged with all new sitemap URLs (results below).

## Scorecard
| Date | Window | Impressions | Clicks | CTR | Avg pos | Indexed pages | Top100/20/10/3 queries | Growing pages | Declining pages | Conversions |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-08 | 7d | n/a (no GSC yet) | n/a | n/a | n/a | 23 URLs + llms.txt in sitemap | n/a | n/a | n/a | n/a |
| | 28d | | | | | | | | | |
| | 90d | | | | | | | | | |
