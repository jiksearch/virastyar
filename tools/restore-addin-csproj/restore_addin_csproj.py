#!/usr/bin/env python3
"""Restore full Add-in csproj files from base64 chunks in tools/restore-addin-csproj/"""
import base64, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHUNK_DIR = os.path.dirname(os.path.abspath(__file__))

TARGETS = {
    "addin2010": os.path.join(ROOT, "VirastyarWordAddin", "VirastyarWordAddin2010", "VirastyarWordAddin.csproj"),
    "addin_legacy": os.path.join(ROOT, "VirastyarWordAddin", "VirastyarWordAddin", "VirastyarWordAddin.csproj"),
}

def restore(name, dest):
    parts = sorted(f for f in os.listdir(CHUNK_DIR) if f.startswith(name + ".part") and f.endswith(".b64"))
    if not parts:
        print(f"ERROR: no chunks for {name}")
        return False
    data = "".join(open(os.path.join(CHUNK_DIR, p)).read().strip() for p in parts)
    raw = base64.b64decode(data)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "wb").write(raw)
    print(f"OK {dest} ({len(raw)} bytes)")
    return True

ok = True
for name, dest in TARGETS.items():
    ok = restore(name, dest) and ok
sys.exit(0 if ok else 1)
