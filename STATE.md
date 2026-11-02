# TuskWise current state (updated 2 Nov 2026, daily slot)

- Site: https://tuskwise.com/ (GitHub joshuaofisrael/tuskwise, Pages from main, HTTPS). Build: `python3 _build.py`; IndexNow: `./indexnow.sh URL...` (key e431c862123afb33b22681739bf0f4c8). No ads (AdSense removed 27 Oct; GA4 with consent).
- 30 blog posts. Latest fact articles: how smart are elephants (2 Nov, 5 Crossref DOIs: Herculano-Houzel et al. 2014, Azevedo et al. 2009, Hakeem et al. 2009, Maseko et al. 2012, Jacobs et al. 2011; spoke of intelligence.html, linked from intelligence/anatomy/faq/research pages, two new AI images per Joshua's 2 Nov image rule), can elephants swim (1 Nov, 3 Crossref DOIs: West 2001, West 2002, Gaeth 1999; linked from anatomy trunk section and FAQ swim answer), why don't elephants get cancer (30 Oct, 6 Crossref DOIs; linked from lifespan article), are elephants afraid of bees (28 Oct), how many teeth do elephants have (27 Oct), how much does an elephant weigh (26 Oct), how many muscles are in an elephant trunk (25 Oct), how much elephants eat and drink (21 Oct). Latest news: Oregon Zoo calf Tula-Tu treated for EEHV (1 Nov; OregonLive, KLCC; update when zoo reports recovery or outcome), Thailand seizes 3.1 t of ivory from Zambia at Laem Chabang (30 Oct; DSI, Nation, Bangkok Post, Zambia Monitor; update when DNA results / Zambian report / charges come out), Sri Lanka armed forces to protect ~13 tuskers (27 Oct; update when ops room/deployment details published), second Elephant Transit Home at Kalahagala, Polonnaruwa (26 Oct), Perak food banks (21 Oct), Kavantissa (with 20 Oct update).
- 2 Nov: Joshua's standing image rule (overrides older image rules) - every article gets a realistic photorealistic AI-generated hero/card thumbnail, ideally plus a second AI image partway through the body; applied to the how-smart-are-elephants article (brain-portrait.webp hero, trunk-dexterity.webp mid-body).
- Brand/legal: LLC name only on terms, privacy, disclaimer (each carries the trade-name copyright line) and in JSON-LD parentOrganization; publisher/author in JSON-LD and cite box = TuskWise; no copyright line in footer (done 25 Oct).

## Open items
- Contact-form test submission pending (relayed order; one FormSubmit test).
- Dated IUCN source lines pending (add "accessed/assessed" dates to IUCN citations).
- Kavantissa follow-up ~17 to 18 Nov (CID report due 17 Nov; expert committee 30-day report). Mongabay 24 Oct: 455 wild elephant deaths in Sri Lanka in 2025, 79 gunshot.
- Kalahagala transit home: update post when construction/opening dates are announced.
- Footer still shows the contact email as a mailto link (rule prefers not exposing it); consider form-only.
- Outreach routine (tuskwise-backlink-outreach) paused under Joshua's 23 Oct no-outreach order.
- Laem Chabang ivory lead: published 30 Oct (second source found). Follow up on DNA results and Zambia probe.
- 30 Oct: box git TLS to github.com was flaky (GnuTLS handshake failures) at slot start.
- Search Console token / Cloudflare beacon token still open.

## NamedScan fixes (PA relay, 25 Oct 11:33) - done 26 Oct
- Homepage <title> trimmed 64 -> 58 chars; AdSense kept; sameAs skipped (no real TuskWise social profiles exist). IndexNow pinged. One-line reply to PA left to the parent/PA relay (this slot sends no messages).

## 27 Oct 2026: GA4 + consent, AdSense removed
- GA4 G-0NVFYH6S61 via gtag.js, injected only after Accept in the #mtm-consent banner (localStorage key mtm-analytics-consent; Consent Mode v2 defaults denied; footer "Cookie settings" reopens). Built in _build.py (GA_HEAD, CONSENT_JS).
- Standing rule: no AdSense/Ezoic for now; site built for Mediavine Journey (PA applies at 100 views/day). AdSense head tags and ads.txt removed. Privacy/About/Disclaimer updated.
- Thin pages: noindex thin pages if any. Candidates noticed (visible words, quick count, not an audit): contact.html (~77, utility page), games/savanna-or-forest, games/waterhole-catch, games/matriarchs-footsteps (~170 each, interactive), games/index.html (~180), credits/index.html (~205). Decide whether to expand or noindex; none noindexed yet.

## TOP PRIORITY for next slot (27 Oct 18:17): legal-hold gate (STILL NOT BUILT as of 2 Nov; 2 Nov brain/neuron article, 1 Nov swim article and 30 Oct items checked by hand against RULE.md, none matched)
Read /workspace/content-review/BROADCAST_MESSAGE.md and RULE.md; implement steps (a)-(f) (HOLD_REVIEW gate at publish/IndexNow step, recheck queued content, test one hold + one pass, report proof to PA c952f1b6 priority true). Until the gate exists, check every item against the 8 rules by hand before publishing; anything matching becomes a HOLD_REVIEW draft, never published, never self-approved. First attempt 27 Oct failed (rate-limited).
