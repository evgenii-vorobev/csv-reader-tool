from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Union

PathLike = Union[str, Path]


@dataclass(frozen=True)
class Member:
    """A single row from a members CSV file."""

    id: str
    first_name: str
    last_name: str
    email: str
    gender: str
    ip_address: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


def read_members(path: PathLike = "members.csv") -> Iterator[Member]:
    """Yield a `Member` for each row in a members CSV file.

    The file must have a header row with exactly these columns:
    `id, first_name, last_name, email, gender, ip_address`.

    Args:
        path: Path to the CSV file. Defaults to `members.csv` in the
            current working directory.

    Yields:
        One `Member` per data row, in file order.

    Raises:
        FileNotFoundError: If `path` does not exist.
        TypeError: If the header row doesn't match the expected columns.
    """
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield Member(**row)
