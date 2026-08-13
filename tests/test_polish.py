from __future__ import annotations

import subprocess

from mdpolish.polish import polish_file, polish_text


def test_removes_extra_blank_lines():
    assert polish_text("# a\n\n\n# b\n") == "# a\n\n# b\n"


def test_preserves_single_blank_line():
    assert polish_text("# a\n\n# b\n") == "# a\n\n# b\n"


def test_handles_multiple_trailing_blanks():
    assert polish_text("# a\n\n\n\n") == "# a\n"


def test_handles_setext_underlines():
    assert polish_text("===\n\n===\n") == "===\n\n===\n"


def test_empty_file():
    assert polish_text("") == ""


def test_no_trailing_newline_behavior():
    # Non-markdown noisy input without trailing newline; preserve best-effort.
    assert polish_text("# a# b") == "# a# b"

def test_polish_file_rewrites(tmp_path):
    p = tmp_path / "README.md"
    p.write_text("# a\n\n\n# b\n", encoding="utf-8")
    result = polish_file(p)
    assert result == "# a\n\n# b\n"


def test_cli_main_quiet_clean_file(tmp_path):
    p = tmp_path / "README.md"
    p.write_text("# a\n\n# b\n", encoding="utf-8")
    from mdpolish.cli import main

    assert main(["-q", str(p)]) == 0


def test_cli_missing_file_returns_error():
    from mdpolish.cli import main

    rc = main(["/nonexistent/path"])
    assert rc == 1


def test_cli_polishes_quietly_when_clean(tmp_path):
    p = tmp_path / "README.md"
    p.write_text("# a\n\n# b\n", encoding="utf-8")
    out = (
        subprocess.check_output(["mdpolish", str(p)])
        .decode("utf-8")
        .strip()
    )
    assert "Already clean" in out
