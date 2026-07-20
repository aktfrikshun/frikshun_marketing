#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
COVER = ROOT / "rodnoy-dom-cover.png"
OUT = ROOT / "rodnoy-dom-credits.png"
REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

source = Image.open(COVER).convert("RGB")
background = ImageOps.fit(source, (1080, 1080), method=Image.Resampling.LANCZOS)
background = background.filter(ImageFilter.GaussianBlur(30))
background = ImageEnhance.Brightness(background).enhance(0.28)
background = ImageEnhance.Color(background).enhance(0.65).convert("RGBA")

veil = Image.new("RGBA", background.size, (5, 15, 27, 90))
canvas = Image.alpha_composite(background, veil)
draw = ImageDraw.Draw(canvas)
amber = (210, 143, 67, 255)
white = (242, 244, 245, 255)
muted = (164, 180, 194, 255)

draw.rounded_rectangle((120, 120, 960, 960), radius=26, fill=(4, 12, 22, 215), outline=(210, 143, 67, 170), width=2)
draw.rectangle((120, 120, 127, 960), fill=amber)
draw.text((540, 220), "DAUGHTER OF ECHOES  /  TRACK 12", anchor="mm", font=ImageFont.truetype(REGULAR, 25), fill=amber)
draw.text((540, 365), "РОДНОЙ ДОМ", anchor="mm", font=ImageFont.truetype(BOLD, 62), fill=white)
draw.text((540, 435), "RODNOY DOM", anchor="mm", font=ImageFont.truetype(REGULAR, 25), fill=muted)
draw.line((260, 510, 820, 510), fill=(210, 143, 67, 135), width=2)
draw.text((540, 575), "A SONG BY", anchor="mm", font=ImageFont.truetype(REGULAR, 21), fill=muted)
draw.text((540, 625), "CHLOE KATASTROPHE", anchor="mm", font=ImageFont.truetype(BOLD, 35), fill=white)
draw.text((540, 720), "ARCHIVE / CREATIVE DIRECTION", anchor="mm", font=ImageFont.truetype(REGULAR, 20), fill=muted)
draw.text((540, 768), 'ALLEN "FRIKSHUN" TAYLOR', anchor="mm", font=ImageFont.truetype(REGULAR, 29), fill=white)
draw.text((540, 885), "FRIKSHUN.COM/ARCHIVES/CHLOE-KATASTROPHE/SITE", anchor="mm", font=ImageFont.truetype(REGULAR, 15), fill=muted)
canvas.convert("RGB").save(OUT, quality=96)
