"""Wallet 3 entry for news-image-20261117: minimal iconography.

Picture summary: a near-white page headed by a giant red "17" and the
words NOVEMBER 2026. Eight flat icons in coloured rings stand for eight
headlines of Tuesday 17 November 2026: a bridge for the Kerch strike, a
drone for Bahrain, a jet for Japan, a virus for measles in America, an
aircraft for the Russian crash, a house for the settlement sanctions, a
leaf for COP31, and a crowd for the marches in France.

The eight captions are listed in this program as data. Publishing walks
that list once (for the printed manifest) and then writes the bundled
picture to the output folder with a single write of its full contents,
after confirming the contents start with a PNG or JPEG signature.
"""
import os
import sys

FOLDER = os.path.dirname(os.path.abspath(__file__))
PICTURE_PATH = os.path.join(FOLDER, "entry.png")
CAPTIONS = [
    "Ukraine hits Kerch Bridge",
    "Iran drones target Bahrain",
    "Japan scrambles jets",
    "US loses measles-free status",
    "Russian warplane crash kills 19",
    "UK sanctions settlement builders",
    "COP31 draft: $120bn for climate",
    "146,000 march across France",
]
SIGNATURES = {b"\x89PNG": "PNG", b"\xff\xd8": "JPEG"}


def detect_format(blob):
    for signature, label in SIGNATURES.items():
        if blob.startswith(signature):
            return label
    return None


def run():
    with open(PICTURE_PATH, "rb") as handle:
        blob = handle.read()
    label = detect_format(blob)
    if label is None:
        raise SystemExit("bundled picture has an unknown signature")
    out_folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_folder, exist_ok=True)
    destination = os.path.join(out_folder, "entry.png")
    with open(destination, "wb") as handle:
        handle.write(blob)
    print(f"destination folder ready: {out_folder}")
    for position, caption in enumerate(CAPTIONS, start=1):
        print(f"symbol {position} of {len(CAPTIONS)}: {caption}")
    print(f"{label} picture published in one write: {len(blob)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(run())
