#!/usr/bin/env python3
"""Extract readable Markdown-like text from HTML/Markdown/text paper notes.

Usage:
  python3 example.py input.html output.md
  python3 example.py input.md output.md

This helper is intentionally dependency-free. It is useful for noisy Notion-style
HTML exports, but it does not replace reading the original paper when available.
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class ReadableHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"style", "script"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in {"h1", "h2", "h3", "h4"}:
            self.parts.append("\n" + "#" * int(tag[1]) + " ")
        elif tag in {"p", "div"}:
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "tr":
            self.parts.append("\n")
        elif tag in {"td", "th"}:
            self.parts.append(" | ")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"style", "script"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag in {"h1", "h2", "h3", "h4", "p", "li", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = re.sub(r"\s+", " ", data).strip()
        if text:
            self.parts.append(text)


def normalize(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def extract(input_path: Path) -> str:
    raw = input_path.read_text(encoding="utf-8", errors="replace")
    if input_path.suffix.lower() in {".html", ".htm"}:
        parser = ReadableHTMLParser()
        parser.feed(raw)
        return normalize("".join(parser.parts))
    return normalize(raw)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 example.py <input.html|md|txt> <output.md>", file=sys.stderr)
        return 2
    input_path = Path(sys.argv[1]).expanduser()
    output_path = Path(sys.argv[2]).expanduser()
    output_path.write_text(extract(input_path), encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
