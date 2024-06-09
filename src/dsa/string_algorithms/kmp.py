"""
The Knuth-Morris-Pratt (KMP) algorithm is a string matching algorithm that searches for
occurrences of a "pattern" within a main "text" string. The key idea behind KMP is to
avoid re-evaluating characters of the text that have already been matched against the
pattern. This is achieved by using the prefix function, which is computed using the
compute_prefix function provided.
"""


def compute_prefix(pattern: str) -> list[int]:
    """
    Compute the prefix function for a string.

    Parameters
    ----------
    pattern : str
        The pattern string

    Returns
    -------
    pi : list[int]
        The prefix function for the pattern

    """
    m = len(pattern)
    pi = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    return pi


def kmp_search(text: str, pattern: str) -> None:
    """
    Search for the pattern in the text using the Knuth-Morris-Pratt algorithm.

    Parameters
    ----------
    text : str
        The text to search
    pattern : str
        The pattern to find

    Returns
    -------
    None

    """
    n = len(text)
    m = len(pattern)
    pi = compute_prefix(pattern)
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            print(f"Pattern found at index {i - m + 1}")
            j = pi[j - 1]
