#!/usr/bin/env python3

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
)

ROOT = Path(__file__).resolve().parents[3]
BOOK_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output" / "pdf"

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
FONT_FILES = {
    "ArchiveSans": FONT_DIR / "Arial.ttf",
    "ArchiveSans-Bold": FONT_DIR / "Arial Bold.ttf",
    "ArchiveSans-Italic": FONT_DIR / "Arial Italic.ttf",
    "ArchiveSans-BoldItalic": FONT_DIR / "Arial Bold Italic.ttf",
    "ArchiveMono": FONT_DIR / "Courier New.ttf",
}

INK = colors.HexColor("#171A1F")
MUTED = colors.HexColor("#60656D")
PAPER = colors.HexColor("#F7F3EB")
GOLD = colors.HexColor("#A67C45")
GOLD_LIGHT = colors.HexColor("#D9C2A0")
NIGHT = colors.HexColor("#10141B")
QUOTE_BG = colors.HexColor("#EEE7DB")
RULE = colors.HexColor("#D8CCBC")


def register_fonts() -> None:
    for name, path in FONT_FILES.items():
        if not path.exists():
            raise FileNotFoundError(f"Required font missing: {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily(
        "ArchiveSans",
        normal="ArchiveSans",
        bold="ArchiveSans-Bold",
        italic="ArchiveSans-Italic",
        boldItalic="ArchiveSans-BoldItalic",
    )


def inline_markup(text: str) -> str:
    value = html.escape(text.strip())
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="#7E5D32"><u>\1</u></link>', value)
    value = re.sub(r"`([^`]+)`", r'<font name="ArchiveMono" size="8.6">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


class ArchiveDocTemplate(BaseDocTemplate):
    def __init__(self, filename: Path, title: str):
        self.book_title = title
        super().__init__(
            str(filename),
            pagesize=LETTER,
            leftMargin=0.82 * inch,
            rightMargin=0.82 * inch,
            topMargin=0.78 * inch,
            bottomMargin=0.72 * inch,
            title=title,
            author='Allen "FrikShun" Taylor and Chloe Katastrophe Archive',
            subject="Working Chloe continuity manual",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="archive", frames=[frame], onPage=self.draw_page))

    def draw_page(self, canvas, doc) -> None:
        canvas.saveState()
        if doc.page == 1:
            canvas.setFillColor(NIGHT)
            canvas.rect(0, 0, LETTER[0], LETTER[1], stroke=0, fill=1)
            canvas.setStrokeColor(GOLD)
            canvas.setLineWidth(1.2)
            canvas.line(0.85 * inch, 0.72 * inch, LETTER[0] - 0.85 * inch, 0.72 * inch)
        else:
            canvas.setFillColor(PAPER)
            canvas.rect(0, 0, LETTER[0], LETTER[1], stroke=0, fill=1)
            canvas.setStrokeColor(RULE)
            canvas.setLineWidth(0.45)
            canvas.line(self.leftMargin, LETTER[1] - 0.53 * inch, LETTER[0] - self.rightMargin, LETTER[1] - 0.53 * inch)
            canvas.setFont("ArchiveSans", 7.5)
            canvas.setFillColor(MUTED)
            canvas.drawString(self.leftMargin, LETTER[1] - 0.40 * inch, self.book_title.upper())
            canvas.drawRightString(LETTER[0] - self.rightMargin, 0.39 * inch, f"CHLOE ARCHIVE  /  {doc.page - 1}")
        canvas.restoreState()


def make_styles():
    sample = getSampleStyleSheet()
    styles = {
        "cover_title": ParagraphStyle(
            "cover_title",
            parent=sample["Title"],
            fontName="ArchiveSans-Bold",
            fontSize=31,
            leading=35,
            textColor=colors.HexColor("#F1E5D2"),
            alignment=TA_CENTER,
            spaceAfter=18,
        ),
        "cover_subtitle": ParagraphStyle(
            "cover_subtitle",
            parent=sample["Normal"],
            fontName="ArchiveSans",
            fontSize=12,
            leading=17,
            textColor=GOLD_LIGHT,
            alignment=TA_CENTER,
            spaceAfter=10,
        ),
        "cover_meta": ParagraphStyle(
            "cover_meta",
            parent=sample["Normal"],
            fontName="ArchiveSans",
            fontSize=8.5,
            leading=13,
            textColor=colors.HexColor("#B9B3A9"),
            alignment=TA_CENTER,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=sample["Heading1"],
            fontName="ArchiveSans-Bold",
            fontSize=20,
            leading=24,
            textColor=INK,
            spaceBefore=4,
            spaceAfter=12,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=sample["Heading2"],
            fontName="ArchiveSans-Bold",
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#6F512B"),
            spaceBefore=14,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "h3",
            parent=sample["Heading3"],
            fontName="ArchiveSans-Bold",
            fontSize=11.5,
            leading=15,
            textColor=INK,
            spaceBefore=12,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "body",
            parent=sample["BodyText"],
            fontName="ArchiveSans",
            fontSize=9.4,
            leading=13.35,
            textColor=INK,
            spaceAfter=7,
            allowWidows=0,
            allowOrphans=0,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=sample["BodyText"],
            fontName="ArchiveSans",
            fontSize=9.2,
            leading=13.0,
            textColor=INK,
            leftIndent=16,
            firstLineIndent=-8,
            bulletIndent=4,
            spaceAfter=3.2,
        ),
        "quote": ParagraphStyle(
            "quote",
            parent=sample["BodyText"],
            fontName="ArchiveSans-Italic",
            fontSize=10.2,
            leading=15,
            textColor=colors.HexColor("#493C2D"),
            leftIndent=18,
            rightIndent=18,
            borderColor=GOLD,
            borderWidth=1.5,
            borderPadding=(7, 10, 7, 10),
            backColor=QUOTE_BG,
            spaceBefore=5,
            spaceAfter=10,
        ),
        "code": ParagraphStyle(
            "code",
            parent=sample["Code"],
            fontName="ArchiveMono",
            fontSize=8.1,
            leading=11,
            textColor=INK,
            backColor=colors.HexColor("#ECE8E0"),
            borderColor=RULE,
            borderWidth=0.5,
            borderPadding=8,
            leftIndent=8,
            rightIndent=8,
            spaceBefore=5,
            spaceAfter=10,
        ),
    }
    return styles


def parse_markdown(source: Path, styles) -> tuple[str, str, list]:
    lines = source.read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip()
    subtitle = "Working Reference Edition"
    if len(lines) > 2 and lines[2].startswith("## "):
        subtitle = lines[2].lstrip("# ").strip()

    story = []
    story.append(Spacer(1, 1.65 * inch))
    story.append(Paragraph("CHLOE KATASTROPHE ARCHIVE", styles["cover_subtitle"]))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph(inline_markup(title), styles["cover_title"]))
    story.append(Paragraph(inline_markup(subtitle), styles["cover_subtitle"]))
    story.append(Spacer(1, 2.45 * inch))
    story.append(Paragraph("LIVING DRAFT  /  JULY 2026", styles["cover_meta"]))
    story.append(Paragraph("Canon • Hypothesis • Memory • Mystery", styles["cover_meta"]))
    story.append(PageBreak())

    paragraph_buffer: list[str] = []
    quote_buffer: list[str] = []
    code_buffer: list[str] = []
    in_code = False

    def flush_paragraph():
        if paragraph_buffer:
            text = " ".join(x.strip() for x in paragraph_buffer)
            story.append(Paragraph(inline_markup(text), styles["body"]))
            paragraph_buffer.clear()

    def flush_quote():
        if quote_buffer:
            text = "<br/>".join(inline_markup(x) for x in quote_buffer)
            story.append(Paragraph(text, styles["quote"]))
            quote_buffer.clear()

    for index, raw in enumerate(lines):
        if index == 0 or (index == 2 and raw.startswith("## ")):
            continue
        line = raw.rstrip()
        if line.startswith("```"):
            flush_paragraph()
            flush_quote()
            if in_code:
                story.append(Preformatted("\n".join(code_buffer), styles["code"]))
                code_buffer.clear()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_buffer.append(line)
            continue
        if not line.strip():
            flush_paragraph()
            flush_quote()
            continue
        if line.startswith(">"):
            flush_paragraph()
            quote_buffer.append(line.lstrip("> "))
            continue
        flush_quote()
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            story.append(Paragraph(inline_markup(heading.group(2)), styles[f"h{level}"]))
            continue
        bullet = re.match(r"^\s*-\s+(.+)$", line)
        if bullet:
            flush_paragraph()
            story.append(Paragraph(inline_markup(bullet.group(1)), styles["bullet"], bulletText="•"))
            continue
        numbered = re.match(r"^\s*(\d+)\.\s+(.+)$", line)
        if numbered:
            flush_paragraph()
            story.append(Paragraph(inline_markup(numbered.group(2)), styles["bullet"], bulletText=f"{numbered.group(1)}."))
            continue
        paragraph_buffer.append(line)

    flush_paragraph()
    flush_quote()
    if code_buffer:
        story.append(Preformatted("\n".join(code_buffer), styles["code"]))
    return title, subtitle, story


def render(source_name: str, output_name: str) -> Path:
    styles = make_styles()
    source = BOOK_DIR / source_name
    output = OUTPUT_DIR / output_name
    title, _, story = parse_markdown(source, styles)
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = ArchiveDocTemplate(output, title)
    doc.build(story)
    return output


def main() -> int:
    register_fonts()
    outputs = [
        render("THE_CHLOE_KATASTROPHE_BIOGRAPHY.md", "the-chloe-katastrophe-biography-working-draft.pdf"),
        render("THE_BOOK_OF_CHLOE.md", "the-book-of-chloe-living-reference.pdf"),
    ]
    for output in outputs:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
