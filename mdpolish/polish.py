from __future__ import annotations

from pathlib import Path


def polish_text(text: str) -> str:
    if not text:
        return ""

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    raw = normalized.splitlines()

    while raw and raw[0] == "":
        raw.pop(0)

    stripped = [line.rstrip(" \t") for line in raw]

    tidy = []
    prev_blank = False
    for line in stripped:
        blank = line == ""
        if blank:
            if prev_blank:
                continue
            prev_blank = True
        else:
            prev_blank = False
        tidy.append(line)

    result = "\n".join(tidy)
    if text.endswith("\n") and result and not result.endswith("\n"):
        result += "\n"
    return result


def polish_file(path: str | Path) -> str:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    polished = polish_text(text)
    if polished != text:
        p.write_text(polished, encoding="utf-8")
    return polished
