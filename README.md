# csv-reader-tool

Read member records from a CSV file as typed Python objects. Use it as a
library inside another application, or run it as a standalone command-line
tool.

[![Tests](https://github.com/evgenii-vorobev/csv-reader-tool/actions/workflows/tests.yml/badge.svg)](https://github.com/evgenii-vorobev/csv-reader-tool/actions/workflows/tests.yml)

## Features

- Zero third-party dependencies (standard library only)
- Typed `Member` dataclass with a `full_name` property
- Lazy, memory-efficient reading (rows are yielded one at a time)
- Bundled `csv-reader-tool` CLI
- Python 3.9+

## Installation

Install directly from GitHub with pip:

```bash
pip install git+https://github.com/evgenii-vorobev/csv-reader-tool.git
```

Or clone it and install in editable mode for local development:

```bash
git clone https://github.com/evgenii-vorobev/csv-reader-tool.git
cd csv-reader-tool
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux
pip install -e .[dev]
```

## CSV format

The input file must have a header row with exactly these columns:

| Column       | Description                  |
|--------------|-------------------------------|
| `id`         | Unique identifier            |
| `first_name` | Given name                   |
| `last_name`  | Family name                  |
| `email`      | Email address                |
| `gender`     | Gender                       |
| `ip_address` | IP address                   |

See [`examples/members_sample.csv`](examples/members_sample.csv) for a
working example.

## Usage as a library

```python
from csv_reader_tool import read_members

for member in read_members("members.csv"):
    print(member.full_name)   # e.g. "Haskell Helmke"
    print(member.email)
```

`read_members(path)` returns a generator of `Member` objects:

```python
@dataclass(frozen=True)
class Member:
    id: str
    first_name: str
    last_name: str
    email: str
    gender: str
    ip_address: str

    @property
    def full_name(self) -> str: ...
```

`path` defaults to `"members.csv"` in the current working directory, or you
can pass any `str` or `pathlib.Path`.

### Error handling

| Exception            | When it's raised                                    |
|-----------------------|------------------------------------------------------|
| `FileNotFoundError`   | The given path doesn't exist                         |
| `TypeError`           | The CSV header doesn't match the expected columns     |

```python
from csv_reader_tool import read_members

try:
    members = list(read_members("members.csv"))
except FileNotFoundError:
    print("members.csv not found")
```

## Usage as a CLI

After installing, a `csv-reader-tool` command is available on your PATH:

```bash
csv-reader-tool                  # reads ./members.csv
csv-reader-tool path/to/file.csv # reads a specific file
```

Each line of output is one member's full name.

## Development

```bash
pip install -e .[dev]
pytest
```

Project layout:

```
src/csv_reader_tool/   # library + CLI source
tests/                 # pytest test suite
examples/              # sample CSV data
```

## License

[MIT](LICENSE)
