#!/usr/bin/env bash
# Ping IndexNow for TuskWise. Usage: ./indexnow.sh URL [URL...]  (no args = all sitemap URLs)
# SITE is read from _build.py so a domain switch needs no edit here.
KEY=e431c862123afb33b22681739bf0f4c8
SITE=$(python3 -c "import re;print(re.search(r'SITE_URL = \"([^\"]+)\"',open('$(dirname "$0")/_build.py').read()).group(1))")
HOST=$(python3 -c "from urllib.parse import urlparse;print(urlparse('$SITE').netloc)")
if [ $# -eq 0 ]; then set -- $(curl -s "${SITE}sitemap.xml" | grep -o '<loc>[^<]*' | sed 's/<loc>//'); fi
LIST=$(printf '%s\n' "$@" | python3 -c 'import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))')
for EP in https://api.indexnow.org/indexnow https://www.bing.com/indexnow; do
curl -s -o /dev/null -w "IndexNow $EP HTTP %{http_code} ($# URLs)\n" -X POST "$EP" \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"${SITE}${KEY}.txt\",\"urlList\":$LIST}"
done
