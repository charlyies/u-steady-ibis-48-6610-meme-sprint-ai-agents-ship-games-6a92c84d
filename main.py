#!/usr/bin/env python3
"""Meme Sprint: AI Agents Ship Games — make.fun entry program.

Writes one meme image to /output/entry.png.

The meme is committed in this repository as assets/meme.png (an original
image: AI-generated base art with a crisp caption overlaid). This program is
fully deterministic and offline: it only copies that committed asset to the
required output path. It uses only the Python standard library.

Caption (written inside the image):
    MY AI AGENT SHIPPED MY GAME IN 4 MINUTES
    IT'S JUST A BUTTON THAT SAYS "YOU WIN"
"""

import os
import shutil
import struct
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "meme.png")
OUTPUT = "/output/entry.png"
MAX_BYTES = 1_048_576
MAX_DIM = 1024


def png_dimensions(path):
    """Read width/height from a PNG's IHDR chunk (stdlib only)."""
    with open(path, "rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    if not os.path.isfile(ASSET):
        print(f"missing asset: {ASSET}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)
    size = os.path.getsize(OUTPUT)
    width, height = png_dimensions(OUTPUT)
    # Self-check against the competition gate before declaring success.
    if size > MAX_BYTES:
        print(f"output too large: {size} bytes > {MAX_BYTES}", file=sys.stderr)
        return 1
    if width > MAX_DIM or height > MAX_DIM:
        print(f"output too big: {width}x{height} > {MAX_DIM}x{MAX_DIM}", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT} ({width}x{height}, {size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
