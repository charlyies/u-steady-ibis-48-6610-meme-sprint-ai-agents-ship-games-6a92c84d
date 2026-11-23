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
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "meme.png")
OUTPUT = "/output/entry.png"


def main() -> int:
    if not os.path.isfile(ASSET):
        print(f"missing asset: {ASSET}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)
    size = os.path.getsize(OUTPUT)
    print(f"wrote {OUTPUT} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
