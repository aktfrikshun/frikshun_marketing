#!/usr/bin/env python3
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OVERLAYS = ROOT / "overlays"
SIZE = (1080, 1920)
AVENIR = "/System/Library/Fonts/Avenir Next.ttc"
BASKERVILLE = "/System/Library/Fonts/Supplemental/Baskerville.ttc"


def font(path, size, index=0):
    return ImageFont.truetype(path, size=size, index=index)


def canvas():
    image = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    return image, ImageDraw.Draw(image)


def center_text(draw, y, text, face, fill, shadow=True, stroke=0):
    box = draw.textbbox((0, 0), text, font=face, stroke_width=stroke)
    x = (SIZE[0] - (box[2] - box[0])) / 2
    if shadow:
        draw.text((x, y + 5), text, font=face, fill=(0, 0, 0, 205), stroke_width=stroke)
    draw.text((x, y), text, font=face, fill=fill, stroke_width=stroke)


def spaced_text(draw, y, text, face, fill, spacing):
    widths = [draw.textlength(char, font=face) for char in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x = (SIZE[0] - total) / 2
    for char, width in zip(text, widths):
        draw.text((x, y + 4), char, font=face, fill=(0, 0, 0, 190))
        draw.text((x, y), char, font=face, fill=fill)
        x += width + spacing


def save(image, name):
    image.save(OVERLAYS / name, format="PNG", optimize=True)


def render():
    OVERLAYS.mkdir(parents=True, exist_ok=True)

    image, draw = canvas()
    spaced_text(draw, 126, "A NEW RECOVERED RECORDING", font(AVENIR, 30), (230, 197, 184, 255), 6)
    draw.line((300, 207, 780, 207), fill=(215, 169, 149, 190), width=2)
    spaced_text(draw, 222, "TOMORROW WE MET", font(BASKERVILLE, 58), (246, 238, 233, 255), 6)
    spaced_text(draw, 300, "CHLOE KATASTROPHE", font(AVENIR, 25), (216, 181, 168, 255), 5)
    save(image, "01-recovered-recording.png")

    image, draw = canvas()
    center_text(draw, 1395, "What if love survives", font(BASKERVILLE, 59, 2), (255, 248, 242, 255))
    center_text(draw, 1469, "even when memory does not?", font(BASKERVILLE, 59, 2), (255, 248, 242, 255))
    save(image, "02-question.png")

    image, draw = canvas()
    center_text(draw, 1388, "She remembers", font(BASKERVILLE, 65), (255, 248, 242, 255))
    center_text(draw, 1470, "the feeling first.", font(BASKERVILLE, 69, 2), (230, 185, 170, 255))
    save(image, "03-feeling-first.png")

    image, draw = canvas()
    center_text(draw, 1370, "The comfort. The warmth.", font(BASKERVILLE, 65), (255, 248, 242, 255))
    center_text(draw, 1453, "The quiet certainty that someone", font(BASKERVILLE, 51, 2), (217, 181, 168, 255))
    center_text(draw, 1519, "once made the world feel like home.", font(BASKERVILLE, 51, 2), (217, 181, 168, 255))
    save(image, "04-comfort-warmth.png")

    image, draw = canvas()
    spaced_text(draw, 1360, "TOMORROW WE MET", font(BASKERVILLE, 72), (255, 248, 242, 255), 4)
    spaced_text(draw, 1460, "OUT NOW", font(AVENIR, 36), (226, 182, 167, 255), 9)
    draw.line((330, 1554, 750, 1554), fill=(215, 169, 149, 215), width=2)
    spaced_text(draw, 1572, "CHLOE KATASTROPHE", font(AVENIR, 25), (238, 225, 218, 255), 5)
    save(image, "05-out-now.png")


if __name__ == "__main__":
    render()
