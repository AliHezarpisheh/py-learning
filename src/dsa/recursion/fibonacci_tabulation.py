"""Module containing Fibonacci function using tabulation."""


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to be calculated.

    Returns
    -------
    int
        The nth Fibonacci number.

    """
    if not isinstance(n, int):
        raise ValueError("n should be an integer")

    fib = [1, 1]
    for num in range(2, n):
        fib.append(fib[num - 1] + fib[num - 2])

    return fib[-1]


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print(fibonacci(n))
