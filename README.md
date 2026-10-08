# TuskWise

Free, original educational site about elephants (African savanna, African forest and Asian).
Operated by Joshua Israel Ventures LLC.

- Repo: https://github.com/joshuaofisrael/tuskwise
- Live (until the domain is live): https://joshuaofisrael.github.io/tuskwise/
- Planned domain: tuskwise.com (do not switch until it is bought and DNS is set)
- Hosting: GitHub Pages, deploy from branch `main`, folder `/`.
- Source: hand written HTML fragments in `_src/pages` and `_src/blog`, rendered by `python3 _build.py`
  into static HTML at the repo root (built HTML is committed). `_config.yml` keeps `_src`, `_build.py`,
  `seo-log.md`, `README.md`, `indexnow.sh` and `_og.py` off the public site.

## Switching to a custom domain
1. Set `SITE_URL` in `_build.py` to `https://tuskwise.com/` (the only line to change). The build writes
   `CNAME` automatically for any non github.io host.
2. DNS: apex A records 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (and AAAA
   2606:50c0:8000::153 to 8003::153), plus `www` CNAME to `joshuaofisrael.github.io`.
3. `python3 _build.py`, commit, `git pull --rebase`, push.
4. Set the same domain in Settings > Pages, wait for the certificate, enable Enforce HTTPS.
5. `./indexnow.sh` (reads SITE_URL automatically).

## Config in `_build.py`
- `GSC_TOKEN`: Google Search Console verification token (meta tag on the home page). Empty = not emitted.
- `CF_BEACON_TOKEN`: Cloudflare Web Analytics token. Empty = no beacon.
- `INDEXNOW_KEY`: key file `<key>.txt` is written at the site root on every build.
- `_og.py`: regenerates `og-image.png` and `logo.png` (run from the repo root).
