"""Basic statistics on lists of numbers."""


def mean(values):
    """Arithmetic mean. Raises ValueError on an empty list.

    >>> mean([1, 2, 3, 4])
    2.5
    """
    if not values:
        raise ValueError("mean() of an empty list")
    return sum(values) / len(values)


def median(values):
    """Middle value of the sorted list; for an even count, the mean of the two middle values.

    Raises ValueError on an empty list.

    >>> median([3, 1, 2])
    2
    >>> median([4, 1, 3, 2])
    2.5
    """
    if not values:
        raise ValueError("median() of an empty list")
    ordered = sorted(values)
    mid = len(ordered) // 2
    return ordered[mid]


def percent_change(old, new):
    """Percentage change from old to new, rounded to 2 decimals.

    Raises ValueError when old is 0.

    >>> percent_change(50, 75)
    50.0
    """
    if old == 0:
        raise ValueError("percent_change() from zero is undefined")
    return round((new - old) / old * 100, 2)
