"""Example for unicode use cases and analysis in Python."""


def analyze_unicode(s: str) -> list[tuple[str, str, list[int]]]:
    """Analyze the unicode aspects of characters of an string."""
    return [(char, f"U+{ord(char):04X}", list(char.encode("utf-8"))) for char in s]
