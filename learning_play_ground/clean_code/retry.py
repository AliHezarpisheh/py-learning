"""Retry mechanism module with function and class for implementing retry logic."""

import functools
from typing import Any, Callable, Optional, Type


class Retry:
    """
    Class implementing a retry mechanism for function calls.

    Parameters
    ----------
    retries_limit : int, optional
        Maximum number of retries. Defaults to 3.
    allowed_exceptions : tuple[Type[BaseException]], optional
        Tuple of exception types that are allowed to be caught and retried. Defaults to
        None, which catches all exceptions.

    Attributes
    ----------
    _retries_limit : int
        Maximum number of retries.
    _allowed_exceptions : tuple[Type[BaseException]]
        Tuple of allowed exception types.

    Returns
    -------
    Callable
        Decorated function.
    """

    def __init__(
        self,
        retries_limit: int = 3,
        allowed_exceptions: Optional[tuple[Type[BaseException]]] = None,
    ) -> None:
        """
        Initialize Retry instance with retries limit and allowed exceptions.

        Parameters
        ----------
        retries_limit : int, optional
            Maximum number of retries. Defaults to 3.
        allowed_exceptions : tuple[Type[BaseException]], optional
            Tuple of exception types that are allowed to be caught and retried. Defaults
            to None, which catches all exceptions.
        """
        self._retries_limit = retries_limit
        self._allowed_exceptions = allowed_exceptions or (Exception,)

    def __call__(self, func: Callable) -> Callable:
        """
        Decorates a function to implement the retry mechanism.

        Parameters
        ----------
        func : Callable
            Function to be decorated.

        Returns
        -------
        Callable
            Decorated function.
        """

        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            """
            Wrapped function that executes the decorated function with retries.

            Parameters
            ----------
            *args
                Arguments to be passed to the decorated function.
            **kwargs
                Keyword arguments to be passed to the decorated function.

            Returns
            -------
            Any
                Result of the decorated function.

            Raises
            ------
            BaseException
                If all retries fail, the last raised exception is raised.
            """
            last_raised = None

            for _ in range(self._retries_limit):
                try:
                    return func(*args, **kwargs)
                except self._allowed_exceptions as error:
                    last_raised = error

            if last_raised is not None:
                raise last_raised

        return wrapped


def retry(
    func: Optional[Callable] = None,
    *,
    retries_limit: int = 3,
    allowed_exceptions: Optional[tuple[Type[BaseException]]] = None,
) -> Callable:
    """
    Function decorator implementing a retry mechanism for function calls.

    Parameters
    ----------
    func : Callable, optional
        Function to be decorated. Defaults to None.
    retries_limit : int, optional
        Maximum number of retries. Defaults to 3.
    allowed_exceptions : tuple[Type[BaseException]], optional
        Tuple of exception types that are allowed to be caught and retried. Defaults to
        None, which catches all exceptions.

    Returns
    -------
    Callable
        Decorated function.
    """
    allowed_exceptions = allowed_exceptions or (Exception,)

    if func is None:
        return functools.partial(
            retry, retries_limit=retries_limit, allowed_exceptions=allowed_exceptions
        )

    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        """
        Wrapped function that executes the decorated function with retries.

        Parameters
        ----------
        *args
            Arguments to be passed to the decorated function.
        **kwargs
            Keyword arguments to be passed to the decorated function.

        Returns
        -------
        Any
            Result of the decorated function.

        Raises
        ------
        BaseException
            If all retries fail, the last raised exception is raised.
        """
        last_raised: Optional[BaseException] = None

        for _ in range(retries_limit):
            try:
                return func(*args, **kwargs)
            except allowed_exceptions as error:
                last_raised = error

        if last_raised is not None:
            raise last_raised

    return wrapped
