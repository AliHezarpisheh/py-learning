"""
The Karatsuba algorithm is a fast multiplication algorithm that is
based on the divide-and-conquer approach. It is based on the observation
that the product of two numbers can be broken down into four parts: the
products of the highest powers of two digits, the product of the
middle digits, and the product of the lowest powers of two digits.

The algorithm starts by recursively dividing the input x and y into
two parts, each of length m = n/2, where n is the length of the longest
input. It then computes three products: the product of the highest powers
of two digits, the product of the middle digits, and the product of the
lowest powers of two digits. Finally, it combines these products to
obtain the final result.

The running time of the algorithm is O(n^1.585), which is faster than the
naive algorithm for multiplying two n-digit numbers, which has a running
time of O(n^2). However, the constant hidden in the big O notation is
much larger, so the Karatsuba algorithm is generally not used in practice.
"""


def karatsuba(x, y, /):
    """
    Multiply two integers x and y using the Karatsuba algorithm.

    Parameters
    ----------
    x : int
        First integer to be multiplied.
    y : int
        Second integer to be multiplied.

    Returns
    -------
    int
        The product of x and y.
    """

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split x & y in to two parts.
    a = x // (10**m)
    b = x % (10**m)
    c = y // (10**m)
    d = y % (10**m)

    # Recursive steps.
    z0 = karatsuba(a, c)
    z1 = karatsuba(b, d)
    z2 = karatsuba(a + b, c + d) - z0 - z1

    return z0 * 10 ** (2 * m) + z2 * 10**m + z1


if __name__ == "__main__":
    x = 1234
    y = 5678
    print("Result of", x, "*", y, "using Karatsuba algorithm:", karatsuba(x, y))
