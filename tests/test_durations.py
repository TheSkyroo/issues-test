import pytest

from toolbelt.durations import format_duration, parse_duration


def test_parse_duration_single_unit():
    assert parse_duration("90s") == 90
    assert parse_duration("2h") == 7200


def test_parse_duration_invalid():
    with pytest.raises(ValueError):
        parse_duration("soon")


def test_format_duration():
    assert format_duration(5400) == "1h30m"
    assert format_duration(0) == "0s"
