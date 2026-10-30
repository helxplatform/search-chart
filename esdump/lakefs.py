"""Minimal lakeFS client for the esdump jobs: upload, commit, download.

Stdlib only, so the image carries no lakectl (and none of its Go dependency
CVEs). Every transfer goes through the lakeFS API itself, never to pre-signed
URLs on the backing object store.

Reads LAKECTL_SERVER_ENDPOINT_URL, LAKECTL_CREDENTIALS_ACCESS_KEY_ID and
LAKECTL_CREDENTIALS_SECRET_ACCESS_KEY.

  lakefs.py upload   <repo> <branch> <path> <local file>
  lakefs.py commit   <repo> <branch> <message> [key=value ...]
  lakefs.py download <repo> <ref> <path> <local file>
"""
import base64
import json
import os
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request


def call(method, url_path, query=None, body=None, content_type=None, length=None):
    base = os.environ["LAKECTL_SERVER_ENDPOINT_URL"].rstrip("/")
    if not base.endswith("/api/v1"):
        base += "/api/v1"
    url = base + url_path + ("?" + urllib.parse.urlencode(query) if query else "")
    creds = f'{os.environ["LAKECTL_CREDENTIALS_ACCESS_KEY_ID"]}:{os.environ["LAKECTL_CREDENTIALS_SECRET_ACCESS_KEY"]}'
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", "Basic " + base64.b64encode(creds.encode()).decode())
    if content_type:
        req.add_header("Content-Type", content_type)
    if length is not None:
        req.add_header("Content-Length", str(length))
    return urllib.request.urlopen(req)


def main(cmd, repo, ref, *rest):
    r, b = urllib.parse.quote(repo, safe=""), urllib.parse.quote(ref, safe="")
    if cmd == "upload":
        path, src = rest
        with open(src, "rb") as f:
            call("POST", f"/repositories/{r}/branches/{b}/objects", {"path": path},
                 f, "application/octet-stream", os.path.getsize(src)).read()
    elif cmd == "commit":
        message, *meta = rest
        body = json.dumps({"message": message, "metadata": dict(m.split("=", 1) for m in meta)}).encode()
        commit = json.load(call("POST", f"/repositories/{r}/branches/{b}/commits", body=body,
                                content_type="application/json"))
        print("committed", commit["id"])
    elif cmd == "download":
        path, dest = rest
        with call("GET", f"/repositories/{r}/refs/{b}/objects", {"path": path}) as resp, open(dest, "wb") as out:
            shutil.copyfileobj(resp, out)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    try:
        main(*sys.argv[1:])
    except urllib.error.HTTPError as e:
        sys.exit(f"lakeFS {e.code}: {e.read().decode(errors='replace')}")
