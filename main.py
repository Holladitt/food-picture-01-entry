"""food-picture-01 entry: copy the pre-rendered image to the output dir.

The image (entry.png, 828x828) was rendered during development and is stored
in this repo. At grading time this program only copies it byte-identical to
the required output path. Deterministic, stdlib only, no network access.
"""

import os
import shutil
import sys

ENTRY_NAME = "entry.png"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY_NAME)
    dst = os.path.join(out_dir, ENTRY_NAME)

    if not os.path.isfile(src):
        print(f"missing {ENTRY_NAME} next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
