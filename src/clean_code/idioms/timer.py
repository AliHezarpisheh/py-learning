"""Module for measuring the execution time of a function."""

import contextlib
import time
from typing import Generator


@contextlib.contextmanager
def log_function_execution_time() -> Generator[None, None, None]:
    """Context manager to time code execution."""
    start_time = time.time()
    yield
    end_time = time.time()
    duration = end_time - start_time
    print(f"Execution time: {round(duration, 2)} seconds")


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
        duration = end_time - self._start_time
        print(f"Execution time: {round(duration, 2)} seconds")
