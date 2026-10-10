import pytest

from toolbelt.lists import chunk, dedupe


def test_chunk_even_split():
    assert chunk([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]


def test_chunk_invalid_size():
    with pytest.raises(ValueError):
        chunk([1, 2], 0)


def test_dedupe_keeps_order():
    assert dedupe([3, 1, 3, 2, 1]) == [3, 1, 2]
