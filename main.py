"""Food picture entry: copy the bundled ramen image to the output dir.

Deterministic, stdlib only, no network. The image is shipped in the
repository as entry.png next to this script; this program copies it
byte-for-byte to <output>/entry.png.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)


if __name__ == "__main__":
    main()

# Notes on the image (round 4, candidate d1):
# Winner-recipe clone: dark speckled bowl, golden glossy noodle pull
# with chili flakes, off-centre ajitama with a thick yolk drip, tight
# chashu fan on one side, nori sheet, scallion mound, scattered red
# chili oil on ivory broth, thick steam, warm amber bokeh background.
# The copy is exact, so two runs produce byte-identical output.
