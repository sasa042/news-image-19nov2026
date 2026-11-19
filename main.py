#!/usr/bin/env python3
"""make.fun bounty entry: news-image-20261119.

Sum up the world's news of Thursday 19 November 2026 in one image.

The entry image is ``entry.png`` in this repository. This program simply
copies it to ``/output/entry.png``. It uses only the standard library,
makes no network calls, and is fully deterministic: every run writes
the exact same bytes.
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> int:
    if not SRC.is_file():
        print(f"missing source image: {SRC}", file=sys.stderr)
        return 1
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    digest = hashlib.sha256(DST.read_bytes()).hexdigest()
    print(f"wrote {DST} ({DST.stat().st_size} bytes, sha256={digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
