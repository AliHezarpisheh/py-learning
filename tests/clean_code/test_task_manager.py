"""Test module for testing the TaskManager class."""

from datetime import datetime

import pytest

from src.clean_code.idioms.task_manager import Task, TaskManager


@pytest.fixture(name="task1", scope="module")
def task1_fixture() -> Task:
    """
    Fixture for creating Task 1.

    Returns
    -------
    Task
        An instance of the Task class.
    """
    return Task(
        title="Complete Project",
        description="Finish the coding and documentation for the project",
        due_date=datetime(2024, 2, 28),
        priority=2,
        status=False,
    )


@pytest.fixture(name="task2", scope="module")
def task2_fixture() -> Task:
    """
    Fixture for creating Task 2.

    Returns
    -------
    Task
        An instance of the Task class.
    """
    return Task(
        title="Meeting Preparation",
        description="Prepare agenda and materials for the team meeting",
        due_date=datetime(2024, 3, 10),
        priority=1,
        status=True,
    )


@pytest.fixture(name="task_manager", scope="module")
def task_manager_fixture(task1: Task, task2: Task) -> TaskManager:
    """
    Fixture for creating a TaskManager instance with Task 1 and Task 2.

    Parameters
    ----------
    task1 : Task
        The first task.
    task2 : Task
        The second task.

    Returns
    -------
    TaskManager
        An instance of the TaskManager class.
    """
    return TaskManager(task1, task2)


def test_task_manager_indexing(
    task_manager: TaskManager, task1: Task, task2: Task
) -> None:
    """
    Test indexing operations on TaskManager.

    Parameters
    ----------
    task_manager : TaskManager
        The TaskManager instance to test.
    task1 : Task
        The first task.
    task2 : Task
        The second task.

    Returns
    -------
    None
    """
    assert len(task_manager) == 2

    assert task_manager[0] == task1
    assert task_manager[1] == task2
    assert task_manager[-1] == task2


def test_task_manager_slicing(
    task_manager: TaskManager,
    task1: Task,
    task2: Task,
) -> None:
    """
    Test slicing operations on TaskManager.

    Parameters
    ----------
    task_manager : TaskManager
        The TaskManager instance to test.
    task1 : Task
        The first task.
    task2 : Task
        The second task.

    Returns
    -------
    None
    """
    assert task_manager[:1] == [task1]
    assert task_manager[1:] == [task2]
    assert task_manager[:] == [task1, task2]


def test_task_manager_invalid_indexing_and_slicing(
    task_manager: TaskManager,
) -> None:
    """
    Test invalid indexing and slicing operations on TaskManager.

    Parameters
    ----------
    task_manager : TaskManager
        The TaskManager instance to test.

    Returns
    -------
    None
    """
    with pytest.raises(
        TypeError, match="TaskManager indices must be `integers` or `slices`"
    ):
        task_manager["test"]  # type: ignore  # pylint: disable=W0104

    with pytest.raises(
        TypeError, match="TaskManager indices must be `integers` or `slices`"
    ):
        task_manager[1.10]  # type: ignore  # pylint: disable=W0104


def test_task_manager_iterating(
    task_manager: TaskManager,
    task1: Task,
    task2: Task,
) -> None:
    """
    Test iteration over TaskManager.

    Parameters
    ----------
    task_manager : TaskManager
        The TaskManager instance to test.
    task1 : Task
        The first task.
    task2 : Task
        The second task.

    Returns
    -------
    None
    """
    assert len(task_manager) == 2

    task_manager_iterator = iter(task_manager)
    assert task1 == next(task_manager_iterator)
    assert task2 == next(task_manager_iterator)

    with pytest.raises(StopIteration, match="End of iteration"):
        next(task_manager_iterator)


def test_task_manager_contains(
    task_manager: TaskManager,
    task1: Task,
    task2: Task,
) -> None:
    """
    Test the 'in' operator on TaskManager.

    Parameters
    ----------
    task_manager : TaskManager
        The TaskManager instance to test.
    task1 : Task
        The first task.
    task2 : Task
        The second task.

    Returns
    -------
    None
    """
    assert task1 in task_manager
    assert task2 in task_manager
    assert "test" not in task_manager
