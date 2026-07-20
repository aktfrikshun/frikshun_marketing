#!/usr/bin/env python3
"""Build a labeled QA sheet from YouTube edition credit frames."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frames", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    frame_dir = Path(args.frames)
    frames = sorted(frame_dir.glob("*.jpg"))
    if not frames:
        raise SystemExit("No QA frames found")

    columns, cell_w, image_h, label_h = 3, 640, 360, 48
    rows = (len(frames) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_w, rows * (image_h + label_h)), "#07090b")
    draw = ImageDraw.Draw(sheet)
    label_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 20)
    for index, path in enumerate(frames):
        x = (index % columns) * cell_w
        y = (index // columns) * (image_h + label_h)
        frame = ImageOps.fit(Image.open(path).convert("RGB"), (cell_w, image_h), method=Image.Resampling.LANCZOS)
        sheet.paste(frame, (x, y))
        label = path.stem.replace("-credits", "").replace("-", " ").title()
        draw.text((x + 14, y + image_h + 12), label, font=label_font, fill="#e8ebed")
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.out, quality=90)


if __name__ == "__main__":
    main()
