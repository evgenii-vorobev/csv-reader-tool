from __future__ import annotations

import argparse
import sys
from typing import Optional, Sequence

from .reader import read_members


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="csv-reader-tool",
        description="Print the full name of each member in a CSV file.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="members.csv",
        help="Path to the members CSV file (default: members.csv in the current directory).",
    )
    args = parser.parse_args(argv)

    try:
        for member in read_members(args.path):
            print(member.full_name)
    except FileNotFoundError:
        print(f"error: file not found: {args.path}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: cannot read file {args.path}: {exc}", file=sys.stderr)
        return 1
    except TypeError as exc:
        print(f"error: unexpected CSV columns in {args.path}: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
