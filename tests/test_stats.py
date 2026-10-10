import pytest

from toolbelt.stats import mean, median, percent_change


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_median_odd_count():
    assert median([3, 1, 2]) == 2


def test_median_empty_raises():
    with pytest.raises(ValueError):
        median([])


def test_percent_change_increase():
    assert percent_change(50, 75) == 50.0
