"""List helpers."""


def chunk(items, size):
    """Split items into consecutive lists of `size` items; the last chunk may be shorter.

    Raises ValueError when size < 1.

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    if size < 1:
        raise ValueError("size must be >= 1")
    items = list(items)
    end = len(items) - len(items) % size
    return [items[i : i + size] for i in range(0, end, size)]


def dedupe(items):
    """Remove duplicates while keeping the first occurrence order.

    >>> dedupe([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
