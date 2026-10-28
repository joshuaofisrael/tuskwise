# TuskWise current state (updated 28 Oct 2026, ~01:27 London)

- Site: https://tuskwise.com/ (GitHub joshuaofisrael/tuskwise, Pages from main, HTTPS). Build: `python3 _build.py`; IndexNow: `./indexnow.sh URL...` (key e431c862123afb33b22681739bf0f4c8). No ads (AdSense removed 27 Oct; GA4 with consent).
- 25 blog posts. Latest fact articles: are elephants afraid of bees (28 Oct), how many teeth do elephants have (27 Oct), how much does an elephant weigh (26 Oct), how many muscles are in an elephant trunk (25 Oct), how much elephants eat and drink (21 Oct). Latest news: Sri Lanka armed forces to protect ~13 tuskers (27 Oct; update when ops room/deployment details published), second Elephant Transit Home at Kalahagala, Polonnaruwa (26 Oct), Perak food banks (21 Oct), Kavantissa (with 20 Oct update).
- Brand/legal: LLC name only on terms, privacy, disclaimer (each carries the trade-name copyright line) and in JSON-LD parentOrganization; publisher/author in JSON-LD and cite box = TuskWise; no copyright line in footer (done 25 Oct).

## Open items
- Contact-form test submission pending (relayed order; one FormSubmit test).
- Dated IUCN source lines pending (add "accessed/assessed" dates to IUCN citations).
- Kavantissa follow-up ~17 to 18 Nov (CID report due 17 Nov; expert committee 30-day report). Mongabay 24 Oct: 455 wild elephant deaths in Sri Lanka in 2025, 79 gunshot.
- Kalahagala transit home: update post when construction/opening dates are announced.
- Footer still shows the contact email as a mailto link (rule prefers not exposing it); consider form-only.
- Outreach routine (tuskwise-backlink-outreach) paused under Joshua's 23 Oct no-outreach order.
- News lead (28 Oct, not posted, time): Thailand Laem Chabang seizure of 469 African elephant tusks (~3.04 t) from Zambia (Bangkok Post 27 Oct); needs 2nd source; no named individuals.
- Search Console token / Cloudflare beacon token still open.

## NamedScan fixes (PA relay, 25 Oct 11:33) - done 26 Oct
- Homepage <title> trimmed 64 -> 58 chars; AdSense kept; sameAs skipped (no real TuskWise social profiles exist). IndexNow pinged. One-line reply to PA left to the parent/PA relay (this slot sends no messages).

## 27 Oct 2026: GA4 + consent, AdSense removed
- GA4 G-0NVFYH6S61 via gtag.js, injected only after Accept in the #mtm-consent banner (localStorage key mtm-analytics-consent; Consent Mode v2 defaults denied; footer "Cookie settings" reopens). Built in _build.py (GA_HEAD, CONSENT_JS).
- Standing rule: no AdSense/Ezoic for now; site built for Mediavine Journey (PA applies at 100 views/day). AdSense head tags and ads.txt removed. Privacy/About/Disclaimer updated.
- Thin pages: noindex thin pages if any. Candidates noticed (visible words, quick count, not an audit): contact.html (~77, utility page), games/savanna-or-forest, games/waterhole-catch, games/matriarchs-footsteps (~170 each, interactive), games/index.html (~180), credits/index.html (~205). Decide whether to expand or noindex; none noindexed yet.

## TOP PRIORITY for next slot (27 Oct 18:17): legal-hold gate
Read /workspace/content-review/BROADCAST_MESSAGE.md and RULE.md; implement steps (a)-(f) (HOLD_REVIEW gate at publish/IndexNow step, recheck queued content, test one hold + one pass, report proof to PA c952f1b6 priority true). Until the gate exists, check every item against the 8 rules by hand before publishing; anything matching becomes a HOLD_REVIEW draft, never published, never self-approved. First attempt 27 Oct failed (rate-limited).
