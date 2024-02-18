"""Test module for testing the log function exection time function and class."""

import time

import pytest

from learning_play_ground.clean_code.timer import (
    log_function_execution_time,
    LogFunctionExecutionTime,
)


def sample_function() -> None:
    """Perform a sample computation. This function is for testing purposes."""
    [num * 2 for num in range(100000)]  # pylint: disable=W0106


def test_log_function_execution_time_func(capsys: pytest.CaptureFixture) -> None:
    """
    Test the log_function_execution_time context manager for a function.

    Parameters
    ----------
    capsys : pytest.CaptureFixture
        Pytest fixture to capture stdout and stderr.
    """
    with log_function_execution_time():
        start_time = time.time()
        sample_function()
        end_time = time.time()

    actual_output = capsys.readouterr().out
    expected_output = f"Execution time: {round(end_time - start_time, 2)} seconds\n"
    assert actual_output == expected_output


def test_log_function_execution_time_cls(capsys: pytest.CaptureFixture) -> None:
    """
    Test the LogFunctionExecutionTime context manager for a class.

    Parameters
    ----------
    capsys : pytest.CaptureFixture
        Pytest fixture to capture stdout and stderr.
    """
    with LogFunctionExecutionTime():
        start_time = time.time()
        sample_function()
        end_time = time.time()

    actual_output = capsys.readouterr().out
    expected_output = f"Execution time: {round(end_time - start_time, 2)} seconds"
    assert expected_output in actual_output
