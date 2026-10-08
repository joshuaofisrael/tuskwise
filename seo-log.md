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
  only hours old. Live check at /tuskwise/: all 24 sitemap URLs + robots, sitemap, llms.txt, key file 200; brand
  and footer contact verified on 25/25 HTML pages.
- IndexNow (all 24 new sitemap URLs, 11:58 BST): api.indexnow.org HTTP 202, bing.com/indexnow HTTP 202.
- FormSubmit: one approved test submission 11:58 BST; response "This form needs Activation" (activation email sent
  to joshuaofisrael@gmail.com; Personal assistant to click).

## 2026-10-08 ~12:05 London: logo tusks
- Added two ivory tusks to the elephant mark (header SVG, favicon.svg, logo.png, og-image.png via _og.py, supersampled).
- Page HTML change is only the inline logo SVG; sitemap and content unchanged, so no IndexNow re-ping.

## 2026-10-08 ~12:35 London: custom domain https://tuskwise.com/ live (one push, commit 64745bc)
- DNS verified with dig (1.1.1.1 and 8.8.8.8): apex A 185.199.108.153/.109/.110/.111; www CNAME joshuaofisrael.github.io.
  Namecheap order 216171348 (bought by Personal assistant).
- SITE_URL = https://tuskwise.com/; build wrote CNAME (tuskwise.com). Canonicals, sitemap, robots Sitemap line, llms.txt,
  OG and JSON-LD URLs all on https://tuskwise.com/; no github.io references in built output. 404 links now root relative.
- Pages custom domain set via API (PUT pages cname). Certificate approved within minutes (Let's Encrypt, CN=tuskwise.com,
  covers www); https_enforced = true.
- Live: https://tuskwise.com/ 200; http -> https 301; www (http and https) -> https://tuskwise.com/ 301 (paths kept);
  old https://joshuaofisrael.github.io/tuskwise/* 301 to the same path on tuskwise.com. All 24 sitemap URLs, sitemap.xml,
  robots.txt, llms.txt, key file https://tuskwise.com/e431c862123afb33b22681739bf0f4c8.txt: 200. Footer contact + LLC on 25/25.
- robots.txt is now at the host root, so it is authoritative for crawlers (the github.io limitation is gone).
- IndexNow (host tuskwise.com, 24 URLs, 12:32 BST): api.indexnow.org HTTP 202, bing.com/indexnow HTTP 202.
- FormSubmit: one approved test from https://tuskwise.com/contact.html at 12:33 BST; response "This form needs
  Activation. We've sent you an email containing an 'Activate Form' link." Personal assistant to click.
- Next: GSC Domain property for tuskwise.com (Joshua), Cloudflare beacon token for tuskwise.com, Bing Webmaster Tools.

## Scorecard
| Date | Window | Impressions | Clicks | CTR | Avg pos | Indexed pages | Top100/20/10/3 queries | Growing pages | Declining pages | Conversions |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-08 | 7d | n/a (no GSC yet) | n/a | n/a | n/a | 23 URLs + llms.txt in sitemap | n/a | n/a | n/a | n/a |
| | 28d | | | | | | | | | |
| | 90d | | | | | | | | | |

## 2026-10-08: Education campaign, step 1 (teachers hub, research page, cite boxes). Commit d5a33a1
- New: /teachers/ hub, 4 printables (species fact sheet, anatomy label the diagram with an original SVG, adaptations worksheet, quiz with answer key),
  NGSS lesson ideas by grade band (1-LS1-2, 3-LS2-1, 3-LS4-3, 4-LS1-1, MS-LS2-2, HS-LS2-8, HS-LS4-5, all checked against nextgenscience.org), vocabulary
  linked to the glossary, and a "Classroom games: coming soon" spot (/games/ was 404 at build time). /research/ lists 23 papers; every DOI was checked one at a time on the Crossref API.
- Fix: Hart et al. 2001 DOI on intelligence.html was wrong (10.1006/anbe.2001.1811 points to a raptor paper). Corrected to 10.1006/anbe.2001.1815.
- Template: a "Last reviewed" date plus a Cite this page box (APA, MLA, Chicago) on every article and blog post; LearningResource JSON-LD (educationalLevel,
  NGSS AlignmentObject) on teacher pages; ItemList of ScholarlyArticle on /research/; no ad slots on teacher or research pages; print CSS is black on white with chrome hidden.
- Nav "For Teachers", footer link, and homepage tiles for Teachers and Research. Sitemap 32 URLs; llms.txt has a new Classroom section.
- Target queries: elephant worksheet for 3rd grade, elephant adaptations lesson plan, elephant anatomy worksheet, elephant quiz with answer key, elephant research papers.
- outreach/ (targets.csv, directories.md, pinterest-plan.md, email-template.md) is in the _config.yml exclude list and not published.
