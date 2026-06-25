#!/usr/bin/env python3
import hashlib, json, os, sys, re, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

def sha1(p):
    h = hashlib.sha1()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def read_version():
    src = (ROOT / "manifest.yaml").read_text()
    m = re.search(r"^version:\s*(\S+)", src, re.M)
    return m.group(1) if m else "v0.0.0"

def collect(group):
    d = ROOT / group
    out = []
    if not d.exists():
        return out
    for f in sorted(d.glob("*.yaml")):
        out.append({"file": f"{group}/{f.name}", "sha1": sha1(f)})
    return out

manifest = {
    "version": read_version(),
    "generated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "boards": collect("boards"),
    "sensors": collect("sensors"),
    "snippets": collect("snippets"),
}
(ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print(f"wrote manifest.json (version={manifest['version']}, "
      f"boards={len(manifest['boards'])}, "
      f"sensors={len(manifest['sensors'])}, "
      f"snippets={len(manifest['snippets'])})")
