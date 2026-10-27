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
- IndexNow (32 sitemap URLs: new teacher and research pages plus all pages changed by the nav, cite box and Last reviewed date), 14:45 BST: api.indexnow.org HTTP 200, bing.com/indexnow HTTP 200.
- Outreach files moved out of the public repo to /workspace/animal-sites/elephants/outreach/ (commits 3c6c988 and 2b1243d); outreach/ is now in .gitignore. They are still in git history at 364fa23.

## 2026-10-09 ~03:30 London - Games launch (daily slot catch-up)
- Action: shipped /games/ hub + 3 original browser games; nav + homepage tile + teachers #games links; IndexNow 10 URLs.
- Why highest EV: new indexable interactive URLs + classroom link from teachers hub; matches animal-sites GAMES-BRIEF and mentor SnakeWise pattern.
- Result: Pages status built; live HTTP 200 on hub + 3 games + CREDITS.md; IndexNow api.indexnow.org 200 and bing.com 200.
- Commit: 749f33b
- 2026-10-09 11:12 London: daily fact article published: /blog/do-elephants-have-names-for-each-other.html (Pardo et al. 2024 Nat Ecol Evol 10.1038/s41559-024-02420-w; Poole 2005 Nature; Stoeger 2012 Curr Biol; Soltis 2010 Zoo Biol; all DOIs Crossref verified). Sitemap, blog index, llms.txt updated; IndexNow pinged.
- 2026-10-11 01:20 London: daily fact article published: /blog/can-elephants-recognize-themselves-in-a-mirror.html (Plotnik, de Waal and Reiss 2006 PNAS 10.1073/pnas.0608062103; Povinelli 1989 J Comp Psychol; Gallup 1970 Science; Reiss and Marino 2001 PNAS; all DOIs Crossref verified). Sitemap, blog index, llms.txt updated; IndexNow pinged.
- 2026-10-12 01:15 London: daily fact article published: /blog/how-do-elephants-communicate-over-long-distances.html (Payne, Langbauer and Thomas 1986 Behav Ecol Sociobiol 10.1007/BF00300007; Garstang 2004 J Comp Physiol A 10.1007/s00359-004-0553-0; Herbst et al. 2012 Science 10.1126/science.1219712; O'Connell-Rodwell et al. 2006 10.1007/s00265-005-0136-2 and 2007 JASA 10.1121/1.2747161; all DOIs Crossref verified). Sitemap, blog index, llms.txt updated; IndexNow pinged.
- 2026-10-14 01:14 London: daily fact article published: /blog/how-long-do-elephants-sleep.html (Gravett et al. 2017 PLOS ONE 10.1371/journal.pone.0171903; Tobler 1992 Sleep 10.1093/sleep/15.1.1; Holdgate et al. 2016 PLOS ONE 10.1371/journal.pone.0153301; Siegel 2005 Nature 10.1038/nature04285; all DOIs Crossref verified). Sitemap, blog index, llms.txt updated; IndexNow 200 both endpoints (commit dc2c9c9).

## 2026-10-14 ~01:16 London - Internal linking to new sleep article
- Action: linked the sleep cluster hub-to-spoke: behavior.html #sleep section, anatomy.html legs section ("sleep standing up" anchor) and the FAQ "Do elephants sleep standing up?" answer now link to /blog/how-long-do-elephants-sleep.html.
- Why highest EV: no GSC data yet (token outstanding); the new long-tail article targets "how long do elephants sleep" / "do elephants sleep standing up", and these three evergreen pages already answer the query briefly, so contextual links pass authority and help crawlers find the new URL fast.
- Result: built 42 pages; IndexNow pinged for the 3 changed pages.

## 2026-10-15 ~01:09 London - Daily fact: do elephants use tools?
- Action: published /blog/do-elephants-use-tools.html (fly switches, platform insight, water and hose tool use; 6 Crossref-verified DOIs; FAQ schema; cite box; ~1,197 body words).
- Why highest EV: high-intent long-tail query ("do elephants use tools") with strong peer reviewed evidence; intelligence.html already answered briefly without a dedicated spoke page.
- DOIs: 10.1006/anbe.1993.1183; 10.1006/anbe.1994.1209; 10.1006/anbe.2001.1815; 10.1371/journal.pone.0023251; 10.26451/abc.07.03.04.2020; 10.1016/j.cub.2024.10.017.
- News: no relevant news (Oct 14 to 15 items were local HEC tragedies, a single-source Thailand contraception item, or a week-old Assam GPS report; skipped rather than stretch a NewsArticle).
- SEO follow-up in same slot: contextual link from intelligence.html #tools and FAQ answer to the new article.
- Browser: none used.

## 2026-10-16 ~01:15 London - Daily fact: how long do elephants live?
- Action: published /blog/how-long-do-elephants-live.html (wild vs zoo lifespan, Amboseli and Myanmar timber-camp demography, no menopause, capture costs, molars, TP53; 7 Crossref-verified DOIs; FAQ schema; cite box; ~924 body words, ~1,190 incl. lead and FAQ).
- Why highest EV: "how long do elephants live" is one of the highest-volume elephant fact queries and no existing page answered it; strong peer reviewed evidence base.
- DOIs: 10.1017/S0952836901001212; 10.1007/s00265-015-2051-5; 10.1126/science.1164298; 10.1890/12-0834.1; 10.1186/s12983-014-0054-0; 10.1038/s41467-018-05515-8; 10.1001/jama.2015.13134.
- SEO follow-up in same slot: contextual links to the new article from anatomy.html #teeth (last molar set wearing out) and the faq.html "How long do elephants live?" answer (the page's existing quick answer for this query). Article wording aligned with the FAQ's median figures (max age stated as "into their sixties", not 70).
- News: no relevant news post. Best candidate was the Reuters feature (Japan Times, 15 Oct) on Sri Lanka human-elephant conflict (avg 138 human and 402 elephant deaths a year since 2019, record 488 elephant deaths in 2023, 7,451 wild elephants, ~70% outside protected areas). It is a feature recapping existing DWC statistics rather than a new event, and a two-source fact check plus a NewsArticle template (the build only emits Article/BlogPosting) did not fit the 01:25 deadline. Other items: Malaysia orchard incursions (local), Malawi Kasungu collaring (9 Oct, IFAW release), Assam GPS report (6 Oct). Candidate for a later slot if a fresh Sri Lanka development appears.
- Browser: none used.

## 2026-10-18 (01:05 slot)
- Fact article: blog/why-are-some-elephants-born-without-tusks.html (4 Crossref-verified DOIs: Campbell-Staton et al. 2021, Jachmann et al. 1995, Chiyo et al. 2015, Whitehouse 2002).
- News: published blog/sri-lanka-tusker-kavantissa-dies-after-gunshot-wound.html (Kavantissa died 16 Oct; checked against Daily Mirror x2, Newswire, News 1st, Onlanka, Mongabay; no photos). Added NewsArticle JSON-LD to _build.py via "news": true meta flag.
- SEO action: internal links to the tusklessness article from anatomy.html #tusks, conservation.html (poaching paragraph) and african-vs-asian-elephant.html (tusk callout), building a tusk/ivory topic cluster.

## 2026-10-19 (01:13 slot)
- Fact article: blog/why-do-elephants-throw-mud-and-dust-on-themselves.html (6 Crossref-verified DOIs: Lillywhite and Stein 1987, Wright and Luck 1984, Martins et al. 2018, Dunkin et al. 2013, Mole et al. 2016, Weissenböck et al. 2010).
- News: no new news post. Updated the Kavantissa post: post-mortem done 17 Oct (Prof. Kavindra Wijesundera, Univ. of Peradeniya), samples sent for tests, cause of death still unpublished (Hiru News, Sunday Times SL, 18 Oct).
- SEO action: started a skin/thermoregulation cluster: linked the new article from anatomy.html #skin and added a "Do elephants sweat?" Q&A (in FAQPage JSON-LD) to faq.html linking to it.

## 2026-10-20 (01:05 slot)
- Fact article: blog/how-fast-can-elephants-run.html (5 Crossref-verified DOIs: Hutchinson et al. 2003 Nature, Hutchinson et al. 2006 JEB, Ren and Hutchinson 2008 J R Soc Interface, Genin et al. 2010 JEB, Wall et al. 2006 Curr Biol). Fills a gap: no page answered the high-volume "how fast can an elephant run" query. Linked from anatomy.html #feet.
- News: no new news post. Kavantissa post updated with a dated 20 Oct update: cause of death still unpublished; presidential expert committee appointed 19 Oct (report in 30 days; Newswire, Newscenter.lk); arrests and CID inquiry due 17 Nov (News 1st, LK Post, Onlanka). Other item seen: tusker Agbo found safe at Nachchaduwa (Army.lk, Esana, 19 Oct), minor, not used.
- SEO action: added "How fast can an elephant run?" Q&A (in FAQPage JSON-LD) to faq.html linking to the new article, starting a locomotion/legs cluster with anatomy #feet.
- Browser: none used.

## 2026-10-21 (01:05 slot)
- Fact article: blog/how-much-do-elephants-eat-and-drink.html (4 Crossref-verified DOIs: Clauss et al. 2003 J Anim Physiol Anim Nutr, Clauss et al. 2003 Oecologia, Sukumar 1990 J Trop Ecol, Cerling et al. 2006 PNAS; intake figures from SDZWA and Smithsonian). Targets "how much do elephants eat/drink a day". Linked from habitats #diet and asian-elephant #diet.
- News: published blog/perak-studies-elephant-food-banks-to-curb-conflict.html (NewsArticle; The Star x2, NST, Bernama, FMT; context from Sukumar 1990). Kavantissa: no official cause or committee findings yet; no update (Sunday Times antibiotic claims still unconfirmed).
- SEO action: FAQ "How much does an elephant eat a day?" (FAQPage JSON-LD) on faq.html linking to the article, starting a diet/feeding cluster (habitats, asian-elephant, news post).
- Browser: none used.

## 2026-10-23 (London) site-wide photos and design polish (0f8f9e7)
- Added 10 photorealistic AI-generated, labelled images (images/*.webp, 1280x720, 86-182 KB): home gallery of 3, blog index thumbnails, hero on 5 section pages and 14 fact articles (reused sensibly). None on Kavantissa or Perak news posts. "About our images" note on /about.html#images, footer updated.
- Design polish in style.css/_build.py; fixed bad width attributes on 2 real photos. Contact form verified statically (no test sent). IndexNow pinged for all 50 sitemap URLs.

## 2026-10-23 (London) Google AdSense site code, ads.txt, privacy update
- Added AdSense script and google-adsense-account meta (ca-pub-5681559774142917) to the shared head() in _build.py, so all 51 pages carry them. No ad units, no separate consent banner (Google's consent message comes via the AdSense script).
- ads.txt written by _build.py. Privacy page (/privacy.html, URL unchanged) has a new Advertising section and updated analytics/cookies/lead text; About and Disclaimer no longer say "no ads". Removed "no ads" from the page meta line.
- Removed remaining "no ads" / "no tracking" wording (games index and two game pages meta, teachers index and species fact sheet, games/CREDITS.md); now "free to play/use, no sign-up". No em dashes. 6 pages reindexed via IndexNow.

## 2026-10-25 (London) Daily slot
- Fact article: "How Many Muscles Are in an Elephant's Trunk? Trunk Anatomy Explained" /blog/how-many-muscles-are-in-an-elephant-trunk.html (~990 words, FAQPage 6 Qs, cite box, sources). 6 DOIs verified on Crossref and abstracts checked via Europe PMC: Longren et al. 2023 Curr Biol 10.1016/j.cub.2023.09.007; Eigen et al. 2025 Commun Biol 10.1038/s42003-025-08998-6; Schulz et al. 2021 JRSI 10.1098/rsif.2021.0215; Wu et al. 2018 JRSI 10.1098/rsif.2018.0377; Schulz et al. 2022 PNAS 10.1073/pnas.2122563119; Deiringer et al. 2023 Commun Biol 10.1038/s42003-023-04945-5. Sitemap, blog index, llms.txt rebuilt; IndexNow pinged.
- News: no new post. Kavantissa covered already (Mongabay 24 Oct adds context, noted for the Nov follow-up); Polonnaruwa transit home only one source so far.
- SEO/compliance action: applied Joshua's 24 Oct legal-name rule sitewide. Removed footer copyright/LLC line; JSON-LD Organization name now TuskWise with parentOrganization Joshua Israel Ventures LLC; cite box MLA/Chicago publisher TuskWise; teachers print line, llms.txt, About page and game notes no longer name the LLC; terms, privacy, disclaimer carry the trade-name copyright line. All pages reindexed via IndexNow.
- STATE.md created.

## 2026-10-26 (London) Daily slot
- Fact article: "How Much Does an Elephant Weigh? Weights by Species and Sex" /blog/how-much-does-an-elephant-weigh.html (~840 words, FAQPage 6 Qs, cite box, sources). 3 DOIs verified on Crossref, claims checked against full text/abstracts: Larramendi 2016 Acta Palaeontol Pol 10.4202/app.00136.2014 (open-access PDF read); Mumby et al. 2015 BMC Evol Biol 10.1186/s12862-015-0487-x; Myhrvold et al. 2012 PLoS ONE 10.1371/journal.pone.0047018. (Shrader 2006 and Lee & Moss 1995 considered but dropped: abstracts not accessible to verify.)
- News: "Sri Lanka plans a second Elephant Transit Home in Polonnaruwa" /blog/sri-lanka-plans-second-elephant-transit-home-polonnaruwa.html, NewsArticle JSON-LD, no image; sources News 1st, Newswire, Lanka Leader (24 Oct).
- SEO action: homepage <title> trimmed from 64 to 58 chars ("TuskWise: Elephant Facts, Species, Behavior & Conservation"); og/twitter titles follow. sameAs skipped (no real TuskWise profiles). AdSense kept. IndexNow pinged.

## 2026-10-27 (01:05 slot)
- Fact article: How many teeth do elephants have? (3 Crossref-verified DOIs: Laws 1966, Lee et al. 2012, Roth & Shoshani 1988), FAQ schema, cite box, sitemap, IndexNow.
- News: Sri Lanka armed forces to help protect ~13 wild tuskers (The Island, Sri Lanka Army, Sunday Times, The Morning).
- SEO action: internal link from anatomy.html teeth section to the new teeth article (topical cluster); anatomy modified date bumped.
