# ElephantWise

Free, original educational site about elephants (African savanna, African forest and Asian).
Operated by Joshua Israel Ventures LLC.

- Live (until a domain is chosen): https://joshuaofisrael.github.io/elephantwise/
- Hosting: GitHub Pages, deploy from branch `main`, folder `/`.
- Source: hand written HTML fragments in `_src/pages` and `_src/blog`, rendered by `python3 _build.py`
  into static HTML at the repo root (built HTML is committed). `_config.yml` keeps `_src`, `_build.py`,
  `seo-log.md`, `README.md` and `indexnow.sh` off the public site.

## Switching to a custom domain
1. Set `SITE_URL` in `_build.py` (the only place the base URL lives), e.g. `https://example.com/`.
2. Add a `CNAME` file containing the bare domain.
3. `python3 _build.py`, commit, `git pull --rebase`, push.
4. Set the same domain in Settings > Pages, wait for the certificate, enable Enforce HTTPS.
5. `./indexnow.sh` (reads SITE_URL automatically).

## Config in `_build.py`
- `GSC_TOKEN`: Google Search Console verification token (meta tag on the home page). Empty = not emitted.
- `CF_BEACON_TOKEN`: Cloudflare Web Analytics token. Empty = no beacon.
- `INDEXNOW_KEY`: key file `<key>.txt` is written at the site root on every build.
