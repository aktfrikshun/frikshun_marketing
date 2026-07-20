#!/usr/bin/env python3
"""Render deterministic, cover-matched 16:9 music credits."""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


WIDTH, HEIGHT = 1920, 1080
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def fit_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def wrapped_title(title: str) -> str:
    return "\n".join(textwrap.wrap(title.upper(), width=28, break_long_words=False))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cover", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--main-out", required=True)
    parser.add_argument("--accent", required=True)
    parser.add_argument("--collection", required=True)
    parser.add_argument("--track-label", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--artist", required=True)
    parser.add_argument("--credit-role", required=True)
    parser.add_argument("--credit-name", required=True)
    args = parser.parse_args()

    accent = tuple(bytes.fromhex(args.accent))
    source = Image.open(args.cover).convert("RGB")
    background = fit_cover(source, (WIDTH, HEIGHT)).filter(ImageFilter.GaussianBlur(34))
    background = ImageEnhance.Brightness(background).enhance(0.34)
    background = ImageEnhance.Color(background).enhance(0.72)
    tint = Image.new("RGB", (WIDTH, HEIGHT), accent)
    background = Image.blend(background, tint, 0.12)

    main_canvas = background.convert("RGBA")
    main_card = fit_cover(source, (860, 860))
    main_card = ImageOps.expand(main_card, border=2, fill=(225, 228, 232))
    main_canvas.alpha_composite(main_card.convert("RGBA"), ((WIDTH - main_card.width) // 2, (HEIGHT - main_card.height) // 2))
    Path(args.main_out).parent.mkdir(parents=True, exist_ok=True)
    main_canvas.convert("RGB").save(args.main_out, quality=95)

    canvas = background.convert("RGBA")
    card = fit_cover(source, (650, 650))
    card = ImageOps.expand(card, border=2, fill=(225, 228, 232))
    canvas.alpha_composite(card.convert("RGBA"), (74, 214))

    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rounded_rectangle((790, 104, 1805, 975), radius=24, fill=(7, 9, 11, 205), outline=(*accent, 155), width=2)
    draw.rectangle((790, 104, 795, 975), fill=(*accent, 245))
    canvas = Image.alpha_composite(canvas, overlay)
    draw = ImageDraw.Draw(canvas)

    x = 850
    draw.text((x, 170), f"{args.collection.upper()}  /  {args.track_label.upper()}", font=font(FONT_REGULAR, 25), fill=(*accent, 255))
    title_text = wrapped_title(args.title)
    draw.multiline_text((x, 255), title_text, font=font(FONT_BOLD, 50), fill=(245, 247, 248), spacing=8)
    title_lines = title_text.count("\n") + 1
    artist_y = 385 + (title_lines - 1) * 58
    draw.text((x, artist_y), "A SONG BY", font=font(FONT_REGULAR, 22), fill=(155, 162, 168))
    draw.text((x, artist_y + 38), args.artist.upper(), font=font(FONT_REGULAR, 34), fill=(245, 247, 248))
    credit_y = artist_y + 142
    draw.text((x, credit_y), args.credit_role.upper(), font=font(FONT_REGULAR, 22), fill=(155, 162, 168))
    draw.text((x, credit_y + 38), args.credit_name.upper(), font=font(FONT_REGULAR, 32), fill=(218, 221, 224))
    draw.line((x, 860, 1735, 860), fill=(*accent, 145), width=2)
    draw.text((x, 893), "FRIKSHUN.COM/ARCHIVES/CHLOE-KATASTROPHE/SITE", font=font(FONT_REGULAR, 16), fill=(145, 152, 158))

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(args.out, quality=95)


if __name__ == "__main__":
    main()
