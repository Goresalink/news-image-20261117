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
two runs write identical bytes. The output is verified after writing: it must
exist and stay within the contest's 1 MiB size limit.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "frontpage.png")
DEST = "/output/entry.png"
MAX_BYTES = 1024 * 1024  # contest limit: entry image must be <= 1 MiB


def ensure_output_dir(path):
    """Create the output directory if missing (robust to a fresh /output)."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def main():
    ensure_output_dir(DEST)
    shutil.copyfile(SOURCE, DEST)
    size = os.path.getsize(DEST)  # raises if the copy did not land
    if size > MAX_BYTES:
        raise SystemExit(
            f"output too large: {size} bytes exceeds the 1 MiB limit"
        )
    print(f"wrote {DEST} ({size} bytes)")


if __name__ == "__main__":
    main()
