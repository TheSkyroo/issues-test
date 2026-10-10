from toolbelt.text import slugify, truncate


def test_slugify_simple_title():
    assert slugify("Hello World") == "hello-world"


def test_truncate_long_text():
    assert truncate("abcdefghij", 6) == "abc..."


def test_truncate_short_text_unchanged():
    assert truncate("short", 10) == "short"
