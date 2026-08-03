#!/usr/bin/env bash
set -euo pipefail

port="${1:-4173}"
host="127.0.0.1"
url="http://${host}:${port}/"
site_dir="$(cd "$(dirname "$0")" && pwd)"
pid_file="${TMPDIR:-/tmp}/book-of-reframe-preview-${port}.pid"
log_file="${TMPDIR:-/tmp}/book-of-reframe-preview-${port}.log"

if ! curl --silent --show-error --fail --connect-timeout 1 --max-time 2 "$url" >/dev/null 2>&1; then
  if [[ -f "$pid_file" ]] && ! kill -0 "$(<"$pid_file")" 2>/dev/null; then
    rm -f "$pid_file"
  fi
  if [[ ! -f "$pid_file" ]]; then
    (cd "$site_dir" && nohup python3 dev-server.py --host "$host" --port "$port" >"$log_file" 2>&1 & echo $! >"$pid_file")
    for _ in {1..20}; do
      curl --silent --show-error --fail --connect-timeout 1 --max-time 1 "$url" >/dev/null 2>&1 && break
      sleep .1
    done
  fi
fi

if command -v open >/dev/null 2>&1; then
  open "$url"
else
  echo "System browser launcher unavailable. Open $url"
fi
echo "Book preview: $url"
