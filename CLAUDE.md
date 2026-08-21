# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`csv-reader-tool` — an installable Python package (`src/csv_reader_tool/`) that reads member records (columns: `id, first_name, last_name, email, gender, ip_address`) from a CSV file and exposes them as `Member` objects. Ships both a library API (`read_members`) and a `csv-reader-tool` CLI entry point. No third-party runtime dependencies — standard library only (`csv`).

## Environment

A virtualenv exists at `venv/`. Activate it, then install the package in editable mode with dev dependencies (pytest):
```
venv\Scripts\activate
pip install -e .[dev]
```

## Running

```
csv-reader-tool                    # reads ./members.csv
csv-reader-tool path/to/file.csv   # reads a specific file
python -m csv_reader_tool.cli      # equivalent, without installing the entry point
```

`members.csv` (real data) is gitignored — see `examples/members_sample.csv` for a checked-in sample used by the test suite.

## Testing

```
pytest
```

## Layout

```
src/csv_reader_tool/   # library (reader.py) + CLI (cli.py)
tests/                 # pytest suite, reads examples/members_sample.csv
examples/               # sample CSV for docs and tests
```

See `README.md` for the full public API and usage examples.
