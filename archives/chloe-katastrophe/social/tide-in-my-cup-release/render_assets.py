from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "tide-in-my-cup-foxy-source.png"
ART = ROOT / "tide-in-my-cup-cover-art-v2.png"
COVER = ROOT / "tide-in-my-cup-cover-v2.png"
COVER_JPG = ROOT / "tide-in-my-cup-cover-v2.jpg"
STORY = ROOT / "tide-in-my-cup-story-v2.png"
FONT = "/System/Library/Fonts/Avenir Next.ttc"

source = Image.open(SOURCE).convert("RGB")

# Square crop keeps Chloe, the drink, falling sand, camera bag, palms, and sea.
crop_size = source.width
top = 430
square = source.crop((0, top, crop_size, top + crop_size))
square = square.resize((3000, 3000), Image.Resampling.LANCZOS)
square.save(ART, optimize=True)

# Typography is layered without regenerating or altering Chloe's identity.
cover = square.convert("RGBA")
shade = Image.new("RGBA", cover.size, (0, 0, 0, 0))
shade_px = shade.load()
for x in range(3000):
    left = max(0.0, 1.0 - x / 1480.0)
    top_weight = max(0.0, 1.0 - x / 1900.0) * max(0.0, 1.0 - x / 1900.0)
    for y in range(3000):
        vertical = max(0.0, 1.0 - y / 1160.0)
        bottom = max(0.0, (y - 2540.0) / 460.0)
        alpha = int(min(150, 100 * left + 42 * top_weight * vertical + 45 * bottom))
        shade_px[x, y] = (7, 13, 14, alpha)
cover = Image.alpha_composite(cover, shade)

draw = ImageDraw.Draw(cover)
title_font = ImageFont.truetype(FONT, 176, index=5)
artist_font = ImageFont.truetype(FONT, 56, index=3)
archive_font = ImageFont.truetype(FONT, 34, index=3)

warm_white = (248, 242, 229, 255)
sea_glass = (145, 226, 218, 255)
soft_gold = (244, 197, 118, 255)

draw.text((155, 155), "TIDE IN", font=title_font, fill=warm_white)
draw.text((155, 330), "MY CUP", font=title_font, fill=warm_white)
draw.line((160, 548, 610, 548), fill=sea_glass, width=7)
draw.text((160, 588), "CHLOE KATASTROPHE", font=artist_font, fill=soft_gold)

archive = "A RECOVERED RECORDING"
box = draw.textbbox((0, 0), archive, font=archive_font)
draw.text((3000 - (box[2] - box[0]) - 125, 2890), archive, font=archive_font, fill=(248, 242, 229, 220))

cover_rgb = cover.convert("RGB")
cover_rgb.save(COVER, optimize=True)
cover_rgb.save(COVER_JPG, quality=96, subsampling=0, optimize=True)

# Story poster: blurred full-bleed extension, square cover, and restrained release line.
story_bg = square.resize((1080, 1920), Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(34))
story_bg = ImageEnhance.Brightness(story_bg).enhance(0.52).convert("RGBA")
story = story_bg
cover_story = cover.resize((980, 980), Image.Resampling.LANCZOS)
story.alpha_composite(cover_story, ((1080 - 980) // 2, 470))
story_draw = ImageDraw.Draw(story)
story_font = ImageFont.truetype(FONT, 38, index=3)
story_draw.text((540, 1550), "NEW RECOVERED RECORDING", font=story_font, fill=warm_white, anchor="mm")
story_draw.line((370, 1595, 710, 1595), fill=sea_glass, width=4)
story.convert("RGB").save(STORY, optimize=True)

for path in (ART, COVER, COVER_JPG, STORY):
    print(path)
