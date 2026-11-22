#!/usr/bin/env python3
"""Entry program for make.fun bounty 'news-image-20261122'.

Writes the pre-built news-summary image to /output/entry.png.
Deterministic: no network, no randomness, no time dependence —
every run writes the exact same bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")


def main() -> int:
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
