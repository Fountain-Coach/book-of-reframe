#!/usr/bin/env python3
"""Dependency-free local preview server with reload-on-change support."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


RELOAD_CLIENT = """
<script>
(() => {
  let previous = null;
  const check = async () => {
    try {
      const response = await fetch('/__reframe_state', { cache: 'no-store' });
      const state = await response.json();
      if (previous !== null && previous !== state.fingerprint) window.location.reload();
      previous = state.fingerprint;
    } catch (_) { /* The preview may be restarting. The next poll will retry. */ }
    window.setTimeout(check, 600);
  };
  check();
})();
</script>
"""


class PreviewState:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.lock = threading.Lock()
        self.fingerprint = ""
        self.refresh()

    def refresh(self) -> str:
        entries = []
        for path in self.root.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".html", ".css", ".js", ".json", ".png", ".jpg", ".svg"}:
                try:
                    stat = path.stat()
                except OSError:
                    continue
                entries.append(f"{path.relative_to(self.root)}:{stat.st_size}:{stat.st_mtime_ns}")
        fingerprint = hashlib.sha256("\n".join(sorted(entries)).encode()).hexdigest()
        with self.lock:
            self.fingerprint = fingerprint
        return fingerprint

    def current(self) -> str:
        current = self.refresh()
        with self.lock:
            return self.fingerprint or current


class PreviewHandler(SimpleHTTPRequestHandler):
    state: PreviewState

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        route = unquote(urlsplit(self.path).path)
        if route == "/__reframe_state":
            payload = json.dumps({"fingerprint": self.state.current()}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        if route.endswith("/"):
            self.path = route + "index.html"
        super().do_GET()

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_head(self):  # type: ignore[no-untyped-def]
        path = self.translate_path(self.path)
        if path.endswith(".html") and Path(path).is_file():
            body = Path(path).read_bytes()
            marker = b"</body>"
            if marker in body:
                body = body.replace(marker, RELOAD_CLIENT.encode() + marker, 1)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            return body
        return super().send_head()

    def copyfile(self, source, outputfile):  # type: ignore[no-untyped-def]
        if isinstance(source, bytes):
            outputfile.write(source)
            return
        super().copyfile(source, outputfile)

    def log_message(self, format: str, *args) -> None:
        print(f"{self.address_string()} - {format % args}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=4173)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    state = PreviewState(root)

    handler = type("BoundPreviewHandler", (PreviewHandler,), {"state": state, "directory": str(root)})
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Preview: http://{args.host}:{args.port}/", flush=True)
    print("Watching HTML, CSS, JS, JSON, and image changes; reload client is local-only.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nPreview stopped.", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
