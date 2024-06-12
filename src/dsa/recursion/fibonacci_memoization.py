"""Fibonacci Sequence using Memoization"""


def fibonacci(n: int, lookup: list[int | None]) -> int:
    """
    Calculate the nth Fibonacci number using memoization.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to calculate.
    lookup : list
        A list to store the calculated Fibonacci numbers.

    Returns
    -------
    int
        The nth Fibonacci number.

    Raises
    ------
    ValueError
        If the input is not an integer.
    """
    if not isinstance(n, int):
        raise ValueError("n should be an integer")

    if 0 <= n <= 1:
        return n

    if lookup[n] is None:
        lookup[n] = fibonacci(n - 1, lookup) + fibonacci(n - 2, lookup)

    return lookup[n]


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    lookup = [None] * (n + 1)

    print(fibonacci(n, lookup))
