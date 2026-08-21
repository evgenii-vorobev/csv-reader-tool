from pathlib import Path

import pytest

from csv_reader_tool import Member, read_members

SAMPLE_CSV = Path(__file__).parent.parent / "examples" / "members_sample.csv"


def test_read_members_yields_member_instances():
    members = list(read_members(SAMPLE_CSV))
    assert members
    assert all(isinstance(m, Member) for m in members)


def test_full_name_combines_first_and_last():
    members = list(read_members(SAMPLE_CSV))
    assert members[0].full_name == f"{members[0].first_name} {members[0].last_name}"


def test_read_members_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        list(read_members("does_not_exist.csv"))
