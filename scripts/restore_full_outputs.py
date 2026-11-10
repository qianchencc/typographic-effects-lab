#!/usr/bin/env python3
"""Restore archived binary output chunks to an exactly checksum-matched PNG."""
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "assets/outputs/04-wave-memory.png"
parts = [ROOT / f"assets/outputs/chunks/04-wave-memory.png.part0{i}" for i in (1, 2)]
expected = "b690dfd086abcf36996e3e3faf61373d4be73bc44a86ce850fea18f9c6e6eb3b"
if not all(p.is_file() for p in parts):
    sys.exit("Missing one or more archived PNG chunks")
data = b"".join(p.read_bytes() for p in parts)
actual = hashlib.sha256(data).hexdigest()
if actual != expected:
    sys.exit(f"Checksum mismatch: got {actual}, expected {expected}")
if out.exists() and out.read_bytes() != data:
    sys.exit("Existing output differs from archived bytes; refusing overwrite")
out.write_bytes(data)
print(f"Restored {out.relative_to(ROOT)} ({len(data)} bytes; SHA256 {actual})")
