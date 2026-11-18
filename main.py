#!/usr/bin/env python3
"""News image entry for make.fun bounty news-image-20261117.

Writes the front page summing up the world news of Tuesday 17 November 2026
to /output/entry.png. The front page (frontpage.png, bundled in this repo) is
a collage of four real news photos of the day's top stories:

  - Iran fired drones at a U.S. military radar in Bahrain
  - Ukraine's strike damaged the Crimea (Kerch) Bridge
  - Trump travelled to Asia for APEC and planned nuclear talks with Xi and Putin
  - Japan scrambled fighter jets after suspected Russian aircraft violated
    its airspace

No network access is needed: the program only copies the bundled image, so
two runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "frontpage.png")
DEST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print(f"wrote {DEST} ({os.path.getsize(DEST)} bytes)")


if __name__ == "__main__":
    main()
