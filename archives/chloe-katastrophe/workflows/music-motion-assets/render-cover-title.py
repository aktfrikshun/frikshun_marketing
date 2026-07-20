#!/usr/bin/env python3
"""Add deterministic release typography to text-free square cover art."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", required=True)
    args = parser.parse_args()

    image = Image.open(args.input).convert("RGBA")
    width, height = image.size
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((0, 0, width, int(height * 0.31)), fill=(3, 10, 18, 126))
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=7))
    image = Image.alpha_composite(image, overlay)
    draw = ImageDraw.Draw(image)

    margin = int(width * 0.065)
    title_font = ImageFont.truetype(FONT, int(width * 0.095))
    subtitle_font = ImageFont.truetype(FONT_BOLD, int(width * 0.025))
    draw.text((margin, int(height * 0.07)), args.title, font=title_font, fill=(244, 239, 224), stroke_width=1, stroke_fill=(5, 12, 20))
    draw.line((margin, int(height * 0.205), int(width * 0.45), int(height * 0.205)), fill=(210, 143, 67), width=max(2, width // 500))
    draw.text((margin, int(height * 0.225)), args.subtitle.upper(), font=subtitle_font, fill=(213, 219, 224))

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(args.out, quality=96)


if __name__ == "__main__":
    main()
