#!/usr/bin/env python3
"""Create Russian working translations of the two Chloe reference books."""

from pathlib import Path
import re

from argostranslate import translate


ROOT = Path(__file__).resolve().parents[3]
BOOKS = ROOT / "archives" / "chloe-katastrophe" / "books"

SOURCES = {
    "THE_CHLOE_KATASTROPHE_BIOGRAPHY.md": "БИОГРАФИЯ_ХЛОИ_КАТАСТРОФИ.md",
    "THE_BOOK_OF_CHLOE.md": "КНИГА_ХЛОИ.md",
}

# Canon terms are protected from machine translation and restored consistently.
GLOSSARY = [
    ("The Chloe Katastrophe Biography", "Биография Хлои Катастрофи"),
    ("The Book of Chloe", "Книга Хлои"),
    ("Chloe Katastrophe", "Хлоя Катастрофи"),
    ("Daughter of Echoes", "Дочь эха"),
    ("Echo Traversal", "Эхо-траверс (Echo Traversal)"),
    ("Echo Bloom", "Эхо-цветение (Echo Bloom)"),
    ("Event Topology", "Топология событий (Event Topology)"),
    ("Identity State", "Состояние идентичности (Identity State)"),
    ("Soul State", "Состояние души (Soul State)"),
    ("Graph-Independent Consciousness", "Внеграфовое сознание (Graph-Independent Consciousness)"),
    ("Identity Convergence", "Конвергенция идентичности (Identity Convergence)"),
    ("Convergence", "Конвергенция"),
    ("Terminal Event", "Терминальное событие"),
    ("FrikShun", "FrikShun"),
    ("Katastrophe", "Катастрофи"),
    ("ChloKat", "ChloKat"),
]


def alpha_token(prefix, number):
    """Return a model-stable ASCII token containing letters only."""
    chars = []
    number += 1
    while number:
        number, remainder = divmod(number - 1, 26)
        chars.append(chr(ord("A") + remainder))
    return f"X{prefix}{''.join(reversed(chars))}X"


def protect(text):
    replacements = {}
    for i, (source, target) in enumerate(GLOSSARY):
        token = alpha_token("TERM", i)
        text = text.replace(source, token)
        replacements[token] = target
    # Protect inline code independently; its wording is often canonical syntax.
    for i, match in enumerate(list(re.finditer(r"`[^`]+`", text))):
        original = match.group(0)
        token = alpha_token("CODE", i)
        text = text.replace(original, token, 1)
        replacements[token] = original
    return text, replacements


def restore(text, replacements):
    # Inline code restoration can reintroduce protected terms, so make two passes.
    for _ in range(2):
        for token, value in replacements.items():
            text = re.sub(re.escape(token), value, text, flags=re.IGNORECASE)
    return text


def translate_text(text, translator):
    if not text.strip() or re.fullmatch(r"[-—–*#>\s]+", text):
        return text
    protected, replacements = protect(text)
    result = translator.translate(protected)
    return restore(result, replacements)


def translate_markdown(source, destination, translator):
    lines = source.read_text(encoding="utf-8").splitlines()
    output = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            output.append(line)
            continue
        if in_code:
            output.append(translate_text(line, translator))
            continue

        # Translate bold Markdown labels independently so the model cannot
        # collapse their surrounding spaces or closing delimiter.
        bold_label = re.match(r"^(\s*(?:[-*]\s+)?)(\*\*)(.+?)(\*\*)(\s*)(.*)$", line)
        if bold_label:
            prefix, opening, label, closing, spacing, remainder = bold_label.groups()
            translated_label = translate_text(label, translator).strip()
            translated_remainder = translate_text(remainder, translator) if remainder else ""
            output.append(prefix + opening + translated_label + closing + (spacing or " ") + translated_remainder.strip())
            continue

        match = re.match(r"^(\s*(?:#{1,6}\s+|[-*]\s+|\d+\.\s+|>\s*|))(.+)$", line)
        if not match:
            output.append(line)
            continue
        prefix, body = match.groups()
        roman = ""
        if "#" in prefix:
            roman_match = re.match(r"^([IVXLCDM]+\.\s+)(.*)$", body)
            if roman_match:
                roman, body = roman_match.groups()
        output.append(prefix + roman + translate_text(body, translator))

    text = "\n".join(output) + "\n"
    text = text.replace("Рабочий проект v0.6", "Русский перевод v0.1 / на основе v0.6")
    text = text.replace("Рабочий черновик v0.6", "Русский перевод v0.1 / на основе v0.6")
    text = text.replace("Живое справочное руководство v0.6", "Русский перевод v0.1 / на основе v0.6")
    text = text.replace("Living Reference Manual v0.6", "Русский перевод v0.1 / на основе v0.6")
    text = text.replace("Грегори", "Грегор")
    # The offline model occasionally mutates the protected token for Convergence.
    text = re.sub(r"XTERMLLX", "Конвергенция", text, flags=re.IGNORECASE)
    destination.write_text(text, encoding="utf-8")


def main():
    installed = translate.get_installed_languages()
    source_language = next(lang for lang in installed if lang.code == "en")
    target_language = next(lang for lang in installed if lang.code == "ru")
    translator = source_language.get_translation(target_language)

    for source_name, destination_name in SOURCES.items():
        source = BOOKS / source_name
        destination = BOOKS / destination_name
        translate_markdown(source, destination, translator)
        print(destination)


if __name__ == "__main__":
    main()
