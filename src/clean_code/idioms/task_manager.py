"""Module for managing tasks."""

from collections import namedtuple
from collections.abc import Sequence
from typing import Iterator, Union


Task = namedtuple(
    "Task", "title description due_date priority status", defaults=[False]
)


class TaskManager(Sequence):
    """A class representing a manager for tasks."""

    def __init__(self, *tasks: Task) -> None:
        """Initialize the TaskManager with the given tasks."""
        self._tasks = list(tasks)

    def __getitem__(self, key: Union[int, slice]) -> Union[Task, list[Task]]:
        """
        Get a task or a list of tasks based on the provided key (index or slice).

        Parameters
        ----------
        key : int or slice
            Index or slice to retrieve tasks.

        Returns
        -------
        Union[Task, list[Task]]
            Task or list of tasks based on the provided key.

        Raises
        ------
        TypeError
            If the index is not an integer or a slice.
        """
        if isinstance(key, int):
            return self._tasks[key]
        if isinstance(key, slice):
            return self._tasks[key]

        raise TypeError(
            f"TaskManager indices must be `integers` or `slices`, not `{type(key)}`"
        )

    def __len__(self) -> int:
        """
        Get the number of tasks in the TaskManager.

        Returns
        -------
        int
            Number of tasks in the TaskManager.
        """
        return len(self._tasks)

    def __iter__(self) -> Iterator:
        """
        Initialize the iterator for iterating over tasks.

        Returns
        -------
        Iterator
            Iterator for tasks.
        """
        self._index = 0
        return self

    def __next__(self) -> Task:
        """
        Get the next task during iteration.

        Returns
        -------
        Task
            Next task in the iteration.

        Raises
        ------
        StopIteration
            If the end of the iteration is reached.
        """
        if self._index < len(self._tasks):
            task = self._tasks[self._index]
            self._index += 1
            return task

        raise StopIteration("End of iteration")

    def __contains__(self, value: object) -> bool:
        """
        Check if a specific task is contained in the TaskManager.

        Parameters
        ----------
        value : object
            Task to check for existence.

        Returns
        -------
        bool
            True if the task is in the TaskManager, False otherwise.
        """
        return value in self._tasks
