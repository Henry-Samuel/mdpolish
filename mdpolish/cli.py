import argparse
import difflib
import sys
from pathlib import Path

from mdpolish import polish_file, polish_text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mdpolish", description="Polish Markdown files")
    parser.add_argument("path", nargs="?", help="Markdown file path to rewrite cleanly")
    parser.add_argument("--diff", action="store_true", help="Print unified diff without rewriting")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress success messages")
    args = parser.parse_args(argv)

    if args.path is None:
        return parser.print_help() or 0

    path = Path(args.path)
    if not path.exists() or not path.is_file():
        print(f"mdpolish: not a file: {args.path}", file=sys.stderr)
        return 1

    original = path.read_text(encoding="utf-8")
    polished = polish_text(original)

    if polished == original:
        if not args.quiet:
            print(f"Already clean: {path}")
        return 0

    if args.diff:
        diff = difflib.unified_diff(
            original.splitlines(keepends=True),
            polished.splitlines(keepends=True),
            fromfile=f"a/{path.name}",
            tofile=f"b/{path.name}",
        )
        sys.stdout.writelines(diff)
        return 0

    path.write_text(polished, encoding="utf-8")
    print(f"Polished: {path}")
    return 0
