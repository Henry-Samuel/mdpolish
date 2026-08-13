# mdpolish

[![Python Versions](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Minimal Markdown polish cleaner: removes extra blank lines, trailing whitespace, and unnecessary leading/trailing blank lines. Designed for small readmes and docs where noisy diffs obscure real changes.

## Features

- Remove repeated blank lines
- Strip trailing whitespace
- Trim leading and trailing blank lines
- Preserve meaningful single blank sections
- Working directory/rewrite CLI with `--diff` mode

## Installation

```bash
pip install mdpolish
```

Requires Python 3.10+.

## Usage

Polish a Markdown file in place:

```bash
mdpolish README.md
```

Preview changes without rewriting:

```bash
mdpolish --diff README.md
```

Use quiet mode for CI scripts:

```bash
mdpolish -q README.md
```

## CLI

```
mdpolish [--diff] [-q] <path>
```

- `path`: Markdown file to clean
- `--diff`: show unified diff instead of rewriting
- `-q, --quiet`: suppress success output

## API

```python
from mdpolish import polish_text, polish_file

polished = polish_text(raw_markdown)
polish_file("README.md")
```

## Project structure

```text
mdpolish/
  mdpolish/
    __init__.py
    polish.py
    cli.py
  tests/
    test_polish.py
  pyproject.toml
  README.md
```

## Tags

markdown, polish, cleanup, cli, tidy, readme
