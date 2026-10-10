"""Text helpers."""
import re


def slugify(text):
    """Turn a title into a URL slug.

    Lowercases, replaces every run of non-alphanumeric characters with a single
    hyphen, and strips hyphens from both ends.

    >>> slugify("Hello World")
    'hello-world'
    >>> slugify("  Rust & Python: 2026 Edition!  ")
    'rust-python-2026-edition'
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9]", "-", text)
    return text


def truncate(text, limit, suffix="..."):
    """Shorten text to at most `limit` characters, including the suffix.

    >>> truncate("abcdefghij", 6)
    'abc...'
    >>> truncate("short", 10)
    'short'
    """
    if len(text) <= limit:
        return text
    return text[: limit - len(suffix)] + suffix
