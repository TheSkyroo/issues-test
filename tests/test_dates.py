from toolbelt.dates import days_in_month, is_leap_year


def test_is_leap_year_regular():
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False


def test_is_leap_year_century():
    assert is_leap_year(1900) is False


def test_days_in_month_february_leap():
    assert days_in_month(2024, 2) == 29


def test_days_in_month_april():
    assert days_in_month(2023, 4) == 30
