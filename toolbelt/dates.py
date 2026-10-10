"""Calendar helpers (Gregorian calendar)."""

_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    """Gregorian leap year: divisible by 4, except centuries, unless divisible by 400.

    >>> is_leap_year(2024), is_leap_year(1900), is_leap_year(2000)
    (True, False, True)
    """
    return year % 4 == 0 and year % 100 != 0


def days_in_month(year, month):
    """Number of days in a month (month is 1-12).

    >>> days_in_month(2024, 2)
    29
    """
    if not 1 <= month <= 12:
        raise ValueError("month must be 1-12")
    if month == 2 and is_leap_year(year):
        return 29
    return _DAYS[month - 1]
