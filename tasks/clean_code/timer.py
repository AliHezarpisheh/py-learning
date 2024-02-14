"""Module for measuring the execution time of a function."""

import time
import functools
import contextlib
from typing import Generator, Callable, Any


@contextlib.contextmanager
def log_function_execution_time() -> Generator[None, None, None]:
    """Context manager to time code execution."""
    start_time = time.time()
    yield
    end_time = time.time()
    duration = start_time - end_time
    print(f"Execution time: {duration} seconds")


class LogFunctionExecutionTime(contextlib.ContextDecorator):
    """
    A context decorator for measuring the execution time of a function and printing
    information.
    """

    def __enter__(self) -> "LogFunctionExecutionTime":
        """
        Enters the context, initializing the start time for measuring execution.

        Returns
        -------
        LogFunctionExecutionTime
            The context manager instance.
        """
        self._start_time = time.time()
        return self

    def __exit__(self, *args, **kwargs) -> None:
        """
        Exits the context, calculates the duration of execution, and prints the result.

        Parameters
        ----------
        *args : tuple
            Variable positional arguments.
        **kwargs : dict
            Variable keyword arguments.
        """
        end_time = time.time()
        self._duration = self._start_time - end_time

    def __call__(self, func: Callable) -> Any:
        """
        Decorates a function to measure its execution time and print relevant
        information.

        Parameters
        ----------
        func : Callable
            The function to be decorated.

        Returns
        -------
        Any
            The decorated function.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> None:
            """
            Wrapper function that measures the execution time of the decorated function
            and prints information.

            Parameters
            ----------
            *args : tuple
                Variable positional arguments.
            **kwargs : dict
                Variable keyword arguments.
            """
            print(f"Function: {func.__name__}")
            print(f"Arguments: {args}, {kwargs}")
            print(f"Execution time: {self._duration} seconds")

        return wrapper
