#!/usr/bin/env python3
"""Check original generation outputs by file size, hash, dimensions and color mode."""
from pathlib import Path
import hashlib
import json
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
records = json.loads((ROOT / "data/asset-manifest.json").read_text(encoding="utf-8"))
ok = True
for item in records:
    file = ROOT / "assets" / item["file"]
    if not file.exists():
        print(f"MISSING {file.relative_to(ROOT)}")
        ok = False
        continue
    raw = file.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    png = raw[:8] == b"\x89PNG\r\n\x1a\n"
    if png and len(raw) >= 26:
        width, height = struct.unpack(">II", raw[16:24])
        color = raw[25]  # 2 = RGB, 6 = RGBA
    else:
        width, height, color = None, None, None
    valid = (sha == item["sha256"] and len(raw) == item["bytes"] and png
             and (width, height) == (item["width"], item["height"])
             and color == 2)
    print(("OK" if valid else "FAIL"), item["file"], f"{width}x{height}", sha)
    ok &= valid
sys.exit(0 if ok else 1)
