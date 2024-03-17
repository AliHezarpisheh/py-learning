"""Module providing caching utilities for Python functions."""

import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """
    Decorator to cache the result of a function.

    Parameters
    ----------
    func : Callable
        The function to be cached.

    Returns
    -------
    Callable
        The wrapped function that caches its result.
    """
    cache_dict = {}

    @functools.wraps(func)
    def wrapped(*args) -> Any:
        """
        Wrapped function that caches the result of the decorated function.

        Parameters
        ----------
        *args : Any
            Arguments to be passed to the decorated function.

        Returns
        -------
        Any
            The result of the decorated function.
        """
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]

    return wrapped


class Cache:
    """Class providing caching functionality for functions."""

    def __call__(self, func: Callable) -> Callable:
        """
        Decorates a function to cache its result.

        Parameters
        ----------
        func : Callable
            The function to be cached.

        Returns
        -------
        Callable
            The wrapped function that caches its result.
        """
        cache_dict = {}

        @functools.wraps(func)
        def wrapped(*args) -> Any:
            """
            Wrapped function that caches the result of the decorated function.

            Parameters
            ----------
            *args : Any
                Arguments to be passed to the decorated function.

            Returns
            -------
            Any
                The result of the decorated function.
            """
            if args not in cache_dict:
                cache_dict[args] = func(*args)
                print(cache_dict)
            return cache_dict[args]

        return wrapped


@Cache()
def fibonacci(number: int) -> int:
    """
    Calculate the Fibonacci number for a given integer.

    Parameters
    ----------
    number : int
        The index of the Fibonacci number to calculate.

    Returns
    -------
    int
        The Fibonacci number corresponding to the input index.

    Raises
    ------
    AssertionError
        If the input is not a positive integer.
    """
    assert isinstance(number, int), f"number should be `int`, got `{type(number)}`"
    assert number > -1, f"positive numbers acceptable, got `{number}`"

    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":
    print(fibonacci(10))
