"""Parse and format human durations such as "1h30m" or "45s"."""
import re

_UNITS = {"d": 86400, "h": 3600, "m": 60, "s": 1}
_TOKEN = re.compile(r"(\d+)([dhms])")


def parse_duration(text):
    """Convert a duration string to seconds.

    Accepts one or more <number><unit> parts with units d, h, m, s, in any order,
    optionally separated by spaces. Raises ValueError on anything else.

    >>> parse_duration("90s")
    90
    >>> parse_duration("1h30m")
    5400
    >>> parse_duration("2d 4h")
    187200
    """
    text = text.strip().lower()
    match = _TOKEN.match(text)
    if not match:
        raise ValueError(f"invalid duration: {text!r}")
    number, unit = match.groups()
    return int(number) * _UNITS[unit]


def format_duration(seconds):
    """Format seconds as a compact duration, largest units first, zero parts omitted.

    >>> format_duration(5400)
    '1h30m'
    >>> format_duration(0)
    '0s'
    """
    if seconds == 0:
        return "0s"
    parts = []
    for unit, size in _UNITS.items():
        count, seconds = divmod(seconds, size)
        if count:
            parts.append(f"{count}{unit}")
    return "".join(parts)
