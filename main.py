#!/usr/bin/env python3
"""Entry program for the make.fun bounty "news-image-20261122".

Copies the pre-built news image (news.png, sitting next to this file)
into the grader's output directory as entry.png.

The output directory comes from MAKEFUN_OUTPUT_DIR when the harness
sets it, and falls back to /output. The program is deterministic:
no network, no randomness, no clock reads -- every run writes the
same bytes. It never changes permissions on anything.
"""

import os
import shutil
import sys


def entry_image_path():
    """Absolute path of the image shipped beside this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "news.png")


def output_path():
    """Destination path inside the grader's output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.png")


def main() -> int:
    source = entry_image_path()
    target = output_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.copyfile(source, target)
    size = os.path.getsize(target)
    if size != os.path.getsize(source):
        raise SystemExit(
            "copy incomplete: wrote {} bytes, expected {}".format(
                size, os.path.getsize(source)
            )
        )
    print("wrote {} ({} bytes)".format(target, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
